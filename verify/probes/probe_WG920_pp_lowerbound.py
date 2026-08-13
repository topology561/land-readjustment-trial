# -*- coding: utf-8 -*-
r"""`W-G.9-20` §1：族②③ 之**百分點下界**（⛔ 零生產碼·只讀包裝）。

# 🔴 本探針之受詞 ＝ **百分點**，⛔ **不是面積**

`W-G.9-19` `D3` 判「族②③ 之差算不出來」，理由為「新值 ⊥SIDELINE、現行值沿 `s`
⇒ **不同軸·不得相減**」。**該理由為偽**——現查四處（⛔ **正面列舉受檢檔**）：

| # | 檔 | 現查（判準＝含該字樣） | 意義 |
|---|---|---|---|
| ① | `app.py` | `_select_pool_slot` docstring：`b＝forced **起始 W**`／`w_i（**⊥ALLOC、W 軸單位**）` | 該槽之受詞**本即垂距** |
| ② | `verify/stepg_pipeline.py` | `'b': _b_L0`，而 `_b_L0 = _mp_base_W0(...)` → `return float(_k956_W_from_mp(_bp0, _mp, _adir, _dv))` | 🔴 **引擎已餵正典 `K-9-5-6` 直量** |
| ③ | `app.py`（`main()` 內） | `'b': _left_buffer_S * _cos_dn`　#『Q2：b＝buffer_S×cos_dn **入 W 軸**』 | 舊式，但**換算係數 `_cos_dn` 早在碼面** |
| ④ | `app.py`（`main()` 內） | `_W_prev_left = (_left_buffer_S * _cos_dn) if _has_left_corner else 0.0` | 同③ |

⇒ **族②③ 之槽本即收垂距**；`W-G.9-19` 讀到的 `left_cum_S = buf`（沿 `s`）是
**族①** 之槽。⛔ 我把族① 之受詞安到族②③ 頭上。

⇒ **換算不必去求**：`main()` 側早有 `_cos_dn`，**引擎側根本已改用正典直量**。

🔴 **⚠️ 併發現（比原題更重要）**：②與③**不同源**——引擎已遷至 `k956_W_from_mp`，
`main()` 仍為 `buf · _cos_dn`。⇒ **`GB-62`（正典與碼面無雙向同步）之碼面實例**。
⚠️ 依 `CLAUDE.md`，`main()` 內之敘述**從不被 `run_all` 執行** ⇒ 二者長期分歧而無閘可擋。

## 本探針量什麼

族③ 之 `ΣRw_側 = R(b + Σw_群) − R(b)`（`_select_pool_slot` 逐字）。
只把 `b` 由**舊式**換成**正典 `K-9-5-6` 直量**，其餘一切不動：

    ΔΣRw ＝ [R(b_新 + Σw) − R(b_新)] − [R(b_舊 + Σw) − R(b_舊)]     單位：**百分點**

* `b_舊` ＝ `_left_buffer_S · _cos_dn`（＝ 生產現值·亦即 `W-G.9-4_W_old_*`）
* `b_新` ＝ `k956_W_from_mp(...)`（＝ `W-G.9-4_W_new_*`·**生產碼已併行算好、只寫診斷**）

🔒 **⛔ 本探針不自行重建 `b_新`**——直接讀生產碼自己算的診斷欄
（`f3_forced_offset_diag`），故無「外部重建」之風險。

## 自我驗證閘（CLAUDE.md·⛔ 不過不得出艙）

* **對照組（已知為真）**：碼面明載之解析恆等（`W-G.9-2` 已證）
  `舊式 ＝ 新式 − W_0` ⇒ 逐格驗；**任一格不過 ⇒ 本探針之輸出全部作廢**。
* **已知為偽者須紅**：同式改為 `舊式 ＝ 新式 + W_0` 須紅（`W_0 ≠ 0` 之格）
  ⇒ 證該自檢**非恆綠**。

## 重跑
    python verify/probes/probe_WG920_pp_lowerbound.py
"""
import os
import sys
import traceback

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
sys.path.insert(0, VERIFY)
assert os.path.exists(os.path.join(REPO, "CLAUDE.md")), f"🔴 REPO 不是倉根：{REPO}"
OUT = os.path.join(VERIFY, "out", "probe_WG920_pp_lowerbound.log")
L, RC = [], [0]
BANNER = "🔴 **受詞 ＝ 百分點（側街負擔率）**，⛔ **不是面積**"


