# -*- coding: utf-8 -*-
r"""`W-G.9-99 補正③ v2`：**名稱鍵之射程**——`(街廓, a_m2)` 代理鍵之二處污染。

## 受詞（⛔ 二項皆非土地結論）

`補正②` 之**三項核心結果**（`ΣΔ`／`Σ被踢除G`／池增量／`R1 ΣΔ`）**不動**；
本檔只正其**附帶計數表**之二處，二者根因同一 ＝ **代理鍵**：

1. `§三` 表「跨次 `G` 相異者（全倉 ＝ `4` 組）」之第 2 列 ＝ 代理鍵**偽項**（真 `3`／代理 `5`）。
2. `§四`／`VR-055 三·依據` 之「末趟 `5`」＝ 代理鍵之 `None` 名稱使 `lastseq` 塌縮（真值 `6`）。

## 🔒 資料源 ＝ **本檔實跑管線之捕獲**

⛔ 未 import `probe_WG999c_true_chain.py`、⛔ 未解析其 log。
名稱**改自 caller frame** 取 `tp['暫編地號']`／`blk_label`（⛔ 非 `(街廓, a_m2)` 代理鍵）；
街廓標籤由**驅動迴圈自持**（⛔ 不層疊 `run_step_g`）。

## 二鍵並跑（同一批捕獲·**只換鍵**）

- **精確** ＝ `(blk_label, 暫編地號)`（caller frame）。
- **代理** ＝ `(blk_label, round(a_m2, 2))`；**一鍵對到 > 1 真名者其名解為 `None`**（＝ 既有探針之行為）。

## 預測值之出處（`fixture-provenance`）

`P-1`〜`P-14` 之期望值**逐項引自施工單** `W-G.9-99 補正③ v2` `§2-2`
（⛔ 非由本檔現跑一次回填）。停機②〜⑦ 亦逐字引自該單 `§二`。

## 重跑

    python verify/probes/probe_WG9100_keyscope.py

`rc` **恆 `0`**；停機以**逐字具名**表示。
log 落 `verify/out/probe_WG9100_keyscope_<基座短碼>.log`（檔名綁**基座**·考古節 `122`）。
"""
import collections
import contextlib
import io
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
sys.path.insert(0, VERIFY)
sys.path.insert(0, HERE)

import numpy as np                                                  # noqa: E402

from app_harvest import harvest                                     # noqa: E402
import run_verification as rv                                       # noqa: E402
from selection_pipeline import run_corner_pk                        # noqa: E402
from stepg_pipeline import run_step_g                               # noqa: E402

import probe_WG992_blue as w92                                      # noqa: E402
import probe_WG940_startperp as w40                                 # noqa: E402

OUTDIR = os.path.join(VERIFY, "out")
BASE_REF = "84bb7a6"
WIDTH = 112
EPS = 1e-9
SB = 0.0
FBACK_MAX = 6

PROD_FILES = ["app.py", "verify/stepg_pipeline.py", "verify/selection_pipeline.py",
              "verify/run_verification.py", "verify/wd4_tier_list.py",
              "verify/wf_f0.py", "verify/wf_f1.py", "verify/wf_f2.py",
              "verify/wf_f3.py", "verify/wf_f4.py"]

SELF = ["verify/probes/probe_WG9100_keyscope.py",
        "verify/out/probe_WG9100_keyscope_%s.log" % BASE_REF,
        "docs/reports/W-G.9-99_乙之遞補鏈shim.md（【三度更正】段）",
        "docs/驗證裁定登記表.md（`VR-056`）",
        "docs/reports/W-G.9波_claude.ai側自誤登記.md（自誤 `112`／`113`／`114`）"]

# ── 施工單 `§2-2` 之預測值（⛔ 非本檔現跑回填）────────────────────────────────
EXP_CAP = 124
EXP_KW = ["A", "B", "C", "F", "S_max", "W_prev", "a_m2", "allocation_dir",
          "avg_depth", "baseline_pt", "blk_poly", "d_hat", "is_corner",
          "l_front", "l_side", "near_dir", "side", "side_mid", "tab6_burden"]
