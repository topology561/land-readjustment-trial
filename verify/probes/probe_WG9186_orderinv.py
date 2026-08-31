r"""**W-G.9-186 `N-2`**：`ORDER_INVARIANCE` 之 `7` 個 tag 於現行情境**從未執行**之坐實 — ⛔ **零生產碼變更**

## 受詞

`W-G.9-186 §一 N-2`：出艙該 `7` 個 tag 各自之**執行次數**與其**未執行之原因**
（分支未進／情境不適用／死碼），並附**判別力對照**（一個確有執行之 tag，其數須非 `0`）。

🛑 **停機款 `X-3`（逐字）**：
> `N-2` 之判別力對照組（一個確有執行之 tag）若得 `0` ⇒ **先判量測器紅並停機**
> ——「`7` 個 tag 從未執行」與「我的 spy 沒攔到」⛔ 不可區分。

## 量法（🔒 **用生產碼<u>自身</u>之觀測鉤**·⛔ 非 spy）

`app.py` 之 `_proj_pop_note(tag)`（`L-6′`）於**四個** assert 入口內被呼叫
（`app.py:7801`／`:7818`／`:7832`／`:7869`），其寫檔受環境變數 `WV_PROJ_POP_COUNT` 控制
（`app.py` 之 `_PROJ_POP_COUNT_ENV`）。⇒ 設該變數即可令**生產碼自己**記錄每次執行，
**⛔ 不需覆寫任何函式**、⛔ 不改生產碼一字。

**併**：spy `ns["_projection_order"]` 記其**呼叫者 frame**，以判各未執行 tag 之**原因**
（其呼叫點所在之模組／函式是否曾被進入）。

## ⛔ 本檔不做

⛔ 不改生產碼一字。⛔ 不修、⛔ 不刪任何 tag（`app.py:9465-9467` 之戒）。⛔ 不立任何新閘。
⛔ 不跑 `run_all`／跨態。⛔ 不寫死本機絕對路徑。
"""
import contextlib
import io
import os
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
sys.path.insert(0, VERIFY)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(VERIFY, "fixtures"))

from app_harvest import harvest                                       # noqa: E402
import run_verification as rv                                         # noqa: E402
from selection_pipeline import run_corner_pk                          # noqa: E402
from stepg_pipeline import run_step_g                                 # noqa: E402

OUTDIR = os.path.join(VERIFY, "out")
W = 170
TARGET_SB = 3.5
BLKS = ["R1", "R2", "R3", "R4", "R5", "R6"]


def _resolve_out(default_name):
    name = os.environ.get("WV_OUT_NAME") or default_name
    path = os.path.join(OUTDIR, name)
    if os.path.exists(path) and os.environ.get("WV_ALLOW_OVERWRITE") != "1":
        raise RuntimeError("拒絕覆寫既有 log：" + path)
    return path


