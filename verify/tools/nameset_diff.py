r"""**`run_all` 名目集合正規化對拍器**（K-6-A2 段四 §0-5 升格入倉）。

## 為何存在

換機確認之第 2 項（「132 名目／86 PASS／46 FAIL 零進零出」）原以**拋棄式腳本**跑，
`f2decad` 只 commit 了兩份 `.md` ⇒ **倉內既無工具亦無 log**，該宣稱無從複驗。
這正是 `run_all.py:157`（BLOCKED-3 案由）與 **GB-29／GB-30** 反覆咬到的同一形狀，
亦即段四 §四-1 才剛為此把三支拋棄式腳本升格之理由。⇒ 本器升格入倉。

## 判準

⛔ **不以計數驗收**——計數相同不代表名目相同（可能一進一出而總數不變）。
本器輸出**集合差**：**出**（靶有本次無）／**進**（本次有靶無）／**判定翻轉**。
三者皆 0 才算「零進零出零翻轉」。

## 正規化

只取 `✅ PASS`／`🔴 FAIL` 之**判定＋名目**，並剝除**與機器相關**之雜訊：
絕對路徑（Windows `C:\…` 與 POSIX `/…/x.py` 皆處理）、`line N`、`0x…` 位址、連續空白。
⚠️ 刻意**只掃判定行**，不掃 `🔴` 診斷行——診斷行含全精度浮點，
**跨主機不穩定**（GB-30／GB-31 已實證）⇒ 掃入會製造假差異。

## 用法

    python verify/tools/nameset_diff.py <靶.log> <本次.log>

rc：0 ＝ 零進零出零翻轉；1 ＝ 有差異（⇒ 依施工單停機上呈）；2 ＝ 用法錯誤。
🔒 路徑一律由參數給、輸出以 `os.path.relpath` 相對化 ⇒ **可攜**，⛔ 無寫死絕對路徑。
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))       # verify/tools/ → verify/ → repo

VERDICT = re.compile(r"^\s*(✅ PASS|🔴 FAIL)\s+(.*?)\s*$")


def normalize(name):
    """剝除與機器相關之雜訊，使兩機之同一名目化為同一字串。"""
    name = re.sub(r"[A-Za-z]:\\[^\s'\"]+", "<PATH>", name)      # Windows 絕對路徑
    name = re.sub(r"/(?:[\w.-]+/)+[\w.-]+\.py", "<PATH>", name)  # POSIX 路徑
    name = re.sub(r"\bline \d+\b", "line <N>", name)
    name = re.sub(r"0x[0-9a-fA-F]+", "<ADDR>", name)
    return re.sub(r"\s+", " ", name).strip()


def load(path):
    """回 {正規化名目: 'PASS'|'FAIL'}。"""
    out = {}
    with open(path, encoding="utf-8", errors="replace") as f:
        for line in f:
            m = VERDICT.match(line.rstrip("\n"))
            if m:
                out[normalize(m.group(2))] = "PASS" if "PASS" in m.group(1) else "FAIL"
    if not out:
        raise RuntimeError(
            f"🔴 {path}：掃不到任何 `✅ PASS`／`🔴 FAIL` 判定行。"
            f"該檔是 `run_all` 之輸出嗎？（no-silent-fallback：不靜默回空集合）")
    return out


def rel(p):
    try:
        return os.path.relpath(p, REPO)
    except ValueError:                      # 跨磁碟機 ⇒ 保留原樣（Windows）
        return p


def main(argv):
    for _st in (sys.stdout, sys.stderr):
        try:
            _st.reconfigure(encoding="utf-8")
        except Exception:
            pass
    if len(argv) != 3:
        print(__doc__)
        return 2
    tgt, cur = load(argv[1]), load(argv[2])

    def tally(d):
        return sum(v == "PASS" for v in d.values()), sum(v == "FAIL" for v in d.values())

    tp, tf = tally(tgt)
    cp, cf = tally(cur)
    print("=" * 100)
    print(f"靶   {rel(argv[1])}: {len(tgt)} 名目  PASS={tp}  FAIL={tf}")
    print(f"本次 {rel(argv[2])}: {len(cur)} 名目  PASS={cp}  FAIL={cf}")
    print("=" * 100)
    gone = sorted(set(tgt) - set(cur))
    came = sorted(set(cur) - set(tgt))
    flip = sorted(n for n in (set(tgt) & set(cur)) if tgt[n] != cur[n])
    print(f"\n── 出（靶有·本次無）{len(gone)} ──")
    for n in gone:
        print(f"  - [{tgt[n]}] {n}")
    print(f"── 進（本次有·靶無）{len(came)} ──")
    for n in came:
        print(f"  + [{cur[n]}] {n}")
    print(f"── 判定翻轉 {len(flip)} ──")
    for n in flip:
        print(f"  ! {n}: {tgt[n]} → {cur[n]}")
    ok = not (gone or came or flip)
    print("\n✅ 零進零出零翻轉" if ok else "\n🛑 有差異 ⇒ 依施工單停機上呈（⛔ 禁改碼／禁調容差使其變綠）")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
