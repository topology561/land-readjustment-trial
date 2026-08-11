# -*- coding: utf-8 -*-
r"""`W-G.9-8`／`W-G.9-9`：三支**真 app 路徑端到端複本**之**終止點**守護夾具。

## 受詞（🔒 ⛔ 逐字採考古 65 第四層——⛔ **不是**「三支跑不跑得通」）

> 守護閘之判準 **⛔ 不可寫成「該功能是否成功」**（在有既有另案時恆假、閘永紅而失義），
> 須寫成**受詞本身之命題**。

⇒ 受詞 ＝ **「三支之 `raise` 點 ＋ 例外型別 ＋ 例外訊息，與凍存者相符」**
（`W-G.9-9` 起**已去呈現層**·見下「投影」）。

**為何**：`verify/wg_g1_smoke.py`／`wg_g2_smoke.py`／`wg_g3.py` 皆為
「app `_build_wf_ctx` → `wf_f0`→`f4` 全鏈」之端到端複本（其中 `wg_g3.py` 係
`CLAUDE.md` 所訂 **W-G 收官判準 ①** 之終驗工具），惟**三支皆不在任何自動流程內**
（`W-G.9-6` §6）。若以 `rc=0` 為判準掛入，將新增**三個永紅項** ＝ 把
`W-G.9-6`／`W-G.9-7` 剛修好的病**再造一次**。

## 🔒 投影（`W-G.9-9`）——**投影 ≠ 正規化，⛔ 不得混同**

| | 正規化（`R1`／`R2`·`wv_reconcile`） | **投影**（本檔 `_project`） |
|---|---|---|
| 作用 | 兩端**變形後**比對 | **縮小受詞**——明確放棄某些內容 |
| 風險 | 產生**看不見**之盲點 | 放棄之內容**永不比對** |
| 聲明 | 「這條會讓我看不見什麼」 | **「本投影放棄了什麼」**（見下） |

**定義**：取 traceback 之**最後一個 `File "…", line N, in <func>` 幀**（＝`raise` 點）
＋ 其後**自末端往回連續之無縮排行**（＝例外型別＋訊息）。
**套用序**：**先投影、後正規化**；`R1`／`R2` 照舊套用於投影後之 `File` token
——⛔ **本檔未新增任何正規化規則**。

### 🔴 本投影放棄了什麼（⛔ 逐條·**永不比對**）

| # | 放棄 | 後果 |
|---|---|---|
| 1 | `Traceback (most recent call last):` 標題行 | 該行措辭改變不再致紅 |
| 2 | **上游各幀**之 `File` 行（`wg_g1_smoke.py:101`／`:58` 等） | **呼叫鏈形狀改變不再致紅**（只要 `raise` 點不變） |
| 3 | 各幀之**原始碼列** | 呼叫處寫法（換行、參數重排）改變不再致紅 |
| 4 | **錯誤位置標記行**（`~~~~^^`／`^^^^`） | 直譯器標記樣式改變不再致紅 |
| 5 | **摺疊標記**（`...<N lines>...`） | 摺疊行數改變不再致紅 |
| 6 | **`rc` 值** | ⚠️ 單看 `rc` 不再致紅——惟 `rc=0` 幾必伴隨「無幀、無例外行」⇒ 投影變 `["(無 traceback 幀)"]` ⇒ **仍紅** |
| 7 | **stdout**（`W-G.9-8` 已放棄·本批延續） | 進度輸出之任何變動不再致紅 |
| 8 | traceback 之**中段空行** | 無實質後果 |

### 🔴 這份凍存綁死了什麼環境（⛔ 逐項·不得留空）

| # | 綁死 | 說明／緩解 |
|---|---|---|
| 1 | **`raise` 所在檔之行號**（`stepg_pipeline.py` 之 `line N`） | **刻意保留**：raise 換位置須被看見 ⇒ 落**類 II**、由人具名確認 |
| 2 | **例外訊息中之一切數值**（`理論@k*`／`實跑`／`Δ`） | 綁死當前之 CAD／地籍資料／快照；資料一變即**類 III**——**這是要的** |
| 3 | **例外型別名**（`RuntimeError`） | 型別改變即紅 |
| 4 | **語系與編碼**（正體中文＋emoji） | 擷取須 `PYTHONIOENCODING=utf-8`（本檔已設）；⛔ 非 UTF-8 環境擷取會失真 |
| 5 | **「最後一幀即 raise 點」之格式假設** | 若直譯器改變幀序／加註尾幀，受詞會位移 ⇒ 落類 III（loud、非靜默） |
| 6 | **「例外塊 ＝ 尾端連續無縮排行」之格式假設** | ⚠️ 若環境於 traceback **之後**再印無縮排警告（如關閉期 `ResourceWarning`），該行**會被納入**受詞 ⇒ 致紅。**已知耦合·本批不處理** |
| 7 | **檔案路徑之倉相對形式** | 由 `R1`／`R2` 保證 ⇒ **不**綁工作樹之絕對位置 |
| 8 | **直譯器之 traceback 呈現層**（標記行／摺疊） | 🔒 **`W-G.9-9` 之投影已解除此耦合** |

## 🔴 本夾具**轉紅之因**（⛔ 逐項列舉·非單一）

1. **`raise` 點改變**——檔名或函式名不同 ⇒ **類 III**；⚠️ 僅**行號**不同 ⇒ **類 II**（須人具名確認）。
2. **例外型別改變**（如 `RuntimeError` → 他型）⇒ 類 III。
3. **例外訊息改變**——含其中之**任何數值**（幾何／資料／快照一變即中）⇒ 類 III。
4. **某支不再拋例外**（結構閘另案修好、跑得更遠或跑通）⇒ 投影變 `["(無 traceback 幀)"]` ⇒ 類 III。
   🔒 **此即設計意圖：特性，不是缺陷。**⛔ 屆時不得逕自重凍了事，須先確認「跑得更遠」確為預期。
5. **腳本不存在**（被改名／刪除）⇒ 紅。
6. **凍存檔不存在或解析出 0 筆** ⇒ 紅（⛔ 空集合不得算通過）。
7. **名目集合改變**（三支之檔名清單變動）⇒ 紅。
8. ⚠️ **環境耦合 6 之副作用**（traceback 後之無縮排警告）⇒ 紅（已知、非本閘所欲守）。

⇒ ⛔ **不再致紅者**：呈現層 token（標記行／摺疊）、上游幀、原始碼列、`rc`、stdout。

## 沿用（⛔ 不另寫第二套正規化·`#20` 族）

`normalize`／`classify`／`report`／`render_list`／`parse_list` **一律取自**
`verify/wv_reconcile.py`。⚠️ 凍存檔沿用該格式，故每筆以 `🔴 FAIL  <腳本名>` 起頭
——**此處該標記之義為「終止記錄」**，⛔ 非「該腳本是一道失敗之閘」。

## 重跑
    python verify/fixture_e2e_termination.py                       # rc=0 ⇒ 綠
    python verify/fixture_e2e_termination.py --freeze              # 途徑乙：重跑三支後投影
    python verify/fixture_e2e_termination.py --project <舊凍存> <輸出>  # 途徑甲：投影既有凍存
"""
import os
import re
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import wv_reconcile as WR                                    # noqa: E402

