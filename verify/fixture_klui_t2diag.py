# -*- coding: utf-8 -*-
r"""`W-G.9-184`：`GB-123` 之守備（`M-E-4` 候選 (a)）——**KL UI 產物之凍存對拍**。

## 受詞（🔒 ⛔ **不是**「app 之池算得對不對」）

> 受詞 ＝ **「倉內 `verify/out/KL_UI_3.5m_*_stdout.log` 之 `[T2-DIAG]` <u>整列</u>，
> 與凍存者逐位相符；且其<u>街廓序列</u>與凍存者相同」**。

**為何需要**：`GB-123` ＝ **生產路徑（app）之池⛔ 無任何自動守備**——
`run_all` 所掛 `21` 項中，其 `got` 端經 `app.py:main()` 產生者 ＝ **`0`**
（`CLAUDE.md` 之「`main()` 內之敘述**從不被 `run_all` 執行**」）。
而 `W-G.9-183R` 已判「**本波所尋之覆蓋自檢實不存在**」（式(ii) 構造恆真·判 (B)）
⇒ **覆蓋類自檢結構上⛔ 不可能**偵測 app-vs-shim 之差 ⇒ **唯一可行者係「值之直接對拍」**。
本夾具即該對拍之機械載體：池之**唯一人工錨**（`stdout.log` 之 `[T2-DIAG]`）自此有**可紅之物**。

## 🔴 本夾具**轉紅之因**（⛔ 逐項列舉·非單一）

1. **任一 `[T2-DIAG]` 整列之任一字元改變** ⇒ 紅（含逐帶 `s` 寬／逐帶面積／`Σ池`／
   `覆蓋殘差`／`Σ 殘差`／`宗-宗疊`／`內部縫`／`退化帶`／`s 域`／`宗數`／`池帶片數`）。
2. **街廓序列改變** ⇒ 紅。🔒 **含 `R5` 之出現**——見下「凍存為期望事實者」。
3. **某 log 之 `[T2-DIAG]` 列數改變**（趟數變動）⇒ 紅。
4. **log 檔被增刪／改名** ⇒ 紅（名目集合改變）。
5. **凍存檔不存在或解析出 0 筆** ⇒ 紅（⛔ 空集合不得算通過）。
6. **判別力自檢失效**（注入擾動後仍綠）⇒ 紅（⛔ 一個永綠之守備器比沒有更糟）。

## 🔒 凍存為**期望事實**者（⛔ 非疏漏·`M-I-1 2`）

🔴 **`R5` 於二 log 皆⛔ 無 `[T2-DIAG]`**——`W-G.9-183R` 已坐實其於
`KL_UI_3.5m_2e08a41_stdout.log:2985` 拋
`RuntimeError: 🔴 K-9-4 BASELINE 臨接閘未過：【未配到屁股線】1 宗——R5 之 628-53(2)`
而終止 ⇒ 該趟從未抵達 `R5` 之 `[T2-DIAG]`。
⇒ 🔒 **「`R5` 缺席」係凍存之一部**；日後 `R5` 出現 ⇒ **本夾具轉紅以逼人來看**
（設計意圖同 `fixture_e2e_termination.py`：**特性，不是缺陷**）。
⛔ 屆時不得逕自重凍了事，須先確認「`R5` 跑到了」確為預期。

## 🔴 本夾具之**射程外**（⛔ 逐項·`VR-082`·不得留空）

| # | 射程外 | 說明 |
|---|---|---|
| 1 | **只守「已入倉之那一趟」** | KL 下次實跑之產物須**人工入倉**方進入母體 ⇒ **仍非全自動**；`GB-123` **⛔ 未消滅**，只是自此有可紅之物 |
| 2 | **該 log 之態⛔ 不可自證**（`GB-119`） | 檔名之 `2e08a41`／`a3c97aa` 係人工命名，⛔ 無機械保證其為該 commit 之產物 |
| 3 | **守「變動」⛔ 非守「正確」** | 凍存值本身若已錯（如 app 之池算法有誤），本夾具**恆綠** ⇒ ⛔ 不得讀為「app 之池已驗證正確」 |
| 4 | ⛔ 不涵蓋 `R5`（無錨） | `R5` 之池於 KL UI 側**從未產生**⇒ 無值可守；shim 側之值見 `probe_WG9183_pool_cover_9f4b8301.log` |
| 5 | ⛔ 不比對 app-vs-shim | 本夾具二端**皆為 app 側**（凍存 vs 現值）；app-vs-shim 之差（如 `R2` 族② `0.1171`）**⛔ 非本夾具之受詞** |

## ⛔ 本檔不做

⛔ 不改 `app.py`／`stepg_pipeline.py`／`run_verification.py` 一字。
⛔ 不改任何既有夾具。⛔ 不寫入 `verify/out/KL_UI_3.5m_*` 之任何一檔（**唯讀**）。
⛔ 不由本檔現算期望值——期望值**一律自獨立凍存檔讀入**（`M-I-1 3`）。
⛔ 不寫死本機絕對路徑。
"""
import glob
import hashlib
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
OUTDIR = os.path.join(HERE, "out")
FROZEN = os.path.join(OUTDIR, "WG9184_KLUI_T2DIAG_凍存.txt")
LOG_GLOB = os.path.join(OUTDIR, "KL_UI_3.5m_*_stdout.log")
MARK = "[T2-DIAG]"
RC = [0]


