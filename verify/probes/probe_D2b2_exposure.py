# -*- coding: utf-8 -*-
r"""**D-2b-2 §一**：街廓鋪滿之**全案暴露量測**（⛔ 生產碼零觸·⛔ 不放寬生產閘）。

## 為何需要本檔

`_pool_strips_for_block` 之 ①' 覆蓋閘（`grep -n "覆蓋閘破" app.py`）以 `raise` 實作
⇒ Step-G 街廓迴圈於**第一個破格街廓**中止。`verify/out/D2b1_runall.log` 中
`街廓 R` 之出現**僅 R1**（`grep -o "街廓 R[0-9]" … | sort | uniq -c` ⇒ `6 街廓 R1`）
⇒ **R2 以後從未評估**，`12.0568㎡` 只是 R1 一格之值、**非全案暴露**。

## 手法（⛔ 探針側 shim·⛔ 不改 app.py 一字）

於 `ns` 內以 wrapper 取代 `_pool_strips_for_block`（`finally` 還原）：

1. **replica**：以**同一組** ns helper（`_strip_s_range`／`_block_strip`／`_S_EPS`）
   重跑原函式之步驟 1–5（**無閘**），得池片與 `union`。
2. **呼叫原函式**：
   - 未 raise ⇒ 回傳**原函式之輸出**（⇒ 該街廓之生產行為**逐位不變**），
     並做**正對照**：replica 之片數／面積／殘差 `==` 原函式（證 replica 忠實）。
   - raise 且訊息含 `覆蓋閘破` ⇒ 記錄 replica 殘差、回傳 replica 池片（令迴圈續行）。
   - **其他任何例外一律 re-raise** ——⛔ 只 shim 覆蓋閘、其餘閘全部保持 loud。

⇒ shim **不改任何數值**，只解除「中止」。下游所見與「該閘不存在」時**完全相同**。

## 🔒 不變量

- **反靜默退路計數**：`咬到`／`原函式通過`／`shim 吸收` 三數印出；總數 0 ⇒ **結論不可據**。
- **帶號合計與絕對值合計並列**（`CLAUDE.md` §「凡列合計」）：`Σδ` 與 `Σ|δ|`。
  δ **帶號**定義 ＝ `union − 街廓`（負 ＝ 缺地／楔形空隙；正 ＝ 溢出）。
- **殘差閘**（§一）：`Σ|δ|` 與 `Σ街廓 − Σunion`（＝ `−Σδ`）之差 ≤ 0.01。
  二者相等 ⟺ **每格 δ ≤ 0（全為缺地、無溢出）**；不等 ⇒ 尚有未列入之流失源 ⇒ **停機**。
- **例外停機**（§一）：殘差格中若有**不含街角第 1 宗**者 ⇒ 成因非 `K-9-5-4 ②` ⇒ **停機上呈**。
  「含街角第 1 宗」＝ `winners_state[blk]['p1_end']` 或 `['p2_end']` 非空。
- 框內重複鍵 ＝ 0（同情境同街廓被呼叫多次即 loud 列出）。
"""
import io
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
sys.path.insert(0, VERIFY)

from app_harvest import harvest                                     # noqa: E402
import run_verification as rv                                       # noqa: E402
from selection_pipeline import run_corner_pk                        # noqa: E402
from stepg_pipeline import run_step_g                               # noqa: E402

OUTDIR = os.path.join(VERIFY, "out")
LOG = os.path.join(OUTDIR, "probe_D2b2_exposure.log")

COVER_TOL = 0.01          # ＝生產閘門檻（⛔ 本檔不放寬·僅用以判「哪些格算殘差格」）
EQ_TOL = 1e-9             # 正對照容差（replica vs 原函式）

W = 200


