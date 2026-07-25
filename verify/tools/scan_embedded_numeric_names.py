# -*- coding: utf-8 -*-
r"""F-7-6(c)：掃「名目字串內嵌**會隨案變動之數值**」者，供 P-H 判「同閘改名」vs「名目增減」。

**判準（明列·可復現）**：名目字串中出現下列任一 pattern（tag `0m`/`3.5m` 本身不計）：
  P1 `\d+\s*(列|筆|宗|對|格|群|片|端)`   計數型（如「115 列」「三對」之數字化）
  P2 `\{.*\d.*\}`                        dict/set 字面內含數值（如 k* 六塊、GSA 六格）
  P3 `\d+→\d+`                           轉換型（如「31→17」）
  P4 `Σ=|＝\d`                            合計型
用法：python verify/tools/scan_embedded_numeric_names.py <run_log> [out_md]
"""
import re
import sys
import io

PATS = [(r'\d+\s*(?:列|筆|宗|對|格|群|片|端)', 'P1 計數'),
        (r'\{[^}]*\d[^}]*\}', 'P2 dict/set 字面'),
        (r'\d+→\d+', 'P3 轉換'),
        (r'Σ=|＝\d', 'P4 合計')]


def scan(log_path):
    names = []
    for l in io.open(log_path, encoding='utf-8', errors='replace'):
        m = re.search(r'(✅ PASS|🔴 FAIL)\s+(.+)', l)
        if m:
            names.append(m.group(2).strip())
    hits = []
    for n in sorted(set(names)):
        core = re.sub(r'\b(?:0m|3\.5m)\b', '', n)     # tag 不計
        kinds = [k for p, k in PATS if re.search(p, core)]
        if kinds:
            hits.append((n, '／'.join(kinds)))
    return names, hits


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")   # NOTE-1：cp950 崩（本專案反覆踩之雷）
    except Exception:
        pass
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    names, hits = scan(sys.argv[1])
    out = [f"# F-7-6(c) 內嵌數值之名目清單（判準見 scan_embedded_numeric_names.py docstring）",
           f"", f"來源 log：`{sys.argv[1]}`｜名目 {len(names)} 行／{len(set(names))} 唯一"
           f"｜**命中 {len(hits)} 列**", ""]
    out.append("| # | 名目 | 命中判準 |")
    out.append("|---|---|---|")
    for i, (n, k) in enumerate(hits, 1):
        out.append(f"| {i} | `{n}` | {k} |")
    txt = "\n".join(out)
    if len(sys.argv) > 2:
        io.open(sys.argv[2], 'w', encoding='utf-8').write(txt + "\n")
        print(f"寫入 {sys.argv[2]}（命中 {len(hits)} 列）")
    else:
        print(txt)
    return 0


if __name__ == "__main__":
    sys.exit(main())
