# -*- coding: utf-8 -*-
"""`W-G.9-248` 工項三之 `V-4` 合成案：混型欄之 Arrow 轉換。

🛑 **本檔⛔ 生產碼**（`verify/probes/`）·⛔ 被 `run_all`／`run_verification` 消費。
🔒 **受詞之態 ＝ `verify/W-G.9-248-c1`**（含 `c1`／`c2`）。於**未含該二 commit 之態**
   （如主線 `6010a80`）跑必 **loud 失敗**並具名——**此為預期**，⛔ 缺陷。

🔑 **本器⛔ 取代單 `V-4` 所令之「拋棄式實跑」**——實跑須操作 UI 至該三頁面，
   屬 `V-K`（KL 目檢）之射程。本器所證者為**型別層**：
   ① 修後之三表皆可通過 `pyarrow` 轉換（`ArrowInvalid` 不再發生）；
   ② **判別力**：還原任一欄之混型 ⇒ **必重現 `ArrowInvalid`**（證本器⛔ 恆綠）；
   ③ 哨兵 `'—'`／`'-'` 之語意於修後**仍可辨**（欄值傾印為證）。

跑法：`python verify/probes/probe_wg9248_arrow_mixed.py`（`PYTHONIOENCODING=utf-8`）。
"""
import ast
import os
import sys

import pandas as pd
import pyarrow

_HERE = os.path.dirname(os.path.abspath(__file__))
_APP = os.path.join(_HERE, os.pardir, os.pardir, "app.py")


def _load_helper():
    """自 `app.py` **AST 抽取** `wg9248_stringify_mixed_cols` 並 exec。

    ⛔ import／exec 整個 `app.py`（其為 Streamlit 腳本·會再入）。
    🔒 找不到 ⇒ **loud `SystemExit`** 並具名（`no-silent-fallback`）。
    """
    with open(_APP, "rb") as f:
        src = f.read().replace(b"\r\n", b"\n").decode("utf-8")
    tree = ast.parse(src)
    for n in ast.walk(tree):
        if isinstance(n, ast.FunctionDef) and n.name == "wg9248_stringify_mixed_cols":
            seg = ast.get_source_segment(src, n)
            ns = {}
            exec(compile(seg, "<app.py:wg9248_stringify_mixed_cols>", "exec"), ns)
            return ns["wg9248_stringify_mixed_cols"], len(seg.encode("utf-8"))
    raise SystemExit(
        "🔴 `wg9248_stringify_mixed_cols` 不在 `app.py` 中 ⇒ 本器之受詞不存在。\n"
        "   本器之受詞態 ＝ `verify/W-G.9-248-c1`（含 c1／c2）；\n"
        "   於未含該二 commit 之態跑，本失敗係**預期**、⛔ 缺陷。"
    )


def _arrow_ok(df):
    """試 `pyarrow` 轉換；回 `(成功?, 例外之型別名, 訊息首行)`。"""
    try:
        pyarrow.Table.from_pandas(df)
        return True, "", ""
    except Exception as e:                                   # noqa: BLE001
        return False, type(e).__name__, str(e).splitlines()[0][:110]


# ── 三表之**代表性**資料（逐欄依碼面之二臂構造·⛔ 臆造欄名）────────────────
DF1_ROWS = [   # `_corner_rows_init`：有左無右 ／ 有右無左 ／ 兩側皆有
    {'街廓': 'R1', '分類': '住宅區', '正面路寬(m)': 8.0,
     '【左】路寬(m)': 8.0, '【右】路寬(m)': '—',
     '街廓分配深度(m)': 33.15, '法定最小寬(m)': 3.5, '法定最小深(m)': 14.0,
     '【左】截角(㎡)': 12.5, '【右】截角(㎡)': '—',
     '【左】街角最小面積(㎡)': 225.24, '【右】街角最小面積(㎡)': None},
    {'街廓': 'R4', '分類': '住宅區', '正面路寬(m)': 8.0,
     '【左】路寬(m)': '—', '【右】路寬(m)': 12.0,
     '街廓分配深度(m)': 33.10, '法定最小寬(m)': 3.5, '法定最小深(m)': 14.0,
     '【左】截角(㎡)': '—', '【右】截角(㎡)': 18.0,
     '【左】街角最小面積(㎡)': None, '【右】街角最小面積(㎡)': 116.08},
]
DF1_COLS = ['【左】路寬(m)', '【右】路寬(m)', '【左】截角(㎡)', '【右】截角(㎡)']

