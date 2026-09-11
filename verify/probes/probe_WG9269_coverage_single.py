#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""`W-G.9-269` 補令四 `§三-2`：**單態**覆蓋帳量測器（`P-1` 之基準）。

🛑 **本器⛔ 取二態，活體檢依構造不適用；⛔ 後人以「補齊活體檢」為由加裝
   ——欲加者須先讀 `W-G.9-269` 補令四 `§三-2`。**
   （上句係單 `§三-2` 款 `(2)` 之**逐字**要求·⛔ 改寫·體例承 `268p 補令十四 §二-4`。）

🩸 **本器之存在理由**（補令四 `§三-1`／`自誤 356`）
   `P-1`（覆蓋帳維持歸零）原繫於 `probe_WG9268p_mem.py`——**旗標二態**器，
   其二態繫於 `WG9268P_ANCHOR_GEOM`，而該旗標已於 `W-G.9-268′ c3` **移除**
   （生產碼 `4` 檔命中 `0`）⇒ 其選擇器活體檢**必拒測**（`rc = 4`）
   ⇒ **`P-1` 於該器上結構上無從量**。
   🔒 **該器之拒絕判綠<u>正確</u>**（其即 `Q-3` 之受詞）；本器係**另立**，⛔ 取代、⛔ 修之。

🔒 **舊器之處置（`坑 24` 所令：令拆器須同時令舊器內之處置）**
   `probe_WG9268p_mem.py` **原地保留、⛔ 改一字**；其**覆蓋帳段自 `c3` 起結構上不可達**
   （其於 `assert_live` 處即 `return 4`）⇒ 於本線**⛔ 得再作為 `P-1` 之基準**。
   本器**⛔ 承接**其 `D-1`／`D-2`／`D-3` 三段——該三段之受詞非 `P-1`，其處置候發單側。

🔒 **四款**（補令四 `§三-2` 逐字）
  `(1)` **單態**——只量**當前工作樹**之覆蓋帳，**⛔ 態之切換**（本器全檔⛔ 觸 `os.environ`）。
  `(2)` **⛔ 裝選擇器活體檢**（見上首段之逐字宣告）。
  `(3)` **幾何自記憶體取**（`app_harvest` ＋ `rv.build_pipeline`／`run_step_g`），
        **⛔ 自 CSV、⛔ 依賴 `_partial`**。
  `(4)` **判別力 ＝ 人造三造**：相疊矩形須得 `1.0`／相離須得 `0.0`／
        **於一原綠之組注入 `+1㎡` 須轉紅**。**三造任一不成立 ⇒ loud 拒測。**

🔒 **幾何原語⛔ 另寫第二份定義**（`GB-48` 族）——`poly`／`as_coords`／`pairs_of`／`group`
   一律**自 `probe_WG9268p_mem.py` import**（其又沿用 `probe_WG9265_coverage_account.py` 之逐字）。

🔒 **出艙**（`P-1` 之新形所令）：本器**必印**其所量之 `commit` 與 `app.py` 之 blob `sha1`
   ——以證二次量測確為不同態。

用法：`python verify/probes/probe_WG9269_coverage_single.py`
`rc`：`0` 全綠／`2` **量測器紅**（三造不成立 ⇒ loud 拒測）／`5` 覆蓋帳非零（**受詞紅**）。
🛑 `rc ≠ 0` ⛔ 等同「受詞紅」——須讀其逐項（`坑 9`）。
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)          # 🔒 自 `__file__` 上溯·⛔ 硬編他樹（`GB-161`）
sys.path.insert(0, VERIFY)
sys.path.insert(0, os.path.join(VERIFY, "fixtures"))
sys.path.insert(0, HERE)

from shapely.ops import unary_union                                 # noqa: E402

from app_harvest import harvest                                     # noqa: E402
import run_verification as rv                                       # noqa: E402
from selection_pipeline import run_corner_pk                        # noqa: E402
from stepg_pipeline import run_step_g                               # noqa: E402

# 🔒 幾何原語：⛔ 另寫第二份定義
from probe_WG9268p_mem import poly, as_coords, pairs_of, group      # noqa: E402

SCEN = (("0m", 0.0), ("3.5m", 3.5))
W = 118
INJECT = 1.0                            # 造三之注入面積（㎡）


def _state():
    """本器所量之態（`P-1` 新形所令·⛔ 省）。"""
    def g(*a):
        r = subprocess.run(["git", "-C", REPO] + list(a),
                           capture_output=True, text=True)
        return r.stdout.strip() if r.returncode == 0 else "⛔ 可得"
    return g("rev-parse", "HEAD"), g("rev-parse", "HEAD:app.py"), g(
        "status", "--porcelain")


