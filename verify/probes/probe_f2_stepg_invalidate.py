# -*- coding: utf-8 -*-
r"""補正 F-2：**Step G 停機後舊成果不得殘留**之三項驗證（段三(c)-3 §四 升格為正式探針）。

## 🔒 非套套邏輯

本檔**不重寫**失效邏輯，而是**自 `app.py` 原始碼抽出那幾行敘述**並 `exec` 之
⇒ 驗的是**倉內真正那幾行**；任何人改了那幾行，本檔的結論就會跟著變。
K-9-4 閘亦直接呼叫 `app.k94_assert_baseline_touch` 真符號。

## 三項

1. **成功路徑不變**：閘未 raise ⇒ `f3_G_values` 存在且為**新**成果、`f3_g_needs_rerun` 不存在。
2. **失敗路徑清乾淨**：閘 raise ⇒ `f3_G_values`／`f3_G_trace` **皆不存在**、`f3_g_needs_rerun` 為 `True`。
3. **紅線反向對照**：同一次失敗後 `f3_corner_winners`／`f3L_corner_winners` **仍在**
   ——證明未照抄 `_f3L_invalidate_g_cache` 之鍵名清單（那會連 Step G 之**上游輸入**一起 pop）。

## 重跑

    python verify/probes/probe_f2_stepg_invalidate.py

`rc=0` ⇒ 三項全過。輸出 `verify/out/F2_stepg_invalidate.log`。
"""
import os
import re
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


SRC = open(os.path.join(REPO, "app.py"), encoding="utf-8").read().split("\n")


def extract(after_pat, stop_pat, want):
    """自 app.py 抽出 `after_pat` 之後、`stop_pat` 之前，含 `want` 之敘述行（去註解、去縮排）。"""
    i = next(k for k, l in enumerate(SRC) if re.search(after_pat, l))
    j = next(k for k in range(i + 1, len(SRC)) if re.search(stop_pat, SRC[k]))
    return [l.strip() for l in SRC[i + 1:j]
            if l.strip() and not l.strip().startswith("#") and want in l]


INVAL = extract(r"^\s*detail_trace = \{\}\s*$", r"^\s*_params_for_g = dict\(", "session_state")
SUCC = [l.strip() for l in SRC if re.search(
    r"^\s*st\.session_state\['f3_G_(values|trace)'\] = (g_rows|detail_trace)$", l)]
SUCC += [l.strip() for l in SRC if "pop('f3_g_needs_rerun', None)" in l]

P("=" * 100)
P("【補正 F-2】Step G 停機後舊成果不得殘留（自 app.py 抽出真敘述並執行）")
P("=" * 100)
P("\n自 app.py 抽出之【失效區塊】敘述：")
for l in INVAL:
    P(f"    {l}")
P("自 app.py 抽出之【成功區塊】敘述：")
for l in SUCC:
    P(f"    {l}")
assert len(INVAL) == 3, f"失效區塊敘述數異常：{INVAL}"
assert len(SUCC) == 3, f"成功區塊敘述數異常：{SUCC}"


class FakeST:
    def __init__(self):
        self.session_state = {}


# ── 真資料 ────────────────────────────────────────────────────────────────────
ns, fake_st = harvest()
snapshot = rv.load_snapshot()
cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
v6 = open(rv.V6DXF, "rb").read()
tp, bp, _ = rv.build_build_parcels(ns, fake_st, v6, list(cb_by.values()), snapshot)
fcb = ns["F3_CATEGORY_BURDEN"]
bb = [b for b in cb_by.values() if fcb.get(b.get("category", ""), "") == "可建築土地"]
verts = {b["label"]: (b.get("vertices") or []) for b in bb}
BLS = cad.get("baselines", {}) or {}
bl = {l: ns["_baseline_pts_from_manual"](BLS.get(l), verts[l]) for l in verts}
params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, 0.0)
_, _, _, ws, fm = run_corner_pk(ns, fake_st, list(cb_by.values()), cad, params,
                                tp, bp, 0.0, snapshot=snapshot)
sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot,
                params, bp, ws, fm, 0.0)
land, _ = ns["k94_partition_land_rows"](sg["g_rows"])
OKB = {b["label"] for b in bb}
GOOD = [{"label": str(r.get("所屬街廓", "")), "pid": str(r.get("暫編地號", "")),
         "coords": r.get("cut_coords") or []}
        for r in land if str(r.get("所屬街廓", "")) in OKB]