EXP_PER_BLK = {"R1": 10, "R2": 30, "R4": 4, "R6": 28, "R5": 24, "R3": 28}
EXP_JIA = (73, 14, 59, 6)
EXP_YI = (67, 12, 55, 5)
EXP_BROKEN_SEQ = [53, 54, 55, 67, 68, 69]
EXP_FORCED_MULTI = [(55, 57), (69, 71)]
EXP_FORCED_SING = [53, 54, 67, 68]
EXP_R3 = {"628-28(1)": 114.00, "628-29(1)": 114.00,
          "628-47(1)": 246.00, "628-48(1)": 246.00}
EXP_DIF_EX = {("R1", "628-36(1)"), ("R5", "628-21(2)"), ("R6", "628-53(1)")}
EXP_KEYPOP = (59, 57)
EXP_DIF_PX_N = 5
EXP_F_EX = {("R1", 5, 6), ("R1", 7, 9), ("R2", 25, 32),
            ("R3", 117, 123), ("R5", 84, 90), ("R6", 69, 71)}
EXP_F_PX = EXP_F_EX - {("R3", 117, 123)}
EXP_F_YI = EXP_F_EX - {("R6", 69, 71)}
EXP_KICK = {"R2": [("628-42(1)", 3.82), ("628-27(1)", 29.08)],
            "R5": [("628-53(2)", 0.99), ("628-45(1)", 51.22)]}
EXP_SUMK, EXP_SUMD, EXP_POOL = 85.1100, 1.030000, 84.0800
EXP_PER = {"R2": (0.760000, 32.1400), "R5": (0.270000, 51.9400)}
EXP_R1D = 0.0
EXP_CT = {(True, "左側"): 8, (False, "無"): 108, (True, "右側"): 8}

L, STOPS, SKIPPED = [], [], []
CAP, RAISES = [], []
CURBLK = {"lbl": None}


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


def skipped(tag, text):
    SKIPPED.append((tag, text))
    P("  ⚠️ **略過 %s**：%s（⛔ 不計為證據·亦⛔ 不計為反證）" % (tag, text))


def judge(got, exp, note=""):
    ok = got == exp
    return "%s 實得 %s ｜ 預測 %s%s" % ("✅" if ok else "🛑", got, exp,
                                       ("　%s" % note) if note else ""), ok


def git1(a):
    return subprocess.run(["git"] + a, cwd=REPO, capture_output=True,
                          check=True).stdout.decode("utf-8").strip()


def prod_hashes():
    return {f: git1(["hash-object", f]) for f in PROD_FILES}


def make_spy(orig):
    """🔒 全捕 spy：`19` kwarg ＋ `res` ＋ 呼叫序；名稱沿 `f_back` 上溯（上限 `FBACK_MAX` 層）。"""
    def _f(**kw):
        res, lab = orig(**kw)
        nm = blk = None
        depth = None
        fr = sys._getframe()
        for d in range(1, FBACK_MAX + 1):
            fr = fr.f_back
            if fr is None:
                break
            tp = fr.f_locals.get("tp")
            if isinstance(tp, dict) and "暫編地號" in tp:
                nm = tp["暫編地號"]
                blk = fr.f_locals.get("blk_label")
                depth = d
                break
        CAP.append({"seq": len(CAP), "drv": CURBLK["lbl"], "lbl": blk, "name": nm,
                    "depth": depth, "kw": dict(kw),
                    "G": float(res.get("G", float("nan"))),
                    "W_far": float(res.get("W_far", float("nan")))})
        return res, lab
    return _f


def proxy_key(c):
    """🔒 代理鍵 ＝ `(blk_label, round(a_m2, 2))`（施工單 `§2-1`）。"""
    return (c["lbl"], round(float(c["kw"].get("a_m2", 0) or 0), 2))


def blue_area(C, j0, j1):
    """🔒 藍影（⛔ 不重造）：`_halfplane`＠`probe_WG992_blue.py`。"""
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