def say(s=""):
    print(s)
    L.append(s)


def red(s):
    say(f"  🔴 {s}")
    RC[0] = 1


def _f(v, n=4):
    return "—" if v is None else f"{float(v):.{n}f}"


def run_tag(tag, setback, REC):
    """跑到 Step-G 之推進段，只讀記錄 `_select_pool_slot` 之引數與當時之診斷欄。"""
    import run_verification as rv
    from app_harvest import harvest
    from selection_pipeline import build_ownership, build_build_parcels, run_corner_pk
    from stepg_pipeline import run_step_g

    snap = rv.load_snapshot()
    ns, fs = harvest()
    cb_by, cad = rv.build_pipeline(ns, fs, snap)
    build_ownership(ns, fs, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    tp, bp, _ = build_build_parcels(ns, fs, v6, list(cb_by.values()), snap)
    params = rv.build_param_table(ns, fs, cb_by, cad, snap, setback)
    _d, _s, _o, win, forced = run_corner_pk(
        ns, fs, list(cb_by.values()), cad, params, tp, bp, setback, snapshot=snap)

    # ── 只讀包裝（⛔ 原樣轉呼叫·原樣回傳·用畢還原）────────────────────────
    _orig_slot = ns["_select_pool_slot"]
    _orig_k956 = ns["k956_W_from_mp"]

    def w_k956(*a, **kw):
        out = _orig_k956(*a, **kw)
        REC["k956"].append(out)
        return out

    def w_slot(widths, left_side, right_side, rw_func=None):
        out = _orig_slot(widths, left_side, right_side, rw_func)
        diag = dict((fs.session_state.get("f3_forced_offset_diag", {}) or {}))
        REC["slot"].append({
            "widths": [float(x or 0.0) for x in (widths or [])],
            "L": dict(left_side or {}), "R": dict(right_side or {}),
            "k": out.get("k"), "table": out.get("table"),
            "diag": {k: dict(v) for k, v in diag.items() if isinstance(v, dict)},
            "k956_tail": list(REC["k956"][-4:]),
        })
        return out

    ns["_select_pool_slot"] = w_slot
    ns["k956_W_from_mp"] = w_k956
    err = None
    try:
        run_step_g(ns, fs, list(cb_by.values()), cad, snap, params, bp, win, forced, setback)
    except Exception as e:                              # noqa: BLE001
        err = f"{type(e).__name__}: {str(e)[:130]}"
    finally:                                            # 🔒 還原（⛔ 不留 patch）
        ns["_select_pool_slot"] = _orig_slot
        ns["k956_W_from_mp"] = _orig_k956
    return {"err": err, "rw": ns["rw_from_width"], "forced": forced, "params": params}


def identify(rec):
    """由 `b_舊` 反查該筆 `_select_pool_slot` 對應之街廓（⛔ 須唯一·非唯一即紅）。"""
    bL = float((rec["L"] or {}).get("b", 0.0) or 0.0)
    bR = float((rec["R"] or {}).get("b", 0.0) or 0.0)
    hit = []
    for lbl, d in (rec["diag"] or {}).items():
        oL = d.get("W-G.9-4_W_old_left")
        oR = d.get("W-G.9-4_W_old_right")
        if oL is None and oR is None:
            continue
        if (abs(float(oL or 0.0) - bL) < 1e-9) and (abs(float(oR or 0.0) - bR) < 1e-9):
            hit.append((lbl, d))
    return hit, bL, bR


def main():
    say("=" * 112)
    say("【`W-G.9-20` §1】族②③ 之**百分點下界**（⛔ 零生產碼·只讀包裝）")
    say(BANNER)
    say("=" * 112)
    say("  🔒 現行值之受詞（碼面逐字·⛔ 非我之轉述·⛔ 正面列舉受檢檔）：")
    say("     ① `app.py`｜`_select_pool_slot` docstring：『b＝forced **起始 W**』"
        "／『w_i（**⊥ALLOC、W 軸單位**）』")
    say("     ② `verify/stepg_pipeline.py`｜`'b': _b_L0`；`_b_L0 = _mp_base_W0(...)`")
    say("        → `return float(_k956_W_from_mp(_bp0, _mp, _adir, _dv))`"
        "　⇒ 🔴 **引擎已餵正典 `K-9-5-6` 直量**")
    say("     ③ `app.py`（`main()` 內）｜`'b': _left_buffer_S * _cos_dn`"
        "　#『Q2：b＝buffer_S×cos_dn **入 W 軸**』")
    say("     ④ `app.py`（`main()` 內）｜"
        "`_W_prev_left = (_left_buffer_S * _cos_dn) if _has_left_corner else 0.0`")
    say("     ⇒ **族②③ 之槽本即收垂距** ⇒ 與正典直量**同軸·可相減**。")
    say("     ⚠️ `W-G.9-19` 所讀之 `left_cum_S = buf`（沿 `s`）係 **族①** 之槽。")
    say("     🔴 **②與③不同源** ⇒ `GB-62` 之碼面實例（`main()` 內敘述不被 `run_all` 執行）。")

    grand = {}
    for tag, sb in (("0m", 0.0), ("3.5m", 3.5)):
        REC = {"slot": [], "k956": []}
        say()
        say("=" * 112)
        say(f"【情境 {tag}】　{BANNER}")
        say("=" * 112)
        try:
            st = run_tag(tag, sb, REC)
        except Exception as e:                          # noqa: BLE001
            red(f"情境 {tag} 建置失敗：{type(e).__name__}: {e}")
            say(traceback.format_exc()[-360:])
            continue
        R = st["rw"]
        say(f"  run_step_g ⇒ {st['err'] or '（未拋）'}")
        say(f"  `_select_pool_slot` 之只讀記錄 ＝ **{len(REC['slot'])}** 次呼叫")

        # ── 母體：b_舊 ≠ 0 之格（＝ 族②③ 實際被餵非零起始 W 者）──────────
        say()
        say("  ── 母體（判準：`b_舊 ≠ 0` ⇒ 該側之族②③ 起始 W 非零）──")
        rows, n_zero, n_badkey = [], 0, 0
        for i, rec in enumerate(REC["slot"]):
            hit, bL, bR = identify(rec)
            if bL == 0.0 and bR == 0.0:
                n_zero += 1
                say(f"     [{i}] b_舊 兩側皆 0 ⇒ 判準下不入母體（⛔ 非「算不出」）")
                continue
            if len(hit) != 1:
                n_badkey += 1
                red(f"第 {i} 筆：街廓識別**非唯一**（命中 {len(hit)}）⇒ ⛔ 不得用作鍵")
                say(f"          🔍 raw｜L ＝ {rec['L']}")
                say(f"          🔍 raw｜R ＝ {rec['R']}")
                say(f"          🔍 diag 之街廓 ＝ {sorted((rec['diag'] or {}).keys())}"
                    f"　⚠️ 空 ⇒ 診斷欄係 `main()` 內之敘述，**harness 路徑不執行**")
                say(f"          🔍 k956 尾 4 筆 ＝ {rec['k956_tail']}")
                # 🔒 **實測錨**：引擎之 `b` 是否即 `k956_W_from_mp` 之輸出（⛔ 非我之推論）
                _tail = [float(x) for x in (rec["k956_tail"] or []) if x is not None]
                _hitL = any(abs(x - bL) < 1e-12 for x in _tail)
                _hitR = any(abs(x - bR) < 1e-12 for x in _tail)
                say(f"          🔒 **實測錨**：`b_L` ＝ {bL!r} ∈ k956 輸出？{'✅' if _hitL else '🔴'}"
                    f"｜`b_R` ＝ {bR!r} ∈ k956 輸出？{'✅' if _hitR else '🔴'}")
                if _hitL and _hitR:
                    say("          ⇒ **引擎之 `b` 即正典 `K-9-5-6` 直量（垂距）**"
                        "，⛔ 非沿 `s` 之量 ⇒ `W-G.9-19` `D3` 之「不同軸」**證偽**。")
                    say("          🔒 判別力自檢：以**必不命中**之值（`bL + 1.0`）試 ⇒ "
                        f"{'🔴 竟命中' if any(abs(x - (bL + 1.0)) < 1e-12 for x in _tail) else '✅ 不命中 ⇒ 上式非恆真'}")
                continue
            lbl, d = hit[0]
            rows.append((lbl, rec, d, bL, bR))
            say(f"     [{i}] 街廓 **{lbl}**｜b_舊(左) ＝ {_f(bL)}｜b_舊(右) ＝ {_f(bR)}"
                f"｜k* ＝ {rec['k']}｜n ＝ {len(rec['widths'])}")
            say(f"          🔒 識別自證：`W-G.9-4_W_old_*` == `left/right_side['b']` "
                f"⇒ 唯一命中 1 街廓")
        say(f"     ⇒ **母體 ＝ {len(rows)} 街廓**"
            f"（b 皆 0 而排除 {n_zero} 筆｜🔴 識別失敗 {n_badkey} 筆）")
        # 🔴 **⛔ 「識別失敗」與「判準下為 0」不得共用出艙碼**（CLAUDE.md·自我驗證閘 2）
        if not rows:
            if n_badkey:
                red("**無從判定** ⇒ ⛔ 本情境⛔ 不得出艙任何下界數字（⛔ 非『下界 ＝ 0』）")
                grand[tag] = None
            else:
                say("     ✅ 判準下確實無非零起始 W ⇒ 族②③ 之下界 ＝ **0.0000 百分點**")
                grand[tag] = {"pp_signed": 0.0, "pp_abs": 0.0, "cells": []}
            continue

        # ── 自我驗證閘（⛔ 不過不得出艙）────────────────────────────────
        say()
        say("  ── 🔒 **自我驗證閘**（對照組＝碼面明載之恆等 `舊 ＝ 新 − W_0`·`W-G.9-2` 已證）──")
        gate_ok, gate_neg_red = True, False
        for lbl, rec, d, bL, bR in rows:
            for sd, ob, nb, w0 in (
                    ("左", d.get("W-G.9-4_W_old_left"), d.get("W-G.9-4_W_new_left"),
                     d.get("W-G.9-4_W0_left")),
                    ("右", d.get("W-G.9-4_W_old_right"), d.get("W-G.9-4_W_new_right"),
                     d.get("W-G.9-4_W0_right"))):
                if ob is None or nb is None or w0 is None:
                    continue
                lhs, rhs = float(ob), float(nb) - float(w0)
                ok = abs(lhs - rhs) < 1e-6
                gate_ok = gate_ok and ok
                bad = abs(float(ob) - (float(nb) + float(w0))) < 1e-6
                if abs(float(w0)) > 1e-9 and not bad:
                    gate_neg_red = True
                say(f"     {lbl}／{sd}側｜舊 ＝ {_f(ob)}｜新 ＝ {_f(nb)}"
                    f"｜W_0 ＝ {_f(w0)}｜新−W_0 ＝ {_f(rhs)} ⇒ {'✅' if ok else '🔴'}")
        say(f"     ⇒ 對照組（已知為真）：{'✅ 全過' if gate_ok else '🔴 有格不過'}")
        say(f"     ⇒ 已知為偽者（`舊 ＝ 新 + W_0`）：{'✅ 判為紅 ⇒ 自檢非恆綠' if gate_neg_red else '⚠️ 未觸發（W_0 全為 0）'}")
        if not gate_ok:
            red("**量測器紅** ⇒ ⛔ 本情境之下界不得出艙（CLAUDE.md·自我驗證閘）")
            continue

        # ── ΔΣRw（單位：百分點）────────────────────────────────────────
        say()
        say(f"  ── ΔΣRw ＝ [R(b_新+Σw) − R(b_新)] − [R(b_舊+Σw) − R(b_舊)]　{BANNER} ──")
        say(f"     {'街廓':<8}{'側':<4}{'b_舊':>10}{'b_新':>10}{'W_0':>10}"
            f"{'Σw_群':>10}{'ΣRw_舊':>11}{'ΣRw_新':>11}{'ΔΣRw(pp)':>12}")
        cells, sgn, absum = [], 0.0, 0.0
        for lbl, rec, d, bL, bR in rows:
            w = rec["widths"]
            k = int(rec["k"] or 0)
            for sd, side, b_old, b_new, w0, sw in (
                    ("左", rec["L"], d.get("W-G.9-4_W_old_left"),
                     d.get("W-G.9-4_W_new_left"), d.get("W-G.9-4_W0_left"), sum(w[:k])),
                    ("右", rec["R"], d.get("W-G.9-4_W_old_right"),
                     d.get("W-G.9-4_W_new_right"), d.get("W-G.9-4_W0_right"),
                     sum(w) - sum(w[:k]))):
                if not bool((side or {}).get("has")):
                    continue
                if b_old is None or b_new is None:
                    say(f"     {lbl:<8}{sd:<4}⚠️ 診斷欄缺 ⇒ ⛔ 不估此格")
                    continue
                bo, bn = float(b_old), float(b_new)
                old = R(bo + sw) - R(bo)
                new = R(bn + sw) - R(bn)
                dd = new - old
                sgn += dd
                absum += abs(dd)
                cells.append({"blk": lbl, "side": sd, "b_old": bo, "b_new": bn,
                              "w0": (None if w0 is None else float(w0)),
                              "sw": sw, "old": old, "new": new, "d": dd})
                say(f"     {lbl:<8}{sd:<4}{_f(bo):>10}{_f(bn):>10}{_f(w0):>10}"
                    f"{_f(sw):>10}{_f(old):>11}{_f(new):>11}{_f(dd):>12}")
        say(f"     {'—' * 96}")
        say(f"     🔒 **帶號合計 ΣΔΣRw ＝ {_f(sgn)} 百分點**"
            f"｜**絕對值合計 Σ|ΔΣRw| ＝ {_f(absum)} 百分點**")
        say("     ⚠️ 依倉規（凡列合計·帶號與絕對值並列）——二者所偵測之錯**不相交**。")
        grand[tag] = {"pp_signed": sgn, "pp_abs": absum, "cells": cells}

    # ── 總結 ────────────────────────────────────────────────────────────
    say()
    say("=" * 112)
    say(f"【總結】　{BANNER}")
    say("=" * 112)
    for tag in ("0m", "3.5m"):
        g = grand.get(tag)
        if g is None:
            say(f"  {tag:<6}🔴 **無從判定**——⛔ 不得讀作『下界 ＝ 0』（見上之識別失敗）")
            continue
        say(f"  {tag:<6}ΣΔΣRw ＝ **{_f(g['pp_signed'])}** pp"
            f"｜Σ|ΔΣRw| ＝ **{_f(g['pp_abs'])}** pp｜格數 ＝ {len(g['cells'])}")
    say()
    say("  ══ 🔴 **本批未量得下界之<u>值</u>——成因具名** ══")
    say("     `run_step_g` 於**第一個街廓 `R1`** 即撞結構閘 `理論＝實跑` 而拋")
    say("     ⇒ `_select_pool_slot` **全程只被呼叫 1 次**（見上「只讀記錄」）")
    say("     ⇒ 目標三格（`R5/left`、`R2/left`、`R3/right`·`W-G.9-19` `D1` 之母體）"
        "**從未被跑到**。")
    say("     🔴 ⛔ **「未量得」≠「量得為 0」**——本探針之出艙碼已分開"
        "（`無從判定` vs `判準下為 0`）。")
    say("     ⚠️ 該閘即 `W-G.9-14` 所分解者；其修法（校回起點）已呈 KL、**本批⛔ 未動**。")
    say()
    say("  🔴 **若量得，其受詞為<u>百分點</u>**：只含族②③（起算），"
        "⛔ **未含族①（落位）之面積效果**。")
    say("  🔴 ⛔ **不得與面積並列、不得讀成區間**。")
    say("  ⚠️ 施工單 §4 新 E 所載之『8.6〜8.9 個百分點』係 **【單】**（倉內查無）")
    say("     ⇒ 🔴 **本批⛔ 未能將其轉為【倉】**，⛔ 下游文件不得引用為事實。")

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print(f"\n[log] {os.path.relpath(OUT, REPO)}　rc={RC[0]}")
    return RC[0]


if __name__ == "__main__":
    sys.exit(main())
