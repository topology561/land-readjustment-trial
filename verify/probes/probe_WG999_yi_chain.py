# -*- coding: utf-8 -*-
r"""`W-G.9-99`：「乙」之**遞補鏈 shim**（⛔ 零生產碼·⛔ 非落地）。

## 受詞

KL 逐字（`docs/reports/W-G.4_泛用阻塞項登記表.md:2371-2372`＠`23a63d3`）：
「先落乙，把最基本的幾何分配位置及方式確定，才做後續甲矩形容納」／
「落地前，先以 shim 量出各自的土地後果」。

`-91` 之 shim 自陳其數「係**第一輪**（⛔ 無遞補）」（`probe_WG991_yishim.py:859`）
⇒ 缺的正是**遞補鏈**。本檔補之。

## 路線（`W-G.9-99` 施工單 §三）

- `3-1` **管線驅動**（`-91` 體例：`run_corner_pk` ⇒ 逐街廓 `run_step_g`），
  ⛔ 非 `-96` 之 pipeline-free——`_solve_G_one` 之 `blk_poly`／`d_hat`／`baseline_pt`／
  `S_max`／`avg_depth`／`tab6_burden` 皆於 `run_step_g` **內**組裝。
  ⇒ 本檔⛔ 不裝 `_forbidden` 護欄；零生產碼之證 ＝ 10 支生產檔 `git hash-object` 出艙前後逐位相同。
- `3-2` 既有 `probe_WG981_scope.spy_solve` 僅自 `kw` 取 **4** 鍵（⛔ 不含 `a_m2`）
  ⇒ **本檔自寫全捕 spy**，逐次呼叫全量存 `kw`（**19** 鍵）＋ `res`。
- `3-3` `W_prev` 係**逐側串接** ⇒ 重播義務：遞補後之序列須自該側**首宗起逐宗重跑**。
- `3-4` 藍影門檻於生產碼**不存在** ⇒ **原樣 import** `probe_WG992_blue._halfplane`＠`:244`
  ＋ `probe_WG940_startperp.line_isect`／`s_of`；⛔ 不重造該式。

## 🔒 三處「層疊而非取代」（⛔ 未改任一既有探針一字）

1. `w81.spy_solve` ← 包一層全捕（`w81.CAP`／`SOLVE` 行為逐位不變）。
2. `w92.run_corner_pk` ← 包一層捕 `wins`／`forced`（`w92.build()` 內部丟棄之，本檔需之）。
3. 二者皆於 `finally` 還原原物並逐位比對。

## `ordered_v2` 之重建（施工單 `§五-2` 所令之法·⛔ 非另訂）

`_projection_order(_stage1_parcels, p1, p2)` 取投影序 ⇒ 依 `app.py:7670-7699` 之 winner
`pop`／`insert` 重放 ＝ **`_spatial_order_parcels_v2`**（其 `pre_position` 於該區間**不被改動**·
`app.py:7670-7699` 之 `pre_position` 命中 ＝ `0`）。
`pk_winners` 取自**實跑之 `run_corner_pk`**（⛔ 非自 CSV 猜測其 `p1_end`／`p2_end` 對應）。

## ⛔ 本檔不做

⛔ 落地、⛔ 移線、⛔ 建介面、⛔ 改任何生產碼／baseline／CSV／DXF／既有探針。
⛔ 就遞補／調配池／合併調配／超配出任何裁定題或提名。

## 重跑

    python verify/probes/probe_WG999_yi_chain.py

`rc` **恆 `0`**；停機以**逐字具名**表示。log 落 `verify/out/probe_WG999_yi_chain_<基座短碼>.log`。
"""
import ast
import collections
import contextlib
import hashlib
import io
import math
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
sys.path.insert(0, VERIFY)
sys.path.insert(0, HERE)

import numpy as np                                                  # noqa: E402

import probe_WG992_blue as w92                                      # noqa: E402
import probe_WG981_scope as w81                                     # noqa: E402
import probe_WG940_startperp as w40                                 # noqa: E402

OUTDIR = os.path.join(VERIFY, "out")
BASE_REF = "23a63d3"
WIDTH = 108

PROD_FILES = ["app.py", "verify/stepg_pipeline.py", "verify/selection_pipeline.py",
              "verify/run_verification.py", "verify/wd4_tier_list.py",
              "verify/wf_f0.py", "verify/wf_f1.py", "verify/wf_f2.py",
              "verify/wf_f3.py", "verify/wf_f4.py"]

SELF = ["verify/probes/probe_WG999_yi_chain.py",
        "verify/out/probe_WG999_yi_chain_%s.log" % BASE_REF,
        "docs/reports/W-G.9-99_乙之遞補鏈shim.md"]

MAX_ROUNDS = 12

L, STOPS = [], []
FULLKW, CAPSEQ, WINS = {}, [], {}


def P(s=""):
    print(s)
    L.append(s)


