# -*- coding: utf-8 -*-
"""`c1` 之**合成案**（`CLAUDE.md`：`main()` 內之敘述，`run_all` ⛔ 單獨作為驗收依據）。

🩸 **本案之必要性**：`c1` 之四呼叫點中，**二處落於 `app.py` 之 `def main()` 內**
   （AST 實查·見 `§三`）；`harvest()` 以 AST 跳過 UI、harness 走 `run_step_g`
   ⇒ **該二處從不被 `run_all`／`run_verification` 執行**。
   ⇒ 其驗收**必須**另附合成案（`CLAUDE.md` 之「🔒 `main()` 內之敘述」款）。

🔒 **期望值之來源（⛔ 由本碼現跑回填·`fixture-provenance`）**：
   `_strip_s_range` 之 docstring 逐字載**恆等式** `s(corner_pt + s0·d_hat) ≡ s0`
   ⇒ 以 `corner_pt + s_i·d̂ + u_j·n̂` 造點者，其 `max strip` **閉式恆為 `max(s_i)`**。
   本案即以此閉式為期望值，**⛔ 現跑回填**。
"""
import ast
import io
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = (r"C:/Users/admin/Desktop/land-readjustment-trial/.claude/worktrees"
        r"/w-g-9-268p-s1-correction-f41d70")
sys.path.insert(0, os.path.join(REPO, "verify"))
os.chdir(REPO)

sys.path.insert(0, HERE)
from app_harvest import harvest                                     # noqa: E402
import wg9268p_selector_liveness as _LIVE                          # noqa: E402

FAIL = []


def chk(name, got, want, tol=1e-9):
    ok = (want is None and got is None) or (
        got is not None and want is not None and abs(got - want) <= tol)
    print("  %-58s 得 %-18s 期 %-18s %s"
          % (name, ("%.10f" % got) if got is not None else "None",
             ("%.10f" % want) if want is not None else "None", "✅" if ok else "🔴"))
    if not ok:
        FAIL.append(name)


W = 118
print("=" * W)
print("【`W-G.9-268′` `c1` 合成案】`_wg9268p_anchor_advance`（**`main()` 內之敘述⛔ 由 run_all 驗**）")
print("=" * W)
print()

ns, _fake_st = harvest()      # 🩸 harvest() 回 (ns, fake_st) 之 tuple（本器首版誤取為 dict·自捕）

# ── 選擇器活體檢（補令十一 `§二-2`·置於全部判定之前）────────────────
# 🔴 **本支之活體檢⛔ 為本倉之證據**：上方 `REPO` 係**硬編之他窗 worktree**
#    （且 `os.chdir(REPO)`）⇒ `harvest()` 所讀者為**該樹之 `app.py`**、⛔ 本倉者。
#    ⇒ 縱 `c3` 於本倉移除旗標，只要該他窗之樹仍存旗標，本檢仍會通過 ⇒ **假綠**。
#    🛑 其處置（改 `REPO` 之取得法）**逾補令十一之授權** ⇒ 已具名上呈，⛔ 於本批自行修。
print("🛑 **本支之 `REPO` 係硬編之他窗 worktree** ⇒ 下列活體檢之受詞為**該樹**，⛔ 本倉")
print("   `REPO` ＝ %s" % REPO)
if not _LIVE.assert_live(ns, "probe_WG9268p_c1_synth.py（受詞 ＝ 硬編之他窗樹）"):
    print("🔴 選擇器活體檢不過 ⇒ 本次輸出⛔ 出艙（⛔ 判綠·⛔ 靜默續跑）")
    sys.exit(4)
print()

adv = ns["_wg9268p_anchor_advance"]
osm = ns["_oblique_s_max"]
print("🔒 受測符號自 `harvest()` 取得：`_wg9268p_anchor_advance` %s ／ `_oblique_s_max` %s"
      % (callable(adv), callable(osm)))
print()

# ── 合成幾何（**斜交**·⛔ 正交特例·`_strip_axis` docstring 之戒）──────────
d_hat = (1.0, 0.0)
corner = (100.0, 200.0)
_a = math.radians(93.7)                       # ALLOC 與 FRONT 斜交 3.7°（UC9898 實測帶 2.6–5.3°）
alloc = (math.cos(_a), math.sin(_a))
n_hat = (-alloc[1], alloc[0])
S_LIST = [0.5, 2.0, 7.25, 3.0]                # ⇒ 閉式期望 max strip ＝ 7.25
U_LIST = [-4.0, 11.0]
CC = [[corner[0] + s * d_hat[0] + u * n_hat[0],
       corner[1] + s * d_hat[1] + u * n_hat[1]]
      for s in S_LIST for u in U_LIST]
S_GEO = max(S_LIST)

print("── 合成之閉式自證（`_oblique_s_max` ＝ `max(s_i)`·恆等式 `s(corner+s0·d̂) ≡ s0`）──")
print("   斜交角 ＝ %.1f°（⛔ 正交）／頂點 %d 個／`s_i` ＝ %s"
      % (math.degrees(_a) - 90.0, len(CC), S_LIST))
chk("`_oblique_s_max`（閉式期望 max(s_i)）", float(osm(CC, d_hat, corner, alloc)), S_GEO, 1e-9)
print()

print("── 造 `a`：旗標 **off** ⇒ **原值原樣**（⛔ 觸幾何）──")
os.environ["WG9268P_ANCHOR_GEOM"] = "0"
chk("off·`cum_S ＝ 1.0` 而 `s_geo ＝ 7.25`（須仍 1.0）", float(adv(1.0, CC, d_hat, corner, alloc)), 1.0)
os.environ.pop("WG9268P_ANCHOR_GEOM", None)
chk("off（環境變數**未設**）·同上", float(adv(1.0, CC, d_hat, corner, alloc)), 1.0)
print()

