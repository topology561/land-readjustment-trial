# -*- coding: utf-8 -*-
r"""`W-G.9-99 補正②`：`W_prev` **真鏈**之構造性還原 ＋ 忠實重播 ⇒ 池增量定案。

## 受詞

`W-G.9-99` 之重播把整條 `ordered_v2` 壓成**一條** `W` 鏈，`補正①` 已證其**非 baseline-faithful**。
本檔以**實跑管線之捕獲**還原**真鏈**，據之重播，並回答三問：

1. `side` kwarg 是否為鏈鍵？
2. 真鏈之結構（含**不在任何鏈上**之 singleton 宗）為何？
3. 沿真鏈之忠實重播，其 `ΣΔ` 與池增量為何？`R1` 之 `ΣΔ` 是否為 `0`？

## 🔒 資料源 ＝ **本檔實跑管線之捕獲**（⛔ 不自任何 log 讀 `Δ`）

`§四-4` 之硬約束。本檔**不解析** `probe_WG999_yi_chain_*.log`；一切數皆由本次執行之
`_solve_G_one` 捕獲現算。

## 真鏈之還原規則（施工單 `§一-2`）

> 沿**呼叫序**掃描；`W_prev == 0` ⇒ **起新鏈**；否則須 `W_prev[k] == W_far[k-1]`（`≤ 1e-9`）。

## 四處「層疊而非取代」（⛔ 未改任一既有探針一字）

1. `w81.spy_solve` ← 包全捕（`kw` 19 鍵 ＋ `res` ＋ **呼叫序**）。
2. `w92.run_corner_pk` ← 包 `wins` 攔截。
3. `w92.run_step_g` ← 包**當前街廓標籤**之攔截（本檔新增·供逐街廓分鏈）。
4. 皆於 `finally` 還原並逐位比對。

⛔ 不得修改 `probe_WG999_yi_chain.py`／`probe_WG999b_pool_conservation.py`／
`probe_WG992_blue.py`／`probe_WG981_scope.py` 等既有探針（常規一 `②`）。

## 重跑

    python verify/probes/probe_WG999c_true_chain.py

`rc` **恆 `0`**；停機以**逐字具名**表示。
log 落 `verify/out/probe_WG999c_true_chain_<基座短碼>.log`（檔名綁**基座**·考古節 `122`）。
"""
import collections
import contextlib
import io
import math
import os
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
BASE_REF = "3103ab5"
WIDTH = 112
EPS = 1e-9
BLUE_EPS = 1e-6

PROD_FILES = ["app.py", "verify/stepg_pipeline.py", "verify/selection_pipeline.py",
              "verify/run_verification.py", "verify/wd4_tier_list.py",
              "verify/wf_f0.py", "verify/wf_f1.py", "verify/wf_f2.py",
              "verify/wf_f3.py", "verify/wf_f4.py"]

SELF = ["verify/probes/probe_WG999c_true_chain.py",
        "verify/out/probe_WG999c_true_chain_%s.log" % BASE_REF,
        "docs/reports/W-G.9-99_乙之遞補鏈shim.md（【更正之更正】段）",
        "docs/驗證裁定登記表.md（`VR-055`）",
        "docs/reports/W-G.9波_claude.ai側自誤登記.md（自誤 `111`）"]

L, STOPS = [], []
CAP = []                    # 逐次呼叫：{'seq','lbl','kw','G','W_far','res'}
CURBLK = {"lbl": None}
WINS = {}


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