def hdr(s):
    P("")
    P("=" * WIDTH)
    P(s)
    P("=" * WIDTH)


def stop(tag, text):
    STOPS.append((tag, text))
    P("  🛑 **停機 %s**：%s" % (tag, text))


def git1(a):
    return subprocess.run(["git"] + a, cwd=REPO, capture_output=True,
                          check=True).stdout.decode("utf-8").strip()


def prod_hashes():
    return {f: git1(["hash-object", f]) for f in PROD_FILES}


def blob_of(p, ref=BASE_REF):
    return subprocess.run(["git", "cat-file", "blob", "%s:%s" % (ref, p)],
                          cwd=REPO, capture_output=True, check=True).stdout


def blue_area(C, j0, j1):
    """🔒 藍影 ＝ `block` ∩ {第 0 宗遠側界之外側} ∩ {通過 `B1` 之 ∥ALLOC 之內側}。

    ⛔ 不重造：`_halfplane`＠`probe_WG992_blue.py:244`、`line_isect`／`s_of`＠`probe_WG940_startperp`；
    合成次序逐字依 `probe_WG992_blue.py:333-348`。
    """
    L0p, L0u = C["lots"][j0]["pj"], C["lots"][j0]["uj"]
    L1u = C["lots"][j1]["uj"]
    if L0p is None or L0u is None or L1u is None or C["block"] is None:
        return None, None, None, "取不到解算面／街廓"
    B1 = w40.line_isect(tuple(np.asarray(L0p, float)[:2]),
                        tuple(np.asarray(L0u, float)[:2]), C["bpt"], C["bdir"])
    if B1 is None:
        return None, None, None, "`B1` 求不出（第 0 宗遠側界 ∥ BASELINE？）"
    r0 = C["lots"][j0]["poly"].representative_point()
    r1 = C["lots"][j1]["poly"].representative_point()
    H0 = w92._halfplane(L0p, L0u, (r1.x, r1.y))
    H1 = w92._halfplane(B1, L1u, (r0.x, r0.y))
    blue = C["block"].intersection(H0).intersection(H1)
    Pf = w40.line_isect(tuple(np.asarray(B1, float)[:2]),
                        tuple(np.asarray(L1u, float)[:2]), C["o"], C["d"])
    sreq = w40.s_of(tuple(Pf), C["o"], C["d"]) if Pf is not None else float("nan")
    return float(blue.area), (float(B1[0]), float(B1[1])), sreq, blue.geom_type


def replay(orig_solve, C, seq_idx, w0=0.0):
    """🔒 `§三-3`：自該側首宗起逐宗重跑，`W_prev` 取前一宗 `res['W_far']`。"""
    out, wp = [], float(w0)
    for i in seq_idx:
        ro = C["lots"][i].get("_res_obj")
        kw = FULLKW.get(id(ro)) if ro is not None else None
        if kw is None:
            raise RuntimeError("🔴 `%s` 索引 %d 之 `kw` 未捕獲 ⇒ ⛔ 禁靜默兜底" % (C["_lbl"], i))
        k2 = dict(kw)
        k2["W_prev"] = wp
        res, _lab = orig_solve(**k2)
        out.append((i, float(res.get("G", float("nan"))), res, wp))
        wp = float(res.get("W_far", wp))
    return out


def replay_bump(orig_solve, C, seq_idx, k, bump):
    """🔒 與 `replay` 同，惟於**第 `k` 宗**之 `W_prev` 加 `bump`（正向對照用）。"""
    out, wp = [], 0.0
    for q, i in enumerate(seq_idx):
        ro = C["lots"][i].get("_res_obj")
        kw = FULLKW.get(id(ro)) if ro is not None else None
        if kw is None:
            raise RuntimeError("🔴 `%s` 索引 %d 之 `kw` 未捕獲 ⇒ ⛔ 禁靜默兜底" % (C["_lbl"], i))
        k2 = dict(kw)
        k2["W_prev"] = wp + (bump if q == k else 0.0)
        res, _lab = orig_solve(**k2)
        out.append((i, float(res.get("G", float("nan"))), res, k2["W_prev"]))
        wp = float(res.get("W_far", wp))
    return out


