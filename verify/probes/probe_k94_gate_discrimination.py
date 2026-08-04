# -*- coding: utf-8 -*-
r"""K-9-4 BASELINE 臨接閘之**鑑別力三合成案**（K-6-A2 段二-1(c) §四·段三(c)-3 §四 升格為正式探針）。

## 為何是正式探針、不是拋棄式腳本

`CLAUDE.md` 常設紀律：「凡新增或修改落在 `main()` 內之可執行敘述，`run_all` 之名目集合結果
不得單獨作為驗收依據，**必須另附合成案**」。合成案若寫成拋棄式，日後動同一段碼時
會落入「**證據在（log 已入庫）、重跑器沒了**」⇒ 故升格為 `verify/probes/` 之正式探針
（相對路徑·可攜）。

## 三案（⛔ 皆以擾動**輸入**驅動·生產碼一字未改·**未調容差**）

| 案 | 擾動 | 期望 |
|---|---|---|
| 對照組 | 無 | 不 raise |
| (i) 未達 | 某宗後緣頂點沿 BASELINE 法向推 `0.5m` | raise【未配到屁股線】|
| (ii) 跨過 | 某街廓 BASELINE 沿法向往內平移約半個進深 | raise【跨過屁股線】＋切街廓指引 |
| (iii) 屁股線誤派 | R2 之 BASELINE 換成 #0/#2 那條 | raise【未配到】15/16 宗 |

⛔ **只調容差不算數**——那只證明比較會動，不證明閘能咬到真情形。

## 重跑

    python verify/probes/probe_k94_gate_discrimination.py

`rc=0` ⇒ 三案皆咬且對照組不咬；`rc=1` ⇒ 有案未咬到。
輸出 `verify/out/K9_4_gate_discrimination.log`。
"""
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

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8")
    except Exception:
        pass

OUT = []


def P(s=""):
    OUT.append(s)
    print(s)


ns, fake_st = harvest()
snapshot = rv.load_snapshot()
cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
v6 = open(rv.V6DXF, "rb").read()
tp, bp, _ = rv.build_build_parcels(ns, fake_st, v6, list(cb_by.values()), snapshot)
fcb = ns["F3_CATEGORY_BURDEN"]
bb = [b for b in cb_by.values() if fcb.get(b.get("category", ""), "") == "可建築土地"]
params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, 0.0)
_, _, _, ws, fm = run_corner_pk(ns, fake_st, list(cb_by.values()), cad, params,
                                tp, bp, 0.0, snapshot=snapshot)
sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot,
                params, bp, ws, fm, 0.0)
ok = {b["label"] for b in bb}
verts = {b["label"]: (b.get("vertices") or []) for b in bb}
BLS = cad.get("baselines", {}) or {}


def bl_by(over=None):
    o = over or {}
    return {l: ns["_baseline_pts_from_manual"](o.get(l, BLS.get(l)), verts[l]) for l in ok}


land, no_land = ns["k94_partition_land_rows"](sg["g_rows"])
BASE = [{"label": str(r.get("所屬街廓", "")), "pid": str(r.get("暫編地號", "")),
         "coords": r.get("cut_coords") or []}
        for r in land if str(r.get("所屬街廓", "")) in ok]

P("=" * 108)
P("【K-9-4 上閘鑑別力】三合成案例（臨時·不改生產碼·不調容差）")
P(f"母體：受配土地之宗 {len(BASE)}｜無地宗（現金補償/孤立公設地）{len(no_land)}")
P("=" * 108)


def run(tag, parcels, bl):
    rows = ns["k94_baseline_touch_by_parcel"](parcels, bl)
    try:
        ns["k94_assert_baseline_touch"](rows)
        return rows, None
    except RuntimeError as e:
        return rows, str(e)


# ── 對照組：未擾動 ────────────────────────────────────────────────────────────
rows0, err0 = run("base", BASE, bl_by())
P("\n【對照組】未擾動")
P(f"  閘結果 = {'🔴 raise' if err0 else '✅ 不 raise（零違例）'}")

# ── (i) 未達：某宗後緣頂點沿 BASELINE 法向往前推 0.5m ─────────────────────────
TGT = BASE[0]
ax = ns["_baseline_normal_axis"](bl_by()[TGT["label"]])
b0x, b0y, bnx, bny = ax
sgn = 1.0 if sum((float(q[0]) - b0x) * bnx + (float(q[1]) - b0y) * bny
                 for q in TGT["coords"]) > 0 else -1.0
moved = []
for q in TGT["coords"]:
    off = (float(q[0]) - b0x) * bnx + (float(q[1]) - b0y) * bny
    if abs(off) <= 0.01:                       # 後緣頂點
        moved.append((float(q[0]) + sgn * 0.5 * bnx, float(q[1]) + sgn * 0.5 * bny))
    else:
        moved.append((float(q[0]), float(q[1])))
