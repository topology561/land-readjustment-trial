# -*- coding: utf-8 -*-
"""`W-G.9-98 補正①` §一 探針：正向對照 `D′`（**保證擾動**）。

## 存在理由

`W-G.9-98` §一 之正向對照 `D`（把 `pre_position` 改吃 `G` 值降冪名次）於街廓 `R4`
**退化為恆真**（`G` 降冪序恰 ≡ 投影序 ⇒ 擾動量 ＝ `0` ⇒ 閘綠）⇒ 觸停機。

該綠**⛔ 非**「閘失去 `K-6:59` 判別力」，而係**對照組本身無判別力**。
本檔以一個**擾動量恆 ＝ 2**、⛔ 不可能退化之正向對照 `D′` 補測，以區辨二者。

## `D′` 之構造

於各納入街廓，正常建成 `ordered_v2` 後，取 **`pre_position` ＝ `1` 與 ＝ `2`** 之二筆，
**對調其 `pre_position` 之值**（⛔ 不動 `ordered_v2` 之清單順序、⛔ 不動 `_stage1_parcels`），
再重跑閘之判定式（`verify/stepg_pipeline.py:501-504` 之 `_pos_bad` 構造·本檔逐字複刻）。

🔒 **為何用相鄰對調**：`n ≥ 2` 時擾動量**恆 ＝ `2`**，⛔ 不可能退化為恆真
——這正是對照 `D` 所缺之性質（`W-G.9-98 補正①` 自誤 `109`）。

## 機制（⛔ 不跑管線）

沿用 `W-G.9-98` 之 pipeline-free harness 與 `_forbidden` 呼叫護欄：
`stepg_pipeline.run_step_g`／`selection_pipeline.run_corner_pk`／`run_verification.main`
於本檔開頭即覆蓋為 `raise` 版 ⇒ **機械證明未跑管線**（收工印其計數須全 `0`）。

⛔ 不改任何 baseline／CSV／DXF；⛔ 不修改 `probe_WG998_gate_paths.py` 一字。
路徑全程由 `__file__` 導出（`verify/run_all.py:76` 之禁寫死絕對路徑閘）。

## 併須複核（自既有 log 逐字取值·⛔ 不得憑記憶）

`verify/out/probe_WG998_gate_paths_7bb32b8.log:121` 之「對照 `D` 擾動量為零之街廓集合」
須恰 ＝ `['R4(n=2)']`。

## 重跑指令

    python verify/probes/probe_WG998b_control_dprime.py

log 落 `verify/out/probe_WG998b_control_dprime_<基座短碼>.log`（檔名綁**基座**·考古節 `122`）。

## 停機條件（`W-G.9-98 補正①` 施工單 §一）

`D′` 任一街廓為**綠**、或擾動量 ≠ `2`、或 `_pos_bad` 筆數 ≠ `2`
⇒ `raise`；`D` 之零擾動集合 ≠ `['R4(n=2)']` ⇒ `raise`。
"""
import ast
import collections
import contextlib
import io
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
sys.path.insert(0, VERIFY)
sys.path.insert(0, HERE)

OUTDIR = os.path.join(VERIFY, "out")
BASE_REF = "c4c75ac"                     # 🔒 基座（log 檔名綁此·⛔ 不綁 HEAD·考古節 122）
PRIOR_LOG = os.path.join(OUTDIR, "probe_WG998_gate_paths_7bb32b8.log")
PRIOR_LINE = 121                         # `D` 零擾動集合所在行
PRIOR_EXPECT = "['R4(n=2)']"

WIDTH = 100
L = []
CALLGUARD = collections.Counter()


def say(s=""):
    print(s)
    L.append(s)


def hdr(s):
    say("")
    say("=" * WIDTH)
    say(s)
    say("=" * WIDTH)


def git1(args):
    return subprocess.run(["git"] + args, cwd=REPO, capture_output=True,
                          check=True).stdout.decode("utf-8").strip()


def _forbidden(name):
    def _f(*a, **kw):
        CALLGUARD[name] += 1
        raise RuntimeError(
            "🔴 `W-G.9-98 補正①` §一：本批⛔ 不得呼叫 `%s`（本探針於函式層量測）" % name)
    return _f


