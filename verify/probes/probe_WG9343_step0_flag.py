# -*- coding: utf-8 -*-
r"""`W-G.9-343`：`K-9-29 二`（廢前置合併）之旗標量測器（⛔ 零生產碼）。

案由：`app.py` `k6_step0_enabled()` 之預設由 `on` 改為 `off`（`K-9-29 二` 之碼側落地·旗標翻轉、⛔ 刪碼）。
      既有之 `verify/probes/wg9309/chk_wg9309.py` 只有二態（`甲` ＝ 旗標未設·`乙` ＝ `off`），⛔ 能驅動 `on`；
      改後「未設」即 `off` ⇒ 須三值（`unset`／`on`／`off`）方能證「`on` 逐位復現改前之預設」。
      既有之 `verify/probes/probe_WG9272_step0_ab.py` 經 `CLAUDE.md` 之失效註（態 `b4a6f5a` 只錄 `R1` 五宗、`rc 6`）⛔ 據以實算。

五子命令（逐項三值出艙）：
  run   <repo> <unset|on|off> <0.0|3.5> <out.json>
        以 `runpy` 執行 `chk_wg9309.py`（態引數 `甲`），於其 `harvest()` 之後、建宗地之前設定旗標；
        出艙 ＝ `chk_wg9309.py` 之 json ＋ `flag`／`step0_ran`（`f3_k6_step0_diag` 是否寫入）／`step0_diag`／`own`（原地號 → 歸戶）。
        rc ＝ 0；`err` 非空 ⇒ rc 1；地主宗 `0` ⇒ rc 90（器紅）。
  cmp   <A.json> <B.json>
        比 `err`／`forced`／`rows`（逐列逐欄·含 `cut_coords`·依原序）／`gates` 四鍵。rc ＝ 相異項數（上限 `89`）；二份任一無地主宗 ⇒ rc 90。
  table <A.json（合併·step0_ran 真）> <B.json（未合併·step0_ran 偽）>
        出艙：逐街廓之強制抵費地、抵費地片、合併組之改前改後、他宗 |ΔG| > 0.005 或狀態變者、合計。
        性質閘（rc ＝ 破者數）：
          t1  B 之暫編地號以 `+` 結尾者 ＝ 0；A 以 `+` 結尾者 ＝ A 之合併組數。
          t2  A 之每一合併組，其成員於 B 皆存在（地主列 ∪ 剔出列）。
          t3  非合併組成員之地主宗，A、B 之集合同。
          t4  B 之每一街廓：地主宗兩兩不重疊（`own_own_overlap` 空）且列之聯集 ≡ 街廓（對稱差 ≤ 0.001 ㎡）。
        器紅（rc 90）：A 之 `step0_ran` 非真、或 B 之 `step0_ran` 非偽、或二份退縮不同。
  runall <before.log> <after.log>
        二份 `python verify/run_all.py` 之全文出艙逐項對拍：名目列 ＝ 行首二空白後接 `✅ PASS` 或 `🔴 FAIL` 再二空白者；
        違規數 ＝ 該項之「本閘違規總計」之數，無該列者 ＝ 該項名目列之下、次一名目列之前，去前導空白後以 `[` 起首之列數；
        本體 ＝ 名目列之下、次一名目列（或含「【對帳】」之列）之前之各列；比對前將 traceback 之 `File "<任意>/verify/…"` 正規化為 `File "<R>/verify/…"`（路徑分隔一律 `/`）。
        末端夾具列 ＝ 含「末端夾具」或「夾具 FAIL」或「golden」之列（去首尾空白、併連續空白）。
        出艙：項數與 PASS 數；名目、狀態、違規數、本體任一相異之項（逐項·本體只出「同／異」、⛔ 出相異列數——traceback 之列數隨直譯器版本而異）；末端夾具列相異數；對帳段之名目數；二份之末列。
        rc ＝ 0；二份項數不同或任一份 `0` 項 ⇒ rc 90（器紅）。
  selftest <A.json> <B.json>
        判別力：對 B 施四種單點突變（名加 `+`／刪一成員列／增一人造非成員列／某街廓對稱差設 `1.0`），
        t1〜t4 須各自轉紅。rc ＝ 未轉紅之突變數（原樣未皆過者另加 `100`）。
"""
import json, os, runpy, sys
from collections import defaultdict
sys.stdout.reconfigure(encoding="utf-8")
ENV = "WV_K6_STEP0"          # ＝ `app.py` 之 `K6_STEP0_ENV`（逐字）
KEYS = ("err", "forced", "rows", "gates")