def main():                                                          # noqa: C901
    log_path = os.path.join(OUTDIR, "probe_WG999_yi_chain_%s.log" % BASE_REF)
    H_BEFORE = prod_hashes()

    hdr("【W-G.9-99】「乙」之遞補鏈 shim（⛔ 零生產碼·⛔ 非落地）")
    P("  基座（log 檔名所綁）＝ **%s**" % BASE_REF)
    P("  🔒 KL 逐字（`docs/reports/W-G.4_泛用阻塞項登記表.md:2371-2372`）：")
    P("     「先落乙，把最基本的幾何分配位置及方式確定，才做後續甲矩形容納」")
    P("     「落地前，先以 shim 量出各自的土地後果」")

    # ── §一　A0-1〜A0-8 ─────────────────────────────────────────────────────
    hdr("【§一】開工閘 `A0-*`（⛔ 其後受詞在此之前一律未開辦）")
    ok = [True]

    def gate(gid, exp, got, cmd):
        good = (str(exp) == str(got))
        ok[0] = ok[0] and good
        P("  %-6s %s  期望＝%s" % (gid, "✅" if good else "🔴", exp))
        P("         現查＝%s   （%s）" % (got, cmd))
        if not good:
            stop("①", "`%s` 閘紅 ⇒ ⛔ 不得續辦 `§五`" % gid)
        return good

    head = git1(["rev-parse", "HEAD"])
    gate("A0-1", "23a63d3a494532784d392cf7138d76daed8bfdd8", head, "git rev-parse HEAD")
    gate("A0-2", "23a63d3a494532784d392cf7138d76daed8bfdd8",
         git1(["rev-parse", "origin/wip/s1-endpart"]), "git rev-parse origin/wip/s1-endpart")
    ab = git1(["rev-parse", "HEAD:app.py"])
    gate("A0-3", "a9e5671d64d254907a0396f898f046d9d85e8283", ab, "git rev-parse HEAD:app.py")
    gate("A0-4", ab, git1(["hash-object", "app.py"]), "git hash-object app.py（⇒ 工作區未髒）")

    ZI = "docs/reports/W-G.9波_claude.ai側自誤登記.md"
    K6 = "docs/rulings/K-6_街角地分配程序與可分配判準.md"
    P("")
    P("  🔒 **量測框**：`A0-5`／`A0-6` 取 **blob（LF）** 口徑（本機 `core.autocrlf=true`）。")
    for gid, path, el, ec, es in [
            ("A0-5", ZI, 2757, 182538,
             "e8ddd4c194eca5be6bb13f35fbcc27512542e764391c73f15a0c26f0e2c2bd62"),
            ("A0-6", K6, 3037, 207289,
             "b533700407165efef2976c32653ca221dd9baad5d63d5e80f3b084a49221104e")]:
        b = blob_of(path)
        gate(gid, "%d 列／%d B／%s" % (el, ec, es),
             "%d 列／%d B／%s" % (b.count(b"\n"), len(b), hashlib.sha256(b).hexdigest()),
             "blob 之 wc-l／wc-c／sha256")
    zi = blob_of(ZI).decode("utf-8").split("\n")
    nz = [int(m.group(1)) for l in zi for m in [re.match(r"^## 自誤 ([0-9]+)", l)] if m]
    gate("A0-7", "max=109 命中=66", "max=%d 命中=%d" % (max(nz), len(nz)), "^## 自誤 [0-9]+")
    k6 = blob_of(K6).decode("utf-8").split("\n")
    nk = [int(m.group(1)) for l in k6
          for m in [re.match(r"^###\s*(?:🔒\s*)?`?K-9-([0-9]+)\b", l)] if m]
    gate("A0-8", "max=17 命中=30", "max=%d 命中=%d" % (max(nk), len(nk)), "K-9 窄樣式")
    if not ok[0]:
        return finish(log_path, H_BEFORE)

    # ── §二　管線驅動 ＋ 二處層疊 ────────────────────────────────────────────
    hdr("【§二】管線驅動（`-91` 體例）＋ 全捕 spy ＋ `wins` 攔截（皆**層疊**·⛔ 未改既有探針）")
    src_app = open(os.path.join(REPO, "app.py"), encoding="utf-8").read()
    fdef = [n for n in ast.walk(ast.parse(src_app))
            if isinstance(n, ast.FunctionDef) and n.name == "_solve_G_one"]
    kwn = sorted(a.arg for a in fdef[0].args.kwonlyargs) if fdef else []
    P("  `_solve_G_one` 定義命中 ＝ **%d**；`kwonly` ＝ **%d** 鍵（預測 19 ⇒ %s）"
      % (len(fdef), len(kwn), "✅" if len(kwn) == 19 else "🔴"))
    P("     %s" % "／".join(kwn))
    n_pp = sum(1 for l in src_app.split("\n")[7669:7699] if "pre_position" in l)
    P("  🔒 `app.py:7670-7699`（winner `pop`／`insert`）之 `pre_position` 命中 ＝ **%d**"
      "（⇒ 重排⛔ 不改 `pre_position`·施工單錨）" % n_pp)
    if len(fdef) != 1 or len(kwn) != 19:
        stop("①", "`_solve_G_one` 簽名與 `§三-2` 不符")
        return finish(log_path, H_BEFORE)

    of_spy, of_rcp = w81.spy_solve, w92.run_corner_pk

    def spy_factory(orig):
        inner = of_spy(orig)

        def _f(**kw):
            res, lab = inner(**kw)
            FULLKW[id(res)] = dict(kw)
            CAPSEQ.append(id(res))
            return res, lab
        return _f

    def rcp(*a, **kw):
        out = of_rcp(*a, **kw)
        WINS["wins"], WINS["forced"] = out[3], out[4]
        return out

    w81.spy_solve, w92.run_corner_pk = spy_factory, rcp
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            CELL, REAL = w92.build()
    finally:
        w81.spy_solve, w92.run_corner_pk = of_spy, of_rcp
    P("  還原後同一物：`w81.spy_solve` ＝ %s；`w92.run_corner_pk` ＝ %s"
      % (w81.spy_solve is of_spy, w92.run_corner_pk is of_rcp))
    P("  `w81.CAP` ＝ **%d** 街廓記錄；全捕 ＝ **%d** 次；`kw` 鍵數（相異）＝ %s"
      % (len(REAL), len(CAPSEQ), sorted({len(v) for v in FULLKW.values()})))
    P("  `run_corner_pk` 之 `wins` 攔截 ＝ %s" % ("✅ 取得" if "wins" in WINS else "🔴 未取得"))
    if "wins" not in WINS:
        stop("⑥", "`wins` 未攔截到 ⇒ ⛔ 不得改自 CSV 猜測 `p1_end`／`p2_end` 對應")
        return finish(log_path, H_BEFORE)

    from app_harvest import harvest                                  # noqa: E402
    import run_verification as rv                                    # noqa: E402
    with contextlib.redirect_stdout(io.StringIO()):
        ns2, fs2 = harvest()
        snap = rv.load_snapshot()
        cb_by, cad = rv.build_pipeline(ns2, fs2, snap)
        rv.build_ownership(ns2, fs2, rv.ANON_XLSX)
        with open(rv.V6DXF, "rb") as f:
            v6 = f.read()
        _tp, build_p, _sw = rv.build_build_parcels(ns2, fs2, v6, list(cb_by.values()), snap)
    orig_solve = ns2["_solve_G_one"]
    SOP2, PO = ns2["_spatial_order_parcels_v2"], ns2["_projection_order"]

    # ── §三　A0-9〜A0-11 ────────────────────────────────────────────────────
    hdr("【§三】開工閘 `A0-9`〜`A0-11`（harness 層）")
    ghosts = [t for t in build_p if t.get("_is_ghost_sliver", False)]
    nong = [t for t in build_p if not t.get("_is_ghost_sliver", False)]
    by_blk = collections.OrderedDict()
    for t in nong:
        by_blk.setdefault(t.get("所屬街廓"), []).append(t)
    raw = collections.Counter(t.get("所屬街廓") for t in build_p)
    gate("A0-9", "cb_by=11 build_parcels=61 ghost=2 非ghost=59",
         "cb_by=%d build_parcels=%d ghost=%d 非ghost=%d"
         % (len(cb_by), len(build_p), len(ghosts), len(nong)), "harness")
    RB = ["R1", "R2", "R3", "R4", "R5", "R6"]
    gate("A0-10", "R1:5／R2:15／R3:14／R4:2／R5:12／R6:11",
         "／".join("%s:%d" % (b, len(by_blk.get(b, []))) for b in RB), "非-ghost 逐街廓")
    # 🔒 `A0-11` 之受詞係 ghost 之**具名集合**＋面積，⛔ 非 `build_parcels` 之迭代**序**
    #    （首版以 join 後字串相等施測 ⇒ 得「集合同而序不同」之假紅；改正者為**檢**、⛔ 非資料）
    gate("A0-11", "_GHOST_(R1)(5.28)／_GHOST_(R4)(8.09)",
         "／".join(sorted("%s(%.2f)" % (g.get("暫編地號"),
                                        float(g.get("_ghost_area_m2", 0) or 0)) for g in ghosts)),
         "ghost 具名＋面積（**排序後**·受詞為集合）")
    P("")
    P("  🩸 併記覆驗：未扣 ghost 之原始 `build_parcels` 逐街廓 ＝ %s"
      % "／".join("%s:%d" % (b, raw.get(b, 0)) for b in RB))
    P("     ⇒ 二 ghost 恰各落 `R1`／`R4`；⛔ 不得把 `61` 直接按街廓拆帳。")
    if not ok[0]:
        return finish(log_path, H_BEFORE)

    for lbl, C in CELL.items():
        C["_lbl"] = lbl
        rs = C["rec"].get("ress") or []
        for i in C["lots"]:
            C["lots"][i]["_res_obj"] = rs[i] if i < len(rs) else None
    tot = sum(len(C["lots"]) for C in CELL.values())
    hit = sum(1 for C in CELL.values() for i in C["lots"]
              if C["lots"][i]["_res_obj"] is not None
              and id(C["lots"][i]["_res_obj"]) in FULLKW)
    P("")
    P("  🔒 **`kw` 覆蓋率先驗**（`id(res)` 對應）：宗 ＝ **%d**／可重播 ＝ **%d**" % (tot, hit))
    if hit != tot:
        stop("⑥", "`kw` 覆蓋 %d／%d ⇒ ⛔ 不得自造替代式、⛔ 不得靜默略過" % (hit, tot))
        return finish(log_path, H_BEFORE)

    # ── §四　段一：`ordered_v2`（施工單 `§五-2` 所令之法）─────────────────────
    hdr("【§四】`§五 段一`：各街廓**各側**之街角重排後序列 `ordered_v2`（⛔ 非重排前）")
    P("  🔒 重建法 ＝ 施工單 `§五-2` 所令：`_projection_order` ⇒ `app.py:7670-7699` 之 winner")
    P("     `pop`／`insert`（＝ `_spatial_order_parcels_v2`）；`pk_winners` 取自**實跑之 `run_corner_pk`**。")
    FL = (fs2.session_state.get("f3_cad_front_lines") or {}) or (cad.get("front_lines") or {})
    wins = WINS["wins"] or {}
    ORD, SIDES = {}, []
    for lbl in RB:
        st1 = [t for t in by_blk.get(lbl, []) if "配地階段" not in t]
        fl = FL.get(lbl) or {}
        if not st1 or not (fl.get("p1") and fl.get("p2")):
            P("  `%s`：⛔ 略過（階段1宗 ＝ %d／FRONT_LINE ＝ %s）"
              % (lbl, len(st1), bool(fl.get("p1") and fl.get("p2"))))
            continue
        w = (wins.get(lbl) or {})
        res = SOP2(parcels_in_block=st1, d_hat=None, front_line_p1=fl["p1"],
                   front_line_p2=fl["p2"], pk_winners=w, forced_offset={})
        ordered = res["ordered"]
        ORD[lbl] = ordered
        names = [e["tp"]["暫編地號"] for e in ordered]
        pres = [e["pre_position"] for e in ordered]
        P("")
        P("  `%s`  n=%d｜`pk_winners` ＝ %s" % (lbl, len(ordered), w or "{}（無 winner）"))
        P("     `ordered_v2`（括號 ＝ **重排前投影序號** `pre_position`）：")
        P("       %s" % " → ".join("%s⁽%s⁾%s" % (nm, pp, "★" if ordered[q].get("is_corner_winner") else "")
                                   for q, (nm, pp) in enumerate(zip(names, pres))))
        for slot, key in (("右(p1)", "p1_end"), ("左(p2)", "p2_end")):
            if w.get(key):
                SIDES.append((lbl, slot, key))
        if not w:
            P("     ⛔ 該街廓無 winner ⇒ `§五 段一`／`段四` 之受詞不成立 ⇒ 二側皆略過（具名）")
    P("")
    P("  POPULATION=%d PRINTED=%d SUPPRESSED=%d  # 街廓（納入 ＝ 有 FRONT_LINE 且有階段1宗）"
      % (len(RB), len(ORD), len(RB) - len(ORD)))
    P("  有 winner 之側 ＝ **%d**：%s" % (len(SIDES), "、".join("%s|%s" % (a, b) for a, b, _ in SIDES)))

    # ── §五　`§五-2` 之獨立重建（停機②）─────────────────────────────────────
    hdr("【§五】`§五-2`：第一輪遞補宗之**獨立重建**（停機② 之判準）")
    EXP = {"R2": (["628-41(1)", "628-42(1)", "628-27(1)", "628-40(1)"], "628-42(1)", "628-27(1)"),
           "R5": (["628-18(2)", "628-53(2)", "628-45(1)", "628-7(2)"], "628-53(2)", "628-45(1)")}
    P("  %-4s %-56s %-14s %-14s %s" % ("街廓", "重建之 `ordered_v2` 前四位", "違反宗", "遞補宗", "判"))
    ok2 = True
    for lbl in ("R2", "R5"):
        exp4, vio, succ = EXP[lbl]
        got = [e["tp"]["暫編地號"] for e in ORD.get(lbl, [])][:4]
        good = (got == exp4)
        ok2 = ok2 and good
        P("  %-4s %-56s %-14s %-14s %s"
          % (lbl, " → ".join(got or ["（取不到）"]), vio,
             (got[2] if len(got) > 2 else "—"), "✅" if good else "🔴"))
        if not good:
            stop("②", "`%s` 之重建 %s ≠ 預測 %s ⇒ ⛔ 不得就地改判準" % (lbl, got, exp4))
        elif got[2] != succ:
            ok2 = False
            stop("②", "`%s` 之遞補宗 %s ≠ 預測 %s" % (lbl, got[2], succ))
    P("  🔒 判準：**逐格相同**方得續辦（⛔ 不以「無異常」為證）。")
    if not ok2:
        return finish(log_path, H_BEFORE)

    return measure(CELL, ORD, SIDES, orig_solve, log_path, H_BEFORE)


