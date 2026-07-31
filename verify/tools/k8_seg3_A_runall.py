# -*- coding: utf-8 -*-
"""K-8 §三 commit A 驗收跑：`run_all` ＋ **全母體 `diff_rows` 增量落檔**。

案由（施工單 §2.6-7）：`run_verification` 只印 `viol[:12]` ⇒ **禁以打印輸出當 delta 母體**
（K-8 段二曾因此差點漏掉第三個增配群 G033）。故此處**包住 `rv.diff_rows`**，把每一次比對之
**完整**違規列增量寫入 CSV，再由 `k8_seg3_A_recon.py` 對帳。

用法：
    python verify/tools/k8_seg3_A_runall.py <out_tag>
輸出：
    verify/out/<out_tag>.log        run_all 全文（含 REAL_EXIT）
    verify/out/<out_tag>_viol.csv   全母體違規列（來源測項／鍵／欄／期望／實得）
"""
import csv
import os
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # verify/
REPO = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(REPO, "tests"))


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    tag = sys.argv[1] if len(sys.argv) > 1 else "K8_seg3_A"
    outdir = os.path.join(HERE, "out")
    os.makedirs(outdir, exist_ok=True)
    csv_path = os.path.join(outdir, f"{tag}_viol.csv")

    import run_verification as rv
    _orig = rv.diff_rows
    fh = open(csv_path, "w", encoding="utf-8-sig", newline="")
    wr = csv.writer(fh)
    wr.writerow(["測項", "違規列序", "違規全文"])

    def _wrapped(rows, baseline_csv, keys, name, *a, **k):
        ok, viol = _orig(rows, baseline_csv, keys, name, *a, **k)
        for i, v in enumerate(viol):          # **全母體**（非 viol[:12]）
            wr.writerow([name, i, str(v)])
        fh.flush()
        return ok, viol

    rv.diff_rows = _wrapped
    import run_all
    rc = run_all.main()
    fh.close()
    print(f"\n[全母體違規列已落檔] {csv_path}")
    return rc


if __name__ == "__main__":
    sys.exit(main())
