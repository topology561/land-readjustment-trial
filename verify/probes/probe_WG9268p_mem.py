# -*- coding: utf-8 -*-
"""`W-G.9-268′` 補令五 `§三-2`：**記憶體側**取幾何之量測器（覆蓋帳／`D-1`／`D-2`／`D-3`）。

🩸 **本器之存在理由**（補令五 `§三-1`）：`got_G值_退縮*_partial.csv` **只在管線中止時產生**
   且**只有它有 `cut_coords`**（`53` 欄 vs 完整檔之 `50` 欄）
   ⇒ `probe_WG9265_coverage_account.py`（其 `SCEN` 寫死 `_partial`）於**旗標 `on`**（管線跑完）之態
   **`FileNotFoundError`** ⇒ 🔴 **併線前必答第 `1` 項於「修好」之態結構上不可量**。
   🔒 **通則（補令五 `§三-1` 逐字）**：**凡驗收條件所繫之量測管道，其存在本身若取決於「缺陷仍在」，
   該條件即為自毀式，⛔ 立。立閘時須同時問：「此閘所欲驗之事成立時，此閘還量得到嗎？」**

🔒 **本器之四款**（補令五 `§三-2`）
  `1.` **幾何之取得 ＝ 記憶體側**——`run_step_g` 之回傳 `_sg['g_rows']`（或中止時 `e.partial['g_rows']`）
       之 `cut_coords`，**⛔ 自 CSV 取**。
  `2.` **幾何之真值 ＝ 生產碼之 `_oblique_s_max`／`_strip_axis`**（`#20` 單一真相源）
       ——**⛔ 另寫第二份定義、⛔ 用擬合框**（`c0-5` 之擬合框已依補令五 `§二` **降級·⛔ 為驗收端**）。
  `3.` 🛑 **自我驗證閘（硬·不過即 loud 拒測·`rc ≠ 0`）**：於**旗標 `off`** 之態，
       記憶體側 `cut_coords` 與 `partial` CSV 同欄**逐位相符**；覆蓋帳逐組逐對與 `S-6` 既有實測**逐位相符**。
  `4.` **⛔ 改** `probe_WG9265_coverage_account.py` 一字（其為既有落檔之來源）；本器係**另立**。

🔑 **錨之真值取得法 ＝ 對 `ns['_wg9268p_anchor_advance']` 掛<u>間諜</u>**
   ——其記錄**生產碼實際傳入之引數**（`cum_S`／`cut_coords`／`d_hat`／`base_pt`／`allocation_dir`），
   **⛔ 於器內重新推導 `d_hat`／`corner_pt`／`alloc`**（重導即開第二份定義·`GB-48` 族）。

🩸 **`cut_coords` 之二側形**：**記憶體側為 `list`、落檔側為<u>字串</u>**
   ⇒ 只吃字串之 parser 於記憶體側會落入靜默退路。本器**二形皆吃**並具名。

用法：`python verify/probes/probe_WG9268p_mem.py [輸出目錄]`（預設 `verify/out`）。
🛑 本器**自行切換** `WG9268P_ANCHOR_GEOM` 以取 `off`／`on` 二態，⛔ 依賴外部環境變數。
"""
import ast
import csv
import io
import os
import sys
import contextlib
from itertools import combinations

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
sys.path.insert(0, VERIFY)
sys.path.insert(0, os.path.join(VERIFY, "fixtures"))
sys.path.insert(0, HERE)

from shapely.geometry import Polygon                                # noqa: E402
from shapely.ops import unary_union                                 # noqa: E402

from app_harvest import harvest                                     # noqa: E402
import wg9268p_selector_liveness as _LIVE                          # noqa: E402
import run_verification as rv                                       # noqa: E402
from selection_pipeline import run_corner_pk                        # noqa: E402
from stepg_pipeline import run_step_g                               # noqa: E402

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(VERIFY, "out")
SCEN = (("0m", 0.0), ("3.5m", 3.5))
TOL_OVL = 1e-6
TOL_CUM = 0.01                  # `累積S(m)` 之 2dp 捨入
DP = 4
FLAG = "WG9268P_ANCHOR_GEOM"

# 🔒 閘之靶（`S-6` 覆蓋帳之既有實測·**⛔ 本器所生**·補令五 `§三-2 3.` 逐字）
GATE_TARGET = {
    ("0m", "R2", "left"): [19.8142, 26.1624],
    ("3.5m", "R5", "left"): [56.8186],
}
W = 126
FAIL = []


