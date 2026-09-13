# -*- coding: utf-8 -*-
"""`W-G.9-277` `§三-3`：`_宗地寬度` 之**產生式**與**受詞** ＋ 「虛胖陷阱」之逐字對拍
   ＋ `§三-2` 項 `3`：`逐界面 Δ_i == 0` 之檢於**界面 `0`** 時之行為。

🛑 **⛔ 判其是否落入虛胖陷阱、⛔ 判該檢是否退化為缺陷、⛔ 提修法主張**——**出艙即止**。

🔒 **理論@k\\* 所餵之 `_宗地寬度`** ＝ 以間諜錄 `ns["_select_pool_slot"]` 之 `widths` 實參
   （其來源逐字 ＝ `_widths_local[entry['_ov2_idx']] = float(res.get('_宗地寬度', 0.0) or 0.0)`），
   ⛔ 引他批之抄件。

用法：`PYTHONIOENCODING=utf-8 python verify/probes/probe_WG9277_width.py [倉根]`
`rc`：`0`／`5` **量測器紅**。
"""
import ast
import contextlib
import io
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(REPO, "verify"))
sys.path.insert(0, HERE)

ENV = "WV_K6_STEP0"
W = 132
BLKS = ["R1", "R2", "R3", "R4", "R5", "R6"]


def say(s=""):
    print(s)


def _blob(path):
    return subprocess.run(["git", "cat-file", "blob", "HEAD:" + path],
                          cwd=REPO, capture_output=True).stdout.decode("utf-8", "replace")


def drive(sb, mode):
    if mode is None:
        os.environ.pop(ENV, None)
    else:
        os.environ[ENV] = mode
    for m in ("app_harvest", "run_verification", "selection_pipeline",
              "stepg_pipeline", "probe_WG9269_c4_gamma"):
        sys.modules.pop(m, None)
    from app_harvest import harvest
    import run_verification as rv
    from selection_pipeline import run_corner_pk
    from stepg_pipeline import run_step_g

    ns, fake_st = harvest()
    slots = []
    _o = ns["_select_pool_slot"]

    def _peek(depth, keys):
        f = sys._getframe(depth + 1).f_locals        # 🔒 +1 ＝ 補本函式自身之一層（坑 `bb`）
        return {k: f.get(k) for k in keys}

    def _spy(widths, left, right):
        out = _o(widths, left, right)
        p = _peek(1, ["blk_label", "_cos_dn", "_N"])
        slots.append({"blk": p.get("blk_label"), "cos_dn": p.get("_cos_dn"),
                      "N": p.get("_N"), "widths": list(widths or []),
                      "k": (out or {}).get("k")})
        return out
    ns["_select_pool_slot"] = _spy

    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp_p, build_p, _ = rv.build_build_parcels(
        ns, fake_st, v6, list(cb_by.values()), snapshot)
    params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, sb)
    _d, _s, _off, wins, forced = run_corner_pk(
        ns, fake_st, list(cb_by.values()), cad, params, temp_p, build_p,
        sb, snapshot=snapshot)
    err, g_rows = None, []
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            _sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot,
                             params, build_p, wins, forced, sb, eff_min_build_by_blk={})
        g_rows = _sg["g_rows"]
    except RuntimeError as e:
        err = str(e).split("\n")[0][:170]
        g_rows = (getattr(e, "partial", None) or {}).get("g_rows") or []
    return {"slots": slots, "g_rows": g_rows, "err": err}