def _replica(ns, block_poly, d_hat, corner_pt, allocation_dir, biz_polys):
    """原函式步驟 1–5 之**無閘** replica。逐字對映 `_pool_strips_for_block`。

    ⚠️ 本 replica 之忠實性**不靠宣稱**——由下方「原函式未 raise 之格 `==` 對照」證明。
    """
    import numpy as np
    from shapely.ops import unary_union

    _strip_s_range = ns["_strip_s_range"]
    _block_strip = ns["_block_strip"]
    if "_S_EPS" not in ns:
        raise RuntimeError("🔴 ns 缺 `_S_EPS` ——replica 與生產退化界不同源，停（no-silent-fallback）")
    _S_EPS = ns["_S_EPS"]

    _biz = [p for p in (biz_polys or []) if p is not None and not p.is_empty]

    # 1. 街廓 s 域
    dom = _strip_s_range(block_poly, d_hat, corner_pt, allocation_dir)
    if dom is None:
        raise RuntimeError("🔴 replica：街廓 s 域不可定義（與生產同條件），停")
    s_min, s_max = dom

    # 2. 業主宗 s 區間
    biz_iv = []
    for p in _biz:
        r = _strip_s_range(p, d_hat, corner_pt, allocation_dir)
        if r is not None:
            biz_iv.append(r)
    biz_iv.sort()

    # 3. 聯集
    merged = []
    for a, b in biz_iv:
        if merged and a <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], b))
        else:
            merged.append((a, b))

    # 4. 補區間＝池 s-帶（＋退化濾除）
    pool_iv = []
    cur = s_min
    for a, b in merged:
        if a > cur:
            pool_iv.append((cur, min(a, s_max)))
        cur = max(cur, b)
    if cur < s_max:
        pool_iv.append((cur, s_max))
    n_degen = len([1 for a, b in pool_iv if (b - a) <= _S_EPS])
    pool_iv = [(a, b) for a, b in pool_iv if (b - a) > _S_EPS]

    # 5. 以同一 `_block_strip` 切出
    pieces = []
    for (a, b) in pool_iv:
        bp = np.asarray(corner_pt, dtype=float) + a * np.asarray(d_hat, dtype=float)
        g, _ = _block_strip(block_poly, d_hat, bp, b - a, allocation_dir=allocation_dir)
        if g is None or g.is_empty:
            continue
        if g.buffer(-1e-4).is_empty:
            continue
        pieces.append(g)

    _all = _biz + pieces
    uni = unary_union(_all) if _all else None
    uni_area = float(uni.area) if uni is not None else 0.0
    blk_area = float(block_poly.area)
    return {
        "pieces": sorted(pieces, key=lambda g: g.area, reverse=True),
        "n_biz": len(_biz),
        "n_pieces": len(pieces),
        "n_degen": n_degen,
        "uni_area": uni_area,
        "blk_area": blk_area,
        "delta": uni_area - blk_area,          # 🔒 帶號：負＝缺地、正＝溢出
        "s_dom": (s_min, s_max),
    }


