r"""**W-G.9-187 `S-5`／`X-T`**：六街廓 `[T2-DIAG]` **整列逐位**之基準量／期末量 — ⛔ 零生產碼變更

## 受詞

`W-G.9-187 §零 S-5`（逐字）：

> 於**⛔ 未改一字之期初態**，先以逐街廓 `run_step_g` 取 **`R1`〜`R6` 六街廓之 `[T2-DIAG]`
> 全欄位**並落檔（`verify/out/probe_WG9187_baseline_f2ea2e4d.log`）。
> 🛑 **此係 `X-T` 之唯一比較端**，須在**動任何一字之前**取得。

`W-G.9-187 §二 X-T`（逐字）：

> 🔑 **落地前後，`R1`〜`R6` 六街廓之 `[T2-DIAG]` 全欄位逐位相同**（比較端 ＝ `S-5` 之基準量）。
> 任一欄位不同 ⇒ **停機上呈**——本批係觀測模式，⛔ 不應有任何配地變化。

## 量法

與 `probe_WG9183_pool_cover.py` **同法**（`harvest()` ⇒ `run_corner_pk` ⇒ **逐街廓**
`run_step_g`），惟本檔**⛔ 不 spy**、⛔ 不重建任何內部量——只**攔生產碼自身之 stdout**
並抽 `[T2-DIAG]` **整列原文**（框 ＝ 含該標記之列·⛔ 未解析欄位·體例同
`verify/fixture_klui_t2diag.py:107` 逐字「框 ＝ 含 `[T2-DIAG]` 之列·⛔ 未解析欄位」）。

🔒 **⛔ 不解析欄位之由**：`X-T` 之受詞係「**全欄位逐位相同**」⇒ 比較端須為**整列原始字元**；
一旦解析為 float 再比，`4dp` 顯示值之下的差異即被抹掉（`GB-101` 同族）。

🔒 **逐街廓例外照實記載**：`R2`／`R4`／`R5` 於本 harness 各拋 `RuntimeError`，
惟 `[T2-DIAG]` 之列印在 `_pool_strips_for_block` 內、**早於**該例外 ⇒ **攔取在前**
（交接文 `§七` 逐字）。例外訊息**併入輸出**，其變動亦屬 `X-T` 之受詞。

## ⛔ 本檔不做

⛔ 不改生產碼一字。⛔ 不 spy／不覆寫任何 `ns` 符號。⛔ 不改任何既有自檢器。
⛔ 不立任何新閘。⛔ 不跑 `run_all`／跨態。⛔ 不寫死本機絕對路徑。
"""
import contextlib
import hashlib
import io
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
sys.path.insert(0, VERIFY)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(VERIFY, "fixtures"))

from app_harvest import harvest                                       # noqa: E402
import run_verification as rv                                         # noqa: E402
from selection_pipeline import run_corner_pk                          # noqa: E402
from stepg_pipeline import run_step_g                                 # noqa: E402

OUTDIR = os.path.join(VERIFY, "out")
BLKS = ["R1", "R2", "R3", "R4", "R5", "R6"]
TARGET_SB = 3.5
MARK = "[T2-DIAG]"


def main():                                                          # noqa: C901
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8")
        except Exception:                                            # noqa: BLE001
            pass
    os.makedirs(OUTDIR, exist_ok=True)

    name = os.environ.get("WV_OUT_NAME") or "probe_WG9187_baseline_f2ea2e4d.log"
    path = os.path.join(OUTDIR, name)
    if os.path.exists(path) and os.environ.get("WV_ALLOW_OVERWRITE") != "1":
        raise RuntimeError("拒絕覆寫既有 log：" + path)

    L = []

    def P(s=""):
        L.append(s)
        print(s, file=sys.stderr)

    P("=" * 110)
    P("【W-G.9-187 S-5／X-T】六街廓 [T2-DIAG] 整列逐位 — ⛔ 零生產碼")
    P("=" * 110)
    import shapely
    P("  環境：shapely %s | GEOS %s | python %s"
      % (shapely.__version__, shapely.geos_version, sys.version.split()[0]))
    P("  框 ＝ 含 `%s` 之整列原文（⛔ 未解析欄位）" % MARK)
    P("")

    ns, fake_st = harvest()
    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp_p, build_p, _ = rv.build_build_parcels(
        ns, fake_st, v6, list(cb_by.values()), snapshot)
    cb_all = list(cb_by.values())
    params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, TARGET_SB)
    _d0, _s2, _o2, wins, forced = run_corner_pk(
        ns, fake_st, cb_all, cad, params, temp_p, build_p, TARGET_SB, snapshot=snapshot)

    # app.py 之 sha256（本態之受測物指紋·⛔ 供辨識、非判準）
    _app = os.path.join(os.path.dirname(VERIFY), "app.py")
    _appsha = hashlib.sha256(open(_app, "rb").read()).hexdigest()
    P("  受測物 app.py sha256 = %s" % _appsha)
    P("")

    ERRS = {}
    LINES = {}
    for blk in BLKS:
        buf = io.StringIO()
        try:
            with contextlib.redirect_stdout(buf):
                try:
                    run_step_g(ns, fake_st, cb_all, cad, snapshot, params,
                               [tp for tp in build_p if tp.get("所屬街廓") == blk],
                               wins, forced, TARGET_SB)
                except Exception as e:                               # noqa: BLE001
                    ERRS[blk] = "%s: %s" % (type(e).__name__, str(e)[:400])
        finally:
            pass
        LINES[blk] = [ln for ln in buf.getvalue().splitlines() if MARK in ln]
        print("  [%s] T2-DIAG %d 列%s"
              % (blk, len(LINES[blk]),
                 ("  err=" + ERRS[blk][:70]) if blk in ERRS else ""),
              file=sys.stderr)

    P("── 一、逐街廓 run_step_g 之終止情形（⛔ 非停機款·照實載） ──")
    for blk in BLKS:
        P("  %-3s ｜ [T2-DIAG] %d 列 ｜ %s"
          % (blk, len(LINES[blk]),
             ("例外 " + ERRS[blk]) if blk in ERRS else "⛔ 無例外"))
    P("")

    P("── 二、[T2-DIAG] 整列逐位（X-T 之比較端·⛔ 未解析欄位） ──")
    flat = []
    for blk in BLKS:
        if not LINES[blk]:
            P("  🔴 %s：**⛔ 無 [T2-DIAG]** ⇒ 逐字具名，⛔ 不以推定代之" % blk)
            continue
        for i, ln in enumerate(LINES[blk]):
            P("  <%s#%d> %s" % (blk, i, ln))
            flat.append("%s#%d\t%s" % (blk, i, ln))
    P("")

    P("── 三、X-T 之比較指紋 ──")
    payload = "\n".join(flat)
    P("  [T2-DIAG] 總列數 = %d" % len(flat))
    P("  逐街廓列數 = %s" % {b: len(LINES[b]) for b in BLKS})
    P("  payload bytes = %d" % len(payload.encode("utf-8")))
    P("  payload sha256 = %s" % hashlib.sha256(payload.encode("utf-8")).hexdigest())
    P("")
    P("  🔒 X-T 之判準 ＝ 上開『總列數 ＋ 逐街廓列數 ＋ payload sha256 ＋ 逐列原文』")
    P("     四者<u>皆須</u>與期初量相同；⛔ 僅 sha256 相同不足（須併看列數，防兩造皆空之假綠）。")
    P("=" * 110)

    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(L) + "\n")
    print("\n  ✅ 已落檔：%s" % path, file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
