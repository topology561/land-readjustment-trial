# -*- coding: utf-8 -*-
"""
W-P.005　配地結果之取出（重劃後三圖層與地號對照表之輸入）。

命令列：python plots/alloc_state.py --out <目錄> --setback <退縮公尺> [--setback …]
輸出（皆寫至 --out，⛔ 入倉）：配地結果_退縮<退縮>m.json（每一退縮一檔）。

所據：出圖線/orders/W-P.005_重劃後三圖層與地號對照表.md（§一 3、§二 1）。
  來源 ＝ 既有之無畫面之配地流程（verify/ 之管線·唯呼叫·⛔ 改），依 verify/run_verification.py 之 main
  之序：load_snapshot → harvest → build_pipeline → build_param_table → build_ownership →
  build_build_parcels → run_corner_pk_k6b → run_step_g（eff_min_build_by_blk＝{}）。
  所取者 ＝ 階段一之終（段三後·調配〔核心線階段二〕之前）之 g_rows；調配之新模組入主線後，唯改本檔之來源。
  「推進側別」＝「抵費地」之列 ⇒ 類別「抵費地」（同 app.py export_allocated_dxf）；他列 ⇒「分配地」。
  面積二位四捨五入為 0.00 之列不成宗，列於「略」（印之·⛔ 靜默）。
  W-P.005_補令一（KL 2026-10-30 08:00）：分配地加「S」（G 值計算之臨正面道路寬度·g_rows 之 S(m)）與
  「街角第1宗側別」（g_rows 之「第1筆街角」＝是者之「街角側別」：左／右）；街廓加「側面道路線」（CAD 之
  side_lines_by_side·左／右·各 [p1, p2]）——供公告分配地籍線之「寬」（顯示 S）與街角宗之「深」（含道路截角）。
  W-P.006（附表 13、24·KL 2026-10-30 19:28）：分配地加 G 式之各項（「a」＝g_rows 之 a 面積、「a原位次」＝該宗之
  分攤登記面積〔build_parcels·二位〕、「併入面積」＝ a − a原位次、「重劃前區段」、「F」、「W」〔g_rows 之 W(m)·Rw 所查〕、
  「Rw」〔%〕、「l側」、「l正」）；檔加「財務」（stepg_pipeline._compute_v3_finance 之 B、C、重劃後單價〔街廓〕、
  重劃前單價〔區段〕·全精度·同 run_step_g 所用）、「歸戶表」（地號 → 歸戶之代號·t8_ownership_map）、
  「現金補償」（階段一未判 ⇒ []；調配之新模組入主線後由本檔填之·每項 {"歸戶", "金額"}）。
缺值一律報錯停止（⛔ 靜默補值）。
"""
import argparse
import contextlib
import io
import json
import os
import sys
from decimal import Decimal, ROUND_HALF_UP

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(REPO, "verify"))

SOURCE_NOTE = "階段一之終（段三後·未經調配）：verify/stepg_pipeline.run_step_g 之 g_rows"
CASH_NOTE = "階段一未判現金補償（調配之新模組未成）"
KIND_LOT, KIND_OFFSET = "分配地", "抵費地"
OFFSET_SIDE = "抵費地"
OUT_FMT = "配地結果_退縮{}m.json"
SIDE_NAME = {"left": "左", "right": "右"}
CORNER_SIDE = {"左側": "左", "右側": "右"}


class SourceError(RuntimeError):
    """資料與單之所據不符 ⇒ 停機上呈。"""


def q2(x):
    return float(Decimal(repr(float(x))).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))


def tag_of(setback):
    s = f"{setback:g}"
    return s