SCRIPTS = ("wg_g1_smoke.py", "wg_g2_smoke.py", "wg_g3.py")
FROZEN = os.path.join(HERE, "out", "WG99_端到端複本_終止點凍存_投影.txt")
FRAME = re.compile(r'^\s+File "(?P<f>[^"]*)", line (?P<n>\d+), in (?P<fn>.*)$')
RC = [0]


def red(msg):
    print(f"  🔴 {msg}")
    RC[0] = 1


# ══════════════════════════════════════════════════════════════════════════
# 投影（`W-G.9-9`·定義與 `docs/reports/W-G.9-9_前置登記.md` §1 逐字相符）
# ══════════════════════════════════════════════════════════════════════════
def _project(lines):
    """縮小受詞：最後一個 `File` 幀（raise 點）＋ 尾端連續之無縮排行（例外型別＋訊息）。

    ⛔ **非正規化**——被放棄之內容**永不比對**（放棄清單見本檔 docstring）。
    """
    frames = [i for i, l in enumerate(lines) if FRAME.match(l)]
    if frames:
        i = frames[-1]
        head = [lines[i].strip()]
        tail = lines[i + 1:]
    else:
        head = ["(無 traceback 幀)"]          # ⛔ loud·非靜默 fallback
        tail = lines
    exc = []
    for l in reversed(tail):
        if (not l.strip()) or l[:1].isspace():
            break
        exc.insert(0, l.rstrip())
    return head + exc


def _record(lines):
    """投影 → 正規化（⛔ 序不可倒；`R1`／`R2` 取自 `wv_reconcile`）。"""
    return [WR.normalize(x) for x in _project(lines)]


def observe():
    """實跑三支，回 [(腳本名, 投影後之終止記錄)]。⛔ 不吞例外：stderr 全入投影輸入。"""
    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    items = []
    for s in SCRIPTS:
        p = os.path.join(HERE, s)
        if not os.path.exists(p):
            red(f"腳本不存在：{s} ⇒ ⛔ 不得視為通過")
            items.append((s, ["(腳本不存在)"]))
            continue
        r = subprocess.run([sys.executable, p], capture_output=True, text=True,
                           encoding="utf-8", env=env, timeout=1800)
        items.append((s, _record([x.rstrip() for x in (r.stderr or "").splitlines()])))
    return items


def _write(items, path, src):
    body = WR.render_list(items, src, "（見檔頭之本體雜湊）",
                          batch="W-G.9-9 端到端複本終止點·投影後")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(body)
    # 🔒 考古 68 修法 ①／考古 67 修法 ④：寫後以獨立途徑驗其落地
    assert os.path.exists(path), "🔴 凍存檔未建立"
    back = WR.parse_list(open(path, encoding="utf-8").read())
    assert len(back) == len(items), f"🔴 反讀 {len(back)} 筆 ≠ 寫入 {len(items)} 筆"
    assert back == items, "🔴 反讀內容 ≠ 寫入內容"
    return path