case_i = [dict(TGT, coords=moved)] + [p for p in BASE if p is not TGT]
rows_i, err_i = run("i", case_i, bl_by())
P("\n【(i) 未達】把 %s/%s 之後緣頂點沿 BASELINE 法向推 0.5m" % (TGT["label"], TGT["pid"]))
P(f"  擾動宗之 gap：{[r for r in rows_i if r['pid'] == TGT['pid']][0]['gap']:.6f} m")
P(f"  閘結果 = {'🔴 raise ✅（咬到）' if err_i else '未 raise 🔴（閘失效）'}")
if err_i:
    P(f"  訊息：{err_i[:230]}")

# ── (ii) 跨過：某街廓 BASELINE 沿法向往內平移約半個進深 ───────────────────────
B2 = "R1"
d2 = ns["_compute_block_depth_alloc"](
    verts[B2], 0.0, (cad.get("alloc_dir_by_block", {}) or {}).get(B2),
    front_pts=[(cad["front_lines"][B2]["p1"]), (cad["front_lines"][B2]["p2"])],
    baseline_pts=bl_by()[B2])["D_avg"]
ax2 = ns["_baseline_normal_axis"](bl_by()[B2])
fp1 = cad["front_lines"][B2]["p1"]
s_front = (float(fp1[0]) - ax2[0]) * ax2[2] + (float(fp1[1]) - ax2[1]) * ax2[3]
sh = (1.0 if s_front > 0 else -1.0) * (d2 / 2.0)
mb2 = dict(BLS[B2])
mb2["point"] = (mb2["point"][0] + sh * ax2[2], mb2["point"][1] + sh * ax2[3])
rows_ii, err_ii = run("ii", BASE, bl_by({B2: mb2}))
_cr = [r for r in rows_ii if r["crosses"]]
P(f"\n【(ii) 跨過】{B2} 之 BASELINE 沿法向往街廓內平移 {abs(sh):.3f}m（≈半個進深 {d2}m）")
P(f"  該街廓實質橫跨之宗數：{len([r for r in _cr if r['label'] == B2])}")
P(f"  閘結果 = {'🔴 raise ✅（咬到）' if err_ii else '未 raise 🔴（閘失效）'}")
if err_ii:
    P(f"  訊息：{err_ii[:260]}")

# ── (iii) 屁股線誤派（主案）：R2 之 BASELINE 換成 #0/#2 那條（R1/R4 之屁股線）──
B3, SRC = "R2", "R1"
a_b3 = BLS[B3]["angle_deg"] % 180
a_src = BLS[SRC]["angle_deg"] % 180
rows_iii, err_iii = run("iii", BASE, bl_by({B3: dict(BLS[SRC])}))
_ms = [r for r in rows_iii if r["label"] == B3 and not r["touch"]]
_n3 = len([r for r in rows_iii if r["label"] == B3])
P(f"\n【(iii) 屁股線誤派·主案】{B3} 之 BASELINE 換成 {SRC} 之（＝#0/#2 那條·亦即 {B3} 之末端境界線）")
P(f"  兩線方位：{B3} 原 {a_b3:.4f}° vs 誤派 {a_src:.4f}°（夾角 {abs(a_b3 - a_src):.4f}°）")
P(f"  {B3} 受配宗 {_n3} 宗，其中未配到屁股線者 **{len(_ms)}** 宗")
if _ms:
    P("  逐宗（前 6）：" + "；".join(f"{r['pid']} 差 {r['gap']:.3f}m" for r in _ms[:6]))
_touch3 = [r for r in rows_iii if r["label"] == B3 and r["touch"]]
P(f"  仍碰得到該線者 {len(_touch3)} 宗"
  + ("（＝末端第 1 筆·符合『得兼任鄰街廓末端塊起始境界線』）" if _touch3 else ""))
P(f"  閘結果 = {'🔴 raise ✅（咬到）' if err_iii else '未 raise 🔴（閘失效）'}")
if err_iii:
    P(f"  訊息：{err_iii[:260]}")

P("\n" + "=" * 108)
_all = bool(err_i) and bool(err_ii) and bool(err_iii) and (err0 is None)
P(f"三案總結：對照組不 raise ＋ 三案皆 raise ⇒ {'✅ 閘具鑑別力' if _all else '🔴 有案未咬到'}")
P("=" * 108)

with open(os.path.join(REPO, "verify", "out", "K9_4_gate_discrimination.log"),
          "w", encoding="utf-8") as f:
    f.write("\n".join(OUT) + "\n")
sys.exit(0 if _all else 1)
