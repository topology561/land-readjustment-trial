# -*- coding: utf-8 -*-
# `W-G.9-340`：`W-G.9-338` 工項四之 `main()` 內改動之**合成案**（`CLAUDE.md`「🔒 `main()` 內之敘述」款）。
# 由：`app.py` 之改動 11 段中 9 段落於 `def main()` 內；`harvest()` 以 AST 跳過 UI、harness 走 `run_step_g`
#     ⇒ 該 9 段從不被 `run_all`／`chk_wg9309`／`F2`〜`F4` 執行（`W-G.9-338R` ⑦-1 CC 自捕）。
# 本器分三部：
#   甲　合成幾何（⛔ 取 UC9898 實料）：`_right_origin_is_front_p2`／`_right_chain_origin_s` 之真值表與閉式期值。
#       期值之出處 ＝ `_strip_axis` docstring 之恆等式「點 p = bp + t·d_hat + u·n_hat ⇒ s(p) ≡ t」
#       （⛔ 由受測碼現跑回填）；d_hat 與 ALLOC 皆斜交（⛔ 正交特例）。
#   乙　`main()` 內接線之 AST 實查（與 `verify/stepg_pipeline.py` 之同構）：呼叫點數、引數形、綁定之位與其文、
#       錨點外推之呼叫點數、首宗斷言之同文。
#   丙　判別力：對 `app.py` 之原文施四種單點突變，乙部須逐一轉紅（⛔ 器恆綠）。
# 用法：python probe_WG9340_main_synth.py <repo>
# rc ＝ 紅項數（甲＋乙）；丙部任一突變未轉紅 ⇒ 另加 100（器紅）。
import ast, io, os, sys, contextlib, math, re
sys.stdout.reconfigure(encoding="utf-8")
REPO = sys.argv[1]
sys.path.insert(0, os.path.join(REPO, "verify"))
RED = []
def chk(tag, ok, got, exp):
    print(("✅" if ok else "🔴"), tag, "得", got, "期", exp)
    if not ok: RED.append(tag)

# ───────────── 甲　合成幾何 ─────────────
from app_harvest import harvest
with contextlib.redirect_stdout(io.StringIO()):
    ns, _fake_st = harvest(os.path.join(REPO, "app.py"))
f_dec = ns.get("_right_origin_is_front_p2"); f_org = ns.get("_right_chain_origin_s"); f_obl = ns.get("_oblique_s_max")
chk("甲0 三函式皆在 ns", all(callable(x) for x in (f_dec, f_org, f_obl)), [callable(x) for x in (f_dec, f_org, f_obl)], [True]*3)
if all(callable(x) for x in (f_dec, f_org, f_obl)):
    import numpy as np
    th = math.radians(20.0); ph = math.radians(23.7)          # d_hat 20°、ALLOC 23.7°（斜交 3.7°）
    d = np.array([math.cos(th), math.sin(th)]); ad = np.array([math.cos(ph), math.sin(ph)])
    nh = np.array([-ad[1], ad[0]])                              # n_hat ＝ rot90(ALLOC)（`_strip_axis` 逐字）
    bp = np.array([310000.0, 2650000.0])
    S_FAR, U_DEEP, L_FRONT = 32.5, 20.0, 30.0
    V = [tuple(bp + s * d + u * nh) for s, u in ((0, 0), (S_FAR, 0), (S_FAR, U_DEEP), (0, U_DEEP))]
    p2 = bp + L_FRONT * d
    # 甲1 決定點之真值表
    for hs, fo, e in ((True, False, True), (True, True, False), (False, False, False), (False, True, False)):
        chk(f"甲1 _right_origin_is_front_p2({hs},{fo})", f_dec(hs, fo) is e, f_dec(hs, fo), e)
    # 甲2 斜交極值之閉式（前提：本合成幾何之 s_max 恰為 S_FAR）
    so = f_obl(V, d, bp, ad)
    chk("甲2 _oblique_s_max 閉式", abs(so - S_FAR) < 1e-9, round(so, 10), S_FAR)
    # 甲3 真分支 ＝ ‖p2 − corner‖（且 ≠ 斜交極值 ⇒ 必變）
    t = f_org(V, d, bp, ad, front_p2=p2, has_side_right=True, forced_right=False)
    chk("甲3 真分支 ＝ L_FRONT（必變）", abs(t - L_FRONT) < 1e-9 and abs(t - so) > 1.0, round(t, 10), L_FRONT)
    # 甲4 偽分支三形 ≡ 斜交極值（逐位）
    for hs, fo in ((True, True), (False, False), (False, True)):
        r = f_org(V, d, bp, ad, front_p2=p2, has_side_right=hs, forced_right=fo)
        chk(f"甲4 偽分支({hs},{fo}) ≡ _oblique_s_max 逐位", r == so, r, so)
    # 甲5 偽分支不讀 front_p2（缺值亦同）
    r = f_org(V, d, bp, ad, front_p2=None, has_side_right=True, forced_right=True)
    chk("甲5 偽分支 front_p2=None ≡ 斜交極值", r == so, r, so)
    # 甲6 真分支之 loud（⛔ 靜默退回斜交極值）
    def raises(**kw):
        try:
            f_org(V, d, bp, ad, has_side_right=True, forced_right=False, **kw); return False
        except RuntimeError:
            return True
    chk("甲6a front_p2=None ⇒ raise", raises(front_p2=None), "raise" if raises(front_p2=None) else "無", "raise")
    off = p2 + 0.01 * nh
    chk("甲6b p2 離射線 0.01 m ⇒ raise", raises(front_p2=off), "raise" if raises(front_p2=off) else "無", "raise")
    back = bp - L_FRONT * d
    chk("甲6c p2 在 corner 反向 ⇒ raise", raises(front_p2=back), "raise" if raises(front_p2=back) else "無", "raise")
    # 甲7 閾內（橫距 5e-7 ≤ 1e-6）⇒ 受之，值 ＝ 沿 d_hat 之投影
    near = p2 + 5e-7 * np.array([-d[1], d[0]])
    r = f_org(V, d, bp, ad, front_p2=near, has_side_right=True, forced_right=False)
    chk("甲7 橫距 5e-7 ⇒ 受之", abs(r - L_FRONT) < 1e-9, round(r, 10), L_FRONT)

