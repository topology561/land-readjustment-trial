# -*- coding: utf-8 -*-
"""W-G.9-395 量測器（發單端擬·檔 F39·⛔ 由受單側改一字）：末端塊之競合之二形（`K-9-60` ①③·KL 裁 `2026-10-05 22:59`；
KL `2026-10-25 03:58`「二是、三丙」·`10:13`·`10:18`「一甲、二甲」）＋ 取得即鎖定之於末端塊之合併再試（`K-9-80`）。

所量之性質：
  ① 一筆土地同時跨占同一街廓二端之末端塊範圍（二端皆無側街）：二端各依原位次試；只一端拿得下 ⇒ 歸該端；二端皆拿得下
     ⇒ 歸落於範圍內面積（取至 2 位）大之一端，相同 ⇒ 左端（p1 側）；他端視為未被此筆跨占（除之而重選·以暫編地號）；
     一端之當選見於他端之列而為「未達」者 ⇒ 其列「歸他端」（合併再試⛔ 以之為候選）。二端皆拿不下而皆入合併再試者 ⇒
     其群為 `K-9-50` 題二之競合（⛔ 停機）。
  ③ 同一末端塊屬二以上之競合：該端仍依原位次，輪到者始處理其競合；二位以上地主互相等待（二端之原位次相反·成環）⇒
     環中序鍵最小者先處理——序鍵 ＝ 該群於其二端之未達候選（街廓內之土地）之試算 G 之和 → 重劃前面積之和 → 最小之暫編地號
     （`k967_rank`）；其餘依原位次續行。
  鎖 各端之當選者⛔ 為他端之合併再試所併。

子命令（一律 python3 verify/probes/probe_WG9395_k960.py <子命令> …）：
  selftest <repo>
           合成對照（⛔ 讀本案資料·`harvest(app.py)` 取諸函式·期值皆手算）。
           甲（`end_block_apply`·玩具街廓：FRONT 沿 x 軸 p1 ＝ (0,0) → p2 ＝ (L,0)、宗地分配線 ∥ y 軸、深 30、畸零地寬 3.5·二端皆
           無側街·R_end 各 105）：
           T1 X 跨二端（左交 45、右交 75）而唯左拿得下 ⇒ X 歸左、右強制抵費地、右之 X 之列「歸他端」（⛔ 先比面積而唯右試）；
           T2 二端皆拿得下、右交大 ⇒ X 歸右；左除 X 而重選（A 未達 ⇒ 強制抵費地）、左之列 ＝ [A 未達, X 歸他端]；
           T3 二端皆拿得下、交相等（75／75）⇒ X 歸左；T4 左交大（75／45）⇒ 歸左；
           T5 二端皆拿不下 ⇒ 二端皆強制抵費地、X 之列二端皆「未達」；T6 左之 A 先當選（X 未試）、右 X 當選 ⇒ 二端各一；
           T7 一宗之街廓（長 20·X 滿之）·准強制 ⇒ X 歸左、右強制；⛔ 准 ⇒ 停機、訊息含「各筆單獨試算皆未達」與「right」；
           T8 同一原地號之二片 X(1)、X(2)：X(1) 為二端之當選而歸右；左除 X(1) 而重選 ⇒ X(2) 當選（⛔ 以原地號除）；右之 X(2) 之列
              「歸他端」；
           T9 換名、旋轉 37°、鏡射、TWD97 之尺度：T1〜T4、T8 之結果除名稱外同；T10 左右互換（FRONT 反向）⇒ 結果左右互換；
           T11 無同時跨占者（長 40·各宗皆不跨二端）⇒ 同改前（二端各當選·「歸他端」之列 0）。
           乙（`end_block_merge_run`〔其內 `k6b_stage3_run` 為真〕·玩具同 F13 之法：`alloc_eval` 依所給之候選序評選、G ＝
           分攤登記面積 ＋ 面積）：
           U1 一筆 Z1(1) 為同一街廓二端之未達候選 ⇒ 題二之競合（⛔ 停機）：二端皆以同街廓之 Z2(1) 拿得下、右交大 ⇒ 歸右、
              左皆未達；
           U2 取得即鎖定：右端之當選 Z2(1) 與左端之未達候選 Z1(1) 同群相連 ⇒ 左之合併再試⛔ 併 Z2(1)（左皆未達）；
           V0 一端屬二競合而二端之順序一致（丁、戊）⇒ 依原位次（丁先）·⛔ 停機；
           V1 二端之順序相反（E：丁先·F：戊先）⇒ 互相等待 ⇒ 序鍵（G 之和 戊 81 ＞ 丁 63）⇒ 戊先：戊得 E、F 強制抵費地
              （⛔ 以交面積之和〔丁 70 ＞ 戊 40〕、⛔ 以街廓之名）；
           V2 G 之和（戊 72 ＞ 丁 63）與最大之一片（丁 50 ＞ 戊 36）異 ⇒ 依和（戊先）；
           V3 G 之和相等（72）⇒ 重劃前面積之和大者（戊 72 ＞ 丁 62）先（道路片之重劃前面積⛔ 計）；
           V4 G 之和與重劃前面積之和皆相等 ⇒ 最小之暫編地號小者（丁之 D1(1)）先；
           V5 三位地主互相等待成環（丁 E→G、戊 E→F、己 F→G）⇒ 序鍵最小者先、其餘依原位次；
           V6 換名（街廓名之序反之、地號改名）⇒ V1 之結果除名稱外同；
           V7 先處理者（丁）在另一端之前尚有不在競合中之第三人（庚）⇒ 庚照原位次先試（被延後之戊退至丁之後）；
           V8 環成即處理（其後之他街廓之列〔T〕於互相等待之處理之後）。
           （補令一 ″·`W-G.9-395` 停機上呈之 A-1／A-2·塊 `K44`：被延後之首列退至夥伴之列之**現位**之緊後、夥伴之列之後之
            他人之前；退至同一夥伴之列之後者二以上 ⇒ 依其最終序位〔原位次〕。以下三例皆二街廓 BE〔上〕、BF〔下〕直接相鄰、
            每位地主二片上下相連、二端之門檻皆極大〔皆未成〕，量其逐列之序；每例設時限 60 s〔逾 ⇒ 紅〕。）
           V9 夥伴之列本身已被延後過（三位地主·E 戊己丁·F 丁己戊）⇒ 依其現位而退·⛔ 無限迴圈（原單之字面
              「夥伴之列之最終序位 ＋ 0.5」於此形不止）；
           V10 二首列先後退至同一夥伴之列之後而其退之先後與原位次相反（E 己丁戊·F 丁戊己）⇒ 依原位次（己之 J1 先於丁之 D1）·
              ⛔ 依回列之先後；
           V11 退至一已被延後之夥伴之列之後者，排在同退於更前之夥伴之列之後之他人之前（四位地主·E 丁己辛戊·F 戊辛己丁）⇒
              丁之 D1 緊隨己之 J1、先於辛之 K1（⛔ 以小數之位〔現位 ＋ 0.5〕而越過之）；
           V12 換名與換端：V11 之街廓改名（序同）、地號改名（各片之原地號仍各異）、二端皆為右端 ⇒ 逐列之序與結果除名稱外同
               （⛔ 寫死街廓名、端）；
           V13 被延後者之夥伴之列其後自身又被延後（四位地主·E 己辛戊丁·F 戊己丁辛·G 丁 90／辛 50／戊 30／己 20）⇒ 被延後者
               隨其夥伴之列而移、恆在其後（己之 J1 隨戊之 U1）·⛔ 停於前次之位而反排其前（KL `10:18`「二甲」之「處理後不重排」）。
           （判別力之證 ＝ 單之突變之表〔發單端施於其原型〕與主線 `d4928d4` 之紅·本器⛔ 含突變。）
           （V7 之讀 ＝ `K-9-60` ③「該端仍依 K-9-49 以原投影序逐一試其跨占者」與 `K-9-50` 讀法 2：先處理者之競合候其夥伴之列，
            夥伴之列之前之他人照原位次先試；三丙唯定二位地主之先後。）
  wiring   <repo> <基準 commit>
           W1 `end_block_apply` 內⛔ 有訊息含 `GB-207` 之 `raise`、⛔ 有 `k6_program_stop` 之呼叫；
           W2 `end_block_merge_run` 內⛔ 有訊息含「同時跨占二以上末端塊」「屬二以上之競合」之 `raise`；仍有含「三個以上之末端塊」
              者（`K-9-60` ② 另單）；
           W3 `k6b_stage3_run` 之 `_k950_rows` 內⛔ 有訊息含「屬二以上之競合」之 `raise`、仍有含「列數 ≠ 2」者
           （W1〜W3 唯計 `raise` 之句內之字串·docstring 與註⛔ 計）；
           W4 `app.py` 之頂層之名⛔ 增減；頂層節點之相異 ＝ `{end_block_apply, end_block_merge_run, k6b_stage3_run}`；
           W5 所改之三節點內⛔ 新增案件字面；W6 `verify/` 頂層之 `*.py` 對基準相異 0。
  run      <repo> [<退縮> …]
           harness 實跑本案（預設退縮 `3.5`、`0.0`）之末端塊之評選之紀錄與合併再試之紀錄：
           R1 觸發之端 4、皆有當選、「歸他端」之列 0（本案無一筆同時跨占二端）；R2 合併再試之標的 0、競合 0。
rc：0 相符／1 不符／2 用法錯。
"""
import ast, contextlib, copy, io, math, os, re, subprocess, sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:  # noqa: BLE001
    pass