def _run(repo, flag, sb, out):
    if flag not in ("unset", "on", "off"):
        print("🔴 旗標須為 unset／on／off"); return 90
    sys.path.insert(0, os.path.join(repo, "verify")); sys.path.insert(0, os.path.join(repo, "verify", "probes"))
    import app_harvest
    _orig = app_harvest.harvest

    def _harvest(*a, **k):
        r = _orig(*a, **k)
        if flag == "unset":
            os.environ.pop(ENV, None)
        else:
            os.environ[ENV] = flag
        return r
    app_harvest.harvest = _harvest
    sys.argv = ["chk_wg9309.py", repo, "甲", sb, out]
    g = runpy.run_path(os.path.join(repo, "verify", "probes", "wg9309", "chk_wg9309.py"), run_name="__main__")
    ss = g["fake_st"].session_state
    diag = ss.get("f3_k6_step0_diag")
    d = json.load(open(out, encoding="utf-8"))
    d["flag"] = flag
    d["step0_ran"] = diag is not None
    d["step0_diag"] = diag
    d["own"] = dict(ss.get("t8_ownership_map", {}) or {})
    json.dump(d, open(out, "w", encoding="utf-8"), ensure_ascii=False, default=str)
    n_own = sum(1 for r in d["rows"] if r.get("推進側別") != "抵費地")
    n_plus = sum(1 for r in d["rows"] if str(r.get("暫編地號", "")).endswith("+"))
    print("【run】旗標 %s·退縮 %s·err %s·列 %d·地主宗 %d·名以 + 結尾 %d·步驟 0 執行 %s·合併組 %s"
          % (flag, sb, d.get("err"), len(d["rows"]), n_own, n_plus, d["step0_ran"],
             (len(diag.get("merged", [])) if diag else 0)))
    if n_own == 0:
        print("🔴 器紅：地主宗 0"); return 90
    return 1 if d.get("err") else 0


def _load(p):
    return json.load(open(p, encoding="utf-8"))


def _cmp(pa, pb):
    A, B = _load(pa), _load(pb)
    for nm, D in (("A", A), ("B", B)):
        if not any(r.get("推進側別") != "抵費地" for r in D.get("rows", [])):
            print("🔴 器紅：%s 無地主宗" % nm); return 90
    diffs = []
    for k in ("err", "forced", "gates"):
        if json.dumps(A.get(k), sort_keys=True, ensure_ascii=False) != json.dumps(B.get(k), sort_keys=True, ensure_ascii=False):
            diffs.append("鍵 %s 相異" % k)
    ra, rb = A.get("rows", []), B.get("rows", [])
    if len(ra) != len(rb):
        diffs.append("列數 %d ≠ %d" % (len(ra), len(rb)))
    for i, (x, y) in enumerate(zip(ra, rb)):
        if json.dumps(x, sort_keys=True, ensure_ascii=False) != json.dumps(y, sort_keys=True, ensure_ascii=False):
            ks = sorted(set(x) | set(y), key=str)
            fk = [k for k in ks if json.dumps(x.get(k), ensure_ascii=False) != json.dumps(y.get(k), ensure_ascii=False)]
            diffs.append("列 %d（%s／%s）相異欄 %s" % (i, x.get("所屬街廓"), x.get("暫編地號"), fk[:6]))
    print("【cmp】%s ↔ %s：列 %d／%d·相異項 %d" % (os.path.basename(pa), os.path.basename(pb), len(ra), len(rb), len(diffs)))
    for s in diffs[:12]:
        print("   ", s)
    return min(len(diffs), 89)