def controls(sample):
    """人造三造（補令四 `§三-2` 款 `(4)`）。回 (三造皆成立, 逐造之判)。

    `sample` ＝ 一**原綠**之組之 `[(x, y), …]` 清單（供造三之注入）。
    🛑 造三⛔ 以「轉紅」為足——須檢其紅之**理由**（注入對之面積 ≈ `INJECT`·`坑 17`）。
    """
    rows = []

    a = poly([(0, 0), (2, 0), (2, 1), (0, 1)])
    b = poly([(1, 0), (3, 0), (3, 1), (1, 1)])
    v1 = (a.area + b.area) - unary_union([a, b]).area
    ok1 = abs(v1 - 1.0) < 1e-9
    rows.append(("造一 [必紅] 人造相疊矩形 Σ−∪", "%.10f" % v1, "1.0", ok1))

    c = poly([(0, 0), (2, 0), (2, 1), (0, 1)])
    d = poly([(5, 0), (6, 0), (6, 1), (5, 1)])
    v2 = (c.area + d.area) - unary_union([c, d]).area
    ok2 = abs(v2) < 1e-12
    rows.append(("造二 [必綠] 人造相離矩形 Σ−∪", "%.10f" % v2, "0.0", ok2))

    # ── 造三：於一**原綠之組**注入 +1㎡ ⇒ 須轉紅，且其紅之理由須為該注入 ──
    #
    # 🩸 **本窗自捕（首版之缺陷·`自解款` 白名單類 `5`）**：首版將注入矩形錨於
    #    `tgt.bounds` 之**外接框左下角**——該角**⛔ 必在多邊形內**（宗地多為斜交四邊形）
    #    ⇒ 實測 `tgt ∩ inj` 恆 `0.000000` ⇒ 造三**必不成立**，而其紅**係器之紅、⛔ 受詞之紅**。
    #    **攔法**：改以 `buffer(-0.75)` 取**確在內部**之區，於其 `representative_point()`
    #    為心造邊長 `1.0` 之正方形——心到角之距 `√0.5 ≈ 0.707 < 0.75`
    #    ⇒ **該方全含於 `tgt`** ⇒ 重疊**恰 `INJECT` ㎡**（構造保證·⛔ 試誤）。
    if not sample:
        rows.append(("造三 [必轉紅] 原綠之組注入 +%.1f㎡" % INJECT,
                     "⛔ 可施行（無原綠之組）", "≈%.1f" % INJECT, False))
        return False, rows
    base = [poly(cc) for cc in sample]
    pre = pairs_of(base)
    half = INJECT / 2.0
    inner = None
    tgt = None
    # 取組內**面積最大**者（⛔ 取首筆——`G ≈ 0` 之退化宗容不下 1㎡ 之方）
    for cand in sorted(base, key=lambda p: -p.area):
        ring = cand.buffer(-(half + 0.25))
        if (not ring.is_empty) and ring.area > 0:
            tgt, inner = cand, ring
            break
    if tgt is None:
        rows.append(("造三 [必轉紅] 原綠之組注入 +%.1f㎡" % INJECT,
                     "⛔ 可施行（組內無容得下該方之宗）", "≈%.1f" % INJECT, False))
        return False, rows
    ctr = inner.representative_point()
    inj = poly([(ctr.x - half, ctr.y - half), (ctr.x + half, ctr.y - half),
                (ctr.x + half, ctr.y + half), (ctr.x - half, ctr.y + half)])
    got = pairs_of(base + [inj])
    new = [p for p in got if p not in pre]
    area_new = sum(p[2] for p in new)
    # 🛑 其紅之理由須為該注入（`坑 17`：⛔ 只看紅不紅）——
    #    注入所生之對，其面積須 ＝ `tgt ∩ inj`，且該交集須 ＝ `INJECT`（構造保證）。
    expect = tgt.intersection(inj).area
    ok3 = (len(pre) == 0 and len(new) > 0
           and abs(area_new - expect) < 1e-9
           and abs(expect - INJECT) < 1e-9)
    rows.append(("造三 [必轉紅] 原綠之組注入 %.1f㎡ 之方" % INJECT,
                 "原 %d 對 → %d 對·新增面積 %.10f" % (len(pre), len(got), area_new),
                 "原 0 對·新增 ＝ 交集 %.10f ＝ %.1f" % (expect, INJECT), ok3))
    return (ok1 and ok2 and ok3), rows