# 已去之停機之訊息之字樣（以短段之和書之·⛔ 為 F23／F24 之字樣之錨·retro 2026-10-23）
GONE_DUP = "".join(("同時跨", "占二以", "上末", "端塊"))
GONE_TGC = "".join(("屬二以", "上之競", "合"))
KEEP_HIT3 = "".join(("三個以", "上之末", "端塊"))
KEEP_ROWS = "".join(("列數", " ≠ ", "2"))
CASE_LIT_RE = re.compile(r"^(R|RD|G)\d+$|^G\d{3}$|^\d{3}(-\d+)*(\(\d+\))?$")
CHG_TOP = {"end_block_apply", "end_block_merge_run", "k6b_stage3_run"}
MW, DEP = 3.5, 30.0
H = "住宅區"


def _harvest(repo):
    sys.path.insert(0, os.path.join(repo, "verify"))
    from app_harvest import harvest
    with contextlib.redirect_stdout(io.StringIO()):
        ns, fake_st = harvest(os.path.join(repo, "app.py"))
    return ns, fake_st


# ───────────────────────── 甲：end_block_apply ─────────────────────────

def _xf(ang_deg, mirror, tx, ty):
    import numpy as np
    c, s = math.cos(math.radians(ang_deg)), math.sin(math.radians(ang_deg))

    def f(p):
        x, y = float(p[0]), float(p[1])
        if mirror:
            x = -x
        return np.array((c * x - s * y + tx, s * x + c * y + ty))

    def v(d):
        x, y = float(d[0]), float(d[1])
        if mirror:
            x = -x
        return np.array((c * x - s * y, s * x + c * y))
    return f, v


ID = _xf(0, False, 0.0, 0.0)
FR = _xf(37, True, 307123.4, 2654321.7)


def _e(pid, lot, coords, frame):
    f, _v = frame
    return {"tp": {"暫編地號": pid, "原地號": lot, "polygon_coords": [list(map(float, f(c))) for c in coords]},
            "pre_position": 0, "is_corner_winner": False, "side": "中段"}


def _ap(ns, length, parts, G, frame=ID, allow=True, swap=False, ren=None):
    """parts ＝ [(暫編地號, 原地號, coords)]（自 p1 起之原位次）；G ＝ {(暫編地號, 'left'|'right'): 試算G}。
    swap ⇒ FRONT 反向（p1 ＝ (length,0)）、序反之、G 之端互換；ren ＝ 暫編地號之換名表。
    回 (序列之暫編地號, {端: (當選, [(暫編地號, 結果)…])})——換名者以原名回之。"""
    import numpy as np
    from shapely.geometry import Polygon
    f, v = frame
    ren = ren or {}
    back = {b: a for a, b in ren.items()}
    nm = lambda p: ren.get(p, p)
    blk = Polygon([f(p) for p in [(0, 0), (length, 0), (length, DEP), (0, DEP)]])
    if swap:
        p1, p2, dh = (length, 0.0), (0.0, 0.0), (-1.0, 0.0)
        seq = [_e(nm(p), nm(l), c, frame) for p, l, c in reversed(parts)]
        Gx = {(nm(p), {"left": "right", "right": "left"}[s]): g for (p, s), g in G.items()}
    else:
        p1, p2, dh = (0.0, 0.0), (length, 0.0), (1.0, 0.0)
        seq = [_e(nm(p), nm(l), c, frame) for p, l, c in parts]
        Gx = {(nm(p), s): g for (p, s), g in G.items()}
    cad = v((0.0, 1.0))
    cache = {}
    out, info = ns["end_block_apply"](
        seq, blk_label="BX", block_poly=blk, d_hat=v(dh), corner_pt=f(p1), front_p2=f(p2), cad_alloc=cad,
        allocation_dir=ns["alloc_normal_axis"](cad), min_width=MW,
        has_side_pk={"left": False, "right": False}, has_side_cad={"left": False, "right": False},
        corner_range_polys={}, trial=lambda tp, s, w: (Gx[(tp["暫編地號"], s)], 5.0), cache=cache,
        allow_forced=lambda s: allow)
    rec = cache.get("BX") or {}
    sides = (("left", "right"), ("right", "left")) if swap else (("left", "left"), ("right", "right"))
    res = {}
    for want, have in sides:
        r = rec.get(have) or {}
        w = r.get("當選")
        res[want] = (back.get(w, w), [(back.get(x.get("暫編地號"), x.get("暫編地號")), x.get("結果", "MISSING"))
                                     for x in (r.get("候選") or [])])
    o = [back.get(x["tp"]["暫編地號"], x["tp"]["暫編地號"]) for x in out]
    return (list(reversed(o)) if swap else o), res


def _R(x0, x1, y0=0.0, y1=DEP):
    return [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]


