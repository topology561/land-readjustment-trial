#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""`W-G.9-269` 補令十 `§三-2`：**`c2` 之三必答**（`G011` 之梯次／釋池之會計／`3.5m` 之不對稱）。

🩸 **本器之存在理由**（補令十 `§三-1` `(b)` 逐字）
   「**重複釋池之虞**：`F.0` 梯3 已令 `G025`／`G030` 之 `G` **全額釋回原街廓池**；
     `c2` 之閘一剔除又令其入調配池 ⇒ **同一筆地是否被釋池二次？**」
   🛑 **⛔ 以「守恆帳沒紅」推定為 `(甲)`**（單 `§三-2` 款 `2` 明令）——本器出艙其**機械依據**。

🔒 **三必答**
  `1` **`G011` 之四梯分級**：自 `wd4_tier_list.compute()` **當次實跑**取之（⛔ baseline·`GB-162`）。
  `2` **釋池之會計**：逐街廓出艙 `poolA`（trunk A）／`poolB`（trunk B ＝ `F.0` 後）／`池差`，
      **於旗標二態各量一次**，並以其差判 `(甲)` 同一筆 抑或 `(乙)` 二筆。
  `3` **`3.5m` 之不對稱**：逐情境出艙三宗之閘一判（`驗_B藍影`）與其是否落於終態 `g_rows`。

🔒 **⛔ 引任何自 `verify/baselines` 取得之數**（`GB-162`）——本器之數**全自當次實跑**。
🔒 **態宣告二值並報**（`坑 m`）：`git rev-parse HEAD:app.py` ⋀ `git hash-object app.py`（**以後者為實**）。
🛑 **本器⛔ 改任何生產碼**；其翻旗標係**以環境變數**為之（⛔ 改其預設之字面）。