def run_pipeline(setbacks):
    """⇒ (cb_by, cad, omap, {退縮: g_rows}, {退縮: build_parcels}, 財務)。管線之印出一律收於記憶體（⛔ 擾本程式之輸出）。"""
    import run_verification as rv
    from app_harvest import harvest
    from selection_pipeline import build_ownership, build_build_parcels, run_corner_pk_k6b
    from stepg_pipeline import run_step_g, _compute_v3_finance
    sink = io.StringIO()
    with contextlib.redirect_stdout(sink):
        snapshot = rv.load_snapshot()
        ns, fake_st = harvest()
        cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
        build_ownership(ns, fake_st, rv.ANON_XLSX)
        with open(rv.V6DXF, "rb") as f:
            v6 = f.read()
        temp, build, _sw = build_build_parcels(ns, fake_st, v6, list(cb_by.values()), snapshot)
        fin = _compute_v3_finance(ns, snapshot, list(cb_by.values()), cad)
        rows, bps = {}, {}
        for sb in setbacks:
            params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, sb)
            _d, _s, _o, win, forced, _tp3, bp3 = run_corner_pk_k6b(
                ns, fake_st, list(cb_by.values()), cad, params, temp, build, sb, snapshot=snapshot)
            sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot, params, bp3,
                            win, forced, sb, eff_min_build_by_blk={})
            rows[sb] = sg["g_rows"]
            bps[sb] = bp3
        omap = dict(fake_st.session_state["t8_ownership_map"])
    return cb_by, cad, omap, rows, bps, fin


def finance_of(fin):
    out = {"B": float(fin["B"]), "C": float(fin["C"]),
           "重劃後單價": {k: float(v) for k, v in sorted(fin["post_price_by_block"].items())},
           "重劃前單價": {k: float(v) for k, v in sorted(fin["pre_price_by_zone"].items())}}
    if not (0 < out["B"] < 1 and 0 < out["C"] < 1) or not out["重劃後單價"] or not out["重劃前單價"]:
        raise SourceError(f"財務之值不合：B {out['B']}、C {out['C']}")
    return out


def blocks_of(cb_by, cad):
    alloc = cad.get("alloc_dir_by_block") or {}
    front = cad.get("front_lines") or {}
    sides = cad.get("side_lines_by_side") or {}
    out = {}
    for lbl in sorted(cb_by):
        b = cb_by[lbl]
        vs = b.get("vertices") or []
        if len(vs) < 3:
            raise SourceError(f"街廓 {lbl} 之頂點不足")
        cat = b.get("category")
        if not cat:
            raise SourceError(f"街廓 {lbl} 無分類")
        d = {"分類": cat, "面積": float(b["area_m2"]), "多邊形": [[float(x), float(y)] for x, y in vs]}
        if lbl in alloc:
            if lbl not in front:
                raise SourceError(f"街廓 {lbl} 有宗地分配線而無正面臨路線")
            d["宗地分配線方向"] = [float(v) for v in alloc[lbl]]
            d["正面臨路線"] = [[float(v) for v in front[lbl]["p1"]], [float(v) for v in front[lbl]["p2"]]]
            sl = {}
            for side, nm in SIDE_NAME.items():
                if side in sides.get(lbl, {}):
                    s = sides[lbl][side]
                    sl[nm] = [[float(v) for v in s["p1"]], [float(v) for v in s["p2"]]]
            d["側面道路線"] = sl
        out[lbl] = d
    return out


def own_area_of(build):
    """build_parcels ⇒ {暫編地號: 分攤登記面積_m2}（缺 ⇒ 不入；用時缺即停）。"""
    out = {}
    for b in build:
        k = b.get("暫編地號")
        if k in out:
            raise SourceError(f"build_parcels 之暫編地號 {k} 重複")
        if k and b.get("分攤登記面積_m2") is not None:
            out[k] = float(b["分攤登記面積_m2"])
    return out


