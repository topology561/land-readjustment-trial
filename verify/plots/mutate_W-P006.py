# -*- coding: utf-8 -*-
"""
W-P.006 之故意錯誤之測（單 §三 4）：成果須綠、Ⓐ〜Ⓔ 共 5 種變異體須各紅（量測 ＝ check_W-P006.py 之 V0〜V6）。

命令列：python verify/plots/mutate_W-P006.py <成果目錄> <重劃前成果目錄> <dict-revised.json> <拋棄式之工作目錄>
  成果目錄 ＝ plots/alloc_state.py、plots/post_maps.py、plots/post_tables.py 之 --out（⛔ 改之）。
  唯驗退縮 3.5 m。各變異體 ＝ plots/ 之複本（於工作目錄）之 post_tables.py 改一處之字（MUTANTS）後，以子行程重出
  附表 13、24 於工作目錄，再以 check_W-P006 量之（V6 之子行程亦用該變異體）；V6 費時，唯成果與 Ⓔ 量之。
結束碼：成果綠且 5 種皆紅 ⇒ 0；否則 1。
"""
import importlib.util
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
_spec = importlib.util.spec_from_file_location("check_W_P006", os.path.join(HERE, "check_W-P006.py"))
chk = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(chk)
TAG = "3.5"

MUTANTS = [   # (名, 說明, 原字, 改字, 跑 V6 否)
    ("Ⓐ", "抵費地負擔面積漏 ÷(1−C)", "b1 = q(G * C / (1 - C), 2)", "b1 = q(G * C, 2)", False),
    ("Ⓑ", "附表 24 漏一宗", "    for e in es:\n        no, ln = numbers", "    for e in es[1:]:\n        no, ln = numbers",
     False),
    ("Ⓒ", "地價比 A 以個位之重劃前單價計", "    A = post / pre\n", "    A = post / q(pre, 0)\n", False),
    ("Ⓓ", "抵費地與公設之備註互換", "NOTE_OFFSET if e[\"類別\"] == KIND_OFFSET else NOTE_PUBLIC",
     "NOTE_PUBLIC if e[\"類別\"] == KIND_OFFSET else NOTE_OFFSET", False),
    ("Ⓔ", "現金補償之備註漏寫", "note = NOTE_CASH.format(cash[k]) if k in cash else None", "note = None", True),
]


def _measure(out, pre, moe, prog, with_v6):
    c = chk.load(out, pre, TAG)
    red = []
    for name, fn in (("V0", chk.v0), ("V1", chk.v1), ("V2", chk.v2), ("V3", chk.v3), ("V4", chk.v4), ("V5", chk.v5)):
        if chk.run(fn, c):
            red.append(name)
    if with_v6 and chk.run(chk.v6, c, moe, prog):
        red.append("V6")
    return red


def main(argv):
    out, pre, moe, work = argv
    if os.path.exists(work):
        shutil.rmtree(work)
    os.makedirs(work)
    ok = True
    base = _measure(out, pre, moe, chk.PROG, True)
    print(f"成果：{'綠' if not base else '紅 ' + '、'.join(base)}")
    ok &= not base
    src = open(os.path.join(REPO, "plots", "post_tables.py"), encoding="utf-8").read()
    for name, desc, a, b, v6 in MUTANTS:
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
        for k in ("state", "map", "color"):
            shutil.copy(os.path.join(out, chk.FMT[k].format(TAG)), o)
        prog = os.path.join(pdir, "post_tables.py")
        # 複本之 plots/ 不在倉內 ⇒ prelim_maps 之 REPO 指向複本之上層；以符號連結補 data／verify（唯讀）
        for sub in ("data", "verify"):
            os.symlink(os.path.join(REPO, sub), os.path.join(d, sub))
        r = subprocess.run([sys.executable, prog, "--state", os.path.join(o, chk.FMT["state"].format(TAG)),
                            "--moedict", moe, "--out", o], capture_output=True, text=True, encoding="utf-8")
        if r.returncode != 0:
            red = ["出表即停"]
        else:
            red = _measure(o, pre, moe, prog, v6)
        print(f"{name}（{desc}）：{'紅 ' + '、'.join(red) if red else '綠（未捕）'}")
        ok &= bool(red)
    print("結論：" + ("成果綠、變異體皆紅" if ok else "不合"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main(sys.argv[1:]))
