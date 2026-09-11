#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""`W-G.9-269` 補令十 `§三-2`：六宗之 `所屬街廓`／`G`／閘一判（`off` 態·逐情境）。

🩸 **其用**：`補令十 §三-2` 款 `2` 令「**逐街廓**出艙釋池量」⇒ 須先將受詞三宗
   （及其**同歸戶之另一宗**）定位至街廓，方能逐街廓對帳。
🔒 **母體** ＝ `run_step_g` 之 `g_rows`（**當次實跑**·⛔ baseline·`GB-162`）。
🔒 **旗標** ＝ **`off`**（本器於執行期 `pop` 該環境變數）⇒ 其所量者為**剔除前**之態。
🔒 `REPO` 自 `__file__` 上溯（⛔ 硬編他樹·`GB-161`）。
用法：`python verify/probes/probe_WG9269_c2_blk.py`
"""
import contextlib
import io
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)          # 🔒 自 `__file__` 上溯·⛔ 硬編他樹
sys.path.insert(0, VERIFY)
sys.path.insert(0, os.path.join(VERIFY, "fixtures"))
sys.path.insert(0, HERE)

from app_harvest import harvest                                     # noqa: E402
import run_verification as rv                                       # noqa: E402
from selection_pipeline import run_corner_pk                        # noqa: E402
from stepg_pipeline import run_step_g                               # noqa: E402

# 受詞三宗 ＋ 其**同歸戶之另一宗**（`G011`／`G025`／`G030` 各二宗）
SUBJ = ("628-42(1)", "628-53(2)", "628-27(1)", "628-42(2)", "628-53(1)", "628-27(2)")


def main():
    os.environ.pop("WG9269_K917_BACKFILL", None)      # 🔒 `off` 態
    ns, fake_st = harvest()
    snap = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snap)
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp, build, _ = rv.build_build_parcels(ns, fake_st, v6, list(cb_by.values()), snap)
    print("| 宗地 | 情境 | 所屬街廓 | G(㎡) | 驗_B藍影 |")
    print("|---|---|---|---|---|")
    n = 0
    for tag, sb in (("0m", 0.0), ("3.5m", 3.5)):
        params = rv.build_param_table(ns, fake_st, cb_by, cad, snap, sb)
        _d, _s, _o, wins, forced = run_corner_pk(
            ns, fake_st, list(cb_by.values()), cad, params, temp, build, sb, snapshot=snap)
        with contextlib.redirect_stdout(io.StringIO()):
            sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snap, params, build,
                            wins, forced, sb, eff_min_build_by_blk={})
        by = {str(r.get("暫編地號", "")): r for r in sg["g_rows"]}
        for pid in SUBJ:
            r = by.get(pid)
            n += 1
            if r is None:
                print("| `%s` | `%s` | ⛔ 在 `g_rows` | — | — |" % (pid, tag))
                continue
            print("| `%s` | `%s` | `%s` | %.2f | `%s` |"
                  % (pid, tag, r.get("所屬街廓"), float(r.get("G(㎡)", 0) or 0),
                     r.get("驗_B藍影")))
    if n == 0:                                        # loud 拒測（判定集為空）
        print("🔴 判定集為空 ⇒ loud 拒測")
        return 3
    print("判定集基數 ＝ **%d** 格" % n)
    return 0


if __name__ == "__main__":
    sys.exit(main())