def lots_of(g_rows, blocks, omap, own_area):
    lots, dropped = [], []
    seen = set()
    for r in g_rows:
        pid = r.get("暫編地號")
        if not pid or pid in seen:
            raise SourceError(f"配地之列之暫編地號缺或重複：{pid!r}")
        seen.add(pid)
        blk = r.get("所屬街廓")
        if blk not in blocks or "宗地分配線方向" not in blocks[blk]:
            raise SourceError(f"{pid} 之街廓 {blk!r} 非可分配之街廓")
        cs = r.get("cut_coords") or []
        if len(cs) < 3:
            raise SourceError(f"{pid} 無多邊形")
        area = q2(r["幾何面積(㎡)"])
        kind = KIND_OFFSET if r.get("推進側別") == OFFSET_SIDE else KIND_LOT
        if area == 0:
            dropped.append({"配地暫編": pid, "街廓": blk, "類別": kind, "幾何面積": float(r["幾何面積(㎡)"])})
            continue
        d = {"配地暫編": pid, "街廓": blk, "類別": kind, "面積": area,
             "多邊形": [[float(x), float(y)] for x, y in cs]}
        if kind == KIND_LOT:
            ln = r.get("原地號")
            if not ln or ln not in omap:
                raise SourceError(f"{pid} 之原地號 {ln!r} 不在歸戶表")
            w = r.get("宗地寬度(m)")
            if w is None or float(w) <= 0:
                raise SourceError(f"{pid} 之宗地寬度缺")
            s = r.get("S(m)")
            if s is None or float(s) <= 0:
                raise SourceError(f"{pid} 之 S 缺")
            d.update({"原地號": ln, "歸戶": omap[ln], "G": q2(r["G(㎡)"]), "宗地寬度": q2(w), "S": q2(s)})
            if pid not in own_area:
                raise SourceError(f"{pid} 無分攤登記面積（build_parcels）")
            a = Decimal(repr(float(r["a 面積(㎡)"]))).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
            a0 = Decimal(repr(own_area[pid])).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
            if a <= 0 or a0 <= 0 or a0 > a:
                raise SourceError(f"{pid} 之 a {a}、分攤登記面積 {a0} 不合")
            zone = r.get("重劃前區段")
            if not zone:
                raise SourceError(f"{pid} 之重劃前區段缺")
            for k in ("F(m)", "W(m)", "Rw(%)", "l₁ 側面尺度", "l₂ 正面尺度"):
                if r.get(k) is None or float(r[k]) < 0:
                    raise SourceError(f"{pid} 之 {k} 缺或負")
            d.update({"a": float(a), "a原位次": float(a0), "併入面積": float(a - a0), "重劃前區段": zone,
                      "F": float(r["F(m)"]), "W": float(r["W(m)"]), "Rw": float(r["Rw(%)"]),
                      "l側": float(r["l₁ 側面尺度"]), "l正": float(r["l₂ 正面尺度"])})
            first = r.get("第1筆街角")
            if first == "是":
                side = CORNER_SIDE.get(r.get("街角側別"))
                if side is None:
                    raise SourceError(f"{pid} 為街角第 1 宗而街角側別 {r.get('街角側別')!r} 不明")
                if side not in blocks[blk]["側面道路線"]:
                    raise SourceError(f"{pid} 為{side}側街角第 1 宗而街廓 {blk} 無該側之側面道路線")
                d["街角第1宗側別"] = side
            elif first != "否":
                raise SourceError(f"{pid} 之「第1筆街角」{first!r} 非是／否")
        lots.append(d)
    return lots, dropped


def main(argv=None):
    ap = argparse.ArgumentParser(description="W-P.005 配地結果之取出")
    ap.add_argument("--out", required=True)
    ap.add_argument("--setback", type=float, action="append", required=True)
    a = ap.parse_args(argv)
    os.makedirs(a.out, exist_ok=True)
    cb_by, cad, omap, rows, bps, fin = run_pipeline(a.setback)
    blocks = blocks_of(cb_by, cad)
    finance = finance_of(fin)
    for sb in a.setback:
        lots, dropped = lots_of(rows[sb], blocks, omap, own_area_of(bps[sb]))
        doc = {"退縮_m": sb, "來源": SOURCE_NOTE, "街廓": blocks, "宗": lots, "略": dropped,
               "財務": finance, "歸戶表": {k: omap[k] for k in sorted(omap)},
               "現金補償": [], "現金補償之來源": CASH_NOTE}
        p = os.path.join(a.out, OUT_FMT.format(tag_of(sb)))
        with open(p, "w", encoding="utf-8") as f:
            json.dump(doc, f, ensure_ascii=False, indent=1)
            f.write("\n")
        n_off = sum(1 for x in lots if x["類別"] == KIND_OFFSET)
        print(f"退縮 {tag_of(sb)} m：宗 {len(lots)}（分配地 {len(lots) - n_off}、抵費地 {n_off}）；"
              f"略 {[x['配地暫編'] for x in dropped]}")
        print(f"輸出 {p}")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
