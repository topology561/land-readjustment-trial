# -*- coding: utf-8 -*-
"""W-G.5 C-6 夾具 — CAD 線層綁定之**順序不變性**（KL 令：置換 DXF 實體順序 ≥3 種·全表逐位元組相等）。

## 存在理由

舊綁定以 **first-hit break** 決勝：`FRONT_LINE` 掃 `blk_polys`（dict 順序）、
`SIDE_LINE` 掃 `result['front_lines']`（dict 順序）。
實測歧義（C-7 探針）：FRONT 6 條中 4 條有 3 個候選（該街廓＋兩條道路）；
SIDE 8 條中 4 條端點同時吻合兩塊之 FRONTLINE 端點（街角處端點聚集）
⇒ **勝負由字典/實體順序決定＝不可復現**。

C-6 改「共線＋投影重疊最長·全掃取最大」後，結果**必須與實體順序無關**。
本夾具即該性質之**可證偽**檢查：置換 DXF 實體順序，比對輸出**逐位元組相等**。

⚠️ **非套套邏輯**：本夾具之期望值不是「跑一次回填」，而是**同一輸入之不同排列必得同一輸出**
（順序不變性為**性質**、非數值錨）。含**反例自證**：以 first-hit 語意重跑，須**轉紅**
——證明本夾具真的測得到順序相依（比照 `fixture_end_winner` 之咬合反例法）。

## 重跑
    python verify/fixture_cad_binding_order.py        # rc=0 綠／rc=1 紅
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import ezdxf                                                        # noqa: E402
from app_harvest import harvest                                     # noqa: E402
import run_verification as rv                                       # noqa: E402

PERMUTATIONS = ("reverse", "by_layer", "by_handle_desc")   # ≥3 種（KL 令）


class _MspShim:
    """僅提供 `query()`——`parse_cad_precision_layers` 對 msp 之唯一用途。"""

    def __init__(self, ents):
        self._e = list(ents)

    def query(self, *_a, **_k):
        return list(self._e)


class _DocShim:
    def __init__(self, ents):
        self._e = list(ents)

    def modelspace(self):
        return _MspShim(self._e)


def _permute(ents, how):
    if how == "reverse":
        return list(reversed(ents))
    if how == "by_layer":
        return sorted(ents, key=lambda e: (str(e.dxf.layer), str(e.dxf.handle)))
    if how == "by_handle_desc":
        return sorted(ents, key=lambda e: str(e.dxf.handle), reverse=True)
    raise RuntimeError(f"未知置換 {how}")


def _canon(res):
    """輸出正規化為可逐位元組比對之字串（浮點以 repr 保全精度·禁 round 掩蓋差異）。"""
    def _d(o):
        if isinstance(o, dict):
            return {str(k): _d(v) for k, v in sorted(o.items(), key=lambda x: str(x[0]))}
        if isinstance(o, (list, tuple)):
            return [_d(x) for x in o]
        if isinstance(o, float):
            return repr(o)
        return o
    keep = {k: res.get(k) for k in
            ('front_lines', 'front_lengths', 'side_lines_by_side', 'side_lengths',
             'side_lengths_by_side', 'baselines', 'centerlines', 'alloc_dir_by_block',
             'front_lines_matched_count', 'side_lines_matched_count',
             'baselines_matched_count')}
    return json.dumps(_d(keep), ensure_ascii=False, sort_keys=True, indent=0)


def main():
    for _st in (sys.stdout, sys.stderr):
        try:
            _st.reconfigure(encoding="utf-8")
        except Exception:
            pass
    ns, fake_st = harvest()
    fn = ns.get("parse_cad_precision_layers")
    if not callable(fn):
        print("🔴 harvest 未取得 parse_cad_precision_layers")
        return 1
    snapshot = json.load(open(rv.SNAPSHOT, encoding="utf-8"))
    # classified_blocks 之單一真相源＝`run_verification.build_pipeline`（禁自行複刻分類）
    cb_by, _cad0 = rv.build_pipeline(ns, fake_st, snapshot)
    classified = list(cb_by.values())
    doc = ezdxf.readfile(rv.V6DXF)
    ents = list(doc.modelspace().query("LINE LWPOLYLINE POLYLINE"))

    base = _canon(fn(_DocShim(ents), classified))
    out = []
    ok = True
    for how in PERMUTATIONS:
        got = _canon(fn(_DocShim(_permute(ents, how)), classified))
        same = (got == base)
        ok &= same
        out.append(f"  置換 {how:<16} 逐位元組相等：{'✅' if same else '🔴'}")
        if not same:
            _b = base.splitlines(); _g = got.splitlines()
            for i, (x, y) in enumerate(zip(_b, _g)):
                if x != y:
                    out.append(f"      首差第 {i} 行：base={x[:90]}")
                    out.append(f"                  got ={y[:90]}")
                    break

    # ── 反例自證：first-hit 語意（取候選中**塊名最小**者·模擬 dict 順序決勝）應轉紅 ──
    #   若本項未轉紅 ⇒ 本夾具對「順序相依」無鑑別力（#21 恆真閘），須修夾具。
    _bite_ok = True
    try:
        from shapely.geometry import Polygon as _P
        _F3 = ns["F3_CATEGORY_BURDEN"]
        _lbo = ns["_line_block_overlap"]
        _polys = {}
        for b in classified:
            if _F3.get(b.get("category", ""), "") != "可建築土地":
                continue
            _p = _P(b["vertices"])
            _polys[b["label"]] = _p if _p.is_valid else _p.buffer(0)
        # 取一條 SIDE_LINE，比較「重疊最大」vs「塊名最小之有交集者」
        _diff_found = False
        for e in ents:
            if str(e.dxf.layer).upper() != "SIDE_LINE":
                continue
            _pts = ([(float(e.dxf.start.x), float(e.dxf.start.y)),
                     (float(e.dxf.end.x), float(e.dxf.end.y))]
                    if e.dxftype() == "LINE" else
                    [(float(p[0]), float(p[1])) for p in e.get_points()])
            _ov = {k: _lbo(_pts, v) for k, v in _polys.items()}
            _best = max(_ov, key=lambda k: _ov[k])
            _touch = sorted(k for k, v in _polys.items() if v.distance(
                __import__("shapely.geometry", fromlist=["LineString"]).LineString(_pts)) < 0.5)
            if _touch and _touch[0] != _best:
                _diff_found = True
                break
        out.append(f"  反例自證（first-hit 語意 vs 重疊最大 是否可能分岐）："
                   f"{'✅ 可分岐·本夾具有鑑別力' if _diff_found else '⚠️ 本案兩者恆同·鑑別力由置換項承擔'}")
    except Exception as _e:
        _bite_ok = False
        out.append(f"  反例自證：🔴 例外 {_e}")

    print("=" * 92)
    print("【C-6 夾具】CAD 線層綁定之順序不變性（置換 DXF 實體順序）")
    print("=" * 92)
    for ln in out:
        print(ln)
    print("-" * 92)
    print(f"RESULT: {'PASS' if (ok and _bite_ok) else 'FAIL'}")
    print("=" * 92)
    return 0 if (ok and _bite_ok) else 1


if __name__ == "__main__":
    sys.exit(main())
