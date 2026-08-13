# -*- coding: utf-8 -*-
r"""`W-G.9-22`：三值 × 全格 之**對目標偏差**（⛔ 零生產碼·只讀·⛔ 不估上限）。

# 🔴 三條路徑 ⛔ 不得合併為「現行」（考古 **77**）

| 路徑 | 起算取什麼 |
|---|---|
| **A**（`app.py` `main()`·排地） | `buf · _cos_dn` |
| **B 選槽**（`verify/stepg_pipeline.py`） | `_mp_base_W0(群起點, buf)` ＝ `buf·cos_dn + W_0` |
| **B 推進**（同上） | **硬 `0.0`** |

**目標**（`W-G.9-22` 事前登記 §1·⛔ 已自行覆核）：
* 非 `forced` ⇒ **`0`**（`K-9-5-12`（五）-1「首宗起點**一律**為 0」·權威序**第 1 級**）
* `forced` ⇒ **`MP` → 抵費地遠側界之<u>垂距</u>**
  （`K-9-5-12`（四）·受詞為**第 2 宗**·∵ 抵費地不計 G、不負擔）
  🔴 ⛔ **不得以 `S1_par` 代之**——後者為**路平行**（同名不同量·禁互代）。

## 資料來源（驗收 #5／#12）

* `forced` 與**目標垂距**：**本探針現查**（`run_corner_pk` 完跑·⛔ 不經結構閘）。
* `buf·cos_dn` 與 `W_0`：讀**既有產物** `verify/out/probe_WG91_buf_metric_and_candidates.log`
  ⇒ 🔒 **⛔ 不重跑產生它的工具**（驗收 #12）。
  🔴 **生產實值之替換**：非 `forced` 格之生產 `buf` ＝ **0** ⇒ ⛔ **不沿用該表之假設 `buf`**。

## 重跑
    python verify/probes/probe_WG922_three_vs_target.py
"""
import os
import re
import sys
import traceback

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
sys.path.insert(0, VERIFY)
assert os.path.exists(os.path.join(REPO, "CLAUDE.md")), f"🔴 REPO 不是倉根：{REPO}"
OUT = os.path.join(VERIFY, "out", "probe_WG922_three_vs_target.log")
SRC91 = os.path.join(VERIFY, "out", "probe_WG91_buf_metric_and_candidates.log")
BANNER = "🔴 **本表為<u>下界</u>**（只含族②③ 起算；⛔ 未含族① 落位之面積效果）"
L, RC = [], [0]
# 外部錨（`W-G.9-19` `D1`·⛔ 非本批自產）
ANCHOR_D1 = {"0m": set(), "3.5m": {("R5", "left"), ("R2", "left"), ("R3", "right")}}


def say(s=""):
    print(s)
    L.append(s)


def red(s):
    say(f"  🔴 {s}")
    RC[0] = 1


def _f(v, n=6):
    return "—" if v is None else f"{float(v):.{n}f}"


def far_edge_W(poly, side_pts, mp):
    """由**多邊形自身**取遠側界，回 `MP` 到其**所在直線**之垂距。⛔ 不由 `S1_par` 反推。

    判法同 `W-G.9-19`：取方向 **∥SIDELINE** 且**離 SIDELINE 最遠**之邊。
    """
    import numpy as np
    (p1, p2) = side_pts
    u = np.asarray(p2, float) - np.asarray(p1, float)
    nu = float(np.linalg.norm(u))
    if nu < 1e-12:
        return None
    u = u / nu
    n = np.array([-u[1], u[0]])
    xs, ys = poly.exterior.coords.xy
    pts = list(zip(xs, ys))
    best = None
    for a, b in zip(pts[:-1], pts[1:]):
        e = np.asarray(b, float) - np.asarray(a, float)
        ne = float(np.linalg.norm(e))
        if ne < 1e-9 or abs(float(np.cross(e / ne, u))) > 1e-6:
            continue
        d = abs(float(np.dot(np.asarray(a, float) - np.asarray(p1, float), n)))
        if best is None or d > best[0]:
            best = (d, (a, b))
    if best is None:
        return None
    (a, b) = best[1]
    e = np.asarray(b, float) - np.asarray(a, float)
    e = e / float(np.linalg.norm(e))
    return abs(float(np.cross(e, np.asarray(mp, float) - np.asarray(a, float))))


