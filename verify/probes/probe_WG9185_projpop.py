r"""**W-G.9-185 `M-J-1`／`M-J-2`**：`_projection_order` 呼叫點之完整清單與**母體同步之直接實測** — ⛔ **零生產碼變更**

## 受詞

`W-G.9-185 §一 N-2`：
- `M-J-1`：呼叫點之**完整清單**（`檔:行`／第一實參／所屬函式／母體類別）。
- `M-J-2`：於各呼叫點**攔截其實收之第一實參**，取其**暫編地號集合**，逐對比對是否**逐位相同**。
  🛑 **⛔ 不得以「跑完沒 raise」代替上列量測**（`GB-105 ③` 逐字）⇒ 本檔**逐 tag 印出實收集合本身**。

## 🔴 單之前提已過時（照實回報·`S-2`）

單 `N-2` 引 `GB-105` 之**原始**「現況處置」，惟：
1. 🔓 **`GB-105` 已於 `W-G.9-166`（claude.ai 裁 `2026-08-28`）解除**
   （`docs/reports/W-G.4_泛用阻塞項登記表.md` 之 `### 🔓 \`GB-105\` **解除**`）。
2. 單稱「母體須分 **`5`** 類」——實為**三受詞類**（`GB-105` **加註三**·`W-G.9-160`）：
   `POP_SYNC`／`ORDER_INVARIANCE`／`NAME_DERIVATION`。
3. 單引之「以**暫編地號集合逐位相同**之直接不變式串起**全部**呼叫點」已被加註三**逐字否定**：
   「**一條不變式加在十二點上，會取消後二類既有之檢查**」。

⇒ 本檔仍執行 `M-J-1`／`M-J-2`（其量測價值⛔ 不因解除而消滅——係對既有不變式之**獨立復現**），
   惟 `M-J-3` 之受詞改為「**既有三類不變式之射程與缺口**」，見報告 `§三-4`。

## 量法

spy `app.py` 之四個斷言入口（`_proj_pop_assert_seq`／`_passthrough`／`_diff`／`_subset`）
＋ `_projection_order` 本身（記其**呼叫者 frame**）。⛔ 全部經 `ns` 覆寫，⛔ 未改生產碼一字。

## ⛔ 本檔不做

⛔ 不改生產碼一字。⛔ 不修任何母體不同步（本批只**量**）。⛔ 不立任何新閘。
⛔ 不跑 `run_all`／跨態。⛔ 不寫死本機絕對路徑。
"""
import ast
import contextlib
import io
import os
import sys

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
W = 190
TARGET_SB = 3.5
BLKS = ["R1", "R2", "R3", "R4", "R5", "R6"]
NAME = "_projection_order"


def _resolve_out(default_name):
    name = os.environ.get("WV_OUT_NAME") or default_name
    path = os.path.join(OUTDIR, name)
    if os.path.exists(path) and os.environ.get("WV_ALLOW_OVERWRITE") != "1":
        raise RuntimeError("拒絕覆寫既有 log：" + path)
    return path


