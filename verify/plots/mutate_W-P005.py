# -*- coding: utf-8 -*-
"""
W-P.005 之故意錯誤之測（單 §三 4）：成果須綠、Ⓐ〜Ⓘ 共 9 種變異體須各紅（量測 ＝ check_W-P005.py 之 V0〜V8）。
  Ⓕ〜Ⓘ：W-P.005_補令一（KL 2026-10-30 08:00·寬顯示 S、深 ＝ 面積 ÷ W、街角第 1 宗之深含道路截角）。

命令列：python verify/plots/mutate_W-P005.py <成果目錄> <重劃前圖.dxf> <dict-revised.json> <拋棄式之工作目錄>
  成果目錄 ＝ plots/alloc_state.py 與 plots/post_maps.py 之 --out（⛔ 改之；變異體皆寫於工作目錄）。
  唯驗退縮 3.5 m（量測之 V7 之子行程略之·以省時；V7 之判別力另以 Ⓔ 之外之成果之量測證之）。
  Ⓒ〜Ⓗ 掛換 plots/post_maps.py 之函式後重出（於本行程之記憶體中·⛔ 改檔）；Ⓐ、Ⓑ 改成果之複本；
  Ⓘ 改配地結果之複本（街角第 1 宗之 W 改為截角後之寬）後重出。
結束碼：成果綠且 9 種皆紅 ⇒ 0；否則 1。
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


def _regen(d, env, attr, val, edit_state=None):
    import json
    pm = _plots()
    orig = getattr(pm, attr) if attr else None
    if attr:
        setattr(pm, attr, val)
    try:
        if os.path.exists(d):
            shutil.rmtree(d)
        os.makedirs(d)
        st = os.path.join(env["out"], chk.FMT["state"].format(TAG))
        shutil.copy(st, d)
        if edit_state:
            st = os.path.join(d, chk.FMT["state"].format(TAG))
            doc = json.load(open(st, encoding="utf-8"))
            edit_state(doc)
            with open(st, "w", encoding="utf-8") as f:
                json.dump(doc, f, ensure_ascii=False, indent=1)
        pm.main(["--state", st, "--pre-dxf", env["pre"], "--moedict", env["moe"], "--out", d])
    finally:
        if attr:
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


def _cad_lines_with(d, env, change):
    pm = _plots()
    orig = pm.cad_lines

    def cad_lines(e, no, blocks):
        return orig(change(dict(e)), no, blocks)
    _regen(d, env, "cad_lines", cad_lines)


def mF_width_W(d, env):
    """圖面之寬仍註 W（宗地寬度）而非 S。"""
    def ch(e):
        if "S" in e:
            e["S"] = e["宗地寬度"]
        return e
    _cad_lines_with(d, env, ch)


def mG_no_cut(d, env):
    """街角第 1 宗之深未納道路截角面積。"""
    def ch(e):
        e.pop("街角第1宗側別", None)
        return e
    _cad_lines_with(d, env, ch)


def mH_depth_by_S(d, env):
    """深以 S 除（面積 ÷ S）而非 W。"""
    def ch(e):
        if "S" in e:
            e["宗地寬度"] = e["S"]
        return e
    _cad_lines_with(d, env, ch)


def mI_post_cut_width(d, env):
    """街角第 1 宗之 W 改為截角後之寬（配地結果之複本·宗地寬度 − 理論角至正面臨路線上最近之頂點之距）。"""
    import math
    from shapely.geometry import LineString, Point, Polygon

    def edit(doc):
        for x in doc["宗"]:
            if "街角第1宗側別" not in x:
                continue
            b = doc["街廓"][x["街廓"]]
            fl = LineString(b["正面臨路線"])
            c = Point(chk._theory_corner(chk_ctx(doc), x))
            near = min(math.dist(p, c.coords[0]) for p in Polygon(x["多邊形"]).exterior.coords
                       if fl.distance(Point(p)) <= 0.02)
            x["宗地寬度"] = round(x["宗地寬度"] - near, 2)
    _regen(d, env, None, None, edit_state=edit)


def chk_ctx(doc):
    c = chk.Ctx()
    c.state = doc
    return c


MUTANTS = [
    ("Ⓐ 公告分配地籍線漏一宗", mA_drop_lot, True),
    ("Ⓑ 二宗同號", mB_dup_number, True),
    ("Ⓒ S 型不交替", mC_no_alternation, False),
    ("Ⓓ 歸戶之色錯位", mD_owner_shift, False),
    ("Ⓔ 重劃後地價圖用重劃前地價", mE_pre_price, False),
    ("Ⓕ 寬仍註 W 而非 S", mF_width_W, False),
    ("Ⓖ 街角第 1 宗之深未納道路截角", mG_no_cut, False),
    ("Ⓗ 深以 S 除而非 W", mH_depth_by_S, False),
    ("Ⓘ 街角第 1 宗之 W 用截角後之寬", mI_post_cut_width, False),
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
