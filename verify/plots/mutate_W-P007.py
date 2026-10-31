# -*- coding: utf-8 -*-
"""
W-P.007 之故意錯誤之測（單 §三 4）：成果須綠、Ⓐ〜Ⓔ 共 5 種變異體須各紅（量測 ＝ check_W-P007.py 之 L0〜L6）。

命令列：python verify/plots/mutate_W-P007.py <成果目錄> <舊版成果目錄> <dict-revised.json> <拋棄式之工作目錄>
  成果目錄 ＝ plots/alloc_state.py、plots/post_maps.py、plots/post_tables.py 之 --out（⛔ 改之）。
  唯驗退縮 3.5 m。各變異體 ＝ plots/ 之複本（於工作目錄）之 post_tables.py 改一處之字（MUTANTS）後，以子行程重出
  附表 13、24 於工作目錄，再以 check_W-P007 對舊版成果量之。
結束碼：成果綠且 5 種皆紅 ⇒ 0；否則 1。
"""
import importlib.util
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
_spec = importlib.util.spec_from_file_location("check_W_P007", os.path.join(HERE, "check_W-P007.py"))
chk = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(chk)
TAG = "3.5"
STATE, MAP = "配地結果_退縮{}m.json", "地號對照表_退縮{}m.xlsx"

MUTANTS = [   # (名, 說明, 原字, 改字)
    ("Ⓐ", "住址之標籤未跨四列", '(4, 11, 7, 11, "住址")', '(4, 11, 5, 11, "住址")'),
    ("Ⓑ", "欄名改用他名（取配面積→分配面積）", '(9, 6, 10, 6, "取配面積(㎡)")', '(9, 6, 10, 6, "分配面積(㎡)")'),
    ("Ⓒ", "鄉鎮市區漏直書", "A13_VERT = ((4, 11), (8, 24), (9, 1), (9, 3),", "A13_VERT = ((4, 11), (8, 24), (9, 3),"),
    ("Ⓓ", "外框未加粗", "Border(left=thick if c == 1 else thin", "Border(left=thin if c == 1 else thin"),
    ("Ⓔ", "首列登記人之姓名與統編錯格", "    (4, 8, 4, 10), (5, 8, 5, 10), (4, 12, 5, 24),",
     "    (5, 8, 5, 10), (4, 8, 4, 10), (4, 12, 5, 24),"),
]
CHECKS = (("L0", chk.l0), ("L1", chk.l1), ("L2", chk.l2), ("L3", chk.l3), ("L4", chk.l4), ("L5", chk.l5),
          ("L6", chk.l6))


def _measure(out, old):
    new, ref = chk.load(out, old, TAG)
    return [name for name, fn in CHECKS if chk.run(fn, new, ref)]


def main(argv):
    out, old, moe, work = argv
    if os.path.exists(work):
        shutil.rmtree(work)
    os.makedirs(work)
    ok = True
    base = _measure(out, old)
    print(f"成果：{'綠' if not base else '紅 ' + '、'.join(base)}")
    ok &= not base
    src = open(os.path.join(REPO, "plots", "post_tables.py"), encoding="utf-8").read()
    for name, desc, a, b in MUTANTS:
        if src.count(a) != 1:
            print(f"{name}（{desc}）：原字不唯一或不在（{src.count(a)}）")
            ok = False
            continue
        d = os.path.join(work, name)
        pdir = os.path.join(d, "plots")
        shutil.copytree(os.path.join(REPO, "plots"), pdir, ignore=shutil.ignore_patterns("__pycache__"))
        with open(os.path.join(pdir, "post_tables.py"), "w", encoding="utf-8") as f:
            f.write(src.replace(a, b))
        o = os.path.join(d, "out")
        os.makedirs(o)
        for k in (STATE, MAP):
            shutil.copy(os.path.join(out, k.format(TAG)), o)
        # 複本之 plots/ 不在倉內 ⇒ prelim_maps 之 REPO 指向複本之上層；以符號連結補 data／verify（唯讀）
        for sub in ("data", "verify"):
            os.symlink(os.path.join(REPO, sub), os.path.join(d, sub))
        r = subprocess.run([sys.executable, os.path.join(pdir, "post_tables.py"), "--state",
                            os.path.join(o, STATE.format(TAG)), "--moedict", moe, "--out", o],
                           capture_output=True, text=True, encoding="utf-8")
        red = ["出表即停"] if r.returncode != 0 else _measure(o, old)
        print(f"{name}（{desc}）：{'紅 ' + '、'.join(red) if red else '綠（未捕）'}")
        ok &= bool(red)
    print("結論：" + ("成果綠、變異體皆紅" if ok else "不合"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main(sys.argv[1:]))