def main():                                                        # noqa: C901
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8")
        except Exception:
            pass
    os.makedirs(OUTDIR, exist_ok=True)

    L = []
    L.append("=" * W)
    L.append("【D-2b-2 §一】街廓鋪滿之全案暴露量測 — ⛔ 生產碼零觸·⛔ 未放寬任何生產閘")
    L.append("=" * W)
    L.append("  🔒 δ **帶號**定義 ＝ `union(宗+池) − 街廓`（**負 ＝ 缺地／楔形空隙**；正 ＝ 溢出）")
    L.append("  🔒 shim 僅吸收 `覆蓋閘破` 一種 RuntimeError；其餘例外一律 re-raise")
    L.append("  🔒 原函式**未 raise** 之格 ⇒ 回傳**原函式輸出**（生產行為逐位不變）＋ replica 正對照")

    ns, fake_st = harvest()
    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp_p, build_p, _ = rv.build_build_parcels(
        ns, fake_st, v6, list(cb_by.values()), snapshot)

    REC = []                       # 逐次呼叫紀錄
    CNT = {"bite": 0, "orig_pass": 0, "shim_absorb": 0, "mismatch": 0}
    CUR = {"sb": ""}
    _orig = ns["_pool_strips_for_block"]

    def _shim(block_poly, d_hat, corner_pt, allocation_dir,
              biz_polys, _label='', _depth=None, _verbose=True):
        CNT["bite"] += 1
        rep = _replica(ns, block_poly, d_hat, corner_pt, allocation_dir, biz_polys)
        row = {"sb": CUR["sb"], "label": str(_label), **{k: v for k, v in rep.items()
                                                         if k != "pieces"}}
        try:
            out = _orig(block_poly, d_hat, corner_pt, allocation_dir, biz_polys,
                        _label=_label, _depth=_depth, _verbose=_verbose)
        except RuntimeError as e:
            if "覆蓋閘破" not in str(e):
                raise                       # ⛔ 只 shim 覆蓋閘·其餘閘保持 loud
            CNT["shim_absorb"] += 1
            row["path"] = "shim吸收"
            row["cmp"] = "—（原函式 raise·無可對照）"
            REC.append(row)
            return rep["pieces"]

        # ── 正對照：replica `==` 原函式（證 replica 忠實·⛔ 非「不同即通過」）──
        CNT["orig_pass"] += 1
        row["path"] = "原函式通過"
        a_rep = sorted(float(g.area) for g in rep["pieces"])
        a_org = sorted(float(g.area) for g in out)
        ok = (len(a_rep) == len(a_org)
              and all(abs(x - y) <= EQ_TOL for x, y in zip(a_rep, a_org)))
        if ok:
            row["cmp"] = f"✅ == （片數 {len(a_org)}·最大面積差 " + (
                f"{max((abs(x - y) for x, y in zip(a_rep, a_org)), default=0.0):.2e}）")
        else:
            CNT["mismatch"] += 1
            row["cmp"] = (f"🔴 ≠ replica 片數 {len(a_rep)} vs 原 {len(a_org)}"
                          f"／面積 {a_rep} vs {a_org}")
        REC.append(row)
        return out

    ns["_pool_strips_for_block"] = _shim

    WINS, SGERR = {}, {}
    try:
        for setback in (0.0, 3.5):
            sb = f"{setback:g}m"
            CUR["sb"] = sb
            params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
            _d0, _s2, _o2, _w, _f = run_corner_pk(
                ns, fake_st, list(cb_by.values()), cad, params, temp_p, build_p,
                setback, snapshot=snapshot)
            WINS[sb] = {k: dict(v) for k, v in (_w or {}).items()}
            try:
                run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot,
                           params, build_p, _w, _f, setback)
            except Exception as _e:
                # 🔒 不吞——逐字記錄；殘差量測本身仍有效（REC 於 raise 前已寫入）
                SGERR[sb] = f"{type(_e).__name__}: {_e}"
    finally:
        ns["_pool_strips_for_block"] = _orig

    # ══ 0. 反靜默退路計數 ══════════════════════════════════════════════
    L.append("")
    L.append("【0】🔒 反靜默退路計數（shim 是否真的咬到）")
    L.append("-" * W)
    L.append(f"  wrapper 咬到 **{CNT['bite']}** 次｜原函式通過 **{CNT['orig_pass']}**｜"
             f"shim 吸收覆蓋閘破 **{CNT['shim_absorb']}**｜正對照不符 **{CNT['mismatch']}**")
    if CNT["bite"] == 0:
        L.append("  🔴 **wrapper 從未被呼叫 ⇒ 本檔全部結論不可據·停查**")
    else:
        L.append("  ⇒ ✅ shim 確實生效")
    if CNT["mismatch"]:
        L.append("  🔴 **replica 與原函式不符 ⇒ replica 不忠實 ⇒ 殘差數字不可據·停查**")
    elif CNT["orig_pass"] == 0:
        # 🔒 空真陷阱：`mismatch==0` 於**母體 0** 時亦成立 ⇒ ⛔ 不得判 ✅
        #   （`CLAUDE.md`「計數為 0 而結論為『無變化』者，一律先當作 patch 沒生效」之同族）
        L.append("  🔴 **正對照母體 ＝ 0**——無任何『原函式未 raise』之格可供對照 ⇒ "
                 "**replica 之忠實性未經證明**。")
        L.append("     ⛔ `mismatch==0` 於此係**空真**（vacuous），⛔ **不得**據以宣稱 replica 忠實。")
        L.append("     ⇒ 下方殘差數字之地位 ＝ **『與生產同構之獨立重算』，非『經對照證實』**。")
    else:
        L.append(f"  ⇒ ✅ replica 於**全部 {CNT['orig_pass']} 個未 raise 之格**與原函式逐格 `==`"
                 f"（replica 忠實·殘差可據）")
    for sb, msg in SGERR.items():
        L.append(f"  ⚠️ `run_step_g[{sb}]` 仍以例外收尾（逐字）：{msg[:150]}")

    # ══ 1. 框內重複鍵 ══════════════════════════════════════════════════
    keys = [(r["sb"], r["label"]) for r in REC]
    dup = sorted({k for k in keys if keys.count(k) > 1})
    L.append("")
    L.append("【1】🔒 框內重複鍵")
    L.append("-" * W)
    L.append(f"  母體列數 ＝ **{len(REC)}**｜相異鍵 ＝ **{len(set(keys))}**｜重複鍵 ＝ **{len(dup)}**")
    if dup:
        L.append(f"  ⚠️ 重複鍵（同情境同街廓被呼叫多次·逐項列出）：{dup}")

    # ══ 2. 逐街廓暴露 ══════════════════════════════════════════════════
    L.append("")
    L.append("【2】逐街廓暴露（⛔ 比對欄以**欄名**指名）")
    L.append("-" * W)
    hdr = (f"{'情境':<6}{'街廓':<7}{'街廓(㎡)':>14}{'union(㎡)':>14}{'δ=union−街廓(㎡)':>20}"
           f"{'|δ|(㎡)':>12}{'宗數':>6}{'池片':>6}{'退化':>6}  {'含街角第1宗':<13}{'路徑':<11}{'正對照'}")
    L.append(hdr)
    L.append("-" * W)
    for r in REC:
        w = WINS.get(r["sb"], {}).get(r["label"], {}) or {}
        has_corner = bool(w.get("p1_end")) or bool(w.get("p2_end"))
        r["has_corner"] = has_corner
        L.append(f"{r['sb']:<6}{r['label']:<7}{r['blk_area']:>14.4f}{r['uni_area']:>14.4f}"
                 f"{r['delta']:>+20.4f}{abs(r['delta']):>12.4f}"
                 f"{r['n_biz']:>6}{r['n_pieces']:>6}{r['n_degen']:>6}  "
                 f"{('✅ 有' if has_corner else '🔴 無'):<13}{r['path']:<11}{r['cmp']}")

    # ══ 3. 合計（🔒 帶號與絕對值並列）＋ 殘差閘 ════════════════════════
    L.append("")
    L.append("【3】🔒 合計（**帶號與絕對值並列**）＋ 殘差閘")
    L.append("-" * W)
    s_blk = sum(r["blk_area"] for r in REC)
    s_uni = sum(r["uni_area"] for r in REC)
    s_sig = sum(r["delta"] for r in REC)
    s_abs = sum(abs(r["delta"]) for r in REC)
    L.append(f"  Σ街廓 ＝ **{s_blk:.4f}**㎡　Σunion ＝ **{s_uni:.4f}**㎡")
    L.append(f"  **Σδ（帶號）＝ {s_sig:+.4f}㎡**　　**Σ|δ|（絕對值）＝ {s_abs:.4f}㎡**")
    lhs = s_abs
    rhs = s_blk - s_uni
    gate = abs(lhs - rhs)
    L.append(f"  殘差閘：|Σ|δ| − (Σ街廓 − Σunion)| ＝ |{lhs:.4f} − {rhs:.4f}| ＝ **{gate:.6f}** "
             f"（≤ 0.01 ⇒ 過）")
    if gate <= 0.01:
        L.append("  ⇒ ✅ **過**——⟺ 每格 δ ≤ 0（**全為缺地·無溢出**）⇒ 無未列入之流失源")
    else:
        L.append("  ⇒ 🛑 **破 ⇒ 停機**（有格 δ > 0 ＝ 溢出 ⇒ 尚有未列入之流失源）")

    # ══ 4. 停機條件 ════════════════════════════════════════════════════
    L.append("")
    L.append("【4】🛑 §一 之例外停機條件：殘差格中是否有**不含街角第 1 宗**者")
    L.append("-" * W)
    bad = [r for r in REC if abs(r["delta"]) > COVER_TOL]
    L.append(f"  殘差格（|δ| > {COVER_TOL}）＝ **{len(bad)}** ／ 母體 {len(REC)}")
    off = [r for r in bad if not r["has_corner"]]
    for r in bad:
        L.append(f"    {r['sb']:<6}{r['label']:<7}δ={r['delta']:+.4f}　"
                 f"含街角第1宗＝{'✅ 有' if r['has_corner'] else '🔴 無'}")
    if off:
        L.append(f"  ⇒ 🛑 **停機上呈**——{len(off)} 格殘差街廓**不含街角第 1 宗** "
                 f"⇒ 成因非 `K-9-5-4 ②`：{[(r['sb'], r['label']) for r in off]}")
    else:
        L.append("  ⇒ ✅ **全部殘差格皆含街角第 1 宗** ⇒ 成因與 `K-9-5-4 ②` 一致·不觸發停機")

    # ══ 5. 獨立性（§一 要求正面陳述）══════════════════════════════════
    L.append("")
    L.append("【5】🔒 各街廓之殘差是否獨立於 R1 之 shim（§一 要求正面陳述）")
    L.append("-" * W)
    L.append("  **陳述**：shim ⛔ 不改任何數值，只解除「中止」。其對下游之輸出為：")
    L.append("    · 原函式未 raise 之格 ⇒ 回傳**原函式本身之輸出**（逐位相同·非 replica）")
    if CNT["orig_pass"] > 0:
        L.append(f"    · 原函式 raise 之格 ⇒ 回傳 replica 池片，而 replica 已於**全部 "
                 f"{CNT['orig_pass']} 個可對照之格**與原函式 `==`（【0】）")
    else:
        L.append("    · 原函式 raise 之格 ⇒ 回傳 replica 池片。⚠️ **本次正對照母體 ＝ 0**"
                 "（【0】）⇒ replica 忠實性**未經證明**，此路徑之等價性為**未證主張**。")
    L.append("  ⇒ 下游所見 ＝ **「該閘不存在」時之生產值**。")
    L.append("  ⚠️ **未主張**各街廓殘差彼此統計獨立——Step-G 街廓迴圈之上游（PK／階段1／階段2）")
    L.append("     若對前一街廓之結果有依賴，該依賴**仍在**；本檔僅主張 shim **未注入新值**。")
    L.append(f"  ⚠️ 對照組：`verify/out/D2b1_runall.log` 僅評估到 R1（`grep -o \"街廓 R[0-9]\"` "
             f"⇒ 6 街廓 R1）；本檔評估 **{len(set(r['label'] for r in REC))}** 個相異街廓。")

    # ══ 6. 🛑 §一 目標達成度（⛔ 禁以「已量到」帶過）════════════════════
    L.append("")
    L.append("【6】🛑 §一 之目標達成度：**未達**")
    L.append("-" * W)
    n_lbl = len(set(r["label"] for r in REC))
    L.append(f"  §一 之目標 ＝「取得**全部街廓**之殘差」；本檔實得 **{n_lbl}** 個相異街廓"
             f"（{sorted(set(r['label'] for r in REC))}）⇒ **未達**。")
    L.append("")
    L.append("  **成因 ＝ 第二道阻塞·非覆蓋閘**：覆蓋閘 shim 解除後，R1 於**下游**另一道閘中止：")
    for sb, msg in SGERR.items():
        L.append(f"    · [{sb}] {msg}")
    L.append("")
    L.append("  🔒 **該閘⛔不可 shim**：其為 `verify/stepg_pipeline.py:1035-1039` 之**行內 raise**，")
    L.append("     ⛔ 非 `ns` 內之函式 ⇒ 探針側無法取代；要 shim 就得改 `verify/`＝**違 §一「生產碼零觸」**。")
    L.append("")
    L.append("  🔒 **該閘之破⛔不是本 shim 造成**（結構證明·非經驗巧合）：")
    L.append("     telescoping 只讀 `_adv_final['rows']`／`W0_*`／`Wf_*`；")
    L.append("     `_adv_final` 賦值於 `stepg_pipeline.py:780`／`:821`，**早於**被 shim 之呼叫 `:928`。")
    L.append("     ⇒ 其輸入於 shim 生效前**已定案** ⇒ 本 shim 不可能改變之；")
    L.append("     ⇒ 該破係 **D-2b-1 態既有、僅被覆蓋閘之 raise 遮蔽**（先 raise 者勝）。")
    L.append("     佐證：`結構閘 telescoping 破` 於 `K6A2_seg6_gb40`／`D1`／`D2`／`D2b1` 四份 "
             "`run_all` log 命中**各 0**。")
    L.append("")
    L.append("  🔒 **⛔ 已排除之替代路徑**（⛔ 非未想到·係想過而不可用）：")
    L.append("     「自 `cb` 剔除 R1 以觸及 R2…」**不可用**——`compute_total_burden_rate`")
    L.append("     （`stepg_pipeline.py:69-70`）以 `sum(area_m2 for b in cb ...)` 算**重劃總負擔率**，")
    L.append("     剔除任一街廓即改變全域負擔率 ⇒ 改變**每一格 G** ⇒ **非保值**，量到的不是生產值。")
    L.append("")
    L.append("  ⇒ 🛑 **上呈**：§一 之方法前提（『shim 覆蓋閘 ⇒ 得全部街廓殘差』）**不成立**。")
    L.append("     全案暴露之取得**須先處置 R1 之 telescoping 破**，或另授權改 `verify/`。")

    L.append("")
    L.append("=" * W)
    txt = "\n".join(L)
    with io.open(LOG, "w", encoding="utf-8") as f:
        f.write(txt + "\n")
    print(txt)
    print(f"\n[written] {LOG}")


if __name__ == "__main__":
    main()