print("── 造 `b`：旗標 **on** ∧ `s_geo > cum_S` ⇒ **須變為 `s_geo`**（判別力·證非死碼）──")
os.environ["WG9268P_ANCHOR_GEOM"] = "1"
chk("on·`cum_S ＝ 1.0` ⇒ 須 `7.25`", float(adv(1.0, CC, d_hat, corner, alloc)), S_GEO)
print()

print("── 造 `c`：旗標 **on** ∧ `s_geo < cum_S` ⇒ **取 `max` ⇒ ⛔ 後退**──")
chk("on·`cum_S ＝ 9.0` ⇒ 須仍 `9.0`", float(adv(9.0, CC, d_hat, corner, alloc)), 9.0)
print()

print("── 造 `d`：旗標 **on** ∧ 幾何缺 ⇒ 原值（⛔ 靜默造值）──")
chk("on·`cut_coords ＝ []`", float(adv(3.5, [], d_hat, corner, alloc)), 3.5)
chk("on·`cut_coords ＝ None`", float(adv(3.5, None, d_hat, corner, alloc)), 3.5)
chk("on·`d_hat ＝ None`", float(adv(3.5, CC, None, corner, alloc)), 3.5)
chk("on·`base_pt ＝ None`", float(adv(3.5, CC, d_hat, None, alloc)), 3.5)
print()

print("── 造 `e`：旗標 **on** ∧ 帶軸退化（切線 ∥ 推進向）⇒ **須 raise**（no-silent-fallback）──")
try:
    v = adv(1.0, CC, d_hat, corner, (0.0, 1.0))     # n̂ ＝ (−1,0)、m̂ ＝ (0,−1) ⇒ denom ＝ 0
    print("  %-58s 得 %-18s 期 %-18s 🔴" % ("退化 ⇒ 須 raise", repr(v), "RuntimeError"))
    FAIL.append("退化未 raise")
except RuntimeError as e:
    ok = "_strip_axis" in str(e)
    print("  %-58s %s %s" % ("退化 ⇒ raise（loud）", str(e)[:40] + "…", "✅" if ok else "🔴"))
    if not ok:
        FAIL.append("退化 raise 之訊息⛔ 出自 `_strip_axis`")
os.environ.pop("WG9268P_ANCHOR_GEOM", None)
print()

# ── §三　四呼叫點之 AST 實查 ────────────────────────────────────
print("=" * W)
print("【§三】四呼叫點之 **AST 實查**（⛔ 硬編行號·⛔ 以 grep 代）")
print("=" * W)
SITES = {"app.py": [], "verify/stepg_pipeline.py": []}
for p in SITES:
    tree = ast.parse(io.open(os.path.join(REPO, p), encoding="utf-8").read())
    mains = [n for n in ast.walk(tree)
             if isinstance(n, ast.FunctionDef) and n.name == "main"]
    rng = (mains[0].lineno, mains[0].end_lineno) if mains else None
    for nd in ast.walk(tree):
        if not isinstance(nd, ast.Call):
            continue
        f = nd.func
        nm = f.id if isinstance(f, ast.Name) else getattr(f, "attr", None)
        if nm != "_wg9268p_anchor_advance":
            continue
        args = []
        for a in nd.args:
            if isinstance(a, ast.Name):
                args.append(a.id)
            elif isinstance(a, ast.Call):
                args.append(ast.unparse(a))
            else:
                args.append(ast.unparse(a))
        SITES[p].append((nd.lineno, tuple(args),
                         bool(rng and rng[0] <= nd.lineno <= rng[1])))
    print("  %-28s `def main` 區間 ＝ %s" % (p, rng))
    for ln, args, inmain in SITES[p]:
        print("      :%-6d 引數 %d ＝ %s   **在 `main()` 內 ＝ %s**"
              % (ln, len(args), args, inmain))

tot = sum(len(v) for v in SITES.values())
print("  呼叫點總數 ＝ %d（須 4）%s" % (tot, "✅" if tot == 4 else "🔴"))
if tot != 4:
    FAIL.append("呼叫點總數 ≠ 4")

shapes = {tuple(a[1][1:]) for v in SITES.values() for a in v}
print("  引數形（去第 1 引數 `cum_S`）之相異形 ＝ %d：" % len(shapes))
for s in sorted(shapes):
    print("      %s" % (s,))
want = {("res.get('cut_coords')", "d_hat", "corner_pt", "allocation_dir_block"),
        ("res.get('cut_coords')", "d_hat_rev", "end_pt", "allocation_dir_block")}
ok = shapes == want
print("  ⇒ 恰為「左鏈 `(d_hat, corner_pt)`／右鏈 `(d_hat_rev, end_pt)`」二形 ＝ %s %s"
      % (shapes == want, "✅" if ok else "🔴"))
if not ok:
    FAIL.append("引數形⛔ 為所期之二形")

n_main = sum(1 for v in SITES.values() for a in v if a[2])
print("  🔴 **落於 `main()` 內者 ＝ %d 處**（＝ `run_all`／`run_verification` **從不執行**者）"
      "⇒ **本合成案即其唯一驗收路徑**" % n_main)
print()

print("=" * W)
if FAIL:
    print("🔴 **合成案紅 ＝ %d 項** ⇒ 本次輸出⛔ 出艙：" % len(FAIL))
    for x in FAIL:
        print("   · %s" % x)
    print("=" * W)
    sys.exit(3)
print("✅ 合成案全綠：閉式自證 ⋀ 造 a（off 原值）⋀ 造 b（on 必變）⋀ 造 c（max 語意）"
      " ⋀ 造 d（缺值原值）⋀ 造 e（退化 raise）⋀ 四呼叫點 AST 實查")
print("=" * W)