def measure():
    """單態：只量當前工作樹。回 {(tag, blk, side): [(i, j, area)…]}、組數、宗數。"""
    ns, fake_st = harvest()
    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp_p, build_p, _ = rv.build_build_parcels(
        ns, fake_st, v6, list(cb_by.values()), snapshot)
    print("🔒 記憶體側管線已建（`harvest()` ＋ `rv.build_pipeline` ＋ `build_build_parcels`）"
          "：街廓 `%d`／宗 `%d`" % (len(cb_by), len(build_p)))

    import contextlib
    import io
    out = {}
    for tag, sb in SCEN:
        params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, sb)
        _d0, _s2, _o2, wins, forced = run_corner_pk(
            ns, fake_st, list(cb_by.values()), cad, params, temp_p, build_p,
            sb, snapshot=snapshot)
        g_rows, ab = [], None
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                _sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot,
                                 params, build_p, wins, forced, sb,
                                 eff_min_build_by_blk={})
            g_rows = _sg["g_rows"]
        except RuntimeError as e:
            p = getattr(e, "partial", None) or {}
            g_rows = p.get("g_rows") or []
            ab = p.get("aborted_blk")
        gs = group(g_rows)
        print("  情境 %-5s ⇒ `g_rows` **%3d** 列／組 **%2d**／中止街廓 %s"
              % (tag, len(g_rows), len(gs), ab or "（無·跑完）"))
        for (blk, side), items in sorted(gs.items()):
            out[(tag, blk, side)] = ([poly(cc) for _r, cc in items],
                                     [cc for _r, cc in items])
    return out


def main():                                                         # noqa: C901
    head, appblob, porcelain = _state()
    print("=" * W)
    print("【`W-G.9-269` 補令四 `§三-2`】**單態**覆蓋帳量測器（`P-1` 之基準）")
    print("=" * W)
    print("🔒 所量之態（`P-1` 新形所令）")
    print("   `commit`          ＝ %s" % head)
    print("   `app.py` blob `sha1` ＝ %s" % appblob)
    print("   `git status --porcelain` ＝ %s"
          % ("（空·乾淨）" if not porcelain else "🟡 非空（%d 列）" % len(porcelain.splitlines())))
    print()

    groups = measure()
    print()

    # 供造三：取一**原綠**之組（逐對為空者）
    sample = None
    for k, (polys, coords) in sorted(groups.items()):
        if len(coords) >= 1 and not pairs_of(polys):
            sample = coords
            break

    print("── 判別力：人造三造（`§三-2` 款 `(4)`·三造任一不成立 ⇒ loud 拒測）──")
    ok, rows = controls(sample)
    for name, got, exp, good in rows:
        print("  %-36s 得 %-46s 期 %-32s %s"
              % (name, got, exp, "✅" if good else "🔴"))
    if not ok:
        print("\n🔴 **量測器紅**（三造未全成立）⇒ 本次輸出⛔ 出艙（`rc = 2`）")
        print("🛑 此係「**無從量**」，⛔「量得為零」、⛔「受詞紅」。")
        return 2
    print()

    print("=" * W)
    print("【覆蓋帳】逐組逐對交集面積（單態·`P-1` 之受詞）")
    print("=" * W)
    print("  %-26s %5s %s" % ("組", "宗數", "逐對（面積 ㎡）"))
    bad = []
    tot_pairs = 0
    for (tag, blk, side), (polys, coords) in sorted(groups.items()):
        prs = pairs_of(polys)
        tot_pairs += len(prs)
        if prs:
            bad.append(((tag, blk, side), prs))
        print("  %-26s %5d %s  %s"
              % ("%s·%s·%s" % (tag, blk, side), len(polys),
                 ("**0 對**" if not prs
                  else "／".join("(%d,%d) %.6f" % p for p in prs)),
                 "✅" if not prs else "🔴"))
    print()
    print("  母體基數 ＝ **%d** 組／**逐對總數 ＝ %d**" % (len(groups), tot_pairs))
    if bad:
        print("\n🔴 **覆蓋帳非零 ＝ %d 組**（**受詞紅**·⛔ 量測器紅）：" % len(bad))
        for k, prs in bad:
            print("   %s：%s" % ("·".join(k), prs))
        return 5
    print("\n🟢 **全部組之重疊對數 ⋀ 逐對面積皆為 `0`** ⇒ `P-1` 之受詞於本態**成立**")
    print("🔒 本判之態 ＝ `%s`（`app.py` blob `sha1` `%s`）" % (head, appblob))
    return 0


if __name__ == "__main__":
    sys.exit(main())