def poly(coords):
    """沿用 `probe_WG9265_coverage_account.py` 之逐字（⛔ 另寫第二份幾何原語）。"""
    p = Polygon(coords)
    if not p.is_valid:
        p = p.buffer(0)
    return p


def as_coords(v):
    """🩸 記憶體側為 `list`、落檔側為**字串** ⇒ 二形皆吃（⛔ 靜默退路）。"""
    if v is None:
        return None
    if isinstance(v, str):
        s = v.strip()
        if not s:
            return None
        try:
            v = ast.literal_eval(s)
        except Exception:                                           # noqa: BLE001
            return None
    try:
        out = [(float(a), float(b)) for a, b in v]
    except Exception:                                               # noqa: BLE001
        return None
    return out if len(out) >= 3 else None


def pairs_of(polys):
    out = []
    for (i, p1), (j, p2) in combinations(list(enumerate(polys)), 2):
        a = p1.intersection(p2).area
        if a > TOL_OVL:
            out.append((i, j, a))
    return out


def controls():
    a = poly([(0, 0), (2, 0), (2, 1), (0, 1)])
    b = poly([(1, 0), (3, 0), (3, 1), (1, 1)])
    v = (a.area + b.area) - unary_union([a, b]).area
    c = poly([(0, 0), (2, 0), (2, 1), (0, 1)])
    d = poly([(5, 0), (6, 0), (6, 1), (5, 1)])
    v2 = (c.area + d.area) - unary_union([c, d]).area
    print("  [必紅] 人造相疊矩形 Σ−∪ ＝ %.10f（須 1.0）%s"
          % (v, "✅" if abs(v - 1.0) < 1e-9 else "🔴"))
    print("  [必綠] 人造相離矩形 Σ−∪ ＝ %.10f（須 0.0）%s"
          % (v2, "✅" if abs(v2) < 1e-12 else "🔴"))
    return abs(v - 1.0) < 1e-9 and abs(v2) < 1e-12


