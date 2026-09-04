# -*- coding: utf-8 -*-
"""W-G.9-219R2 前置閘 `G4'`：**Streamlit widget 生命週期之實測**（⛔ 以推理代之）。

受詞（`W-G.9-219R2` `G4'` 逐字）：
    「退縮欄所在分支未渲染 ⇒ 下次 `.get` 回落預設」是否成立。

法：`streamlit.testing.v1.AppTest` 跑一支**最小重現**，其結構與 `app.py` 之步驟 L 同形——
一個 `if not <flag>: … else: <st.number_input(key=…)>` 之二分支，鍵名與 app 同
（`f3L_setback_default`），並在同一 script 內同時放一個**非 widget** 之 session 鍵作對照。

🔒 **判別力自證（`常規五`·兩造對照）**
  - 器須綠：非 widget 鍵（代稱 `PLAIN`）於同一輪未渲染時**存活** ⇒ 證「⛔ 全清 session」。
  - 器須紅：widget 鍵於分支未渲染時**消失** ⇒ 證該機制**確為 widget 專屬**。
  二者若同向（皆存活／皆消失），本探針即**無判別力**，其結論⛔ 得採。

🔒 **本探針⛔ 讀寫 `app.py`**，亦⛔ 動任何生產碼；其唯一產物係 stdout 之逐輪表。
用法：`python verify/probes/probe_WG9219R2_widget_lifecycle.py`　退出 `0` ＝ 受詞成立。
"""
import sys

import streamlit as _st_mod
from streamlit.testing.v1 import AppTest

KEY = "f3L_setback_default"
PLAIN = "plain_marker_not_a_widget"

SRC = '''
import streamlit as st

st.session_state.setdefault("%(plain)s", "SET_ONCE")     # 對照：非 widget 之 session 鍵
_show = st.session_state.get("_show", True)
if not _show:
    st.info("branch-not-rendered")
else:
    st.markdown("---")
    _init = float(st.session_state.get("%(key)s", 3.5))
    st.number_input("setback", min_value=0.0, max_value=10.0,
                    value=_init, step=0.1, key="%(key)s")
''' % {"key": KEY, "plain": PLAIN}


def snap(at, lab, rows):
    ss = at.session_state
    present = KEY in ss
    rows.append({
        "步": lab,
        "widget 渲染": len(at.number_input) > 0,
        "widget 鍵在": present,
        "值": (ss[KEY] if present else "ABSENT"),
        "非 widget 鍵在": (PLAIN in ss),
    })
    return rows[-1]


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 104)
    print("【`G4'`】Streamlit widget 生命週期之實測（`streamlit` ＝ **%s**）" % _st_mod.__version__)
    print("  受詞：**退縮欄所在分支未渲染 ⇒ 下次 `.get` 回落預設**")
    print()

    def seq(first_value, lab):
        at = AppTest.from_string(SRC, default_timeout=60)
        rows = []
        at.run()
        snap(at, "① 首跑（分支渲染）", rows)
        at.number_input[0].set_value(first_value).run()
        snap(at, "② 使用者輸入 %g" % first_value, rows)
        at.session_state["_show"] = False
        at.run()
        snap(at, "③ 分支**未渲染**（第 1 輪）", rows)
        at.run()
        snap(at, "④ 分支**未渲染**（第 2 輪）", rows)
        at.session_state["_show"] = True
        at.run()
        snap(at, "⑤ 分支**回復渲染**", rows)
        print("  ── 序列：%s ──" % lab)
        print()
        print("  | 步 | widget 渲染 | widget 鍵在 | 值 | 非 widget 鍵在 |")
        print("  |---|---|---|---|---|")
        for r in rows:
            print("  | %s | %s | %s | `%r` | %s |"
                  % (r["步"], r["widget 渲染"], r["widget 鍵在"], r["值"], r["非 widget 鍵在"]))
        print()
        return rows

    A = seq(2.0, "使用者輸入 **2.0**（≠ 預設）")
    B = seq(3.5, "使用者輸入 **3.5**（＝ 預設·丙案之致命盲點）")

    ok_drop = (A[1]["widget 鍵在"] and not A[2]["widget 鍵在"] and not A[3]["widget 鍵在"])
    ok_back = (A[4]["widget 鍵在"] and abs(float(A[4]["值"]) - 3.5) < 1e-9)
    ok_ctrl = all(r["非 widget 鍵在"] for r in A + B)
    ok_b = (B[1]["widget 鍵在"] and not B[2]["widget 鍵在"] and B[4]["widget 鍵在"])
    print("=" * 104)
    print("【判】")
    print("  🔒 `A②` 鍵在且值 ＝ 使用者值；`A③`／`A④` **鍵消失** ＝ **%s**（受詞之核心）" % ok_drop)
    print("  🔒 `A⑤` 鍵回來且值 **回落預設 3.5** ＝ **%s**（使用者之 2.0 已失）" % ok_back)
    print("  🔒 `B`（輸入 3.5）亦同：`B③` 鍵消失、`B⑤` 鍵回來 ＝ **%s**" % ok_b)
    print("  🔒 **對照組（器須綠）**：非 widget 鍵**全程存活** ＝ **%s**" % ok_ctrl)
    print("     ⇒ 該機制**係 widget 專屬**，**⛔ 「整個 session_state 被清」**。")
    ok = ok_drop and ok_back and ok_ctrl and ok_b
    print()
    print("  🛑 **`G4'` ＝ %s**（受詞%s成立）" % ("PASS" if ok else "FAIL", "" if ok else "**不**"))
    print("  🔒 ⇒ **乙案之前提坐實**：旗標若持久，其將活得比值久 ⇒ 錯報「使用者輸入」；")
    print("     而「來源 ＝ 使用者輸入 ⟺ 鍵在 ∧ 旗標」則於 `③`〜`⑤` 一律得「預設」，**自我修復**。")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