def _corner(r):
    return ("街角" + ("左" if r.get("街角側別") == "左側" else "右")) if r.get("第1筆街角") == "是" else ""


def _st(r):
    return {"保留": "合格", "剔除": "未達"}.get(r.get("驗_總判"), "?")


def _table(pa, pb):
    A, B = _load(pa), _load(pb)
    if not A.get("step0_ran") or B.get("step0_ran") or A.get("sb") != B.get("sb"):
        print("🔴 器紅：A 須為步驟 0 已執行、B 須為未執行、退縮須同"); return 90
    return len(_tab(A, B, os.path.basename(pa), os.path.basename(pb), True))


def _tab(A, B, na_, nb_, verbose):
    diag, own = A["step0_diag"], A.get("own", {})
    groups = {m["命名"]: m for m in diag.get("merged", [])}
    members = {x for m in diag.get("merged", []) for x in m["成員"]}
    dropA = {x["暫編地號"]: x for v in A["gates"]["dropped"].values() for x in v}
    dropB = {x["暫編地號"]: x for v in B["gates"]["dropped"].values() for x in v}
    oa = {r["暫編地號"]: r for r in A["rows"] if r["推進側別"] != "抵費地"}
    ob = {r["暫編地號"]: r for r in B["rows"] if r["推進側別"] != "抵費地"}
    bad = []
    nplusA = sum(1 for k in oa if k.endswith("+")); nplusB = sum(1 for k in ob if k.endswith("+"))
    bad += [] if (nplusB == 0 and nplusA == len(groups)) else ["t1（A 之 + 名 %d·組 %d·B 之 + 名 %d）" % (nplusA, len(groups), nplusB)]
    miss = [x for x in members if x not in ob and x not in dropB]
    bad += [] if not miss else ["t2（成員缺 %s）" % miss]
    na = {k for k in oa if k not in groups} | {k for k in dropA}
    nb = {k for k in ob if k not in members} | {k for k in dropB if k not in members}
    bad += [] if na == nb else ["t3（A 有 B 無 %s·B 有 A 無 %s）" % (sorted(na - nb), sorted(nb - na))]
    for blk, bg in B["gates"]["blocks"].items():
        if bg.get("own_own_overlap") or (bg.get("union_symdiff_block") or 0) > 0.001:
            bad.append("t4（%s 重疊 %s·對稱差 %s）" % (blk, bg.get("own_own_overlap"), bg.get("union_symdiff_block")))
    if not verbose:
        return bad
    print("【table】退縮 %s m·A ＝ %s（合併組 %d·吸收 %d 宗）→ B ＝ %s"
          % (A["sb"], na_, len(groups), diag.get("parcels_absorbed", -1), nb_))
    blocks = sorted({r["所屬街廓"] for r in A["rows"]})
    for blk in blocks:
        fa = {s: A["forced"][blk][s + "_corner_min_area"] for s in ("left", "right") if A["forced"].get(blk, {}).get(s + "_forced_offset")}
        fb = {s: B["forced"][blk][s + "_corner_min_area"] for s in ("left", "right") if B["forced"].get(blk, {}).get(s + "_forced_offset")}
        pa_ = [round(float(r["幾何面積(㎡)"]), 2) for r in A["rows"] if r["所屬街廓"] == blk and r["推進側別"] == "抵費地"]
        pb_ = [round(float(r["幾何面積(㎡)"]), 2) for r in B["rows"] if r["所屬街廓"] == blk and r["推進側別"] == "抵費地"]
        print("  ── %s　強制抵費地 改前 %s → 改後 %s｜抵費地片 改前 %s（計 %.2f）→ 改後 %s（計 %.2f）"
              % (blk, fa, fb, pa_, sum(pa_), pb_, sum(pb_)))
        for k, r in sorted(oa.items()):
            if r["所屬街廓"] != blk:
                continue
            if k in groups:
                aft = []
                for m in groups[k]["成員"]:
                    if m in ob:
                        aft.append("%s %s%s %s" % (m, ob[m]["G(㎡)"], (" " + _corner(ob[m])) if _corner(ob[m]) else "", _st(ob[m])))
                    elif m in dropB:
                        aft.append("%s 剔出（G %s）" % (m, dropB[m]["G(㎡)"]))
                print("     合併 %s〔%s〕 %s%s %s ⇒ %s" % (k, own.get(r["原地號"]), r["G(㎡)"],
                                                    (" " + _corner(r)) if _corner(r) else "", _st(r), "；".join(aft)))
            elif k in ob:
                b = ob[k]; dg = round(float(b["G(㎡)"]) - float(r["G(㎡)"]), 2)
                if abs(dg) > 0.005 or _corner(b) != _corner(r) or _st(b) != _st(r):
                    print("     他宗 %s〔%s〕 %s%s %s ⇒ %s%s %s（ΔG %+.2f）" % (k, own.get(r["原地號"]), r["G(㎡)"],
                          (" " + _corner(r)) if _corner(r) else "", _st(r), b["G(㎡)"],
                          (" " + _corner(b)) if _corner(b) else "", _st(b), dg))
    for nm, D, O in (("改前", A, oa), ("改後", B, ob)):
        g_own = sum(float(r["幾何面積(㎡)"]) for r in D["rows"] if r["推進側別"] != "抵費地")
        g_pool = sum(float(r["幾何面積(㎡)"]) for r in D["rows"] if r["推進側別"] == "抵費地")
        n_bad = sum(1 for r in O.values() if r.get("驗_總判") == "剔除")
        drop = {x["暫編地號"]: x["G(㎡)"] for v in D["gates"]["dropped"].values() for x in v}
        print("  〔%s〕地主宗 %d（未達 %d）·地主幾何面積 %.2f·抵費地 %.2f·剔出 %s" % (nm, len(O), n_bad, g_own, g_pool, drop))
    print("  性質閘 t1〜t4：%s" % ("🟢 皆過" if not bad else "🔴 破 " + "；".join(bad)))
    return bad


