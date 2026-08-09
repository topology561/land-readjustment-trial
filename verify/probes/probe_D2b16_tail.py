# -*- coding: utf-8 -*-
r"""**D-2b-16 §e-1／§e-3**：對拍補「舊判準是否破」欄 ＋ `.intersection()` 呼叫點**AST 窮舉**。

§e-3 之窮舉**以 AST 為之**，⛔ 非字面 grep——`.intersection()` 可能以**鏈式**
（`a.intersection(b).intersection(c)`）、**別名**、或經 `shapely.ops` **間接**出現，
單純 grep 字面必漏（本波已有兩次「固定 regex 代窮舉」之教訓：`W_far` 寫 6 實 7、已廢止式寫 2 實 4）。
"""
import ast
import io
import math
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
sys.path.insert(0, VERIFY)

from app_harvest import harvest                                     # noqa: E402

OUTDIR = os.path.join(VERIFY, "out")
LOG = os.path.join(OUTDIR, os.environ.get("WV_TAIL_LOG", "probe_D2b16_tail.log"))
TOL = 1e-6
W = 200

# shapely 之集合運算／間接呼叫（§e-3 提醒 3：不只 `.intersection`）
SET_OPS = {"intersection", "intersects", "difference", "symmetric_difference",
           "union", "overlaps", "within", "contains", "crosses", "touches"}
OPS_FUNCS = {"unary_union", "cascaded_union", "shared_paths", "split", "snap"}


def _u(v):
    n = math.hypot(v[0], v[1])
    return (v[0] / n, v[1] / n)


def _old_gate(pieces):
    """**已作廢**之舊判準（最大兩兩 `.intersection()`）——僅供對拍，⛔ 非生產。"""
    mx, pair = 0.0, None
    for i in range(len(pieces)):
        for j in range(i + 1, len(pieces)):
            if pieces[i].is_empty or pieces[j].is_empty:
                continue
            x = float(pieces[i].intersection(pieces[j]).area)
            if x > mx:
                mx, pair = x, (i, j)
    return mx, pair


def _ast_scan(path):
    """AST 窮舉：回傳 [(lineno, 形式, 受詞片段)]。"""
    src = io.open(path, encoding="utf-8").read()
    tree = ast.parse(src)
    lines = src.splitlines()
    hits = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        f = node.func
        if isinstance(f, ast.Attribute) and f.attr in SET_OPS:
            _recv = "鏈式" if isinstance(f.value, ast.Call) else "單一"
            hits.append((node.lineno, f".{f.attr}()", _recv,
                         lines[node.lineno - 1].strip()[:120]))
        elif isinstance(f, ast.Name) and f.id in OPS_FUNCS:
            hits.append((node.lineno, f"{f.id}()", "ops", lines[node.lineno - 1].strip()[:120]))
        elif isinstance(f, ast.Attribute) and f.attr in OPS_FUNCS:
            hits.append((node.lineno, f"{f.attr}()", "ops", lines[node.lineno - 1].strip()[:120]))
    return sorted(hits)


