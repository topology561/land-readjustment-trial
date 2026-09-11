# -*- coding: utf-8 -*-
"""`W-G.9-269` 補令十四 `§三-2`：**選擇器活體檢**（`K-9-17` 遞補旗標之態選擇機制）。

🩸 **其存在理由（自毀式之<u>第二次</u>·`§三-2` 逐字）**
   `c3` 移除旗標 `WG9269_K917_BACKFILL` ⇒ 遞補迴圈變為**無條件執行**
   ⇒ 三支以 `environ[FLAG]='0'` 取 `off` 態之探針，其 `off` 態將**取得 `on` 態**，
   二態遂逐位相同 ⇒ **靜默之假綠**。
   🔒 **`c2` 所行之修（`pop` → 顯式 `'0'`）⛔ 擋得住本例**——`c3` 後**分支本身消失**，設任何值皆同。

🔒 **本檢之受詞（`§三-2` 逐字·⛔ 改寫）**
   > **本探針所構造之二態，須於一個<u>具名之可觀測量</u>上確有相異**；
   > **二態於該量上逐位相同 ⇒ 🛑 loud 拒測（`rc ≠ 0`）**，並逐字具名二種可能成因：
   > `(a)` 受測之變更為 no-op；`(b)` **態之選擇機制已失效（如旗標已被 `c3` 移除）**。
   > **⛔ 判綠、⛔ 靜默續跑。**

🔴 **⛔ 沿用 `wg9268p_selector_liveness.py`（其適用性<u>不成立</u>·`§三-2` 令「沿用者須出艙其適用性之證」）**
   該模組之 `FLAG` ＝ **`WG9268P_ANCHOR_GEOM`**（**他旗標**），其可觀測量 ＝
   `_oblique_s_max` 經 `_wg9268p_anchor_advance` 之被呼叫次數。
   🛑 **該旗標已於 `W-G.9-268′` `c3` 移除** ⇒ 其二態**現已恆同** ⇒ 以之為本批之檢，
      其結果**與 `WG9269_K917_BACKFILL` 是否仍活<u>無關</u>** ⇒ **恰為本檢所欲防之假綠**。
   ⇒ 本模組**另立**，⛔ 取代、⛔ 修該模組一字。

🔑 **所取之可觀測量 ＝ `k917_should_drop` 之<u>被呼叫次數</u>**（⛔ 動生產碼）
   —— 其**直接**即「態之選擇機制」本身：
   `if ns['k917_backfill_enabled']():` 為 `False` ⇒ 該塊**整個不執行** ⇒ `k917_should_drop` **`0` 次**；
   為 `True` ⇒ 逐宗呼叫之 ⇒ **`> 0` 次**。
   🔒 `c3` 移除旗標後遞補迴圈無條件執行 ⇒ **二態之計數相同** ⇒ **本檢轉紅**（即其設計意圖）。
   🔒 **⛔ 需任何幾何為真**——本檢只數**分支之被觀測**，其替身**原樣委派**原函式
      （⛔ 改其回傳）⇒ ⛔ 影響受測探針之任何判定（承 `wg9268p_selector_liveness` 之設計）。

🛑 **本模組⛔ 改任何既有探針之判準與容差**——本檢係**增設**，且置於其全部判定**之前**。
"""

FLAG = "WG9269_K917_BACKFILL"
OBS = "`k917_should_drop` 之被呼叫次數"
SYM = "k917_should_drop"


def install(ns):
    """以**計數替身**包住 `ns[SYM]`（**原樣委派**·⛔ 改其回傳）。回計數器 `dict`。

    🛑 `ns` 內⛔ 有該符號 ⇒ **回 `None`**，其由呼叫端轉為 loud（⛔ 靜默略過）。
    """
    if SYM not in ns:
        return None
    c = {"n": 0, "_orig": ns[SYM]}
    orig = c["_orig"]

    def _counting(*a, **k):
        c["n"] += 1
        return orig(*a, **k)

    ns[SYM] = _counting
    return c


def uninstall(ns, c):
    if c is not None and "_orig" in c:
        ns[SYM] = c["_orig"]


def reset(c):
    if c is not None:
        c["n"] = 0