def measure(CELL, ORD, SIDES, orig_solve, log_path, H_BEFORE):       # noqa: C901
    # ── §六　段四 ＋ 段五：藍影門檻 ⇒ 連鎖遞補；`G` 重算 ────────────────────
    hdr("【§六】`段四`（藍影門檻⇒連鎖遞補·每輪出艙）＋`段五`（遞補宗與其後各宗 `G` 重算）")
    P("  🔒 藍影式⛔ 未重造（`_halfplane`＠`probe_WG992_blue.py:244`；合成序依 `:333-348`）。")
    P("  🔒 `G` 重算 ＝ `§三-3` 之 `W_prev` 逐宗重串（自該側**首宗**起）。")
    P("  ⚠️ **本 shim 之射程（⛔ 具名·非靜默）**：重播時僅 `W_prev` 隨序列改變；`baseline_pt`／")
    P("     `S_max`／`avg_depth` 等**位置相依** kwarg 取該宗**捕獲之原值**（held fixed）。")
    P("     ⇒ `G_新` 係**遞補鏈之一階近似**，⛔ 不得充作落地後之最終 `G`。")
    CHAIN = []
    for lbl, slot, key in SIDES:
        C = CELL.get(lbl)
        ordered = ORD[lbl]
        if C is None:
            P("  `%s|%s`：⛔ 略過（`CELL` 無該街廓·具名）" % (lbl, slot))
            continue
        nm2i = {}
        for i in C["lots"]:
            nm2i[C["lots"][i]["name"]] = i
        seq = [e["tp"]["暫編地號"] for e in ordered]
        if key == "p2_end":
            seq = list(reversed(seq))
        idxs = [nm2i.get(n) for n in seq]
        if any(x is None for x in idxs):
            P("  `%s|%s`：⛔ 略過——`ordered_v2` 有宗不在 `CELL` 之 `lots` 內（%s）·具名"
              % (lbl, slot, [n for n, x in zip(seq, idxs) if x is None]))
            continue
        P("")
        P("  ── 街廓 `%s`／側 `%s`（n=%d·第 0 宗 ＝ `%s`）──" % (lbl, slot, len(idxs), seq[0]))
        cur, kicked, pool, rounds, conv = list(idxs), [], 0.0, 0, None
        while True:
            rounds += 1
            if rounds > MAX_ROUNDS:
                stop("③", "`%s|%s` 之遞補鏈於自訂上限 `%d` 輪仍未收斂 ⇒ ⛔ 不得截斷後宣稱終態"
                     % (lbl, slot, MAX_ROUNDS))
                conv = False
                break
            if len(cur) < 2:
                P("     第 %d 輪：該側僅餘 %d 宗 ⇒ 無第 1 宗可評 ⇒ **收斂**（具名）" % (rounds, len(cur)))
                conv = True
                break
            j0, j1 = cur[0], cur[1]
            ba, B1, sreq, diag = blue_area(C, j0, j1)
            if ba is None:
                stop("⑥", "`%s|%s` 第 %d 輪之藍影取不到（%s）⇒ ⛔ 不得自造替代式"
                     % (lbl, slot, rounds, diag))
                conv = False
                break
            rep = replay(orig_solve, C, cur)
            g1 = dict((i, g) for i, g, _r, _w in rep).get(j1)
            fail = (g1 is not None) and (g1 < ba)
            P("     第 %d 輪：候選第 1 宗 ＝ `%s`｜`G₁` ＝ %.4f｜藍影 ＝ %.6e｜`G₁−藍影` ＝ %+.6e｜判 ＝ %s"
              % (rounds, C["lots"][j1]["name"], g1 if g1 is not None else float("nan"),
                 ba, (g1 - ba) if g1 is not None else float("nan"),
                 "🔴 **未達 ⇒ 遞補**" if fail else "✅ 達標 ⇒ 收斂"))
            P("        `B1` ＝ %s｜`S_req` ＝ %.6f｜藍影幾何 ＝ %s"
              % (("(%.3f, %.3f)" % B1) if B1 else "—", sreq, diag))
            P("        ⛔ **會使本判為否之輸入**：`G₁ ≥ %.6e` ⇒ 判「達標」。" % ba)
            if not fail:
                conv = True
                break
            rel = C["lots"][j1].get("G")
            rel = float(rel) if rel is not None else float("nan")
            pool += (0.0 if math.isnan(rel) else rel)
            kicked.append((C["lots"][j1]["name"], rel))
            cur = [cur[0]] + cur[2:]
        rep = replay(orig_solve, C, cur)
        P("        `段五` 逐宗 `G_舊 → G_新`（`W_prev` 重串後·⛔ 全列）：")
        nd = 0
        for i, g, _r, wp in rep:
            go = C["lots"][i].get("G")
            go = float(go) if go is not None else float("nan")
            d = g - go
            if abs(d) > 1e-9:
                nd += 1
            P("           %-16s W_prev=%-10.4f G_舊=%-10.4f → G_新=%-10.4f Δ=%+.6f"
              % (C["lots"][i]["name"], wp, go, g, d))
        P("        `Δ ≠ 0` 之宗數 ＝ **%d**／%d｜`段二` 被踢除宗（入調配池）＝ %s｜**入池合計 ＝ %.4f ㎡**"
          % (nd, len(rep),
             ("、".join("`%s`(%.4f㎡)" % (a, b) for a, b in kicked) if kicked else "（無）"), pool))
        CHAIN.append({"lbl": lbl, "slot": slot, "rounds": rounds, "conv": conv,
                      "kicked": kicked, "pool": pool, "nd": nd})
    P("")
    P("  POPULATION=%d PRINTED=%d SUPPRESSED=0  # 有 winner 之側（全列）" % (len(SIDES), len(CHAIN)))
    P("  收斂 ＝ **%d**／未收斂 ＝ **%d**｜`Δ≠0` 至少一宗之側 ＝ **%d**／%d"
      % (sum(1 for c in CHAIN if c["conv"] is True),
         sum(1 for c in CHAIN if c["conv"] is False),
         sum(1 for c in CHAIN if c["nd"] > 0), len(CHAIN)))
    if CHAIN and all(c["nd"] == 0 for c in CHAIN):
        stop("⑤", "全側之 `Δ` 皆 ＝ 0 ⇒ **重算未生效**（＝對照組退化之同型）⇒ ⛔ 不得計為證據")

    # ── §六-b　正向對照（`驗收 7`／`§六-4`／自誤 `109`）────────────────────────
    hdr("【§六-b】正向對照：重播機制之**擾動量自證**（⛔ 擾動 ＝ 0 者列 `略過`·⛔ 不計為證據亦不計為反證）")
    P("  🩸 **本檔首版之對照已退化、具名保留**：首版把 `+1.0` 加於**首宗**，而首宗恰為")
    P("     `is_corner=True` 之街角 winner ⇒ 其 `G` 不隨 `W_prev` 動、`W_far` 由幾何定")
    P("     ⇒ 擾動當場被吸收 ⇒ **全 8 側擾動量 ＝ 0**。此即 `§附 A-6` 已預警之分層")
    P("     （`is_corner=True ∧ W_prev 基值 ＝ 0` ⇒ `G` 不動）⇒ **對照組退化、⛔ 非被測物失能**。")
    P("  🔒 **改正後之構造**：於該側**首個 `W_prev` 基值 ≠ 0 之非街角宗**（索引 `k`）注入 `+1.0`，")
    P("     重播全側 ⇒ 數其**下游** `G` 有動之宗。⛔ 若該側無此種宗 ⇒ 列 `略過` 並具名。")
    P("")
    P("  %-4s %-8s %-5s %-5s %-18s %-8s %-14s %s"
      % ("街廓", "側", "n", "k", "注入點宗", "擾動量", "max|ΔG|", "判"))
    ctl_ok, ctl_deg = 0, []
    for lbl, slot, key in SIDES:
        C = CELL.get(lbl)
        if C is None:
            continue
        nm2i = {C["lots"][i]["name"]: i for i in C["lots"]}
        seq = [e["tp"]["暫編地號"] for e in ORD[lbl]]
        if key == "p2_end":
            seq = list(reversed(seq))
        idxs = [nm2i.get(n) for n in seq]
        if any(x is None for x in idxs):
            continue
        base = replay(orig_solve, C, idxs, 0.0)
        kk = None
        for q, (i, _g, _r, wp) in enumerate(base):
            if abs(wp) > 1e-12 and not C["lots"][i]["is_corner"]:
                kk = q
                break
        if kk is None:
            ctl_deg.append("%s|%s（無「`W_prev` 基值 ≠ 0 且非街角」之宗）" % (lbl, slot))
            P("  %-4s %-8s %-5d %-5s %-18s %-8s %-14s %s"
              % (lbl, slot, len(idxs), "—", "—", "—", "—",
                 "🩸 **無可注入點 ⇒ 略過（退化）**"))
            continue
        pert = replay_bump(orig_solve, C, idxs, kk, 1.0)
        gb = {i: g for i, g, _r, _w in base}
        gp = {i: g for i, g, _r, _w in pert}
        d = [abs(gp[i] - gb[i]) for i in gb]
        nmv = sum(1 for x in d if x > 1e-9)
        mx = max(d) if d else 0.0
        if nmv > 0:
            ctl_ok += 1
        else:
            ctl_deg.append("%s|%s（注入於 k=%d 仍無動）" % (lbl, slot, kk))
        P("  %-4s %-8s %-5d %-5d %-18s %-8d %-14.6f %s"
          % (lbl, slot, len(idxs), kk, C["lots"][base[kk][0]]["name"], nmv, mx,
             "✅ 擾動量 > 0" if nmv > 0 else "🩸 **擾動量 ＝ 0 ⇒ 略過（退化）**"))
    P("")
    P("  母體 ＝ **%d** 側／擾動量 > 0 ＝ **%d**／退化（略過·逐項具名）＝ **%d**"
      % (len(SIDES), ctl_ok, len(ctl_deg)))
    for x in ctl_deg:
        P("     略過：`%s`" % x)
    if ctl_ok == 0:
        stop("⑤", "全側之對照擾動量皆 ＝ 0 ⇒ 對照組**全退化** ⇒ ⛔ 不計為證據亦⛔ 不計為反證")
    else:
        P("  ⇒ 重播機制**確實會動**（⛔ 非恆真）⇒ `段五` 之 `G_舊 → G_新` 具判別力。")

    # ── §七　段二：不交叉 ───────────────────────────────────────────────────
    hdr("【§七】`段二`：境界線**不交叉**（判準原樣 ＝ `probe_WG992_blue.nocross_rows`＠`:194`）")
    rows = w92.nocross_rows(CELL)
    bad = [r for r in rows if r.get("cross")]      # 🔒 鍵為 `cross`（`probe_WG992_blue.py:238`）
    P("  母體 ＝ **%d** 列；判「交叉」＝ **%d** 列" % (len(rows), len(bad)))
    for r in bad:
        P("     🔴 %-22s 理由=%-16s 面積=%.4f ㎡" % (r["key"], r["reason"], r["area"]))
    P("  🔒 `§五-1` 之現行有效結論 ＝ **2 宗／4.7950 ㎡**（`R2 左 第1宗` `3.8082`／`R5 左 第1宗` `0.9867`）")
    P("     ⇒ 本批母體之受詞為**相鄰對**（`prev`→`i`），與該結論之**宗**層⛔ 非同一受詞 ⇒ ⛔ 不代換。")

    # ── §八　段七：守恆（停機⑦）────────────────────────────────────────────
    hdr("【§八】`段七`：終態守恆（停機⑦）")
    for lbl in sorted(CELL):
        C = CELL[lbl]
        gs = [C["lots"][i].get("G") for i in C["lots"]]
        P("     `%s`：捕獲宗 ＝ %d／具 `G` 者 ＝ %d｜街廓面積 ＝ %.4f ㎡"
          % (lbl, len(gs), sum(1 for g in gs if g is not None),
             float(C["block"].area) if C["block"] is not None else float("nan")))
    stop("⑦", "`R2`／`R5` 之 `run_step_g` 於 `②-宗` 圍堵閘 `raise`（`GB-67`·⛔ 尚未修）、`R4` 於"
              "結構閘「理論＝實跑」`raise` ⇒ **終態（抵費地／池）不可由管線取得** ⇒ "
              "逐字具名 **【須執行該碼·本批不跑】**")
    P("  🔒 ⛔ 未以「捕到 `G` 就算有終態」代替；亦⛔ 未自造獨立幾何路徑——")
    P("     理由：`池 ≝ 街廓面積 − Σ配地` 係**定義式**，據之算殘差**恆為 `0`** ⇒ 恆真空檢")
    P("     （考古節 `123`）⇒ ⛔ 不得充作守恆之獨立驗證。")
    return finish(log_path, H_BEFORE)