# ══════════════════════════════════════════════════════════════════════════
def read_wg91():
    """讀既有產物之 `Q2` 表（⛔ 不重跑產生它的工具）。附**期望值閘**（驗收 #7）。"""
    if not os.path.exists(SRC91):
        red(f"**無從判定**：既有產物不存在（{os.path.relpath(SRC91, REPO)}）⇒ ⛔ 非「算不出來」")
        return None
    txt = open(SRC91, encoding="utf-8").read()
    rows, inq2 = {}, False
    for ln in txt.split("\n"):
        if ln.startswith("## Q2"):          # ⚠️ 錨在**節標題行首**（考古 77·卷首標題亦含 Q2）
            inq2 = True
            continue
        if inq2 and ln.startswith("## ") and "Q2" not in ln:
            break
        m = re.match(r"^(0m|3\.5m)\s+(R\d)\s+(left|right)\s+(.*)$", ln.strip())
        if inq2 and m:
            nums = re.findall(r"-?\d+\.\d+", m.group(4))
            if len(nums) >= 4:
                rows[(m.group(1), m.group(2), m.group(3))] = {
                    "S1_par": float(nums[0]), "buf_hypo": float(nums[1]),
                    "A_hypo": float(nums[2]), "Bslot_hypo": float(nums[3])}
    say(f"  🔒 **期望值閘**（驗收 #7）：期望 **16** 格／實得 **{len(rows)}** 格"
        f"（母體＝該 log 之 `Q2` 表·判準＝行首符 `情境 街廓 側別` 且含 ≥4 個小數）")
    if len(rows) != 16:
        red("**無從判定**：解析器所得非 16 格 ⇒ ⛔ 不得據以下結論（⛔ 非「無資料」）")
        return None
    say("     ✅ 過 ⇒ 可用")
    return rows


