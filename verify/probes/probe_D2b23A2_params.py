r"""**D-2b-23【甲】commit A′**：`_solve_G_one` 五實參之**甲前**基準 —— ⛔ **零生產碼變更**

## 為何存在（KL 裁 2026-08-09·②「唯一殘餘條件」）

「街角資格不翻轉」之預測，其依據為**街角第 1 宗位於 W 鏈上游**
（`_corner_first_lot_G` 以 `W_prev=0.0`／`is_corner=True` 呼叫 `_solve_G_one`；
`grep -n "W_prev=0.0)" app.py` ⇒ `:11922`）。**上游不受下游影響係構造事實。**

⚠️ **惟該上游性只擋住「經第 2 宗幾何回饋」一條路。** `_solve_G_one` 之實參尚含
`S_max` 與案級參數 `A`／`B`／`C`／`tab6_burden`；若此五者於甲前甲後**有變**，
本預測即**不在射程內**。

⇒ 本檔記錄**甲前**值。commit C 以同法記**甲後**值，逐格對拍：
**相同** ⇒ 預測成立；**不同** ⇒ 預測作廢並依施工單 §9-3 停機上呈。
🔒 KL 逐字：「⛔ 逐街廓分跑下『應該相同』不算證據，**須有印出之值**。」

## 母體（⛔ 兩條路徑都要·⛔ 非只取其一）

- **資格路徑**：`run_corner_pk` 內（`_corner_block_true_G` → `_corner_first_lot_G` → `_solve_G_one`）
  ——`3.5m` R2／R5／R3 之 `真G` 即出於此。
- **實配路徑**：`run_step_g` 內。

## 方法

於兩段執行期間各掛一次 spy，記錄每次 `_solve_G_one` 之
`(S_max, A, B, C, tab6_burden)`；**逐 (情境, 街廓, 路徑) 收其相異值集合**，
並印出 `sha256` 摘要供甲後一眼對拍。⛔ 不做任何篩選或四捨五入以外之加工。
"""
import contextlib
import hashlib
import io
import json
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
W = 200
KEYS = ("S_max", "A", "B", "C", "tab6_burden")

def _resolve_out(default_name):
    """輸出檔名解析 ＋ **拒絕覆寫**守衛（⛔ 禁覆寫任何已入庫 log）。

    `WV_OUT_NAME=<新檔名>` 覆寫預設；⛔ 目標已存在即 raise，
    除非明示 `WV_ALLOW_OVERWRITE=1`。⇒ 甲前／甲後兩份得以**並存、可逐格對拍**。
    """
    name = os.environ.get("WV_OUT_NAME") or default_name
    path = os.path.join(OUTDIR, name)
    if os.path.exists(path) and os.environ.get("WV_ALLOW_OVERWRITE") != "1":
        raise RuntimeError(
            f"🔴 拒絕覆寫既有 log：{path}"
            f"　⇒ 請設 WV_OUT_NAME=<新檔名>（⛔ 禁覆寫已入庫實料）")
    return path



def _canon(v):
    """可比較之正規化表示（⛔ 不改值·只求可 hash／可印）。"""
    if isinstance(v, float):
        return repr(round(v, 9))
    if isinstance(v, dict):
        return "{" + ",".join(f"{k!r}:{_canon(v[k])}" for k in sorted(map(str, v))) + "}"
    if isinstance(v, (list, tuple)):
        return "[" + ",".join(_canon(x) for x in v) + "]"
    return repr(v)


def main():                                                          # noqa: C901
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8")
        except Exception:                                             # noqa: BLE001
            pass
    os.makedirs(OUTDIR, exist_ok=True)
    out = _resolve_out("probe_D2b23A2_params_before.log")   # ⚠️ **fail-fast**：先解析再跑（⛔ 別跑完才攔）
    L = []

    def P(s=""):
        L.append(s)
        print(s, file=sys.stderr)

    P("=" * W)
    P("【D-2b-23【甲】commit A′】`_solve_G_one` 五實參之**甲前**基準 — ⛔ 零生產碼變更")
    P("=" * W)
    P(f"  受記實參：{KEYS}")
    P("  依據：KL 2026-08-09 ②「唯一殘餘條件·須量不得推定」")

    ns, fake_st = harvest()
    SEEN = {}                     # (情境, 街廓, 路徑) -> {canon_tuple: count}
    _orig = ns["_solve_G_one"]

    def _spy(**kw):
        key = (_spy.tag, _spy.blk, _spy.path)
        tup = tuple(_canon(kw.get(k)) for k in KEYS)
        SEEN.setdefault(key, {})
        SEEN[key][tup] = SEEN[key].get(tup, 0) + 1
        return _orig(**kw)
    _spy.tag = _spy.blk = _spy.path = ""

    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp_p, build_p, _ = rv.build_build_parcels(
        ns, fake_st, v6, list(cb_by.values()), snapshot)
    cb_all = list(cb_by.values())
    blks = []
    for tp in build_p:
        _l = tp.get("所屬街廓")
        if _l and _l not in blks:
            blks.append(_l)

    for setback in (0.0, 3.5):
        sb = f"{setback:g}m"
        params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)

        # ── 資格路徑：run_corner_pk（⚠️ 一次跑全街廓 ⇒ 街廓欄記 '(全案)'）──
        _spy.tag, _spy.blk, _spy.path = sb, "(全案)", "資格"
        ns["_solve_G_one"] = _spy
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                _d0, _s2, _o2, wins, forced = run_corner_pk(
                    ns, fake_st, cb_all, cad, params, temp_p, build_p,
                    setback, snapshot=snapshot)
        finally:
            ns["_solve_G_one"] = _orig

        # ── 實配路徑：run_step_g（逐街廓 solo）──
        for lbl in blks:
            _spy.tag, _spy.blk, _spy.path = sb, lbl, "實配"
            ns["_solve_G_one"] = _spy
            try:
                with contextlib.redirect_stdout(io.StringIO()):
                    try:
                        run_step_g(ns, fake_st, cb_all, cad, snapshot, params,
                                   [tp for tp in build_p if tp.get("所屬街廓") == lbl],
                                   wins, forced, setback)
                    except Exception:                                 # noqa: BLE001
                        pass
            finally:
                ns["_solve_G_one"] = _orig
            print(f"    [{sb}] {lbl} 擷取完畢", file=sys.stderr)

    if not SEEN:
        raise RuntimeError("🔴 母體為空 ⇒ ⛔ 不得據此下任何結論")

    P("")
    P(f"  母體 ＝ {len(SEEN)} 個 (情境,街廓,路徑)（⛔ 非空）"
      f"／`_solve_G_one` 總呼叫 {sum(sum(d.values()) for d in SEEN.values())} 次")
    P("")
    for key in sorted(SEEN, key=lambda k: (k[0], k[2], k[1])):
        sb, blk, path = key
        d = SEEN[key]
        blob = json.dumps({",".join(t): c for t, c in sorted(d.items())},
                          ensure_ascii=False, sort_keys=True)
        dig = hashlib.sha256(blob.encode("utf-8")).hexdigest()
        P(f"  ── [{sb}] {blk}／{path}　相異組合 {len(d)}　呼叫 {sum(d.values())} 次"
          f"　sha256 {dig} ──")
        for t, c in sorted(d.items()):
            P(f"     ×{c:<4}" + "　".join(f"{k}={v}" for k, v in zip(KEYS, t)))

    with open(out, "w", encoding="utf-8") as fh:
        fh.write("\n".join(L) + "\n")
    print(f"\n📄 {out}", file=sys.stderr)


if __name__ == "__main__":
    main()
