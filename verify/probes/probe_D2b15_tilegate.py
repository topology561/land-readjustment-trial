# -*- coding: utf-8 -*-
r"""**D-2b-15 §d-0／§d-1／§d-2／§d-4**：鋪滿閘② 量法失效之實證、複現條件、新舊對拍。"""
import io
import math
import os
import random
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
sys.path.insert(0, VERIFY)
sys.path.insert(0, os.path.join(VERIFY, "fixtures"))

from app_harvest import harvest                                     # noqa: E402
import case_D2b15_tilegate_intersection as C                        # noqa: E402

OUTDIR = os.path.join(VERIFY, "out")
LOG = os.path.join(OUTDIR, os.environ.get("WV_TILE_LOG", "probe_D2b15_tilegate.log"))
TOL = 1e-6
W = 200


def _u(v):
    n = math.hypot(v[0], v[1])
    return (v[0] / n, v[1] / n)


def _old_gate(pieces):
    """**已作廢**之舊判準（最大兩兩 `.intersection()` 面積）——僅供對拍，⛔ 非生產。"""
    mx, pair = 0.0, None
    for i in range(len(pieces)):
        for j in range(i + 1, len(pieces)):
            if pieces[i].is_empty or pieces[j].is_empty:
                continue
            x = float(pieces[i].intersection(pieces[j]).area)
            if x > mx:
                mx, pair = x, (i, j)
    return mx, pair


