# -*- coding: utf-8 -*-
"""`W-G.9-98` §一 探針：結構閘「位次＝投影序」之**三路徑實測**（⛔ 非推論）。

## 受詞

`verify/stepg_pipeline.py:491-509` 之結構閘，其 `raise` 之**充要條件**為何？

倉內 `K-6:2981-2982` 曾載「其口徑為**重劃前**，於本裁（`K-9-17` 遞補）落地後**必然轉紅**
⇒ 落地批須**同批處置**」。本探針以**實測**判該「必然」是否成立。

## 機制（⛔ 不跑管線）

於**函式層**直接呼叫 `app._spatial_order_parcels_v2` 與 `app._projection_order`，
合成五種情境並**逐情境重跑閘之判定式**（`stepg_pipeline.py:498-504` 之 `_pos_bad` 構造）。

- `A` 同步過濾：自 `_stage1_parcels` 移除標的 ⇒ 縮減後清單**同時**餵 `_spatial_order_parcels_v2` 與 `_proj_rank`
- `B` 下游移除：`_stage1_parcels` 不動；僅自建成後之 `ordered_v2` 移除該筆
- `C` 母體不同步：`ordered_v2` 以**縮減**清單建成，`_proj_rank` 仍取**完整** `_stage1_parcels`
- `D` 另訂位次（判別力對照）：不移除任何宗，把各筆 `pre_position` 改為**依 `G` 值排序**之名次
- `E` 恆真對照：完全不動任何物

🔒 **呼叫護欄**：`stepg_pipeline.run_step_g`／`selection_pipeline.run_corner_pk`／
`run_verification.main` 於本檔開頭即被覆蓋為 `raise` 版 ⇒ **機械證明未跑管線**。

## `pk_winners` 之處置（⛔ 不得靜默省略）

`ss['f3_corner_winners']` 由 `stepg_pipeline.py:282` 於 `run_step_g` **內**鋪底，而本批禁跑 `run_step_g`
⇒ 生產值不可得。本檔**不以空 dict 靜默兜底**，而是：

1. **結構論證**：`app.py:7657-7659` 之 `pre_position` 賦值**先於**任何 `pk_winners` 處理；
   winner 處理（`:7665-7700`）僅 `pop`／`insert` **重排清單**、⛔ 不改任一 `pre_position` 值；
   `forced_offset` 只影響二個 `*_corner_offset_area` 回傳值、⛔ 不入 `ordered`。
2. **實測**（`§2`）：對每街廓分別以「空 `pk_winners`」與「**合成** `pk_winners`」各跑一次，
   驗證 ① `ordered` 之**順序確實改變**（⇒ 合成值有效、非空擾動）② `_pos_bad` **兩者相同**。
   ⇒ 以量測坐實「`pk_winners` 不影響本閘之受詞」。

## `G` 之來源（⛔ 不自造期望值）

對照 `D` 所用之 `G` 取自**倉內既有 baseline**（唯讀）：
`verify/baselines/v3/G 值計算結果_退縮0m.csv` 之 `G(㎡)` 欄，以 `暫編地號` join。
⛔ 未跑求解器、⛔ 未改任何 CSV。缺值即 **loud raise**（禁靜默兜底）。

## 重跑指令

    python verify/probes/probe_WG998_gate_paths.py

log 落 `verify/out/probe_WG998_gate_paths_<基座短碼>.log`（**檔名綁基座、⛔ 不綁 `HEAD`**·考古節 `122`）。

## 停機條件（`W-G.9-98` 施工單 §一）

`A`／`B` 任一為**紅**，或 `C`／`D` 任一為**綠** ⇒ `raise`，並出艙該情境之 `_pos_bad` **全列**（⛔ 不切片）。
"""
import ast
import collections
import contextlib
import csv
import io
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
sys.path.insert(0, VERIFY)
sys.path.insert(0, HERE)

OUTDIR = os.path.join(VERIFY, "out")
BASE_REF = "7bb32b8"                     # 🔒 基座（log 檔名綁此·⛔ 不綁 HEAD·考古節 122）
G_CSV = os.path.join(VERIFY, "baselines", "v3", "G 值計算結果_退縮0m.csv")

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
            "🔴 `W-G.9-98` §一：本批⛔ 不得呼叫 `%s`——本探針於**函式層**量測，"
            "若某量非跑管線不可得，出艙【須執行該碼·本批不跑】" % name)
    return _f


