# -*- coding: utf-8 -*-
"""`W-G.9-269` `c4` `§三-(b)`：`GB-160` 閘 `γ` 之**重量**（退化之宗移出配地母體後·**單態**）。

🩸 **既有二器何以皆⛔ 可用（逐項機械具名·⛔ 推定）**
  `(A)` `probe_WG9268p_c2_v1prime_mem.py`：其二態由旗標 `WG9268P_ANCHOR_GEOM` 驅動，
        而該旗標已由 `W-G.9-268′` `c3` **移除** ⇒ 其選擇器活體檢 **loud 拒測**
        （本批當場實測 `rc = 4`·落檔 `verify/out/WG9269Rc4_gb160.log`）⇒ 結構上量不到本受詞（坑 `ae`）。
  `(B)` `probe_WG9266_V1prime_3groups.py`：其資料源 ＝ `got_G值_退縮3.5m_partial.csv`，
        而 `_partial` **只在管線中止時產生**；病一落地後管線**已跑完** ⇒ 該檔⛔ 存在（**自毀式**·補令八 `§二`）。
        且**完整落檔⛔ 帶 `cut_coords` 欄**（本批實測：`18` 支 `got_*` 逐檔皆⛔ 含該欄）
        ⇒ 自落檔量 `γ` 於結構上**不可能**。

🔑 **本器之作法**：閘 `γ`（共用邊恰 `2` 頂點）係**單態**之自我驗證閘，**⛔ 需二態**
  ⇒ 以**記憶體側**驅動生產管線**一次**（現態·旗標已不存在 ⇒ 遞補迴圈無條件執行），
  取其 `g_rows` 之 `cut_coords`，再以**倉內既有 `V1` 之 `side_rows`／`shared_edge` 逐字**判 `γ`。
  🔒 ⇒ **⛔ 另寫第二份 `γ` 之定義**（`GB-48` 族）；**⛔ 改 `V1` 一字**；**⛔ 改任何生產碼一字**。
  🛑 **⛔ 以 `environ.pop(FLAG)` 取態**——本器**⛔ 觸任何旗標**（其已不存在）。

🔒 **判別力二造（⛔ 恆綠亦⛔ 恆紅）**
  `(甲)` 一**未受本批影響**之側 ⇒ 其 `γ` 須能全過（證閘能綠）；
  `(乙)` **注入式**：將受詞側之一宗 `cut_coords` 平移 `+1000 m`（必然破壞共用邊）
        ⇒ 其 `γ` 須**轉紅**（證閘能紅·`常規八` 二 ②）。
  🛑 二造任一不如預期 ⇒ **量測器紅** ⇒ ⛔ 出艙任何判。

用法：`python verify/probes/probe_WG9269_c4_gamma.py [倉根]`
`rc`：`0` 量得並出艙／`3` 母體為 `0`（loud 拒測）／`5` **量測器紅**（二造不如預期）。
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
import run_verification as rv                                       # noqa: E402
from selection_pipeline import run_corner_pk                        # noqa: E402
from stepg_pipeline import run_step_g                               # noqa: E402

import probe_WG9266_V1prime_3groups as V1                           # noqa: E402

SB = 3.5                     # 🔒 `GB-160` 之受詞逐字為 `3.5m`
TAG = "3.5m"
TARGETS = [("R5", "left"), ("R6", "right")]          # `GB-160` 所載之二側
CONTROL_A = ("R3", "left")                            # 造甲：未受本批影響之側
OLD = {("R5", "left"): (3, 5), ("R6", "right"): (3, 4)}   # `GB-160` 所載之舊值


def to_csv_like(g_rows):
    """記憶體側 → CSV 形（`cut_coords` 還原為**字串**·其餘轉 `str`）。⛔ 靜默丟列。"""
    out, skipped = [], 0
    for r in g_rows:
        cc = r.get("cut_coords")
        if isinstance(cc, str):
            s = cc
        elif cc:
            s = repr([[float(a), float(b)] for a, b in cc])
        else:
            s = ""
            skipped += 1
        d = {}
        for k, v in r.items():
            d[k] = s if k == "cut_coords" else ("" if v is None else str(v))
        out.append(d)
    return out, skipped


def gamma(rows, blk, side):
    """逐字沿用 `V1.side_rows` ＋ `V1.shared_edge`。回 (過數, 對數, 明細, 宗數)。"""
    items = V1.side_rows(rows, blk, side)
    detail = []
    for i in range(len(items) - 1):
        sh = V1.shared_edge(items[i][1], items[i + 1][1])
        detail.append(((items[i][0].get("暫編地號") or "").strip(),
                       (items[i + 1][0].get("暫編地號") or "").strip(), len(sh)))
    ng = sum(1 for _a, _b, n in detail if n == 2)
    return ng, len(detail), detail, len(items)


def main():                                                         # noqa: C901
    print("=" * 112)
    print("【`W-G.9-269` `c4` `§三-(b)`】`GB-160` 閘 `γ` 之重量（情境 `%s`·**單態·記憶體側**）" % TAG)
    print("=" * 112)
    print("🔒 判準之來源 ＝ 倉內既有 `probe_WG9266_V1prime_3groups` 之 `side_rows`／`shared_edge`（逐字·⛔ 改一字）")
    print("🛑 本器**⛔ 觸任何旗標**（`WG9268P_ANCHOR_GEOM` 已由 `W-G.9-268′` `c3` 移除）")
    print()

    ns, fake_st = harvest()
    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp_p, build_p, _ = rv.build_build_parcels(
        ns, fake_st, v6, list(cb_by.values()), snapshot)
    fl = cad["front_lines"]
    print("🔒 管線已建：街廓 `%d`／宗 `%d`／`FRONT_LINE` `%d` 街廓（生產解析器 `cad['front_lines']`）"
          % (len(cb_by), len(build_p), len(fl)))

    params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, SB)
    _d, _s, _off, wins, forced = run_corner_pk(
        ns, fake_st, list(cb_by.values()), cad, params, temp_p, build_p,
        SB, snapshot=snapshot)
    aborted = None
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            _sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot,
                             params, build_p, wins, forced, SB,
                             eff_min_build_by_blk={})
        g_rows = _sg["g_rows"]
    except RuntimeError as e:
        p = getattr(e, "partial", None) or {}
        g_rows = p.get("g_rows") or []
        aborted = p.get("aborted_blk")
    rows, skipped = to_csv_like(g_rows)
    print("🔒 `g_rows` **%d** 列（母體基數）／中止街廓 %s／⛔ 帶 `cut_coords` 之列 **%d**"
          % (len(rows), aborted or "無·跑完", skipped))
    print()
    if not rows:
        print("🛑 母體為 **0** 列 ⇒ **loud 拒測**（⛔ 靜默綠）")
        return 3

    print("── 受詞（`GB-160` 所載之二側）──")
    print("   %-14s %-8s %-10s %-10s %s" % ("側", "宗數", "相鄰對數", "閘 γ", "判"))
    res = {}
    for blk, side in TARGETS:
        res[(blk, side)] = gamma(rows, blk, side)
        ng, npair, _d2, nlot = res[(blk, side)]
        print("   %-14s %-8d %-10d %-10s %s"
              % ("%s·%s" % (blk, side), nlot, npair, "%d/%d" % (ng, npair),
                 "🛑 母體為 0 ⇒ ⛔ 靜默綠" if npair == 0
                 else ("✅ 過" if ng == npair else "🔴 不過")))
    print()
    print("── 逐對明細 ──")
    for blk, side in TARGETS:
        ng, npair, detail, _n = res[(blk, side)]
        print("   ▸ %s·%s" % (blk, side))
        for a, b, n in detail:
            print("       %-24s ─ %-24s 共用頂點 **%d** %s"
                  % (a, b, n, "✅" if n == 2 else "🔴"))
    print()

    print("── 判別力二造 ──")
    cb, cs = CONTROL_A
    ngA, npA, _dA, _nA = gamma(rows, cb, cs)
    okA = (npA > 0 and ngA == npA)
    print("   造甲［未受本批影響·須能全過］ %s·%s ⇒ γ %d/%d ⇒ %s"
          % (cb, cs, ngA, npA, "✅ 能綠" if okA else "🔴"))

    import ast
    tb, ts = TARGETS[0]
    items = V1.side_rows(rows, tb, ts)
    victim = (items[1][0].get("暫編地號") or "").strip() if len(items) > 1 else None
    inj, nmoved = [], 0
    for r in rows:
        d = dict(r)
        if ((d.get("所屬街廓") or "").strip() == tb
                and (d.get("推進側別") or "").strip() == ts
                and (d.get("暫編地號") or "").strip() == victim):
            v = ast.literal_eval((d.get("cut_coords") or "").strip())
            d["cut_coords"] = str([(float(a) + 1000.0, float(b)) for a, b in v])
            nmoved += 1
        inj.append(d)
    ngB, npB, _dB, _nB = gamma(inj, tb, ts)
    okB = (npB > 0 and ngB < npB)
    print("   造乙［注入·必轉紅］ %s·%s 之 `%s` 平移 +1000 m（改 **%d** 列）⇒ γ %d/%d ⇒ %s"
          % (tb, ts, victim, nmoved, ngB, npB, "✅ 能紅" if okB else "🔴 **閘失能**"))
    print()
    if not (okA and okB):
        print("🛑 **量測器紅**（二造未如預期）⇒ ⛔ 出艙任何判（坑 `u`）")
        return 5
    print("   ⇒ 量測器判 ＝ ✅ **非紅**（能綠亦能紅）")
    print()

    print("── 與 `GB-160` 所載之舊值對照 ──")
    print("   %-14s %-14s %-14s %s" % ("側", "GB-160 舊值", "本批重量", "判"))
    allpass = True
    for blk, side in TARGETS:
        ng, npair, _d3, _n = res[(blk, side)]
        o = OLD[(blk, side)]
        ok = (npair > 0 and ng == npair)
        allpass &= ok
        print("   %-14s %-14s %-14s %s"
              % ("%s·%s" % (blk, side), "%d/%d" % o, "%d/%d" % (ng, npair),
                 "🟢 已過" if ok else "🔴 仍不過"))
    print()
    print("🔒 判：%s" % ("🟢 二側之閘 `γ` 皆已過 ⇒ `GB-160` 之「無從量」已解"
                        if allpass else
                        "🔴 仍有側不過 ⇒ 成因⛔ 在退化幾何，須另診並具名（補令十六 `§三-(b)`）"))
    print("=" * 112)
    return 0


if __name__ == "__main__":
    sys.exit(main())