# T1〜T4：A [0,a]、X [a,b]、B [b,20]；R_end 左 [0,3.5]、右 [16.5,20]
def _p3(a, b):
    return [("A(1)", "A", _R(0, a)), ("X(1)", "X", _R(a, b)), ("B(1)", "B", _R(b, 20))]


def _g(xl, xr, al=10.0, br=10.0):
    return {("A(1)", "left"): al, ("X(1)", "left"): xl, ("X(1)", "right"): xr, ("B(1)", "right"): br,
            ("A(1)", "right"): al, ("B(1)", "left"): br}


# T8：A L 形、X(1) 前緣之帶 [1,40]×[0,10]、X(2) 後半 [2,40]×[10,30]（同一原地號 X）；長 40
P8 = [("A(1)", "A", [(0, 0), (1, 0), (1, 10), (2, 10), (2, 30), (0, 30)]),
      ("X(1)", "X", _R(1, 40, 0, 10)), ("X(2)", "X", _R(2, 40, 10, 30))]
G8 = {("A(1)", "left"): 10.0, ("X(1)", "left"): 200.0, ("X(2)", "left"): 300.0,
      ("A(1)", "right"): 10.0, ("X(1)", "right"): 200.0, ("X(2)", "right"): 50.0}
REN = {"A(1)": "甲-7(3)", "X(1)": "乙-2(1)", "X(2)": "乙-2(5)", "B(1)": "丙-9(2)"}


def _cases_a(ns):
    C = []

    def run(name, fn, exp):
        try:
            got = fn()
        except Exception as ex:  # noqa: BLE001
            got = ("例外", type(ex).__name__, str(ex)[:160])
        C.append((name, got, exp))

    t1 = (["X(1)", "A(1)", "B(1)"], {"left": ("X(1)", [("A(1)", "未達"), ("X(1)", "當選")]),
                                     "right": (None, [("B(1)", "未達"), ("X(1)", "歸他端")])})
    run("T1 X 跨二端（交 左 45／右 75）而唯左拿得下 ⇒ X 歸左、右強制、右之 X「歸他端」",
        lambda: _ap(ns, 20, _p3(2, 19), _g(200, 50)), t1)
    t2 = (["A(1)", "B(1)", "X(1)"], {"left": (None, [("A(1)", "未達"), ("X(1)", "歸他端")]),
                                     "right": ("X(1)", [("B(1)", "未達"), ("X(1)", "當選")])})
    run("T2 二端皆拿得下、右交大（45／75）⇒ 歸右；左除 X 重選 ⇒ 強制", lambda: _ap(ns, 20, _p3(2, 19), _g(200, 200)), t2)
    t3 = (["X(1)", "A(1)", "B(1)"], {"left": ("X(1)", [("A(1)", "未達"), ("X(1)", "當選")]),
                                     "right": (None, [("B(1)", "未達"), ("X(1)", "歸他端")])})
    run("T3 二端皆拿得下、交相等（75／75）⇒ 歸左（p1 側）", lambda: _ap(ns, 20, _p3(1, 19), _g(200, 200)), t3)
    run("T4 二端皆拿得下、左交大（75／45）⇒ 歸左", lambda: _ap(ns, 20, _p3(1, 18), _g(200, 200)), t3)
    t5 = (["A(1)", "X(1)", "B(1)"], {"left": (None, [("A(1)", "未達"), ("X(1)", "未達")]),
                                     "right": (None, [("B(1)", "未達"), ("X(1)", "未達")])})
    run("T5 二端皆拿不下 ⇒ 二端皆強制·X 之列皆「未達」", lambda: _ap(ns, 20, _p3(2, 19), _g(50, 50)), t5)
    t6 = (["A(1)", "B(1)", "X(1)"], {"left": ("A(1)", [("A(1)", "當選")]),
                                     "right": ("X(1)", [("B(1)", "未達"), ("X(1)", "當選")])})
    run("T6 左之 A 先當選（X 未試）、右 X 當選 ⇒ 二端各一", lambda: _ap(ns, 20, _p3(2, 19), _g(200, 200, al=200)), t6)
    one = [("X(1)", "X", _R(0, 20))]
    g1 = {("X(1)", "left"): 999.0, ("X(1)", "right"): 999.0}
    run("T7 一宗之街廓·准強制 ⇒ X 歸左、右強制",
        lambda: _ap(ns, 20, one, g1),
        (["X(1)"], {"left": ("X(1)", [("X(1)", "當選")]), "right": (None, [("X(1)", "歸他端")])}))

    def t7b():
        try:
            _ap(ns, 20, one, g1, allow=False)
        except RuntimeError as ex:
            m = str(ex)
            return ("停", "各筆單獨試算皆未達" in m and "right" in m)
        return ("過",)
    run("T7b 一宗之街廓·⛔ 准強制 ⇒ 停機（訊息含「各筆單獨試算皆未達」與 right）", t7b, ("停", True))
    t8 = (["X(2)", "A(1)", "X(1)"], {"left": ("X(2)", [("A(1)", "未達"), ("X(1)", "歸他端"), ("X(2)", "當選")]),
                                     "right": ("X(1)", [("X(2)", "歸他端"), ("X(1)", "當選")])})
    run("T8 同一原地號之二片：X(1) 歸右（交 25／35）；左重選 ⇒ X(2)（⛔ 以原地號除）；右之 X(2)「歸他端」",
        lambda: _ap(ns, 40, P8, G8), t8)
    run("T9 換名·旋轉 37°·鏡射·TWD97 ⇒ T1〜T4、T8 同",
        lambda: [_ap(ns, 20, _p3(2, 19), _g(200, 50), frame=FR, ren=REN),
                 _ap(ns, 20, _p3(2, 19), _g(200, 200), frame=FR, ren=REN),
                 _ap(ns, 20, _p3(1, 19), _g(200, 200), frame=FR, ren=REN),
                 _ap(ns, 20, _p3(1, 18), _g(200, 200), frame=FR, ren=REN),
                 _ap(ns, 40, P8, G8, frame=FR, ren=REN)],
        [t1, t2, t3, t3, t8])

    # 左右互換（FRONT 反向·序反·G 之端互換·其結果譯回原向）：T1、T2、T8 同；T3 之並列 ⇒ 歸 p1 側（原向之右端）＝ T2 之形
    run("T10 左右互換（FRONT 反向）⇒ T1、T2、T8 之結果（譯回原向）同；T3 之並列歸 p1（原向之右）",
        lambda: [_ap(ns, 20, _p3(2, 19), _g(200, 50), swap=True), _ap(ns, 20, _p3(2, 19), _g(200, 200), swap=True),
                 _ap(ns, 40, P8, G8, swap=True), _ap(ns, 20, _p3(1, 19), _g(200, 200), swap=True)],
        [t1, t2, t8, t2])
    t11 = (["A(1)", "C(1)", "B(1)"], {"left": ("A(1)", [("A(1)", "當選")]), "right": ("B(1)", [("B(1)", "當選")])})
    run("T11 無同時跨占（長 40·A [0,10]、C [10,30]、B [30,40]）⇒ 二端各當選、「歸他端」0",
        lambda: _ap(ns, 40, [("A(1)", "A", _R(0, 10)), ("C(1)", "C", _R(10, 30)), ("B(1)", "B", _R(30, 40))],
                    {("A(1)", "left"): 200.0, ("B(1)", "right"): 200.0, ("C(1)", "left"): 1.0,
                     ("C(1)", "right"): 1.0, ("A(1)", "right"): 1.0, ("B(1)", "left"): 1.0}), t11)
    return C