# ───────────── 乙　main() 接線之 AST 實查 ─────────────
KW_EXP = {"front_p2": "_front_p2_blk", "has_side_right": "_has_right_corner", "forced_right": "_fo_right"}
POS_EXP = ["blk_meta['vertices']", "d_hat", "corner_pt", "allocation_dir_block"]
def calls_in(node, name):
    return [c for c in ast.walk(node) if isinstance(c, ast.Call) and isinstance(c.func, ast.Name) and c.func.id == name]
def fn_of(tree, name):
    fs = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == name]
    return fs[0] if len(fs) == 1 else None
def loop_body_of(fn):
    """最外層之「街廓迴圈」：其 target 含 `blk_label` 之 For（app：`main()` 內；stepg：`_run_step_g_impl` 內）。"""
    fs = [n for n in ast.walk(fn) if isinstance(n, ast.For) and "blk_label" in ast.unparse(n.target)]
    fs.sort(key=lambda n: n.lineno)
    return fs[0] if fs else None
def top_assign(loop, name):
    """迴圈體**直屬**（無條件）之 `name = …`；回 [(lineno, 右式之 ast.dump)]"""
    out = []
    for st in loop.body:
        if isinstance(st, ast.Assign) and any(isinstance(t, ast.Name) and t.id == name for t in st.targets):
            out.append((st.lineno, ast.dump(st.value)))
    return out
def any_assign(node, name):
    out = []
    for st in ast.walk(node):
        if isinstance(st, ast.Assign) and any(isinstance(t, ast.Name) and t.id == name for t in st.targets):
            out.append((st.lineno, ast.unparse(st.value)))
    return out
def guard_ifs(node):
    return [n for n in ast.walk(node) if isinstance(n, ast.If) and "_right_origin_is_front_p2" in ast.unparse(n.test)]

