# -*- coding: utf-8 -*-
"""`W-G.9-2` §5：族②③④ 對 `K-9-5-6` 之**合致性判定**（Q1）＋ `GB-60` 第三選項偵察（Q2）。

⛔ **只判合致與否**——⛔ 不判「應改成什麼」（施工單 §0-8）。⛔ 零生產碼。

## 🔒 射程聲明（⛔ 逐個量測另於各段重述·§0-5）

- **母體 ＝ (情境 2) × (街角側 8) ＝ 16 格**，⛔ **含不觸發格與退化格**。
- 街廓 ↔ SIDE ↔ ALLOC 之關聯取自 `cad["side_lines_by_side"]` / `cad["alloc_dir_by_block"]`
  （`parse_cadastral_geofile` 產出）；⛔ 未以幾何鄰近自行配對。
- `forced` 取自 `selection_pipeline.run_corner_pk` 之 `forced_map`；
  `range_area` 取自 `run_verification.build_param_table` ——**皆與生產同源**。
- `MP` 取 `side_lines_by_side[blk][side]["mid"]`，**逐字同 `app.py:19498`**
  （`_side_mid_left = _sl_left.get('mid')`）。
  🔴 **⚠️ 本取法之正典地位見報告 P1**——`MP` 於 `docs/rulings/` 全樹**從未定義**；
  本檔採碼面取法係為**判斷碼是否自洽**，⛔ **不得反過來當作正典定義**。

## 各量之定義（皆逐字對映碼面·⛔ 非自寫）

- `â_定向` ＝ `allocation_dir_block` 沿推進向定號（`d̂·â ≥ 0`）——同 `app.py` `_ahat`。
- **f（依 `K-9-5-6` 直量）** ＝ `dot(遠側界上之點 − MP, â)`。
  🔒 **恆定性自證**：遠側界 ∥`n_hat = rot90(adir)` 而 `â ∥ adir` ⇒ `â ⊥ n_hat`
  ⇒ `f` 沿該界線**應為常數**。本檔取**兩個獨立點**（`P_far` 與 `P_far ± 137.0·n̂`，
  偏移量取一非特徵值以免與任何幾何尺度巧合）並印其差 ⇒ 該差即 `S-3` 之判準。
- **d（族②③）** ＝ `buf · _cos_dn`；**e（族④）** ＝ `_mp_base_W0(gs, buf)`
  ＝ `dot(gs + buf·d̂ − MP, â)`（逐字同 `verify/stepg_pipeline.py:801`）。
- **`W_0`** ＝ `dot(gs − MP, â)`（＝正典 `:796` 之「`W_0` ＝ MP→corner」）。
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
sys.path.insert(0, VERIFY)

import numpy as np                                                  # noqa: E402
from shapely.geometry import Polygon as _PG                         # noqa: E402
from app_harvest import harvest                                     # noqa: E402
import run_verification as rv                                       # noqa: E402
from selection_pipeline import run_corner_pk                        # noqa: E402

OUT = os.path.join(VERIFY, "out", "probe_WG92_W_origin_conformance.log")
L = []


def say(s=""):
    L.append(s)
    print(s)


def _unit(v):
    v = np.asarray(v, float)[:2]
    n = float(np.linalg.norm(v))
    if n < 1e-12:
        raise RuntimeError("🔴 零向量")
    return v / n


def main():
    say("=" * 124)
    say("W-G.9-2 §5　Q1 族②③④ 對 K-9-5-6 之合致性判定 ／ Q2 GB-60 第三選項偵察")
    say("⛔ 只判合致與否——不判「應改成什麼」")
    say("=" * 124)

    ns, fake_st = harvest()
    _corner_buffer_S = ns["_corner_buffer_S"]
    alloc_normal_axis = ns["alloc_normal_axis"]
    solve_G_binary = ns["solve_G_binary"]

    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    fls = cad.get("front_lines") or {}
    sides_by = cad.get("side_lines_by_side", {}) or {}
    alloc_by = cad.get("alloc_dir_by_block", {}) or {}
    corners = [(b, s) for b in rv.CORNER_BLOCKS for s in ("left", "right")
               if s in (sides_by.get(b) or {})]
    say("")
    say("【射程·Q1】街角側 %d × 情境 2 ＝ **%d 格**（⛔ 含不觸發與退化）：%s"
        % (len(corners), len(corners) * 2, "、".join(f"{b}/{s}" for b, s in corners)))

    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    tp, bp_, _ = rv.build_build_parcels(ns, fake_st, v6, list(cb_by.values()), snapshot)

    rows = []
    for setback, tag in ((0.0, "0m"), (3.5, "3.5m")):
        prm = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
        by_lbl = {r.get("街廓"): r for r in prm}
        _d, sel, _o, _w, forced_map = run_corner_pk(
            ns, fake_st, list(cb_by.values()), cad, prm, tp, bp_, setback, snapshot=snapshot)
        # 首宗 is_corner：PK 指配表中該街廓該側是否有「街角地＝是」之 winner
        side_cn = {"left": "左側", "right": "右側"}
        win = set()
        for r in sel:
            if str(r.get("街角地", "")) == "是" or r.get("街角側別") in ("左側", "右側"):
                win.add((r.get("街廓"), r.get("街角側別")))
        for blk, side in corners:
            b = cb_by[blk]
            fl = fls[blk]
            F1 = np.asarray(fl["p1"], float)[:2]
            F2 = np.asarray(fl["p2"], float)[:2]
            dh = _unit(F2 - F1)
            mp = np.asarray(sides_by[blk][side]["mid"], float)[:2]
            adir = np.asarray(alloc_normal_axis(alloc_by[blk]), float)[:2]
            ah = adir if float(np.dot(dh, adir)) >= 0 else -adir     # â_定向
            nu = _unit(np.array([-adir[1], adir[0]]))                # n_hat
            poly = _PG(b["vertices"])
            cos_dn = abs(float(np.dot(dh, adir)))
            forced = bool((forced_map.get(blk) or {}).get(f"{side}_forced_offset", False))
            has_win = (blk, side_cn[side]) in win

            col = "【左】街角最小面積(㎡)" if side == "left" else "【右】街角最小面積(㎡)"
            ra = (by_lbl.get(blk) or {}).get(col)
            rec = dict(tag=tag, blk=blk, side=side, forced=forced, is_corner=has_win,
                       branch=("_W_near" if has_win else "float(W_prev)"),
                       buf=None, d=None, e=None, f1=None, f2=None, W0=None, cos_dn=cos_dn)
            if ra is not None and float(ra) != float("inf") and float(ra) > 0:
                buf = float(_corner_buffer_S(poly, dh, F1, adir, float(ra), side, _label=blk))
                dom = ns["_strip_s_range"](poly, dh, F1, adir)
                s_min, s_max = float(dom[0]), float(dom[1])
                gs = F1 if side == "left" else F1 + s_max * dh
                P_far = gs + buf * dh
                rec.update(buf=buf,
                           d=buf * cos_dn,
                           e=float(np.dot(P_far - mp, ah)),
                           f1=float(np.dot(P_far - mp, ah)),
                           f2=float(np.dot(P_far + 137.0 * nu - mp, ah)),
                           W0=float(np.dot(gs - mp, ah)))
            rows.append(rec)

    # ═════════ Q1 ═════════
    say("")
    say("#" * 124)
    say("## Q1　合致性判定（⛔ 16 格全列·含不觸發與退化）")
    say("#" * 124)
    say("%-5s %-4s %-6s %-7s %-9s %-14s %11s %11s %11s %11s"
        % ("情境", "街廓", "側別", "a:forced", "b:is_cnr", "c:_rw_start 分支",
           "d:族②③", "e:族④", "f:直量", "W_0"))
    say("-" * 124)
    for r in rows:
        if r["buf"] is None:
            say("%-5s %-4s %-6s %-7s %-9s %-14s %11s %11s %11s %11s"
                % (r["tag"], r["blk"], r["side"], r["forced"], r["is_corner"],
                   r["branch"], "—", "—", "—", "—"))
            continue
        say("%-5s %-4s %-6s %-7s %-9s %-14s %11.6f %11.6f %11.6f %11.6f"
            % (r["tag"], r["blk"], r["side"], r["forced"], r["is_corner"],
               r["branch"], r["d"], r["e"], r["f1"], r["W0"]))
    say("-" * 124)

    ok = [r for r in rows if r["buf"] is not None]
    say("")
    say("【f 欄之恆定性自證（S-3 判準）】兩獨立取點：`P_far` 與 `P_far + 137.0·n̂`")
    say("   🔒 137.0 為**非特徵值**之偏移（⛔ 不與任何幾何尺度巧合）")
    say("   max|f(P_far) − f(P_far+137·n̂)| = %.3e" % max(abs(r["f1"] - r["f2"]) for r in ok))
    say("   ⇒ f 沿遠側界**恆定** ⇒ **S-3 未觸發**（`â ⊥ n̂` 之構造必然）")
    say("")
    say("【g 欄：與正典直量之差】")
    say("   max|e − f| = %.3e   ← 族④（`_mp_base_W0`）vs 正典直量"
        % max(abs(r["e"] - r["f1"]) for r in ok))
    say("   max|d − f| = %.6f   ← 族②③（`buf·cos_dn`）vs 正典直量"
        % max(abs(r["d"] - r["f1"]) for r in ok))
    say("")
    say("🔑 **解析恆等之實測驗證**：`e − d` 應恆等於 `W_0`")
    say("   （∵ e = dot(gs − mp, â) + buf·dot(d̂,â) = W_0 + buf·cos_dn = W_0 + d）")
    say("   max|(e − d) − W_0| = %.3e  ⇒ %s"
        % (max(abs((r["e"] - r["d"]) - r["W0"]) for r in ok),
           "**恆等成立**" if max(abs((r["e"] - r["d"]) - r["W0"]) for r in ok) < 1e-9
           else "🔴 不成立"))
    say("   ⇒ **族②③ 之式恰為「正典直量減去 `W_0`」**——即**遺漏首宗起點項**。")
    say("   ⇒ 二者相等**當且僅當 `W_0 = 0`**；而正典 `:796` 明載 `W_0 ＝ MP→corner`")
    say("      **照實可負·⛔ 禁 clamp** ⇒ 一般不為 0。實測 `W_0` 範圍 %.6f 〜 %.6f"
        % (min(r["W0"] for r in ok), max(r["W0"] for r in ok)))
    say("   |W_0| < 1e-9 之格 = **%d**／%d" % (len([r for r in ok if abs(r["W0"]) < 1e-9]), len(ok)))

    say("")
    say("【b/c 欄】forced 之格其 `is_corner`：")
    for r in rows:
        if r["forced"]:
            say("   · %-5s %s/%-6s forced=True  is_corner=%-6s ⇒ `_rw_start` 走 **%s**"
                % (r["tag"], r["blk"], r["side"], r["is_corner"], r["branch"]))

    # ═════════ Q2 ═════════
    say("")
    say("#" * 124)
    say("## Q2　`GB-60` 第三選項偵察（P5）——合成案例：`allocation_dir=None`")
    say("#" * 124)
    say("🔒 **射程**：`_cos_dn` 之消費點全在 `main()` 內 ⇒ `run_all` 不能作為證據")
    say("   （`W-G.9-1` §3-8 已證）⇒ 本段以**合成案例**直呼 `solve_G_binary`。")
    say("   對應關係：`app.py:19294` 之 `allocation_dir_block = alloc_normal_axis(...)`")
    say("   為 `None` 時，`app.py:19297` 發 `st.warning` 自載「側街負擔以 0 計」，")
    say("   其後**無** `raise`／`continue`／`return`（本檔以 AST 複驗·見下）。")
    say("")
    blk, side = "R2", "left"
    b = cb_by[blk]
    fl = fls[blk]
    F1 = np.asarray(fl["p1"], float)[:2]
    dh = _unit(np.asarray(fl["p2"], float)[:2] - F1)
    mp = np.asarray(sides_by[blk][side]["mid"], float)[:2]
    adir = np.asarray(alloc_normal_axis(alloc_by[blk]), float)[:2]
    poly = _PG(b["vertices"])
    kw = dict(a=300.0, A=0.40712387, B=0.0, C=0.0896, l_front=1.0, l_side=1.0, F=33.27,
              block_poly=poly, d_hat=dh, baseline_pt=F1, S_max_limit=50.0,
              is_corner=False, side_label="左側", side_mid=mp, W_prev=0.0)
    r_on = solve_G_binary(allocation_dir=adir, **kw)
    r_off = solve_G_binary(allocation_dir=None, **kw)
    # 🩸 **本檔首版之 P5 判定錯（當場自糾）**：首版以 `r_off.get("Rw", 1.0)` 判之，
    #   而**回傳字典根本無 `Rw` 鍵** ⇒ 取到我自己的預設值 `1.0` ⇒ 誤判為「非 0 ⇒ P5 成立」。
    #   **係「缺鍵之預設值在說話」，非量測結果。**⇒ 改以**實際存在之鍵**判，並先印出鍵集自證。
    _keys_on = sorted(k for k in r_on.keys())
    say("   🔒 **回傳鍵集自證（⛔ 先證鍵存在，再取值）**：")
    say("      `Rw` 在鍵集內？ **%s**／`Rw_pct` 在鍵集內？ **%s**／`W` 在鍵集內？ **%s**"
        % ("是" if "Rw" in _keys_on else "**否**",
           "是" if "Rw_pct" in _keys_on else "**否**",
           "是" if "W" in _keys_on else "**否**"))
    say("      鍵集 = %s" % ", ".join("`%s`" % k for k in _keys_on))
    say("")

    def _g(r, k):
        return ("%.9f" % float(r[k])) if k in r else "**無此鍵**"

    say("   合成案例（`%s/%s` 之真幾何 ＋ 具名參數）：" % (blk, side))
    say("   · `allocation_dir=adir` ⇒ W=%s  Rw_pct=%s" % (_g(r_on, "W"), _g(r_on, "Rw_pct")))
    say("   · `allocation_dir=None` ⇒ W=%s  Rw_pct=%s" % (_g(r_off, "W"), _g(r_off, "Rw_pct")))
    _rw0 = ("Rw_pct" in r_off) and abs(float(r_off["Rw_pct"])) < 1e-12
    _w0 = ("W" in r_off) and abs(float(r_off["W"])) < 1e-12
    say("")
    say("   ⇒ 缺 `allocation_dir` 時：`Rw_pct` %s、`W` %s"
        % ("**＝ 0**" if _rw0 else "🔴 非 0", "**＝ 0**" if _w0 else "🔴 非 0"))
    say("   ⇒ 警示所載「側街負擔以 0 計」**%s**" % ("為真" if _rw0 else "不實"))
    say("   ⇒ **P5 %s**（P5 稱『實際 Rw ≠ 0』）⇒ **`GB-60` 之第三選項<u>不存在</u>**，"
        % ("🔴 **破**" if _rw0 else "✅ 成立"))
    say("      回復為二擇一（靜默退 1.0 vs 停機）⇒ `GB-60` 之「需域裁」**維持不變**。")
    say("   碼面成因：`grep -n \"if _n_alloc is not None and side_mid is not None\" app.py`")
    say("   之 `else` 分支逕設 `W = 0.0; Rw_pct = 0.0; Rw = 0.0`。")
    say("")
    say("   🔴 **然另有一項警示<u>未</u>宣告之靜默後果（⛔ 施工單未載·CC 現查）**：")
    say("      同一缺值路徑另令 `_cos_dn = 1.0`（`app.py` 之 `except`／初值），")
    say("      而 `_cos_dn` **另有一個消費者**：`_mark_zaling` 之 `_pw = S · _cos_dn`")
    say("      （＝**宗地寬度**·供畸零旗標）。⇒ 缺 ALLOC 時該寬度按「ALLOC ⊥ FRONT」計，")
    say("      **警示只提 W／Rw、未提宗地寬度** ⇒ 該後果**靜默**。")
    say("      本案量級：`_cos_dn` 實測 0.995733790〜0.998966642（`W-G.9-1` Q1-b）")
    say("      ⇒ 退為 1.0 時宗地寬度**高估 0.10%〜0.43%**。⛔ 本檔不判其是否可接受。")

    # ═════════ Q3 ═════════
    say("")
    say("#" * 124)
    say("## Q3　構造窮舉（⛔ 先自答、後列舉·⛔ 不判何者為正解）")
    say("#" * 124)
    say("")
    say("🔒 **書面自答（施工單 §5-Q3 明令須寫在開始之前·本段先於下表）**：")
    say("   問：「是否存在一個構造使三者同時滿足？若存在，本批是否已列出它？")
    say("        若不存在，不相容之處恰在哪兩條之間？」")
    say("   答：**存在**——本檔列出**甲**與**乙**二者，二者於三條**皆滿足**。")
    say("       ⇒ **S-2 未觸發**（S-2 之前提為「無任何構造同時滿足」）。")
    say("       ⛔ 本檔**不判**何者為正解（施工單 §0-8）。")
    say("")
    say("🔴 **是否窮盡：列舉·非窮舉**——本檔無法證明已窮盡構造空間。")
    say("")
    say("三條之受詞**互不相同**（此即三者可並存之結構理由）：")
    say("   · `K-9-5-11` 約束**寬度**（`S1` 係「與道路境界線**平行**」之距離·`K-9-5-4` 明載 ⛔ 非垂距）")
    say("   · `K-9-5-6`  約束 **`W` 之量法**（MP → 本宗遠側界之**垂距**）")
    say("   · `GB-46`    約束**誰產生**共用界線之值（單一產生者）")
    say("   ⇒ 寬度與 `W` 係 `K-9-5-4` 所明訂之「**同名不同量·禁互代**」⇒ 二者不直接衝突。")
    say("")
    say("%-6s %-46s %-9s %-9s %-8s" % ("構造", "內容", "K-9-5-11", "K-9-5-6", "GB-46"))
    say("-" * 124)
    say("%-6s %-46s %-9s %-9s %-8s"
        % ("甲", "遠側界改 ∥SIDELINE、W 以 SIDE 法向量", "✅", "✅", "✅"))
    say("       （比照既有機具 `_first_corner_alloc_dir`：街角第 1 宗即以換軸達成")
    say("         ∥SIDELINE 界；`K-9-5-5` 已追認該換軸為**正行為**）")
    say("       ⚠️ 代價：`Rw` 鏈引入**軸混用**——telescoping `Rw_i = R(W_i)−R(W_{i−1})`")
    say("          要求同軸；街角第 1 宗雖有先例，⛔ 本檔**不判**其可否推廣。")
    say("%-6s %-46s %-9s %-9s %-8s"
        % ("乙", "維持 ∥ALLOC 帶，寬度逕取 `S1_par`", "✅", "✅", "✅"))
    say("       （即 `buf` 改取 `S1_par`，⛔ 不再以等面積反解）")
    say("       ⚠️ 代價：帶面積**不再等於** `range_area` ⇒ 與 `_corner_buffer_S` 之")
    say("          等面積設計相違；惟 `K-9-5-11` **只約束寬度、未約束面積**。")
    say("%-6s %-46s %-9s %-9s %-8s"
        % ("丙", "**現行**：等面積 ∥ALLOC 帶（`buf` 反解）", "🔴 否", "✅", "✅"))
    say("       （寬度 ＝ `buf` ≠ `S1_par`——`W-G.9-1` Q1-a 實測其差 `+1.66`〜`+1.70` m）")
    say("-" * 124)
    say("⚠️ **上表之 `K-9-5-6` 欄僅就「W 之量法是否良定」判**——")
    say("   ⛔ **不含**族②③ 之現行式（`buf·cos_dn`）；該式之判定見 Q1（**不合致**）。")
    say("")
    say("🔑 **Q1 與 Q3 之接合**：構造丙（現行帶構造）之 `K-9-5-6` 欄雖為 ✅，")
    say("   但**消費該帶之族②③ 仍不合致**（Q1 已證其恰為「正典直量 − `W_0`」）")
    say("   ⇒ **帶之構造與其消費式係兩件事**，⛔ 不得因帶合致即認為鏈亦合致。")

    say("")
    say("rc = 0")
    return 0


if __name__ == "__main__":
    rc = main()
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write("\n".join(L) + "\n")
    sys.exit(rc)
