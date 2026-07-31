# -*- coding: utf-8 -*-
"""K-8 §三 commit A **三層驗收對帳**（交接文 §三·施工單 §2.6）。

三層缺一不可：
  ① 測項**名目集合**雙向 diff        （治：測項憑空消失／新增）
  ② PASS/FAIL **狀態**逐項比對＋翻轉歸因（治：測項健在但結果變了）
  ③ **golden 段**另行清點             （run_all [1/3] 之夾具與探針不進 `results`
                                        ⇒ 前兩層都看不到）

用法：
    python verify/tools/k8_seg3_A_recon.py <基準log> <實測log> [預測log]

`預測log` 給定時，額外做施工單 §2.6-2 之「靶對帳」：
  · 新增紅集合 ⊆ 預測集合          （超出者逐項列出）
  · 預測而未出現者                  （「該紅而沒紅」與「不該紅而紅」同樣是訊號）
"""
import os
import re
import sys

RES = re.compile(r"^\s{2}(✅ PASS|🔴 FAIL)\s{2}(.+?)\s*$")
GOLDEN = re.compile(r"^\s{2}(✅|🔴)\s(.+?)\s*$")


def parse_results(path):
    """`run_verification` 之 132 名目：{name: 'PASS'|'FAIL'}（保序）。"""
    out = {}
    for ln in open(path, encoding="utf-8", errors="replace"):
        m = RES.match(ln.rstrip("\n"))
        if m:
            out[m.group(2)] = "PASS" if "PASS" in m.group(1) else "FAIL"
    return out


def parse_golden(path):
    """run_all [1/3] golden 段：出現在 `### [2/3]` 之前的 ✅/🔴 行。"""
    out, on = [], False
    for ln in open(path, encoding="utf-8", errors="replace"):
        s = ln.rstrip("\n")
        if s.startswith("### [1/3]"):
            on = True
            continue
        if s.startswith("### [2/3]"):
            break
        if not on:
            continue
        m = GOLDEN.match(s)
        if m and not s.lstrip().startswith("│"):
            out.append((m.group(1), m.group(2)))
    return out


def _hdr(t):
    print("\n" + "=" * 96)
    print(t)
    print("=" * 96)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    base_p, got_p = sys.argv[1], sys.argv[2]
    pred_p = sys.argv[3] if len(sys.argv) > 3 else None
    base, got = parse_results(base_p), parse_results(got_p)
    rc = 0

    _hdr("① 測項名目集合 雙向 diff")
    only_b = [n for n in base if n not in got]
    only_g = [n for n in got if n not in base]
    print(f"  基準 {os.path.basename(base_p)}：{len(base)} 名目")
    print(f"  實測 {os.path.basename(got_p)}：{len(got)} 名目")
    print(f"  基準∖實測（消失）：{len(only_b)}")
    for n in only_b:
        print("     −", n)
    print(f"  實測∖基準（新增）：{len(only_g)}")
    for n in only_g:
        print("     +", n)
    if only_b or only_g:
        rc = 1

    _hdr("② PASS/FAIL 狀態 逐項比對")
    flips = [(n, base[n], got[n]) for n in base if n in got and base[n] != got[n]]
    print(f"  基準 PASS/FAIL＝{sum(v=='PASS' for v in base.values())}/"
          f"{sum(v=='FAIL' for v in base.values())}")
    print(f"  實測 PASS/FAIL＝{sum(v=='PASS' for v in got.values())}/"
          f"{sum(v=='FAIL' for v in got.values())}")
    print(f"  狀態翻轉：{len(flips)}")
    for n, b, g in flips:
        print(f"     {b}→{g}  {n}")

    _hdr("③ golden 段清點（不進 results·前兩層看不到）")
    gb, gg = parse_golden(base_p), parse_golden(got_p)
    print(f"  基準 {len(gb)} 支（紅 {sum(1 for s,_ in gb if s=='🔴')}）")
    print(f"  實測 {len(gg)} 支（紅 {sum(1 for s,_ in gg if s=='🔴')}）")
    nb = [n for _, n in gb]
    ng = [n for _, n in gg]
    for n in nb:
        if n not in ng:
            print("     − 消失：", n)
            rc = 1
    for n in ng:
        if n not in nb:
            print("     + 新增：", n)
    for s, n in gg:
        if s == "🔴":
            print("     🔴 紅：", n)
            rc = 1

    if pred_p:
        _hdr("④ 靶對帳（施工單 §2.6-2）：新增紅 vs 預測集合")
        pred = parse_results(pred_p)
        base_red = {n for n, v in base.items() if v == "FAIL"}
        got_red = {n for n, v in got.items() if v == "FAIL"}
        pred_red = {n for n, v in pred.items() if v == "FAIL"}
        new_red = got_red - base_red
        pred_new = pred_red - base_red
        print(f"  基準紅 {len(base_red)}｜預測紅 {len(pred_red)}（其中新增 {len(pred_new)}）"
              f"｜實測紅 {len(got_red)}（其中新增 {len(new_red)}）")
        over = sorted(new_red - pred_new)
        miss = sorted(pred_new - new_red)
        print(f"  ⊄ 超出預測（不該紅而紅）：{len(over)}")
        for n in over:
            print("     ⚠️", n)
        print(f"  預測而未出現（該紅而沒紅）：{len(miss)}")
        for n in miss:
            print("     ⚠️", n)
        if over or miss:
            rc = 1

    _hdr("對帳結論")
    print("  rc =", rc, "（0＝三層皆相符且新增紅落在預測集合內）")
    return rc


if __name__ == "__main__":
    sys.exit(main())