def blue_area(C, j0, j1):
    """🔒 藍影（⛔ 不重造）：`_halfplane`＠`probe_WG992_blue.py:244`；合成序依 `:333-348`。"""
    L0p, L0u = C["lots"][j0]["pj"], C["lots"][j0]["uj"]
    L1u = C["lots"][j1]["uj"]
    if L0p is None or L0u is None or L1u is None or C["block"] is None:
        return None
    B1 = w40.line_isect(tuple(np.asarray(L0p, float)[:2]),
                        tuple(np.asarray(L0u, float)[:2]), C["bpt"], C["bdir"])
    if B1 is None:
        return None
    r0 = C["lots"][j0]["poly"].representative_point()
    r1 = C["lots"][j1]["poly"].representative_point()
    H0 = w92._halfplane(L0p, L0u, (r1.x, r1.y))
    H1 = w92._halfplane(B1, L1u, (r0.x, r0.y))
    return float(C["block"].intersection(H0).intersection(H1).area)


def main():                                                          # noqa: C901
    log_path = os.path.join(OUTDIR, "probe_WG999c_true_chain_%s.log" % BASE_REF)
    H_BEFORE = prod_hashes()

    hdr("【W-G.9-99 補正②】`W_prev` 真鏈之還原 ＋ 忠實重播（⛔ 零生產碼·🔒 實跑管線·⛔ 不讀 log）")
    P("  基座（log 檔名所綁）＝ **%s**" % BASE_REF)
    P("  HEAD ＝ %s；`app.py` blob ＝ %s"
      % (git1(["rev-parse", "HEAD"]), git1(["rev-parse", "HEAD:app.py"])))
    P("  🔒 **資料源 ＝ 本次執行之捕獲**；本檔⛔ 未解析任何既有 log（`§四-4` 之硬約束）。")

    # ── §一　四處層疊 ＋ 實跑 ────────────────────────────────────────────────
    hdr("【§一】管線驅動（`-91` 體例）＋ 四處**層疊**（⛔ 未改任一既有探針）")
    of_spy, of_rcp, of_rsg = w81.spy_solve, w92.run_corner_pk, w92.run_step_g

    def spy_factory(orig):
        inner = of_spy(orig)

        def _f(**kw):
            res, lab = inner(**kw)
            CAP.append({"seq": len(CAP), "lbl": CURBLK["lbl"], "kw": dict(kw),
                        "G": float(res.get("G", float("nan"))),
                        "W_far": float(res.get("W_far", float("nan"))),
                        "rid": id(res)})
            return res, lab
        return _f

    def rcp(*a, **kw):
        out = of_rcp(*a, **kw)
        WINS["wins"] = out[3]
        return out

    def rsg(*a, **kw):
        lbl = None
        try:
            for x in a:
                if isinstance(x, list) and x and isinstance(x[0], dict) and "所屬街廓" in x[0]:
                    lbl = x[0]["所屬街廓"]
                    break
        except Exception as e:                                       # noqa: BLE001
            raise RuntimeError("🔴 街廓標籤攔截失敗（no-silent-fallback）：%r" % (e,))
        if lbl is None:
            raise RuntimeError("🔴 `run_step_g` 之參數中找不到街廓標籤 ⇒ ⛔ 禁靜默兜底")
        CURBLK["lbl"] = lbl
        try:
            return of_rsg(*a, **kw)
        finally:
            CURBLK["lbl"] = None

    w81.spy_solve, w92.run_corner_pk, w92.run_step_g = spy_factory, rcp, rsg
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            CELL, REAL = w92.build()
    finally:
        w81.spy_solve, w92.run_corner_pk, w92.run_step_g = of_spy, of_rcp, of_rsg
    P("  還原後同一物：`spy_solve`＝%s／`run_corner_pk`＝%s／`run_step_g`＝%s"
      % (w81.spy_solve is of_spy, w92.run_corner_pk is of_rcp, w92.run_step_g is of_rsg))
    P("  捕獲 ＝ **%d** 次；街廓標籤皆非空 ＝ %s"
      % (len(CAP), all(c["lbl"] for c in CAP)))
    if not CAP or not all(c["lbl"] for c in CAP):
        stop("捕獲", "捕獲為空或有未標街廓者 ⇒ ⛔ 不得續辦")
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
    SOP2 = ns2["_spatial_order_parcels_v2"]
    FL = (fs2.session_state.get("f3_cad_front_lines") or {}) or (cad.get("front_lines") or {})

    # ── 名稱解析（`(街廓, a_m2)`·**歧義限縮具名**）────────────────────────────
    #   🩸 首版對「任一歧義」即全域停機 ⇒ 受詞外之 `R3`（`628-28(1)`/`628-29(1)`、
    #      `628-47(1)`/`628-48(1)` 分攤登記面積相同）也擋下本批 ⇒ **檢過寬**。
    #   🩸 二版把 `baseline_pt` 放進簽章 ⇒ 自我否定（`baseline_pt` **本身隨鏈而異**，
    #      正是 `R1` 換鏈之現象）⇒ 13 筆未解析。
    #   ⇒ 定案：以 `(街廓, a_m2)` 為鍵、**歧義鍵逐項具名**，僅當歧義落於本批受詞
    #      （`R1`／`R2`／`R5`）之鏈成員時方停機。
    nm, amb = {}, {}
    for tp in build_p:
        if tp.get("_is_ghost_sliver", False) or "配地階段" in tp:
            continue
        k = (tp.get("所屬街廓"), round(float(tp.get("分攤登記面積_m2", 0) or 0), 4))
        if k in nm and nm[k] != tp.get("暫編地號"):
            amb.setdefault(k, {nm[k]}).add(tp.get("暫編地號"))
        nm[k] = tp.get("暫編地號")
    P("  名稱解析鍵 `(街廓, a_m2)`：相異 ＝ **%d**；**歧義鍵 ＝ %d**（逐項具名）" % (len(nm), len(amb)))
    for k, v in sorted(amb.items()):
        P("     🩸 歧義 `%s` a_m2=%.4f ⇒ %s" % (k[0], k[1], "／".join(sorted(v))))
    for c in CAP:
        k = (c["lbl"], round(float(c["kw"].get("a_m2", 0) or 0), 4))
        c["name"] = None if k in amb else nm.get(k)
    unres = [c for c in CAP if c["name"] is None]
    P("  捕獲 ＝ %d；已解析 ＝ **%d**；未解析 ＝ **%d**（皆因上開歧義鍵）"
      % (len(CAP), len(CAP) - len(unres), len(unres)))
    bad = sorted({c["lbl"] for c in unres} & {"R1", "R2", "R5"})
    if bad:
        stop("名稱", "本批受詞之街廓 `%s` 有捕獲未能解析 ⇒ ⛔ 不得續辦" % "／".join(bad))
        return finish(log_path, H_BEFORE)
    P("  ✅ 未解析者**全數落在 `%s`** ⇒ ⛔ 不在本批受詞（`R1`／`R2`／`R5`）內。"
      % "／".join(sorted({c["lbl"] for c in unres})) if unres else
      "  ✅ 無未解析者。")

    # ── §二　`side` 是否為鏈鍵 ──────────────────────────────────────────────
    hdr("【§二】`side` kwarg 之值分佈——⛔ 是否可作鏈鍵？")
    dist = collections.Counter(str(c["kw"].get("side")) for c in CAP)
    P("  `side` 值分佈 ＝ %s" % dict(dist))
    P("  ⇒ 非街角宗恆為 `無` ⇒ **`side` 僅標街角宗、⛔ 不得用以分鏈**"
      if dist.get("無", 0) > 0 else "  ⇒ 分佈與預期不同（具名）")
    P("  ⛔ **會使本判為否之輸入**：若 `side` 之相異值數 ≥ 鏈數且逐鏈一一對應，則可作鏈鍵。")
    # 🔒 模態詞「非街角宗**恆**為 `無`」之**反例搜尋**（`驗收 9`）
    ct = collections.Counter((bool(c["kw"].get("is_corner")), str(c["kw"].get("side")))
                             for c in CAP)
    P("")
    P("  🔒 **模態詞之反例搜尋**：斷言「非街角宗**恆**為 `無`」⇒ 反例 ＝ `is_corner=False` 而 `side≠無`。")
    P("     交叉表 `(is_corner, side)` ＝ %s" % dict(ct))
    ce = sum(v for (ic, sd), v in ct.items() if (not ic) and sd != "無")
    ce2 = sum(v for (ic, sd), v in ct.items() if ic and sd == "無")
    P("     ⇒ **反例（`is_corner=False` ∧ `side≠無`）＝ %d**；"
      "併查（`is_corner=True` ∧ `side＝無`）＝ %d" % (ce, ce2))
    P("     ⇒ 該模態斷言於本母體（%d 次捕獲）%s"
      % (len(CAP), "**成立**（反例 0）" if ce == 0 else "🔴 **不成立**（有反例）"))

    # ── §三　真鏈之還原 ────────────────────────────────────────────────────
    hdr("【§三】真鏈之構造性還原（`W_prev == 0` ⇒ 起新鏈；否則 `W_prev[k] == W_far[k-1]`）")
    chains, broken = [], []
    cur = None
    for c in CAP:
        wp = float(c["kw"].get("W_prev", 0.0) or 0.0)
        if abs(wp) <= EPS:
            cur = {"lbl": c["lbl"], "items": [c]}
            chains.append(cur)
        else:
            if cur is not None and cur["lbl"] == c["lbl"] \
                    and abs(wp - cur["items"][-1]["W_far"]) <= EPS:
                cur["items"].append(c)
            else:
                broken.append((c, None if cur is None else cur["items"][-1]["W_far"]))
                cur = {"lbl": c["lbl"], "items": [c], "_broken": True}
                chains.append(cur)
    # 🩸 命名：⛔ 不得與 §五 之 `multi`（`(街廓,宗)→捕獲`）同名——首版同名致 §七 取錯物
    multi_chains = [ch for ch in chains if len(ch["items"]) > 1]
    P("  鏈 母體 ＝ **%d** 組（其中**多元素鏈 ＝ %d** 組·singleton ＝ %d 組）；"
      "**接不上者 ＝ %d**（逐項具名）" % (len(chains), len(multi_chains), len(chains) - len(multi_chains),
                                        len(broken)))
    for c, prev in broken:
        P("     🔴 seq=%d lbl=`%s` name=`%s` W_prev=%.6f 前一 W_far=%s"
          % (c["seq"], c["lbl"], c["name"], c["kw"].get("W_prev", 0), prev))
    bad_chain = sorted({c["lbl"] for c, _p in broken})
    if broken:
        P("")
        P("  🔴 **發現：還原規則⛔ 非普遍成立**——接不上者**全數落在 `%s`**。"
          % "／".join(bad_chain))
        P("     現象：同一宗以**同一 `W_prev`** 被反覆呼叫而 `W_far` 遞增"
          "（如 `628-53(1)`：`7.20→7.20`／`7.20→7.30`／`7.20→7.50`／`7.20→7.70`）。")
        P("     🩸 **成因未查明·⛔ 不臆造**；本批**只認定其為還原規則之射程限制**。")
        P("     ⛔ **會使本判為否之輸入**：該六次之 `W_prev` 等於其前一次之 `W_far`。")
    scope = {"R1", "R2", "R5"}
    if set(bad_chain) & scope:
        stop("鏈", "本批受詞之街廓 `%s` 有呼叫接不上真鏈 ⇒ ⛔ 不得續辦"
             % "／".join(sorted(set(bad_chain) & scope)))
        return finish(log_path, H_BEFORE)
    if broken:
        P("  ✅ 接不上者⛔ 不在本批受詞（`R1`／`R2`／`R5`）內 ⇒ 續辦，惟上開限制須逐字出艙。")
    P("")
    P("  逐組（⛔ 全列）：")
    for i, ch in enumerate(chains, 1):
        P("     #%-2d `%s`  n=%-2d  %s" % (i, ch["lbl"], len(ch["items"]),
            " → ".join("%s[%.2f→%.2f]" % (it["name"], it["kw"].get("W_prev", 0), it["W_far"])
                       for it in ch["items"])))
    P("  POPULATION=%d PRINTED=%d SUPPRESSED=0  # 鏈（全列）" % (len(chains), len(chains)))

    # ── §四　singleton 宗 ──────────────────────────────────────────────────
    hdr("【§四】**singleton 宗**（`W_prev ≡ 0` 且 `W_far ≡ 0` ⇒ ⛔ 不在任何鏈上）")
    P("  %-4s %-8s %-8s %s" % ("街廓", "在鏈宗", "singleton", "singleton 名單（⛔ 全列）"))
    SING = {}
    for lbl in sorted({c["lbl"] for c in CAP}):
        chs = [ch for ch in chains if ch["lbl"] == lbl]
        # 🔒 `R3` 之歧義鍵使部分 `name` ＝ `None` ⇒ 排序前須濾除並**具名其數**
        _sg = {ch["items"][0]["name"] for ch in chs
               if len(ch["items"]) == 1 and abs(ch["items"][0]["W_far"]) <= EPS}
        _ic = {it["name"] for ch in chs if len(ch["items"]) > 1 for it in ch["items"]}
        n_none = sum(1 for x in _sg | _ic if x is None)
        single = sorted(x for x in _sg if x is not None)
        inchain = sorted(x for x in _ic if x is not None)
        if n_none:
            P("  🩸 `%s` 有 **%d** 個未解析名稱（`R3` 歧義鍵）⇒ 已自上表濾除並具名" % (lbl, n_none))
        P("  %-4s %-8d %-8d %s" % (lbl, len(inchain), len(single), "、".join(single) or "（無）"))
        SING[lbl] = single

    # ── §五　`R1` 之二趟換鏈 ────────────────────────────────────────────────
    hdr("【§五】`R1`：同一宗被呼叫多次 ⇒ **換鏈**（`G` 隨之異）")
    P("  🔒 判準：同 `(街廓, 宗)` 之捕獲次數 > 1。**⛔ 會使本判為否之輸入**：每宗恰 1 次。")
    multi = collections.defaultdict(list)
    for c in CAP:
        multi[(c["lbl"], c["name"])].append(c)
    mm = {k: v for k, v in multi.items() if len(v) > 1}
    difG = {k: v for k, v in mm.items()
            if max(x["G"] for x in v) - min(x["G"] for x in v) > 1e-9}
    P("  被呼叫 > 1 次之 `(街廓, 宗)` ＝ **%d**；其中**跨次 `G` 相異者 ＝ %d**（＝真正之換鏈）"
      % (len(mm), len(difG)))
    P("  🔒 排序鍵對 `None` 名稱以 `\"\"` 代之（`R3` 歧義鍵）·⛔ 不因排序而丟列。")
    P("")
    P("  **跨次 `G` 相異者（⛔ 全列）**：")
    for (lbl, name), v in sorted(difG.items(), key=lambda kv: (kv[0][0], kv[0][1] or "")):
        P("     `%s`｜`%s`：%d 次 ⇒ %s" % (lbl, name, len(v),
            "、".join("seq=%d W_prev=%.2f→W_far=%.2f G=%.4f"
                      % (x["seq"], x["kw"].get("W_prev", 0), x["W_far"], x["G"]) for x in v)))
        P("        🔒 **定案值 ＝ 末次呼叫** ⇒ `G ＝ %.4f`" % v[-1]["G"])
    P("  POPULATION=%d PRINTED=%d SUPPRESSED=%d  # 跨次 G 相異者（全列）"
      % (len(difG), len(difG), 0))
    P("  ⚠️ 其餘 **%d** 組雖被多次呼叫而 `G` 逐次相同 ⇒ ⛔ 非換鏈、不列。" % (len(mm) - len(difG)))
    FINAL_G = {}
    for (lbl, name), v in multi.items():
        FINAL_G[(lbl, name)] = v[-1]["G"]

    # ── §六　遞補鏈（重推被踢除宗·⛔ 不自 log 讀）─────────────────────────────
    hdr("【§六】被踢除宗之重推（`ordered_v2` ＋ 藍影門檻·⛔ 未自 log 讀取）")
    wins = WINS.get("wins") or {}
    KICK = {}
    for lbl in ("R2", "R5"):
        C = CELL.get(lbl)
        st1 = [t for t in build_p
               if t.get("所屬街廓") == lbl and not t.get("_is_ghost_sliver", False)
               and "配地階段" not in t]
        fl = FL.get(lbl) or {}
        w = wins.get(lbl) or {}
        ordered = SOP2(parcels_in_block=st1, d_hat=None, front_line_p1=fl["p1"],
                       front_line_p2=fl["p2"], pk_winners=w, forced_offset={})["ordered"]
        seq = [e["tp"]["暫編地號"] for e in ordered]
        if w.get("p2_end") and not w.get("p1_end"):
            seq = list(reversed(seq))
        i2 = {C["lots"][i]["name"]: i for i in C["lots"]}
        curs, kicked = list(seq), []
        while len(curs) >= 2:
            j0, j1 = i2[curs[0]], i2[curs[1]]
            ba = blue_area(C, j0, j1)
            g1 = FINAL_G.get((lbl, curs[1],))
            if ba is None or g1 is None:
                stop("重推", "`%s` 之藍影或 `G` 取不到 ⇒ ⛔ 不得自造替代式" % lbl)
                break
            if g1 < ba:
                kicked.append((curs[1], g1))
                curs = [curs[0]] + curs[2:]
            else:
                break
        KICK[lbl] = kicked
        P("  `%s` 被踢除宗（重推）＝ %s｜`Σ被踢除G` ＝ **%.4f ㎡**"
          % (lbl, "、".join("`%s`(%.4f)" % (a, b) for a, b in kicked) or "（無）",
             sum(b for _a, b in kicked)))

    # ── §七　忠實重播（沿真鏈）────────────────────────────────────────────────
    hdr("【§七】🔒 **忠實重播**：沿**真鏈**剔除被踢除宗後重串 `W_prev`")
    def replay_chain(items, drop):
        """🔒 重播直接用**該次捕獲之 `kw`**（⛔ 不經名稱查表）；僅 `W_prev` 沿鏈重串。"""
        out, wp = [], 0.0
        for it in items:
            if it["name"] in drop:
                continue
            k2 = dict(it["kw"])
            k2["W_prev"] = wp
            res, _l = orig_solve(**k2)
            g = float(res.get("G", float("nan")))
            out.append((it["name"], wp, float(it["kw"].get("W_prev", 0) or 0),
                        FINAL_G[(it["lbl"], it["name"])], g))
            wp = float(res.get("W_far", wp))
        return out

    # 🔒 **只取末趟之鏈**（⛔ 否則重複計算）
    #   🩸 首版把同街廓之**兩趟**鏈都重播並累加 ⇒ `R2` 得 `ΣΔ=1.52`（＝2×0.76）、
    #      `R5` 得 `0.54`（＝2×0.27）；`R1` 更以**第一趟**之鏈對**末次** `G` 相比而得 `+9.30`。
    #   ⇒ 判準：鏈之**每一項皆為該 `(街廓, 宗)` 之末次呼叫**者，方為末趟。
    lastseq = {}
    for c in CAP:
        k = (c["lbl"], c["name"])
        lastseq[k] = max(lastseq.get(k, -1), c["seq"])

    def is_final_chain(ch):
        return all(it["seq"] == lastseq[(it["lbl"], it["name"])] for it in ch["items"])

    P("  🔒 **末趟過濾**：多元素鏈 %d 組 ⇒ 末趟 **%d** 組（⛔ 其餘為前趟·不得累加）"
      % (len(multi_chains), sum(1 for ch in multi_chains if is_final_chain(ch))))
    for ch in multi_chains:
        P("     %-4s n=%-2d %-6s %s"
          % (ch["lbl"], len(ch["items"]),
             "**末趟**" if is_final_chain(ch) else "前趟",
             " → ".join(it["name"] or "?" for it in ch["items"])))
    P("")
    P("  %-4s %-16s %-12s %-12s %-12s %-12s %s"
      % ("街廓", "宗", "W_prev舊", "W_prev新", "G_舊", "G_新", "Δ"))
    tot_d = tot_k = 0.0
    per = {}
    for lbl in ("R2", "R5"):
        drop = {a for a, _b in KICK[lbl]}
        chs = [ch for ch in chains
               if ch["lbl"] == lbl and len(ch["items"]) > 1 and is_final_chain(ch)]
        d_sum = 0.0
        for ch in chs:
            for name, wpn, wpo, go, gn in replay_chain(ch["items"], drop):
                d = gn - go
                d_sum += d
                P("  %-4s %-16s %-12.4f %-12.4f %-12.4f %-12.4f %+.6f"
                  % (lbl, name, wpo, wpn, go, gn, d))
        k_sum = sum(b for _a, b in KICK[lbl])
        per[lbl] = (k_sum, d_sum, k_sum - d_sum)
        tot_d += d_sum
        tot_k += k_sum
        P("     ⇒ `%s`：`Σ被踢除G` ＝ %.4f｜`ΣΔ` ＝ %+.4f｜**池增量 ＝ %.4f ㎡**"
          % (lbl, k_sum, d_sum, k_sum - d_sum))
    P("")
    P("  🔒 **合計：`Σ被踢除G` ＝ %.4f｜`ΣΔ` ＝ %+.4f｜池增量 ＝ `%.4f ㎡`**"
      % (tot_k, tot_d, tot_k - tot_d))

    # ── §八　`R1` 之忠實重播（否證 56.4000）──────────────────────────────────
    hdr("【§八】🔒 `R1` 之忠實重播（**實跑**·⛔ 非以「應為 0」推論）⇒ 否證 `56.4000`")
    r1d = 0.0
    for ch in [ch for ch in chains if ch["lbl"] == "R1"
               and len(ch["items"]) > 1 and is_final_chain(ch)]:
        for name, wpn, wpo, go, gn in replay_chain(ch["items"], set()):
            d = gn - go
            r1d += d
            P("  `R1` %-16s W_prev 舊=%-10.4f 新=%-10.4f  G_舊=%-11.4f G_新=%-11.4f Δ=%+.6f"
              % (name, wpo, wpn, go, gn, d))
    P("")
    P("  🔒 **`R1` 忠實重播之 `ΣΔ` ＝ %+.6f**（`-99` 之單鏈重播得 `+27.6800`）" % r1d)
    if abs(r1d) <= 1e-9:
        P("  ⇒ `56.4000 ㎡` 之 `27.6800` **係鏈壓縮之偽項** ⇒ **否證**；甲／乙二射程之對立不成立。")
    else:
        stop("R1", "`R1` 忠實重播之 `ΣΔ` ＝ %+.6f ≠ 0 ⇒ 否證未成立（逐字具名）" % r1d)

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
    P("     ⇒ ⛔ 不在本檔任一母體內（母體皆為捕獲／鏈／宗·⛔ 非檔案母體）。")
    P("  🔒 **⛔ 未讀任何既有 log**：本檔之數皆由本次執行之 `_solve_G_one` 捕獲現算。")
    P("")
    if STOPS:
        P("  🛑 **本批之停機（逐字具名·`rc` 恆 `0`）**：")
        for t, x in STOPS:
            P("     停機 %s：%s" % (t, x))
    else:
        P("  ✅ 本檔未觸任一停機條件。")
    os.makedirs(OUTDIR, exist_ok=True)
    with open(log_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(L) + "\n")
    print("")
    print("log -> %s" % os.path.relpath(log_path, REPO).replace(os.sep, "/"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