def _selftest(pa, pb):
    """判別力：對 B 施四種單點突變，t1〜t4 須各自轉紅（⛔ 器恆綠）。rc ＝ 未轉紅之突變數；原樣須皆過。"""
    import copy
    A, B = _load(pa), _load(pb)
    if not A.get("step0_ran") or B.get("step0_ran") or A.get("sb") != B.get("sb"):
        print("🔴 器紅：A 須為步驟 0 已執行、B 須為未執行、退縮須同"); return 90
    base = _tab(A, B, "", "", False)
    print("【selftest】原樣：%s" % ("🟢 皆過" if not base else "🔴 " + "；".join(base)))
    mem = [x for m in A["step0_diag"]["merged"] for x in m["成員"]]
    own_idx = [i for i, r in enumerate(B["rows"]) if r["推進側別"] != "抵費地"]
    mi = [i for i in own_idx if B["rows"][i]["暫編地號"] in mem][0]
    nm = [i for i in own_idx if B["rows"][i]["暫編地號"] not in mem][0]
    blk0 = sorted(B["gates"]["blocks"])[0]

    def m1(D): D["rows"][nm]["暫編地號"] = D["rows"][nm]["暫編地號"] + "+"
    def m2(D): del D["rows"][mi]
    def m3(D):
        r = copy.deepcopy(D["rows"][nm]); r["暫編地號"] = "人造-9999(9)"; D["rows"].append(r)
    def m4(D): D["gates"]["blocks"][blk0]["union_symdiff_block"] = 1.0
    miss = 0
    for tag, f in (("t1", m1), ("t2", m2), ("t3", m3), ("t4", m4)):
        D = copy.deepcopy(B); f(D)
        got = _tab(A, D, "", "", False)
        hit = any(x.startswith(tag) for x in got)
        print("  %s 突變 %s ⇒ %s" % ("✅" if hit else "🔴", tag, got if got else "皆過（未轉紅）"))
        miss += 0 if hit else 1
    return (miss + (100 if base else 0))


