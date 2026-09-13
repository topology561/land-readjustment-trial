# -*- coding: utf-8 -*-
"""`W-G.9-270` 補令七 序 `4`：**`Σa 513.93` 之復現**。

🔒 **受詞 ＝ `Σa`（重劃前面積）·⛔ `Σ幾何面積_m2`**（補令七 序 `4` 明令）。
🔒 **複製 `wd4_tier_list.compute()` 之呼叫序**（⛔ 另寫第二份判準）以取 `g_rows`。
🛑 **自我驗證閘**：重建之逐戶 `ΣG_戶` 與 `宗數` 須與**同態 `compute()` 之 dump** 逐格相同；
  ⛔ 相符 ⇒ `rc = 5` loud 拒測，**⛔ 據以下任何結論**。
🛑 **⛔ 判孰誤、⛔ 追改發單側之記載**（序 `4` 明令）——相異即照實並報二值與各自之受詞。

用法：`PYTHONIOENCODING=utf-8 python verify/probes/probe_WG9270R5e_sigma_a.py <compute dump json>`
`rc`：`0` 量測成立／`5` 量測器紅。
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(REPO, "verify"))
os.chdir(REPO)

W = 100
GID = "G010"
MEMBERS = ("628-40(1)", "628-43(1)")     # 步驟 0 之成員（`a2c4b2b` commit message 逐字）
MERGED = "628-40(1)+"                     # 其合併後之命名


def hr(t=""):
    print("\n── %s %s" % (t, "─" * max(0, W - len(t) - 4)))


def main():
    ref_path = sys.argv[1]
    from app_harvest import harvest
    import run_verification as rv
    from selection_pipeline import build_ownership, build_build_parcels, run_corner_pk
    from stepg_pipeline import run_step_g

    print("=" * W)
    print("【`W-G.9-270` 補令七 序 `4`】**`Σa 513.93` 之復現**（受詞 ＝ `Σa`·⛔ `Σ幾何面積_m2`）")
    print("=" * W)
    print("🛑 ⛔ 判孰誤、⛔ 追改發單側之記載。")

    snapshot = rv.load_snapshot()
    ns, fake_st = harvest()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    build_ownership(ns, fake_st, rv.ANON_XLSX)
    groups = dict(fake_st.session_state["t8_ownership_groups"])
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp, build, _sw = build_build_parcels(ns, fake_st, v6, list(cb_by.values()), snapshot)

    with open(ref_path, encoding="utf-8") as f:
        ref = json.load(f)

    rc = 0
    for setback, tag in ((0.0, "0m"), (3.5, "3.5m")):
        params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
        _pk = run_corner_pk(ns, fake_st, list(cb_by.values()), cad,
                            params, temp, build, setback, snapshot=snapshot)
        sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot,
                        params, build, _pk[3], _pk[4], setback)
        g_rows = [r for r in sg["g_rows"] if r.get("推進側別") != "抵費地"]
        by_parent = {}
        for r in g_rows:
            by_parent.setdefault(r["原地號"], []).append(r)

        # ── 自我驗證閘 ────────────────────────────────────────────
        refg = {g["歸戶鍵Gxxx"]: g for g in ref[tag]["groups"]}
        bad = []
        for gid, parents in groups.items():
            lots = [r for p in parents for r in by_parent.get(p, [])]
            if gid not in refg:
                continue
            if len(lots) != int(refg[gid]["宗數"]):
                bad.append("%s 宗數 重建 %d vs compute %s" % (gid, len(lots), refg[gid]["宗數"]))
            s = round(sum(float(r.get("G(㎡)", 0) or 0) for r in lots), 2)
            if abs(s - float(refg[gid]["ΣG_戶(㎡)"])) > 1e-9:
                bad.append("%s ΣG_戶 重建 %s vs compute %s" % (gid, s, refg[gid]["ΣG_戶(㎡)"]))
        hr("情境 `退縮 %s`　自我驗證閘（重建 vs `compute()` dump）" % tag)
        print("   不符之項 ＝ %d %s" % (len(bad), "✅ 全綠" if not bad else "🔴"))
        for b in bad[:10]:
            print("     · %s" % b)
        if bad:
            print("   🛑 **loud 拒測** ⇒ ⛔ 據以下任何結論")
            rc = 5
            continue

        # ── 受詞：G010 之逐宗四欄 ─────────────────────────────────
        lots = [r for p in groups.get(GID, []) for r in by_parent.get(p, [])]
        hr("情境 `退縮 %s`　歸戶 `%s` 之逐宗（受詞 ＝ `a 面積(㎡)` ＝ 重劃前面積）" % (tag, GID))
        print("   | 暫編地號 | 原地號 | 所屬街廓 | `a 面積(㎡)` | `幾何面積(㎡)` | `G(㎡)` |")
        print("   |---|---|---|---|---|---|")
        sa = 0.0
        sgeo = 0.0
        for r in sorted(lots, key=lambda x: str(x.get("暫編地號"))):
            a = float(r.get("a 面積(㎡)", 0) or 0)
            geo = float(r.get("幾何面積(㎡)", 0) or 0)
            sa += a
            sgeo += geo
            print("   | `%s` | `%s` | `%s` | `%s` | `%s` | `%s` |"
                  % (r.get("暫編地號"), r.get("原地號"), r.get("所屬街廓"), a, geo, r.get("G(㎡)")))
        print("   ⇒ **`Σa` ＝ %.2f**（%d 宗）／`Σ幾何面積` ＝ %.2f" % (sa, len(lots), sgeo))

        hr("情境 `退縮 %s`　二值並報（⛔ 判孰誤）" % tag)
        print("   | 量 | 受詞 | 發單側／commit message 所載 | 本批實測 | 判 |")
        print("   |---|---|---|---|---|")
        print("   | `Σa` | **重劃前面積之和** | `513.93`（發單側現查·依賴序更正節） | **`%.2f`** | %s |"
              % (sa, "🟢 **相符**" if abs(sa - 513.93) < 0.005 else "🔴 **相異 %.2f**" % (sa - 513.93)))
        print("   | `Σ幾何面積_m2` | **幾何面積之和** | `513.79`（`a2c4b2b` commit message 逐字） | **`%.2f`** | %s |"
              % (sgeo, "🟢 **相符**" if abs(sgeo - 513.79) < 0.005 else "🔴 **相異 %.2f**" % (sgeo - 513.79)))
        print("   🔒 **成員（`a2c4b2b` 逐字）** ＝ `%s` ＋ `%s` ⇒ 合併後 `%s`"
              % (MEMBERS[0], MEMBERS[1], MERGED))
        print("   🛑 **⛔ 判孰誤、⛔ 追改發單側之記載**——相異即照實並報二值與各自之受詞。")
    return rc


if __name__ == "__main__":
    sys.exit(main())