# (i) 案擾動（沿用段二-1(c) §四）：某宗後緣頂點沿 BASELINE 法向推 0.5m
T = GOOD[0]
ax = ns["_baseline_normal_axis"](bl[T["label"]])
b0x, b0y, bnx, bny = ax
sgn = 1.0 if sum((float(q[0]) - b0x) * bnx + (float(q[1]) - b0y) * bny
                 for q in T["coords"]) > 0 else -1.0
BAD = [dict(T, coords=[((float(q[0]) + sgn * 0.5 * bnx), (float(q[1]) + sgn * 0.5 * bny))
                       if abs((float(q[0]) - b0x) * bnx + (float(q[1]) - b0y) * bny) <= 0.01
                       else (float(q[0]), float(q[1])) for q in T["coords"]])] \
      + [p for p in GOOD if p is not T]

OLD_G = [{"暫編地號": "舊成果-請勿殘留"}]
OLD_T = {"舊": "trace"}
WIN = {"R1": {"winner": "上游輸入·不得被清"}}


def scenario(tag, parcels):
    st = FakeST()
    st.session_state["f3_G_values"] = OLD_G
    st.session_state["f3_G_trace"] = OLD_T
    st.session_state["f3_corner_winners"] = WIN
    st.session_state["f3L_corner_winners"] = WIN
    g = {"st": st, "g_rows": None, "detail_trace": None}
    for l in INVAL:                              # ← app.py 真敘述
        exec(l, g)
    rows = ns["k94_baseline_touch_by_parcel"](parcels, bl)
    err = None
    try:
        ns["k94_assert_baseline_touch"](rows)
        g["g_rows"] = [{"暫編地號": "新成果"}]
        g["detail_trace"] = {"新": "trace"}
        for l in SUCC:                           # ← app.py 真敘述
            exec(l, g)
    except RuntimeError as e:
        err = str(e)
    return st.session_state, err


ok = True


def chk(desc, got, exp):
    global ok
    hit = (got == exp)
    ok &= hit
    P(f"    {desc:<52} → {got!r:<28}（期 {exp!r}）  {'OK' if hit else '🔴 FAIL'}")


# ── 驗證 1：成功路徑不變 ───────────────────────────────────────────────────────
ss, err = scenario("A", GOOD)
P("\n【驗證 1】成功路徑不變（Step G 正常跑完）")
P(f"    閘：{'未 raise ✅' if err is None else '🔴 raise（不應）'}")
ok &= (err is None)
chk("f3_G_values 存在", "f3_G_values" in ss, True)
chk("f3_G_values 已是新成果（非舊）", ss.get("f3_G_values"), [{"暫編地號": "新成果"}])
chk("f3_g_needs_rerun 不存在", "f3_g_needs_rerun" in ss, False)

# ── 驗證 2：失敗路徑清乾淨 ─────────────────────────────────────────────────────
ss2, err2 = scenario("B", BAD)
P("\n【驗證 2】失敗路徑清乾淨（K-9-4 閘 raise）")
P(f"    閘：{'raise ✅' if err2 else '🔴 未 raise（不應）'}")
ok &= bool(err2)
if err2:
    P(f"    訊息：{err2[:120]}")
chk("f3_G_values 不存在（舊成果已清）", "f3_G_values" in ss2, False)
chk("f3_G_trace 不存在（舊成果已清）", "f3_G_trace" in ss2, False)
chk("f3_g_needs_rerun 為 True", ss2.get("f3_g_needs_rerun"), True)

# ── 驗證 3：紅線反向對照（未誤清上游輸入）────────────────────────────────────
P("\n【驗證 3】紅線反向對照：同一次失敗後，上游輸入仍在")
chk("f3_corner_winners 仍在", ss2.get("f3_corner_winners"), WIN)
chk("f3L_corner_winners 仍在", ss2.get("f3L_corner_winners"), WIN)
P("    ⇒ 證明未照抄 _f3L_invalidate_g_cache 之鍵名清單（該清單會連上游輸入一起 pop）")

P("\n" + "=" * 100)
P(f"總結：{'✅ 三項驗證全過' if ok else '🔴 有項未過'}")
P("=" * 100)

with open(os.path.join(REPO, "verify", "out", "F2_stepg_invalidate.log"),
          "w", encoding="utf-8") as f:
    f.write("\n".join(OUT) + "\n")
sys.exit(0 if ok else 1)
