# -*- coding: utf-8 -*-
"""`W-G.9-268′` 補令十一 `§二-2`：**選擇器活體檢**（`state-selector liveness`）。

🩸 **其存在理由（自毀式之第三例·補令十一 `§二-1`）**
   `c3` 移除旗標 `WG9268P_ANCHOR_GEOM` ⇒ 錨之計算變為**無條件執行**
   ⇒ 全倉**七支**以 `environ[FLAG]='0'` 取 `off` 態之探針，其 `off` 態將**取得 `on` 態**，
   二態遂逐位相同。
   🔴 **其後果較前二例為重**：`S-1` 之「六數全 `0`」⇒ **恆紅**（loud）；
   覆蓋帳之 `_partial` 缺失 ⇒ `FileNotFoundError`（loud）；**本例 ⇒ 靜默之<u>假綠</u>**。
   🔒 **既有之修（`683b7fa`：`pop` → 顯式 `'0'`）⛔ 擋得住本例**——**分支本身消失**，設任何值皆同。

🔒 **本檢之受詞（補令十一 `§二-2` 逐字）**
   > **本探針所構造之二態，須於一個<u>具名之可觀測量</u>上確有相異**。
   > **二態於該量上逐位相同 ⇒ 🛑 loud 拒測（`rc ≠ 0`）**，並逐字具名二種可能成因：
   > `(a)` 受測之變更為 no-op；`(b)` **態之選擇機制已失效（如旗標已被 `c3` 移除）**。
   > **⛔ 判綠、⛔ 靜默續跑。**

🔑 **所取之可觀測量 ＝ `(‵_oblique_s_max‵ 之被呼叫次數, 回傳值)`**（⛔ 動生產碼）
   —— 其**直接**即「態之選擇機制」本身：旗標 `off` 之分支**逕回 `cum_S` 而⛔ 呼叫** `_oblique_s_max`；
   旗標 `on` 則必呼叫之。`c3` 移除旗標後二態皆呼叫 ⇒ 該量逐位相同 ⇒ 本檢轉紅。
   🔒 對**以「相同」為期望結果之探針**（如 `probe_WG9268p_offsrc.py`：`run_corner_pk` 結構上⛔ 讀該旗標）
   亦適用，⛔ 需另備「已知須相異」之管線輪（補令十一 `§二-2` 末款所慮者）。

🩸 **⛔ 以合成幾何為受詞（本模組首版之自捕）**
   首版以「單位正方形 ＋ `d̂ = (1,0)` ＋ `allocation_dir = (0,1)`」為合成輸入，
   而 `_strip_axis` 之 `m_hat ∥ allocation_dir` ⇒ `denom = d̂·m̂ = 0` ⇒ **`RuntimeError`（loud）**
   ⇒ 二態皆拋例外、皆「相同」⇒ **甲乙二造同紅**，本檢失能（由其**兩造自證**當場擋下）。
   🛑 **且⛔ 得改用 `alloc ∥ d_hat`**——`_strip_axis` docstring 逐字載其為**失敗考古 `#7`**：
   「首版合成測用 `alloc ∥ d_hat`（正交）全綠＝**只測了自己的想像**；**斜交是本案常態**」。
   ⇒ 本模組**改以<u>分支之被觀測</u>為受詞**，**⛔ 需任何幾何為真**（`_oblique_s_max` 以替身取代）。

🛑 **本模組⛔ 改任何既有探針之判準與容差**（補令十一 `§二-2` 明令：本檢係**增設**）。
"""
import os

FLAG = "WG9268P_ANCHOR_GEOM"
OBS = "`(｀_oblique_s_max｀ 之被呼叫次數, 回傳值)`"

_CC = [(0.0, 0.0), (1.0, 0.0), (1.0, 1.0)]
_SENT = 1.0                  # 替身之回傳值（⛔ 幾何·⛔ 需為真）


def probe(ns):
    """回 `(ok, v_off, v_on, err)`。⛔ 吞例外——其為 loud 之一部分。

    🔒 以**替身**取代 `ns['_oblique_s_max']`，只數其**被呼叫次數**
       ⇒ ⛔ 依賴任何幾何為真（首版之自捕·見模組 docstring）。
    """
    fn = ns.get("_wg9268p_anchor_advance")
    if fn is None:
        return False, None, None, "`ns` 內⛔ 有 `_wg9268p_anchor_advance`"
    if "_oblique_s_max" not in ns:
        return False, None, None, "`ns` 內⛔ 有 `_oblique_s_max`"
    calls = {"n": 0}
    orig_osm = ns["_oblique_s_max"]

    def _stub(*_a, **_k):
        calls["n"] += 1
        return _SENT

    vals = {}
    old = os.environ.get(FLAG)
    ns["_oblique_s_max"] = _stub
    try:
        for mode, v in (("off", "0"), ("on", "1")):
            os.environ[FLAG] = v
            calls["n"] = 0
            r = fn(0.0, _CC, (1.0, 0.0), (0.0, 0.0), (0.0, 1.0))
            vals[mode] = (calls["n"], float(r))
    except Exception as e:                                          # noqa: BLE001
        return False, vals.get("off"), vals.get("on"), "呼叫拋例外：%r" % (e,)
    finally:
        ns["_oblique_s_max"] = orig_osm
        if old is None:
            os.environ.pop(FLAG, None)
        else:
            os.environ[FLAG] = old
    return (vals["off"] != vals["on"]), vals["off"], vals["on"], None


def assert_live(ns, who):
    """置於**全部判定之前**。不過 ⇒ 印 loud 訊息並回 `False`（呼叫端須 `rc ≠ 0`）。"""
    ok, vo, vn, err = probe(ns)
    print("── 選擇器活體檢（`state-selector liveness`·補令十一 `§二-2`）──")
    print("   受檢之探針 ＝ `%s`" % who)
    print("   具名之可觀測量 ＝ %s" % OBS)
    print("   旗標 `off`（顯式 `'0'`）⇒ %r" % (vo,))
    print("   旗標 `on` （顯式 `'1'`）⇒ %r" % (vn,))
    if err:
        print("   🛑 **loud 拒測**：%s" % err)
    elif ok:
        print("   ⇒ 二態於該量上**確有相異** ⇒ ✅ **選擇器仍活**")
        return True
    else:
        print("   🛑 **二態於該量上逐位相同 ⇒ loud 拒測**（⛔ 判綠、⛔ 靜默續跑）")
    print("   🛑 **二種可能成因（逐字具名·⛔ 擇一而不言其二）**：")
    print("      `(a)` 受測之變更為 **no-op**；")
    print("      `(b)` **態之選擇機制已失效**（如旗標 `%s` 已被 `c3` 移除）。" % FLAG)
    return False