def red(msg):
    RC[0] = 1
    print("  🔴 " + msg)


def observe():
    """自倉內 log 抽 `[T2-DIAG]` **整列**。回傳 [(basename, idx, 整列原文), …]。

    🔒 **⛔ 不解析欄位、⛔ 不正規化**——受詞係整列逐位，任何解析都會產生
      「放棄了什麼」之盲點（`fixture_e2e_termination` 之投影表所示）。"""
    rows = []
    for p in sorted(glob.glob(LOG_GLOB)):
        base = os.path.basename(p)
        txt = open(p, encoding="utf-8", errors="replace").read()
        k = 0
        for ln in txt.splitlines():
            if MARK in ln:
                k += 1
                rows.append((base, k, ln))
    return rows


def blk_of(line):
    m = re.search(r"街廓 (\S+?)｜", line)
    return m.group(1) if m else "?"


def freeze():
    """`--freeze`：產生凍存檔。🛑 **⛔ 非夾具之一部**——只由 CC 於建置時執行一次，
    其過程逐字記錄於 `W-G.9-184R` 報告。"""
    rows = observe()
    if not rows:
        print("🔴 抽不到任何 [T2-DIAG] ⇒ ⛔ 不產生凍存")
        return 1
    meta = {}
    for base, _k, ln in rows:
        meta.setdefault(base, []).append(blk_of(ln))
    lines = [
        "# `W-G.9-184` `GB-123` 守備之凍存：KL UI 產物之 `[T2-DIAG]` **整列**",
        "# 來源 ＝ verify/out/KL_UI_3.5m_*_stdout.log（框 ＝ 含 `[T2-DIAG]` 之列·⛔ 未解析欄位）",
        "# 🔒 `R5` 之缺席係**期望事實**（其於 K-9-4 BASELINE 臨接閘終止）⇒ 出現即須轉紅",
        "# 格式：#META\\t<log>\\t<列數>\\t<街廓序列>　／　<log>\\t<序>\\t<整列原文>",
    ]
    for base, blks in meta.items():
        lines.append("#META\t%s\t%d\t%s" % (base, len(blks), ",".join(blks)))
    for base, k, ln in rows:
        lines.append("%s\t%d\t%s" % (base, k, ln))
    with open(FROZEN, "w", encoding="utf-8", newline="") as f:
        f.write("\n".join(lines) + "\n")
    body = "\n".join(x for x in lines if not x.startswith("#")) + "\n"
    print("WROTE %s" % os.path.relpath(FROZEN, REPO))
    print("  列數 = %d（其中 #META %d 列／資料 %d 列）"
          % (len(lines), len(meta), len(rows)))
    print("  本體 sha256（扣除 `#` 檔頭行）= %s"
          % hashlib.sha256(body.encode("utf-8")).hexdigest())
    return 0


def parse_frozen(txt):
    meta, rows = {}, []
    for ln in txt.splitlines():
        if ln.startswith("#META\t"):
            _, base, n, seq = ln.split("\t", 3)
            meta[base] = (int(n), seq.split(",") if seq else [])
        elif ln.startswith("#") or not ln.strip():
            continue
        else:
            base, k, body = ln.split("\t", 2)
            rows.append((base, int(k), body))
    return meta, rows


