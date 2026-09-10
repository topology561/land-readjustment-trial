# -*- coding: utf-8 -*-
"""W-G.9-267 工項二：`d-1` 閘之**結構盲區**（`SIDE ∥ ALLOC` ⇒ 鑑別力為零）。唯讀探針。

🔒 唯讀：讀 harness 落檔 ＋ **生產解析器**之輸出（`cad['alloc_dir_by_block']`／
   `cad['side_lines_by_side']`）。**⛔ 動 `app.py` 與 `verify/` 生產路徑一字。**

【受詞】`d-1`（`K-9-9 一` ∥ALLOCLINE 之驗）於 `SIDE ∥ ALLOC` 之街廓側上，
  「∥ALLOC」與「∥SIDE」為**同一述詞** ⇒ 該閘於該類**鑑別力為零**
  ——既不能證違反、亦不能證未違反 ⇒ 須標「**不可判**」，⛔ 併入違反計數。

【框之來源（逐項具名·`⛔ 新造`）】
  `∥` 之容差 `0.5°` ＝ **既有 `d-1` 之框**（承 `probe_WG9266_d1_d3.py` 之 `par = d < 0.5`）。
  `SIDE∥ALLOC` 之判 ＝ **同一 `0.5°`**（⇔ `|cross(û_ALLOC, û_SIDE)| < sin(0.5°) = 8.726535e-03`）
  ——🔒 **承既有 `d-1` 之框，⛔ 自擬**：`d-1` 之述詞係「遠側界 ∥ALLOC（容差 `0.5°`）」；
  凡 `|∠SIDE−∠ALLOC| < 0.5°` 者，任一 ∥SIDE 之邊必同時 ∥ALLOC ⇒ 二述詞在**該閘之解析度下**不可分。

🩸 **單所載之 `|cross| < 1e-9` ⛔ 採（`常規二` ＋ `自解款` 白名單 `6`·詳見報告之自解清單）**
  ——實測 `R6/right` 之 `|cross| = 4.74169e-08`，**`> 1e-9`** ⇒ 依該框其判為「可判」，
  與**單自身之必紅**（`§三`：`R6/right` 須輸出「不可判」）**相斥**。二讀法皆⛔ 動土地
  ⇒ 取**較嚴者**（＝ 標更多為「不可判」者）續辦並具名。本探針**二框並列出艙**。

【自我驗證閘（`探針還原內部幾何須設自我驗證閘` 所令）】
  重建之「共有頂點取邊」須復現 `-266R` 之「第 1 宗以後 ∥ALLOCLINE」⇒ 必綠組須全數 ∥ALLOC。
  **閘不過 ⇒ ⛔ 得據以下任何結論。**

【否證對照（同格載判定集基數）】
  必紅 ＝ `3.5m`·`R6`·`right`（`|∠SIDE−∠ALLOC| ≈ 2.7e-06°`）⇒ 須輸出「不可判」（基數 1）。
  必綠 ＝ `3.5m`·`R1`·`right`（`0.6908°`）⇒ 須輸出「可判·且遠側界取 SIDE」（基數 1）。
  基數 `0` ⇒ **loud 拒測**，⛔ 計為通過。
"""
import ast
import csv
import io
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
OUT = os.path.join(REPO, "verify", "out")
SCEN = [("0m", "got_G值_退縮0m_partial.csv"), ("3.5m", "got_G值_退縮3.5m_partial.csv")]
QK = 1e-6
PAR_TOL_DEG = 0.5          # 承 probe_WG9266_d1_d3.py（⛔ 新造）
CROSS_TOL_ORDER = 1e-9     # 🩸 單所載之框（⛔ 採為判準·僅並列出艙以具名其相斥）
CROSS_TOL = math.sin(math.radians(PAR_TOL_DEG))   # ＝ 8.726535e-03（承 d-1 之 0.5°）