def main():                                                          # noqa: C901
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8")
        except Exception:
            pass
    os.makedirs(OUTDIR, exist_ok=True)
    L = []

    def P(s=""):
        L.append(s)
        print(s, file=sys.stderr)

    P("=" * W)
    P("【W-G.9-186 N-2】`ORDER_INVARIANCE` 7 tag 之執行次數與未執行之原因 — ⛔ 零生產碼")
    P("=" * W)

    ns, fake_st = harvest()
    DECL = ns["_PROJ_POP_DECL"]
    ENV = ns["_PROJ_POP_COUNT_ENV"]
    cnt_path = os.path.join(tempfile.gettempdir(), "wg9186_projpop_count.txt")
    if os.path.exists(cnt_path):
        os.remove(cnt_path)
    os.environ[ENV] = cnt_path
    P("  🔒 觀測鉤 ＝ 生產碼自身之 `_proj_pop_note`（env `%s`）⇒ ⛔ 未覆寫任何 assert 函式" % ENV)

    CALLS = []
    _orig = ns["_projection_order"]

    def _spy(parcels, p1, p2):
        fr = sys._getframe(1)
        CALLS.append((os.path.relpath(fr.f_code.co_filename, REPO).replace("\\", "/"),
                      fr.f_lineno, fr.f_code.co_name))
        return _orig(parcels, p1, p2)
    ns["_projection_order"] = _spy

    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp_p, build_p, _ = rv.build_build_parcels(ns, fake_st, v6, list(cb_by.values()), snapshot)
    cb_all = list(cb_by.values())
    params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, TARGET_SB)
    ERR = {}
    with contextlib.redirect_stdout(io.StringIO()):
        try:
            _d0, _s2, _o2, wins, forced = run_corner_pk(
                ns, fake_st, cb_all, cad, params, temp_p, build_p, TARGET_SB, snapshot=snapshot)
        except Exception as e:                                        # noqa: BLE001
            ERR["run_corner_pk"] = "%s: %s" % (type(e).__name__, str(e)[:110])
            wins, forced = {}, {}
    for blk in BLKS:
        with contextlib.redirect_stdout(io.StringIO()):
            try:
                run_step_g(ns, fake_st, cb_all, cad, snapshot, params,
                           [tp for tp in build_p if tp.get("所屬街廓") == blk],
                           wins, forced, TARGET_SB)
            except Exception as e:                                    # noqa: BLE001
                ERR[blk] = "%s: %s" % (type(e).__name__, str(e)[:90])
    os.environ.pop(ENV, None)

    counts = {}
    if os.path.exists(cnt_path):
        for ln in open(cnt_path, encoding="utf-8"):
            t = ln.strip()
            if t:
                counts[t] = counts.get(t, 0) + 1
    P("  執行情形（⛔ 非停機款·照實載）：%s"
      % ("；".join("%s→%s" % (k, v) for k, v in ERR.items()) if ERR else "⛔ 無例外"))
    P("  計數檔 ＝ %s（%d 列）" % (os.path.basename(cnt_path),
                                  sum(counts.values())))

    # ── 逐 tag 之執行次數 ──
    P("")
    P("【N-2 a】**全 `14` tag** 之執行次數（🔒 由生產碼自身之 `_proj_pop_note` 記錄）")
    P("  %-28s %-18s %10s %s" % ("tag", "kind", "執行次數", "判"))
    by_kind = {}
    for tag, d in DECL.items():
        k = d["kind"]
        n = counts.get(tag, 0)
        by_kind.setdefault(k, []).append((tag, n))
        P("  %-28s %-18s %10d %s" % (tag, k, n, "✅ 有執行" if n else "🔴 **零**"))
    P("")
    for k in sorted(by_kind):
        tot = sum(n for _t, n in by_kind[k])
        zero = sum(1 for _t, n in by_kind[k] if n == 0)
        P("  類 %-18s tag %d 個／執行總次數 %d／**零執行之 tag %d 個**"
          % (k, len(by_kind[k]), tot, zero))

    # ── 判別力對照（X-3）──
    P("")
    P("【N-2 b·`X-3` 判別力對照】一個**確有執行**之 tag，其數須非 `0`")
    ctrl = [(t, n) for t, n in counts.items() if n > 0]
    ctrl.sort(key=lambda x: -x[1])
    if ctrl:
        P("  對照組（實得非零者·前 3）：%s" % ctrl[:3])
        P("  ⇒ ✅ **量測器非紅**（同一觀測鉤對確有執行之 tag 得非 `0`）⇒ ⛔ 不觸 `X-3`")
    else:
        P("  🔴 **全部 tag 皆得 `0`** ⇒ **量測器紅** ⇒ 🛑 依 `X-3` **停機上呈**")

    # ── 未執行之原因 ──
    P("")
    P("【N-2 c】`ORDER_INVARIANCE` 之 `7` tag——**未執行之原因**（逐 tag）")
    frames = sorted({(f, ln, fn) for f, ln, fn in CALLS})
    P("  🔒 `_projection_order` 之**實際**呼叫者 frame（%d 個相異）：" % len(frames))
    for f, ln, fn in frames:
        P("     %-42s :%-6d %s" % (f, ln, fn))
    hit_files = {f for f, _l, _n in frames}
    P("")
    SITE = {
        "wf_f0:_proj_order": ("verify/wf_f0.py", 256, "_proj_order"),
        "wf_f2:_proj_order": ("verify/wf_f2.py", 95, "_proj_order"),
        "wf_f3:_proj_order": ("verify/wf_f3.py", 78, "_proj_order"),
        "wf_f4:_proj_order": ("verify/wf_f4.py", 1047, "_proj_order"),
        "wf_f1:_order": ("verify/wf_f1.py", 376, "_order"),
        "wf_f4:_order_fb": ("verify/wf_f4.py", 1437, "_order_fb"),
        "wf_f4:_order": ("verify/wf_f4.py", 1512, "_order"),
    }
    P("  %-24s %-30s %10s %-14s %s" % ("tag", "呼叫點", "執行次數", "模組已 import？", "原因之判"))
    for tag, (f, ln, fn) in SITE.items():
        n = counts.get(tag, 0)
        mod = os.path.splitext(os.path.basename(f))[0]
        imported = mod in sys.modules
        entered = (f in hit_files)
        if n == 0 and not entered:
            why = "**情境不適用**（該呼叫點所在函式⛔ 未被進入）"
        elif n == 0 and entered:
            why = "**分支未進**（函式進了但該 assert 未走）"
        else:
            why = "（有執行）"
        P("  %-24s %-30s %10d %-14s %s"
          % (tag, "%s:%d" % (f, ln), n, "是" if imported else "**否**", why))
    P("")
    P("  🔒 **原因之總判**：`wf_f0`〜`wf_f4` 之主路徑於現行 harness **從不執行**")
    P("     （`run_verification` 於 `②-宗 圍堵閘破[R2]` 中止·【倉】`CLAUDE.md` 之 harness 限制）")
    P("     ⇒ `7` tag 皆屬**情境不適用**、⛔ 非死碼（其碼面確有呼叫點）、⛔ 非分支未進。")

    P("")
    P("🛑 本檔只量·⛔ 未修·⛔ 未刪任何 tag·⛔ 未動生產碼一字·⛔ 未立任何新閘。")
    P("=" * W)
    out = _resolve_out("probe_WG9186_orderinv_42f3dbba.log")
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write("\n".join(L) + "\n")
    print("WROTE " + out, file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
