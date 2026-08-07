# -*- coding: utf-8 -*-
r"""**D-2b-1 §三＋§四**：切換後哨兵（正對照 `==`）＋ 與 D-2b-0 凍存表對帳。

⛔ 禁否定式「與切換前不同即通過」；🔒 每支附**反靜默退路計數器**。

## 五項哨兵

| # | 受測 | 期望 |
|---|---|---|
| (a) | 逐候選真G | D-2b-0 凍存表之新值 |
| (b) | 逐格 winner／強制抵費地 | **13／3**（凍存表：達標翻轉 0、winner 異動 0） |
| (c) | **第 1 宗實配寬度成為定值** | 三深度之**路平行距**互差 ≤ `1e-6` |
| (d) | `3.5m R1/right 628(5)` 之**實配**最小寬 vs `T=7.00` | ≥ 0 ⇒ 「面積過、寬不足構造上不可能」；< 0 ⇒ 🛑 |
| (e) | **第 2 宗**逐格最小寬（**實配**·非指示值） vs 畸零地最小寬 | 只量不處置（D 波界線 #3） |

## 🔒 不變量（§四）

框內重複鍵 ＝ 0（否則 raise）／母體列數印出／**比對欄以欄名指名並印出**。
"""
import io
import math
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
sys.path.insert(0, VERIFY)

from app_harvest import harvest                                     # noqa: E402
import run_verification as rv                                       # noqa: E402
from selection_pipeline import run_corner_pk                        # noqa: E402
from stepg_pipeline import run_step_g                               # noqa: E402

OUTDIR = os.path.join(VERIFY, "out")
LOG = os.path.join(OUTDIR, "probe_D2b1_sentinel.log")
FROZEN = os.path.join(OUTDIR, "probe_D2b_expect_凍存.log")
_SN = {"左": "left", "右": "right"}
TOL_C = 1e-6
COLNAMES = ("真G(㎡)", "門檻(㎡)", "達標", "選中★")


def _u(ax, ay):
    n = math.hypot(ax, ay)
    return (ax / n, ay / n)