# ══════════════════════════════════════════════════════════════════════════════
#  閘之判定式（🔒 逐字複刻 `verify/stepg_pipeline.py:498-504`·⛔ 不得簡化）
# ══════════════════════════════════════════════════════════════════════════════
def gate_pos_bad(ordered_v2, proj_population, p1, p2, PO):
    _proj_rank = {tp['暫編地號']: _i + 1 for _i, tp in enumerate(PO(proj_population, p1, p2))}
    _pos_bad = [(e['tp']['暫編地號'], e.get('pre_position'),
                 _proj_rank.get(e['tp']['暫編地號']))
                for e in ordered_v2
                if e.get('pre_position') != _proj_rank.get(e['tp']['暫編地號'])]
    return _pos_bad


def main():                                                          # noqa: C901
    head = git1(["rev-parse", "HEAD"])
    head_s = git1(["rev-parse", "--short", "HEAD"])
    app_blob = git1(["rev-parse", "HEAD:app.py"])
    log_path = os.path.join(OUTDIR, "probe_WG998b_control_dprime_%s.log" % BASE_REF)

    hdr("【W-G.9-98 補正① §一】正向對照 `D′`（相鄰對調·擾動量恆 ＝ 2）")
    say("  基座（log 檔名所綁）＝ **%s**" % BASE_REF)
    say("  產生時 HEAD ＝ %s（%s）" % (head_s, head))
    say("  `app.py` blob ＝ %s" % app_blob)

    import stepg_pipeline as _sg
    import selection_pipeline as _sp
    import run_verification as rv
    _sg.run_step_g = _forbidden("run_step_g")
    _sp.run_corner_pk = _forbidden("run_corner_pk")
    rv.main = _forbidden("run_all_main")
    say("  🛑 **呼叫護欄已裝**：`run_step_g`／`run_corner_pk`／`run_verification.main` 皆覆蓋為 raise 版")

    import shapely                                                   # noqa: E402
    import numpy                                                     # noqa: E402
    say("  環境：shapely %s | GEOS %s | numpy %s"
        % (shapely.__version__, shapely.geos_version, numpy.__version__))

    # ── §0　既有 log 之複核（逐字取值·⛔ 不得憑記憶）──────────────────────────
    hdr("【§0】複核：`W-G.9-98` 對照 `D` 之零擾動街廓集合（自既有 log 逐字取值）")
    with open(PRIOR_LOG, encoding="utf-8") as fh:
        prior = fh.read().replace("\r\n", "\n").split("\n")
    say("  來源 ＝ `%s`（共 %d 行）"
        % (os.path.relpath(PRIOR_LOG, REPO).replace(os.sep, "/"), len(prior)))
    line = prior[PRIOR_LINE - 1]
    say("  `:%d` 逐字 ＝ %s" % (PRIOR_LINE, line.strip()))
    m = re.search(r"\[[^\]]*\]", line)
    got = m.group(0) if m else "（無法自該行抽出集合）"
    ok_prior = (got == PRIOR_EXPECT)
    say("  抽出之集合 ＝ `%s`；期望 ＝ `%s` ⇒ %s" % (got, PRIOR_EXPECT, "✅" if ok_prior else "🔴"))
    if not ok_prior:
        raise RuntimeError("🛑 `D` 之零擾動集合 ≠ %s ⇒ 停機" % PRIOR_EXPECT)

    # ── §0-2　取生產函式 ＋ 判別力先驗 ───────────────────────────────────────
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        from app_harvest import harvest
        from selection_pipeline import build_build_parcels
        ns, fake_st = harvest()
        snap = rv.load_snapshot()
        cb_by, cad = rv.build_pipeline(ns, fake_st, snap)
        rv.build_ownership(ns, fake_st, rv.ANON_XLSX)      # 🩸 硬前置：否則 `所屬街廓` 靜默給錯
        with open(rv.V6DXF, "rb") as f:
            v6 = f.read()
        temp_p, build_p, _sw = build_build_parcels(
            ns, fake_st, v6, list(cb_by.values()), snap)

    PO = ns["_projection_order"]
    SOP2 = ns["_spatial_order_parcels_v2"]
    app_src = open(os.path.join(REPO, "app.py"), encoding="utf-8").read()
    defs = {nd.name: nd.lineno for nd in ast.walk(ast.parse(app_src))
            if isinstance(nd, ast.FunctionDef)
            and nd.name in ("_projection_order", "_spatial_order_parcels_v2")}

    hdr("【§0-2】同一性與判別力先驗（⛔ 未過此關則其後數字無效）")
    ok0 = True
    for nm, fn in (("_projection_order", PO), ("_spatial_order_parcels_v2", SOP2)):
        same = (fn.__code__.co_firstlineno == defs.get(nm))
        ok0 &= same
        say("  `%s`：`co_firstlineno` ＝ **%d**／AST ＝ **%d** ⇒ %s"
            % (nm, fn.__code__.co_firstlineno, defs.get(nm, -1), "✅ 同一物" if same else "🔴 不同"))
    if not ok0:
        raise RuntimeError("🔴 取到之函式非 `app.py` 之定義 ⇒ 停機")

    def mk(name, x):
        return {"暫編地號": name,
                "polygon_coords": [(x, 0.0), (x + 1.0, 0.0), (x + 1.0, 1.0), (x, 1.0)]}
    syn = [mk("A", 0.0), mk("B", 10.0), mk("C", 20.0)]
    _ok = [{"tp": syn[i], "pre_position": i + 1} for i in range(3)]
    _bad = [{"tp": syn[0], "pre_position": 2}, {"tp": syn[1], "pre_position": 1},
            {"tp": syn[2], "pre_position": 3}]
    g_ok = gate_pos_bad(_ok, syn, (0.0, 0.0), (100.0, 0.0), PO)
    g_bad = gate_pos_bad(_bad, syn, (0.0, 0.0), (100.0, 0.0), PO)
    say("  閘複刻判別力：正序 `_pos_bad` ＝ **%d**（須 0）／**相鄰對調** ＝ **%d**（須 2）⇒ %s"
        % (len(g_ok), len(g_bad),
           "✅ 可轉紅且擾動量正是 2" if (not g_ok and len(g_bad) == 2) else "🔴 空檢或擾動量非 2"))
    if g_ok or len(g_bad) != 2:
        raise RuntimeError("🔴 閘複刻無判別力或相鄰對調之擾動量 ≠ 2 ⇒ 停機（考古節 123）")

    # ── §1　母體 ─────────────────────────────────────────────────────────────
    hdr("【§1】母體（`data/V6.dxf` 全街廓）")
    ss = fake_st.session_state
    FL = ss.get("f3_cad_front_lines") or {}
    all_blocks = sorted(cb_by.keys())
    by_blk = {}
    n_ghost = 0
    for tp in build_p:
        if tp.get("_is_ghost_sliver", False):
            n_ghost += 1
            continue
        by_blk.setdefault(tp.get("所屬街廓"), []).append(tp)
    included, skipped = [], []
    for lbl in all_blocks:
        st1 = [tp for tp in by_blk.get(lbl, []) if "配地階段" not in tp]
        fl = FL.get(lbl) or {}
        if not st1:
            skipped.append((lbl, "無可建築宗地（`build_parcels` 之 `所屬街廓` 命中 0）"))
        elif not (fl.get("p1") and fl.get("p2")):
            skipped.append((lbl, "缺 FRONT_LINE ⇒ `_degenerate_order` ⇒ 生產碼亦跳過該閘（`:495`）"))
        elif len(st1) < 2:
            skipped.append((lbl, "階段1宗數 ＝ %d < 2 ⇒ 無「排名 1 與 2」可對調" % len(st1)))
        else:
            included.append(lbl)
    say("  `cb_by`（DXF 街廓）**母體 ＝ %d**：%s" % (len(all_blocks), all_blocks))
    say("  `build_parcels` ＝ **%d** 宗；`_is_ghost_sliver` 扣除 ＝ **%d** ⇒ 餘 **%d** 宗"
        % (len(build_p), n_ghost, len(build_p) - n_ghost))
    say("  **母體 ＝ %d／納入 ＝ %d／略過 ＝ %d**" % (len(all_blocks), len(included), len(skipped)))
    for lbl, why in skipped:
        say("     略過 `%s`：%s" % (lbl, why))
    say("  🔒 **本批產物之自扣**（`§Z-8` 補款②）：本探針、其 log、本批報告**皆不在**上開母體內"
        "（母體 ＝ `cb_by` 之街廓·⛔ 非檔案母體）⇒ 量測器⛔ 未量到自身。")
    if not included:
        raise RuntimeError("🔴 納入母體為空 ⇒ ⛔ 不得以空母體充作通過")

    # ── §2　`D′` 逐街廓實測 ──────────────────────────────────────────────────
    hdr("【§2】對照 `D′` 逐街廓實測（相鄰對調 `pre_position`）")
    say("  構造：正常建成 `ordered_v2` 後，取 `pre_position` ＝ 1 與 ＝ 2 之二筆**對調其值**；")
    say("        ⛔ 不動 `ordered_v2` 清單順序、⛔ 不動 `_stage1_parcels`。")
    say("")
    say("  %-5s %-4s %-8s %-10s %s" % ("街廓", "n", "擾動量", "_pos_bad", "判"))
    say("  " + "-" * 50)
    rows = []
    allred = True
    for lbl in included:
        st1 = [tp for tp in by_blk[lbl] if "配地階段" not in tp]
        p1, p2 = FL[lbl]["p1"], FL[lbl]["p2"]
        ordered = SOP2(parcels_in_block=st1, d_hat=None, front_line_p1=p1,
                       front_line_p2=p2, pk_winners={}, forced_offset={})["ordered"]
        e1 = next((e for e in ordered if e.get("pre_position") == 1), None)
        e2 = next((e for e in ordered if e.get("pre_position") == 2), None)
        if e1 is None or e2 is None:
            raise RuntimeError(
                "🔴 街廓 %s 找不到 `pre_position` ＝ 1 或 2 之筆（實得 %s）⇒ ⛔ 禁靜默兜底"
                % (lbl, sorted(e.get("pre_position") for e in ordered)))
        before = [e.get("pre_position") for e in ordered]
        e1["pre_position"], e2["pre_position"] = 2, 1
        after = [e.get("pre_position") for e in ordered]
        perturb = sum(1 for a, b in zip(before, after) if a != b)
        bad = gate_pos_bad(ordered, st1, p1, p2, PO)
        verdict = "紅" if bad else "綠"
        allred &= bool(bad) and perturb == 2 and len(bad) == 2
        rows.append((lbl, len(st1), perturb, bad, verdict))
        say("  %-5s %-4d %-8d %-10d %s" % (lbl, len(st1), perturb, len(bad), verdict))

    say("")
    say("  逐街廓 `_pos_bad` **全列**（暫編, `pre_position`, 投影排名·⛔ 未切片）：")
    for lbl, n, perturb, bad, verdict in rows:
        say("     `%s`（n＝%d·擾動量＝%d）＝ %s" % (lbl, n, perturb, bad))

    # ── §3　判定 ─────────────────────────────────────────────────────────────
    hdr("【§3】判定")
    n_red = sum(1 for r in rows if r[4] == "紅")
    n_p2 = sum(1 for r in rows if r[2] == 2)
    n_b2 = sum(1 for r in rows if len(r[3]) == 2)
    say("  納入街廓 ＝ **%d**；紅 ＝ **%d**；擾動量 ＝ 2 者 ＝ **%d**；`_pos_bad` ＝ 2 者 ＝ **%d**"
        % (len(rows), n_red, n_p2, n_b2))
    good = (n_red == len(rows) == n_p2 == n_b2) and len(rows) > 0
    say("  預測：`6／6` 全紅·擾動量恆 2·`_pos_bad` 恆 2 ⇒ %s" % ("✅ 相符" if good else "🔴 不符"))
    say("")
    if good:
        say("  ✅ **`D′` 全紅** ⇒ 對照 `D`@`R4` 之綠係**該例之退化**（擾動量 ＝ 0），")
        say("     ⛔ **非**該閘失去 `K-6:59` 之判別力 ⇒ `W-G.9-98` §一 之停機**得以解除**。")
    else:
        say("  🛑 **停機**：`D′` 與預測不符")
    say("")
    say("  🔒 呼叫護欄計數（須全 0）＝ %s" % (dict(CALLGUARD) or "{}（無任一被呼叫）"))

    os.makedirs(OUTDIR, exist_ok=True)
    with open(log_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(L) + "\n")
    print("")
    print("log -> %s" % os.path.relpath(log_path, REPO).replace(os.sep, "/"))

    if not good:
        raise RuntimeError("🛑 `W-G.9-98 補正①` §一 停機：`D′` 實測與預測不符（詳見 log）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
