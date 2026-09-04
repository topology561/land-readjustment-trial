# -*- coding: utf-8 -*-
"""W-G.9-219R2 工項三 `a`：**六情境**之實測（⛔ 以自報充驗收）。

🔒 **本探針⛔ 鏡寫 app 之邏輯**——受測之三段碼**逐字自 `app.py` 抽出後執行**：
  1. 常設顯示區塊（`W-G.9-219R2` 工項二·`st.expander` 之前）；
  2. 退縮欄專屬 `on_change`（`_f3L_setback_changed`）；
  3. 下游三入口之讀取式：`_need`（`_build_wf_ctx` 內）與 `_wf_tag_of`（模組級）之**定義原文**，
     以及主路徑之 `.get(KEY)` ＋ `is None` 硬停二列。
  抽出以**標記字樣**定位並 `assert` 命中數 ＝ 1；抽出之逐字一併出艙供人核。

🔒 **下游「逐入口」之射程界（⛔ 誇稱）**：本探針量的是**三入口之讀取式**在該輪 session 上之
  實收值；**⛔ 為 app 之整輪實跑**（後者需 DXF／Step-G 全狀態，headless ⛔ 可得）。
  三入口之讀取式係自 `app.py` **逐字抽出**，故其對應可逐列復驗。

用法：`python verify/probes/probe_WG9219R2_source_display.py`　退出 `0` ＝ 六情境全符期望。
"""
import os
import re
import subprocess
import sys
import textwrap

from streamlit.testing.v1 import AppTest

KEY = "f3L_setback_default"
FLAG = "f3L_setback_user_set"
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))


def app_lines():
    """索引側 blob（`GB-139 ②`·⛔ 工作樹）。"""
    r = subprocess.run(["git", "-C", REPO, "cat-file", "blob", ":app.py"], capture_output=True)
    assert r.returncode == 0, ("cat-file rc", r.returncode)
    return r.stdout.decode("utf-8").replace("\r\n", "\n").split("\n")


def grab(lines, start_sub, end_sub, lab):
    """抽 [首個含 start_sub 之列 … 其後首個含 end_sub 之列]，二端各 assert 命中 1。"""
    s = [i for i, x in enumerate(lines) if start_sub in x]
    assert len(s) == 1, (lab + "·起", len(s))
    e = [i for i, x in enumerate(lines) if i >= s[0] and end_sub in x]
    assert len(e) >= 1, (lab + "·迄", 0)
    blk = lines[s[0]:e[0] + 1]
    return textwrap.dedent("\n".join(blk)), s[0] + 1, e[0] + 1


def build_script(disp, cb):
    body = textwrap.indent(disp, "    ") + "\n" + textwrap.indent(cb, "    ")
    return (
        "import streamlit as st\n"
        "\n"
        "def _f3L_invalidate_g_cache():        # 樁：app 既有之失效函式（⛔ 本探針之受測物）\n"
        "    st.session_state['_stub_invalidated'] = True\n"
        "\n"
        "_show = st.session_state.get('_show', True)\n"
        "if not _show:\n"
        "    st.info('branch-not-rendered')\n"
        "else:\n"
        + body + "\n"
        "    _setback_init = float(st.session_state.get('" + KEY + "', 3.5))\n"
        "    st.number_input('setback', min_value=0.0, max_value=10.0,\n"
        "                    value=_setback_init, step=0.1,\n"
        "                    key='" + KEY + "', on_change=_f3L_setback_changed)\n"
    )


def make_downstream(lines):
    """自 `app.py` 抽 `_need`／`_wf_tag_of` 之定義原文並執行 ⇒ 下游二入口之真碼。"""
    nd, nd_a, nd_b = grab(lines, "def _need(k):", "return ss[k]", "_need")
    tg, tg_a, tg_b = grab(lines, "def _wf_tag_of(setback):",
                          "非 UC9898 雙情境（0/3.5），引擎凍結錨不適用", "_wf_tag_of")
    g = {}
    exec(tg, g)                                   # `:%d`–`:%d`
    return nd, (nd_a, nd_b), tg, (tg_a, tg_b), g["_wf_tag_of"]