# ───────────────────────── 乙：end_block_merge_run ─────────────────────────

def _tp(pid, blk, cat, poly, a, lot=None, area=0.0):
    return {"暫編地號": pid, "原地號": lot or pid.split("(")[0], "polygon_coords": [list(c) for c in poly],
            "所屬街廓": blk, "街廓分類": cat, "分攤登記面積_m2": float(a), "面積_m2": float(area)}


def _cbs(targets):
    def g(t):
        return float(t.get("分攤登記面積_m2", 0) or 0) + float(t.get("面積_m2", 0) or 0)

    def a_prime(src, dst):
        return g(src)

    def alloc_eval(temp, build):
        by = {b["暫編地號"]: b for b in build}
        out = {}
        for (blk, sd), cfg in targets.items():
            rows, win = [], None
            for c in cfg["cands"]:
                if c not in by:
                    continue
                if c in cfg.get("other", ()):
                    rows.append({"暫編地號": c, "原地號": by[c]["原地號"], "跨占R_end(㎡)": 10.0,
                                 "試算G(㎡)": round(g(by[c]), 2), "臨正街寬(m)": 5.0, "結果": "歸他端"})
                    continue
                ok = g(by[c]) >= cfg["thr"]
                rows.append({"暫編地號": c, "原地號": by[c]["原地號"], "跨占R_end(㎡)": cfg.get("cross", {}).get(c, 10.0),
                             "試算G(㎡)": round(g(by[c]), 2), "臨正街寬(m)": 5.0, "結果": "當選" if ok else "未達"})
                if ok:
                    win = c
                    break
            out.setdefault(blk, {})[sd] = {"觸發": True, "R_end(㎡)": cfg["thr"], "候選": rows, "當選": win}
        return out

    def alloc_state(temp, build):
        kept = {}
        for b in build:
            kept.setdefault(b["所屬街廓"], set()).add(b["暫編地號"])
        return {"kept": kept, "bad_pools": {}, "err": None,
                "G": {b["暫編地號"]: g(b) for b in build}}
    return a_prime, alloc_eval, alloc_state


def _go(ns, world, targets):
    temp, own, blocks, cl = world
    temp = copy.deepcopy(temp)
    build = [t for t in temp if t["街廓分類"] == H]
    ap, ev, st = _cbs(targets)
    t2, b2, log, rec = ns["end_block_merge_run"](temp, build, own, set(), set(), blocks, cl, ap, ev, st,
                                                 setback=3.5, log_print=lambda *x: None)
    main = [(x["候選"], x["層級"], x["結果"]) for x in log if x.get("序") != "後處理"]
    won = sorted({(x["街廓"], x["端"], x["候選"]) for x in log if x.get("結果") == "成" and x.get("序") != "後處理"})
    return main, won, rec.get("皆未達")


def _wz():
    """一街廓 BZ（x∈[0,40]）：甲 Z1(1)[0,20]／Z2(1)[20,35]、他人 W1(1)[35,40]；道路 RZ：甲 Z3(1)[0,20]、他人 W3(1)[20,40]。"""
    t = [_tp("Z1(1)", "BZ", H, [(0, 0), (20, 0), (20, 30), (0, 30)], 100),
         _tp("Z2(1)", "BZ", H, [(20, 0), (35, 0), (35, 30), (20, 30)], 60),
         _tp("W1(1)", "BZ", H, [(35, 0), (40, 0), (40, 30), (35, 30)], 30),
         _tp("Z3(1)", "RZ", "道路", [(0, -10), (20, -10), (20, 0), (0, 0)], 70),
         _tp("W3(1)", "RZ", "道路", [(20, -10), (40, -10), (40, 0), (20, 0)], 10)]
    own = {"Z1": "g1", "Z2": "g1", "Z3": "g1", "W1": "gW", "W3": "gW"}
    blocks = {"BZ": {"category": H}, "RZ": {"category": "道路"}}
    return t, own, blocks, {"RZ": [(-10.0, -5.0), (50.0, -5.0)]}


def _w2(a, area=None, nm=None, third=False, tg=False):
    """二街廓 BE（上·y∈[0,30]）、BF（下·y∈[-40,-10]）隔道路 RX（中心線 y ＝ -5）。丁：D1(1) BE [0,5]、Dr(1) RX [0,5]、
    D2(1) BF [0,5]；戊：U1(1) BE [5,10]、Ur(1) RX [5,10]、U2(1) BF [5,10]；他人 P／R0／Q 於 [10,40]。nm ＝ 換名表。"""
    nm = nm or {}
    n = lambda s: nm.get(s, s)
    area = area or {}
    E, F, RX = n("BE"), n("BF"), n("RX")
    t = [_tp(n("D1(1)"), E, H, [(0, 0), (5, 0), (5, 30), (0, 30)], a["D1"], area=area.get("D1", 0.0)),
         _tp(n("U1(1)"), E, H, [(5, 0), (10, 0), (10, 30), (5, 30)], a["U1"], area=area.get("U1", 0.0)),
         _tp(n("P(1)"), E, H, [(10, 0), (40, 0), (40, 30), (10, 30)], 900),
         _tp(n("Dr(1)"), RX, "道路", [(0, -10), (5, -10), (5, 0), (0, 0)], a["Dr"]),
         _tp(n("Ur(1)"), RX, "道路", [(5, -10), (10, -10), (10, 0), (5, 0)], a["Ur"]),
         _tp(n("R0(1)"), RX, "道路", [(10, -10), (40, -10), (40, 0), (10, 0)], 300),
         _tp(n("D2(1)"), F, H, [(0, -40), (5, -40), (5, -10), (0, -10)], a["D2"], area=area.get("D2", 0.0)),
         _tp(n("U2(1)"), F, H, [(5, -40), (10, -40), (10, -10), (5, -10)], a["U2"], area=area.get("U2", 0.0)),
         _tp(n("Q(1)"), F, H, [(10, -40), (40, -40), (40, -10), (10, -10)], 900)]
    own = {n("D1"): "g丁", n("Dr"): "g丁", n("D2"): "g丁", n("U1"): "g戊", n("Ur"): "g戊", n("U2"): "g戊",
           n("P"): "gP", n("R0"): "gR", n("Q"): "gQ"}
    blocks = {E: {"category": H}, F: {"category": H}, RX: {"category": "道路"}}
    if third:   # 第三人庚：X(1) BF [10,15]（跨占 F）、X2(1) BF [15,20]（同街廓相鄰）；Q 縮為 [20,40]
        t = [x for x in t if x["暫編地號"] != n("Q(1)")]
        t += [_tp("X(1)", F, H, [(10, -40), (15, -40), (15, -10), (10, -10)], 100),
              _tp("X2(1)", F, H, [(15, -40), (20, -40), (20, -10), (15, -10)], 90),
              _tp(n("Q(1)"), F, H, [(20, -40), (40, -40), (40, -10), (20, -10)], 900)]
        own.update({"X": "g庚", "X2": "g庚"})
    if tg:      # 他街廓之末端塊 BG（街廓名在 BE、BF 之後）之未達候選 T(1)（無相連之土地）
        t += [_tp("T(1)", "BG", H, [(60, 0), (65, 0), (65, 30), (60, 30)], 10)]
        own.update({"T": "gT"})
        blocks["BG"] = {"category": H}
    return t, own, blocks, {RX: [(-10.0, -5.0), (50.0, -5.0)]}


