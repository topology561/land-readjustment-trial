# -*- coding: utf-8 -*-
"""`W-G.9-248` 段乙 `I-2` 之**活體**合成案：`st.form` 內 widget 之生效時機。

🛑 **本檔⛔ 生產碼**（`verify/probes/`）·⛔ 被 `run_all`／`run_verification` 消費。
🔒 **立案之由**：單 `§二 c` 之 `I-2` 令「若 form 語意致其延遲 ⇒ **停機上呈**」，
   而該判**⛔ 得憑推理**（`CLAUDE.md`「須實測坐實·⛔ 推理充證」·`W-G.9-226` `G4'` 既例）。

🔑 **受測之二形**（逐字對應 `app.py` 之二介面）
  `A` ＝ **form 外**（介面乙·`f3L_mba_ov_{label}` 之形）——現行 `K-9-1` 覆寫欄所在。
  `B` ＝ **form 內**（介面甲·`f3_road_form` 之形）——單所令之移入目的地。

🔬 **決定性實驗（三步·⛔ 二步）**
  `S1` 改 `B` 之值 ⇒ form 內 widget **⛔ 觸發 rerun** ⇒ 畫面不動（預期）。
  `S2` 改 `A` 之值 ⇒ **觸發一次 rerun**。此時觀察 `B-ret`／`B-ss`：
       若仍為舊值 ⇒ **form 語意確致延遲**（`I-2` 之停機條件成立）。
  `S3` 按 `B` 之 submit ⇒ `B-ret`／`B-ss` 方轉為新值。

🔒 **判別力**：`A` 係**必然即時**之對照組；若 `A` 亦不即時 ⇒ **量測器紅**，
   其結論⛔ 出艙（`CLAUDE.md`「⛔ 停機上呈之前，必先自證量測器非紅」）。

跑法：`preview_start({name: "wg9248-form-probe"})`（`.claude/launch.json`）。
"""
import streamlit as st

st.set_page_config(page_title="W-G.9-248 I-2 form semantics", layout="wide")
st.title("`W-G.9-248` `I-2`：`st.form` 內 widget 之生效時機")
st.caption("受詞 ＝ 「移入 `st.form` 後，其寫回 `session_state` 之時機是否遲於現行」")

if "rerun_n" not in st.session_state:
    st.session_state["rerun_n"] = 0
st.session_state["rerun_n"] += 1
st.metric("本 session 之 rerun 次數", st.session_state["rerun_n"])

st.divider()

# ── A：form 外（介面乙之形·對照組·必然即時）────────────────────────────
st.header("A　form **外**（介面乙 `f3L_mba_ov_` 之形·對照組）")
a_ret = st.number_input("A：覆寫值（form 外）", min_value=0.0, step=1.0,
                        value=0.0, key="probe_A_outside")
st.write("**A-ret（number_input 之回傳值）** =", a_ret)
st.write("**A-ss（session_state[key]）** =", st.session_state.get("probe_A_outside"))

st.divider()

# ── B：form 內（介面甲之形·受測）──────────────────────────────────────
st.header("B　form **內**（介面甲 `f3_road_form` 之形·受測）")
with st.form("probe_form_B", clear_on_submit=False):
    b_ret = st.number_input("B：覆寫值（form 內）", min_value=0.0, step=1.0,
                            value=0.0, key="probe_B_inside")
    b_submitted = st.form_submit_button("✅ 提交（模擬「儲存路寬資料」）")

st.write("**B-ret（number_input 之回傳值）** =", b_ret)
st.write("**B-ss（session_state[key]）** =", st.session_state.get("probe_B_inside"))
st.write("**b_submitted** =", b_submitted)

st.divider()

# ── 消費端：模擬 app.py :20091（在 form 外、之後·即時消費）──────────────
st.header("C　消費端（模擬 `app.py:20091` `k91_min_alloc_contrib_by_blk`）")
st.write("此處讀取二值，模擬「同一輪內即時消費」：")
st.json({
    "自 A 讀（form 外·現行）": a_ret,
    "自 B 讀（form 內·移入後）": b_ret,
    "二者相等?": a_ret == b_ret,
})

st.divider()
st.subheader("🔬 判讀")
st.markdown(
    "- `S1` 改 **B** 之值：畫面**應不動**（form 內 widget ⛔ 觸發 rerun）。\n"
    "- `S2` 改 **A** 之值（觸發 rerun）：\n"
    "  - 若 **B-ret 仍為舊值** ⇒ 🔴 **form 語意確致延遲** ⇒ `I-2` 停機條件**成立**。\n"
    "  - 若 B-ret 已為新值 ⇒ 🟢 無延遲 ⇒ 得續辦工項一。\n"
    "- `S3` 按 **B** 之提交鈕：B-ret／B-ss 方轉為新值。\n"
    "- 🔑 **判別力**：**A** 須於 `S2` 即時反映；A 若不即時 ⇒ **量測器紅**、結論⛔ 出艙。"
)