def freeze():
    """途徑乙：重跑三支 → 投影 → 凍存。"""
    items = observe()
    _write(items, FROZEN, "（實跑 verify/wg_g1_smoke.py 等三支之 stderr → 投影）")
    print(f"✅ 已凍存（途徑乙·重跑後投影）：{os.path.relpath(FROZEN, REPO)}（{len(items)} 支）")
    for nm, det in items:
        for x in det:
            print(f"   {nm:<20} | {x[:110]}")
    return 0


def project_existing(src, dst):
    """途徑甲：由**既有凍存**投影而得（純文字·⛔ 不重跑）。"""
    old = WR.parse_list(open(src, encoding="utf-8").read())
    assert old, f"🔴 來源解析出 0 筆：{src}"
    items = [(nm, _record(det)) for nm, det in old]
    _write(items, dst, f"（投影自 {os.path.relpath(src, REPO).replace(chr(92), '/')}·⛔ 未重跑）")
    print(f"✅ 已產出（途徑甲·投影既有凍存）：{os.path.relpath(dst, REPO)}（{len(items)} 支）")
    return 0


def main():
    print("=" * 92)
    print("# `W-G.9-8`／`W-G.9-9` 夾具：三支端到端複本之**終止點**（⛔ 受詞非「跑不跑得通」）")
    print("=" * 92)
    if not os.path.exists(FROZEN):
        red(f"凍存不存在（{os.path.relpath(FROZEN, REPO)}）⇒ ⛔ 不得視為通過")
        return RC[0]
    frozen = WR.parse_list(open(FROZEN, encoding="utf-8").read())
    if not frozen:
        red("凍存解析出 0 筆 ⇒ ⛔ 空集合不得算通過")
        return RC[0]
    print(f"  凍存 ＝ {os.path.relpath(FROZEN, REPO)}（{len(frozen)} 支·**投影後**）")
    print("  ⚠️ 受詞 ＝ `raise` 幀 ＋ 例外型別＋訊息；⛔ 呈現層／上游幀／原始碼列／`rc`／stdout **永不比對**")
    print("  ⚠️ `raise` 之**行號**仍在受詞內 ⇒ raise 換位置落**類 II**、須人具名確認")

    cur = observe()
    rc0, L = WR.report(WR.classify(frozen, cur), "端到端複本終止點·投影後")
    for x in L:
        print(x)
    if rc0:
        red("終止點／終止原因與凍存不符 ⇒ ⛔ 不得逕自重凍（見 docstring「轉紅之因」第 4 項）")

    # ── 竄改自檢（⛔ 兩態皆印）────────────────────────────────────────────
    #   🔒 受詞 ＝ **投影後之終止記錄**——三支皆終止於此、該記錄即本夾具所比對之物
    #      ⇒ **現查證明必被執行**（⛔ 非「不保證執行到之點」·考古 65 第五層）。
    #   竄改 ＝ 把 `raise` 幀換成**更早階段**之幀（終止點提前）。
    print()
    print("─" * 92)
    print("【竄改自檢】人造「終止點提前」⇒ 必轉紅；還原 ⇒ 轉綠（⛔ 兩態皆印）")
    print("─" * 92)
    victim = cur[0][0]
    early = [(victim, ['File "verify/wg_g1_smoke.py", line 58, in main',
                       "RuntimeError: （合成）於更早階段即終止——W-G.9-9 竄改自檢"])] + cur[1:]
    r_t, _ = WR.report(WR.classify(frozen, early), "竄改態")
    r_r, _ = WR.report(WR.classify(frozen, cur), "還原態")
    print(f"  竄改態（`{victim}` 之 raise 幀改為 `wg_g1_smoke.py:58`）⇒ {'🔴 紅' if r_t else '✅ 綠'}")
    print(f"  還原態                                              ⇒ {'🔴 紅' if r_r else '✅ 綠'}")
    if r_t and not r_r:
        print("  ✅ 竄改自檢具鑑別力（竄改態紅 ∧ 還原態綠）")
    elif r_t and r_r:
        t3 = {n for n, _ in WR.classify(frozen, early)["III"]}
        r3 = {n for n, _ in WR.classify(frozen, cur)["III"]}
        if victim in t3 - r3:
            print(f"  ✅ 具**相對**鑑別力（`{victim}` 因竄改而新出現於類 III）")
        else:
            red("竄改自檢**無鑑別力** ⇒ 本夾具不得計入交付")
    else:
        red("竄改態未轉紅 ⇒ 竄改自檢**無鑑別力** ⇒ 本夾具不得計入交付")

    print()
    print("=" * 92)
    print(f"{'✅ 夾具 PASS' if RC[0] == 0 else '🔴 夾具 FAIL'}（rc={RC[0]}）")
    print("=" * 92)
    return RC[0]


if __name__ == "__main__":
    if "--project" in sys.argv:
        i = sys.argv.index("--project")
        sys.exit(project_existing(sys.argv[i + 1], sys.argv[i + 2]))
    sys.exit(freeze() if "--freeze" in sys.argv else main())