def load(fn):
    p = os.path.join(OUT, fn)
    if not os.path.exists(p):
        return None
    with io.open(p, "r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def parse(s):
    if not s or not s.strip():
        return None
    try:
        v = ast.literal_eval(s)
    except Exception:
        return None
    return [(float(a), float(b)) for a, b in v] if v and len(v) >= 3 else None


def ang_of(v):
    return math.degrees(math.atan2(v[1], v[0])) % 180.0


def unit(v):
    n = math.hypot(v[0], v[1])
    return (v[0] / n, v[1] / n)


def sideline_vec(d):
    """自 `cad['side_lines_by_side'][blk][side]` 取方向向量（⛔ 自寫第二份解析）。"""
    if not d:
        return None
    if "p1" in d and "p2" in d:
        p1, p2 = d["p1"], d["p2"]
        return (float(p2[0]) - float(p1[0]), float(p2[1]) - float(p1[1]))
    pts = d.get("pts")
    if pts and len(pts) >= 2:
        return (float(pts[-1][0]) - float(pts[0][0]), float(pts[-1][1]) - float(pts[0][1]))
    return None


def shared_edge(a, b):
    sh = []
    for x in a:
        for y in b:
            if abs(x[0] - y[0]) < QK and abs(x[1] - y[1]) < QK:
                if not any(abs(x[0] - s[0]) < QK and abs(x[1] - s[1]) < QK for s in sh):
                    sh.append(x)
    return sh if len(sh) == 2 else None


def main():
    sys.path.insert(0, os.path.join(REPO, "verify"))
    import run_verification as rv
    from app_harvest import harvest
    ns, fake = harvest()
    snap = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake, snap)

    ALLOC = cad.get("alloc_dir_by_block") or {}
    SIDES = cad.get("side_lines_by_side") or {}

    print("=" * 116)
    print("【W-G.9-267 工項二】`d-1` 閘之結構盲區（`SIDE ∥ ALLOC` ⇒ 鑑別力為零）")
    print("=" * 116)
    print("   來源層：∠ALLOC ＝ 生產解析器 `cad['alloc_dir_by_block']`；"
          "∠SIDE ＝ 生產解析器 `cad['side_lines_by_side']`（＝ `f3_cad_side_lines_by_side` 之同一表）")
    print("   實測遠側界 ＝ harness 落檔 `verify/out/got_G值_退縮*_partial.csv` 之 `cut_coords`（共有頂點取邊）")
    if not ALLOC or not SIDES:
        print("🔴 **阻斷點**：`alloc_dir_by_block` 或 `side_lines_by_side` 查無 ⇒ ⛔ 得下結論")
        return 5

    # ── 一　全母體：全部街廓側之 |∠SIDE − ∠ALLOC| 表（`自誤 330` 之同族全母體檢查）
    print()
    print("── 一　全母體：**全部街廓側**之 `|∠SIDE − ∠ALLOC|`（⛔ 只列受詞·⛔ 只列受詞之近鄰）──")
    print("   框（判準·逐字）＝ `|∠SIDE−∠ALLOC| < %.1f°` ⇔ `|cross| < sin(%.1f°) = %.6e`（承 `d-1`）"
          % (PAR_TOL_DEG, PAR_TOL_DEG, CROSS_TOL))
    print("   框（單所載·⛔ 判準·並列以具名相斥）＝ `|cross| < %g`" % CROSS_TOL_ORDER)
    print("| 街廓/側 | ∠ALLOC | ∠SIDE | `|∠SIDE−∠ALLOC|` | `|cross(û,û)|` | 判（本探針框） | 判（單所載框 `1e-9`） |")
    print("|---|---|---|---|---|---|---|")
    tbl = {}
    for blk in sorted(SIDES):
        al = ALLOC.get(blk)
        if not al:
            continue
        av = (float(al[0]), float(al[1])) if not isinstance(al, dict) else \
             (al["p2"][0] - al["p1"][0], al["p2"][1] - al["p1"][1])
        aa = ang_of(av)
        ua = unit(av)
        for side in sorted(SIDES[blk]):
            sv = sideline_vec(SIDES[blk][side])
            if sv is None:
                continue
            sa = ang_of(sv)
            us = unit(sv)
            d = min(abs(sa - aa), 180.0 - abs(sa - aa))
            cr = abs(ua[0] * us[1] - ua[1] * us[0])
            blind = cr < CROSS_TOL
            blind_ord = cr < CROSS_TOL_ORDER
            tbl[(blk, side)] = dict(aa=aa, sa=sa, d=d, cross=cr, blind=blind, blind_ord=blind_ord)
            print("| %s/%s | %.4f | %.4f | **%.10g°** | %.6g | %s | %s |"
                  % (blk, side, aa, sa, d, cr,
                     "🔴 **SIDE ∥ ALLOC ⇒ 盲區·不可判**" if blind else "✅ 可判",
                     "盲區" if blind_ord else "可判"))
    n_sides = len(tbl)
    blind_set = sorted(k for k, v in tbl.items() if v["blind"])
    blind_ord_set = sorted(k for k, v in tbl.items() if v["blind_ord"])
    print("   母體 ＝ **%d** 個街廓側（判定集基數 %d）；落盲區者〔本探針框〕＝ %s（**%d** 組）"
          % (n_sides, n_sides, blind_set or "無", len(blind_set)))
    print("   🩸 落盲區者〔單所載框 `1e-9`〕＝ %s（**%d** 組）⇒ **與單自身之必紅相斥**"
          % (blind_ord_set or "無", len(blind_ord_set)))
    print("   [判別力·證此檢⛔ 恆判平行] `|cross(û_ALLOC(R6), û_ALLOC(R1))|` = %.6g"
          % abs(unit(ALLOC["R6"])[0] * unit(ALLOC["R1"])[1] - unit(ALLOC["R6"])[1] * unit(ALLOC["R1"])[0])
          if ("R6" in ALLOC and "R1" in ALLOC) else "")

    # ── 二　自我驗證閘：復現 -266R 之「第 1 宗以後 ∥ALLOCLINE」
    print()
    print("── 二　自我驗證閘（重建之「共有頂點取邊」須復現 `-266R` 之必綠組）──")
    corner_rows, rest_par, rest_npar = [], 0, 0
    far_edge = {}     # (tag, blk, side) -> 街角第 0 宗之遠側界角
    for tag, fn in SCEN:
        rows = load(fn)
        if rows is None:
            print("   🔴 落檔不存在：%s ⇒ **loud 拒測**" % fn)
            return 6
        grp = {}
        for r in rows:
            side = (r.get("推進側別") or "").strip()
            if side == "抵費地":
                continue
            lbl = (r.get("所屬街廓") or "").strip()
            cc = parse(r.get("cut_coords"))
            if cc is None:
                continue
            grp.setdefault((lbl, side), []).append((r, cc))
        for (lbl, side), its in grp.items():
            if lbl not in ALLOC:
                continue
            its.sort(key=lambda t: float(t[0].get("累積S(m)") or 0))
            aa = tbl.get((lbl, side), {}).get("aa")
            for i in range(len(its) - 1):
                sh = shared_edge(its[i][1], its[i + 1][1])
                if sh is None:
                    continue
                ea = ang_of((sh[1][0] - sh[0][0], sh[1][1] - sh[0][1]))
                if aa is None:
                    aa2 = ang_of(unit(ALLOC[lbl]))
                else:
                    aa2 = aa
                d = min(abs(ea - aa2), 180.0 - abs(ea - aa2))
                is_corner = (its[i][0].get("第1筆街角") or "").strip() == "是"
                if is_corner:
                    far_edge[(tag, lbl, side)] = (ea, (its[i][0].get("暫編地號") or "").strip())
                    corner_rows.append((tag, lbl, side, (its[i][0].get("暫編地號") or "").strip(), ea, d))
                else:
                    if d < PAR_TOL_DEG:
                        rest_par += 1
                    else:
                        rest_npar += 1
    print("   必綠組（第 1 宗以後）：∥ALLOC **%d** 宗／⛔∥ **%d** 宗（判定集基數 %d）"
          % (rest_par, rest_npar, rest_par + rest_npar))
    gate_ok = (rest_par + rest_npar) > 0 and rest_npar == 0
    print("   ⇒ 自我驗證閘 %s" % ("✅ 過（全數 ∥ALLOC·與 `-266R` 相符）" if gate_ok
                                 else "🔴 **不過 ⇒ ⛔ 得據以下任何結論**"))
    if not gate_ok:
        return 7

    # ── 三　逐街角側之「可判／不可判」判 ＋ 遠側界之歸屬
    print()
    print("── 三　逐街角第 0 宗：遠側界之實測角 vs ∠ALLOC／∠SIDE ⇒ 可判？取何軸？──")
    print("| 情境 | 街廓/側 | 宗地 | 實測∠ | ∠ALLOC | ∠SIDE | 判 |")
    print("|---|---|---|---|---|---|---|")
    verdict = {}
    for (tag, lbl, side, lot, ea, _d) in sorted(corner_rows):
        t = tbl.get((lbl, side))
        if t is None:
            continue
        da = min(abs(ea - t["aa"]), 180.0 - abs(ea - t["aa"]))
        ds = min(abs(ea - t["sa"]), 180.0 - abs(ea - t["sa"]))
        if t["blind"] or (da < PAR_TOL_DEG and ds < PAR_TOL_DEG):
            v = "🔴 **不可判**（`SIDE ∥ ALLOC`·二述詞同一）"
        elif ds < PAR_TOL_DEG and da >= PAR_TOL_DEG:
            v = "✅ **可判·取 SIDE**"
        elif da < PAR_TOL_DEG and ds >= PAR_TOL_DEG:
            v = "✅ 可判·取 ALLOC"
        else:
            v = "⚠️ 可判·二軸皆不符（Δ_ALLOC %.4f°／Δ_SIDE %.4f°）" % (da, ds)
        verdict[(tag, lbl, side)] = v
        print("| %s | %s/%s | %s | %.4f | %.4f | %.4f | %s |"
              % (tag, lbl, side, lot, ea, t["aa"], t["sa"], v))

    # ── 四　否證對照（同格載判定集基數）
    print()
    print("── 四　否證對照（同格載判定集基數·基數 `0` ⇒ loud 拒測）──")
    rc = 0
    for key, must, name in ((("3.5m", "R6", "right"), "不可判", "必紅"),
                            (("3.5m", "R1", "right"), "可判·取 SIDE", "必綠")):
        hit = [k for k in verdict if k == key]
        n = len(hit)
        if n == 0:
            print("   🔴 %s ＝ %s：**判定集基數 0 ⇒ loud 拒測**（⛔ 計為通過）" % (name, key))
            rc = 8
            continue
        got = verdict[key]
        ok = must in got
        print("   %s %s ＝ `%s`　判定集基數 **%d**　實得「%s」⇒ %s"
              % ("✅" if ok else "🔴", name, key, n, got, "如預期" if ok else "**未如預期 ⇒ 器紅**"))
        if not ok:
            rc = 9
    return rc


if __name__ == "__main__":
    sys.exit(main())