def finish(log_path, H_BEFORE):
    hdr("【§九】收工：生產檔 hash 前後對拍・`SELF` 自扣・停機逐字")
    H_AFTER = prod_hashes()
    same = [f for f in PROD_FILES if H_BEFORE.get(f) == H_AFTER.get(f)]
    P("  10 支生產檔 `git hash-object` 出艙前後**逐位相同** ＝ **%d／%d** ⇒ %s"
      % (len(same), len(PROD_FILES), "✅ 零生產碼變更" if len(same) == len(PROD_FILES) else "🔴"))
    for f in PROD_FILES:
        P("     %-34s %s %s" % (f, H_BEFORE.get(f),
                                "✅" if H_BEFORE.get(f) == H_AFTER.get(f)
                                else "🔴 → %s" % H_AFTER.get(f)))
    if len(same) != len(PROD_FILES):
        stop("①", "生產檔 hash 前後不同 ⇒ 「零生產碼」宣稱**不成立**")
    P("")
    P("  🔒 **`SELF` 自扣**：本批產物 ＝ %s" % "、".join("`%s`" % s for s in SELF))
    P("     ⇒ ⛔ 不在本檔任一母體內（母體皆為街廓／宗地／側／`kw` 鍵·⛔ 非檔案母體）。")
    P("")
    if STOPS:
        P("  🛑 **本批之停機（逐字具名·`rc` 恆 `0`）**：")
        for t, x in STOPS:
            P("     停機 %s：%s" % (t, x))
    else:
        P("  ✅ 本批未觸任一停機條件。")
    os.makedirs(OUTDIR, exist_ok=True)
    with open(log_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(L) + "\n")
    print("")
    print("log -> %s" % os.path.relpath(log_path, REPO).replace(os.sep, "/"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
