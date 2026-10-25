# -*- coding: utf-8 -*-
"""
W-P.002_補令一：以示範之 170 筆（示範001〜示範170·歸戶號 1〜170）出附表 26，供 check_W-P002.py 之 Q6 驗跨頁之排列。
命令列：python verify/plots/synth_W-P002a.py <輸出之 .xlsx>（⛔ 在倉內）
示範之名非實案資料；唯驗 plots/owner_index.write_appx26 之排列與分頁符。
"""
import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(REPO, "plots"))
import owner_index  # noqa: E402

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    owner_index.write_appx26(sys.argv[1], [(f"示範{i:03d}", i) for i in range(1, 171)])
    print("輸出", sys.argv[1])