def drive():
    """🔒 §2-1 之驅動序（`SB = 0.0`）；街廓標籤由**本迴圈自持**、⛔ 不層疊 `run_step_g`。"""
    ns, fst = harvest()
    snap = rv.load_snapshot()
    o_solve = ns["_solve_G_one"]
    cb_by, cad = rv.build_pipeline(ns, fst, snap)
    rv.build_ownership(ns, fst, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp_p, build_p, _sw = rv.build_build_parcels(
        ns, fst, v6, list(cb_by.values()), snap)
    cb_all = list(cb_by.values())
    blks = []
    for tp in build_p:
        _l = tp.get("所屬街廓")
        if _l and _l not in blks:
            blks.append(_l)
    params = rv.build_param_table(ns, fst, cb_by, cad, snap, SB)
    _d0, _s2, _o2, wins, forced = run_corner_pk(
        ns, fst, cb_all, cad, params, temp_p, build_p, SB, snapshot=snap)
    spy = make_spy(o_solve)
    ns["_solve_G_one"] = spy
    try:
        for lbl in blks:
            CURBLK["lbl"] = lbl
            with contextlib.redirect_stdout(io.StringIO()):
                try:
                    run_step_g(ns, fst, cb_all, cad, snap, params,
                               [t for t in build_p if t.get("所屬街廓") == lbl],
                               wins, forced, SB)
                except Exception as e:                               # noqa: BLE001
                    RAISES.append((lbl, str(e)))
            CURBLK["lbl"] = None
    finally:
        ns["_solve_G_one"] = o_solve
    restored = ns["_solve_G_one"] is o_solve
    fl = (fst.session_state.get("f3_cad_front_lines") or {}) or (cad.get("front_lines") or {})
    return {"ns": ns, "o_solve": o_solve, "build_p": build_p, "wins": wins,
            "FL": fl, "SOP2": ns["_spatial_order_parcels_v2"],
            "restored": restored, "spy_obj": spy, "blks": blks}


def build_chains():
    """真鏈還原（`W_prev == 0` ⇒ 起新鏈；否則 `W_prev[k] == W_far[k-1]`）。"""
    chains, broken, cur = [], [], None
    for c in CAP:
        wp = float(c["kw"].get("W_prev", 0.0) or 0.0)
        if abs(wp) <= EPS:
            cur = {"lbl": c["lbl"], "items": [c], "brk": False}
            chains.append(cur)
        elif cur is not None and cur["lbl"] == c["lbl"] \
                and abs(wp - cur["items"][-1]["W_far"]) <= EPS:
            cur["items"].append(c)
        else:
            broken.append(c)
            cur = {"lbl": c["lbl"], "items": [c], "brk": True}
            chains.append(cur)
    return chains, broken


def chain_id(ch):
    return (ch["lbl"], ch["items"][0]["seq"], ch["items"][-1]["seq"])


def lastseq_by(keyf):
    d = {}
    for c in CAP:
        k = keyf(c)
        d[k] = max(d.get(k, -1), c["seq"])
    return d


def finals(multi, ls, keyf):
    """🔒 **同一 `is_final_chain` 定式**（`it["seq"] == lastseq[key(it)]`）·只換鍵。"""
    return {chain_id(ch) for ch in multi
            if all(it["seq"] == ls[keyf(it)] for it in ch["items"])}


def main():                                                          # noqa: C901
    log_path = os.path.join(OUTDIR, "probe_WG9100_keyscope_%s.log" % BASE_REF)
    H_BEFORE = prod_hashes()

    hdr("【W-G.9-99 補正③ v2】代理鍵之射程（⛔ 零生產碼·🔒 實跑管線·⛔ 不讀任何 log）")
    P("  基座（log 檔名所綁）＝ **%s**" % BASE_REF)
    P("  HEAD ＝ %s；`app.py` blob ＝ %s"
      % (git1(["rev-parse", "HEAD"]), git1(["rev-parse", "HEAD:app.py"])))
    P("  🔒 **資料源 ＝ 本次執行之捕獲**；⛔ 未 import `probe_WG999c_true_chain.py`、⛔ 未解析其 log。")
    P("  🔒 **預測值出處 ＝ 施工單 `W-G.9-99 補正③ v2` `§2-2`**（⛔ 非本檔現跑回填）。")

    with contextlib.redirect_stdout(io.StringIO()):
        D = drive()
        CELL, _REAL = w92.build()
    o_solve, build_p = D["o_solve"], D["build_p"]

    # ── §一　驅動與捕獲（`P-1`〜`P-5`）──────────────────────────────────────
    hdr("【§一】驅動與捕獲（`P-1`〜`P-5`）")
    P("  執行期層疊之還原：`ns['_solve_G_one'] is 原物` ＝ **%s**（`finally` 還原·逐位比對）"
      % D["restored"])
    if not D["restored"]:
        stop("①", "`ns['_solve_G_one']` 未還原為原物 ⇒ 零生產碼宣稱不成立")
    txt, ok = judge(len(CAP), EXP_CAP)
    P("  `P-1`　捕獲次數：%s" % txt)
    if not ok:
        stop("②", "`P-1` 捕獲 ＝ %d ≠ %d ⇒ ⛔ 不得續辦" % (len(CAP), EXP_CAP))
        return finish(log_path, H_BEFORE)

    n_bad = sum(1 for c in CAP if c["name"] is None)
    n_same = sum(1 for c in CAP if c["lbl"] == c["drv"])
    dep = dict(collections.Counter(c["depth"] for c in CAP))
    P("  `P-2`　名稱解析失敗 ＝ **%d**（預測 `0`）；"
      "caller `blk_label` ＝ 驅動迴圈標籤 ＝ **%d／%d**（預測 `124／124`）"
      % (n_bad, n_same, len(CAP)))
    P("        `f_back` 上溯深度分佈 ＝ %s（上限 %d 層）" % (dep, FBACK_MAX))
    if n_bad > 0 or n_same != len(CAP):
        stop("③", "`P-2` 解析失敗 ＝ %d、`blk_label` 相同 ＝ %d／%d ⇒ ⛔ 不得續辦"
             % (n_bad, n_same, len(CAP)))
        return finish(log_path, H_BEFORE)

    ks = sorted(CAP[0]["kw"].keys())
    txt, ok = judge(len(ks), len(EXP_KW), "鍵集相同 ＝ %s" % (ks == EXP_KW))
    P("  `P-3`　kwarg 鍵數：%s" % txt)
    P("        %s" % " ".join(ks))
    per = dict(collections.Counter(c["drv"] for c in CAP))
    txt, ok = judge(per, EXP_PER_BLK)
    P("  `P-4`　每街廓捕獲：%s" % txt)
    P("  `P-5`　`raise`（`try/except` 收·逐項全列）：")
    for lbl, msg in RAISES:
        P("        `%s`：%s" % (lbl, msg.replace("\n", " ")[:170]))
    P("        POPULATION=%d PRINTED=%d SUPPRESSED=0  # raise（全列）"
      % (len(RAISES), len(RAISES)))

    # ── 二鍵並跑 ──────────────────────────────────────────────────────────
    pxn = collections.defaultdict(set)
    for c in CAP:
        pxn[proxy_key(c)].add(c["name"])
    PX = {k: (list(v)[0] if len(v) == 1 else None) for k, v in pxn.items()}
    for c in CAP:
        c["pname"] = PX[proxy_key(c)]
    keypop = (len({(c["lbl"], c["name"]) for c in CAP}), len({proxy_key(c) for c in CAP}))
    amb = sorted(k for k, v in pxn.items() if len(v) > 1)

    # ── §二　鏈（`P-6`〜`P-8`）─────────────────────────────────────────────
    hdr("【§二】真鏈之還原 ＋ **二口徑具名**（`P-6`〜`P-8`）")
    chains, broken = build_chains()
    A_multi = [ch for ch in chains if len(ch["items"]) > 1]
    B_ch = [ch for ch in chains if not ch["brk"]]
    B_multi = [ch for ch in B_ch if len(ch["items"]) > 1]
    LS_EX = lastseq_by(lambda c: (c["lbl"], c["name"]))
    LS_PX = lastseq_by(lambda c: (c["lbl"], c["pname"]))
    F_ex = finals(A_multi, LS_EX, lambda c: (c["lbl"], c["name"]))
    F_px = finals(A_multi, LS_PX, lambda c: (c["lbl"], c["pname"]))
    F_yi = finals(B_multi, LS_EX, lambda c: (c["lbl"], c["name"]))
    jia = (len(chains), len(A_multi), len(chains) - len(A_multi), len(F_ex))
    yi = (len(B_ch), len(B_multi), len(B_ch) - len(B_multi), len(F_yi))
    txt, ok6a = judge(jia, EXP_JIA)
    P("  `P-6`　甲（接不上起鏈者**計入**）母體／多元素／singleton／末趟：%s" % txt)
    txt, ok6b = judge(yi, EXP_YI)
    P("  　　　乙（**不計入**）母體／多元素／singleton／末趟：%s" % txt)
    bseq = [c["seq"] for c in broken]
    blbl = sorted({c["lbl"] for c in broken})
    txt, ok7a = judge(bseq, EXP_BROKEN_SEQ, "街廓 ＝ %s" % blbl)
    P("  `P-7`　接不上（`seq`）：%s" % txt)
    fb = [ch for ch in chains if ch["brk"]]
    fm = [(ch["items"][0]["seq"], ch["items"][-1]["seq"]) for ch in fb if len(ch["items"]) > 1]
    fs = [ch["items"][0]["seq"] for ch in fb if len(ch["items"]) == 1]
    txt, ok7b = judge((len(fb), fm, fs), (6, EXP_FORCED_MULTI, EXP_FORCED_SING))
    P("  　　　強制起鏈者（組數／多元素／singleton）：%s" % txt)
    P("  `P-8`　多元素鏈 **%d** 組（⛔ 全列·二鍵之末趟旗標並陳）：" % len(A_multi))
    P("        %-4s %-4s %-11s %-9s %-9s %s" % ("街廓", "n", "seq", "精確鍵", "代理鍵", "起因"))
    for ch in A_multi:
        cid = chain_id(ch)
        P("        %-4s %-4d %-11s %-9s %-9s %s"
          % (cid[0], len(ch["items"]), "%d–%d" % (cid[1], cid[2]),
             "**末趟**" if cid in F_ex else "前趟",
             "**末趟**" if cid in F_px else "前趟",
             "接不上" if ch["brk"] else "`W_prev`＝0"))
    P("        POPULATION=%d PRINTED=%d SUPPRESSED=0  # 多元素鏈（全列）"
      % (len(A_multi), len(A_multi)))

    # ── §三　`R3` 四宗（`P-9`）────────────────────────────────────────────
    hdr("【§三】更正一之被檢物：`R3` 四宗（`P-9`）——代理鍵之 `8` 次實為**四宗各二次**")
    P("  代理鍵歧義（一鍵 > 1 真名·逐項具名）：")
    for k in amb:
        P("        `%s` a_m2=%.2f ⇒ %s" % (k[0], k[1], "／".join(sorted(pxn[k]))))
    r3 = collections.defaultdict(list)
    for c in CAP:
        if c["lbl"] == "R3":
            r3[c["name"]].append(c)
    ok9 = True
    P("        %-14s %-10s %-26s %s" % ("宗", "a_m2", "G 逐次", "相異值數"))
    for n, a in sorted(EXP_R3.items()):
        v = r3.get(n, [])
        nd = len({round(x["G"], 9) for x in v})
        ok9 = ok9 and (nd == 1) and (abs(float(v[0]["kw"]["a_m2"]) - a) <= 5e-3)
        P("        %-14s %-10.2f %-26s %d"
          % ("`%s`" % n, float(v[0]["kw"]["a_m2"]),
             ", ".join("%.2f" % x["G"] for x in v), nd))
    P("  `P-9`　四宗之相異值數**各 `1`** ＝ %s ⇒ %s" % (ok9, "✅" if ok9 else "🛑"))
    P("  ⛔ **會使本判為否之輸入**：該四宗中任一宗其逐次 `G` 之相異值數 `> 1`。")

    # ── §四　判別力對照甲（`P-10`）────────────────────────────────────────
    hdr("【§四】🔒 判別力對照**甲**（跨次 `G` 相異·同一批捕獲·**只換鍵**）（`P-10`）")

    def difG(keyf):
        g = collections.defaultdict(list)
        for c in CAP:
            g[keyf(c)].append(c["G"])
        return {k: v for k, v in g.items() if max(v) - min(v) > 1e-9}

    d_ex = difG(lambda c: (c["lbl"], c["name"]))
    d_px = difG(proxy_key)
    d_pn = difG(lambda c: (c["lbl"], c["pname"]))
    txt, ok10a = judge(keypop, EXP_KEYPOP,
                       "差 ＝ %d ＝ 代理鍵歧義組數 %d ⇒ 歸因閉合 ＝ %s"
                       % (keypop[0] - keypop[1], len(amb),
                          keypop[0] - keypop[1] == len(amb)))
    P("  鍵母體（精確／代理）：%s" % txt)
    txt, ok10b = judge(set(d_ex), EXP_DIF_EX)
    P("  `P-10` 精確鍵之跨次 `G` 相異：%s" % txt)
    txt, ok10c = judge(len(d_px), EXP_DIF_PX_N, "＝ %s" % sorted(d_px))
    P("  　　　 代理鍵之跨次 `G` 相異：%s" % txt)
    P("  　　　 併呈：代理**名**（歧義⇒`None`）之組數 ＝ **%d**（＝ `補正②` 所載之 `4`·"
      "係把代理鍵之 `R3` **二**組併寫為**一**列）" % len(d_pn))
    pert10 = len(d_px) - len(d_ex)
    P("  🔒 **擾動量 ＝ %d 組**（代理 %d − 精確 %d）" % (pert10, len(d_px), len(d_ex)))
    if pert10 == 0:
        skipped("⑥／對照甲", "對照甲之擾動量 ＝ 0（對照退化）")

    # ── §五　判別力對照乙・丙（`P-11`／`P-12`）─────────────────────────────
    hdr("【§五】🔒 判別力對照**乙**（末趟·甲口徑·同一 `is_final_chain` 定式·只換鍵）（`P-11`）")
    txt, ok11a = judge(sorted(F_ex), sorted(EXP_F_EX))
    P("  精確鍵末趟集（`街廓, 首 seq, 末 seq`）：%s" % txt)
    txt, ok11b = judge(sorted(F_px), sorted(EXP_F_PX))
    P("  代理鍵末趟集：%s" % txt)
    P("  🔒 差集（精確 − 代理）＝ %s；**擾動量 ＝ %d 組**"
      % (sorted(F_ex - F_px), len(F_ex - F_px)))
    if len(F_ex - F_px) == 0:
        skipped("⑥／對照乙", "對照乙之擾動量 ＝ 0（對照退化）")
    P("  🔒 **機制（逐字）**：`is_final_chain` 之判準 ＝ `it[\"seq\"] == lastseq[(lbl, name)]`；"
      "代理鍵於 `R3` 四宗皆解為 `None` ⇒ `lastseq[(\"R3\", None)]` 取全體 `None` 之最大 `seq`")
    P("        ⇒ `R3` 末趟鏈（`seq 117–123`）含二個 `None` 名 ⇒ **整條鏈被誤判為前趟** ⇒ 末趟由 `6` 降為 `5`。")
    P("  ⛔ **會使本判為否之輸入**：以精確鍵重跑而 `(R3, 117, 123)` 仍被判前趟。")

    hdr("【§五-2】🔒 對照**丙**：否證「口徑混用」之歸因（`P-12`·自誤 `113`）")
    txt, ok12a = judge(sorted(F_yi), sorted(EXP_F_YI))
    P("  「不計接不上」口徑之**精確**末趟集：%s" % txt)
    same = (F_px == F_yi)
    P("  🔒 二集合之**計數**：代理 ＝ %d／不計接不上 ＝ %d（**同**）；"
      "**集合相等 ＝ %s**（預測 `False`）" % (len(F_px), len(F_yi), same))
    P("        代理集缺 ＝ %s；不計接不上集缺 ＝ %s"
      % (sorted(F_ex - F_px), sorted(F_ex - F_yi)))
    P("  ⇒ **計數同而集合相異** ⇒ 口徑⛔ **非**成因（`自誤 113` 之否證成立）。")
    if same:
        stop("⑦", "`P-12` 之布林為 `True`（二集合相同）⇒ `E1` 之否證不成立 ⇒ 上呈發單側")

    ok4 = all([ok6a, ok6b, ok7a, ok7b, ok9, ok10a, ok10b, ok10c, ok11a, ok11b, ok12a])
    if not ok4:
        stop("④", "`P-6`〜`P-12` 有與預測不符者（逐格見上）⇒ ⛔ 不改被檢物去湊")

    # ── §六　三項核心之不動確認（`P-13`）──────────────────────────────────
    hdr("【§六】🔒 三項核心結果之**不動確認**（`P-13`·⛔ 土地數字）")
    FINAL_G = {}
    mm = collections.defaultdict(list)
    for c in CAP:
        mm[(c["lbl"], c["name"])].append(c)
    for k, v in mm.items():
        FINAL_G[k] = v[-1]["G"]
    KICK = {}
    for lbl in ("R2", "R5"):
        C = CELL[lbl]
        st1 = [t for t in build_p if t.get("所屬街廓") == lbl
               and not t.get("_is_ghost_sliver", False) and "配地階段" not in t]
        fl = D["FL"].get(lbl) or {}
        w = (D["wins"].get(lbl) or {})
        ordered = D["SOP2"](parcels_in_block=st1, d_hat=None,
                            front_line_p1=fl["p1"], front_line_p2=fl["p2"],
                            pk_winners=w, forced_offset={})["ordered"]
        seq = [e["tp"]["暫編地號"] for e in ordered]
        if w.get("p2_end") and not w.get("p1_end"):
            seq = list(reversed(seq))
        i2 = {C["lots"][i]["name"]: i for i in C["lots"]}
        curs, kicked = list(seq), []
        while len(curs) >= 2:
            ba = blue_area(C, i2[curs[0]], i2[curs[1]])
            g1 = FINAL_G.get((lbl, curs[1]))
            if ba is None or g1 is None:
                stop("重推", "`%s` 之藍影或 `G` 取不到 ⇒ ⛔ 不得自造替代式" % lbl)
                break
            if g1 < ba:
                kicked.append((curs[1], round(g1, 4)))
                curs = [curs[0]] + curs[2:]
            else:
                break
        KICK[lbl] = kicked
        P("  `%s` 被踢除宗（重推）＝ %s" % (lbl, kicked))

    def replay(items, drop):
        out, wp = [], 0.0
        for it in items:
            if it["name"] in drop:
                continue
            k2 = dict(it["kw"])
            k2["W_prev"] = wp
            res, _l = o_solve(**k2)
            g = float(res.get("G", float("nan")))
            out.append((it["name"], FINAL_G[(it["lbl"], it["name"])], g))
            wp = float(res.get("W_far", wp))
        return out

    tot_d = tot_k = 0.0
    ok13 = True
    for lbl in ("R2", "R5"):
        drop = {a for a, _b in KICK[lbl]}
        chs = [ch for ch in A_multi if ch["lbl"] == lbl and chain_id(ch) in F_ex]
        ds = sum(gn - go for ch in chs for _n, go, gn in replay(ch["items"], drop))
        ksum = sum(b for _a, b in KICK[lbl])
        tot_d += ds
        tot_k += ksum
        e_d, e_p = EXP_PER[lbl]
        good = (abs(ds - e_d) <= 5e-5 and abs((ksum - ds) - e_p) <= 5e-5
                and KICK[lbl] == EXP_KICK[lbl])
        ok13 = ok13 and good
        P("  %s `%s`：`Σ被踢除G` ＝ %.4f｜`ΣΔ` ＝ %+.6f（預測 %+.6f）｜"
          "**池增量 ＝ %.4f ㎡**（預測 %.4f）"
          % ("✅" if good else "🛑", lbl, ksum, ds, e_d, ksum - ds, e_p))
    g_all = (abs(tot_k - EXP_SUMK) <= 5e-5 and abs(tot_d - EXP_SUMD) <= 5e-5
             and abs((tot_k - tot_d) - EXP_POOL) <= 5e-5)
    ok13 = ok13 and g_all
    P("  %s 合計：`Σ被踢除G` ＝ **%.4f**（預測 %.4f）｜`ΣΔ` ＝ **%+.6f**（預測 %+.6f）｜"
      "**池增量 ＝ `%.4f ㎡`**（預測 %.4f）"
      % ("✅" if g_all else "🛑", tot_k, EXP_SUMK, tot_d, EXP_SUMD,
         tot_k - tot_d, EXP_POOL))
    r1d = sum(gn - go for ch in A_multi if ch["lbl"] == "R1" and chain_id(ch) in F_ex
              for _n, go, gn in replay(ch["items"], set()))
    g_r1 = abs(r1d - EXP_R1D) <= 1e-9
    ok13 = ok13 and g_r1
    P("  %s `R1` 忠實重播 `ΣΔ` ＝ **%+.6f**（預測 %+.6f）"
      % ("✅" if g_r1 else "🛑", r1d, EXP_R1D))
    P("  🔒 出艙稱謂（`VR-054 三`）：池增量 `%.4f ㎡` 係**依守恆式導出·⛔ 非幾何實量**。"
      % (tot_k - tot_d))
    if not ok13:
        stop("⑤", "`P-13` 有與預測不符之**土地數字** ⇒ **立即停機並上呈 KL**·⛔ 不得自行續辦")

    # ── §七　模態斷言之反例（`P-14`）──────────────────────────────────────
    hdr("【§七】模態斷言之反例搜尋（`P-14`）")
    ct = collections.Counter((bool(c["kw"].get("is_corner")), str(c["kw"].get("side")))
                             for c in CAP)
    txt, ok14 = judge(dict(ct), EXP_CT)
    P("  `(is_corner, side)` 交叉表：%s" % txt)
    ce = sum(v for (ic, sd), v in ct.items() if (not ic) and sd != "無")
    P("  ⇒ 反例（`is_corner=False` ∧ `side≠無`）＝ **%d**（預測 `0`）" % ce)
    if not ok14:
        stop("④", "`P-14` 之交叉表與預測不符")

    return finish(log_path, H_BEFORE)


def finish(log_path, H_BEFORE):
    hdr("【§八】收工：生產檔 hash 前後對拍・`SELF` 自扣・停機逐字")
    H_AFTER = prod_hashes()
    same = [f for f in PROD_FILES if H_BEFORE.get(f) == H_AFTER.get(f)]
    P("  10 支生產檔 `git hash-object` 出艙前後**逐位相同** ＝ **%d／%d** ⇒ %s"
      % (len(same), len(PROD_FILES),
         "✅ 零生產碼變更" if len(same) == len(PROD_FILES) else "🔴"))
    for f in PROD_FILES:
        P("     %-34s %s %s" % (f, H_BEFORE.get(f),
                                "✅" if H_BEFORE.get(f) == H_AFTER.get(f)
                                else "🔴 → %s" % H_AFTER.get(f)))
    if len(same) != len(PROD_FILES):
        stop("①", "生產檔 hash 前後不同 ⇒ 「零生產碼」宣稱**不成立**")
    P("")
    P("  🔒 **`SELF` 自扣**：本批產物 ＝ **%d** 檔／段：" % len(SELF))
    for s in SELF:
        P("     `%s`" % s)
    P("     ⇒ ⛔ 不在本檔任一母體內（母體皆為捕獲／鏈／宗·⛔ 非檔案母體）。")
    P("  🔒 **⛔ 未讀任何既有 log**：本檔之數皆由本次執行之 `_solve_G_one` 捕獲現算。")
    P("")
    if SKIPPED:
        P("  ⚠️ **本批之略過（對照退化·⛔ 不計為證據亦不計為反證）**：")
        for t, x in SKIPPED:
            P("     略過 %s：%s" % (t, x))
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
