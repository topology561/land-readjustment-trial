# -*- coding: utf-8 -*-
"""W-G.9-372 量測器（發單側窗七十四擬·檔 F26·⛔ 由受單側改一字）：弱弱聯合之形之盤點（`K-9-57` ③④⑤·`K-9-64`·`K-9-65`）——
本案之調配之輸入（規格步 4 乙之前·以 F24 之 `_pipeline` 求之）中，同街廓同地主（同歸戶）之未在原位配地之建地片
（負擔屬性 ＝ 可建築土地，且類 ＝ 建築街廓內不能分配、或所屬單元以「段三併入」起首），依入池閘之相連之式
（`app.py` 之 `k929_6_fixpoint`：重劃前之片之 `polygon_coords` 經 `buffer(0)`、`k6_shares_segment`·`K-6 §一`·`K-9-54`）
求其相連分量；分量二以上、而該地主於該街廓無原位次配地之片者 ＝「中隔他人」之形（弱弱聯合之受詞之必要條件）。
窗七十二、七十三之倉外器（`probe_ww.py`／`ww_group.py`·相連以精確交集之長 ＞ `1e-3`）之入倉之改寫；相連改取程式之式。

子命令（一律 python verify/probes/probe_WG9372_ww.py <子命令> …）：
  selftest <repo>
           合成對照（⛔ 讀本案資料·`harvest(app.py)` 唯取 `k6_shares_segment`）：K1〜K9 ＝ 各支（期值出自本器·⛔ 呼叫受測碼
           求期）；P0 ＝ 判式自驗（逐項擾動其期須恰該項紅）。
  run      <repo> [<退縮> …]
           harness 實跑本案（預設退縮 `3.5`、`0.0`）：R1「中隔他人」之組 ＝ 本器所載（空）；R2 二片以上之組（街廓·歸戶·
           相連分量·同街廓原位次配地之片）＝ 本器所載；R3 受盤之組數與片數 ＝ 本器所載。
rc：0 相符／1 不符／2 用法錯／3 無從判定（執行中止·⛔ 等同相符）。
"""
import collections, contextlib, io, os, sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:  # noqa: BLE001
    pass

CAND_CLASS = "建築街廓內不能分配"
CAND_UNIT = "段三併入"
ALLOC_CLASS = "原位次配地"
BUILD_ATTR = "可建築土地"


def _harvest(repo):
    sys.path.insert(0, os.path.join(repo, "verify"))
    from app_harvest import harvest
    with contextlib.redirect_stdout(io.StringIO()):
        ns, fake_st = harvest(os.path.join(repo, "app.py"))
    return ns, fake_st


def groups(slices, temp, shares):
    """回 {(街廓, 歸戶): (相連分量〔各為排序之片之元組〕之排序元組, 同街廓原位次配地之片之排序元組, 中隔他人)}。"""
    from shapely.geometry import Polygon
    poly = {str(t["暫編地號"]): t["polygon_coords"] for t in temp}
    cand, alloc = collections.defaultdict(list), collections.defaultdict(list)
    for s in slices:
        if s.get("負擔屬性") != BUILD_ATTR:
            continue
        k, u = (s["所屬街廓"], s["歸戶"]), str(s.get("所屬單元") or "")
        if s.get("類") == CAND_CLASS or u.startswith(CAND_UNIT):
            cand[k].append(str(s["暫編地號"]))
        elif s.get("類") == ALLOC_CLASS:
            alloc[k].append(str(s["暫編地號"]))
    out = {}
    for k, ids in cand.items():
        ids = sorted(set(ids))
        g = {i: Polygon(poly[i]).buffer(0) for i in ids}
        comp, seen = [], set()
        for i in ids:
            if i in seen:
                continue
            c, st = {i}, [i]
            while st:
                x = st.pop()
                for y in ids:
                    if y not in c and shares(g[x], g[y])[0]:
                        c.add(y)
                        st.append(y)
            seen |= c
            comp.append(tuple(sorted(c)))
        al = tuple(sorted(alloc.get(k, ())))
        out[k] = (tuple(sorted(comp)), al, len(comp) >= 2 and not al)
    return out


# ── selftest：合成對照 ──
def _sq(x0, x1, y0=0.0, y1=10.0):
    return [[x0, y0], [x1, y0], [x1, y1], [x0, y1], [x0, y0]]


