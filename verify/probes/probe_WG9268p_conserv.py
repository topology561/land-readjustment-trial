# -*- coding: utf-8 -*-
"""`W-G.9-268′` 補令六 `§三-2`：**守恆必答**（逐街廓**全宗母體**·⛔ 共同鍵子集）。

🔒 **本器所答之四欄**（補令六 `§三-2` 逐字）
  `ΣG`（前・後・增減·帶號）／`Σ池`（前・後・增減·帶號·**並具名其取數之落點與產出階段**）／
  `街廓面積`／**守恆殘差 ＝ `街廓面積 − ΣG − Σ池`**（**須為 `0`·容差具名**）。

🔑 **`Σ池` 之取數落點（本器之核心判·⛔ 沿用 `補令五 §六-2` 之推導式）**
  `補令五 §六-2` 以 **`抵費地 ＝ 街廓面積 − ΣG`** 記帳。該式若逕作 `Σ池`，
  則 `街廓面積 − ΣG − Σ池 ≡ 0` **恆真**（`自誤 245` 恆真族）⇒ **該閘證不出任何事**。
  🔒 **本器改取<u>獨立量測</u>之池**：`run_step_g` 之 `_sg['g_rows']` 中
  `推進側別 == '抵費地'` 之列之 **`幾何面積(㎡)`**（其 `解法 ＝ '幾何剩餘'`、`G(㎡) ≡ 0`）。
  ⇒ 殘差**⛔ 恆零**，係真正之守恆檢。

🔑 **`got_抵費地_退縮*.csv` ⛔ 得作為 `Σ池` 之取數端（＝ 補令六 `§三-2` 之 `(甲)`）**
  機械證據（正面列舉·`verify/run_verification.py`）：
    `:593` `run_corner_pk(...)` → 其第 `3` 回傳 `off`
    `:604` `_dump_csv(off, …got_抵費地_退縮{tag}.csv)`
    `:673` `run_step_g(...)`                       ← **在其後**
  而錨 `_wg9268p_anchor_advance` 之命中：`verify/stepg_pipeline.py` **`5`**／
  `verify/selection_pipeline.py` **`0`**（其唯一 `run_step_g` 字樣為 `:428` 之**註解**、⛔ 呼叫）
  ⇒ 該檔於**錨之上游階段**產出，其值**結構上**不反映本批之變動。

🛑 **中止街廓⛔ 判綠**：管線中止之街廓其池未必已生成 ⇒ 本器**具名列出並排除於判定集**，
   `⛔ 與「殘差為零」共用出艙碼`（`序 11 之一般化` 款 `二`／`三`）。判定集為空 ⇒ loud 拒測。

用法：`python verify/probes/probe_WG9268p_conserv.py [倉根]`（預設 ＝ 本檔上溯二層）。
🛑 本器**自行切換** `WG9268P_ANCHOR_GEOM` 以取 `off`／`on` 二態，⛔ 依賴外部環境變數。
"""
import contextlib
import io
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(HERE))
VERIFY = os.path.join(REPO, "verify")
sys.path.insert(0, VERIFY)
sys.path.insert(0, os.path.join(VERIFY, "fixtures"))
sys.path.insert(0, HERE)

from app_harvest import harvest                                     # noqa: E402
import wg9268p_selector_liveness as _LIVE                          # noqa: E402
import run_verification as rv                                       # noqa: E402
from selection_pipeline import run_corner_pk                        # noqa: E402
from stepg_pipeline import run_step_g                               # noqa: E402

FLAG = "WG9268P_ANCHOR_GEOM"
SCEN = (("0m", 0.0), ("3.5m", 3.5))
POOL_SIDE = "抵費地"
W = 118

# 🔒 容差之出處：`G(㎡)`／`幾何面積(㎡)`／`街廓面積(㎡)` 三欄於 `g_rows` 皆為 **2dp**
#   ⇒ 每列之捨入上界 `0.005`；一街廓之殘差上界 ＝ `(列數 ＋ 1) × 0.005`
#   （`＋1` ＝ `街廓面積` 自身之捨入）。**逐街廓具名、⛔ 用單一魔數。**
ROUND_HALF = 0.005