def compare(meta, frozen, cur):
    """回傳 (是否紅, 訊息列)。⛔ 純函式 ⇒ 判別力自檢可對其重複呼叫。"""
    L, bad = [], False
    cur_meta = {}
    for base, _k, ln in cur:
        cur_meta.setdefault(base, []).append(blk_of(ln))
    if set(cur_meta) != set(meta):
        bad = True
        L.append("    🔴 log 名目集合改變：凍存 %s ／ 現值 %s"
                 % (sorted(meta), sorted(cur_meta)))
    for base in sorted(set(meta) | set(cur_meta)):
        en, eseq = meta.get(base, (0, []))
        gseq = cur_meta.get(base, [])
        ok = (len(gseq) == en and gseq == eseq)
        if not ok:
            bad = True
        L.append("    %s %-46s 列數 %d/%d　街廓序列 %s"
                 % ("✅" if ok else "🔴", base, len(gseq), en,
                    "相符" if gseq == eseq else "**不符**：凍存 %s ／ 現值 %s" % (eseq, gseq)))
    fmap = {(b, k): v for b, k, v in frozen}
    gmap = {(b, k): v for b, k, v in cur}
    keys = sorted(set(fmap) | set(gmap))
    ndiff = 0
    for key in keys:
        fv, gv = fmap.get(key), gmap.get(key)
        if fv != gv:
            ndiff += 1
            bad = True
            if ndiff <= 6:
                L.append("    🔴 逐位不符 %s#%d" % key)
                L.append("       凍存：%s" % (fv if fv is not None else "(缺)"))
                L.append("       現值：%s" % (gv if gv is not None else "(缺)"))
    L.append("    %s 逐位比對：%d 列中 %d 列不符"
             % ("✅" if ndiff == 0 else "🔴", len(keys), ndiff))
    return bad, L


def perturb(frozen):
    """對**凍存之複本**注入一處擾動：首列之 `Σ池` 末位 `+0.0001`（`M-I-2`）。"""
    out, done = [], False
    for base, k, ln in frozen:
        if not done:
            m = re.search(r"Σ池 ([0-9]+\.[0-9]+)", ln)
            if m:
                ln = ln.replace(m.group(0),
                                "Σ池 %.4f" % (float(m.group(1)) + 0.0001), 1)
                done = True
        out.append((base, k, ln))
    return out, done


def main():
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8")
        except Exception:
            pass
    print("=" * 96)
    print("# `W-G.9-184` 夾具：`GB-123` 守備·KL UI `[T2-DIAG]` **整列**凍存對拍")
    print("=" * 96)
    if not os.path.exists(FROZEN):
        red("凍存不存在（%s）⇒ ⛔ 不得視為通過" % os.path.relpath(FROZEN, REPO))
        return RC[0]
    meta, frozen = parse_frozen(open(FROZEN, encoding="utf-8").read())
    if not frozen:
        red("凍存解析出 0 筆 ⇒ ⛔ 空集合不得算通過")
        return RC[0]
    cur = observe()
    if not cur:
        red("倉內 log 抽不到任何 `[T2-DIAG]` ⇒ ⛔ 不得視為通過")
        return RC[0]
    print("  凍存 ＝ %s（%d log／%d 列）"
          % (os.path.relpath(FROZEN, REPO), len(meta), len(frozen)))
    print("  ⚠️ 受詞 ＝ `[T2-DIAG]` **整列逐位** ＋ **街廓序列**；🔒 `R5` 之缺席係**期望事實**")
    print("  ⚠️ 射程外：只守已入倉之那一趟／態⛔ 不可自證／守變動⛔ 非守正確（見 docstring）")
    bad, L = compare(meta, frozen, cur)
    for x in L:
        print(x)
    if bad:
        red("與凍存不符 ⇒ ⛔ 不得逕自重凍（須先確認該變動確為預期）")

    # ── 判別力自檢（`M-I-2`·⛔ 兩態皆印·⛔ 只動記憶體複本）────────────────
    print()
    print("─" * 96)
    print("【判別力自檢】對**凍存之複本**注入一處擾動 ⇒ 須紅；移除 ⇒ 須綠（⛔ 兩態皆印）")
    print("─" * 96)
    tampered, done = perturb(frozen)
    if not done:
        red("⛔ 注入失敗（找不到 `Σ池` 之數）⇒ 判別力**未經證明** ⇒ 本夾具不得計入交付")
        return RC[0]
    r_t, _ = compare(meta, tampered, cur)
    r_r, _ = compare(meta, frozen, cur)
    print("  注入態（首列 `Σ池` 末位 +0.0001）⇒ %s" % ("🔴 紅" if r_t else "✅ 綠"))
    print("  還原態                          ⇒ %s" % ("🔴 紅" if r_r else "✅ 綠"))
    if r_t and not r_r:
        print("  ✅ 判別力成立（注入態紅 ∧ 還原態綠）")
    else:
        red("判別力**不成立** ⇒ 本夾具不得計入交付（`W-G.9-184 X-3`）")

    print()
    print("=" * 96)
    print("%s（rc=%d）" % ("✅ 夾具 PASS" if RC[0] == 0 else "🔴 夾具 FAIL", RC[0]))
    print("=" * 96)
    return RC[0]


if __name__ == "__main__":
    sys.exit(freeze() if "--freeze" in sys.argv else main())