DF2_ROWS = [   # `_corner_select_results`：一側「無此側」 ／ 兩側皆有
    {'街廓': 'R1', '演算法': 'V13', '候選來源': '🤖 自動 PK', '候選數': 5,
     '【左】最小面積(㎡)': '225.24', '【右】最小面積(㎡)': '無此側',
     '【左】達資格候選': 3, '【左】第1宗指配': 'A（628-1）[T-01]', '【左】優先權指數': 0.6712,
     '【右】達資格候選': '—', '【右】第1宗指配': '無此側', '【右】優先權指數': '—'},
    {'街廓': 'R5', '演算法': 'V13', '候選來源': '🎯 使用者標記', '候選數': 8,
     '【左】最小面積(㎡)': '146.50', '【右】最小面積(㎡)': '188.30',
     '【左】達資格候選': 2, '【左】第1宗指配': '⚠️ 強制抵費地', '【左】優先權指數': '—',
     '【右】達資格候選': 4, '【右】第1宗指配': 'B（628-9）[T-11]', '【右】優先權指數': 0.3301},
    # 🔒 **左無右有**之列——⛔ 可省：無此列則 `【左】達資格候選` 於本靶**恆為 int**，
    #    其「還原混型須失敗」之判別力必偽綠、「哨兵可辨」必偽紅（**靶之誤**·⛔ 受詞紅）。
    #    ⇒ **靶須使<u>每一個</u>受詞欄皆實際混型**（同族 ＝ `W-G.9-246R2` 交接文陷阱 `7`）。
    {'街廓': 'R6', '演算法': 'V13', '候選來源': '🤖 自動 PK', '候選數': 6,
     '【左】最小面積(㎡)': '無此側', '【右】最小面積(㎡)': '203.11',
     '【左】達資格候選': '—', '【左】第1宗指配': '無此側', '【左】優先權指數': '—',
     '【右】達資格候選': 5, '【右】第1宗指配': 'C（628-20）[T-31]', '【右】優先權指數': 0.5124},
]
DF2_COLS = ['【左】達資格候選', '【右】達資格候選', '【左】優先權指數', '【右】優先權指數']

DF3_ROWS_FIXED = [   # `cash_flow_data`：**修後**（合計列之哨兵 ＝ None）
    {'年度': '第1年', '工程費': 100.0, '重劃費用': 20.0, '支出小計': 120.0,
     '收入': 0.0, '當期淨現金流量': -120.0, '期初淨額': 0.0,
     '貸款利息': 1.2, '期末餘額': -121.2},
    {'年度': '合計', '工程費': 100.0, '重劃費用': 20.0, '支出小計': 120.0,
     '收入': 500.0, '當期淨現金流量': 380.0, '期初淨額': None,
     '貸款利息': 1.2, '期末餘額': 378.8},
]
DF3_ROWS_OLD = [dict(r) for r in DF3_ROWS_FIXED]
DF3_ROWS_OLD[1]['期初淨額'] = "-"        # 還原為改前之字串哨兵