def drive(setback, flag_on, ns, fake_st, snapshot, cb_by, cad, build_p, temp_p):
    """跑一情境一態；回 (g_rows, anchor_calls, aborted)。"""
    calls = []
    orig = ns["_wg9268p_anchor_advance"]
    osm = ns["_oblique_s_max"]

    def spy(cum_S, cut_coords, d_hat, base_pt, allocation_dir):
        out = orig(cum_S, cut_coords, d_hat, base_pt, allocation_dir)
        s_geo = None
        cc = as_coords(cut_coords)
        if cc is not None and d_hat is not None and base_pt is not None:
            try:
                s_geo = osm(cc, d_hat, base_pt, allocation_dir)
            except Exception:                                       # noqa: BLE001
                s_geo = None
        calls.append({"cum_in": float(cum_S), "cum_out": float(out),
                      "s_geo": (None if s_geo is None else float(s_geo)),
                      "n_pts": (0 if cc is None else len(cc)),
                      # 🔑 以 `cut_coords` **全部頂點**為鍵。
                      #   🩸 **⛔ 用首頂點**——實測 `0m·R2·left` 之 `628-41(1)` 與 `628-42(1)`
                      #      **首頂點相同**（共用界線之端點）⇒ 首頂點鍵會碰撞而誤標宗（本器自捕）。
                      "key": (None if cc is None else
                              tuple((round(x, 6), round(y, 6)) for x, y in cc))})
        return out

    ns["_wg9268p_anchor_advance"] = spy
    if flag_on:
        os.environ[FLAG] = "1"
    else:
        os.environ[FLAG] = '0'      # 🔒 顯式 off（⛔ pop ＝ 取預設·c2 後預設為 on）
    params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
    _d0, _s2, _o2, wins, forced = run_corner_pk(
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
        ns["_wg9268p_anchor_advance"] = orig
        os.environ.pop(FLAG, None)
    return g_rows, calls, aborted


def group(g_rows):
    """回 {(街廓, 側): [row…]}（組內以 `累積S(m)` 昇冪）。"""
    gs = {}
    for r in g_rows:
        cc = as_coords(r.get("cut_coords"))
        if cc is None:
            continue
        k = ((r.get("所屬街廓") or "").strip(), (r.get("推進側別") or "").strip())
        gs.setdefault(k, []).append((r, cc))
    for k in gs:
        gs[k].sort(key=lambda t: float(t[0].get("累積S(m)") or 0))
    return gs


def cov(gs, tag):
    """覆蓋帳：逐組逐對。回 {(tag,blk,side): [(i,j,area)…]}。"""
    out = {}
    for (blk, side), items in sorted(gs.items()):
        out[(tag, blk, side)] = pairs_of([poly(c) for _r, c in items])
    return out


def main():                                                         # noqa: C901
    print("=" * W)
    print("【`W-G.9-268′` 補令五 `§三-2`】記憶體側取幾何之量測器（覆蓋帳／`D-1`／`D-2`／`D-3`）")
    print("=" * W)
    print()
    print("── 否證對照（幾何原語·人造·先跑）──")
    if not controls():
        print("🔴 量測器紅 ⇒ 本次輸出⛔ 出艙")
        return 2
    print()

    ns, fake_st = harvest()
    if not _LIVE.assert_live(ns, "probe_WG9268p_mem.py"):
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
    print("🔒 記憶體側管線已建（`harvest()` ＋ `rv.build_pipeline` ＋ `build_build_parcels`）"
          "：街廓 `%d`／宗 `%d`" % (len(cb_by), len(build_p)))
    print()

    ST = {}
    for tag, sb in SCEN:
        for flag in (False, True):
            g_rows, calls, ab = drive(sb, flag, ns, fake_st, snapshot,
                                      cb_by, cad, build_p, temp_p)
            ST[(tag, flag)] = {"rows": g_rows, "calls": calls, "aborted": ab,
                               "gs": group(g_rows)}
            print("  情境 %-5s 旗標 %-3s ⇒ `g_rows` **%3d** 列／錨呼叫 **%3d** 次／中止街廓 %s"
                  % (tag, "on" if flag else "off", len(g_rows), len(calls), ab or "（無·跑完）"))
    print()

    # ── 閘一：記憶體側 `cut_coords` ＝ `partial` CSV 同欄（**off 態**）────────
    print("=" * W)
    print("【閘一·硬】`off` 態之記憶體側 `cut_coords` ＝ `_partial` CSV 同欄（**逐位**）")
    print("=" * W)
    n_cmp = 0
    for tag, _sb in SCEN:
        p = os.path.join(OUT, "got_G值_退縮%s_partial.csv" % tag)
        if not os.path.exists(p):
            FAIL.append("閘一：`%s` ⛔ 存在 ⇒ loud 拒測" % os.path.basename(p))
            print("  🔴 `%s` ⛔ 存在 ⇒ **loud 拒測**（⛔ 靜默綠）" % os.path.basename(p))
            continue
        with io.open(p, encoding="utf-8-sig", newline="") as f:
            csv_rows = {r["暫編地號"]: r for r in csv.DictReader(f)}
        mem = {r.get("暫編地號"): r for r in ST[(tag, False)]["rows"]}
        common = [k for k in csv_rows if k in mem]
        bad = []
        for k in common:
            a = as_coords(csv_rows[k].get("cut_coords"))
            b = as_coords(mem[k].get("cut_coords"))
            if a != b:
                bad.append(k)
            n_cmp += 1
        print("  情境 %-5s 共同鍵 **%2d** 格／逐位相異 **%d** 格 %s"
              % (tag, len(common), len(bad), "✅" if not bad else "🔴 " + str(bad[:5])))
        if bad:
            FAIL.append("閘一：%s 有 %d 格之 `cut_coords` 相異" % (tag, len(bad)))
    if n_cmp == 0:
        FAIL.append("閘一之判定集為空 ⇒ loud 拒測（⛔ 靜默綠）")
    else:
        print("  判定集基數 ＝ **%d** 格" % n_cmp)
    print("  🩸 二側之形：落檔為**字串**、記憶體為 **`list`** ⇒ 本器二形皆吃後再比（⛔ 靜默退路）")
    print()

    # ── 閘二：覆蓋帳（off 態）＝ `S-6` 之既有實測 ──────────────────
    print("=" * W)
    print("【閘二·硬】`off` 態之覆蓋帳逐組逐對 ＝ `S-6` 之既有實測（**逐位**·%ddp）" % DP)
    print("=" * W)
    print("  🔒 靶之來源 ＝ 補令五 `§三-2 3.` 逐字（其源 ＝ `S-6`·**⛔ 本器所生**）")
    off_cov = {}
    for tag, _sb in SCEN:
        off_cov.update(cov(ST[(tag, False)]["gs"], tag))
    print("  %-24s %6s %-34s %-34s %s" % ("組", "宗數", "本器（逐對·4dp）", "S-6 之靶", "判"))
    for k in sorted(off_cov):
        got = sorted(round(a, DP) for _i, _j, a in off_cov[k])
        want = sorted(round(a, DP) for a in GATE_TARGET.get(k, []))
        n = len(ST[(k[0], False)]["gs"].get((k[1], k[2]), []))
        ok = got == want
        print("  %-24s %6d %-34s %-34s %s"
              % ("%s·%s·%s" % k, n, str(got), str(want), "✅" if ok else "🔴"))
        if not ok:
            FAIL.append("閘二：%s 本器 %s ≠ 靶 %s" % ("%s·%s·%s" % k, got, want))
    print()

    if FAIL:
        print("=" * W)
        print("🔴 **硬閘紅 ＝ %d 項** ⇒ 本次輸出⛔ 出艙（`rc ≠ 0`）：" % len(FAIL))
        for x in FAIL:
            print("   · %s" % x)
        print("=" * W)
        return 3

    # ── 覆蓋帳（on 態）＝ 併線前必答第 1 項 ────────────────────────
    print("=" * W)
    print("【一】覆蓋帳（**`on` 態**·＝ 原單 `§六` 併線前必答第 `1` 項）")
    print("=" * W)
    on_cov = {}
    for tag, _sb in SCEN:
        on_cov.update(cov(ST[(tag, True)]["gs"], tag))
    tot = 0
    print("  %-24s %6s %-24s %s" % ("組", "宗數", "逐對（面積 ㎡）", "判"))
    for k in sorted(on_cov):
        pr = on_cov[k]
        n = len(ST[(k[0], True)]["gs"].get((k[1], k[2]), []))
        tot += len(pr)
        print("  %-24s %6d %-24s %s"
              % ("%s·%s·%s" % k, n,
                 ("／".join("%d×%d %.4f" % p for p in pr) if pr else "**0 對**"),
                 "🔴" if pr else "✅"))
    print("  母體基數 ＝ **%d** 組（`on` 態）／**逐對總數 ＝ %d**" % (len(on_cov), tot))
    print("  ⇒ %s" % ("🟢 **全部可達組之重疊對數 ⋀ 逐對面積皆為 `0`** ⇒ 併線前必答第 `1` 項 **成立**"
                      if tot == 0 else "🔴 **仍有重疊 ⇒ 停機上呈**"))
    if tot:
        FAIL.append("`on` 態覆蓋帳仍有 %d 對重疊" % tot)
    print()

    # ── D-1：以生產碼之 `_oblique_s_max` 為端 ─────────────────────
    print("=" * W)
    print("【`D-1`】錨之位移（**端 ＝ 生產碼之 `_oblique_s_max`**·補令五 `§二` 之降級後）")
    print("=" * W)
    print("  🔒 引數**取自間諜**（生產碼實傳之 `cut_coords`／`d_hat`／`base_pt`／`alloc`）"
          "——⛔ 於器內重導。")
    for tag, _sb in SCEN:
        for flag in (False, True):
            cs = ST[(tag, flag)]["calls"]
            ok = [c for c in cs if c["s_geo"] is not None]
            big = [c for c in ok if abs(c["s_geo"] - c["cum_in"]) > TOL_CUM]
            moved = [c for c in cs if abs(c["cum_out"] - c["cum_in"]) > 1e-12]
            print("  情境 %-5s 旗標 %-3s：呼叫 %3d／可算 `s_geo` %3d／"
                  "`|s_geo − cum_S| > %.2f` **%2d**／**錨實際移動 %2d** 次"
                  % (tag, "on" if flag else "off", len(cs), len(ok), TOL_CUM,
                     len(big), len(moved)))
            for c in big:
                print("      · `cum_S ＝ %.4f` → `s_geo ＝ %.4f`（**δ ＝ %+.4f**）"
                      "／實際 `cum_out ＝ %.4f`"
                      % (c["cum_in"], c["s_geo"], c["s_geo"] - c["cum_in"], c["cum_out"]))
    print()

    # ── D-2 / D-3 ─────────────────────────────────────────────
    print("=" * W)
    print("【`D-2`】最終態之位置變動（級聯）：`Δ累積S` ＝ `on` − `off`（**共同鍵**）")
    print("=" * W)
    D2 = {}
    for tag, _sb in SCEN:
        a = {r.get("暫編地號"): r for r in ST[(tag, False)]["rows"]}
        b = {r.get("暫編地號"): r for r in ST[(tag, True)]["rows"]}
        for k in a:
            if k not in b:
                continue
            try:
                x, y = float(a[k]["累積S(m)"]), float(b[k]["累積S(m)"])
            except (TypeError, ValueError, KeyError):
                continue
            D2[(tag, k)] = (x, y, y - x, (b[k].get("驗_宗序") or "").strip(),
                            (b[k].get("所屬街廓") or "").strip(),
                            (b[k].get("推進側別") or "").strip())
    big = {k: v for k, v in D2.items() if abs(v[2]) > TOL_CUM}
    print("  %-6s %-16s %-10s %11s %11s %11s" % ("情境", "暫編地號", "驗_宗序", "off", "on", "Δ"))
    for k in sorted(big, key=lambda x: (x[0], big[x][0])):
        v = big[k]
        print("  %-6s %-16s %-10s %11.4f %11.4f %+11.4f"
              % (k[0], k[1], v[3][:8], v[0], v[1], v[2]))
    print("  母體基數（共同鍵）＝ **%d** 格／`|Δ| > %.2f` 者 ＝ **%d** 格"
          % (len(D2), TOL_CUM, len(big)))
    s = [v[2] for v in D2.values()]
    print("  **Σ Δ（帶號）＝ %+.4f m** ／ **Σ|Δ| ＝ %.4f m**"
          % (sum(s), sum(abs(x) for x in s)))
    print()
    print("=" * W)
    print("【`D-3`】鏈頭之對位（`驗_宗序 == '街角第1宗'`·**⛔ 上游可級聯**）")
    print("=" * W)
    heads = {k: v for k, v in D2.items() if v[3] == "街角第1宗"}
    print("  %-6s %-16s %-6s %-6s %11s %11s %11s"
          % ("情境", "暫編地號", "街廓", "側", "off", "on", "Δ累積S"))
    for k in sorted(heads, key=lambda x: (x[0], heads[x][4], heads[x][5])):
        v = heads[k]
        print("  %-6s %-16s %-6s %-6s %11.4f %11.4f %+11.4f"
              % (k[0], k[1], v[4], v[5], v[0], v[1], v[2]))
    print("  鏈頭母體基數 ＝ **%d** 格" % len(heads))
    print()

    # ── 【`D-1` 附表】逐宗之生產 `_oblique_s_max`（補令五 `§一-2` 之重得）──
    print("=" * W)
    print("【`D-1` 附表】逐宗之**生產 `_oblique_s_max`**（補令五 `§一-2` 之自行重得）")
    print("=" * W)
    print("  🔑 識別法 ＝ 以 `cut_coords` **全部頂點**為鍵與 `g_rows` 對映（⛔ 首頂點·其會碰撞）"
          "——⛔ 於器內另行推導宗序／街廓／側。")
    for tag, _sb in SCEN:
        st = ST[(tag, False)]
        idx = {}
        for r in st["rows"]:
            cc = as_coords(r.get("cut_coords"))
            if cc:
                idx[tuple((round(x, 6), round(y, 6)) for x, y in cc)] = r
        seen = {}
        for c in st["calls"]:
            if c["key"] in idx and c["key"] not in seen:
                seen[c["key"]] = c
        print("  ── 情境 %s（旗標 `off`）·可對映 %d／%d 呼叫 ──"
              % (tag, len(seen), len(st["calls"])))
        print("    %-6s %-8s %-16s %-10s %11s %13s %11s"
              % ("街廓", "側", "暫編地號", "驗_宗序", "累積S", "生產 s_max", "max() 後"))
        for k, c in sorted(seen.items(),
                           key=lambda kv: ((idx[kv[0]].get("所屬街廓") or ""),
                                           (idx[kv[0]].get("推進側別") or ""),
                                           kv[1]["cum_in"])):
            r = idx[k]
            print("    %-6s %-8s %-16s %-10s %11.4f %13s %11.4f"
                  % ((r.get("所屬街廓") or "")[:5], (r.get("推進側別") or "")[:6],
                     (r.get("暫編地號") or "")[:15], (r.get("驗_宗序") or "")[:8],
                     c["cum_in"],
                     ("%.4f" % c["s_geo"]) if c["s_geo"] is not None else "—",
                     c["cum_out"]))
    print()

    print("=" * W)
    if FAIL:
        print("🔴 **閘紅 ＝ %d 項** ⇒ `rc ≠ 0`：" % len(FAIL))
        for x in FAIL:
            print("   · %s" % x)
        print("=" * W)
        return 3
    print("✅ 全閘綠：否證對照 ⋀ 閘一（記憶體 ＝ `partial` CSV）⋀ 閘二（覆蓋帳 ＝ `S-6`）"
          " ⋀ `on` 態覆蓋帳全數歸零")
    print("=" * W)
    return 0


if __name__ == "__main__":
    sys.exit(main())
