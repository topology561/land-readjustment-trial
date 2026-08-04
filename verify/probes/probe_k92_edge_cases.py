# -*- coding: utf-8 -*-
r"""K-9-2 街廓層深度警示之**邊界與 loud raise** 檢（段三(c)-3 §四 升格為正式探針）。

合成輸入·不碰 DXF；**期望值由裁定文義手訂**（非由新碼回填·`fixture-provenance`）。

| 組 | 檢 |
|---|---|
| E1 | 「**等於也警示**」——`13.99/14.00/14.01` 對門檻 `14.00`；門檻確為附表值且**隨路寬變**（20m ⇒ 16.00）|
| E2 | 四條 loud raise：缺深度資訊／缺 `D_k92_min`／缺正面路寬（0）／附表查無深度 |
| E3 | K-9-3：回傳**僅街廓級**、無宗地級欄位 |

## 重跑

    python verify/probes/probe_k92_edge_cases.py

`rc=0` ⇒ 全數 OK。
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
sys.path.insert(0, VERIFY)
from app_harvest import harvest                                     # noqa: E402

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8")
    except Exception:
        pass

ns, _ = harvest()
f = ns["k92_block_depth_check"]
BLK = [{"label": "T1", "category": "住宅區"}]          # 路寬 8 ⇒ 附表 min_depth = 14.00
FW = {"T1": 8.0}


def di(v):
    return {"T1": {"d_front_p1": v, "d_front_p2": v + 1.0, "D_k92_min": v}}


ok = True


def chk(desc, got, exp):
    global ok
    hit = (got == exp)
    ok &= hit
    print(f"  {desc:<58} → {got!r:<8}（期 {exp!r}）　{'OK' if hit else 'FAIL'}")


def chk_raise(desc, fn, must_have):
    global ok
    try:
        r = fn()
        ok = False
        print(f"  {desc:<58} → FAIL 未 raise，回 {repr(r)[:40]}")
    except RuntimeError as e:
        good = all(m in str(e) for m in must_have)
        ok &= good
        print(f"  {desc:<58} → RuntimeError　{'OK' if good else 'FAIL 訊息未具名'}")
    except Exception as e:
        ok = False
        print(f"  {desc:<58} → FAIL {type(e).__name__}: {str(e)[:50]}")


print("【E1】『等於也警示』：門檻 14.00（住宅區×路寬 8m）")
chk("E1a 剖面 13.99 < 14.00 ⇒ warn",            f(BLK, di(13.99), FW)[0]["warn"], True)
chk("E1b 剖面 14.00 == 14.00 ⇒ warn（等於也警示）", f(BLK, di(14.00), FW)[0]["warn"], True)
chk("E1c 剖面 14.01 > 14.00 ⇒ 不 warn",          f(BLK, di(14.01), FW)[0]["warn"], False)
chk("E1d 門檻確為附表值 14.00（非常數兜底）",        f(BLK, di(20.0), FW)[0]["min_depth_table"], 14.00)
chk("E1e 路寬 12m 亦落 (7,15] 列 ⇒ 14.00",
    f(BLK, di(20.0), {"T1": 12.0})[0]["min_depth_table"], 14.00)
chk("E1f 路寬 20m 落 (15,25] 列 ⇒ 16.00（門檻確隨路寬變）",
    f(BLK, di(20.0), {"T1": 20.0})[0]["min_depth_table"], 16.00)

print("\n【E2】缺件 loud raise（禁靜默、禁跳過該街廓）")
chk_raise("E2a 缺深度資訊", lambda: f(BLK, {}, FW), ["K-9-2", "無 N-19′ 深度資訊"])
chk_raise("E2b 缺 D_k92_min",
          lambda: f(BLK, {"T1": {"d_front_p1": 1, "d_front_p2": 2}}, FW),
          ["K-9-2", "D_k92_min"])
chk_raise("E2c 缺正面路寬（0）⇒ 禁以附表最窄列兜底",
          lambda: f(BLK, di(20.0), {"T1": 0.0}), ["K-9-2", "正面路寬"])
chk_raise("E2d 非可建築分區 ⇒ 附表查無深度",
          lambda: f([{"label": "T1", "category": "道路"}], di(20.0), FW),
          ["K-9-2", "查無最小深度"])

print("\n【E3】不判宗地（K-9-3）：回傳僅街廓級")
_r = f(BLK, di(20.0), FW)[0]
chk("E3a 回傳筆數＝街廓數", len(f(BLK, di(20.0), FW)), 1)
chk("E3b 無宗地級欄位", [k for k in _r if "parcel" in k or "宗" in k], [])

print("\n" + ("=" * 60))
print("結果：" + ("全數 OK" if ok else "🔴 有 FAIL"))
sys.exit(0 if ok else 1)