def _toy(rows):
    sl, tp = [], []
    for pid, blk, own, attr, cls, unit, coords in rows:
        sl.append({"暫編地號": pid, "所屬街廓": blk, "歸戶": own, "負擔屬性": attr, "類": cls, "所屬單元": unit})
        tp.append({"暫編地號": pid, "polygon_coords": coords})
    return sl, tp


_B, _N, _O = BUILD_ATTR, CAND_CLASS, ALLOC_CLASS
TOYS = {
    "K1 相連（同街廓同歸戶二片共用界線）⇒ 一分量": [
        ("a1", "甲", "P", _B, _N, "", _sq(0, 10)), ("a2", "甲", "P", _B, _N, "", _sq(10, 20))],
    "K2 中隔他人（地主於該街廓無原位次配地）⇒ 二分量·中隔他人": [
        ("a1", "甲", "P", _B, _N, "", _sq(0, 10)), ("b1", "甲", "Q", _B, _O, "", _sq(10, 20)),
        ("a3", "甲", "P", _B, _N, "", _sq(20, 30))],
    "K3 中隔他人而地主於該街廓有原位次配地（K-9-57 ④）⇒ 非中隔他人": [
        ("a1", "甲", "P", _B, _N, "", _sq(0, 10)), ("b1", "甲", "Q", _B, _O, "", _sq(10, 20)),
        ("a3", "甲", "P", _B, _N, "", _sq(20, 30)), ("a4", "甲", "P", _B, _O, "", _sq(40, 50))],
    "K4 所屬單元以「段三併入」起首者入盤 ⇒ 二分量·中隔他人": [
        ("a1", "甲", "P", _B, _N, "", _sq(0, 10)), ("b1", "甲", "Q", _B, _O, "", _sq(10, 20)),
        ("a3", "甲", "P", _B, _O, "段三併入 Z", _sq(20, 30))],
    "K5 非建地之片⛔ 入盤": [
        ("a1", "甲", "P", _B, _N, "", _sq(0, 10)), ("b1", "甲", "Q", _B, _O, "", _sq(10, 20)),
        ("a3", "甲", "P", "共同負擔用地", _N, "", _sq(20, 30))],
    "K6 異街廓各自成組": [
        ("a1", "甲", "P", _B, _N, "", _sq(0, 10)), ("a3", "乙", "P", _B, _N, "", _sq(20, 30))],
    "K7 單點相接⛔ 相連 ⇒ 二分量·中隔他人": [
        ("a1", "甲", "P", _B, _N, "", _sq(0, 10)), ("a2", "甲", "P", _B, _N, "", _sq(10, 20, 10, 20))],
    "K8 座標相差 0.05 mm 之界線視為共用（K-9-54）⇒ 一分量": [
        ("a1", "甲", "P", _B, _N, "", _sq(0, 10)), ("a2", "甲", "P", _B, _N, "", _sq(10.00005, 20))],
    "K9 異歸戶⛔ 相併": [
        ("a1", "甲", "P", _B, _N, "", _sq(0, 10)), ("c1", "甲", "Q", _B, _N, "", _sq(10, 20))],
}
SELF_EXPECT = {
    "K1": {("甲", "P"): ((("a1", "a2"),), (), False)},
    "K2": {("甲", "P"): ((("a1",), ("a3",)), (), True)},
    "K3": {("甲", "P"): ((("a1",), ("a3",)), ("a4",), False)},
    "K4": {("甲", "P"): ((("a1",), ("a3",)), (), True)},
    "K5": {("甲", "P"): ((("a1",),), (), False)},
    "K6": {("甲", "P"): ((("a1",),), (), False), ("乙", "P"): ((("a3",),), (), False)},
    "K7": {("甲", "P"): ((("a1",), ("a2",)), (), True)},
    "K8": {("甲", "P"): ((("a1", "a2"),), (), False)},
    "K9": {("甲", "P"): ((("a1",),), (), False), ("甲", "Q"): ((("c1",),), (), False)},
}


def _self_cases(shares):
    out = []
    for name, rows in TOYS.items():
        sl, tp = _toy(rows)
        out.append((name, groups(sl, tp, shares), SELF_EXPECT[name.split()[0]]))
    return out