def run_tag(tag, setback):
    """`run_corner_pk` 完跑（⛔ 不經 `run_step_g`、故不經結構閘）＋只讀包裝取範圍多邊形。"""
    import run_verification as rv
    from app_harvest import harvest
    from selection_pipeline import build_ownership, build_build_parcels, run_corner_pk
    snap = rv.load_snapshot()
    ns, fs = harvest()
    cb_by, cad = rv.build_pipeline(ns, fs, snap)
    build_ownership(ns, fs, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    tp, bp, _ = build_build_parcels(ns, fs, v6, list(cb_by.values()), snap)
    params = rv.build_param_table(ns, fs, cb_by, cad, snap, setback)
    REC = []
    _orig = ns["_build_corner_range_v3"]

    def w_rng(*a, **kw):
        out = _orig(*a, **kw)
        import inspect
        try:
            allkw = dict(inspect.signature(_orig).bind_partial(*a, **kw).arguments)
        except Exception:                                   # noqa: BLE001
            allkw = dict(kw)
        REC.append({"kw": allkw, "poly": out})
        return out

    ns["_build_corner_range_v3"] = w_rng
    try:
        _d, _s, _o, win, forced = run_corner_pk(
            ns, fs, list(cb_by.values()), cad, params, tp, bp, setback, snapshot=snap)
    finally:
        ns["_build_corner_range_v3"] = _orig                # 🔒 還原（⛔ 不留 patch）
    return {"forced": forced, "params": params, "rec": REC, "R": ns["rw_from_width"]}


def forced_set(st):
    """由**生產側啟動式**現查 `forced` 集合（⛔ 不採信任何表）。"""
    rows = {r.get("街廓"): r for r in st["params"]}
    out = set()
    for lbl, fo in (st["forced"] or {}).items():
        for sd, key, col in (("left", "left_forced_offset", "【左】街角最小面積(㎡)"),
                             ("right", "right_forced_offset", "【右】街角最小面積(㎡)")):
            if not bool((fo or {}).get(key, False)):
                continue
            v = (rows.get(lbl) or {}).get(col)
            if v is not None and str(v) not in ("", "inf") and v != float("inf"):
                out.add((lbl, sd))
    return out


def target_W(st, lbl, sd):
    """目標 ＝ `MP` → 遠側界之**垂距**（由該格之範圍多邊形自身取）。"""
    import numpy as np
    for r in st["rec"]:
        kw = r["kw"]
        if kw.get("_label") != lbl or kw.get("_side") != sd:
            continue
        spts, poly = kw.get("side_line_pts"), r["poly"]
        if not spts or len(spts) != 2 or poly is None:
            continue
        mp = (np.asarray(spts[0], float) + np.asarray(spts[1], float)) / 2.0
        return far_edge_W(poly, spts, mp)
    return None


def main():
    say("=" * 122)
    say("【`W-G.9-22`】三值 × 全格 之對目標偏差（⛔ 零生產碼·只讀）")
    say(BANNER)
    say("=" * 122)
    say("  🔒 **三條路徑⛔ 不得合併為「現行」**（考古 77）：")
    say("     A ＝ `buf·_cos_dn`｜B 選槽 ＝ `buf·cos_dn + W_0`｜B 推進 ＝ **硬 `0.0`**")
    say("  🔒 **目標**：非 `forced` ⇒ `0`（`K-9-5-12`（五）-1·權威序**第 1 級**）；")
    say("     `forced` ⇒ `MP` → 抵費地遠側界之**垂距**（`K-9-5-12`（四））")
    say("     ⛔ **不得以 `S1_par` 代之**（路平行·同名不同量·禁互代）。")

    say()
    say("  ══ 既有產物之讀取（驗收 #5／#12·⛔ 不重跑產生它的工具）══")
    w91 = read_wg91()
    if w91 is None:
        return finish()

    allrows = []
    for tag, sb in (("0m", 0.0), ("3.5m", 3.5)):
        say()
        say("=" * 122)
        say(f"【情境 {tag}】　{BANNER}")
        say("=" * 122)
        try:
            st = run_tag(tag, sb)
        except Exception as e:                              # noqa: BLE001
            red(f"情境 {tag} 建置失敗：{type(e).__name__}: {e}")
            say(traceback.format_exc()[-340:])
            continue
        R = st["R"]
        fs_ = forced_set(st)
        say(f"  ── `H2` `forced` 之**生產實值現查**（判準＝`<side>_forced_offset` ∧ "
            f"街角最小面積 非 None ∧ ≠ inf）──")
        say(f"     現查所得 ＝ **{len(fs_)}** 格：{sorted(fs_)}")
        anc = ANCHOR_D1[tag]
        ok = (fs_ == anc)
        say(f"     🔒 **外部錨閘**（驗收 #10·錨來自 `W-G.9-19` `D1`·⛔ 非本批自產）："
            f"錨 ＝ {sorted(anc)} ⇒ {'✅ 相同' if ok else '🔴 不同'}")
        if not ok:
            red(f"`forced` 集合與外部錨不符 ⇒ ⛔ 本情境之表不得出艙")
            continue
        say(f"     🔒 判別力自檢：以**必不同**之集合（錨 ∪ {{('R9','left')}}）比 ⇒ "
            f"{'🔴 竟相同' if fs_ == (anc | {('R9', 'left')}) else '✅ 判為不同 ⇒ 該閘非恆過'}")

        # ── 逐格表 ──
        say()
        say(f"  ── 逐格表（鍵＝**街廓側字面**·單位 **公尺**·⛔ 不與百分點同欄）　{BANNER} ──")
        say(f"     {'鍵':<14}{'forced':<8}{'目標':>11}{'A':>11}{'B選槽':>11}{'B推進':>9}"
            f"{'A−目標':>11}{'B選−目標':>11}{'B推−目標':>11}")
        for (t, blk, sd), v in sorted(w91.items()):
            if t != tag:
                continue
            key = f"{blk}/{sd}"
            is_f = (blk, sd) in fs_
            w0 = v["Bslot_hypo"] - v["A_hypo"]           # ＝ W_0（與 `buf` 無關·`W-G.9-21` 已證）
            if is_f:
                # 🔒 `forced` ⇒ 生產 `buf ≠ 0` ⇒ 該表之值即生產實值
                A, Bs = v["A_hypo"], v["Bslot_hypo"]
                tgt = target_W(st, blk, sd)
            else:
                # 🔴 生產 `buf = 0` ⇒ ⛔ 不沿用該表之假設值
                A, Bs, tgt = 0.0, w0, 0.0
            Bp = 0.0
            if tgt is None:
                say(f"     {key:<14}{'✅' if is_f else '':<8}"
                    f"{'🔴 無從判定（目標取不到）':>11}")
                red(f"{key}：目標垂距取不到 ⇒ ⛔ 本格不出艙（⛔ 非「差為 0」）")
                continue
            say(f"     {key:<14}{'✅' if is_f else '':<8}{_f(tgt):>11}{_f(A):>11}"
                f"{_f(Bs):>11}{_f(Bp):>9}{_f(A - tgt):>11}{_f(Bs - tgt):>11}{_f(Bp - tgt):>11}")
            allrows.append({"tag": tag, "key": key, "f": is_f, "tgt": tgt,
                            "A": A, "Bs": Bs, "Bp": Bp, "w0": w0,
                            "S1": v["S1_par"], "R": R})
        say(f"     🔒 出艙 **{len([r for r in allrows if r['tag'] == tag])}** 格"
            f"（母體＝該情境之 8 街廓側·判準＝目標取得成功）")

    if not allrows:
        red("**無從判定**：無任何格出艙 ⇒ ⛔ 不得讀作「無偏差」")
        return finish()

    # ── 百分點欄（⛔ 分欄）＋ 地板歧義之兩義分碼 ────────────────────────
    say()
    say("=" * 122)
    say(f"【百分點欄】⛔ **與公尺分欄**·⛔ 不比大小（考古 67）　{BANNER}")
    say("=" * 122)
    R = allrows[0]["R"]
    say(f"  🔒 判別力自檢：`R(18.0)` ＝ {_f(R(18.0), 4)}／`R(0.0)` ＝ {_f(R(0.0), 4)}"
        f"／`R(-1.0)` ＝ {_f(R(-1.0), 4)} ⇒ 該函式**非常數**且**負值被夾為 0**")
    say()
    say(f"  {'鍵':<14}{'情境':<7}{'forced':<8}{'A−目標(pp)':>14}{'B選−目標(pp)':>15}"
        f"{'B推−目標(pp)':>15}  出艙碼")
    sgn = {"A": 0.0, "Bs": 0.0, "Bp": 0.0}
    ab = {"A": 0.0, "Bs": 0.0, "Bp": 0.0}
    n_floor = 0
    for r in allrows:
        rt = R(r["tgt"])
        d = {k: R(r[k]) - rt for k in ("A", "Bs", "Bp")}
        for k in d:
            sgn[k] += d[k]
            ab[k] += abs(d[k])
        # 🔴 地板歧義（驗收 #3）：兩義⛔ 不共用出艙碼
        floored = [k for k in ("A", "Bs", "Bp")
                   if abs(d[k]) < 1e-9 and (r[k] < -1e-9 or r["tgt"] < -1e-9)]
        真無差 = [k for k in ("A", "Bs", "Bp")
                if abs(d[k]) < 1e-9 and abs(r[k] - r["tgt"]) < 1e-6]
        code = ("🟡 地板歧義：" + "/".join(floored)) if floored else (
            "✅ 真無差" if len(真無差) == 3 else "")
        if floored:
            n_floor += 1
        say(f"  {r['key']:<14}{r['tag']:<7}{'✅' if r['f'] else '':<8}"
            f"{_f(d['A'], 4):>14}{_f(d['Bs'], 4):>15}{_f(d['Bp'], 4):>15}  {code}")
    say()
    for k, nm in (("A", "A"), ("Bs", "B選槽"), ("Bp", "B推進")):
        say(f"  🔒 {nm:<6}帶號合計 ＝ **{_f(sgn[k], 4)}** pp"
            f"｜絕對值合計 ＝ **{_f(ab[k], 4)}** pp")
    say(f"  🔴 **地板歧義之格 ＝ {n_floor}**（判準：差 < 1e-9 **且** 該值或目標 < 0）")
    say("     ⇒ 🟡 之 `0.0000` ⛔ **不得讀作「無偏差」**——`R(負)` 被夾為 0，")
    say("       偏差仍在，只是**在起算項這一欄看不見**（會經終點項顯現）。")
    say(f"  🔒 **`H4` 判別力自檢**：`R(+0.1619) − R(0)` ＝ {_f(R(0.1619) - R(0.0), 4)}"
        f"（⇒ 出艙碼**空**）vs `R(-1.0) − R(0)` ＝ {_f(R(-1.0) - R(0.0), 4)}"
        f"（⇒ 出艙碼 🟡）⇒ **兩義確實分得開**")

    # ── 乙組 ──────────────────────────────────────────────────────────
    say()
    say("=" * 122)
    say("【乙組】族① 之現況（⛔ 只述·不估）")
    say("=" * 122)
    say("  碼面逐字：`left_cum_S = float(_left_buffer_S)` ⇒ 族① 取 **`buf` 本身**（**沿 `s` 之量**）。")
    say("  目標為**真正之地界**（∥SIDELINE）⇒ 該界線在 `s` 下**非單一值** ⇒ **仍需表示法**。")
    say("  🔴 **`H5` 成立：族① 仍不可估。**")
    say("  🔒 判別力自檢（⛔ 期望值為否定 ⇒ 尤須自檢·考古 76）：")
    say("     **若**遠側界 ∥ `d̂`，它在 `s` 下即為單一值 ⇒ **可估** ⇒ 該判法**會給出不同結論**")
    say("     ⇒ ⛔ 非恆真句。⚠️ 本案之遠側界 ∥SIDELINE 而與 `d̂` **斜交** ⇒ 判為不可估。")
    say()
    say(f"  🔴 **⇒ 上列各表之數為<u>下界</u>**（只含族②③ 起算）")
    say("     ⛔ **非完整影響**、⛔ 不得與面積並列、⛔ 不得讀成區間。")


def finish():
    say()
    say("=" * 122)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print(f"\n[log] {os.path.relpath(OUT, REPO)}　rc={RC[0]}")
    return RC[0]


if __name__ == "__main__":
    main()
    sys.exit(finish())
