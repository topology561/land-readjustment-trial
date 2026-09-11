# -*- coding: utf-8 -*-
"""`W-G.9-268′` 補令六 `§三-2` 另須答：`got_抵費地_退縮*.csv` 之 `(甲)`／`(乙)` 判。

🔑 **本器⛔ 比落檔**（坑 `5`：`off` 中止只寫 `_partial`、舊檔仍在原地 ⇒ 二態易比到**同一舊檔**）。
   改**於記憶體側**取 `run_corner_pk` 之第 `3` 回傳 `off`——**即該 CSV 之唯一來源**
   （`verify/run_verification.py:604` `_dump_csv(off, …got_抵費地_退縮{tag}.csv)`）
   ⇒ 二態逐位比其**來源物**，⛔ 受落檔時序污染。

🔒 **併出艙該物之受詞**：其欄為 `街廓`／`端`／`抵費地面積＝range(㎡)`／`指配`
   ——係**街角 PK 階段**之「**強制抵費地**」指派（`K-9-24 二·5`：範圍嚴格等於街角規定範圍），
   **⛔ `run_step_g` 之調配池**。二者同名而異物。

用法：`python verify/probes/probe_WG9268p_offsrc.py [倉根]`
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(HERE))
VERIFY = os.path.join(REPO, "verify")
sys.path.insert(0, VERIFY)
sys.path.insert(0, os.path.join(VERIFY, "fixtures"))
sys.path.insert(0, HERE)

from app_harvest import harvest                                     # noqa: E402
import wg9268p_selector_liveness as _LIVE                          # noqa: E402
import run_verification as rv                                       # noqa: E402
from selection_pipeline import run_corner_pk                        # noqa: E402

FLAG = "WG9268P_ANCHOR_GEOM"
SCEN = (("0m", 0.0), ("3.5m", 3.5))


def ser(rows):
    """逐位可比之正規化序列化（欄序固定·⛔ 依 dict 序）。"""
    if not rows:
        return "<空>"
    cols = sorted(rows[0].keys())
    out = ["\t".join(cols)]
    for r in rows:
        out.append("\t".join(repr(r.get(c)) for c in cols))
    return "\n".join(out)


def main():
    ns, fake_st = harvest()
    if not _LIVE.assert_live(ns, "probe_WG9268p_offsrc.py"):
        print("🔴 選擇器活體檢不過 ⇒ 本次輸出⛔ 出艙（⛔ 判綠·⛔ 靜默續跑）")
        return 4
    print()
    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp_p, build_p, _ = rv.build_build_parcels(
        ns, fake_st, v6, list(cb_by.values()), snapshot)

    print("🔒 管線已建：街廓 %d ／宗 %d" % (len(cb_by), len(build_p)))
    print()
    bad = 0
    for tag, sb in SCEN:
        got = {}
        for flag_on in (False, True):
            if flag_on:
                os.environ[FLAG] = "1"
            else:
                os.environ[FLAG] = '0'   # 🔒 顯式 off（⛔ pop ＝ 取預設·c2 後預設為 on）
            try:
                params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, sb)
                _d, _s, off, _w, _f = run_corner_pk(
                    ns, fake_st, list(cb_by.values()), cad, params, temp_p,
                    build_p, sb, snapshot=snapshot)
            finally:
                os.environ.pop(FLAG, None)
            got["on" if flag_on else "off"] = ser(off)
            print("   [%-4s ／ 旗標 %-3s] `off` 列數 ＝ **%d**（母體基數）"
                  % (tag, "on" if flag_on else "off", len(off)))
            if not flag_on:
                for r in off:
                    print("        %r" % (r,))
        same = got["off"] == got["on"]
        print("   ⇒ 二態逐位相同？ **%s**" % ("是 ✅" if same else "否 🔴"))
        if not same:
            bad += 1
        print()

    print("🔑 **判別力（證本比對非恆綠）**：對同一物注入一必然之改動，須轉紅")
    probe = ser([{"街廓": "R4", "端": "左", "指配": "強制抵費地",
                  "抵費地面積＝range(㎡)": "116.08"}])
    probe2 = ser([{"街廓": "R4", "端": "左", "指配": "強制抵費地",
                   "抵費地面積＝range(㎡)": "116.09"}])
    print("   人造二物逐位相同？ **%s**（須「否」）%s"
          % ("是" if probe == probe2 else "否", "✅" if probe != probe2 else "🔴"))
    print("   人造同物逐位相同？ **%s**（須「是」）%s"
          % ("是" if probe == probe else "否", "✅"))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