def selftest(repo):
    ns, _ = _harvest(repo)
    shares = ns.get("k6_shares_segment")
    if shares is None:
        print("🔴 harvest 無 k6_shares_segment ⇒ 無從判定；rc 3")
        return 3
    cases = _self_cases(shares)
    red = []
    for name, got, exp in cases:
        ok = got == exp
        print(("  ✅ " if ok else "  🔴 ") + name + ("" if ok else f"（得 {got}；期 {exp}）"))
        if not ok:
            red.append(name.split()[0])
    base = set(red)
    n_ok = 0
    for i in range(len(cases)):
        code = cases[i][0].split()[0]
        r = {cases[j][0].split()[0] for j in range(len(cases))
             if cases[j][1] != ("⟨擾動⟩" if j == i else cases[j][2])}
        n_ok += int((r - base) == {code} or (code in base and r == base))
    p0 = n_ok == len(cases)
    print(("  ✅ " if p0 else "  🔴 ") + f"P0 判式自驗（逐項擾動其期須恰該項紅）：{n_ok}／{len(cases)}")
    if not p0:
        red.append("P0")
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


# ── run：本案（harness）──
# 二片以上之組：{(街廓, 歸戶): (相連分量, 同街廓原位次配地之片)}；中隔他人之組：恆空
R2_EXPECT = {
    3.5: {("R3", "G014"): ((("628-28(1)", "628-29(1)"),), ()),
          ("R5", "G007"): ((("628-20(2)", "628-30(1)"),), ("628-45(1)",)),
          ("R6", "G009"): ((("628(2)", "628-1(2)"),), ())},
    0.0: {("R3", "G014"): ((("628-28(1)", "628-29(1)"),), ()),
          ("R6", "G009"): ((("628(2)", "628-1(2)"),), ())},
}
# 受盤之（組數, 片數）
R3_EXPECT = {3.5: (23, 26), 0.0: (21, 23)}


def run(repo, sbs):
    os.chdir(repo)
    ns, fst = _harvest(repo)
    sys.path.insert(0, os.path.join(repo, "verify", "probes"))
    import probe_WG9367_adj4 as F24
    import run_verification as rv
    import selection_pipeline as sp
    shares = ns.get("k6_shares_segment")
    if shares is None:
        print("🔴 harvest 無 k6_shares_segment ⇒ 無從判定；rc 3")
        return 3
    red = []
    for sb in sbs:
        try:
            _, _, it, temp = F24._pipeline(ns, fst, rv, sp, sb)
        except Exception as e:  # noqa: BLE001
            print(f"🔴 退縮 {sb}：harness 中止（{type(e).__name__}: {str(e)[:160]}）⇒ 無從判定；rc 3")
            return 3
        gr = groups(it["slices"], temp, shares)
        star = sorted(k for k, v in gr.items() if v[2])
        multi = {k: (v[0], v[1]) for k, v in gr.items() if sum(len(c) for c in v[0]) >= 2}
        cnt = (len(gr), sum(sum(len(c) for c in v[0]) for v in gr.values()))
        print(f"── 退縮 {sb} ──")
        for k, v in sorted(gr.items()):
            print(f"     {k} 相連分量 {list(v[0])} 同街廓原位次配地 {list(v[1])}" + (" ★中隔他人" if v[2] else ""))
        for nm, got, exp in ((f"R1 {sb}「中隔他人」之組", star, []),
                             (f"R2 {sb} 二片以上之組", multi, R2_EXPECT.get(sb)),
                             (f"R3 {sb} 受盤之（組數, 片數）", cnt, R3_EXPECT.get(sb))):
            ok = got == exp
            print(("  ✅ " if ok else "  🔴 ") + nm + ("" if ok else f"（得 {got}；期 {exp}）"))
            if not ok:
                red.append(nm.split()[0] + "@" + str(sb))
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


def main(argv):
    if len(argv) >= 3 and argv[1] == "selftest":
        return selftest(os.path.abspath(argv[2]))
    if len(argv) >= 3 and argv[1] == "run":
        try:
            sbs = [float(x) for x in argv[3:]] or [3.5, 0.0]
        except ValueError:
            print(__doc__)
            return 2
        return run(os.path.abspath(argv[2]), sbs)
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