def drive(setback, flag_on, ns, fake_st, snapshot, cb_by, cad, build_p, temp_p):
    """跑一情境一態；回 (g_rows, aborted)。⛔ 掛間諜（本器不取錨值）。"""
    if flag_on:
        os.environ[FLAG] = "1"
    else:
        os.environ[FLAG] = '0'      # 🔒 顯式 off（⛔ pop ＝ 取預設·c2 後預設為 on）
    try:
        params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
        _d, _s, _off, wins, forced = run_corner_pk(
            ns, fake_st, list(cb_by.values()), cad, params, temp_p, build_p,
            setback, snapshot=snapshot)
        g_rows, aborted = [], None
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                _sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot,
                                 params, build_p, wins, forced, setback,
                                 eff_min_build_by_blk={})
            g_rows = _sg["g_rows"]
        except RuntimeError as e:
            p = getattr(e, "partial", None) or {}
            g_rows = p.get("g_rows") or []
            aborted = p.get("aborted_blk")
    finally:
        os.environ.pop(FLAG, None)
    return g_rows, aborted


def fnum(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def account(g_rows):
    """逐街廓之帳。回 {blk: dict}。**全宗母體**·⛔ 共同鍵子集。"""
    acc = {}
    for r in g_rows:
        blk = (r.get("所屬街廓") or "").strip()
        if not blk:
            continue
        a = acc.setdefault(blk, {"nG": 0, "sumG": 0.0, "absG": 0.0,
                                 "nP": 0, "sumP": 0.0, "absP": 0.0,
                                 "areas": set(), "rows": 0})
        a["rows"] += 1
        if str(r.get("街廓面積(㎡)")).strip() not in ("", "None"):
            a["areas"].add(round(float(r["街廓面積(㎡)"]), 6))
        if (r.get("推進側別") or "").strip() == POOL_SIDE:
            v = fnum(r.get("幾何面積(㎡)"))
            if v is not None:
                a["nP"] += 1
                a["sumP"] += v
                a["absP"] += abs(v)
        else:
            v = fnum(r.get("G(㎡)"))
            if v is not None:
                a["nG"] += 1
                a["sumG"] += v
                a["absG"] += abs(v)
    return acc


def controls():
    """否證對照（兩造·人造·先跑）：證本器之守恆算式非恆綠亦非恆紅。"""
    good = [{"所屬街廓": "X", "推進側別": "left", "G(㎡)": 60.0,
             "幾何面積(㎡)": 60.0, "街廓面積(㎡)": 100.0},
            {"所屬街廓": "X", "推進側別": POOL_SIDE, "G(㎡)": 0.0,
             "幾何面積(㎡)": 40.0, "街廓面積(㎡)": 100.0}]
    bad = [{"所屬街廓": "Y", "推進側別": "left", "G(㎡)": 60.0,
            "幾何面積(㎡)": 60.0, "街廓面積(㎡)": 100.0},
           {"所屬街廓": "Y", "推進側別": POOL_SIDE, "G(㎡)": 0.0,
            "幾何面積(㎡)": 25.0, "街廓面積(㎡)": 100.0}]
    ga = account(good)["X"]
    ba = account(bad)["Y"]
    rg = list(ga["areas"])[0] - ga["sumG"] - ga["sumP"]
    rb = list(ba["areas"])[0] - ba["sumG"] - ba["sumP"]
    okg, okb = abs(rg) < 1e-9, abs(rb - 15.0) < 1e-9
    print("  [必綠] 人造守恆案　殘差 ＝ %+.10f（須 0）%s" % (rg, "✅" if okg else "🔴"))
    print("  [必紅] 人造破守恆案 殘差 ＝ %+.10f（須 +15）%s" % (rb, "✅" if okb else "🔴"))
    return okg and okb


def main():                                                         # noqa: C901
    print("=" * W)
    print("【`W-G.9-268′` 補令六 `§三-2`】守恆必答（逐街廓·**全宗母體**）")
    print("=" * W)
    print()
    print("── 否證對照（守恆算式·人造·先跑）──")
    if not controls():
        print("🔴 量測器紅 ⇒ 本次輸出⛔ 出艙")
        return 2
    print()

    ns, fake_st = harvest()
    if not _LIVE.assert_live(ns, "probe_WG9268p_conserv.py"):
        print("🔴 選擇器活體檢不過 ⇒ 本次輸出⛔ 出艙（⛔ 判綠·⛔ 靜默續跑）")
        return 4
    print()
    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp_p, build_p, _ = rv.build_build_parcels(
        ns, fake_st, v6, list(cb_by.values()), snapshot)
    print("🔒 管線已建：街廓 `%d`／宗 `%d`" % (len(cb_by), len(build_p)))
    print()

    ST = {}
    for tag, sb in SCEN:
        for flag_on in (False, True):
            g_rows, aborted = drive(sb, flag_on, ns, fake_st, snapshot,
                                    cb_by, cad, build_p, temp_p)
            ST[(tag, flag_on)] = (g_rows, aborted, account(g_rows))
            print("🔒 [%-4s ／ 旗標 %-3s] `g_rows` ＝ **%d** 列（母體基數）"
                  "／中止街廓 ＝ %s／街廓數 ＝ %d"
                  % (tag, "on" if flag_on else "off", len(g_rows),
                     ("**%s**" % aborted) if aborted else "無",
                     len(ST[(tag, flag_on)][2])))
    print()

    # ── 逐 (情境, 街廓) 之四欄 ────────────────────────────────────
    print("=" * W)
    print("§ 一　逐 `(情境, 街廓)` 之守恆帳（**全宗母體**·帶號與絕對值並列）")
    print("=" * W)
    print()
    print("🔑 `Σ池` 之**取數落點** ＝ `run_step_g` 回傳 `_sg['g_rows']` 之")
    print("   `推進側別 == '抵費地'` 列之 **`幾何面積(㎡)`**（`解法 ＝ '幾何剩餘'`·`G(㎡) ≡ 0`）")
    print("🔑 `Σ池` 之**產出階段** ＝ `run_step_g`（**錨 `_wg9268p_anchor_advance` 之下游**）")
    print("🛑 ⛔ 取自 `got_抵費地_退縮*.csv` —— 該檔源於 `run_corner_pk`（錨之**上游**）·見 `§三`")
    print()

    stop = []
    undecidable = []
    decided = 0
    for tag, _sb in SCEN:
        go, ao, acco = ST[(tag, False)]
        gn, an, accn = ST[(tag, True)]
        blks = sorted(set(acco) | set(accn))
        print("── 情境 `%s` ── 中止街廓：`off` ＝ %s ／ `on` ＝ %s"
              % (tag, ao or "無", an or "無"))
        print("   %-5s %-9s %-11s %-11s %-9s %-11s %-11s %-11s %s"
              % ("街廓", "宗數(前→後)", "ΣG 前", "ΣG 後", "ΔΣG",
                 "Σ池 前", "Σ池 後", "ΔΣ池", "判"))
        for blk in blks:
            o = acco.get(blk)
            n = accn.get(blk)
            og = o["sumG"] if o else float("nan")
            ng = n["sumG"] if n else float("nan")
            op = o["sumP"] if o else float("nan")
            npv = n["sumP"] if n else float("nan")
            inc_o = bool(o) and blk != ao
            inc_n = bool(n) and blk != an
            mark = "🟢" if (inc_o and inc_n) else "🟡中止/缺"
            print("   %-5s %-9s %11.4f %11.4f %+9.4f %11.4f %11.4f %+11.4f %s"
                  % (blk,
                     "%s→%s" % (o["nG"] if o else "—", n["nG"] if n else "—"),
                     og, ng, (ng - og) if (o and n) else float("nan"),
                     op, npv, (npv - op) if (o and n) else float("nan"), mark))
        print()

        # 守恆殘差
        print("   守恆殘差 ＝ `街廓面積 − ΣG − Σ池`（容差 ＝ (列數＋1)×0.005·逐街廓具名）")
        print("   %-5s %-6s %-12s %-11s %-11s %-11s %-9s %s"
              % ("街廓", "態", "街廓面積", "ΣG", "Σ池", "殘差", "容差", "判"))
        for blk in blks:
            for lbl, a, ab in (("off", acco.get(blk), ao), ("on", accn.get(blk), an)):
                if not a:
                    print("   %-5s %-6s %s" % (blk, lbl, "🟡 該態無此街廓 ⇒ ⛔ 判（loud）"))
                    undecidable.append((tag, blk, lbl, "該態無此街廓"))
                    continue
                if len(a["areas"]) != 1:
                    print("   %-5s %-6s 🛑 `街廓面積` 相異值 %d 個 ⇒ loud 拒測"
                          % (blk, lbl, len(a["areas"])))
                    stop.append((tag, blk, lbl, "街廓面積不唯一"))
                    continue
                area = list(a["areas"])[0]
                res = area - a["sumG"] - a["sumP"]
                tol = (a["rows"] + 1) * ROUND_HALF
                if blk == ab:
                    print("   %-5s %-6s %12.4f %11.4f %11.4f %+11.4f %9.4f  "
                          "🟡 **中止街廓** ⇒ ⛔ 判（池未必已生成·loud）"
                          % (blk, lbl, area, a["sumG"], a["sumP"], res, tol))
                    undecidable.append((tag, blk, lbl, "中止街廓"))
                    continue
                ok = abs(res) <= tol
                decided += 1
                if not ok:
                    stop.append((tag, blk, lbl, "殘差 %+.4f > 容差 %.4f" % (res, tol)))
                print("   %-5s %-6s %12.4f %11.4f %11.4f %+11.4f %9.4f  %s"
                      % (blk, lbl, area, a["sumG"], a["sumP"], res, tol,
                         "✅" if ok else "🛑 **逾容差**"))
        print()

        # 帶號 ＋ 絕對值合計（`CLAUDE.md` 鐵律：二者必須並列）
        cg = [(accn[b]["sumG"] - acco[b]["sumG"]) for b in blks
              if b in acco and b in accn]
        cp = [(accn[b]["sumP"] - acco[b]["sumP"]) for b in blks
              if b in acco and b in accn]
        print("   🔒 共有街廓之合計（帶號 ／ 絕對值·二者並列）")
        print("      ΣΔ(ΣG) ＝ %+.4f ／ Σ|Δ(ΣG)| ＝ %.4f" % (sum(cg), sum(abs(v) for v in cg)))
        print("      ΣΔ(Σ池) ＝ %+.4f ／ Σ|Δ(Σ池)| ＝ %.4f" % (sum(cp), sum(abs(v) for v in cp)))
        print()

    print("=" * W)
    print("§ 二　判")
    print("=" * W)
    print("   判定集基數 ＝ **%d**（(情境,街廓,態) 之可判者）" % decided)
    if decided == 0:
        print("   🛑 判定集為空 ⇒ **loud 拒測**（⛔ 判綠）")
        return 3
    print("   ⛔ 可判者 ＝ **%d** 項（逐項具名·⛔ 與「殘差為零」共用出艙碼）：" % len(undecidable))
    for t in undecidable:
        print("      🟡 %s" % (t,))
    if stop:
        print()
        print("   🛑 **停機款觸發**（補令六 `§三-2`）：%d 項逾容差" % len(stop))
        for t in stop:
            print("      🛑 %s" % (t,))
        return 1
    print()
    print("   ✅ **全部可判者之守恆殘差皆在其具名容差內** ⇒ 停機款**未觸發**")
    return 0


if __name__ == "__main__":
    sys.exit(main())