def main():
    fn, nbytes = _load_helper()
    print("🔒 已自 `app.py` AST 抽取 `wg9248_stringify_mixed_cols`（%d B）" % nbytes)
    print("   pandas %s ／ pyarrow %s" % (pd.__version__, pyarrow.__version__))
    ok_all = True

    # ── DF-1／DF-2：`.astype(str)` 之修 ───────────────────────────────
    for tag, rows, cols in (("DF-1 `_corner_rows_init`", DF1_ROWS, DF1_COLS),
                            ("DF-2 `_corner_select_results`", DF2_ROWS, DF2_COLS)):
        print("\n" + "=" * 72)
        print("=== %s ===" % tag)
        # 🔑 **靶自檢（⛔ 可省）**：每一受詞欄須**實際混型**（數值 ∪ 字串哨兵），
        #    否則其「還原混型須失敗」之判別力**必偽綠**、「哨兵可辨」**必偽紅**
        #    ——係**靶之誤**、⛔ 受詞紅。本檢係本器自身之量測器自證。
        _bad = []
        for _c in cols:
            _vals = [r[_c] for r in rows]
            _num = any(isinstance(v, (int, float)) and not isinstance(v, bool) for v in _vals)
            _str = any(isinstance(v, str) for v in _vals)
            if not (_num and _str):
                _bad.append(_c)
        print("  ⓪ 靶自檢（每一受詞欄須實際混型）: %s"
              % ("✅ %d 欄皆混型" % len(cols) if not _bad
                 else "🔴 %r ⛔ 混型 ⇒ **靶之誤**" % _bad))
        ok_all &= (not _bad)
        raw = pd.DataFrame(rows)
        ok0, ex0, m0 = _arrow_ok(raw)
        print("  ① 改前（原樣）        Arrow 轉換: %s  %s %s"
              % ("✅ 成功" if ok0 else "🔴 失敗", ex0, m0))
        fixed = fn(raw, cols)
        ok1, ex1, m1 = _arrow_ok(fixed)
        print("  ② 改後（helper 施用）  Arrow 轉換: %s  %s %s"
              % ("✅ 成功" if ok1 else "🔴 失敗", ex1, m1))
        # 判別力：還原**任一**欄之混型 ⇒ 須重現失敗
        part = fn(raw, [c for c in cols if c != cols[0]])
        ok2, ex2, _ = _arrow_ok(part)
        print("  ③ 判別力（還原 `%s` 一欄之混型）: %s %s（須失敗）"
              % (cols[0], "🔴 竟成功" if ok2 else "✅ 失敗", ex2))
        # 哨兵語意仍可辨
        print("  ④ 哨兵語意（修後之欄值傾印）:")
        for c in cols:
            print("       %-16s %s" % (c, list(fixed[c])))
        _sent_ok = all(any(v == '—' for v in fixed[c]) for c in cols)
        print("     `'—'` 於修後之四欄皆仍可辨: %s" % ("✅" if _sent_ok else "🔴"))
        ok_all &= (not ok0) and ok1 and (not ok2) and _sent_ok

    # ── DF-3：`None` ＋ `na_rep` 之修 ────────────────────────────────
    print("\n" + "=" * 72)
    print("=== DF-3 `cash_flow_data` ===")
    old = pd.DataFrame(DF3_ROWS_OLD)
    ok0, ex0, m0 = _arrow_ok(old)
    print("  ① 改前（哨兵 ＝ `\"-\"`）  Arrow 轉換: %s  %s %s"
          % ("✅ 成功" if ok0 else "🔴 失敗", ex0, m0))
    new = pd.DataFrame(DF3_ROWS_FIXED)
    ok1, ex1, m1 = _arrow_ok(new)
    print("  ② 改後（哨兵 ＝ `None`）  Arrow 轉換: %s  %s %s"
          % ("✅ 成功" if ok1 else "🔴 失敗", ex1, m1))
    print("  ③ `期初淨額` 之 dtype: 改前 %s ／ 改後 %s"
          % (old['期初淨額'].dtype, new['期初淨額'].dtype))
    # 語意：`None` 經 .style.format(na_rep="-") 顯示為 `-`
    _rendered = new.style.format({"期初淨額": "{:,.2f}"}, na_rep="-").to_html()
    _has_dash = ">-<" in _rendered.replace(" ", "")
    print("  ④ 語意保留（`.style.format(..., na_rep=\"-\")` 之渲染含 `-`）: %s"
          % ("✅" if _has_dash else "🔴"))
    ok_all &= (not ok0) and ok1 and _has_dash

    print("\n" + "=" * 72)
    print("🟢 V-4（型別層）全綠" if ok_all else "🔴 V-4 有紅")
    print("🛑 **界限（照實·⛔ 頂替）**：本器所證者為**型別層**；")
    print("   單 `V-4` 所令之「拋棄式實跑·`stdout` 之 `ArrowInvalid` 命中 0」")
    print("   須操作 UI 至該三頁面 ⇒ 屬 `V-K`（KL 目檢）之射程。")
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main())