def wiring(app_src, stepg_src):
    """回（紅項清單, 記錄）"""
    red = []; log = []
    def c(tag, ok, got, exp):
        log.append(("✅" if ok else "🔴") + f" {tag} 得 {got} 期 {exp}")
        if not ok: red.append(tag)
    A = ast.parse(app_src); S = ast.parse(stepg_src)
    mainf = fn_of(A, "main"); implf = fn_of(S, "_run_step_g_impl")
    c("乙0 main()／_run_step_g_impl 各恰一", mainf is not None and implf is not None, [mainf is not None, implf is not None], [True, True])
    if mainf is None or implf is None: return red, log
    LA = loop_body_of(mainf); LS = loop_body_of(implf)
    c("乙0′ 街廓迴圈可定位", LA is not None and LS is not None, [getattr(LA, "lineno", None), getattr(LS, "lineno", None)], "皆非 None")
    if LA is None or LS is None: return red, log
    # 乙1 呼叫點數：main() 4（右鏈起點·選槽·池窗·右側診斷）；stepg 3（無診斷）
    ca = calls_in(mainf, "_right_chain_origin_s"); cs = calls_in(implf, "_right_chain_origin_s")
    c("乙1 _right_chain_origin_s 呼叫點（main／stepg）", (len(ca), len(cs)) == (4, 3), (len(ca), len(cs)), (4, 3))
    # 乙2 各呼叫之引數形
    def form(cl):
        return ([ast.unparse(a) for a in cl.args], {k.arg: ast.unparse(k.value) for k in cl.keywords})
    bad = [cl.lineno for cl in ca + cs if form(cl) != (POS_EXP, KW_EXP)]
    c("乙2 引數形逐呼叫 ＝ (vertices, d_hat, corner_pt, allocation_dir_block; front_p2=_front_p2_blk, has_side_right=_has_right_corner, forced_right=_fo_right)", not bad, bad, [])
    # 乙3 各呼叫皆在街廓迴圈內
    outA = [cl.lineno for cl in ca if not (LA.lineno <= cl.lineno <= LA.end_lineno)]
    outS = [cl.lineno for cl in cs if not (LS.lineno <= cl.lineno <= LS.end_lineno)]
    c("乙3 呼叫皆在街廓迴圈內", not outA and not outS, outA + outS, [])
    # 乙4 綁定：迴圈體直屬（無條件）且先於一切呼叫點；app 與 stepg 之右式同文
    for nm in ("_has_right_corner", "_fo_right"):
        ta = top_assign(LA, nm); ts = top_assign(LS, nm)
        okpos = len(ta) == 1 and all(ta[0][0] < cl.lineno for cl in ca) and len(ts) == 1 and all(ts[0][0] < cl.lineno for cl in cs)
        c(f"乙4 {nm}：直屬綁定恰一·先於呼叫點（app／stepg）", okpos, ([x[0] for x in ta], [x[0] for x in ts]), "各恰一·行號 < 各呼叫")
        c(f"乙4′ {nm}：右式 app ≡ stepg（ast.dump）", len(ta) == 1 and len(ts) == 1 and ta[0][1] == ts[0][1], "同" if (ta and ts and ta[0][1] == ts[0][1]) else "異", "同")
    # 乙5 _front_p2_blk：直屬 `= None` 恰一（先於呼叫）；非直屬之賦值恰一且其右式取 `_p2_fl`；corner_pt 同分支取 `_p1_fl`
    for tag, L, cl_, root in (("app", LA, ca, mainf), ("stepg", LS, cs, implf)):
        tn = top_assign(L, "_front_p2_blk"); allv = any_assign(L, "_front_p2_blk")
        ok_none = len(tn) == 1 and tn[0][1] == ast.dump(ast.Constant(None)) and all(tn[0][0] < x.lineno for x in cl_)
        c(f"乙5 {tag} _front_p2_blk 直屬 = None 恰一·先於呼叫", ok_none, [x[0] for x in tn], "恰一")
        others = [v for v in allv if v[1] != "None"]
        c(f"乙5′ {tag} _front_p2_blk 之他賦值恰一·取 _p2_fl", len(others) == 1 and "_p2_fl" in others[0][1], others, "[(…, '…_p2_fl…')]")
        # 同一 If 分支內 corner_pt 取 _p1_fl（⇒ p2 與 corner_pt 為同一 FRONT 段之二端）
        br = [n for n in ast.walk(L) if isinstance(n, ast.If) and any(isinstance(s, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "_front_p2_blk" for t in s.targets) for s in n.body)]
        ok_br = len(br) == 1 and any(isinstance(s, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "corner_pt" for t in s.targets) and "_p1_fl" in ast.unparse(s.value) for s in br[0].body)
        c(f"乙5″ {tag} 同分支 corner_pt 取 _p1_fl", ok_br, len(br), "該分支恰一且含 corner_pt=…_p1_fl…")
    # 乙6 錨點外推之呼叫點：main／stepg 皆 0；app 之函式本體仍在（本批⛔ 刪）
    na = len(calls_in(mainf, "_wg9268p_anchor_advance")); nsg = len(calls_in(implf, "_wg9268p_anchor_advance"))
    c("乙6 _wg9268p_anchor_advance 呼叫點（main／stepg）", (na, nsg) == (0, 0), (na, nsg), (0, 0))
    c("乙6′ _wg9268p_anchor_advance 之 def 仍在 app", fn_of(A, "_wg9268p_anchor_advance") is not None, fn_of(A, "_wg9268p_anchor_advance") is not None, True)
    # 乙7 首宗斷言：main／stepg 各恰一、同文（ast.dump）、在右鏈之 `for entry` 內
    ga = guard_ifs(mainf); gs = guard_ifs(implf)
    same = len(ga) == 1 and len(gs) == 1 and ast.dump(ga[0]) == ast.dump(gs[0])
    c("乙7 首宗斷言 main／stepg 各恰一且同文", same, (len(ga), len(gs), "同" if same else "異"), (1, 1, "同"))
    # 乙8 決定點之呼叫：main 與 stepg 之引數形 ＝ (_has_right_corner, _fo_right)
    da = calls_in(mainf, "_right_origin_is_front_p2"); ds = calls_in(implf, "_right_origin_is_front_p2")
    badd = [x.lineno for x in da + ds if [ast.unparse(a) for a in x.args] != ["_has_right_corner", "_fo_right"] or x.keywords]
    c("乙8 _right_origin_is_front_p2 之呼叫（main／stepg）各恰一·引數 (_has_right_corner, _fo_right)", len(da) == 1 and len(ds) == 1 and not badd, (len(da), len(ds), badd), (1, 1, []))
    # 乙9 _WF_NS_NAMES 納二名
    wf = [n for n in A.body if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "_WF_NS_NAMES" for t in n.targets)]
    names = set()
    for n in wf:
        if isinstance(n.value, (ast.List, ast.Tuple)):
            names |= {e.value for e in n.value.elts if isinstance(e, ast.Constant)}
    c("乙9 _WF_NS_NAMES 納二名", {"_right_origin_is_front_p2", "_right_chain_origin_s"} <= names, sorted({"_right_origin_is_front_p2", "_right_chain_origin_s"} & names), 2)
    return red, log