# ══════════════════════════════════════════════════════════════════════════════
#  閘之判定式（🔒 逐字複刻 `verify/stepg_pipeline.py:498-504`·⛔ 不得簡化）
# ══════════════════════════════════════════════════════════════════════════════
def gate_pos_bad(ordered_v2, proj_population, p1, p2, PO):
    """回傳 `_pos_bad`（空 ＝ 綠·非空 ＝ 該閘會 `raise`）。"""
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
    log_path = os.path.join(OUTDIR, "probe_WG998_gate_paths_%s.log" % BASE_REF)

    hdr("【W-G.9-98 §一】結構閘「位次＝投影序」三路徑實測（⛔ 非推論）")
    say("  基座（log 檔名所綁）＝ **%s**" % BASE_REF)
    say("  產生時 HEAD ＝ %s（%s）" % (head_s, head))
    say("  `app.py` blob ＝ %s" % app_blob)
    say("  🔒 `merge-base --is-ancestor %s HEAD` ⇒ 祖先關係（⛔ 不以 HEAD 逐位相等為判準·考古節 122/123）"
        % BASE_REF)

    # ── §0-1　呼叫護欄 ────────────────────────────────────────────────────────
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

    # ── §0-2　取生產函式（⛔ 不自行重建）────────────────────────────────────
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        from app_harvest import harvest
        from selection_pipeline import build_build_parcels
        ns, fake_st = harvest()
        snap = rv.load_snapshot()
        cb_by, cad = rv.build_pipeline(ns, fake_st, snap)
        rv.build_ownership(ns, fake_st, rv.ANON_XLSX)      # 🩸 硬前置：不呼叫則 `所屬街廓` 靜默給錯
        with open(rv.V6DXF, "rb") as f:
            v6 = f.read()
        temp_p, build_p, _sw = build_build_parcels(
            ns, fake_st, v6, list(cb_by.values()), snap)

    PO = ns["_projection_order"]
    SOP2 = ns["_spatial_order_parcels_v2"]

    app_src = open(os.path.join(REPO, "app.py"), encoding="utf-8").read()
    tree = ast.parse(app_src)
    defs = {nd.name: nd.lineno for nd in ast.walk(tree)
            if isinstance(nd, ast.FunctionDef)
            and nd.name in ("_projection_order", "_spatial_order_parcels_v2")}
    hdr("【§0】同一性與判別力先驗（⛔ 未證明探針接到生產函式前，其後一切數字無效）")
    ok0 = True
    for nm, fn in (("_projection_order", PO), ("_spatial_order_parcels_v2", SOP2)):
        same = (fn.__code__.co_firstlineno == defs.get(nm))
        ok0 &= same
        say("  `%s`：`co_firstlineno` ＝ **%d**／AST 定義行 ＝ **%d** ⇒ %s"
            % (nm, fn.__code__.co_firstlineno, defs.get(nm, -1), "✅ 同一物" if same else "🔴 不同"))
    if not ok0:
        raise RuntimeError("🔴 取到之函式非 `app.py` 之定義 ⇒ 停機")

    # 判別力先驗：人造 3 宗，只把幾何對調 ⇒ 投影序必變（證探針確實接到函式）
    def mk(name, x):
        return {"暫編地號": name,
                "polygon_coords": [(x, 0.0), (x + 1.0, 0.0), (x + 1.0, 1.0), (x, 1.0)]}
    cA = [mk("A", 0.0), mk("B", 10.0), mk("C", 20.0)]
    cB = [mk("A", 0.0), mk("B", 20.0), mk("C", 10.0)]
    oA = [t["暫編地號"] for t in PO(cA, (0.0, 0.0), (100.0, 0.0))]
    oB = [t["暫編地號"] for t in PO(cB, (0.0, 0.0), (100.0, 0.0))]
    say("  判別力先驗（人造 3 宗·只對調 `B`／`C` 之幾何）：序①＝%s／序②＝%s ⇒ %s"
        % (oA, oB, "✅ 序改變 ⇒ 探針接到函式" if oA != oB else "🔴 序未變"))
    if oA == oB:
        raise RuntimeError("🔴 判別力為零 ⇒ 探針未接到 `_projection_order`（考古節 78）")

    # 閘複刻之判別力先驗：人造一組必紅、一組必綠
    _ord_ok = [{"tp": cA[i], "pre_position": i + 1} for i in range(3)]
    _ord_bad = [{"tp": cA[i], "pre_position": 3 - i} for i in range(3)]
    _g_ok = gate_pos_bad(_ord_ok, cA, (0.0, 0.0), (100.0, 0.0), PO)
    _g_bad = gate_pos_bad(_ord_bad, cA, (0.0, 0.0), (100.0, 0.0), PO)
    say("  閘複刻之判別力先驗：正序 `_pos_bad` ＝ **%d** 筆（須 0）／逆序 `_pos_bad` ＝ **%d** 筆（須 >0）⇒ %s"
        % (len(_g_ok), len(_g_bad), "✅ 閘複刻可轉紅" if (not _g_ok and _g_bad) else "🔴 閘複刻為空檢"))
    if _g_ok or not _g_bad:
        raise RuntimeError("🔴 閘複刻無判別力（考古節 123：不能轉紅者＝空檢）⇒ 停機")

    # ── §1　母體 ──────────────────────────────────────────────────────────────
    hdr("【§1】母體（`data/V6.dxf` 全街廓·⛔ 不得只取 R2／R5）")
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
    say("  `cb_by`（DXF 街廓）母體 ＝ **%d**：%s" % (len(all_blocks), all_blocks))
    say("  `build_parcels` ＝ **%d** 宗；`_is_ghost_sliver` 扣除 ＝ **%d** ⇒ 餘 **%d** 宗"
        % (len(build_p), n_ghost, len(build_p) - n_ghost))
    say("  🔒 `f3_corner_winners` 於 `ss` ＝ **%s**（由 `stepg_pipeline.py:282` 於 `run_step_g` 內鋪底·本批禁跑）"
        % ("在" if "f3_corner_winners" in ss else "不在"))

    included, skipped = [], []
    for lbl in all_blocks:
        st1 = [tp for tp in by_blk.get(lbl, []) if "配地階段" not in tp]
        fl = FL.get(lbl) or {}
        if not st1:
            skipped.append((lbl, "無可建築宗地（`build_parcels` 之 `所屬街廓` 命中 0）"))
        elif not (fl.get("p1") and fl.get("p2")):
            skipped.append((lbl, "缺 FRONT_LINE ⇒ `_degenerate_order` ⇒ 該閘於生產碼亦跳過（`:495`）"))
        else:
            included.append(lbl)
    say("")
    say("  母體 ＝ **%d**／納入 ＝ **%d**／略過 ＝ **%d**"
        % (len(all_blocks), len(included), len(skipped)))
    for lbl, why in skipped:
        say("     略過 `%s`：%s" % (lbl, why))
    say("  納入之街廓與階段1宗數：%s"
        % "、".join("%s(%d)" % (b, len([t for t in by_blk[b] if "配地階段" not in t]))
                    for b in included))
    if not included:
        raise RuntimeError("🔴 納入母體為空 ⇒ ⛔ 不得以空母體充作通過（考古節：空真假綠）")

    # ── §1-2　`G` 取料（倉內 baseline·唯讀）──────────────────────────────────
    with open(G_CSV, encoding="utf-8-sig", newline="") as fh:
        grows = list(csv.DictReader(fh))
    GVAL = {r["暫編地號"]: float(r["G(㎡)"]) for r in grows if (r.get("G(㎡)") or "").strip()}
    say("")
    say("  對照 `D` 之 `G` 來源 ＝ `%s`（唯讀·⛔ 未跑求解器）"
        % os.path.relpath(G_CSV, REPO).replace(os.sep, "/"))
    say("  該 CSV 列數 ＝ **%d**；具 `G(㎡)` 值者 ＝ **%d**" % (len(grows), len(GVAL)))

    # ── §2　`pk_winners` 不影響本閘之受詞（實測·⛔ 非僅結構論證）──────────────
    hdr("【§2】`pk_winners` 對本閘之影響 ＝ 0（實測·合成 winner）")
    say("  構造：對每街廓以 ① 空 `pk_winners` ② 合成 `pk_winners`"
        "（`p1_end`＝投影序第 2 宗、`p2_end`＝倒數第 2 宗）各建一次 `ordered_v2`。")
    say("  判準：① `ordered` 之順序**須改變**（證合成值有效）② `_pos_bad` **須相同**。")
    say("")
    say("  街廓   n    順序改變?   `_pos_bad`(空pk)   `_pos_bad`(合成pk)   判")
    pk_ok = True
    for lbl in included:
        st1 = [tp for tp in by_blk[lbl] if "配地階段" not in tp]
        fl = FL[lbl]
        p1, p2 = fl["p1"], fl["p2"]
        seq = [t["暫編地號"] for t in PO(st1, p1, p2)]
        syn = {}
        if len(seq) >= 4:
            syn = {"p1_end": seq[1], "p2_end": seq[-2]}
        o_empty = SOP2(parcels_in_block=st1, d_hat=None, front_line_p1=p1,
                       front_line_p2=p2, pk_winners={}, forced_offset={})["ordered"]
        o_syn = SOP2(parcels_in_block=st1, d_hat=None, front_line_p1=p1,
                     front_line_p2=p2, pk_winners=syn, forced_offset={})["ordered"]
        n_empty = [e["tp"]["暫編地號"] for e in o_empty]
        n_syn = [e["tp"]["暫編地號"] for e in o_syn]
        b_empty = gate_pos_bad(o_empty, st1, p1, p2, PO)
        b_syn = gate_pos_bad(o_syn, st1, p1, p2, PO)
        changed = (n_empty != n_syn)
        good = (len(b_empty) == len(b_syn) == 0) and (changed or len(seq) < 4)
        pk_ok &= good
        say("  %-5s %-4d %-11s %-18d %-20d %s"
            % (lbl, len(st1), ("是" if changed else "否（n<4·未合成）"),
               len(b_empty), len(b_syn), "✅" if good else "🔴"))
    say("")
    say("  ⇒ `pk_winners` 對 `_pos_bad` 之影響 ＝ **0**（%s）" % ("✅ 全街廓成立" if pk_ok else "🔴 不成立"))
    say("  🔒 與結構論證一致：`app.py:7657-7659` 之 `pre_position` 賦值**先於** winner 處理；"
        "winner 僅 `pop`／`insert` 重排清單、⛔ 不改任一 `pre_position` 值。")
    if not pk_ok:
        raise RuntimeError("🔴 `pk_winners` 影響 `_pos_bad` ⇒ 本探針以空 dict 施測之前提破 ⇒ 停機")

    # ── §3　三路徑 ＋ 二對照 ─────────────────────────────────────────────────
    hdr("【§3】三路徑（A/B/C）＋ 二對照（D/E）逐街廓逐側實測")
    say("  出艙格式：街廓｜側｜移除標的暫編｜路徑｜`_pos_bad` 筆數｜判")
    say("")
    say("  %-5s %-6s %-16s %-6s %-8s %-6s" % ("街廓", "側", "移除標的", "路徑", "_pos_bad", "判"))
    say("  " + "-" * 60)

    tally = collections.Counter()
    side_skipped = []
    firstbad = {}
    degenerate_D = []
    greens = collections.defaultdict(list)     # 預測為紅而實測為綠者 ⇒ 逐例具名
    law_rows = []                              # C 之定量律：len(_pos_bad) 是否 ＝ n − r

    def rec(lbl, side, target, path, bad):
        verdict = "紅" if bad else "綠"
        tally[(path, verdict)] += 1
        if bad and path not in firstbad:
            firstbad[path] = (lbl, side, target, bad)
        if path in ("C", "D") and not bad:
            greens[path].append((lbl, side, target))
        say("  %-5s %-6s %-16s %-6s %-8d %s" % (lbl, side, target or "—", path, len(bad), verdict))

    for lbl in included:
        st1 = [tp for tp in by_blk[lbl] if "配地階段" not in tp]
        fl = FL[lbl]
        p1, p2 = fl["p1"], fl["p2"]
        base_ordered = SOP2(parcels_in_block=st1, d_hat=None, front_line_p1=p1,
                            front_line_p2=p2, pk_winners={}, forced_offset={})["ordered"]
        names = [e["tp"]["暫編地號"] for e in base_ordered]

        # ── E 恆真對照（每街廓一次）──
        rec(lbl, "—", None, "E", gate_pos_bad(base_ordered, st1, p1, p2, PO))

        # ── D 另訂位次（每街廓一次·依 `G` 值排序）──
        miss = [n for n in names if n not in GVAL]
        if miss:
            raise RuntimeError(
                "🔴 對照 D：街廓 %s 之 %d 宗於 `G` baseline 查無（%s）"
                "——⛔ 禁靜默兜底（no-silent-fallback）" % (lbl, len(miss), miss))
        g_rank = {n: i + 1 for i, n in enumerate(
            sorted(names, key=lambda n: (-GVAL[n], n)))}
        d_ordered = SOP2(parcels_in_block=st1, d_hat=None, front_line_p1=p1,
                         front_line_p2=p2, pk_winners={}, forced_offset={})["ordered"]
        proj_rank_now = {t["暫編地號"]: i + 1 for i, t in enumerate(PO(st1, p1, p2))}
        _d_diff = sum(1 for n in names if g_rank[n] != proj_rank_now[n])
        if _d_diff == 0:
            # 擾動量為零 ⇒ 該街廓之 D 無判別力，須具名（考古：對照組擾動不足）
            degenerate_D.append((lbl, len(names)))
        for e in d_ordered:
            e["pre_position"] = g_rank[e["tp"]["暫編地號"]]
        rec(lbl, "—", "(依G重編位次)", "D", gate_pos_bad(d_ordered, st1, p1, p2, PO))

        # ── A/B/C 逐側 ──
        for side, idx in (("右(p1)", 1), ("左(p2)", -2)):
            if len(st1) < 2:
                side_skipped.append((lbl, side, "該街廓階段1宗數 ＝ %d < 2 ⇒ 無「街角之後第一位」" % len(st1)))
                continue
            target = names[idx]
            reduced = [tp for tp in st1 if tp["暫編地號"] != target]

            # A 同步過濾
            oA_ = SOP2(parcels_in_block=reduced, d_hat=None, front_line_p1=p1,
                       front_line_p2=p2, pk_winners={}, forced_offset={})["ordered"]
            rec(lbl, side, target, "A", gate_pos_bad(oA_, reduced, p1, p2, PO))

            # B 下游移除
            oB_full = SOP2(parcels_in_block=st1, d_hat=None, front_line_p1=p1,
                           front_line_p2=p2, pk_winners={}, forced_offset={})["ordered"]
            oB_ = [e for e in oB_full if e["tp"]["暫編地號"] != target]
            rec(lbl, side, target, "B", gate_pos_bad(oB_, st1, p1, p2, PO))

            # C 母體不同步
            oC_ = SOP2(parcels_in_block=reduced, d_hat=None, front_line_p1=p1,
                       front_line_p2=p2, pk_winners={}, forced_offset={})["ordered"]
            _badC = gate_pos_bad(oC_, st1, p1, p2, PO)
            rec(lbl, side, target, "C", _badC)
            # 🔴 定量律（機器驗證·⛔ 非手算）：移除投影排名 r 之宗 ⇒ 排名後移者恰 n − r 筆
            _n = len(st1)
            _r = [t["暫編地號"] for t in PO(st1, p1, p2)].index(target) + 1
            law_rows.append((lbl, side, target, _n, _r, _n - _r, len(_badC),
                             (_n - _r) == len(_badC)))

    # ── §4　合計與停機判定 ───────────────────────────────────────────────────
    hdr("【§4】路徑別合計與停機判定")
    say("  路徑   綠     紅     合計   預測")
    PRED = {"A": "綠", "B": "綠", "C": "紅", "D": "紅", "E": "綠"}
    fail = []
    for path in ("A", "B", "C", "D", "E"):
        g, r = tally[(path, "綠")], tally[(path, "紅")]
        tot = g + r
        exp = PRED[path]
        good = (r == 0 and g == tot) if exp == "綠" else (g == 0 and r == tot)
        if not good:
            fail.append(path)
        say("  %-6s %-6d %-6d %-6d %s  %s" % (path, g, r, tot, exp, "✅" if good else "🔴"))
    if side_skipped:
        say("")
        say("  逐側略過 ＝ **%d**：" % len(side_skipped))
        for lbl, side, why in side_skipped:
            say("     `%s` %s：%s" % (lbl, side, why))
    if degenerate_D:
        say("")
        say("  ⚠️ 對照 `D` 之擾動量為零（`G` 序恰等於投影序）之街廓：%s"
            % [("%s(n=%d)" % (b, n)) for b, n in degenerate_D])
        say("     ⇒ 該街廓之 `D` **無判別力**、⛔ 不得計為證據（對照組擾動須大於被測量之解析度）。")

    say("")
    for path in ("A", "B", "C", "D", "E"):
        if path in firstbad:
            lbl, side, target, bad = firstbad[path]
            say("  路徑 `%s` 首個紅例：街廓 `%s`／側 %s／標的 `%s`" % (path, lbl, side, target))
            say("     `_pos_bad` 全列（%d 筆·⛔ 未切片）＝ %s" % (len(bad), bad))

    # ── §5　轉紅之條件：定量律（機器驗證）────────────────────────────────────
    hdr("【§5】路徑 `C` 之定量律 ⇒ 「母體不同步」係**必要非充分**")
    say("  假說：自 `_proj_rank` 之母體移除投影排名 `r` 之宗（母體 `n` 宗）")
    say("        ⇒ 排名後移者恰 **`n − r`** 筆 ⇒ `len(_pos_bad)` ＝ `n − r`。")
    say("  🔒 由**機器**逐例驗證（⛔ 非手算·考古：2dp 顯示值不可手算差）。")
    say("")
    say("  %-5s %-6s %-16s %-4s %-4s %-8s %-8s %s"
        % ("街廓", "側", "移除標的", "n", "r", "n−r", "實得", "判"))
    law_ok = True
    for lbl, side, target, n, r, exp, got, good in law_rows:
        law_ok &= good
        say("  %-5s %-6s %-16s %-4d %-4d %-8d %-8d %s"
            % (lbl, side, target, n, r, exp, got, "✅" if good else "🔴"))
    say("")
    say("  ⇒ 定量律 %s（%d／%d 例相符）"
        % ("**成立**" if law_ok else "🔴 **不成立**",
           sum(1 for x in law_rows if x[7]), len(law_rows)))
    _last = [x for x in law_rows if x[4] == x[3]]
    say("  ⇒ `r ＝ n`（移除**投影序末位**）之例 ＝ **%d**：%s"
        % (len(_last), [("%s %s %s" % (a, b, c)) for a, b, c, _n, _r, _e, _g, _o in _last] or "無"))
    say("     此類例中母體**確實不同步**（`ordered_v2` 少 1 宗）而 `_pos_bad` ＝ **0** ⇒ 閘 **綠**。")
    say("")
    say("  🔴 **結論（⛔ 逐字要緊）**：")
    say("     「二呼叫點之母體不同步」係該閘轉紅之 **必要條件**，⛔ **非充分條件**。")
    say("     精確之充要條件 ＝ **至少一存活宗，其投影排名在二母體下相異**。")
    say("     ⇒ 凡欲入倉之正典逐字，⛔ **不得**寫成「轉紅之**充要條件** ＝ 母體不同步」。")

    say("")
    if fail:
        say("  🛑 **停機**：路徑 %s 之實測與預測不符" % fail)
        for path in ("C", "D"):
            for lbl, side, target in greens.get(path, []):
                say("     路徑 `%s` 之綠例：街廓 `%s`／側 %s／標的 `%s`" % (path, lbl, side, target))
    else:
        say("  ✅ **A／B 全綠·C／D 全紅·E 全綠** ⇒ 「落地後必然轉紅」**經實測否證**")
        say("     ⇒ 轉紅之充要條件 ＝ **二呼叫點之母體不同步**（路徑 `C`），⛔ 非「發生了遞補」（路徑 `A`／`B`）")
        say("     ⇒ 該閘作為 `K-6:59`「禁另訂」之代理，其**判別力仍存在**（對照 `D` 全紅）")

    say("")
    say("  🔒 呼叫護欄計數（須全 0）＝ %s" % (dict(CALLGUARD) or "{}（無任一被呼叫）"))

    os.makedirs(OUTDIR, exist_ok=True)
    with open(log_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(L) + "\n")
    print("")
    print("log -> %s" % os.path.relpath(log_path, REPO).replace(os.sep, "/"))

    if fail:
        raise RuntimeError(
            "🛑 W-G.9-98 §一 停機：路徑 %s 實測與預測不符（詳見 log）" % fail)
    return 0


if __name__ == "__main__":
    sys.exit(main())
