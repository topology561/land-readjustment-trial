# -*- coding: utf-8 -*-
"""
W-P.005 之故意錯誤之測（單 §三 4）：成果須綠、Ⓐ〜Ⓔ 共 5 種變異體須各紅（量測 ＝ check_W-P005.py 之 V0〜V7）。

命令列：python verify/plots/mutate_W-P005.py <成果目錄> <重劃前圖.dxf> <dict-revised.json> <拋棄式之工作目錄>
  成果目錄 ＝ plots/alloc_state.py 與 plots/post_maps.py 之 --out（⛔ 改之；變異體皆寫於工作目錄）。
  唯驗退縮 3.5 m（量測之 V7 之子行程略之·以省時；V7 之判別力另以 Ⓔ 之外之成果之量測證之）。
  Ⓒ、Ⓓ、Ⓔ 掛換 plots/post_maps.py 之函式後重出（於本行程之記憶體中·⛔ 改檔）；Ⓐ、Ⓑ 改成果之複本。
結束碼：成果綠且 5 種皆紅 ⇒ 0；否則 1。
"""
import importlib.util
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
_spec = importlib.util.spec_from_file_location("check_W_P005", os.path.join(HERE, "check_W-P005.py"))
chk = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(chk)
TAG = "3.5"


def _copy(src, dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)
    shutil.copytree(src, dst)


def _plots():
    sys.path.insert(0, os.path.join(REPO, "plots"))
    import post_maps
    return post_maps


def _dxf(d):
    import ezdxf
    p = os.path.join(d, chk.FMT["dxf"].format(TAG))
    return p, ezdxf.readfile(p)


def mA_drop_lot(d, env):
    """公告分配地籍線漏一宗（刪其界線）。"""
    p, doc = _dxf(d)
    msp = doc.modelspace()
    e = next(iter(msp.query(f'LWPOLYLINE[layer=="{chk.L_CAD}"]')))
    msp.delete_entity(e)
    doc.saveas(p)


def mB_dup_number(d, env):
    """二宗同號（改一宗之地號之註記為他宗之號）。"""
    p, doc = _dxf(d)
    msp = doc.modelspace()
    nos = [t for t in msp.query(f'TEXT[layer=="{chk.L_CAD}"]') if chk.NO_RE.match(t.dxf.text)]
    nos[0].dxf.text = nos[1].dxf.text
    doc.saveas(p)


def _regen(d, env, attr, val):
    pm = _plots()
    orig = getattr(pm, attr)
    setattr(pm, attr, val)
    try:
        if os.path.exists(d):
            shutil.rmtree(d)
        os.makedirs(d)
        st = os.path.join(env["out"], chk.FMT["state"].format(TAG))
        shutil.copy(st, d)
        pm.main(["--state", st, "--pre-dxf", env["pre"], "--moedict", env["moe"], "--out", d])
    finally:
        setattr(pm, attr, orig)


def mC_no_alternation(d, env):
    """S 型不交替（每一街廓皆自東而西）。"""
    pm = _plots()
    orig = pm.s_order

    def s_order(doc, ents):
        from shapely.geometry import Polygon
        o = orig(doc, ents)
        pos = {t: i for i, t in enumerate(o)}
        by = {}
        for e in ents:
            by.setdefault(e["街廓"], []).append(e)
        blocks = [b for b in dict.fromkeys(e["街廓"] for e in sorted(ents, key=lambda e: pos[e["暫編"]]))
                  if "宗地分配線方向" in doc["街廓"][b]]
        out = []
        for b in blocks:
            out += [e["暫編"] for e in sorted(by[b], key=lambda e: -Polygon(e["多邊形"]).centroid.x)]
        return out + [t for t in o if t not in set(out)]
    _regen(d, env, "s_order", s_order)


def mD_owner_shift(d, env):
    """原地主之地之色錯一戶（歸戶之色依序錯位）。"""
    pm = _plots()
    orig = pm.owner_scheme

    def owner_scheme(moedict, ents):
        key_of, hh_color, hh_no = orig(moedict, ents)
        ks = list(hh_color)
        cols = [hh_color[k] for k in ks]
        return key_of, dict(zip(ks, cols[1:] + cols[:1])), hh_no
    _regen(d, env, "owner_scheme", owner_scheme)


def mE_pre_price(d, env):
    """重劃後地價圖改用重劃前之區段地價（b 區段 37323）。"""
    pm = _plots()

    def post_prices():
        return {f"R{i}": 37323.0 for i in range(1, 7)}
    _regen(d, env, "post_prices", post_prices)


MUTANTS = [
    ("Ⓐ 公告分配地籍線漏一宗", mA_drop_lot, True),
    ("Ⓑ 二宗同號", mB_dup_number, True),
    ("Ⓒ S 型不交替", mC_no_alternation, False),
    ("Ⓓ 歸戶之色錯位", mD_owner_shift, False),
    ("Ⓔ 重劃後地價圖用重劃前地價", mE_pre_price, False),
]


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if len(argv) != 4:
        print(__doc__)
        return 2
    out, pre, moe, work = argv
    env = {"out": out, "pre": pre, "moe": moe}
    base = chk.run(out, pre, moe, [TAG], quiet=True, run_map=False)
    print(f"成果：{'綠' if not base else '紅 ' + str(base)}")
    ok = not base
    for i, (name, fn, from_copy) in enumerate(MUTANTS):
        d = os.path.join(work, f"m{i}")
        if from_copy:
            _copy(out, d)
        fn(d, env)
        fails = chk.run(d, pre, moe, [TAG], quiet=True, run_map=False)
        print(f"{name}：{'紅 ' + str(fails) if fails else '綠（未捕）'}")
        ok = ok and bool(fails)
    print("合" if ok else "不合")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