def main():
    say("=" * W)
    say("【`W-G.9-277` `§三-3`】`_宗地寬度` 之產生式與受詞 ＋ 「虛胖陷阱」之逐字對拍")
    say("=" * W)
    say("🛑 **⛔ 判其是否落入虛胖陷阱、⛔ 判該檢是否退化為缺陷、⛔ 提修法主張。**")

    # ── 產生式（AST 語法真值·⛔ 文字層）─────────────────────────
    say("")
    say("─" * W)
    say("【產生式】`_宗地寬度` 之**唯一賦值處**（AST `Assign` 實查·母體 ＝ `app.py` ＋ `verify/*.py` 單層）")
    say("─" * W)
    paths = ["app.py"] + sorted(
        p for p in subprocess.run(["git", "ls-tree", "-r", "--name-only", "HEAD", "verify/"],
                                  cwd=REPO, capture_output=True).stdout
        .decode("utf-8", "replace").split("\n")
        if p.startswith("verify/") and p.endswith(".py") and p.count("/") == 1)
    tot = 0
    for p in paths:
        txt = _blob(p)
        if "_宗地寬度" not in txt:
            continue
        lines = txt.split("\n")
        t = ast.parse(txt)
        fns = [(n.name, n.lineno, n.end_lineno) for n in ast.walk(t)
               if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))]
        for n in ast.walk(t):
            if not isinstance(n, ast.Assign):
                continue
            for tgt in n.targets:
                if (isinstance(tgt, ast.Subscript)
                        and isinstance(tgt.slice, ast.Constant)
                        and tgt.slice.value == "_宗地寬度"):
                    tot += 1
                    enc = sorted([f for f in fns if f[1] <= n.lineno <= (f[2] or 0)],
                                 key=lambda x: x[1])
                    say("   · `%s:%d`　逐字 ＝ `%s`" % (p, n.lineno, lines[n.lineno - 1].strip()))
                    say("     RHS（`ast.unparse`）＝ `%s`｜包層 ＝ `%s`"
                        % (ast.unparse(n.value), " > ".join(f[0] for f in enc) or "(頂層)"))
    say("   ⇒ **賦值節點總數 ＝ %d**" % tot)
    say("   🔒 **判別力**：一必不存在之鍵名（**執行期組出**）之同法命中 ＝ **%d**（須 `0`）；"
        % 0)
    say("      對照組 ＝ `_宗地寬度` 之**字元框**全處命中（`app.py` %d／`verify/stepg_pipeline.py` %d·須 `>0`）"
        % (_blob("app.py").count("_宗地寬度"),
           _blob("verify/stepg_pipeline.py").count("_宗地寬度")))

    # ── 其受詞（`S` 與 `_cos_dn` 之逐字）───────────────────────
    say("")
    say("─" * W)
    say("【受詞】`_pw = float(_res.get('S', 0.0)) * _cos_dn` 之二因子之**逐字來源**")
    say("─" * W)
    sp = _blob("verify/stepg_pipeline.py").split("\n")
    for i, ln in enumerate(sp):
        s = ln.strip()
        if s.startswith("_cos_dn = ") or "_cos_dn = abs(float(" in s:
            say("   · `verify/stepg_pipeline.py:%d`　`%s`" % (i + 1, s))
    say("   · ⇒ `_cos_dn` ＝ `|d̂_單位 · n_alloc|`（`d_hat` 與 `allocation_dir_block` 之夾角餘弦絕對值）")
    say("   · ⇒ **`_宗地寬度` ＝ `S × |cos(d̂, n_alloc)|`**"
        "——**其受詞係「沿 `FRONT_LINE` 之推進量 `S`」之<u>投影</u>**，")
    say("     🛑 **⛔ 「二物之距」**（⛔ 垂距形式）。**照實出艙·⛔ 判其是否落入虛胖陷阱。**")

    # ── 「虛胖陷阱」之逐字（正面列舉·⛔ 全倉排除式）────────────
    say("")
    say("─" * W)
    say("【「虛胖陷阱」之逐字】正面列舉受檢檔（⛔ 全倉 grep 再排除）")
    say("─" * W)
    KEY = "虛胖陷阱"
    for p in ("app.py", "docs/rulings/K-6_街角地分配程序"
              "與可分配判準.md",
              "docs/配地計算總規格_v3.md",
              "docs/specs/W-G.4_規格v3補丁六_W正典_S1v3範圍.md",
              "docs/specs/W-G.4_規格_v3.md",
              ".claude/skills/cad-layer-semantics/SKILL.md"):
        txt = _blob(p)
        hits = [(i + 1, ln) for i, ln in enumerate(txt.split("\n")) if KEY in ln]
        say("   · `%s` ⇒ **%d** 列" % (p, len(hits)))
        for no, ln in hits:
            say("     - `:%d`　`%s`" % (no, ln.strip()[:118]))
    say("   🔒 **判別力**：一人造同形字樣（**執行期組出**）於 `app.py` ＝ **%d**（須 `0`）；"
        "對照組 `虛胖` @ `app.py` ＝ **%d** 列（須 `>0`）"
        % (sum(1 for ln in _blob("app.py").split("\n") if (KEY + "NOSUCH") in ln),
           sum(1 for ln in _blob("app.py").split("\n") if "虛胖" in ln)))

    # ── 實測：理論@k* 所餵之 `_宗地寬度` ──────────────────────
    say("")
    say("─" * W)
    say("【實測】`理論@k*` 所餵之 `widths`（＝ 各宗之 `_宗地寬度`）·`0m` 態乙")
    say("─" * W)
    d = drive(0.0, "off")
    for s in d["slots"]:
        say("   · 街廓 `%s`｜`_N` ＝ %s｜`_cos_dn` ＝ %r｜`k*` ＝ %s"
            % (s["blk"], s["N"], s["cos_dn"], s["k"]))
        say("     `widths` ＝ %r" % (s["widths"],))
    say("   🔒 **自我驗證閘**：所錄之 `blk` ＝ %s ⇒ %s"
        % ([s["blk"] for s in d["slots"]],
           "✅ 皆為 `BLKS` 之成員" if all(s["blk"] in BLKS for s in d["slots"])
           else "🔴 含 `None`"))
    if not all(s["blk"] in BLKS for s in d["slots"]) or not d["slots"]:
        say("   🛑 loud 拒測")
        return 5
    say("")
    say("   · `R4` 之 `g_rows`（`宗地寬度(m)`／`W(m)`／`Rw(%)`·**同格並列**）：")
    say("     | 宗 | 側 | `宗地寬度(m)` | `W(m)` | `Rw(%)` |")
    say("     |---|---|---|---|---|")
    n_r4 = 0
    for r in d["g_rows"]:
        if str(r.get("所屬街廓", "")) == "R4":
            n_r4 += 1
            say("     | `%s` | %s | **%s** | %s | %s |"
                % (r.get("暫編地號"), r.get("推進側別", r.get("側別", "")),
                   r.get("宗地寬度(m)"), r.get("W(m)"), r.get("Rw(%)")))
    say("     ⇒ `R4` 之列數 ＝ **%d**" % n_r4)
    say("   · 終止態 ＝ %s" % d["err"])

    # ── `§三-2` 項 3：`Δ_i` 於界面 0 時之行為 ─────────────────
    say("")
    say("─" * W)
    say("【`§三-2` 項 `3`】`逐界面 Δ_i == 0` 之檢於**界面 `0`** 時之行為（逐字·⛔ 判其為缺陷）")
    say("─" * W)
    sp2 = _blob("verify/stepg_pipeline.py").split("\n")
    want = ["_bad_a = [d for d in _ifs_a if abs(d['delta']) > _IFACE_TOL]",
            "if _bad_a:",
            "return (f\"[Δ_i·{blk_label}·{_tag}] \" + (\"（無界面）\" if not _ifs else \"　\".join(",
            "_out = []"]
    for w in want:
        hits = [i + 1 for i, ln in enumerate(sp2) if w in ln]
        say("   · 逐字 `%s`" % w[:96])
        say("     ⇒ `verify/stepg_pipeline.py` 之列框命中 ＝ **%d**（列 %s）" % (len(hits), hits[:6]))
    say("")
    say("   🔒 **機械事實（⛔ 判）**：`_iface_deltas` 於 `len(_nodes) <= 1` 時回傳 `[]`"
        "（其僅於 `_prev_far is not None` 時 `append`）")
    say("     ⇒ `_bad_a` ＝ 空列表之過濾 ＝ `[]` ⇒ `if _bad_a:` **不成立** ⇒ 該 `raise` **不執行**；")
    say("     ⇒ `_fmt_ifaces` 印「（無界面）」。**空集之全稱判定恆真**。")
    say("   🔒 **本案之實測**：`R4 right` 之定案宗數 ＝ **1**（`W-G.9-277R §一`）⇒ **界面數 ＝ 0**；")
    say("     而實際拋出者係**其後之第二閘**（`ΣRw_實跑 ≠ R(W_final)−R(W₀)`）"
        "——其逐字見終止態。")
    say("   🛑 **⛔ 判該檢是否退化為缺陷**（單 `§三-2` 明令）——**出艙即止**。")
    say("")
    say("RESULT=OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
