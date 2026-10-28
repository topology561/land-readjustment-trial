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
KIND_LOT, KIND_OFFSET = "分配地", "抵費地"
OFFSET_SIDE = "抵費地"
OUT_FMT = "配地結果_退縮{}m.json"


class SourceError(RuntimeError):
    """資料與單之所據不符 ⇒ 停機上呈。"""


def q2(x):
    return float(Decimal(repr(float(x))).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))


def tag_of(setback):
    s = f"{setback:g}"
    return s


def run_pipeline(setbacks):
    """⇒ (cb_by, cad, omap, {退縮: g_rows})。管線之印出一律收於記憶體（⛔ 擾本程式之輸出）。"""
    import run_verification as rv
    from app_harvest import harvest
    from selection_pipeline import build_ownership, build_build_parcels, run_corner_pk_k6b
    from stepg_pipeline import run_step_g
    sink = io.StringIO()
    with contextlib.redirect_stdout(sink):
        snapshot = rv.load_snapshot()
        ns, fake_st = harvest()
        cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
        build_ownership(ns, fake_st, rv.ANON_XLSX)
        with open(rv.V6DXF, "rb") as f:
            v6 = f.read()
        temp, build, _sw = build_build_parcels(ns, fake_st, v6, list(cb_by.values()), snapshot)
        rows = {}
        for sb in setbacks:
            params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, sb)
            _d, _s, _o, win, forced, _tp3, bp3 = run_corner_pk_k6b(
                ns, fake_st, list(cb_by.values()), cad, params, temp, build, sb, snapshot=snapshot)
            sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot, params, bp3,
                            win, forced, sb, eff_min_build_by_blk={})
            rows[sb] = sg["g_rows"]
        omap = dict(fake_st.session_state["t8_ownership_map"])
    return cb_by, cad, omap, rows


def blocks_of(cb_by, cad):
    alloc = cad.get("alloc_dir_by_block") or {}
    front = cad.get("front_lines") or {}
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
        out[lbl] = d
    return out


def lots_of(g_rows, blocks, omap):
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
            d.update({"原地號": ln, "歸戶": omap[ln], "G": q2(r["G(㎡)"]), "宗地寬度": q2(w)})
        lots.append(d)
    return lots, dropped


def main(argv=None):
    ap = argparse.ArgumentParser(description="W-P.005 配地結果之取出")
    ap.add_argument("--out", required=True)
    ap.add_argument("--setback", type=float, action="append", required=True)
    a = ap.parse_args(argv)
    os.makedirs(a.out, exist_ok=True)
    cb_by, cad, omap, rows = run_pipeline(a.setback)
    blocks = blocks_of(cb_by, cad)
    for sb in a.setback:
        lots, dropped = lots_of(rows[sb], blocks, omap)
        doc = {"退縮_m": sb, "來源": SOURCE_NOTE, "街廓": blocks, "宗": lots, "略": dropped}
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