def _t2(order_e, order_f, thr_e=90, thr_f=180, cross=None, nm=None):
    nm = nm or {}
    n = lambda s: nm.get(s, s)
    return {(n("BE"), "left"): dict(thr=thr_e, cands=[n(x) for x in order_e], cross={n(k): v for k, v in (cross or {}).items()}),
            (n("BF"), "left"): dict(thr=thr_f, cands=[n(x) for x in order_f], cross={n(k): v for k, v in (cross or {}).items()})}


V1A = dict(D1=36, D2=27, Dr=60, U1=45, U2=36, Ur=150)
V1X = {"D1(1)": 40, "D2(1)": 30, "U1(1)": 20, "U2(1)": 20}      # 交面積：丁 70 ＞ 戊 40（⛔ 為序鍵）
EXP_V1 = ([("U2(1)", "K-9-60 ③", "互相等待 ⇒ 先處理"), ("U1(1)", "②半", "成"), ("U2(1)", "②半", "未成"),
           ("D1(1)", "—", "略·已定案"), ("D2(1)", "②", "未成")],
          [("BE", "左", "U1(1)")], {"BF": ["left"]})


def _w3():
    """三街廓 BE [0,40]×[0,30]、BF [0,40]×[-30,0]（BE 之下·直接相鄰）、BG [40,80]×[-30,30]（右·直接相鄰）；無道路。
    丁：D1(1) BE [30,40]×[0,30]、Dg(1) BG [40,50]×[0,30]；戊：U1(1) BE [0,10]、U2(1) BF [0,10]；
    己：J2(1) BF [30,40]、Jg(1) BG [40,50]×[-30,0]。"""
    t = [_tp("U1(1)", "BE", H, [(0, 0), (10, 0), (10, 30), (0, 30)], 30),
         _tp("D1(1)", "BE", H, [(30, 0), (40, 0), (40, 30), (30, 30)], 20),
         _tp("U2(1)", "BF", H, [(0, -30), (10, -30), (10, 0), (0, 0)], 30),
         _tp("J2(1)", "BF", H, [(30, -30), (40, -30), (40, 0), (30, 0)], 25),
         _tp("Dg(1)", "BG", H, [(40, 0), (50, 0), (50, 30), (40, 30)], 20),
         _tp("Jg(1)", "BG", H, [(40, -30), (50, -30), (50, 0), (40, 0)], 25)]
    own = {"D1": "g丁", "Dg": "g丁", "U1": "g戊", "U2": "g戊", "J2": "g己", "Jg": "g己"}
    blocks = {"BE": {"category": H}, "BF": {"category": H}, "BG": {"category": H}}
    return t, own, blocks, {}