def _ra_parse(p):
    import re
    L = open(p, encoding="utf-8", errors="replace").read().splitlines()
    items, cur, rec = [], None, []
    for l in L:
        if "【對帳】" in l:
            cur = None
        if cur is None and items and ("【對帳】" in l or rec):
            rec.append(l)
        m = re.match(r"^\s{2}(✅ PASS|🔴 FAIL)\s{2}(.*)$", l)
        if m:
            cur = {"st": m.group(1)[2:], "name": m.group(2).strip(), "body": []}; items.append(cur); continue
        if cur is not None:
            cur["body"].append(re.sub(r'File "[^"]*?[\\/](verify[\\/][^"]*)"',
                                  lambda m: 'File "<R>/' + m.group(1).replace("\\", "/") + '"', l))
    for it in items:
        t = [re.search(r"本閘違規總計[^0-9]*(\d+)", b) for b in it["body"]]
        t = [x.group(1) for x in t if x]
        it["v"] = int(t[0]) if t else sum(1 for b in it["body"] if b.strip().startswith("["))
    fx = [re.sub(r"\s+", " ", l.strip()) for l in L if ("末端夾具" in l or "夾具 FAIL" in l or "golden" in l)]
    nm = [re.search(r"名目：凍存 ?(\d+)／現況 ?(\d+)", l) for l in rec]
    nm = [x.groups() for x in nm if x]
    rc_fail = any("對帳 FAIL" in l for l in rec)
    return L, items, fx, (nm[0] if nm else None, rc_fail)


def _runall(pa, pb):
    La, A, FA, RA = _ra_parse(pa); Lb, B, FB, RB = _ra_parse(pb)
    if not A or not B or len(A) != len(B):
        print("🔴 器紅：項數 %d／%d" % (len(A), len(B))); return 90
    print("【runall】項 %d／%d·PASS %d → %d·FAIL %d → %d" % (len(A), len(B), sum(x["st"] == "PASS" for x in A),
          sum(x["st"] == "PASS" for x in B), sum(x["st"] == "FAIL" for x in A), sum(x["st"] == "FAIL" for x in B)))
    k = 0
    for i, (x, y) in enumerate(zip(A, B), 1):
        nb = sum(1 for p, q in zip(x["body"], y["body"]) if p != q) + abs(len(x["body"]) - len(y["body"]))
        if x["name"] != y["name"] or x["st"] != y["st"] or x["v"] != y["v"] or nb:
            k += 1
            nm = x["name"] if x["name"] == y["name"] else "%s ⇒ 名目改為 %s" % (x["name"], y["name"])
            print("  #%02d %s ｜狀態 %s → %s｜違規數 %d → %d｜本體 %s" % (i, nm, x["st"], y["st"], x["v"], y["v"], "異" if nb else "同"))
    fxd = sum(1 for p, q in zip(FA, FB) if p != q) + abs(len(FA) - len(FB))
    print("  相異項 %d；其餘 %d 項之名目、狀態、違規數與本體逐項同" % (k, len(A) - k))
    print("  末端夾具／golden 列：%d／%d·相異 %d" % (len(FA), len(FB), fxd))
    print("  對帳段（【對帳】起·⛔ 入本體）：名目 凍存／現況 %s → %s；含「對帳 FAIL」%s → %s"
          % ("／".join(RA[0]) if RA[0] else "—", "／".join(RB[0]) if RB[0] else "—", RA[1], RB[1]))
    print("  末列：%s ｜ %s" % (La[-1].strip() if La else "", Lb[-1].strip() if Lb else ""))
    return 0


if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "run" and len(a) == 5:
        sys.exit(_run(a[1], a[2], a[3], a[4]))
    if a and a[0] == "cmp" and len(a) == 3:
        sys.exit(_cmp(a[1], a[2]))
    if a and a[0] == "table" and len(a) == 3:
        sys.exit(_table(a[1], a[2]))
    if a and a[0] == "runall" and len(a) == 3:
        sys.exit(_runall(a[1], a[2]))
    if a and a[0] == "selftest" and len(a) == 3:
        sys.exit(_selftest(a[1], a[2]))
    print(__doc__); sys.exit(2)