def main():                                                        # noqa: C901
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8")
        except Exception:
            pass
    os.makedirs(OUTDIR, exist_ok=True)
    import numpy as np
    from shapely.geometry import Polygon

    ns, _ = harvest()
    part = ns["_block_partition"]
    L = []
    L.append("=" * W)
    L.append("【D-2b-16 §e-1／§e-3】對拍補欄 ＋ `.intersection()` AST 窮舉")
    L.append("=" * W)

    # ══ §e-1 對拍補「舊判準是否破」欄 ══
    L.append("")
    L.append("【§e-1】新舊判準對拍（**補『舊判準是否破』欄**·四格全列）")
    L.append("-" * W)
    L.append("  🔒 D-2b-15 之對拍報「0 差異」，但其中**舊判準破者為 0**")
    L.append("     ⇒ 該組**未涵蓋受測現象**（本批所修者正是「舊判準**誤破**」）")
    L.append("     ⇒ 「0 差異」只證明**現象未發生處**兩者都沒事，**未**證明新舊等價。")
    L.append("  🔒 此為「空集合偽裝成沒問題」之**深一層**：母體非空，但**受測現象之子集為空**。")
    L.append("     ⛔ **母體筆數不得作為涵蓋性之證據。**")

    def _corpus(seed, k):
        r = random.Random(seed)
        out = []
        while len(out) < k:
            cx, cy = r.uniform(-211.7, 388.3), r.uniform(-97.1, 271.9)
            n = r.randint(6, 13)
            pts, a = [], r.uniform(0, 2 * math.pi)
            for _ in range(n):
                a += (2 * math.pi / n) * r.uniform(0.45, 1.55)
                rr = r.uniform(31.7, 137.9) * (0.35 if r.random() < 0.35 else 1.0)
                pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
            p = Polygon(pts)
            if not p.is_valid:
                p = p.buffer(0)
            if p.is_empty or p.geom_type != "Polygon" or p.area < 400.0:
                continue
            out.append(p)
        return out, r

    _n_tot = _old_bad = 0
    _c = {'舊破新過': 0, '舊過新破': 0, '皆破': 0, '皆過': 0}
    _ex = []
    for _seed, _k in ((20260809_13, 14), (20260809_14, 10)):
        _ps, r = _corpus(_seed, _k)
        for pp in _ps:
            b = pp.bounds
            base = np.array([(b[0] + b[2]) / 2.0, (b[1] + b[3]) / 2.0])
            for _t in range(10):
                _ang = r.uniform(0, 2 * math.pi)
                dh2 = np.array(_u((math.cos(_ang), math.sin(_ang))))
                k = r.randint(3, 6)
                sv = sorted(r.uniform(-160.0, 160.0) for _ in range(k + 1))
                dirs = [_u((math.cos(_ang + math.radians(r.uniform(2.0, 130.0))),
                            math.sin(_ang + math.radians(r.uniform(2.0, 130.0)))))
                        for _ in range(k + 1)]
                qs = [base + s * dh2 for s in sv]
                ln = list(zip([tuple(map(float, q)) for q in qs], dirs))
                _n_tot += 1
                try:
                    pc, dg = part(pp, dh2, ln, _label="cmp")
                    _newbad = False
                except RuntimeError:
                    pc, _newbad = None, True
                if pc is None:
                    # 新破 ⇒ 無片可餵舊判準；以「舊未知」計入「舊過新破」之保守側
                    _c['舊過新破'] += 1
                    continue
                _o, _pair = _old_gate(pc)
                _oldbad = (_o > TOL)
                if _oldbad:
                    _old_bad += 1
                    if len(_ex) < 3:
                        _ex.append((round(_o, 6), _pair))
                _c['皆破' if (_oldbad and _newbad) else
                   '舊破新過' if _oldbad else
                   '舊過新破' if _newbad else '皆過'] += 1
    L.append("")
    L.append(f"  母體筆數 ＝ **{_n_tot}**")
    L.append(f"  🔑 **舊判準破者筆數（＝現象涵蓋數）＝ {_old_bad}**")
    L.append(f"  四格：舊破新過 **{_c['舊破新過']}**／舊過新破 **{_c['舊過新破']}**"
             f"／兩者皆破 **{_c['皆破']}**／兩者皆過 **{_c['皆過']}**")
    if _ex:
        L.append(f"  舊破之實例（最大兩兩交集, 片對）：{_ex}")
    if _old_bad == 0:
        L.append("  ⇒ 🔒 **本組未涵蓋受測現象，對拍不構成等價性證據**"
                 "（⛔ 不得以四格數字充作等價結論）。")
    else:
        L.append("  ⇒ 本組**已涵蓋**受測現象（舊破 > 0），四格具比較意義。")
    L.append("  🔒 **目前唯一涵蓋該現象之樣本 ＝ fixture 本身，n = 1**"
             "（`verify/fixtures/case_D2b15_tilegate_intersection.py`）。")
    L.append("  ⛔ **未**為使舊破筆數非零而擴大或更換母體——母體與 D-2b-15 §d-4-3 **完全相同**"
             "（同 seed、同生成式）⇒ 兩批可直接對照。")

    # ══ §e-3 `.intersection()` AST 窮舉 ══
    L.append("")
    L.append("【§e-3】生產碼之集合運算呼叫點（**AST 窮舉**·⛔ 非字面 grep）")
    L.append("-" * W)
    L.append(f"  掃描之運算子：{sorted(SET_OPS)}　＋ ops：{sorted(OPS_FUNCS)}")
    hits = _ast_scan(os.path.join(REPO, "app.py"))
    _inter = [h for h in hits if h[1] == ".intersection()"]
    L.append(f"  `app.py` 全部集合運算呼叫點 ＝ **{len(hits)}**；"
             f"其中 `.intersection()` ＝ **{len(_inter)}**")
    _chain = [h for h in _inter if h[2] == "鏈式"]
    L.append(f"  其中**鏈式**（`a.intersection(b).intersection(c)`）＝ **{len(_chain)}**"
             f"　⇒ 字面 grep 之計數會與此**不同**（提醒 3）")
    L.append("")
    L.append(f"  {'行號':>7}  {'形式':<22}{'受詞':<6}  原文")
    for ln, kind, recv, txt in _inter:
        L.append(f"  {ln:>7}  {kind:<22}{recv:<6}  {txt}")
    L.append("")
    L.append("  【型態標註】兩運算元是否為 **sliver**（已多次裁切之細長片）：")
    # 🔴 **自查**：首版以**字面子字串**分類 ⇒ `:9050`（`pg.intersection(bg)`）與
    #   `:9062`（`_biz[i].intersection(_biz[j])`）**皆為片×片**卻被歸入「其他」
    #   ——**又一次「固定 pattern 代窮舉」**（本波第三次）。改為**逐點人工判定**並具名。
    _CLS = {
        4361: ("未判定（宗地 sp × 街廓 sp·兩者皆為輸入多邊形、非本機制切出之片）", False),
        4525: ("未判定（residue × 宗地 × 街廓·`residue` 係差集殘餘 ⇒ **可能為 sliver**）", None),
        7368: ("線 × 道路多邊形（非片×片）", False),
        7771: ("線 × 道路多邊形（非片×片）", False),
        8504: ("街廓 × 半平面（`_block_strip` 雙線）⇒ 非 sliver 互切", False),
        8520: ("街廓 × 平行四邊形（`_block_strip` 單線）⇒ 非 sliver 互切", False),
        8618: ("街廓 × 半平面（`_block_partition` 閘③）⇒ 非 sliver 互切", False),
        8619: ("街廓 × 半平面（`_block_partition` 閘③）⇒ 非 sliver 互切", False),
        8620: ("街廓 × 半平面 × 半平面（閘③ 含斥）⇒ 非 sliver 互切", False),
        8624: ("餘塊 × 半平面（`_block_partition` 削餘）⇒ 非 sliver 互切", False),
        8625: ("餘塊 × 半平面（`_block_partition` 削餘）⇒ 非 sliver 互切", False),
        9047: ("🛑 **池片 × 池片**（`_pool_strips_for_block` ②-池閘）＝ **sliver 互切**", True),
        9050: ("🛑 **池片 × 業主宗片**（同閘）＝ **sliver 互切**", True),
        9062: ("🛑 **業主宗片 × 業主宗片**（②-宗 圍堵閘）＝ **sliver 互切**", True),
        9120: ("池幾何 × 18m 負擔範圍（`_pool_overlap_len_s`）＝ **切出之池 × 構造多邊形**"
               "⇒ **一側為 sliver**", None),
        9506: ("鏈式建構 band（非片×片）", False),
        10203: ("線 × 線（求交點）", False),
        10218: ("無限線 × 街廓 exterior", False),
        11009: ("depth 線 × 無限線（街角）", False),
        11379: ("候選宗 × 街角範圍多邊形 ⇒ **一側為宗地多邊形**", None),
        11391: ("候選宗 × 街角範圍多邊形 ⇒ **一側為宗地多邊形**", None),
        16238: ("union 多邊形 × 宗地多邊形（W-A.2 診斷）", None),
    }
    _sliver_risk, _undet = [], []
    for ln, kind, recv, txt in _inter:
        _t, _flag = _CLS.get(ln, ("🔴 **未登錄之呼叫點·須人工判定**", None))
        if _flag is True:
            if ln not in _sliver_risk:
                _sliver_risk.append(ln)
        elif _flag is None:
            if ln not in _undet:
                _undet.append(ln)
        L.append(f"    :{ln:<6} {_t}")
    L.append("")
    L.append(f"  ⚠️ **未判定（須人工複核）** ＝ {_undet}"
             f"　⛔ 不得以「未判定」等同「安全」")
    L.append("")
    L.append(f"  ⇒ **sliver 互切之呼叫點 ＝ {_sliver_risk if _sliver_risk else '（無）'}**")
    if _sliver_risk:
        L.append("  🛑 **停機上呈（§六 第 3 條）**：生產碼存在 sliver 互切之呼叫點，可能同病。")
    else:
        L.append("  ⇒ ✅ **§六 第 3 條停機條件不觸發**——生產碼之 `.intersection()` "
                 "運算元皆為「街廓／餘塊 × 半平面或矩形」，⛔ 無片與片互切。")
        L.append("     （舊閘② 之片×片互切已於 D-2b-15 §d-3 **整條移除**。）")

    L.append("")
    L.append("=" * W)
    txt = "\n".join(L)
    with io.open(LOG, "w", encoding="utf-8") as f:
        f.write(txt + "\n")
    print(txt)
    print(f"\n[written] {LOG}")


if __name__ == "__main__":
    main()