def _cases_b(ns):
    C = []

    def run(name, fn, exp):
        try:
            got = fn()
        except Exception as ex:  # noqa: BLE001
            got = ("例外", type(ex).__name__, str(ex)[:160])
        C.append((name, got, exp))

    wz = _wz()
    run("U1 一筆 Z1 為二端之未達候選 ⇒ 題二之競合：二端皆以 Z2 拿得下、右交大 ⇒ 歸右、左皆未達",
        lambda: _go(ns, wz, {("BZ", "left"): dict(thr=150, cands=["Z1(1)"], cross={"Z1(1)": 30}),
                             ("BZ", "right"): dict(thr=150, cands=["W1(1)", "Z1(1)"], cross={"Z1(1)": 50})}),
        ([("W1(1)", "②", "未成"), ("Z1(1)", "①", "成"), ("Z1(1)", "①", "未成")], [("BZ", "右", "Z1(1)")], {"BZ": ["left"]}))
    run("U2 取得即鎖定：右之當選 Z2 與左之未達候選 Z1 同群相連 ⇒ 左⛔ 併 Z2 ⇒ 左皆未達",
        lambda: _go(ns, wz, {("BZ", "left"): dict(thr=230, cands=["Z1(1)"]),
                             ("BZ", "right"): dict(thr=60, cands=["W1(1)", "Z2(1)"])}),
        ([("Z1(1)", "②", "未成")], [], {"BZ": ["left"]}))
    w = _w2(V1A)
    run("V0 一端屬二競合而順序一致（E、F 皆丁先）⇒ 依原位次：丁得 E（整片）、戊得 F（整片）",
        lambda: _go(ns, w, _t2(["D1(1)", "U1(1)"], ["D2(1)", "U2(1)"], cross=V1X)),
        ([("D1(1)", "②", "成"), ("D2(1)", "②", "未成"), ("U1(1)", "—", "略·已定案"), ("U2(1)", "②", "成")],
         [("BE", "左", "D1(1)"), ("BF", "左", "U2(1)")], {}))
    run("V1 順序相反 ⇒ 互相等待 ⇒ 序鍵（G 之和 戊 81 ＞ 丁 63）⇒ 戊先：戊得 E、F 強制",
        lambda: _go(ns, w, _t2(["D1(1)", "U1(1)"], ["U2(1)", "D2(1)"], cross=V1X)), EXP_V1)
    w2 = _w2(dict(D1=50, D2=13, Dr=60, U1=36, U2=36, Ur=150))
    run("V2 G 之和（戊 72 ＞ 丁 63）與最大之一片（丁 50 ＞ 戊 36）異 ⇒ 依和：戊先",
        lambda: _go(ns, w2, _t2(["D1(1)", "U1(1)"], ["U2(1)", "D2(1)"])),
        ([("U2(1)", "K-9-60 ③", "互相等待 ⇒ 先處理"), ("U1(1)", "②半", "成"), ("U2(1)", "②半", "未成"),
          ("D1(1)", "—", "略·已定案"), ("D2(1)", "②", "未成")], [("BE", "左", "U1(1)")], {"BF": ["left"]}))
    w3 = _w2(dict(D1=30, D2=32, Dr=200, U1=36, U2=36, Ur=150), area={"D1": 10.0})
    run("V3 G 之和相等（72）⇒ 重劃前面積之和大者（戊 72 ＞ 丁 62·道路片⛔ 計）先：戊得 E、丁得 F",
        lambda: _go(ns, w3, _t2(["D1(1)", "U1(1)"], ["U2(1)", "D2(1)"])),
        ([("U2(1)", "K-9-60 ③", "互相等待 ⇒ 先處理"), ("U1(1)", "②半", "成"), ("U2(1)", "②半", "未成"),
          ("D1(1)", "—", "略·已定案"), ("D2(1)", "②", "成")], [("BE", "左", "U1(1)"), ("BF", "左", "D2(1)")], {}))
    w4 = _w2(dict(D1=36, D2=36, Dr=60, U1=36, U2=36, Ur=150))
    run("V4 G 之和與重劃前面積之和皆相等 ⇒ 最小之暫編地號小者（D1(1)）先：丁得 E、戊得 F",
        lambda: _go(ns, w4, _t2(["D1(1)", "U1(1)"], ["U2(1)", "D2(1)"])),
        ([("D1(1)", "K-9-60 ③", "互相等待 ⇒ 先處理"), ("D1(1)", "②", "成"), ("D2(1)", "②", "未成"),
          ("U1(1)", "—", "略·已定案"), ("U2(1)", "②", "成")], [("BE", "左", "D1(1)"), ("BF", "左", "U2(1)")], {}))
    big = 10 ** 6
    run("V5 三位地主互相等待成環（G 之和 丁 40／戊 60／己 50）⇒ 戊先、其餘依原位次（己、丁）",
        lambda: _go(ns, _w3(), {("BE", "left"): dict(thr=big, cands=["D1(1)", "U1(1)"]),
                                ("BF", "left"): dict(thr=big, cands=["U2(1)", "J2(1)"]),
                                ("BG", "left"): dict(thr=big, cands=["Jg(1)", "Dg(1)"])}),
        ([("U2(1)", "K-9-60 ③", "互相等待 ⇒ 先處理"), ("U2(1)", "—", "未成"), ("U1(1)", "—", "未成"),
          ("Jg(1)", "—", "未成"), ("J2(1)", "—", "未成"), ("D1(1)", "—", "未成"), ("Dg(1)", "—", "未成")],
         [], {"BE": ["left"], "BF": ["left"], "BG": ["left"]}))
    NM = {"BE": "Z9", "BF": "A1", "RX": "M5", "D1(1)": "77(4)", "D2(1)": "77(9)", "Dr(1)": "77(6)", "U1(1)": "31(2)",
          "U2(1)": "31(8)", "Ur(1)": "31(5)", "P(1)": "50(1)", "R0(1)": "51(1)", "Q(1)": "52(1)",
          "D1": "77", "D2": "77", "Dr": "77", "U1": "31", "U2": "31", "Ur": "31", "P": "50", "R0": "51", "Q": "52"}
    inv = {v: k for k, v in NM.items() if "(" in k or k in ("BE", "BF", "RX")}

    def v6():
        m, wn, fl = _go(ns, _w2(V1A, nm=NM), _t2(["D1(1)", "U1(1)"], ["U2(1)", "D2(1)"], cross=V1X, nm=NM))
        b = lambda s: inv.get(s, s)
        return (sorted((b(c), l, r) for c, l, r in m), sorted((b(x), e, b(c)) for x, e, c in wn),
                {b(k): v for k, v in (fl or {}).items()})
    # 逐列之先後隨街廓名之序（各端之列之最終序位依街廓名排·既有）⇒ 比其集（土地之果：定案之端、皆未達）
    run("V6 換名（街廓名之序反之·地號改名）⇒ V1 之結果除名稱外同（逐列之集·定案之端·皆未達）", v6,
        (sorted(EXP_V1[0]), EXP_V1[1], EXP_V1[2]))
    w7 = _w2(dict(D1=50, D2=30, Dr=60, U1=36, U2=36, Ur=150), third=True)
    run("V7 互相等待而先處理者（丁·G 之和 80 ＞ 戊 72）在 F 端之前尚有第三人庚 ⇒ 庚照原位次先試而得 F；丁之競合消滅、丁得 E",
        lambda: _go(ns, w7, _t2(["D1(1)", "U1(1)"], ["U2(1)", "X(1)", "D2(1)"])),
        ([("D1(1)", "K-9-60 ③", "互相等待 ⇒ 先處理"), ("X(1)", "①", "成"), ("D1(1)", "②", "成"),
          ("U1(1)", "—", "略·已定案"), ("D2(1)", "—", "略·已定案"), ("U2(1)", "—", "略·已定案")],
         [("BE", "左", "D1(1)"), ("BF", "左", "X(1)")], {}))
    t8 = _t2(["D1(1)", "U1(1)"], ["U2(1)", "D2(1)"], cross=V1X)
    t8[("BG", "left")] = dict(thr=10 ** 6, cands=["T(1)"])
    run("V8 環成即處理：V1 之環成於 F 端之末列，其後之他街廓之列（T）於其處理之後",
        lambda: _go(ns, _w2(V1A, tg=True), t8),
        (EXP_V1[0] + [("T(1)", "—", "未成")], EXP_V1[1], {"BF": ["left"], "BG": ["left"]}))
    # ── 補令一 ″（塊 `K44`·A-1／A-2）：被延後之首列之新位 ＝ 夥伴之列之現位之緊後；同退者依原位次 ──
    for nm, E, F, G, exp in V9_13:
        run(nm, (lambda E=E, F=F, G=G: _alarm(lambda: _go(ns, _wv9(E, F, G), _tv9(E, F)), 60)), exp)
    _n11, E11, F11, G11, X11 = V9_13[2]
    inv12 = {v: k for k, v in NM12.items()}

    def v12():
        m, wn, fl = _go(ns, _renv9(_wv9(E11, F11, G11), NM12), _tv9([NM12[x] for x in E11], [NM12[x] for x in F11],
                                                                   blk=(NM12["BE"], NM12["BF"]), sd="right"))
        b = lambda x: inv12.get(x, x)
        return ([(b(c), l, r) for c, l, r in m], [(b(x), e, b(c)) for x, e, c in wn],
                {b(k): ["left" if s == "right" else s for s in v] for k, v in (fl or {}).items()})
    run("V12 換名與換端：V11 之街廓改名（A7、B2·序同）、地號改名、二端皆為右端 ⇒ 除名稱外同 V11", lambda: _alarm(v12, 60), X11)
    return C


NM12 = {"BE": "A7", "BF": "B2", "U1(1)": "31(2)", "U2(1)": "36(8)", "J1(1)": "44(1)", "J2(1)": "48(6)",
        "D1(1)": "77(4)", "D2(1)": "79(9)", "K1(1)": "12(3)", "K2(1)": "15(5)"}


def _renv9(world, nm):
    """換名：暫編地號、原地號、所屬街廓、地主之表、街廓之表皆依 nm（原地號 ＝ 換名後之暫編地號之括號之前）。"""
    t, own, blocks, cl = world
    t2, own2 = [], {}
    for x in t:
        y = dict(x)
        y["暫編地號"] = nm[x["暫編地號"]]
        y["原地號"] = y["暫編地號"].split("(")[0]
        y["所屬街廓"] = nm[x["所屬街廓"]]
        own2[y["原地號"]] = own[x["原地號"]]
        t2.append(y)
    return t2, own2, {nm[k]: v for k, v in blocks.items()}, cl


def _alarm(fn, sec):
    """逾 sec 秒 ⇒ 例外（無限迴圈之形·⛔ 卡住）。"""
    import signal

    def h(*_a):
        raise TimeoutError(f"逾 {sec} s（無限迴圈之形）")
    old = signal.signal(signal.SIGALRM, h)
    signal.alarm(sec)
    try:
        return fn()
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, old)