用法：`python verify/probes/probe_WG9269_c2_pool.py`
`rc`：`0` 全綠／`2` **量測器紅**（對照組不如預期 ⇒ loud 拒測）／`3` 判定集為空（loud 拒測）。
🛑 `rc ≠ 0` ⛔ 等同「受詞紅」（`坑 9`）。
"""
import contextlib
import copy
import io
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)          # 🔒 自 `__file__` 上溯·⛔ 硬編他樹（`GB-161`）
sys.path.insert(0, VERIFY)
sys.path.insert(0, os.path.join(VERIFY, "fixtures"))
sys.path.insert(0, HERE)

from app_harvest import harvest                                     # noqa: E402
import run_verification as rv                                       # noqa: E402
from selection_pipeline import run_corner_pk                        # noqa: E402
from stepg_pipeline import run_step_g                               # noqa: E402
import wg9269_selector_liveness as _liveness                        # noqa: E402

W = 116
SCEN = (("0m", 0.0), ("3.5m", 3.5))
FLAG = "WG9269_K917_BACKFILL"
SUBJ = ("628-42(1)", "628-53(2)", "628-27(1)")
# 🔒 `wf_f0.TIER3_LOTS` 之逐字（**⛔ 於本器重寫**——執行期自 `wf_f0` 取）
GIDS = ("G011", "G025", "G030")


def _state():
    def g(*a):
        r = subprocess.run(["git", "-C", REPO] + list(a), capture_output=True, text=True)
        return r.stdout.strip() if r.returncode == 0 else "⛔ 可得"
    return (g("rev-parse", "HEAD"), g("rev-parse", "HEAD:app.py"),
            g("hash-object", os.path.join(REPO, "app.py")))


def build_base():
    """建管線至 `build_parcels`（⛔ 受旗標影響——旗標只在 `run_step_g` 內）。"""
    ns, fake_st = harvest()
    snap = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snap)
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp, build, _ = rv.build_build_parcels(ns, fake_st, v6, list(cb_by.values()), snap)
    return ns, fake_st, snap, cb_by, cad, temp, build


def trunkA(ns, fake_st, snap, cb_by, cad, temp, build, tag, sb):
    """trunk A：`run_corner_pk` ＋ `run_step_g`。回 (sg, params, wins, forced)。"""
    params = rv.build_param_table(ns, fake_st, cb_by, cad, snap, sb)
    _d, _s, _o, wins, forced = run_corner_pk(
        ns, fake_st, list(cb_by.values()), cad, params, temp, build, sb, snapshot=snap)
    with contextlib.redirect_stdout(io.StringIO()):
        sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snap, params, build,
                        wins, forced, sb, eff_min_build_by_blk={})
    return sg, params, wins, forced


def pool_of(sg):
    return {lbl: round(float(v["池總=幾何剩餘(㎡)"]), 2)
            for lbl, v in sg["pool_diag"].items()}


def measure(on):
    """於旗標某態量 trunk A ＋ `F.0`。回 {tag: {...}}。"""
    # 🩸 `W-G.9-269` 補令十四 `§三-2`（**本批自捕**）：原式之 `else` 為 `os.environ.pop(FLAG, None)`，
    #    其繫於**旗標之預設**；而 `c2` 已將該預設翻為 `"1"` ⇒ `pop` 後得 **`on`**
    #    ⇒ 二態**雙雙為 `on`** ⇒ 一切「Δ ＝ 0」之結論皆偽。⇒ 一律**顯式設值**。
    os.environ[FLAG] = "1" if on else "0"
    import wf_f0
    ns, fake_st, snap, cb_by, cad, temp, build = build_base()
    # 🛑 **選擇器活體檢**（補令十四 `§三-2`）：其可觀測量 ＝ `k917_should_drop` 之被呼叫次數。
    #    ⚠️ 須於 `wf_f0`／梯3 隔離量測**之前**讀之（該二者亦跑 `trunkA`、會累加）。
    _lvc = _liveness.install(ns)
    out, ctx = {}, {}
    for tag, sb in SCEN:
        sg, params, wins, forced = trunkA(ns, fake_st, snap, cb_by, cad, temp, build, tag, sb)
        out[tag] = {"gA": sg["g_rows"], "poolA": pool_of(sg), "sgA": sg}
        ctx[tag] = {"ns": ns, "fake_st": fake_st, "cb_by": cb_by, "cad": cad,
                    "snap": snap, "omap": dict(fake_st.session_state["t8_ownership_map"]),
                    "build": build, "params": params, "winners": wins, "forced": forced,
                    "setback": sb, "gA": sg["g_rows"], "poolA": sg["pool_diag"],
                    "temp": temp}
    # 🔒 讀計數並**卸下替身**（其後之 `wf_f0`／梯3 輪⛔ 計入本觀測量）
    out["_lv_n"] = None if _lvc is None else _lvc["n"]
    out["_lv_ns"] = ns
    _liveness.uninstall(ns, _lvc)
    err = None
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            f0 = wf_f0.compute(copy.deepcopy(ctx) if False else ctx)
        for tag, _sb in SCEN:
            out[tag]["pool_rows"] = f0[tag]["pool_rows"]
            out[tag]["removed"] = f0[tag]["removed"]
    except Exception as e:                                          # noqa: BLE001
        err = "%s: %s" % (type(e).__name__, e)
        for tag, _sb in SCEN:
            out[tag].setdefault("pool_rows", None)
            out[tag].setdefault("removed", None)
    # ── 🔑 梯3-only 之**隔離量測**（`F.0` 於二態皆拋時之替代）────────────
    #   受詞 ＝ 「`F.0` 梯3 釋池量」＝ `poolB(梯3 已移除) − poolA`。
    #   🛑 **其與 `wf_f0` 之別（照實·⛔ 頂替）**：本重跑**只移除 `TIER3_LOTS`**，
    #      ⛔ 施加級0／0′ 之合併決策、⛔ 跑 `GSA`／`k*`／旗標等錨檢。
    #      ⇒ 其為**梯3 一項之隔離效應**，⛔ `F.0` 之全量。
    #   🔒 `TIER3_LOTS` **執行期自 `wf_f0` 取**（⛔ 本器重寫·`GB-48`）。
    t3 = set(wf_f0.TIER3_LOTS)
    b_t3 = [tp for tp in build if tp.get("暫編地號") not in t3]
    for tag, sb in SCEN:
        try:
            sgt, _p, _w, _f = trunkA(ns, fake_st, snap, cb_by, cad, temp, b_t3, tag, sb)
            out[tag]["poolT3"] = pool_of(sgt)
            out[tag]["gT3"] = sgt["g_rows"]
        except Exception as e:                                      # noqa: BLE001
            out[tag]["poolT3"] = None
            out[tag]["t3err"] = "%s: %s" % (type(e).__name__, e)
    out["_tier3"] = list(wf_f0.TIER3_LOTS)
    out["_f0err"] = err
    return out


def main():                                                         # noqa: C901
    head, blob, work = _state()
    print("=" * W)
    print("【`W-G.9-269` 補令十 `§三-2`】`c2` 之三必答（`G011` 梯次／釋池會計／`3.5m` 不對稱）")
    print("=" * W)
    print("🔒 **態宣告二值並報**（`坑 m`·**以工作區之值為實**）")
    print("   `commit`                         ＝ %s" % head)
    print("   `app.py` `rev-parse HEAD:app.py` ＝ %s" % blob)
    print("   `app.py` `hash-object`（**實**）  ＝ %s" % work)
    print("   二值 %s" % ("**相同** ✅" if blob == work else "🔴 **相異** ⇒ 須具名"))
    print("")

    # ── 必答 1：`G011` 之四梯分級 ────────────────────────────────────
    print("── 必答 `1`：`G011` 之四梯分級（`wd4_tier_list.compute()` **當次實跑**·⛔ baseline）"
          + "─" * 14)
    import wd4_tier_list as w4
    with contextlib.redirect_stdout(io.StringIO()):
        w4res = w4.compute(fixture=False)
    ok_ctl = True
    for tag, _sb in SCEN:
        grp = w4res[tag]["groups"]
        tiers = {}
        for g in grp:
            tiers[g["梯次"]] = tiers.get(g["梯次"], 0) + 1
        print("  情境 `%-5s` 群數 **%d**／梯次分布 %s" % (tag, len(grp), tiers))
        # 對照組（必命中之已知成員·`自誤 362` 之立準 `A`）：梯3 二群須為 G025／G030
        # 🩸 **本器首版之框為 `== "梯3"` 而該欄之值逐字為 `"3"`**（裸數字·見梯次分布）
        #    ⇒ 得 `[]` ⋀ 對照組當場轉紅 ⇒ **立準 `A` 之施行實例**（否定判被對照組攔下）。
        t3 = sorted(g["歸戶鍵Gxxx"] for g in grp if str(g["梯次"]).strip() == "3")
        print("    梯3 之群（對照組［必命中之已知成員］·期 `['G025', 'G030']`）＝ %s %s"
              % (t3, "✅" if t3 == ["G025", "G030"] else "🔴"))
        if t3 != ["G025", "G030"]:
            ok_ctl = False
        for gid in GIDS:
            r = next((g for g in grp if g["歸戶鍵Gxxx"] == gid), None)
            if r is None:
                print("    🔴 `%s` ⛔ 在清單" % gid)
                ok_ctl = False
                continue
            print("    | `%s` | 軌別 `%s` | 宗數 `%s` | `ΣG_戶 %.2f ㎡` | **梯次 `%s`** | "
                  "對應v3級 `%s` | 阻卻 `%s` |"
                  % (gid, r["軌別"], r["宗數"], float(r["ΣG_戶(㎡)"]), r["梯次"],
                     r["對應v3級"], r["阻卻"]))
            print("      宗清單 ＝ `%s`" % r["宗清單"])
            print("      路徑標註 ＝ `%s`" % r["路徑標註"])
    # 人造哨兵（必為零·執行期組出·字面⛔ 出艙）
    fake_gid = "G" + "".join(chr(c) for c in (57, 57, 57))
    hit = [g for g in w4res["0m"]["groups"] if g["歸戶鍵Gxxx"] == fake_gid]
    print("  對照組乙［人造哨兵·**執行期組出**·字面⛔ 出艙］⇒ 命中 `%d`／期 `0` %s"
          % (len(hit), "✅" if not hit else "🔴"))
    if hit:
        ok_ctl = False
    if not ok_ctl:
        print("")
        print("🔴 **對照組未全如預期 ⇒ 量測器紅 ⇒ loud 拒測**（`坑 u`）")
        return 2
    print("  ⇒ **器非紅** ✅")
    print("")

    # ── 必答 2：釋池之會計（旗標二態）────────────────────────────────
    print("── 必答 `2`：釋池之會計（旗標 `off` ⋀ `on` 各量一次）" + "─" * 46)
    OFF = measure(False)
    ON = measure(True)
    # ── 🛑 **選擇器活體檢**（補令十四 `§三-2`）——置於**全部旗標相依之判定之前** ──
    #    🔒 上開「必答 `1`」（`G011` 之四梯分級）係 `wd4_tier_list` 之量、**旗標無關**
    #       ⇒ 其先於本檢⛔ 違「置於全部判定之前」之旨（本器逐字具名之）。
    print("── **選擇器活體檢**（補令十四 `§三-2`·其後之判定皆旗標相依）" + "─" * 40)
    _ok_a, _m_a = _liveness.check_flag_selector(ON["_lv_ns"])
    print("   " + _m_a)
    _ok_b, _m_b = _liveness.check_two_state(OFF["_lv_n"], ON["_lv_n"])
    print("   " + _m_b)
    if not (_ok_a and _ok_b):
        print("🛑 ⇒ **loud 拒測**（⛔ 判綠、⛔ 靜默續跑）")
        return 4
    print("")
    print("  🔒 `wf_f0.TIER3_LOTS`（執行期自 `wf_f0` 取·⛔ 本器重寫）＝ %s" % OFF["_tier3"])
    for st, name in ((OFF, "off"), (ON, "on")):
        if st["_f0err"]:
            print("  🟡 旗標 `%s` 之 `F.0` 拋出：%s" % (name, st["_f0err"]))
    for tag, _sb in SCEN:
        print("")
        print("  【情境 `%s`】" % tag)
        gidsA = {str(r.get("暫編地號", "")) for r in OFF[tag]["gA"]}
        gidsB = {str(r.get("暫編地號", "")) for r in ON[tag]["gA"]}
        print("    trunk A `g_rows` 列數： `off` **%d** ／ `on` **%d**"
              % (len(OFF[tag]["gA"]), len(ON[tag]["gA"])))
        print("    🔑 **機械依據（單 `§三-2` 款 `2` 所令）**——三宗是否仍在 `c2` 之配地母體"
              "（＝ trunk A 之 `g_rows`）：")
        for pid in SUBJ:
            print("      `%-12s` `off` %s ／ `on` %s"
                  % (pid, "**在**" if pid in gidsA else "⛔ 在",
                     "**在**" if pid in gidsB else "⛔ 在"))
        print("    逐街廓之池（`池總=幾何剩餘(㎡)`·⛔ 累加式）：")
        print("    | 街廓 | `poolA` off | `poolA` on | Δ(on−off) | `池差` off（`F.0` 釋池） "
              "| `池差` on | `poolB` off | `poolB` on |")
        print("    |---|---|---|---|---|---|---|---|")
        prA, prB = OFF[tag].get("pool_rows"), ON[tag].get("pool_rows")
        dA = {r["街廓"]: r for r in prA} if prA else {}
        dB = {r["街廓"]: r for r in prB} if prB else {}
        s_dA = s_dB = s_delta = 0.0
        for lbl in sorted(OFF[tag]["poolA"]):
            pa_o = OFF[tag]["poolA"][lbl]
            pa_n = ON[tag]["poolA"].get(lbl, float("nan"))
            d_o = dA.get(lbl, {}).get("池差(㎡)")
            d_n = dB.get(lbl, {}).get("池差(㎡)")
            pb_o = dA.get(lbl, {}).get("池_F.0(㎡)")
            pb_n = dB.get(lbl, {}).get("池_F.0(㎡)")
            s_delta += (pa_n - pa_o)
            s_dA += float(d_o or 0)
            s_dB += float(d_n or 0)
            print("    | `%s` | %.2f | %.2f | **%+.2f** | %s | %s | %s | %s |"
                  % (lbl, pa_o, pa_n, pa_n - pa_o,
                     ("%.2f" % d_o) if d_o is not None else "（`F.0` 未成）",
                     ("%.2f" % d_n) if d_n is not None else "（`F.0` 未成）",
                     ("%.2f" % pb_o) if pb_o is not None else "—",
                     ("%.2f" % pb_n) if pb_n is not None else "—"))
        # 🛑 **「未量」⛔ 與「量得為零」共用出艙碼**——`F.0` 未成者一律印 `⛔ 可得`，⛔ 印 `0.00`
        f_dA = ("**%.2f**" % s_dA) if prA else "**⛔ 可得**"
        f_dB = ("**%.2f**" % s_dB) if prB else "**⛔ 可得**"
        print("    | **Σ（帶號）** | — | — | **%+.2f** | %s | %s | — | — |"
              % (s_delta, f_dA, f_dB))
        print("    | **Σ|·|（絕對值）** | — | — | **%.2f** | %s | %s | — | — |"
              % (sum(abs(ON[tag]["poolA"][l] - OFF[tag]["poolA"][l])
                     for l in OFF[tag]["poolA"]),
                 ("**%.2f**" % sum(abs(float(dA.get(l, {}).get("池差(㎡)") or 0))
                                   for l in OFF[tag]["poolA"])) if prA else "**⛔ 可得**",
                 ("**%.2f**" % sum(abs(float(dB.get(l, {}).get("池差(㎡)") or 0))
                                   for l in OFF[tag]["poolA"])) if prB else "**⛔ 可得**"))

        # ── 🔑 梯3-only 之隔離量測（`F.0` 未成時之替代·⛔ 其全量）────────
        pt_o, pt_n = OFF[tag].get("poolT3"), ON[tag].get("poolT3")
        print("")
        print("    🔑 **梯3-only 隔離量測**（`poolT3 − poolA`·**只移除 `TIER3_LOTS`**·"
              "⛔ 施加合併決策、⛔ 跑錨檢 ⇒ **⛔ `F.0` 之全量**）：")
        if pt_o is None or pt_n is None:
            print("      🔴 **⛔ 可得**（`off`：%s ／ `on`：%s）"
                  % (OFF[tag].get("t3err", "—"), ON[tag].get("t3err", "—")))
        else:
            print("      | 街廓 | 梯3 釋池量 `off` | 梯3 釋池量 `on` | 判 |")
            print("      |---|---|---|---|")
            so = sn = 0.0
            for lbl in sorted(OFF[tag]["poolA"]):
                ro = pt_o[lbl] - OFF[tag]["poolA"][lbl]
                rn = pt_n[lbl] - ON[tag]["poolA"][lbl]
                so += ro
                sn += rn
                print("      | `%s` | %+.2f | %+.2f | %s |"
                      % (lbl, ro, rn,
                         "**on 已歸零**" if abs(rn) < 0.005 <= abs(ro) else
                         ("二態皆 ~0" if abs(ro) < 0.005 and abs(rn) < 0.005 else "—")))
            print("      | **Σ（帶號）** | **%+.2f** | **%+.2f** | — |" % (so, sn))
            print("      | **Σ|·|（絕對值）** | **%.2f** | **%.2f** | — |"
                  % (sum(abs(pt_o[l] - OFF[tag]["poolA"][l]) for l in OFF[tag]["poolA"]),
                     sum(abs(pt_n[l] - ON[tag]["poolA"][l]) for l in ON[tag]["poolA"])))
        if OFF[tag].get("removed") is not None:
            print("    `F.0` 之 `removed`（`off`）含三宗者 ＝ %s"
                  % sorted(p for p in SUBJ if p in set(OFF[tag]["removed"])))
        if ON[tag].get("removed") is not None:
            print("    `F.0` 之 `removed`（`on`）含三宗者 ＝ %s"
                  % sorted(p for p in SUBJ if p in set(ON[tag]["removed"])))

    # ── 必答 3：`3.5m` 之不對稱 ──────────────────────────────────────
    print("")
    print("── 必答 `3`：`3.5m` 之不對稱（逐情境具名·⛔ 併為一事）" + "─" * 42)
    print("  | 宗地 | 情境 | 閘一 `驗_B藍影`（`off` 態） | `off` 在 `g_rows` | `on` 在 `g_rows` |")
    print("  |---|---|---|---|---|")
    n_judged = 0
    for pid in SUBJ:
        for tag, _sb in SCEN:
            r = next((x for x in OFF[tag]["gA"]
                      if str(x.get("暫編地號", "")) == pid), None)
            v = (r or {}).get("驗_B藍影", "（該宗⛔ 在 `off` 之 `g_rows`）")
            inA = pid in {str(x.get("暫編地號", "")) for x in OFF[tag]["gA"]}
            inB = pid in {str(x.get("暫編地號", "")) for x in ON[tag]["gA"]}
            n_judged += 1
            print("  | `%s` | `%s` | `%s` | %s | %s |"
                  % (pid, tag, v, "在" if inA else "**⛔ 在**", "在" if inB else "**⛔ 在**"))
    if n_judged == 0:
        print("🔴 **判定集為空 ⇒ loud 拒測**")
        return 3
    print("  判定集基數 ＝ **%d** 格" % n_judged)
    return 0


if __name__ == "__main__":
    sys.exit(main())