app_src = open(os.path.join(REPO, "app.py"), encoding="utf-8").read()
stepg_src = open(os.path.join(REPO, "verify", "stepg_pipeline.py"), encoding="utf-8").read()
r, lg = wiring(app_src, stepg_src)
for l in lg: print(l)
RED += r

# ───────────── 丙　判別力（四種單點突變·乙部須轉紅） ─────────────
MUT = [
    ("丙1 main() 一處 forced_right=_fo_right → _fo_left", "forced_right=_fo_right)", "forced_right=_fo_left)"),
    ("丙2 main() 一處 _right_chain_origin_s → _oblique_s_max（退回舊式）", "_smax_o = _right_chain_origin_s(", "_smax_o = _oblique_s_max("),
    ("丙3 main() 刪去 _front_p2_blk 取 p2 之一行", "                                    _front_p2_blk = _np_d.array(_p2_fl, dtype=float)\n", ""),
    ("丙4 main() 首宗斷言去 `and not is_first_corner_r`", "and _lg_idx_right == 0\n                                        and not is_first_corner_r):", "and _lg_idx_right == 0):"),
]
IR = 0
if not r:
    for tag, old, new in MUT:
        # 只突變 main() 之區間（⛔ 碰 stepg／模組層）
        A = ast.parse(app_src); mf = fn_of(A, "main")
        lines = app_src.splitlines(keepends=True)
        head = "".join(lines[:mf.lineno - 1]); body = "".join(lines[mf.lineno - 1:mf.end_lineno]); tail = "".join(lines[mf.end_lineno:])
        n = body.count(old)
        if n < 1:
            print("🔴 器紅", tag, "突變錨未命中（main() 內 0 處）"); IR += 1; continue
        mutated = head + body.replace(old, new, 1) + tail
        rr, _ = wiring(mutated, stepg_src)
        ok = len(rr) > 0
        print(("✅" if ok else "🔴 器紅"), tag, "⇒ 乙部紅項", rr)
        if not ok: IR += 1
else:
    print("⚪ 丙部略（乙部已紅·突變無從證判別力）")
print("紅項", RED, "器紅", IR)
sys.exit(len(RED) + (100 if IR else 0))