def _wv9(E, F, G):
    """二街廓 BE（上·y∈[0,30]）、BF（下·y∈[-30,0]）直接相鄰、無道路。每位地主（暫編地號之首字：U 戊、J 己、D 丁、K 辛）
    各有 BE 一片、BF 一片，同一 x 之欄（U [0,5]、J [5,10]、D [10,15]、K [15,20]）上下相連；每片之分攤登記面積 ＝ G[首字] ÷ 2
    （⇒ 該地主於二端之未達候選之試算 G 之和 ＝ G[首字]）。E、F ＝ 二端之原位次（暫編地號之序）。"""
    col = {"U": 0, "J": 5, "D": 10, "K": 15}
    gid = {"U": "g戊", "J": "g己", "D": "g丁", "K": "g辛"}
    t, own = [], {}
    for pid in E:
        x = col[pid[0]]
        t.append(_tp(pid, "BE", H, [(x, 0), (x + 5, 0), (x + 5, 30), (x, 30)], G[pid[0]] / 2))
        own[pid.split("(")[0]] = gid[pid[0]]
    for pid in F:
        x = col[pid[0]]
        t.append(_tp(pid, "BF", H, [(x, -30), (x + 5, -30), (x + 5, 0), (x, 0)], G[pid[0]] / 2))
        own[pid.split("(")[0]] = gid[pid[0]]
    return t, own, {"BE": {"category": H}, "BF": {"category": H}}, {}


def _tv9(E, F, blk=("BE", "BF"), sd="left"):
    big = 10 ** 6
    return {(blk[0], sd): dict(thr=big, cands=list(E)), (blk[1], sd): dict(thr=big, cands=list(F))}


_PRv = "互相等待 ⇒ 先處理"
_Nv = lambda *ps: [(p, "—", "未成") for p in ps]
_Pv = lambda p: (p, "K-9-60 ③", _PRv)
# 期值（手算·補令一 ″ 附錄戊″ 之逐步）：序鍵 ＝ G 之和大者先（戊 ＞ 己 ＞ 丁 ＞ 辛）
V9_13 = [
    ("V9 夥伴之列已被延後過（E 戊己丁·F 丁己戊·G 戊 60／己 50／丁 40）⇒ 依其現位而退、⛔ 無限迴圈",
     ["U1(1)", "J1(1)", "D1(1)"], ["D2(1)", "J2(1)", "U2(1)"], {"U": 60, "J": 50, "D": 40},
     ([_Pv("U1(1)"), _Pv("U1(1)")] + _Nv("U1(1)", "U2(1)") + [_Pv("J1(1)")] + _Nv("J1(1)", "J2(1)", "D1(1)", "D2(1)"),
      [], {"BE": ["left"], "BF": ["left"]})),
    ("V10 二首列退至同一夥伴之列之後而退之先後與原位次相反（E 己丁戊·F 丁戊己）⇒ 依原位次（J1 先於 D1）",
     ["J1(1)", "D1(1)", "U1(1)"], ["D2(1)", "U2(1)", "J2(1)"], {"U": 60, "J": 50, "D": 40},
     ([_Pv("J1(1)"), _Pv("U2(1)"), _Pv("U2(1)")] + _Nv("U2(1)", "U1(1)", "J1(1)", "J2(1)", "D1(1)", "D2(1)"),
      [], {"BE": ["left"], "BF": ["left"]})),
    ("V11 退至已被延後之夥伴之列（J1）之緊後（E 丁己辛戊·F 戊辛己丁·G 戊 80／己 70／丁 60／辛 50）⇒ D1 先於 K1",
     ["D1(1)", "J1(1)", "K1(1)", "U1(1)"], ["U2(1)", "K2(1)", "J2(1)", "D2(1)"], {"U": 80, "J": 70, "D": 60, "K": 50},
     ([_Pv("U2(1)")] * 3 + _Nv("U2(1)", "U1(1)") + [_Pv("D1(1)"), _Pv("J2(1)")]
      + _Nv("J2(1)", "J1(1)", "D1(1)", "D2(1)", "K1(1)", "K2(1)"),
      [], {"BE": ["left"], "BF": ["left"]})),
    ("V13 被延後者之夥伴之列其後自身又被延後（E 己辛戊丁·F 戊己丁辛·G 丁 90／辛 50／戊 30／己 20）⇒ 己之 J1 隨戊之 U1 而移",
     ["J1(1)", "K1(1)", "U1(1)", "D1(1)"], ["U2(1)", "J2(1)", "D2(1)", "K2(1)"], {"U": 30, "J": 20, "D": 90, "K": 50},
     ([_Pv("U2(1)"), _Pv("K1(1)"), _Pv("K1(1)"), _Pv("D2(1)"), _Pv("D2(1)")]
      + _Nv("D2(1)", "D1(1)", "K1(1)", "K2(1)", "U1(1)", "U2(1)", "J1(1)", "J2(1)"),
      [], {"BE": ["left"], "BF": ["left"]})),
]


NEED = ["end_block_apply", "end_block_merge_run", "k6b_stage3_run", "alloc_normal_axis", "k967_rank"]


def selftest(repo):
    ns, _ = _harvest(repo)
    miss = [n for n in NEED if n not in ns]
    if miss:
        print(f"  🔴 受詞缺 {miss}")
        print("⇒ 紅 ['受詞缺']；rc 1")
        return 1
    red = []
    for title, cases in (("── 甲 end_block_apply（K-9-60 ①）──", _cases_a(ns)),
                         ("── 乙 end_block_merge_run（K-9-60 ①③·取得即鎖定）──", _cases_b(ns))):
        print(title)
        for name, got, exp in cases:
            ok = got == exp
            print(("  ✅ " if ok else "  🔴 ") + name)
            if not ok:
                print(f"       得 {got!r}"[:900])
                print(f"       期 {exp!r}"[:900])
                red.append(name.split()[0])
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


# ───────────────────────── wiring ─────────────────────────

def _git(repo, *a):
    r = subprocess.run(["git", "-C", repo, *a], capture_output=True)
    return r.stdout if r.returncode == 0 else None


def _top(src):
    t = ast.parse(src)
    out = {}
    for n in t.body:
        nm = getattr(n, "name", None)
        if nm is None and isinstance(n, ast.Assign):
            nm = ",".join(x.id for x in n.targets if isinstance(x, ast.Name)) or None
        if nm is None and isinstance(n, ast.AnnAssign) and isinstance(n.target, ast.Name):
            nm = n.target.id
        if nm:
            out.setdefault(nm, []).append(ast.dump(n))
    return out


def _fn(src, name):
    for n in ast.parse(src).body:
        if isinstance(n, ast.FunctionDef) and n.name == name:
            return n, ast.get_source_segment(src, n)
    return None, ""


def _strs(node):
    return [x.value for x in ast.walk(node) if isinstance(x, ast.Constant) and isinstance(x.value, str)]


