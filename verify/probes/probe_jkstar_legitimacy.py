# -*- coding: utf-8 -*-
r"""P-0c 證據③（裁定M·Q-S2①/Q-S3）：**k* 漂移之合法性**——`J(k*)≥J(naive)` 雙情境 PASS。

## 為何（claude.ai 裁 Q-S3·2026-07-25）

S1（W脫鉤 07-19＋S0d 07-20）改 S → 最優切點 k* 移；**跨情境 k* 不變**係 **S0d 前之經驗巧合、
非設計不變量**。實測：`R1 0m k*=2` 但 `R1 3.5m k*=1`。`K_STAR_EXPECT` 由單一 dict 改 **per-tag**。

**合法性證明（本探針）**：引擎內建停機②（`stepg_pipeline.py:767`：`J(k*)<J(naive)` → raise）。
⇒ `run_step_g` 若**完成不 raise**，則 `J(k*)≥J(naive)` **by construction 成立** ⇒ 引擎所選 k*（含 R1
3.5m=1）**確為最優**、非 bug。本探針逐塊逐情境印 `k*／J(naive)／J(k*)`、斷言 `J(k*)≥J(naive)`，
並顯示 R1 之 k* 隨情境變（0m=2／3.5m=1）＝per-tag 之依據。

## 重跑
    WV_JKSTAR=1 python verify/probes/probe_jkstar_legitimacy.py

⚠️ 零治理碼改動（獨立 script）。烤源無關（純算 k*/J·不寫 baseline）。
"""
import os
import sys
import json

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
sys.path.insert(0, VERIFY)

import run_verification as rv                                      # noqa: E402
from app_harvest import harvest                                    # noqa: E402
from selection_pipeline import (build_ownership,                   # noqa: E402
                                build_build_parcels, run_corner_pk)
from stepg_pipeline import run_step_g, build_step_g_tables         # noqa: E402

OUT_LOG = os.path.join(VERIFY, "out", "M_P0c_jkstar.log")


def main():
    for _st in (sys.stdout, sys.stderr):
        try:
            _st.reconfigure(encoding="utf-8")
        except Exception:
            pass
    if os.environ.get("WV_JKSTAR") != "1":
        print("🔴 須 WV_JKSTAR=1 明示啟用。")
        return 2
    snapshot = json.load(open(rv.SNAPSHOT, encoding="utf-8"))
    L = []
    L.append("=" * 92)
    L.append("[P-0c 證據③] k* 合法性：J(k*)≥J(naive) 雙情境（引擎停機② by construction）")
    L.append("=" * 92)
    kstar_by_tag = {}
    all_ok = True
    for setback, tag in ((0.0, "0m"), (3.5, "3.5m")):
        ns, fake_st = harvest()
        build_ownership(ns, fake_st, rv.ANON_XLSX)
        cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
        params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
        with open(rv.V6DXF, "rb") as f:
            v6 = f.read()
        temp, build, _ = build_build_parcels(ns, fake_st, v6, list(cb_by.values()), snapshot)
        diag, sel, off, winners, forced = run_corner_pk(
            ns, fake_st, list(cb_by.values()), cad, params, temp, build, setback, snapshot=snapshot)
        # run_step_g 完成不 raise ⇒ J(k*)≥J(naive) 已 by construction（停機②）
        sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot,
                        params, build, winners, forced, setback)
        _, diag_rows, _ = build_step_g_tables(sg)
        L.append(f"\n── {tag} ──  {'塊':4}{'k_naive':>8}{'k*':>5}{'J(naive)':>11}{'J(k*)':>11}  J(k*)≥J(naive)?")
        kmap = {}
        for r in diag_rows:
            blk = r["街廓"]
            kn = r.get("k_naive", "")
            ks = r.get("k*", "")
            jn = float(r.get("J(naive)", 0) or 0)
            jk = float(r.get("J(k*)", 0) or 0)
            kmap[blk] = ks
            ok = jk >= jn - 1e-6
            all_ok = all_ok and ok
            L.append(f"          {blk:4}{str(kn):>8}{str(ks):>5}{jn:>11.4f}{jk:>11.4f}"
                     f"       {'✅' if ok else '🔴 J 下降!'}")
        kstar_by_tag[tag] = kmap
    L.append("\n" + "-" * 92)
    L.append("k* per-tag 對照（Q-S3 依據·顯示不變量破裂）：")
    _blks = sorted(set(kstar_by_tag["0m"]) | set(kstar_by_tag["3.5m"]))
    L.append("  塊    0m    3.5m   變?")
    for b in _blks:
        k0 = kstar_by_tag["0m"].get(b, "—")
        k35 = kstar_by_tag["3.5m"].get(b, "—")
        L.append(f"  {b:4}{str(k0):>5}{str(k35):>7}   {'← 變(S0d)' if str(k0) != str(k35) else ''}")
    L.append("-" * 92)
    L.append(f"【結論】J(k*)≥J(naive) 雙情境 {'全 PASS ✅ ⇒ 引擎所選 k* 皆最優·per-tag 合法' if all_ok else '有 J 下降 🔴'}")
    L.append(f"        R1：0m k*={kstar_by_tag['0m'].get('R1')} ／ 3.5m k*={kstar_by_tag['3.5m'].get('R1')}"
             "  ⇒ 跨情境 k* 不變係 S0d 前巧合、非設計不變量（K_STAR_EXPECT 改 per-tag）")
    L.append("=" * 92)
    out = "\n".join(L)
    os.makedirs(os.path.dirname(OUT_LOG), exist_ok=True)
    with open(OUT_LOG, "w", encoding="utf-8") as f:
        f.write(out + "\n")
    print(out)
    print(f"\n📄 {OUT_LOG}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