def _fail(kind):
    return (
        "🛑 **選擇器活體檢 loud 拒測**（`%s`）——可觀測量 ＝ %s\n"
        "   其二種可能成因（逐字·⛔ 擇一而不具名另一）：\n"
        "     `(a)` 受測之變更為 **no-op**；\n"
        "     `(b)` **態之選擇機制已失效**（如旗標 `%s` 已被 `c3` 移除 ⇒ 遞補迴圈無條件執行）。\n"
        "   ⛔ 判綠、⛔ 靜默續跑。" % (kind, OBS, FLAG)
    )


def check_two_state(n_off, n_on):
    """二態探針：`off` 須 `0` ⋀ `on` 須 `> 0` ⋀ 二者相異。回 `(ok, 訊息)`。"""
    if n_off is None or n_on is None:
        return False, _fail("`ns` 內⛔ 有 `%s` ⇒ ⛔ 可量" % SYM)
    if n_off == n_on:
        return False, _fail("二態之計數**逐位相同**：off ＝ %d ／ on ＝ %d" % (n_off, n_on))
    if n_off != 0:
        return False, _fail("`off` 態之計數**⛔ 為 `0`**（得 %d）⇒ 該態實非 `off`" % n_off)
    if n_on <= 0:
        return False, _fail("`on` 態之計數**⛔ 為正**（得 %d）⇒ 該態實非 `on`" % n_on)
    return True, ("✅ 選擇器活體：%s ＝ `off` **%d** ／ `on` **%d**（相異 ⋀ `off` 為 `0` ⋀ `on` 為正）"
                  % (OBS, n_off, n_on))


def check_flag_selector(ns):
    """**直接**觀測選擇器本身：`k917_backfill_enabled()` 於二設值下須回相異之布林。

    🛑 **單態探針⛔ 以「計數 ＝ `0`」單獨為證**——`0` 有二讀法：
       `(i)` 分支未執行（**所欲證者**）；`(ii)` 管線**根本未行至該處**。二者徵候相同。
       本檢直接餵選擇器二設值並讀其回傳 ⇒ **⛔ 依賴管線是否行至該處**，
       且 `c3` 移除該符號後即 **loud**（`ns` 內查無）。
    回 `(ok, 訊息)`。
    """
    import os
    fn = ns.get("k917_backfill_enabled")
    if fn is None:
        return False, _fail("`ns` 內⛔ 有 `k917_backfill_enabled` ⇒ 選擇器已不存在")
    prev = os.environ.get(FLAG)
    try:
        os.environ[FLAG] = "0"
        v_off = bool(fn())
        os.environ[FLAG] = "1"
        v_on = bool(fn())
    finally:
        if prev is None:
            os.environ.pop(FLAG, None)
        else:
            os.environ[FLAG] = prev
    if v_off == v_on:
        return False, _fail("選擇器於二設值下**回同值**（`'0'`→%s ／ `'1'`→%s）" % (v_off, v_on))
    if v_off or not v_on:
        return False, _fail("選擇器之極性顛倒（`'0'`→%s ／ `'1'`→%s）" % (v_off, v_on))
    return True, ("✅ 選擇器活體（**直接觀測**）：`k917_backfill_enabled()` "
                  "於 `'0'`→**False** ／ `'1'`→**True**（二值相異 ⋀ 極性正確）")


def check_single_off(n_off, ns=None):
    """單態（`off`）探針：`(1)` 選擇器須活體 ⋀ `(2)` 其計數須恰為 `0`。回 `(ok, 訊息)`。

    🔒 `c3` 後 `k917_backfill_enabled` 消失 ⇒ `(1)` loud；縱其仍在而遞補無條件執行，
       `(2)` 之計數必 `> 0` ⇒ 亦紅。**二款並取**方無 `0` 之二義（見 `check_flag_selector`）。
    """
    msgs = []
    if ns is not None:
        ok1, m1 = check_flag_selector(ns)
        msgs.append(m1)
        if not ok1:
            return False, "\n".join(msgs)
    if n_off is None:
        msgs.append(_fail("`ns` 內⛔ 有 `%s` ⇒ ⛔ 可量" % SYM))
        return False, "\n".join(msgs)
    if n_off != 0:
        msgs.append(_fail("`off` 態之計數**⛔ 為 `0`**（得 %d）⇒ 該態實非 `off`"
                          "（旗標或已被移除）" % n_off))
        return False, "\n".join(msgs)
    msgs.append("✅ 選擇器活體：%s 於所構造之 `off` 態 ＝ **0**"
                "（⇒ 該分支確未執行）" % OBS)
    return True, "\n".join(msgs)
