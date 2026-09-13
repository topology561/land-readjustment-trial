# -*- coding: utf-8 -*-
"""`W-G.9-270` 補令五 `§二-B` 款 `1`：**五錨逐錨分列**（＝ `GB-166` 之現態出艙）。

🛑 **⛔ 動 `verify/wd4_tier_list.py` 一字**——本器於**自身**內 `import` 各常數與 `compute()` 比對
  （補令五 `§二-B` 款 `1` 明令）。
🛑 本器**全唯讀**：⛔ 寫任何生產碼、⛔ 寫 `verify/baselines`、⛔ 設 `WV_BAKE`。
🛑 **⛔ 歸因、⛔ 提處置**（補令五 `§七` 款 `7`：照實出艙即止）。

🔒 **五錨之判定式逐字**（複製自 `verify/wd4_tier_list.py` 之 `main()`·⛔ 另寫第二份判準）
  `ok_m  = (d["mina_qu"] == MINA_QU_EXPECT) and (d["half_disp"] == HALF_EXPECT)`
  `ok_f  = (d["flagged_ct"] == FLAGGED_EXPECT) and (consumed == FLAGGED_EXPECT)`
        其中 `consumed = sum(int(g["含旗標宗數"]) for g in d["groups"])`
  `ok_t  = (d["tracks"] == TRACK_EXPECT) and (d["tiers"] == TIER_EXPECT)`
  `ok_p  = (_pub == PUB_TRACK_GROUPS)`
        其中 `_pub = sorted(g["歸戶鍵Gxxx"] for g in d["groups"] if g["軌別"] == "公設軌")`
  `ok_m2 = (_n_pub_parcels == PUB_PARCELS_EXPECT and _n_pub_holders == PUB_HOLDER_GROUPS_EXPECT)`
        其中 `_n_pub_parcels = sum(int(g["公設宗數"]) for g in d["groups"])`
              `_n_pub_holders = sum(1 for g in d["groups"] if int(g["公設宗數"]) > 0)`
  `allok = allok and ok_m and ok_f and ok_t and ok_p and ok_m2`

🔒 **自我驗證閘（⛔ 可省）**：本器所算之 `allok` 須與「`main()` 之聚合語意」相同
  ——即 `allok == all(五錨)`；且五錨中**至少一為紅**（`ok_m` 係已登記之恆紅）⋀
  **至少一為綠**（否則⛔ 能區辨「逐錨分列」與「全紅」）。二者任一不成立 ⇒ `rc = 5`。

用法：`PYTHONIOENCODING=utf-8 python verify/probes/probe_WG9270R5c_p9p_anchors.py [--dump <json 路徑>]`
`rc`：`0` 量測成立／`5` 量測器紅。
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
VERIFY = os.path.join(REPO, "verify")
sys.path.insert(0, VERIFY)

W = 100


def hr(t=""):
    print("\n── %s %s" % (t, "─" * max(0, W - len(t) - 4)))


def main():
    dump = None
    if "--dump" in sys.argv:
        dump = sys.argv[sys.argv.index("--dump") + 1]

    from wd4_tier_list import (compute, MINA_QU_EXPECT, HALF_EXPECT, FLAGGED_EXPECT,
                               TRACK_EXPECT, TIER_EXPECT, PUB_TRACK_GROUPS,
                               PUB_PARCELS_EXPECT, PUB_HOLDER_GROUPS_EXPECT)

    print("=" * W)
    print("【`W-G.9-270` 補令五 `§二-B` 款 `1`】**五錨逐錨分列**（`GB-166` 之現態出艙·解除條件 `(3)`）")
    print("=" * W)
    print("🛑 ⛔ 歸因、⛔ 提處置——照實出艙即止（補令五 `§七` 款 `7`）。")

    res = compute(fixture=False)
    payload = {}
    allok_by_tag = {}

    for tag in ("0m", "3.5m"):
        d = res[tag]
        g = d["groups"]
        consumed = sum(int(x["含旗標宗數"]) for x in g)
        _pub = sorted(x["歸戶鍵Gxxx"] for x in g if x["軌別"] == "公設軌")
        _np = sum(int(x["公設宗數"]) for x in g)
        _nh = sum(1 for x in g if int(x["公設宗數"]) > 0)

        anchors = [
            ("ok_m", (d["mina_qu"] == MINA_QU_EXPECT) and (d["half_disp"] == HALF_EXPECT),
             "mina_qu=%s / half_disp=%s" % (d["mina_qu"], d["half_disp"]),
             "MINA_QU_EXPECT=%s / HALF_EXPECT=%s" % (MINA_QU_EXPECT, HALF_EXPECT)),
            ("ok_f", (d["flagged_ct"] == FLAGGED_EXPECT) and (consumed == FLAGGED_EXPECT),
             "flagged_ct=%s / consumed=%s" % (d["flagged_ct"], consumed),
             "FLAGGED_EXPECT=%s（二者皆須等之）" % FLAGGED_EXPECT),
            ("ok_t", (d["tracks"] == TRACK_EXPECT) and (d["tiers"] == TIER_EXPECT),
             "tracks=%s / tiers=%s" % (json.dumps(d["tracks"], ensure_ascii=False),
                                       json.dumps(d["tiers"], ensure_ascii=False)),
             "TRACK_EXPECT=%s / TIER_EXPECT=%s" % (json.dumps(TRACK_EXPECT, ensure_ascii=False),
                                                   json.dumps(TIER_EXPECT, ensure_ascii=False))),
            ("ok_p", (_pub == PUB_TRACK_GROUPS),
             "_pub=%s" % json.dumps(_pub, ensure_ascii=False),
             "PUB_TRACK_GROUPS=%s" % json.dumps(PUB_TRACK_GROUPS, ensure_ascii=False)),
            ("ok_m2", (_np == PUB_PARCELS_EXPECT and _nh == PUB_HOLDER_GROUPS_EXPECT),
             "公設宗數Σ=%s / 持有群數=%s" % (_np, _nh),
             "PUB_PARCELS_EXPECT=%s / PUB_HOLDER_GROUPS_EXPECT=%s"
             % (PUB_PARCELS_EXPECT, PUB_HOLDER_GROUPS_EXPECT)),
        ]

        hr("情境 `退縮 %s`　五錨逐錨分列" % tag)
        print("   | 錨 | 判 | 實測值 | 期望值 |")
        print("   |---|---|---|---|")
        for name, ok, got, exp in anchors:
            print("   | `%s` | %s | %s | %s |" % (name, "🟢 綠" if ok else "🔴 **紅**", got, exp))
        vals = [a[1] for a in anchors]
        allok = all(vals)
        allok_by_tag[tag] = allok
        print("   ⇒ 聚合 `allok` ＝ **%s**（`RESULT: W-D.4 %s`）"
              % (allok, "CLEAN" if allok else "FAIL"))
        print("   🔑 **紅錨 ＝ %s**；**綠錨 ＝ %s**"
              % ([a[0] for a in anchors if not a[1]] or "（無）",
                 [a[0] for a in anchors if a[1]] or "（無）"))
        payload[tag] = {
            "anchors": {a[0]: {"ok": a[1], "got": a[2], "exp": a[3]} for a in anchors},
            "allok": allok,
            "mina_qu": d["mina_qu"], "half_disp": d["half_disp"],
            "tracks": d["tracks"], "tiers": d["tiers"], "flagged_ct": d["flagged_ct"],
            "groups": [{k: x.get(k) for k in
                        ("歸戶鍵Gxxx", "軌別", "宗數", "宗清單", "ΣG_戶(㎡)",
                         "含旗標宗數", "梯次", "對應v3級", "公設宗數")} for x in g],
        }

    # ── 自我驗證閘（⛔ 可省）────────────────────────────────────────────
    hr("自我驗證閘（⛔ 可省·證「逐錨分列」非恆紅亦非恆綠）")
    rc = 0
    for tag in ("0m", "3.5m"):
        a = payload[tag]["anchors"]
        reds = [k for k, v in a.items() if not v["ok"]]
        greens = [k for k, v in a.items() if v["ok"]]
        agg_ok = (payload[tag]["allok"] == all(v["ok"] for v in a.values()))
        c1 = len(reds) >= 1
        c2 = len(greens) >= 1
        print("   [%s] `allok == all(五錨)` ＝ %s ／ 紅錨 ≥1 ＝ %s ／ 綠錨 ≥1 ＝ %s"
              % (tag, agg_ok, c1, c2))
        if not (agg_ok and c1 and c2):
            print("   🔴 **量測器紅** ⇒ ⛔ 出艙任何逐錨判")
            rc = 5
    if rc == 0:
        print("   ⇒ **器非紅** ✅")

    if dump:
        with open(dump, "w", encoding="utf-8", newline="") as f:
            json.dump(payload, f, ensure_ascii=False, indent=1)
        print("\n🔒 dump ⇒ %s（%d B）" % (dump, os.path.getsize(dump)))
    return rc


if __name__ == "__main__":
    sys.exit(main())
