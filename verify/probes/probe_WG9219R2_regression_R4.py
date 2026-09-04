# -*- coding: utf-8 -*-
"""W-G.9-219R2 工項三 `b`：**迴歸**——以退縮 `3.5`（併 `0`）執行 `R4` 之分配，
其逐值須與改動前**相同**（改前值**自現態當場實算**為基準·⛔ 採用任何既載數）。

法：`harvest()`（exec `app.py`）→ `rv.build_pipeline` → `build_ownership` →
    `build_build_parcels` → `rv.build_param_table` → `run_corner_pk` → `run_step_g(setback)`，
    取 `g_rows` 中 `所屬街廓 == 'R4'` 之列，**正規化序列化**後出 `sha256`。

🔒 **run_step_g 於某些情境會 loud raise（結構閘）**——本探針**捕捉之並照實序列化**
   （型別＋訊息），⛔ 吞、⛔ 以「跑不完」代替比對：**改前／改後之<u>失敗形</u>亦須逐位相同**。
🔒 用法：於**拋棄式 clone** 內跑二次（改前／改後 `app.py`），對拍其 `sha256`。
   （`run_all` 會改寫已追蹤 log ⇒ 主 checkout 內⛔ 長跑；本探針**⛔ 寫任何檔**。）
🔒 本探針之受詞係 **`app.py` 之引擎符號**（`harvest` 取 `globals()` 之真符號）——
   `W-G.9-219R2` 之改動全在 `main()` 之 Streamlit UI 區塊內，而 `harvest` **從不呼叫 `main()`**
   （`CLAUDE.md` §7 逐字）⇒ 期望為**逐位相同**。
"""
import hashlib
import json
import os
import sys
import traceback

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(REPO, "verify"))

from app_harvest import harvest                                              # noqa: E402
import run_verification as rv                                                # noqa: E402
from selection_pipeline import build_ownership, build_build_parcels, run_corner_pk  # noqa: E402
from stepg_pipeline import run_step_g                                        # noqa: E402

BLK = "R4"
SETBACKS = (3.5, 0.0)


def one(ns, fake_st, cb_by, cad, snapshot, temp, build, setback):
    """回傳該情境之**正規化結果物**（成功 ⇒ R4 逐列；失敗 ⇒ 失敗形）。"""
    try:
        params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
        _d, _s, _o, winners, forced = run_corner_pk(
            ns, fake_st, list(cb_by.values()), cad, params, temp, build,
            setback, snapshot=snapshot)
        sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot,
                        params, build, winners, forced, setback)
    except BaseException as e:                       # noqa: BLE001（照實序列化·⛔ 吞）
        tb = traceback.extract_tb(sys.exc_info()[2])
        return {
            "狀態": "raise",
            "型別": type(e).__name__,
            "訊息": str(e),
            "拋出處": ["%s:%d:%s" % (os.path.basename(f.filename), f.lineno, f.name)
                       for f in tb],
        }
    rows = [r for r in sg["g_rows"] if str(r.get("所屬街廓", "")) == BLK]
    rows.sort(key=lambda r: str(r.get("暫編地號", "")))
    return {
        "狀態": "ok",
        "g_rows 全體列數": len(sg["g_rows"]),
        "%s 列數" % BLK: len(rows),
        "%s 逐列" % BLK: rows,
        "pool_diag[%s]" % BLK: sg.get("pool_diag", {}).get(BLK, {}),
    }


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    snapshot = rv.load_snapshot()
    ns, fake_st = harvest()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp, build, _sw = build_build_parcels(ns, fake_st, v6, list(cb_by.values()), snapshot)

    out = {}
    for sb in SETBACKS:
        out["退縮 %s" % sb] = one(ns, fake_st, cb_by, cad, snapshot, temp, build, sb)

    ser = json.dumps(out, ensure_ascii=False, sort_keys=True, indent=1, default=str)
    print("@@@REGRESSION-BEGIN@@@")
    print(ser)
    print("@@@REGRESSION-END@@@")
    print("@@@SHA256=%s@@@" % hashlib.sha256(ser.encode("utf-8")).hexdigest())
    print("@@@BYTES=%d@@@" % len(ser.encode("utf-8")))
    print("@@@APPPY-SHA256=%s@@@"
          % hashlib.sha256(open(os.path.join(REPO, "app.py"), "rb").read()).hexdigest())
    return 0


if __name__ == "__main__":
    sys.exit(main())