def mj1_static():
    """`M-J-1`：AST 全掃（⛔ 不接 head/tail·`自誤 161` 防線）。"""
    files = [os.path.join(REPO, "app.py")]
    for root, dirs, fs in os.walk(os.path.join(REPO, "verify")):
        dirs[:] = [d for d in dirs if not d.startswith(".") and d != "__pycache__"]
        for f in sorted(fs):
            if f.endswith(".py"):
                files.append(os.path.join(root, f))
    rows, textual = [], 0
    for p in files:
        src = open(p, encoding="utf-8", errors="replace").read()
        textual += sum(1 for ln in src.splitlines() if NAME in ln)
        try:
            tree = ast.parse(src)
        except SyntaxError:
            continue
        owner = {}
        for nd in ast.walk(tree):
            if isinstance(nd, (ast.FunctionDef, ast.AsyncFunctionDef)):
                for ln in range(nd.lineno, (nd.end_lineno or nd.lineno) + 1):
                    owner[ln] = nd.name
        for nd in ast.walk(tree):
            if not isinstance(nd, ast.Call):
                continue
            fn, kind = nd.func, None
            if isinstance(fn, ast.Name) and fn.id == NAME:
                kind = "裸名"
            elif isinstance(fn, ast.Subscript) and isinstance(fn.slice, ast.Constant) \
                    and fn.slice.value == NAME:
                kind = 'ns["…"]'
            elif isinstance(fn, ast.Attribute) and fn.attr == NAME:
                kind = "屬性"
            if kind:
                a0 = ast.get_source_segment(src, nd.args[0]) if nd.args else "(無實參)"
                rows.append((os.path.relpath(p, REPO).replace("\\", "/"), nd.lineno, kind,
                             owner.get(nd.lineno, "(module)"), " ".join(a0.split())[:56]))
    return sorted(rows), textual, len(files)


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
    P("【W-G.9-185 M-J-1／M-J-2】`_projection_order` 呼叫點清單與母體同步之直接實測 — ⛔ 零生產碼")
    P("=" * W)

    # ── M-J-1 ──
    rows, textual, nfiles = mj1_static()
    P("")
    P("【M-J-1】呼叫點之完整清單（**AST**·母體 = app.py ＋ verify/**/*.py = %d 檔）" % nfiles)
    P("  %-3s %-44s %6s %-10s %-30s %s" % ("#", "檔", "行", "形", "所屬函式", "第一實參"))
    prod, probe = [], []
    for i, r in enumerate(rows, 1):
        (prob := probe if r[0].startswith("verify/probes/") else prod).append(r)
        P("  %-3d %-44s %6d %-10s %-30s %s" % (i, r[0], r[1], r[2], r[3], r[4]))
    P("  ── 合計 = %d 處（**生產鏈 %d** ／ 探針 %d）" % (len(rows), len(prod), len(probe)))
    P("  ── 含字面 `%s` 之列數 = %d ⇒ 其中 AST 判為**呼叫**者 = %d（差 %d ＝ 定義列／字串／註解／賦值）"
      % (NAME, textual, len(rows), textual - len(rows)))
    P("  ── 🔒 對拍 `GB-105` 加註一之「**`12`** 處（探針另計·⛔ 不列入）」："
      "本次生產鏈 = %d ⇒ %s" % (len(prod), "✅ **相同**" if len(prod) == 12 else "🔴 不同"))

    ns, fake_st = harvest()
    DECL = ns["_PROJ_POP_DECL"]
    P("")
    P("【M-J-2 前置】`_PROJ_POP_DECL` 之宣告表（`app.py`·現基座）")
    kinds = {}
    for tag, d in DECL.items():
        kinds.setdefault(d["kind"], []).append(tag)
    P("  tag 總數 = %d" % len(DECL))
    for k in sorted(kinds):
        P("    %-18s %d tag：%s" % (k, len(kinds[k]), kinds[k]))
    P("  🔒 三受詞類（`GB-105` 加註三·`W-G.9-160`）——⛔ 非單所載之「5 類」")

    # ── spy ──
    REC = []          # (tag, kind, which, blk, ids)
    CALLS = []        # _projection_order 之呼叫者 frame
    _ids = ns["_proj_pop_ids"]

    def wrap(fname, which_args):
        orig = ns[fname]

        def w(*a, **k):
            try:
                tag = a[0] if a else k.get("tag")
                d = DECL.get(tag, {})
                blk = k.get("blk")
                for pos, label in which_args:
                    seq = a[pos] if len(a) > pos else None
                    if seq is not None and not isinstance(seq, (str, bytes)):
                        REC.append((tag, d.get("kind", "?"), label, blk,
                                    tuple(_ids(seq))))
            except Exception:                                         # noqa: BLE001
                REC.append((repr(a[:1]), "?", "🔴 spy 例外", None, ()))
            return orig(*a, **k)
        ns[fname] = w
        return orig

    o1 = wrap("_proj_pop_assert_seq", [(1, "actual"), (2, "base")])
    o2 = wrap("_proj_pop_assert_diff", [(1, "before"), (2, "after")])
    o3 = wrap("_proj_pop_assert_subset", [(1, "actual"), (2, "base")])
    o4 = ns["_proj_pop_assert_passthrough"]

    def w4(tag, blk=None):
        REC.append((tag, DECL.get(tag, {}).get("kind", "?"), "(passthrough·⛔ 無序參)", blk, ()))
        return o4(tag, blk=blk)
    ns["_proj_pop_assert_passthrough"] = w4

    o5 = ns[NAME]

    def w5(parcels, p1, p2):
        fr = sys._getframe(1)
        CALLS.append((os.path.relpath(fr.f_code.co_filename, REPO).replace("\\", "/"),
                      fr.f_lineno, fr.f_code.co_name, len(parcels or [])))
        return o5(parcels, p1, p2)
    ns[NAME] = w5

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
            ERR["run_corner_pk"] = "%s: %s" % (type(e).__name__, str(e)[:150])
            wins, forced = {}, {}
    for blk in BLKS:
        with contextlib.redirect_stdout(io.StringIO()):
            try:
                run_step_g(ns, fake_st, cb_all, cad, snapshot, params,
                           [tp for tp in build_p if tp.get("所屬街廓") == blk],
                           wins, forced, TARGET_SB)
            except Exception as e:                                    # noqa: BLE001
                ERR[blk] = "%s: %s" % (type(e).__name__, str(e)[:120])

    P("")
    P("  執行情形（⛔ 非停機款·照實載）：%s"
      % ("；".join("%s→%s" % (k, v) for k, v in ERR.items()) if ERR else "⛔ 無例外"))

    # ── `_projection_order` 之實際呼叫者 ──
    P("")
    P("【M-J-2 a】`_projection_order` 之**實際**呼叫者 frame（證哪些靜態點真被執行）")
    agg = {}
    for f, ln, fn, n in CALLS:
        k = (f, ln, fn)
        agg.setdefault(k, []).append(n)
    P("  %-44s %6s %-28s %8s %s" % ("檔", "行", "函式", "次數", "實收長度（去重）"))
    for (f, ln, fn), ns_ in sorted(agg.items()):
        P("  %-44s %6d %-28s %8d %s" % (f, ln, fn, len(ns_), sorted(set(ns_))))
    P("  ── 實際執行之靜態點 = %d ／ 靜態清單之生產鏈 = %d" % (len(agg), len(prod)))
    hit = {(f, ln) for (f, ln, _fn) in agg}
    P("  ── **⛔ 未被執行**之生產鏈點（結構上到不了或本情境未觸）：")
    for r in prod:
        if (r[0], r[1]) not in hit:
            P("       %s:%d  %s（%s）" % (r[0], r[1], r[3], r[4]))

    # ── 逐 tag 之實收集合 ──
    P("")
    P("【M-J-2 b】逐 tag 之**實收**暫編地號集合（🛑 ⛔ 非「沒 raise」·係**值本身**）")
    bytag = {}
    for tag, kind, which, blk, ids in REC:
        bytag.setdefault((tag, kind, which), []).append((blk, ids))
    P("  %-26s %-18s %-24s %6s %8s %s"
      % ("tag", "類", "位置", "次數", "集合大小(去重)", "首 3 號"))
    for (tag, kind, which), lst in sorted(bytag.items()):
        sizes = sorted({len(i) for _b, i in lst})
        samp = next((list(i)[:3] for _b, i in lst if i), [])
        P("  %-26s %-18s %-24s %6d %8s %s" % (tag, kind, which, len(lst), sizes, samp))
    P("  ── 實收 tag 數 = %d ／ 宣告表 tag 數 = %d"
      % (len({t for t, _k, _w in bytag}), len(DECL)))
    unseen = [t for t in DECL if t not in {x[0] for x in bytag}]
    P("  ── **⛔ 未觀測到**之 tag（%d）：%s" % (len(unseen), unseen))

    # ── 逐對對稱差集 ──
    P("")
    P("【M-J-2 c】**逐對對稱差集**（同街廓·同 `kind` 內·逐號具名）")
    for kind in sorted(kinds):
        P("")
        P("  ■ 類 %s" % kind)
        per_blk = {}
        for tag, k2, which, blk, ids in REC:
            if k2 != kind or not ids:
                continue
            per_blk.setdefault(blk, []).append(("%s/%s" % (tag, which), frozenset(ids)))
        for blk in sorted(per_blk, key=lambda x: (x is None, x)):
            items = per_blk[blk]
            uniq = sorted({s for _n, s in items}, key=len)
            P("    街廓 %-6s 觀測 %d 次／相異集合 %d 個／大小 %s"
              % (str(blk), len(items), len(uniq), [len(s) for s in uniq]))
            if len(uniq) > 1:
                base = uniq[-1]
                for s in uniq[:-1]:
                    names = sorted({n for n, ss in items if ss == s})
                    P("       Δ vs 最大集合：−%d 號 %s ／ +%d 號 %s   ← %s"
                      % (len(base - s), sorted(base - s)[:8],
                         len(s - base), sorted(s - base)[:8], names))
            else:
                P("       ⇒ ✅ 該街廓內**集合逐位相同**（相異集合僅 1 個）")

    P("")
    P("🛑 本檔只量·⛔ 未修任何不同步·⛔ 未動生產碼一字·⛔ 未立任何新閘。")
    P("=" * W)
    out = _resolve_out("probe_WG9185_projpop_e9e3d1ed.log")
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write("\n".join(L) + "\n")
    print("WROTE " + out, file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