def _raise_strs(node):
    """`raise` 之句內之字串常數（含 f-string 之常數之段）——停機之訊息之受詞（docstring／註⛔ 計）。"""
    return [s for r in ast.walk(node) if isinstance(r, ast.Raise) for s in _strs(r)]


def _calls(node, name):
    return [x for x in ast.walk(node) if isinstance(x, ast.Call)
            and ((isinstance(x.func, ast.Name) and x.func.id == name)
                 or (isinstance(x.func, ast.Attribute) and x.func.attr == name))]


def wiring(repo, base):
    src = open(os.path.join(repo, "app.py"), encoding="utf-8").read()
    bsrc = _git(repo, "show", f"{base}:app.py")
    red = []

    def rep(tag, ok, msg):
        print(("  ✅ " if ok else "  🔴 ") + f"{tag} {msg}")
        if not ok:
            red.append(tag)
    if bsrc is None:
        print(f"  🔴 基準 {base} 之 app.py 取不到")
        print("⇒ 紅 ['基準']；rc 1")
        return 1
    bsrc = bsrc.decode("utf-8")
    n1, _s1 = _fn(src, "end_block_apply")
    n2, _s2 = _fn(src, "end_block_merge_run")
    n3, _s3 = _fn(src, "k6b_stage3_run")
    if not (n1 and n2 and n3):
        rep("W0", False, "受詞缺")
        print(f"⇒ 紅 {red}；rc 1")
        return 1
    rep("W1", not any("GB-207" in s for s in _raise_strs(n1)) and not _calls(n1, "k6_program_stop"),
        "end_block_apply 內⛔ 有 GB-207 之字面、⛔ 有 k6_program_stop 之呼叫")
    s2 = _raise_strs(n2)
    rep("W2", not any(GONE_DUP in s for s in s2) and not any(GONE_TGC in s for s in s2)
        and any(KEEP_HIT3 in s for s in s2),
        "end_block_merge_run：⛔ 有「同時跨占二以上末端塊」「屬二以上之競合」之停機；仍有「三個以上之末端塊」之停機")
    k950 = [x for x in ast.walk(n3) if isinstance(x, ast.FunctionDef) and x.name == "_k950_rows"]
    s3 = _raise_strs(k950[0]) if len(k950) == 1 else []
    rep("W3", len(k950) == 1 and not any(GONE_TGC in s for s in s3) and any(KEEP_ROWS in s for s in s3),
        "_k950_rows：⛔ 有「屬二以上之競合」之停機、仍有「列數 ≠ 2」之停機")
    a, b = _top(src), _top(bsrc)
    names_ok = set(a) == set(b)
    diff = {k for k in a if a.get(k) != b.get(k)}
    rep("W4", names_ok and diff == CHG_TOP,
        f"頂層之名之增減 {sorted(set(a) ^ set(b))}（期 []）；頂層節點之相異 {sorted(diff)}（期 {sorted(CHG_TOP)}）")
    lits = []
    for nm in sorted(CHG_TOP):
        nn, _ = _fn(src, nm)
        bn, _ = _fn(bsrc, nm)
        cur = [s for s in _strs(nn) if CASE_LIT_RE.match(s)]
        old = [s for s in _strs(bn) if CASE_LIT_RE.match(s)] if bn else []
        lits += [(nm, s) for s in cur if cur.count(s) > old.count(s)]
    rep("W5", not lits, f"所改之三節點內新增案件字面 {sorted(set(lits))}（期 []）")
    out = _git(repo, "diff", "--name-only", base, "--", ":(glob)verify/*.py")
    wt = subprocess.run(["git", "-C", repo, "diff", "--name-only", "--", ":(glob)verify/*.py"], capture_output=True).stdout
    chg = sorted(set((out or b"").decode().split()) | set(wt.decode().split()))
    rep("W6", out is not None and not chg, f"verify/ 頂層之 *.py 對基準相異 {chg}（期 []）")
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


# ───────────────────────── run ─────────────────────────

def _one(repo, sb):
    """harness 實跑本案（段三之入口 `run_corner_pk_k6b` ＋ 定案之配地·同 F37 之法）：回 (末端塊之評選之紀錄, 合併再試之紀錄)。"""
    probes = os.path.join(repo, "verify", "probes")
    if probes not in sys.path:
        sys.path.insert(0, probes)
    os.environ["WV_K6B_STAGE3"] = "on"
    import probe_WG9344_k6s3 as K
    ns, fst, snap, cb_by, cad, tp, bp, params = K._boot(repo, sb)
    import selection_pipeline as sp
    with contextlib.redirect_stdout(io.StringIO()):
        _d, _s, _o, wins, forced, _tp2, bp2 = sp.run_corner_pk_k6b(ns, fst, list(cb_by.values()), cad, params, tp, bp, sb,
                                                                   snapshot=snap)
    mr = copy.deepcopy(fst.session_state.get(ns["SS_END_BLOCK_MERGE"]))
    res = K._materialize(ns, fst, snap, cb_by, cad, params, tp, bp2, wins, forced, sb)
    ebv = copy.deepcopy(fst.session_state.get(ns["SS_END_BLOCK_EVAL"]) or {})
    return res, ebv, mr


def run(repo, setbacks):
    red = []
    for sb in setbacks:
        try:
            res, ev, mr = _one(repo, sb)
        except Exception as e:  # noqa: BLE001
            print(f"  🔴 R0@{sb} 例外 {type(e).__name__}：{str(e)[:200]}")
            red.append(f"R0@{sb}")
            continue
        trig = sorted((b, s) for b in ev for s in ("left", "right") if isinstance((ev.get(b) or {}).get(s), dict)
                      and ev[b][s].get("觸發"))
        wins = [(b, s) for b, s in trig if ev[b][s].get("當選") is not None]
        oth = [(b, s, r.get("暫編地號")) for b, s in trig for r in (ev[b][s].get("候選") or []) if r.get("結果") == "歸他端"]
        ok1 = len(trig) == 4 and len(wins) == 4 and not oth and res.get("err") is None
        print(("  ✅ " if ok1 else "  🔴 ") + f"R1@{sb} 觸發之端 {len(trig)}（期 4）、有當選 {len(wins)}（期 4）、"
              f"「歸他端」之列 {oth}（期 []）、err {res.get('err')!r}")
        if not ok1:
            red.append(f"R1@{sb}")
        ok2 = isinstance(mr, dict) and mr.get("標的") == [] and not mr.get("競合")
        print(("  ✅ " if ok2 else "  🔴 ") + f"R2@{sb} 合併再試之標的 {(mr or {}).get('標的')!r}（期 []）、競合 "
              f"{(mr or {}).get('競合')!r}（期 無）")
        if not ok2:
            red.append(f"R2@{sb}")
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


def main(argv):
    if len(argv) >= 3 and argv[1] == "selftest":
        return selftest(argv[2])
    if len(argv) >= 4 and argv[1] == "wiring":
        return wiring(argv[2], argv[3])
    if len(argv) >= 3 and argv[1] == "run":
        repo = os.path.abspath(argv[2])
        sys.path.insert(0, os.path.join(repo, "verify"))
        os.chdir(repo)
        return run(repo, [float(x) for x in argv[3:]] or [3.5, 0.0])
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
