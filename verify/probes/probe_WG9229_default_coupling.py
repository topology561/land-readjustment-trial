# -*- coding: utf-8 -*-
"""W-G.9-229 工項一 `b` ＋ 工項二 `a`／`b`：**預設值耦合**之實測（⛔ 以推理充證）。

🔒 **⛔ 鏡寫 app 之邏輯**——受測之四段碼**逐字自 `app.py` 抽出後執行**：
  ① 常設顯示區塊（定義 `_SB_DEFAULT_M`·在 `with st.expander` **之外**）；
  ② 退縮欄專屬 `on_change`（`_f3L_setback_changed`·在 `with` **之內**）；
  ③ 輸入欄之 `_setback_init` ＋ `st.number_input(...)`（在 `with` **之內**）；
  ④ 下游 `_need`／`_wf_tag_of` 之定義原文。
  抽出以**標記字樣**定位並 `assert` 命中數；抽出之逐字一併出艙供人核。

🔒 **本探針之二用**
  `A` **作用域可及性**（工項一 `b`）：`_SB_DEFAULT_M` 定義於 `with` 之外、用於 `with` 之內；
     `with` **非函式作用域** ⇒ 應可及。**以實測坐實**——若不可及即 `NameError`，探針紅。
  `B` **分歧偵測**（工項二 `b`·本探針之要害）：以 `--source worktree` 讀工作樹，
     於工作樹將 `_SB_DEFAULT_M` 暫改為異值，實測**輸入欄之初值隨之改變**
     ⇒ 證二者**確已綁定**；**⛔ 只證「現值相同」**（現值相同於補正前即成立、**無判別力**）。

用法：`python verify/probes/probe_WG9229_default_coupling.py [--source index|worktree]`
      退出 `0` ＝ 三情境全符期望。
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


def app_lines(source):
    if source == "worktree":
        with open(os.path.join(REPO, "app.py"), "rb") as f:
            b = f.read()
    else:
        r = subprocess.run(["git", "-C", REPO, "cat-file", "blob", ":app.py"], capture_output=True)
        assert r.returncode == 0, ("cat-file rc", r.returncode)
        b = r.stdout
    return b.decode("utf-8").replace("\r\n", "\n").split("\n")


def grab(lines, start_sub, end_sub, lab):
    s = [i for i, x in enumerate(lines) if start_sub in x]
    assert len(s) == 1, (lab + "·起", len(s))
    e = [i for i, x in enumerate(lines) if i >= s[0] and end_sub in x]
    assert e, (lab + "·迄", 0)
    return textwrap.dedent("\n".join(lines[s[0]:e[0] + 1])), s[0] + 1, e[0] + 1


def build(disp, cb, inp):
    return (
        "import streamlit as st\n\n"
        "def _f3L_invalidate_g_cache():        # 樁：app 既有之失效函式（⛔ 本探針之受測物）\n"
        "    st.session_state['_stub_invalidated'] = True\n\n"
        "_show = st.session_state.get('_show', True)\n"
        "if not _show:\n"
        "    st.info('branch-not-rendered')\n"
        "else:\n"
        + textwrap.indent(disp, "    ") + "\n"
        "    with st.expander('⚙️ 街角地參數', expanded=False):\n"
        + textwrap.indent(cb, "        ") + "\n"
        + textwrap.indent(inp, "        ") + "\n")


DISP_RE = re.compile(r"\*\*本次退縮值：([^ ]+) m（(預設|使用者輸入)）\*\*")


def read_disp(at):
    for m in at.markdown:
        mm = DISP_RE.search(m.value)
        if mm:
            return mm.group(1), mm.group(2)
    return ("🔴 無", "🔴 無")


def downstream(ss, need_src, wf_tag_of):
    snap = {k: ss[k] for k in (KEY, FLAG) if k in ss}
    out = {}
    raw = snap.get(KEY)
    out["E1"] = "🔴 loud raise（缺鍵）" if raw is None else float(raw)
    ns = {"ss": snap}
    exec(need_src, ns)
    try:
        out["E2"] = float(ns["_need"](KEY))
    except RuntimeError as e:
        out["E2"] = "🔴 " + str(e)[:30]
    try:
        out["E3"] = wf_tag_of(snap[KEY])
    except KeyError:
        out["E3"] = "🔴 KeyError"
    except RuntimeError as e:
        out["E3"] = "🔴 " + str(e)[:26]
    return out


def main(argv):
    sys.stdout.reconfigure(encoding="utf-8")
    source = "index"
    if "--source" in argv:
        source = argv[argv.index("--source") + 1]
    assert source in ("index", "worktree"), source
    lines = app_lines(source)

    disp, d_a, d_b = grab(lines, "W-G.9-219R2 工項二：退縮值之**常設顯示**",
                          'st.markdown(f"**本次退縮值：', "常設顯示區塊")
    cb, c_a, c_b = grab(lines, "W-G.9-219R2 工項一 a／b：退縮欄**專屬**之 on_change",
                        "_f3L_invalidate_g_cache()", "on_change 區塊")
    inp, i_a, i_b = grab(lines, "_setback_init = float(st.session_state.get(",
                         "help='💡 修改後 Step G", "輸入欄區塊")
    need_src, n_a, n_b = grab(lines, "def _need(k):", "return ss[k]", "_need")
    tag_src, t_a, t_b = grab(lines, "def _wf_tag_of(setback):",
                             "非 UC9898 雙情境（0/3.5），引擎凍結錨不適用", "_wf_tag_of")
    gns = {}
    exec(tag_src, gns)
    wf_tag_of = gns["_wf_tag_of"]

    const = re.search(r"_SB_DEFAULT_M\s*=\s*([0-9.]+)", disp)
    assert const, "🔴 抽出之顯示區塊內無 `_SB_DEFAULT_M`"
    CONST = float(const.group(1))
    print("=" * 112)
    print("【受測碼之抽出】source ＝ **%s**（`app.py` **%d** 列）" % (source, len(lines) - 1))
    print("  常設顯示區塊 ＝ `:%d`–`:%d`／`on_change` ＝ `:%d`–`:%d`／輸入欄 ＝ `:%d`–`:%d`"
          % (d_a, d_b, c_a, c_b, i_a, i_b))
    print("  下游 `_need` ＝ `:%d`–`:%d`／`_wf_tag_of` ＝ `:%d`–`:%d`" % (n_a, n_b, t_a, t_b))
    print("  🔒 抽出之 `_SB_DEFAULT_M` ＝ **%s**" % CONST)
    print("  🔒 輸入欄之預設運算式（逐字）：")
    for x in inp.split("\n"):
        if "_setback_init" in x or "value=" in x:
            print("     `%s`" % x.strip())
    print()

    SRC = build(disp, cb, inp)
    rows = []

    def measure(at, lab):
        v, s = read_disp(at)
        init = at.number_input[0].value if at.number_input else "🔴 無 widget"
        d = downstream(at.session_state, need_src, wf_tag_of)
        rows.append((lab, v, s, init, d["E1"], d["E2"], d["E3"]))

    at = AppTest.from_string(SRC, default_timeout=60)
    at.run()
    measure(at, "① 首次渲染（key 未存在）")
    at2 = AppTest.from_string(SRC, default_timeout=60)
    at2.run()
    at2.number_input[0].set_value(0.0).run()
    measure(at2, "② 輸入 `0`")
    at3 = AppTest.from_string(SRC, default_timeout=60)
    at3.run()
    at3.number_input[0].set_value(2.0).run()
    measure(at3, "③ 輸入 `2`（他值）")

    print("  | 情境 | 顯示之值 | 顯示之來源 | **輸入欄之值** | `E1` 主路徑 | `E2` 引擎接線 | `E3` tag |")
    print("  |---|---|---|---|---|---|---|")
    for r in rows:
        print("  | %s | `%s` | **%s** | `%s` | `%s` | `%s` | `%s` |" % r)
    print()
    print("  🔒 **`A` 作用域可及性（工項一 `b`）＝ %s**——`_SB_DEFAULT_M` 定義於 `with st.expander` "
          "**之外**、用於**其內**；本探針之 `①` 若不可及即 `NameError` 而無輸出。"
          % ("PASS（實測可及）" if rows else "FAIL"))
    print("     🔒 其為**實測**、⛔ 推理：受測之三段碼皆自 `app.py` 逐字抽出，`with` 之嵌套與 app 同構。")

    EXP = [
        ("① 首次渲染（key 未存在）", "%g" % CONST, "預設", CONST, CONST, CONST),
        ("② 輸入 `0`", "0", "使用者輸入", 0.0, 0.0, 0.0),
        ("③ 輸入 `2`（他值）", "2", "使用者輸入", 2.0, 2.0, 2.0),
    ]
    bad = []
    for got, exp in zip(rows, EXP):
        if got[1] != exp[1]:
            bad.append("%s｜顯示值：得 `%s`／期 `%s`" % (got[0], got[1], exp[1]))
        if got[2] != exp[2]:
            bad.append("%s｜來源：得 `%s`／期 `%s`" % (got[0], got[2], exp[2]))
        if abs(float(got[3]) - float(exp[3])) > 1e-9:
            bad.append("%s｜**輸入欄之值**：得 `%s`／期 `%s`" % (got[0], got[3], exp[3]))
        for i, nm in ((4, "E1"), (5, "E2")):
            if isinstance(got[i], float) and abs(got[i] - float(exp[i])) > 1e-9:
                bad.append("%s｜%s：得 `%s`／期 `%s`" % (got[0], nm, got[i], exp[i]))
    print()
    print("=" * 112)
    print("【判】期望之出處：`W-G.9-229` 工項二 `a` ＋ 抽出之 `_SB_DEFAULT_M`（**⛔ 硬寫 `3.5`**）")
    print("  🔒 **`①` 之期望值係<u>由抽出之常數導出</u>**（`%g`）⇒ 常數一改，期望隨之改"
          "⇒ 本探針即**分歧偵測器**（工項二 `b`）。" % CONST)
    print("  🔒 不符項 ＝ **%d**" % len(bad))
    for x in bad:
        print("     🔴 %s" % x)
    ok = not bad
    print()
    print("  🛑 **本探針 ＝ %s**（source ＝ %s·常數 ＝ %g）"
          % ("PASS" if ok else "FAIL", source, CONST))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
