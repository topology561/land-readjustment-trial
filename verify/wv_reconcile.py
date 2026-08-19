# -*- coding: utf-8 -*-
r"""`W-G.9-7`：期望 FAIL 對帳器——**名目 ＋ 失敗原因**（KL 2026-08-11 裁）。

## 授權與其範圍

> **KL 2026-08-11**：同意把驗收核對方式改成「**名稱＋原因一併比對**」＝**是**。

⇒ 取代舊準則（**正典·權威序第 2 級**·`CLAUDE.md:71-72`：「逐項**名目**相同·⛔ 非計數」）
之**比較內容**；⛔ 不改「非全綠即紅」以外之任何驗收語意。

## 為何舊準則不夠（`W-G.9-6` 實證）

同一名目 `v3·StepG0m`，入單時之原因為 `①' 覆蓋閘破 12.0568㎡`、
現況為 `結構閘 理論＝實跑 破 Δ=2.837`——**根因整個換掉**，而只比名目之對帳**仍為綠**。
⇒ 22 名目中 **4 項**已發生此情形（`verify/out/probe_WG96_reconcile.log`）。

## 三分類（🔒 ⛔ 不得化約為二分類）

| 類 | 定義 | 處置 |
|---|---|---|
| **類 I** | 套正規化規則後**逐字相同** | 自動視為同 |
| **類 II** | 正規化後仍異，且**全部差異皆落於 traceback 行號** | 🔴 **⛔ 不自動視為同**——須**逐項具名確認**（「上方插入行位移」／「raise 換了位置」） |
| **類 III** | 其餘（訊息**實質**不同） | **紅** |

**案由**：行號位移**既可能**無害（`W-G.9-4b` 之 `stepg_pipeline.py 1357→1362`）、
**也可能**是 raise 換了位置（＝真原因改變）。⛔ 二者不可由工具代判。

🔒 **類 II 之偵測器 ≠ 正規化規則**：偵測時所用之「行號抹除」**僅供分類**，
⛔ **不寫入名單、不改變所存之原因全文**（施工單 §3 明文禁止把行號寫進正規化規則）。

## 正規化規則（⛔ 事前登記已封·`docs/reports/W-G.9-7_前置登記.md` §2·事後不得增列）

作用域**皆限於 traceback 之 `File "…"` 引號內之路徑 token**，⛔ 不及於訊息其他部分。

| # | 規則 | 🔴 這條會讓我看不見什麼 |
|---|---|---|
| **R1** | `File "…"` 內 `\` → `/` | 看不見「路徑分隔符本身改變」⇒ 無法分辨 log 產於 Windows 或 POSIX |
| **R2** | `File "…"` 內絕對前綴 → 倉相對 | 看不見「這份 log 產於哪個工作樹／哪個倉」⇒ **誤用他倉基準無法由對帳發現**（前例：`W-G.9-4b` `E4` 之基準產於 `k6a2-d2b21-wiring-6ef500`）。**補償**：名單檔頭載來源 log 之倉相對路徑與 `git hash-object` |

## 用法

    python verify/wv_reconcile.py <log> <名單>          # 對帳（rc=0 綠／1 紅）
    python verify/wv_reconcile.py --freeze <log> <輸出名單>   # 由 log 產生新名單

於 `run_all` 內則由 `reconcile_text()` **自動**呼叫（⛔ 不另需人工執行）。
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)

_FAIL = re.compile(r"^\s*🔴 FAIL\s\s(.*?)\s*$")
_JUDGE = re.compile(r"^\s*(✅ PASS|🔴 FAIL)\s\s")
_SEP = re.compile(r"^\s*={10,}\s*$")          # results 迴圈之收尾分隔線 ⇒ 明細段結束
_LIST_DET = re.compile(r"^\s{4}\|\s?(.*)$")
_FILE_TOKEN = re.compile(r'File "([^"]*)"')
_LINENO = re.compile(r'(, line )\d+')


# ══════════════════════════════════════════════════════════════════════════
# 正規化規則（⛔ 清單已封）
# ══════════════════════════════════════════════════════════════════════════
def _r1(s):
    """R1：`File "…"` 內 `\\` → `/`。"""
    return _FILE_TOKEN.sub(lambda m: 'File "%s"' % m.group(1).replace("\\", "/"), s)


def _r2(s):
    """R2：`File "…"` 內絕對前綴 → 倉相對（截至 `verify/` 或 `app.py`）。"""
    return _FILE_TOKEN.sub(
        lambda m: 'File "%s"' % re.sub(r'^.*?(?=verify/|app\.py)', '', m.group(1)), s)


RULES = (("R1", "File \"…\" 內 \\ → /", _r1),
         ("R2", "File \"…\" 內絕對前綴 → 倉相對", _r2))


def normalize(s, rules=RULES):
    for _id, _desc, fn in rules:
        s = fn(s)
    return s


def _blind(s):
    """🔒 **類 II 之偵測器**（⛔ 非正規化規則·不入名單）：抹 traceback 行號。"""
    return _LINENO.sub(r"\1<行號>", s)


# ══════════════════════════════════════════════════════════════════════════
# 解析／輸出
# ══════════════════════════════════════════════════════════════════════════
def parse_log(text):
    """`run_all`／`run_verification` 輸出 → [(名目, [明細行])]（保序）。

    🔒 明細段止於**下一個判定行**或 `====` 分隔線。
    ⚠️ 無 `====` 停止條件者，末項會吸進 `RESULT:`／`W-V run_all:` 等尾段文字
    （`W-G.9-6` 之探針即如此，其末項明細行數因而灌水）。
    """
    out, cur = [], None
    for ln in text.replace("\r\n", "\n").split("\n"):
        m = _FAIL.match(ln)
        if m:
            cur = (m.group(1), [])
            out.append(cur)
            continue
        if _JUDGE.match(ln) or _SEP.match(ln):
            cur = None
            continue
        if cur is not None and ln.strip():
            cur[1].append(ln.rstrip())
    return out


def parse_list(text):
    out, cur = [], None
    for ln in text.replace("\r\n", "\n").split("\n"):
        if ln.startswith("#"):
            continue
        m = _FAIL.match(ln)
        if m:
            cur = (m.group(1), [])
            out.append(cur)
            continue
        d = _LIST_DET.match(ln)
        if d is not None and cur is not None:
            cur[1].append(d.group(1).rstrip())
    return out


_TB_LINE = re.compile(r'", line \d+, in ')


def assert_list_integrity(items, src_rel, src_text=None):
    """🆕 `W-G.9-71` B 組：**名單產生端**之完整性自檢（🔒 ⛔ **不置於比對路徑**）。

    🔒 **落點之由**：本函式只由 `render_list` 呼叫，而 `render_list` **只**由
      `main(argv)` 之 `--freeze` 分支呼叫；`run_all` 走 `reconcile_text` → `classify`
      ⇒ **本自檢在 `run_all` 路徑上不會被觸發**（施工單 B-3-3）。

    🔴 **受詞（⛔ 非「token 數相等」）**：凡明細行**具 traceback 行之形狀**
      （含 `", line <N>, in `）卻**不含 `File "`** ⇒ 該行係**被截斷之 traceback 行**
      ⇒ `_FILE_TOKEN` 匹配 0 次 ⇒ `R1`／`R2` **無從施力** ⇒ 其絕對路徑前綴永不被移除
      ⇒ 該行必落**類 III** 而恆紅，且**其殘存字串隨路徑長度而異** ⇒ **不可比對**。

    ⚠️ **為何⛔ 不用施工單原訂之「token 數 ＝ 來源 log 之 token 數」**（`W-G.9-71` §C）：
      實測**明細內** token 數 ＝ **凍存 8／來源 log 8**（相等）——`render_list` **未遺失
      任何 token**，截斷發生在**更上游**（`run_verification` 之 `traceback.format_exc()[-300:]`）
      ⇒ 該式**恆綠、永不會咬**。🔑 **一個從未紅過的自檢，跟一段註解證據力相同。**
      🔒 惟**仍併算**該二數並列於訊息中（供人核對），只是**⛔ 不以其為判準**。

    `src_text` 給定時另列來源 log 之同類行數（診斷用·⛔ 不入判準）。
    """
    bad = []
    for nm, det in items:
        for d in det:
            if _TB_LINE.search(d) and 'File "' not in d:
                bad.append((nm, d))
    if not bad:
        return
    n_tok = sum(len(_FILE_TOKEN.findall(d)) for _n, dd in items for d in dd)
    n_src = (sum(len(_FILE_TOKEN.findall(x)) for x in src_text.split("\n"))
             if src_text else None)
    det = "；".join(f"[{nm}] {d.strip()[:70]}" for nm, d in bad[:3])
    raise RuntimeError(
        f"🔴 名單完整性自檢破：**{len(bad)} 行**具 traceback 形狀（`\", line N, in `）"
        f"卻不含 `File \"` ⇒ 係**被截斷之 traceback 行** ⇒ `_FILE_TOKEN` 匹配 0 次 ⇒ "
        f"`R1`／`R2` 無從施力 ⇒ 該行恆紅且不可比對（`GB-86`）。"
        f"｜來源 log ＝ {src_rel}"
        f"｜明細內 `File \"` token：名單 {n_tok}"
        + (f"／來源 log 全檔 {n_src}" if n_src is not None else "")
        + f"｜受影響列（前 3）：{det}{'…' if len(bad) > 3 else ''}"
        f"｜🔒 修法 ＝ **修餵料**（令來源 log 不截斷 traceback），"
        f"⛔ **非**增列正規化規則（`W-G.9-7` §2 已封）。")


def render_list(items, src_rel, src_hash, batch="W-G.9-7", _src_text=None):
    # 🆕 `W-G.9-71` B 組：**生成期**之完整性自檢（⛔ 不在比對路徑上·見其 docstring）
    assert_list_integrity(items, src_rel, _src_text)
    L = [f"# {batch} 期望 FAIL 名單（**名目 ＋ 失敗原因**）",
         f"# 授權      ：KL 2026-08-11「名稱＋原因一併比對」＝是",
         f"# 來源 log  ：{src_rel}",
         f"# 來源 hash ：git hash-object ⇒ {src_hash}",
         f"# 正規化    ：R1 File \"…\" 內 \\→/；R2 File \"…\" 內絕對前綴→倉相對",
         f"#             ⛔ traceback 行號**未**正規化 ⇒ 其差異一律入**類 II**、由人具名確認",
         f"# 對帳器    ：verify/wv_reconcile.py（於 run_all 內自動執行）",
         f"# 計數指令  ：grep -c \"^🔴 FAIL\" <本檔>        ← ⛔ 非 `wc -l`",
         "# " + "-" * 75]
    for nm, det in items:
        L.append(f"🔴 FAIL  {nm}")
        for d in det:
            L.append(f"    | {d}")
    return "\n".join(L) + "\n"


# ══════════════════════════════════════════════════════════════════════════
# 對帳
# ══════════════════════════════════════════════════════════════════════════
def classify(frozen, current, rules=RULES):
    """回 dict：名目層 ＋ 三分類。⛔ 名目差異單獨成項（比原因更嚴重）。"""
    fn_, cn = [x[0] for x in frozen], [x[0] for x in current]
    fd = {k: v for k, v in frozen}
    cd = {k: v for k, v in current}
    res = {"名目_凍存": fn_, "名目_現況": cn,
           "名目_僅凍存有": [x for x in fn_ if x not in cd],
           "名目_僅現況有": [x for x in cn if x not in fd],
           "名目_序不同": (fn_ != cn and sorted(fn_) == sorted(cn)),
           "I": [], "I_raw同": [], "II": [], "III": []}
    for nm in fn_:
        if nm not in cd:
            continue
        a = [normalize(x, rules) for x in fd[nm]]
        b = [normalize(x, rules) for x in cd[nm]]
        if a == b:
            res["I"].append(nm)
            if fd[nm] == cd[nm]:
                res["I_raw同"].append(nm)
        elif [_blind(x) for x in a] == [_blind(x) for x in b]:
            res["II"].append((nm, _diff_pairs(a, b)))
        else:
            res["III"].append((nm, _diff_pairs(a, b)))
    return res


def _diff_pairs(a, b, limit=3):
    out = []
    for i in range(max(len(a), len(b))):
        x = a[i] if i < len(a) else "(無)"
        y = b[i] if i < len(b) else "(無)"
        if x != y:
            out.append((x, y))
            if len(out) >= limit:
                break
    return out


def report(res, title="對帳"):
    """回 (rc, [報表行])。rc=0 ⇔ 名目全同 ∧ 類 II 空 ∧ 類 III 空。"""
    L, bad = [], False
    L.append("─" * 78)
    L.append(f"【{title}】期望 FAIL 名單：**名目 ＋ 失敗原因**（`verify/wv_reconcile.py`）")
    L.append("─" * 78)
    L.append(f"  名目：凍存 {len(res['名目_凍存'])}／現況 {len(res['名目_現況'])}")
    for k, mark in (("名目_僅凍存有", "凍存有而現況無"), ("名目_僅現況有", "現況有而凍存無")):
        if res[k]:
            bad = True
            L.append(f"  🔴 {mark}：{res[k]}")
    if res["名目_序不同"]:
        bad = True
        L.append("  🔴 名目集合相同但**順序**不同")
    if not (res["名目_僅凍存有"] or res["名目_僅現況有"] or res["名目_序不同"]):
        L.append("  ✅ 名目逐項相同")
    L.append(f"  類 I  （正規化後相同·自動視為同）＝ {len(res['I'])} 項"
             f"　其中 raw 即相同 {len(res['I_raw同'])} 項")
    L.append(f"  類 II （僅 traceback 行號不同·⛔ 須逐項具名確認）＝ {len(res['II'])} 項"
             + ("　（**空**）" if not res["II"] else ""))
    for nm, pairs in res["II"]:
        bad = True
        L.append(f"     🔴 {nm}")
        for x, y in pairs:
            L.append(f"        凍存: {x[:150]}")
            L.append(f"        現況: {y[:150]}")
    L.append(f"  類 III（訊息實質不同）＝ {len(res['III'])} 項"
             + ("　（**空**）" if not res["III"] else ""))
    for nm, pairs in res["III"]:
        bad = True
        L.append(f"     🔴 {nm}")
        for x, y in pairs:
            L.append(f"        凍存: {x[:150]}")
            L.append(f"        現況: {y[:150]}")
    L.append("─" * 78)
    L.append(("  🔴 **對帳 FAIL**——名目或失敗原因與凍存不符（⛔ 不得逕自更新名單）"
              if bad else "  ✅ **對帳 PASS**——名目與失敗原因皆與凍存相符"))
    L.append("─" * 78)
    return (1 if bad else 0), L


DEFAULT_LIST = os.path.join(HERE, "out", "K6A2_期望FAIL名單_WG97_名目加原因.txt")


def reconcile_text(cur_text, list_path=DEFAULT_LIST, title="對帳"):
    """供 `run_all` 內**自動**呼叫：吃本次執行之擷取文字，印報表，回 rc。"""
    if not os.path.exists(list_path):
        print(f"  🔴 對帳：凍存名單不存在（{os.path.relpath(list_path, REPO)}）"
              f"⇒ ⛔ 不得視為通過")
        return 1
    frozen = parse_list(open(list_path, encoding="utf-8").read())
    if not frozen:
        print(f"  🔴 對帳：凍存名單解析出 0 名目 ⇒ ⛔ 空集合不得算通過")
        return 1
    rc, L = report(classify(frozen, parse_log(cur_text)), title)
    for x in L:
        print(x)
    return rc


def _hash_object(p):
    import subprocess
    try:
        r = subprocess.run(["git", "hash-object", p], capture_output=True,
                           text=True, cwd=REPO)
        return r.stdout.strip() or "(取不到)"
    except Exception:
        return "(取不到)"


def main(argv):
    sys.stdout.reconfigure(encoding="utf-8")
    if len(argv) >= 4 and argv[1] == "--freeze":
        log, out = argv[2], argv[3]
        _src_text = open(log, encoding="utf-8").read()
        items = parse_log(_src_text)
        items = [(nm, [normalize(x) for x in det]) for nm, det in items]
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, "w", encoding="utf-8") as f:
            # 🆕 `W-G.9-71` B 組：`_src_text` 供完整性自檢並列來源之 token 數（診斷用）
            f.write(render_list(items, os.path.relpath(log, REPO).replace("\\", "/"),
                                _hash_object(log), _src_text=_src_text))
        print(f"✅ 已產生名單：{os.path.relpath(out, REPO)}（{len(items)} 名目）")
        return 0
    if len(argv) < 3:
        print(__doc__)
        return 2
    cur = open(argv[1], encoding="utf-8").read()
    return reconcile_text(cur, argv[2], title=f"對帳 {os.path.basename(argv[1])}")


if __name__ == "__main__":
    sys.exit(main(sys.argv))