def probe_downstream(ss, need_src, wf_tag_of):
    """三入口之實收（逐入口·⛔ 只驗其一）。
    🔒 `AppTest.session_state` 係 `SafeSessionState` 代理，**⛔ `.get()`／⛔ `dict()`**
      （首版誤用致 `AttributeError`·當場更正）⇒ 一律以 `in` ＋ `[]` 取，另建純 dict 供 `_need`。"""
    out = {}
    snap = {}
    for k in (KEY, FLAG):
        if k in ss:
            snap[k] = ss[k]
    # E1 主路徑：`.get(KEY)` ＋ `is None` 硬停（`app.py` 之二列逐字語義）
    raw = snap.get(KEY)
    out["E1"] = "🔴 loud raise（缺鍵）" if raw is None else float(raw)
    # E2 §7 引擎接線：`float(_need(KEY))`——以 app 之 `_need` 原文執行
    ns = {"ss": snap}
    exec(need_src, ns)
    try:
        out["E2"] = float(ns["_need"](KEY))
    except RuntimeError as e:
        out["E2"] = "🔴 " + str(e)[:34]
    # E3 情境 tag：`_wf_tag_of(ss[KEY])`——以 app 之 `_wf_tag_of` 原文執行
    try:
        out["E3"] = wf_tag_of(snap[KEY])
    except KeyError:
        out["E3"] = "🔴 KeyError（缺鍵）"
    except RuntimeError as e:
        out["E3"] = "🔴 " + str(e)[:30]
    return out


DISP_RE = re.compile(r"\*\*本次退縮值：([^ ]+) m（(預設|使用者輸入)）\*\*")


