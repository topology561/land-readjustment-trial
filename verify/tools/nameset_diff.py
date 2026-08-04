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

# 🔴 **第二族：夾具／golden**（K-6-A2 段四(c)-1 補·本器初版之盲區）
#   `run_all` 對夾具／golden 之報告格式為 `  ✅ <名目>…rc=0` ／ `  🔴 <名目>…rc=1`
#   ——**沒有 `PASS`／`FAIL` 字樣** ⇒ 初版之 `VERDICT` 完全掃不到，
#   而 `run_all.py:110` 明明把 `fixture_corner_range_k8.py` 等 8 支夾具掛在裡面。
#   ⚠️ **本器初版曾據此回報「零進零出零翻轉」，而該次實際上有一支夾具 rc 0→1**
#   ——閘看不見它本該守的東西。實測該族於靶檔共 **12 行**（縮排 2·含 `rc=`）。
#   判準：縮排 ≤ 2 ∧ 含 `rc=`（夾具內部之逐項明細縮排 ≥ 4 且不含 `rc=` ⇒ 自然排除）。
FIXTURE = re.compile(r"^\s{0,2}(✅|🔴)\s+(.*?)\s*rc=(\d+)\s*$")


def normalize(name):
    """剝除與機器相關之雜訊，使兩機之同一名目化為同一字串。"""
    name = re.sub(r"[A-Za-z]:\\[^\s'\"]+", "<PATH>", name)      # Windows 絕對路徑
    name = re.sub(r"/(?:[\w.-]+/)+[\w.-]+\.py", "<PATH>", name)  # POSIX 路徑
    name = re.sub(r"\bline \d+\b", "line <N>", name)
    name = re.sub(r"0x[0-9a-fA-F]+", "<ADDR>", name)
    return re.sub(r"\s+", " ", name).strip()


def load(path):
    """回 `(名目族, 夾具族)`；兩族皆為 `{正規化名目: 'PASS'|'FAIL'}`。

    🔴 **兩族須分開比**：`run_all` 對二者之報告格式不同（見 `FIXTURE` 之註）。
    只比第一族會**看不見夾具翻轉**——本器初版即如此，並因而誤報過一次「零進零出」。
    """
    names, fixtures = {}, {}
    with open(path, encoding="utf-8", errors="replace") as f:
        for line in f:
            line = line.rstrip("\n")
            m = VERDICT.match(line)
            if m:
                names[normalize(m.group(2))] = "PASS" if "PASS" in m.group(1) else "FAIL"
                continue
            m = FIXTURE.match(line)
            if m:
                fixtures[normalize(m.group(2))] = "PASS" if m.group(3) == "0" else "FAIL"
    if not names and not fixtures:
        raise RuntimeError(
            f"🔴 {path}：掃不到任何判定行（`✅ PASS`／`🔴 FAIL`，或夾具之 `✅ …rc=N`）。"
            f"該檔是 `run_all` 之輸出嗎？（no-silent-fallback：不靜默回空集合）")
    if not fixtures:
        raise RuntimeError(
            f"🔴 {path}：掃到 {len(names)} 個名目，但**夾具族為空**。"
            f"`run_all.py` 明載掛有 8 支 fixture（`grep -n 'fixture_corner_range_k8.py' verify/run_all.py`）"
            f"⇒ 掃不到即表示格式已變、本器已瞎，⛔ 不得當『沒有夾具』繼續（no-silent-fallback）。")
    return names, fixtures


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
    tgt_n, tgt_f = load(argv[1])
    cur_n, cur_f = load(argv[2])

    def tally(d):
        return sum(v == "PASS" for v in d.values()), sum(v == "FAIL" for v in d.values())

    def section(title, tgt, cur):
        tp, tf = tally(tgt)
        cp, cf = tally(cur)
        print("=" * 100)
        print(f"【{title}】")
        print(f"  靶   {len(tgt):>4} 項  PASS={tp}  FAIL={tf}")
        print(f"  本次 {len(cur):>4} 項  PASS={cp}  FAIL={cf}")
        gone = sorted(set(tgt) - set(cur))
        came = sorted(set(cur) - set(tgt))
        flip = sorted(n for n in (set(tgt) & set(cur)) if tgt[n] != cur[n])
        print(f"  ── 出（靶有·本次無）{len(gone)} ──")
        for n in gone:
            print(f"    - [{tgt[n]}] {n}")
        print(f"  ── 進（本次有·靶無）{len(came)} ──")
        for n in came:
            print(f"    + [{cur[n]}] {n}")
        print(f"  ── 判定翻轉 {len(flip)} ──")
        for n in flip:
            print(f"    ! {n}: {tgt[n]} → {cur[n]}")
        return not (gone or came or flip)

    print(f"靶   {rel(argv[1])}")
    print(f"本次 {rel(argv[2])}")
    ok_n = section("名目族（`✅ PASS`／`🔴 FAIL`）", tgt_n, cur_n)
    ok_f = section("夾具／golden 族（`✅ …rc=N`）", tgt_f, cur_f)
    print("=" * 100)
    ok = ok_n and ok_f
    print("\n✅ 兩族皆零進零出零翻轉" if ok
          else "\n🛑 有差異 ⇒ 依施工單停機上呈（⛔ 禁改碼／禁調容差使其變綠）")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