def main():                                                        # noqa: C901
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8")
        except Exception:
            pass
    os.makedirs(OUTDIR, exist_ok=True)
    import numpy as np
    from shapely.geometry import Polygon

    ver = subprocess.run(
        [sys.executable, "-c",
         "import shapely; print('shapely', shapely.__version__, '| GEOS', shapely.geos_version)"],
        capture_output=True, text=True).stdout.strip()

    ns, _ = harvest()
    part = ns["_block_partition"]
    hp = ns["_strip_halfplane"]
    L = []
    L.append("=" * W)
    L.append(f"【D-2b-15】鋪滿閘② 量法失效：實證／複現條件／新舊對拍　| §d-0 環境：{ver}")
    L.append("=" * W)
    L.append(f"  §d-0 對照值（claude.ai 側）：`shapely 2.1.2 | GEOS (3, 13, 1)`"
             f"　⇒ **{'環境一致' if '2.1.2' in ver and '3, 13, 1' in ver else '🔴 環境不同'}**")

    poly = Polygon(C.BLOCK)
    # ══ §d-1 修前行為（⛔ 改碼前之實測·此處引 fixture 所存逐字）══
    L.append("")
    L.append("【§d-1】修前行為（`bf91181`·⛔ 改碼**之前**實跑所得·逐字）")
    L.append("-" * W)
    L.append(f"  raise 與否：**{C.PRE_FIX_RAISES}**")
    L.append(f"  訊息全文：{C.PRE_FIX_MESSAGE}")
    L.append(f"  片對 ＝ {C.PRE_FIX_BAD_PAIR}　交集 ＝ {C.PRE_FIX_BAD_OVERLAP!r}")
    L.append("  ⚠️ `diag` **無法取得**——舊碼於閘② `raise` 時**不回傳 diag**"
             "（此亦為修前行為之一部分·⛔ 不以事後重算冒充當時 diag）")
    L.append(f"  街廓面積實測 ＝ {poly.area!r}　（fixture 參考 {C.BLOCK_AREA_REF}）")

    # ══ §d-3 三項判準於本案例之實測 ══
    L.append("")
    L.append("【§d-3／§d-4-1】新判準三項於本回歸案例之實測")
    L.append("-" * W)
    pieces, diag = part(poly, C.D_HAT, C.LINES, _label="D2b15")
    L.append(f"  ① 總量恆等 `|Σ片 − 街廓|` ＝ **{abs(diag['resid']):.9e}**　(≤{TOL:g}) ✅")
    L.append(f"  ② 逐步恆等 max `|片−(rem₋₁−rem)|` ＝ **{diag['max_chain_resid']:.9e}** ✅")
    L.append(f"  ③ 互補 max `|hp⁻∩hp⁺|` ＝ **{diag['max_compl_both']:.9e}**"
             f"／max 未覆蓋 gap ＝ **{diag['max_compl_gap']:.9e}** ✅")
    L.append("  逐步面積鏈（⛔ 逐列實測）：")
    for c in diag['chain']:
        L.append(f"    步{c['i']}: rem₋₁ {c['prev']:.6f}　片 {c['piece']:.6f}"
                 f"　rem {c['rem']:.6f}　|resid| {c['resid']:.3e}")
    L.append(f"  各片面積 ＝ {[round(a, 6) for a in diag['areas']]}")
    L.append(f"  fixture 參考鏈 ＝ {C.AREA_CHAIN_REF}")
    _old, _pair = _old_gate(pieces)
    L.append(f"  🔴 **舊判準若仍在**：最大兩兩 `.intersection()` ＝ **{_old!r}**（片對 {_pair}）")
    L.append(f"     ——恰等於**片{_pair[1]} 之全部面積** {diag['areas'][_pair[1]]!r}"
             f" ⇒ `.intersection()` 把整片當成交集")
    # 帶號與 contains 雙重佐證
    _q3 = np.asarray(C.LINES[3][0], float); _g3 = np.asarray(C.LINES[3][1], float)
    _g3 = _g3 / np.linalg.norm(_g3)
    _dh = np.asarray(C.D_HAT, float); _dh = _dh / np.linalg.norm(_dh)
    _w3 = _dh - float(np.dot(_dh, _g3)) * _g3
    _w3 = _w3 / np.linalg.norm(_w3)
    _p = np.asarray(C.SAMPLE_PT, float)
    _f = float(np.dot(_p - _q3, _w3))
    from shapely.geometry import Point
    L.append(f"  🔒 **雙重佐證（分割正確）**：取樣點 {C.SAMPLE_PT}")
    L.append(f"     帶號 `f(L3) = (p−q₃)·ŵ₃` ＝ **{_f:+.6f}**"
             f"（fixture 參考 {C.SAMPLE_F_L3_REF:+.6f}）⇒ ≥0 ⇒ 屬餘塊、**不屬片2**")
    L.append(f"     `片2.contains(取樣點)` ＝ **{pieces[2].contains(Point(*C.SAMPLE_PT))}**")
    L.append("     ⇒ **分割正確、量法失效**（⛔ 非「依序削餘失敗」）")

    # ══ §d-2 複現條件查明 ══
    L.append("")
    L.append("【§d-2】複現條件查明：D-2b-14 之 710 例為何未涵蓋")
    L.append("-" * W)
    _th = []
    for q, g in C.LINES:
        gg = _u(g)
        _th.append(math.degrees(math.acos(min(1.0, abs(gg[0] * _dh[0] + gg[1] * _dh[1])))))
    _th = [90.0 - t if t > 45 else t for t in _th]
    L.append(f"  本案例六線與 d̂ 之夾角（實算）＝ {[round(t, 6) for t in _th]}")
    L.append(f"  fixture 參考 ＝ {C.THETA_DEG_REF}")
    L.append(f"  ⇒ **全部淺角**（{min(_th):.3f}°–{max(_th):.3f}°）且**組內散布 {max(_th) - min(_th):.3f}°**")
    L.append("  🔑 **對照 D-2b-14 之掃描**：其固定 θ 於各級距、組內僅 `θ×uniform(0.85,1.15)` 之擾動")
    L.append("     ⇒ 於 θ=3° 檔，組內散布僅 ±0.45°（約 0.9° 全幅）")
    L.append("     ⇒ **從未產生「淺角 ＋ 組內散布數度」之組態** ⇒ 未涵蓋。")
    L.append("  ⇒ 以下實測該假說：固定平均淺角、**掃描組內散布幅度**")
    rng = random.Random(20260809_15)
    L.append(f"    {'平均θ(°)':>10}{'散布(±°)':>10}{'例數':>6}{'舊判準破':>10}{'新判準破':>10}  判讀")
    _hit_cfg = []
    for _mean in (3.0, 6.0, 9.0, 20.0, 45.0):
        for _spr in (0.5, 2.0, 5.0, 9.0):
            _n = _obad = _nbad = 0
            for _rep in range(25):
                _ang = rng.uniform(0, 2 * math.pi)
                dh2 = np.array(_u((math.cos(_ang), math.sin(_ang))))
                k = 5
                sv = sorted(rng.uniform(-140.0, 140.0) for _ in range(k + 1))
                dirs = [_u((math.cos(_ang + math.radians(_mean + rng.uniform(-_spr, _spr))),
                            math.sin(_ang + math.radians(_mean + rng.uniform(-_spr, _spr)))))
                        for _ in range(k + 1)]
                base = np.array([0.0, 0.0])
                qs = [base + s * dh2 for s in sv]
                ln = list(zip([tuple(map(float, q)) for q in qs], dirs))
                try:
                    pc, dg = part(poly, dh2, ln, _label="scan")
                except RuntimeError:
                    _nbad += 1
                    continue
                _n += 1
                _o, _pp = _old_gate(pc)
                if _o > TOL:
                    _obad += 1
                    if len(_hit_cfg) < 3:
                        _hit_cfg.append((_mean, _spr, _o, _pp))
            L.append(f"    {_mean:>10.1f}{_spr:>10.1f}{_n + _nbad:>6}{_obad:>10}{_nbad:>10}"
                     f"  {'🔑 **舊判準誤報**' if _obad else '—'}")
    L.append(f"  ⇒ 舊判準誤報之組態樣本：{[(m, s, round(o, 4), p) for m, s, o, p in _hit_cfg]}")
    L.append("")
    L.append("  🔴 **判讀更正（⛔ 不得寫成「淺角＋散布」）**——實測與該假說**不符**：")
    L.append("     誤報出現於平均 θ ＝ **3°／9°／20°／45°**（含 **45°·絕非淺角**），")
    L.append("     且**皆在散布 ≥5°** 之列 ⇒ **「淺角」不是判別式**，共同項是**組內散布**。")
    L.append("  🔑 **且本掃描之街廓＝<u>本回歸案例之街廓</u>**（⛔ 非 D-2b-14 之隨機母體）：")
    L.append("     D-2b-14 於 θ=45° 檔之組內散布達 ±6.75°（`θ×uniform(0.85,1.15)`）、")
    L.append("     θ=90° 檔達 ±13.5°，**皆 ≥5°**，卻 **0 不一致** ⇒ **散布亦非充分條件**。")
    L.append("  ⇒ **「D-2b-14 為何未涵蓋」之答**：其**街廓母體**與本案例**不同**——")
    L.append("     本現象在**本案例之街廓**上以散布 ≥5° 即可觸發，於 D-2b-14 之隨機母體上"
             "**跨 0.01°–90° 全域、含大散布皆未觸發** ⇒ **觸發條件繫於<u>街廓幾何本身</u>**，")
    L.append("     ⛔ **非**單由界線角度組態決定。")
    L.append("  ⚠️ **確切之街廓幾何特徵：未查明**（⛔ 不推定）。已排除之候選：")
    L.append("     · 版本差異 —— §d-0 環境**一致**；")
    L.append("     · 單純淺角 —— D-2b-14 已掃 0.01°–90° 全域、0 不一致；")
    L.append("     · 界線未排序 —— D-2b-14 補掃 80 例、0 不一致；")
    L.append("     · 組內散布本身 —— D-2b-14 之大散布檔亦 0 不一致（見上）。")

    # ══ §d-4-3 新舊對拍（既有難幾何母體）══
    L.append("")
    L.append("【§d-4-3】新舊判準對拍（既有難幾何母體·⛔ 母體非空）")
    L.append("-" * W)

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

    _both_ok = _old_only_bad = _new_only_bad = _tot = 0
    _newbad_ex = []
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
                _tot += 1
                _newbad = False
                try:
                    pc, dg = part(pp, dh2, ln, _label="cmp")
                except RuntimeError as e:
                    _newbad = True
                    if len(_newbad_ex) < 3:
                        _newbad_ex.append(str(e)[:130])
                    pc = None
                if pc is None:
                    _new_only_bad += 1
                    continue
                _o, _pp2 = _old_gate(pc)
                if _o > TOL:
                    _old_only_bad += 1
                else:
                    _both_ok += 1
    L.append(f"  母體 ＝ **{_tot}** 例（⛔ 非空）")
    L.append(f"  **舊破而新過**（＝舊判準誤報·新判準修掉者）＝ **{_old_only_bad}** 例")
    L.append(f"  **新破**（不論舊如何）＝ **{_new_only_bad}** 例"
             + ("　🛑 **須查是否為漏報之反面**" if _new_only_bad else ""))
    L.append(f"  兩者皆過 ＝ **{_both_ok}** 例")
    for e in _newbad_ex:
        L.append(f"    🔴 新判準破之例：{e}")
    L.append("  🔒 **停機條件（§七 第 3 條）＝「舊過而新破」**："
             + ("⚠️ 見上列新破之例，須逐例確認舊是否為過" if _new_only_bad
                else "**0 例** ⇒ ✅ 不觸發"))

    L.append("")
    L.append("=" * W)
    txt = "\n".join(L)
    with io.open(LOG, "w", encoding="utf-8") as f:
        f.write(txt + "\n")
    print(txt)
    print(f"\n[written] {LOG}")


if __name__ == "__main__":
    main()