def read_display(at):
    for m in at.markdown:
        mm = DISP_RE.search(m.value)
        if mm:
            return mm.group(1), mm.group(2)
    return ("🔴 無", "🔴 無")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    lines = app_lines()
    disp, d_a, d_b = grab(lines, "W-G.9-219R2 工項二：退縮值之**常設顯示**",
                          'st.markdown(f"**本次退縮值：', "常設顯示區塊")
    cb, c_a, c_b = grab(lines, "W-G.9-219R2 工項一 a／b：退縮欄**專屬**之 on_change",
                        "_f3L_invalidate_g_cache()", "on_change 區塊")
    need_src, nd_ln, tag_src, tg_ln, wf_tag_of = make_downstream(lines)

    print("=" * 112)
    print("【工項三 a】六情境實測——受測碼**逐字自 `app.py` 抽出**（索引側 blob）")
    print("  常設顯示區塊 ＝ `app.py:%d`–`:%d`（**%d** 列）" % (d_a, d_b, d_b - d_a + 1))
    print("  `on_change` 區塊 ＝ `app.py:%d`–`:%d`（**%d** 列）" % (c_a, c_b, c_b - c_a + 1))
    print("  下游 `_need` ＝ `app.py:%d`–`:%d`／`_wf_tag_of` ＝ `app.py:%d`–`:%d`"
          % (nd_ln[0], nd_ln[1], tg_ln[0], tg_ln[1]))
    print()
    print("  ── 抽出之常設顯示區塊（去縮排後之可執行列·註解略）──")
    for x in disp.split("\n"):
        if x.strip() and not x.strip().startswith("#"):
            print("     `%s`" % x)
    print()

    SRC = build_script(disp, cb)
    rows = []

    def measure(at, lab):
        ss = at.session_state
        v, s = read_display(at)
        d = probe_downstream(ss, need_src, wf_tag_of)
        rows.append((lab, v, s, d["E1"], d["E2"], d["E3"],
                     (ss[FLAG] if FLAG in ss else "（無）")))

    # ① 首次渲染
    at = AppTest.from_string(SRC, default_timeout=60)
    at.run()
    measure(at, "① 首次渲染（key 未存在）")
    # ② 輸入 0
    at2 = AppTest.from_string(SRC, default_timeout=60)
    at2.run()
    at2.number_input[0].set_value(0.0).run()
    measure(at2, "② 輸入 `0`")
    # ③ 輸入 3.5
    at3 = AppTest.from_string(SRC, default_timeout=60)
    at3.run()
    at3.number_input[0].set_value(3.5).run()
    measure(at3, "③ 輸入 `3.5`（＝ 預設值）")
    # ④ 輸入 2
    at4 = AppTest.from_string(SRC, default_timeout=60)
    at4.run()
    at4.number_input[0].set_value(2.0).run()
    measure(at4, "④ 輸入 `2`")
    # ⑤ 輸入 2 → 未渲染 → 再回
    at5 = AppTest.from_string(SRC, default_timeout=60)
    at5.run()
    at5.number_input[0].set_value(2.0).run()
    at5.session_state["_show"] = False
    at5.run()
    at5.session_state["_show"] = True
    at5.run()
    measure(at5, "⑤ 輸入 `2` → 未渲染 → 再回")
    # ⑥ 輸入 3.5 → 未渲染 → 再回
    at6 = AppTest.from_string(SRC, default_timeout=60)
    at6.run()
    at6.number_input[0].set_value(3.5).run()
    at6.session_state["_show"] = False
    at6.run()
    at6.session_state["_show"] = True
    at6.run()
    measure(at6, "⑥ 輸入 `3.5` → 未渲染 → 再回（丙案之盲點）")
    # ⑦ 併呈（⛔ 單所令之六情境·本探針加測）：值**曾改變**後回到 3.5
    at7 = AppTest.from_string(SRC, default_timeout=60)
    at7.run()
    at7.number_input[0].set_value(3.6).run()
    at7.number_input[0].set_value(3.5).run()
    measure(at7, "⑦ 併呈：`3.6` → 再改回 `3.5`（值曾改變）")

    print("  | 情境 | 顯示之值 | 顯示之來源 | `E1` `:12677` 主路徑 | `E2` `:14259` 引擎接線 | `E3` `:23810` tag | 旗標 |")
    print("  |---|---|---|---|---|---|---|")
    for r in rows:
        print("  | %s | `%s` | **%s** | `%s` | `%s` | `%s` | `%s` |" % r)
    print()

    # 🔒 **期望之出處（`fixture-provenance`：⛔ 由本探針之輸出回填）**
    #   逐格皆自 `W-G.9-219R2` 工項一 `b`／`c`／`d` ＋ 工項二 `d` 之**逐字**導出：
    #   工項一 `b` 逐字 ＝「來源 ＝『使用者輸入』⟺ 鍵 ∈ session_state **且** 旗標為真」，
    #   工項一 `a` 逐字 ＝ 旗標設於 **`on_change`** ⇒ 🔒 **Streamlit 之 `on_change` 僅於值<u>改變</u>時觸發**
    #   ⇒ `③`（把 `3.5` 設為 `3.5`·**值未變**）**⛔ 觸發** ⇒ 旗標不設 ⇒ 依該 ⟺ 得「**預設**」。
    #   （本列之期望於首版曾誤填「使用者輸入」——係**本探針作者之臆測**、⛔ 單之逐字；已當場更正。
    #     其語意含意見「【判】」末之上呈段。）
    EXP = [
        ("① 首次渲染（key 未存在）", "3.5", "預設", 3.5, 3.5, "3.5m", "（無）"),
        ("② 輸入 `0`", "0", "使用者輸入", 0.0, 0.0, "0m", True),
        ("③ 輸入 `3.5`（＝ 預設值）", "3.5", "預設", 3.5, 3.5, "3.5m", "（無）"),
        ("④ 輸入 `2`", "2", "使用者輸入", 2.0, 2.0, "🔴", True),
        ("⑤ 輸入 `2` → 未渲染 → 再回", "3.5", "預設", 3.5, 3.5, "3.5m", "（無）"),
        ("⑥ 輸入 `3.5` → 未渲染 → 再回（丙案之盲點）", "3.5", "預設", 3.5, 3.5, "3.5m", "（無）"),
        ("⑦ 併呈：`3.6` → 再改回 `3.5`（值曾改變）", "3.5", "使用者輸入", 3.5, 3.5, "3.5m", True),
    ]
    bad = []
    for got, exp in zip(rows, EXP):
        for i, nm in enumerate(("情境", "顯示值", "來源", "E1", "E2", "E3", "旗標")):
            a, b = got[i], exp[i]
            same = (str(a).startswith(str(b)) if (i == 5 and str(b) == "🔴") else a == b)
            if not same:
                bad.append("%s｜%s：得 `%r`／期 `%r`" % (got[0], nm, a, b))
    print("=" * 112)
    print("【判】期望之出處：`W-G.9-219R2` 工項一 `c`／`d` ＋ 工項二 `d` ＋ `W-G.9-226` 之乙案裁")
    print("  🔒 不符項 ＝ **%d**" % len(bad))
    for x in bad:
        print("     🔴 %s" % x)
    print()
    print("  🔒 `④` 之 `E3` 為 loud raise **係正解**——`_wf_tag_of` 逐字令「非 `UC9898` 雙情境"
          "（`0`／`3.5`）⇒ 引擎凍結錨不適用」；⛔ 本批所生之缺陷。")
    print("  🔒 **`⑥` 係乙案勝出之見證**：輸入值恰等預設 `3.5`，經未渲染往返後來源仍判「**預設**」"
          "——丙案（比對值相等）於此**必誤報「使用者輸入」**。")
    print()
    print("  🛑 **上呈（意思決定·⛔ 由 CC 裁）——`③` 與 `⑦` 之語意**")
    print("     `③`（把 `3.5` 設為 `3.5`·**值未變**）得「**預設**」；`⑦`（`3.6` → 再改回 `3.5`·**值曾變**）")
    print("     得「**使用者輸入**」。⇒ 🔒 **旗標所記者係「值曾被使用者<u>改變</u>」，⛔「欄曾被聚焦」**")
    print("     ——此係 `on_change` 之固有射程（Streamlit 僅於值改變時觸發），**⛔ 本實作之選擇**。")
    print("     🔒 二者之**顯示值皆為 `3.5`（正確）**，相異者僅**來源標籤**；且 `③` 之情形下，")
    print("     在用之值**與預設不可分辨**。是否要求 `③` 亦顯示「使用者輸入」，屬 KL 之意思決定。")
    ok = not bad
    print()
    print("  🛑 **工項三 `a` ＝ %s**" % ("PASS" if ok else "FAIL ⇒ 停"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