def main():                                                    # noqa: C901
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8")
        except Exception:
            pass
    os.makedirs(OUTDIR, exist_ok=True)
    from shapely.geometry import Polygon as _PG
    L = []
    L.append("=" * 200)
    L.append("【D-2b-1 §三＋§四】切換後哨兵（正對照 `==`）＋ 對帳 — ⛔ 禁否定式")
    L.append("=" * 200)

    ns, fake_st = harvest()
    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp_p, build_p, _ = rv.build_build_parcels(
        ns, fake_st, v6, list(cb_by.values()), snapshot)
    fl_by = cad.get("front_lines", {}) or {}
    sd_by = cad.get("side_lines_by_side", {}) or {}
    al_by = cad.get("alloc_dir_by_block", {}) or {}
    legal_w = float(snapshot["global"]["法定最小寬_m"])

    # 🔒 反靜默退路計數：切換是否真的生效（`_first_corner_alloc_dir` 之呼叫次數）
    _hits = {"n": 0}
    _orig_fc = ns["_first_corner_alloc_dir"]

    def _fc_count(side_mid):
        _hits["n"] += 1
        return _orig_fc(side_mid)
    ns["_first_corner_alloc_dir"] = _fc_count

    NOW, WIN, SG = {}, {}, {}
    _SGERR = {}
    try:
        for setback in (0.0, 3.5):
            sb = f"{setback:g}m"
            params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
            _d0, _s2, _o2, _w, _f = run_corner_pk(
                ns, fake_st, list(cb_by.values()), cad, params, temp_p, build_p,
                setback, snapshot=snapshot)
            for _dg in (_d0 or []):
                _tg = _dg.get("真G(㎡)")
                NOW[(sb, str(_dg.get("街廓", "")),
                     _SN.get(str(_dg.get("端", "")).strip(), ""),
                     str(_dg.get("候選地號", "")))] = (
                    (f"{float(_tg):.2f}" if _tg not in ("", None) else "—"),
                    f"{float(_dg.get('門檻(㎡)', 0) or 0):.2f}",
                    ("達標" if str(_dg.get("達標", "")) == "達標" else "未達"),
                    ("★" if str(_dg.get("選中", "")) == "✅" else ""))
            WIN[sb] = {k: dict(v) for k, v in (_w or {}).items()}
            # 🔒 `run_step_g` 失敗**不得吞掉**——記錄其逐字訊息並讓 (c)(d)(e) 標「受阻」，
            #   ⛔ 不以「量測失敗」含糊帶過（no-silent-fallback）。
            try:
                SG[sb] = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot,
                                    params, build_p, _w, _f, setback)
            except Exception as _e_sg:
                SG[sb] = None
                _SGERR[sb] = f"{type(_e_sg).__name__}: {_e_sg}"
    finally:
        ns["_first_corner_alloc_dir"] = _orig_fc

    L.append("")
    L.append("【0】🔒 反靜默退路計數（切換是否真的生效）")
    L.append("-" * 200)
    L.append(f"  `_first_corner_alloc_dir` 被呼叫 **{_hits['n']}** 次")
    L.append("  ⇒ " + ("✅ **切換確實生效**" if _hits["n"] > 0
                       else "🔴 **從未被呼叫 ⇒ 本檔全部結論不可據·停查**"))

    # ══ (a)(§四) 對帳 ═══════════════════════════════════════════════════
    _all = io.open(FROZEN, encoding="utf-8").read().splitlines()
    _s = next((i for i, l in enumerate(_all) if l.startswith("情境    街廓/側     候選")), None)
    if _s is None:
        _s = next(i for i, l in enumerate(_all) if "新真G" in l and "現真G" in l)
    _e = next(i for i, l in enumerate(_all) if "§A-5-2 母體列數" in l)
    EXP = {}
    _dup = 0
    for ln in _all[_s:_e]:
        m = re.match(r"^(0m|3\.5m)\s+(R\d)/(left|right)\s+(\S+)\s+"
                     r"(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s*$", ln)
        if not m:
            continue
        k = (m.group(1), m.group(2), m.group(3), m.group(4))
        if k in EXP:
            _dup += 1
        EXP[k] = (m.group(5), m.group(8), m.group(9))     # 新真G／門檻／新達標
    L.append("")
    L.append("【a／§四】對帳：逐候選 vs **D-2b-0 凍存表**（⛔ 不得改凍存表）")
    L.append("-" * 200)
    L.append(f"  🔒 來源：`{os.path.relpath(FROZEN, REPO)}`　解析框 ＝ 第 {_s + 1}〜{_e} 行")
    L.append(f"  🔒 **比對欄（欄名）**：`{COLNAMES[0]}`（凍存之「新真G」）／`{COLNAMES[1]}`／`{COLNAMES[2]}`")
    L.append(f"  🔒 框內重複鍵 ＝ **{_dup}**（應 0）")
    if _dup:
        raise RuntimeError(f"🔴 框內重複鍵 {_dup} ⇒ 停")
    L.append(f"  🔒 母體列數：凍存 **{len(EXP)}**／現況 **{len(NOW)}**／聯集 **{len(set(EXP) | set(NOW))}**")
    L.append("-" * 200)
    L.append(f"{'情境':<6}{'街廓/側':<12}{'候選':<13}"
             f"{'凍存真G':>10}{'現況真G':>10}{'凍存門檻':>10}{'現況門檻':>10}"
             f"{'凍存達標':>9}{'現況達標':>9}  判")
    L.append("-" * 200)
    _ok = _bad = 0
    _mis = []
    for k in sorted(set(EXP) | set(NOW)):
        e = EXP.get(k)
        n = NOW.get(k)
        if e is None or n is None:
            _bad += 1
            _mis.append((k, str(e), str(n)))
            L.append(f"{k[0]:<6}{k[1] + '/' + k[2]:<12}{k[3]:<13}"
                     f"{(e[0] if e else '—'):>10}{(n[0] if n else '—'):>10}"
                     f"{'—':>10}{'—':>10}{'—':>9}{'—':>9}  🔴 **一側缺列**")
            continue
        _hit = (e[0] == n[0] and e[1] == n[1] and e[2] == n[2])
        if _hit:
            _ok += 1
        else:
            _bad += 1
            _mis.append((k, "／".join(e), "／".join(n[:3])))
        L.append(f"{k[0]:<6}{k[1] + '/' + k[2]:<12}{k[3]:<13}"
                 f"{e[0]:>10}{n[0]:>10}{e[1]:>10}{n[1]:>10}{e[2]:>9}{n[2]:>9}  "
                 f"{'✅' if _hit else '🔴 **不符**'}")
    L.append("-" * 200)
    L.append(f"  ⇒ 相符 **{_ok}**／不符 **{_bad}**")
    if _bad:
        for k, e, n in _mis:
            L.append(f"     🔴 {k[0]} {k[1]}/{k[2]} {k[3]}　凍存 `{e}`　現況 `{n}`")

    # ══ (b) winner／強制抵費地 ═════════════════════════════════════════
    L.append("")
    L.append("【b】逐格 winner／強制抵費地（期望 **13／3**）")
    L.append("-" * 200)
    _nw = _nf = 0
    for sb in ("0m", "3.5m"):
        for lbl in sorted(cb_by):
            for w in ("left", "right"):
                if w not in (sd_by.get(lbl) or {}):
                    continue
                p = ((WIN.get(sb) or {}).get(lbl) or {}).get(
                    "p1_end" if w == "left" else "p2_end")
                if p:
                    _nw += 1
                else:
                    _nf += 1
                L.append(f"  {sb:<6}{lbl + '/' + w:<12}{str(p or '（強制抵費地）')}")
    L.append("-" * 200)
    L.append(f"  ⇒ 有 winner **{_nw}**／強制抵費地 **{_nf}**　"
             f"⇒ {'✅ 命中期望 13／3' if (_nw, _nf) == (13, 3) else '🔴 **未命中**'}")

    # ══ (c)(d)(e) 實配幾何 ════════════════════════════════════════════
    def _widths(row, lbl, which, depths):
        """該宗實配環之**路平行距**（沿 FRONT 方向·同 S1 口徑）於指定深度。"""
        cc = row.get("cut_coords") or []
        if len(cc) < 3:
            return None
        fl = fl_by.get(lbl) or {}
        F1 = (float(fl["p1"][0]), float(fl["p1"][1]))
        F2 = (float(fl["p2"][0]), float(fl["p2"][1]))
        dh = _u(F2[0] - F1[0], F2[1] - F1[1])
        nh = (-dh[1], dh[0])
        cen = cb_by[lbl].get("centroid") or (0.0, 0.0)
        if ((float(cen[0]) - F1[0]) * nh[0] + (float(cen[1]) - F1[1]) * nh[1]) < 0:
            nh = (-nh[0], -nh[1])
        st = [(((float(p[0]) - F1[0]) * dh[0] + (float(p[1]) - F1[1]) * dh[1]),
               ((float(p[0]) - F1[0]) * nh[0] + (float(p[1]) - F1[1]) * nh[1]))
              for p in cc]
        out = []
        for t in depths:
            xs = []
            for i in range(len(st) - 1):
                s0, t0 = st[i]
                s1, t1 = st[i + 1]
                if t0 == t1:
                    continue
                if (t0 - t) * (t1 - t) <= 0.0:
                    xs.append(s0 + (t - t0) / (t1 - t0) * (s1 - s0))
            out.append((max(xs) - min(xs)) if len(xs) >= 2 else float("nan"))
        return out

    L.append("")
    L.append("【c】🔑 **第 1 宗實配寬度成為定值**（三深度之路平行距互差 ≤ 1e-6）")
    L.append("-" * 200)
    L.append(f"{'情境':<6}{'街廓/側':<12}{'第1宗':<13}{'w@0.25D':>12}{'w@0.50D':>12}{'w@0.75D':>12}"
             f"{'極差':>12}  判")
    L.append("-" * 200)
    _cn = _cok = 0
    _d1 = {}
    for sb in ("0m", "3.5m"):
        sg = SG[sb]
        if sg is None:
            L.append(f"{sb:<6}🛑 **`run_step_g` 中止 ⇒ 本情境之 (c) 無法量測**：{_SGERR.get(sb, '')}")
            continue
        by = {str(r.get("暫編地號")): r for r in sg["g_rows"]}
        for lbl in sorted(cb_by):
            for w in ("left", "right"):
                if w not in (sd_by.get(lbl) or {}):
                    continue
                p = ((WIN.get(sb) or {}).get(lbl) or {}).get(
                    "p1_end" if w == "left" else "p2_end")
                if not p:
                    L.append(f"{sb:<6}{lbl + '/' + w:<12}{'—':<13}  無 winner（強制抵費地）")
                    continue
                row = by.get(str(p)) or {}
                _tm = max((((float(v[0]) - 0) * 0 + 0) for v in [(0, 0)]), default=0)
                cc = row.get("cut_coords") or []
                if len(cc) < 3:
                    L.append(f"{sb:<6}{lbl + '/' + w:<12}{str(p):<13}  cut_coords 不足")
                    continue
                fl = fl_by.get(lbl) or {}
                F1 = (float(fl["p1"][0]), float(fl["p1"][1]))
                F2 = (float(fl["p2"][0]), float(fl["p2"][1]))
                dh = _u(F2[0] - F1[0], F2[1] - F1[1])
                nh = (-dh[1], dh[0])
                cen = cb_by[lbl].get("centroid") or (0.0, 0.0)
                if ((float(cen[0]) - F1[0]) * nh[0] + (float(cen[1]) - F1[1]) * nh[1]) < 0:
                    nh = (-nh[0], -nh[1])
                _ts = [((float(v[0]) - F1[0]) * nh[0] + (float(v[1]) - F1[1]) * nh[1])
                       for v in cc]
                _tmax = max(_ts)
                ws = _widths(row, lbl, w, [0.25 * _tmax, 0.50 * _tmax, 0.75 * _tmax])
                if ws is None or any(x != x for x in ws):
                    L.append(f"{sb:<6}{lbl + '/' + w:<12}{str(p):<13}  量測失敗")
                    continue
                _rng = max(ws) - min(ws)
                _cn += 1
                _pass = (_rng <= TOL_C)
                _cok += int(_pass)
                _d1[(sb, lbl, w)] = (str(p), ws, _tmax)
                L.append(f"{sb:<6}{lbl + '/' + w:<12}{str(p):<13}"
                         f"{ws[0]:>12.6f}{ws[1]:>12.6f}{ws[2]:>12.6f}{_rng:>12.9f}  "
                         f"{'✅ 定寬' if _pass else '🔴 **非定寬**'}")
    L.append("-" * 200)
    L.append(f"  ⇒ **定寬 {_cok}/{_cn}**（容差 {TOL_C:g}·**先行宣告**）")

    # (d)
    L.append("")
    L.append("【d】🔑 `3.5m R1/right 628(5)` 之**實配**最小寬 vs `T = 7.00`")
    L.append("-" * 200)
    _t = _d1.get(("3.5m", "R1", "right"))
    if _t is None:
        L.append("  🔴 靶格未取得（無 winner 或量測失敗）")
    else:
        _pid, _ws, _tmax = _t
        _mn = min(_ws)
        _T = 3.5 + legal_w
        L.append(f"  winner ＝ `{_pid}`　三深度寬 ＝ {_ws[0]:.6f} ／ {_ws[1]:.6f} ／ {_ws[2]:.6f}")
        L.append(f"  **實配最小寬 ＝ {_mn:.6f}**　T ＝ {_T:.2f}　⇒ **差 ＝ {_mn - _T:+.6f}**")
        if _mn - _T >= 0:
            L.append("  ✅ **≥ 0** ⇒ 「面積過、寬不足」自此**構造上不可能發生**。")
        else:
            L.append("  🛑 **< 0 ⇒ 停機上呈**（D-② 之前提須重新檢討）。")

    # (e)
    L.append("")
    L.append("【e】**第 2 宗**逐格最小寬（**實配**）vs 畸零地最小寬（⛔ 只量不處置·D 波界線 #3）")
    L.append("-" * 200)
    L.append(f"  🔒 對照 GEO-1 §五 之**指示值**（以現況右界量得·非實配）：")
    L.append("     0m R3/right −1.088138／0m R5/left −0.877844／3.5m R1/right −1.057060／")
    L.append("     3.5m R3/right −0.994436／3.5m R6/right −3.272963")
    L.append("-" * 200)
    L.append(f"{'情境':<6}{'街廓/側':<12}{'第2宗':<13}{'實配最小寬':>13}{'畸零地最小寬':>13}{'差':>12}  判")
    L.append("-" * 200)
    _en = _ebad = 0
    for sb in ("0m", "3.5m"):
        sg = SG[sb]
        if sg is None:
            L.append(f"{sb:<6}🛑 **`run_step_g` 中止 ⇒ 本情境之 (e) 無法量測**：{_SGERR.get(sb, '')}")
            continue
        for lbl in sorted(cb_by):
            for w in ("left", "right"):
                if w not in (sd_by.get(lbl) or {}):
                    continue
                rows = [r for r in sg["g_rows"]
                        if str(r.get("所屬街廓")) == lbl and str(r.get("推進側別")) == w]
                rows.sort(key=lambda r: float(r.get("累積S(m)", 0) or 0))
                if len(rows) < 2:
                    L.append(f"{sb:<6}{lbl + '/' + w:<12}{'—':<13}  該側不足 2 宗")
                    continue
                r2 = rows[1]
                cc = r2.get("cut_coords") or []
                if len(cc) < 3:
                    L.append(f"{sb:<6}{lbl + '/' + w:<12}{str(r2.get('暫編地號')):<13}  cut_coords 不足")
                    continue
                fl = fl_by.get(lbl) or {}
                F1 = (float(fl["p1"][0]), float(fl["p1"][1]))
                F2 = (float(fl["p2"][0]), float(fl["p2"][1]))
                dh = _u(F2[0] - F1[0], F2[1] - F1[1])
                nh = (-dh[1], dh[0])
                cen = cb_by[lbl].get("centroid") or (0.0, 0.0)
                if ((float(cen[0]) - F1[0]) * nh[0] + (float(cen[1]) - F1[1]) * nh[1]) < 0:
                    nh = (-nh[0], -nh[1])
                _ts = [((float(v[0]) - F1[0]) * nh[0] + (float(v[1]) - F1[1]) * nh[1])
                       for v in cc]
                _tmax = max(_ts)
                ws = _widths(r2, lbl, w, [0.02 * _tmax, 0.25 * _tmax,
                                          0.50 * _tmax, 0.75 * _tmax, 0.98 * _tmax])
                ws = [x for x in (ws or []) if x == x]
                if not ws:
                    L.append(f"{sb:<6}{lbl + '/' + w:<12}{str(r2.get('暫編地號')):<13}  量測失敗")
                    continue
                _mn = min(ws)
                _en += 1
                _ebad += int(_mn < legal_w)
                L.append(f"{sb:<6}{lbl + '/' + w:<12}{str(r2.get('暫編地號')):<13}"
                         f"{_mn:>13.6f}{legal_w:>13.2f}{_mn - legal_w:>12.6f}  "
                         f"{'✅' if _mn >= legal_w else '🔴 低於'}")
    L.append("-" * 200)
    L.append(f"  ⇒ **低於畸零地最小寬者 {_ebad}/{_en}**　⛔ **只量不處置**（D 波界線 #3 逐字「D 未解決此項，須另案」）")

    txt = "\n".join(L)
    print(txt)
    with io.open(LOG, "w", encoding="utf-8") as f:
        f.write(txt + "\n")
    print(f"\n→ {os.path.relpath(LOG, REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
