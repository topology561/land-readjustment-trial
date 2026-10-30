# -*- coding: utf-8 -*-
"""W-G.9-399 量測器（發單端擬·檔 F42·⛔ 由受單側改一字）：互相等待之二位地主之先後改以**末端塊評選指數**（KL
`2026-10-26 22:09`「用類似街角地的評選機制……計算各街廓之末端塊名次，以名次相加最小者……為先」·`22:42`「1. 權重改用2項
即可：端線 0.4、面積 0.6 2. 「是」，與街角地一致 …… 4. 「是」，兩端、三端用同一規則」·`22:57`「是，但有關"三人以上輪流
互等時"問題，可否以(應分配面積 → 重劃前面積 → 暫編地號)排先後」）。

所量之性質：
  ① 端線（`end_block_end_geom`·於 `end_block_apply` 中併入各端之幾何）＝ 街廓外框自 FRONT 之該端點（左 p1／右 p2）沿外框背離他端點之向至首觸 BASELINE 之一段；其於 `R_end` 之外框上之長
     （同源·分母）；他端點得為截角前之理論角（唯取投影定向）。
  ② 一宗之評選指數 ＝ 0.4 × 臨端線之長 ÷ 端線之長 ＋ 0.6 × 跨占 ÷ R_end（⛔ 計正面道路之長）。
  ③ 名次：一端之未達之列依合併群合計指數（取至 4 位）大者先、同者原位次先者先（比照街角）。
  ④ 二位互相等待之先後（`K-9-28` 之序·唯計共同跨占之端）：有第 1 名者先 → 第 1 名之端數多 →〔皆無第 1 名者〕名次之和小 →
     面積（共同之端之片之重劃前面積·一片一次）大 → 指數之和大 → 暫編地號小。
  ⑤ 三位以上輪流互等（KL 22:42 ④「兩端、三端用同一規則」·22:57 之「但」唯及兩兩比較成圈者·10/25 通知三之 3「同一取法」）：
     兩兩以評選指數比，勝過其餘每一位者先；兩兩比較成圈或二位無共同之端 ⇒ 應分配面積 → 重劃前面積 → 暫編地號（＝ 序鍵）；
     互相等待而缺評選指數 ⇒ 停機。

子命令（一律 python3 verify/probes/probe_WG9399_k960x.py <子命令> …）：
  selftest <repo>
           合成對照（⛔ 讀本案資料·`harvest(app.py)` 取諸函式·期值皆手算）。
           甲（`end_block_side_geom` ＋ `end_block_end_geom`·玩具街廓：FRONT 沿 x 軸、宗地分配線 ∥ y 軸、深 30、畸零地寬 3.5、BASELINE y ＝ 30）：
           E1 矩形（長 20）⇒ 左、右之端線長 30、R_end 105；E2 左之未臨正街三角（外框 (0,0)→(−5,30)）⇒ 左 √925 ＝ 30.4138；
           E3 左端線內斜（(0,0)→(8,30)）⇒ R_end 之端線長 √(3.5² ＋ 13.125²) ＝ 13.5836（⛔ 以全邊 31.0483）；
           E4 左端線二折（(0,0)→(−2,15)→(0,30)）⇒ 2√229 ＝ 30.2655；E5 右端有截角而 p2 為理論角（距外框 √2）⇒ 左仍 30；
           E6 旋轉 37°、鏡射、TWD97 之尺度、FRONT 反向 ⇒ E1〜E4 之長同（差 ≤ 1e-6）；
           E7 BASELINE 未給 ⇒ `end_segs`／`end_len` 皆 None；E8 該端點距外框 0.049 ⇒ 可、0.051 ⇒ 停機；
           E9 BASELINE 不觸外框 ⇒ 停機；E10 BASELINE 過該端點 ⇒ 停機。
           〔補令一 ″·W-2〕E11 BASELINE 過 (10,30) 而偏 0.5° ⇒ 右 30（⛔ 循屁股線延至交點 ⇒ 33.5）、左 30 − 10·tan0.5°；E11′ 同之
           旋轉鏡射 TWD97、FRONT 反向；E12 偏 −0.5° ⇒ 左 30、右 30 − 10·tan0.5°；E13 偏 1.9° ⇒ 右 30；E13′ 偏 2.1°（逾 2°·
           BASELINE 非屁股線）⇒ 右依字面 33.5；E14 端之外框有與 BASELINE 平行而遠之折（深 15 處橫 3）⇒ 端線 15＋3＋15 ＝ 33
           （⛔ 止於其折）；E15 BASELINE ∥ 屁股線而外移 0.049 ⇒ 30、0.051 ⇒ 停機。
           乙（`end_block_apply` ＋ `end_block_pick`·同上之矩形·試算 G 皆小 ⇒ 各列皆未達）：
           P1 A [0,2] 滿深、X [2,10] ⇒ A 臨端線 30、指數 0.742857；X 0、0.257143（⛔ 計正面道路之長）；P2 A1 [0,5]×[0,10]、
           A2 [0,5]×[10,30] ⇒ 0.333333／0.666667；P3 紀錄之 `端線(m)` ＝ 30.0；P4 旋轉鏡射 TWD97 ⇒ P1 之值同；P5 未給 BASELINE ⇒
           列之 `臨端線(m)`／`評選指數` 皆 None。
           〔補令一 ″·W-1〕P6 條片 S(1) [0,0.04]（跨占 1.2）居端、A(1) [0.04,4] ⇒ 端線之每一小段唯歸原位次最先之一宗：
           S 30／0.406857、A 0／0.593143（⛔ 二邊各計 ⇒ S 60；⛔ 一段二宗並計；⛔ 依暫編地號歸 A）；P7 P6 之旋轉鏡射 TWD97 ⇒ 同；
           P8 條片 [0,0.03]（跨占 0.9 ⛔ 計）⇒ A 30／0.994857；P9 P6 之諸列之臨端線之和 30 ≤ 端線 30、指數之和 1.0。
           〔補令一 ″·W-3〕P10 FRONT 之該端點距外框 0.08（BASELINE 已給）⇒ `end_block_apply` 照行（⛔ 停機）：紀錄之 `端線(m)`
           None、`端線之誤` 載「距街廓外框」、列之指數 None、各列之結果與當選 ＝ 未給 BASELINE 者；P11 BASELINE 畫於屁股線外
           0.08 ⇒ 同（「未觸 BASELINE」）；P12 `end_block_eval_rows` 之說明：P10 之端載「端線 — m（無從定：」、P1 之端載
           「端線 30.0 m；」。
           〔補令二 ‴·審查 WARNING-1〕「臨」以該宗之土地判之（∩ R_end 之多邊形之部·經開運算 1e-05 m ⇒ 寬不及 0.02 mm 之刺⛔ 臨）：
           P13 A(1)（原位次先）[0.06,4] 之外另有寬 0.01 mm 之 L 形之刺（沿端線 y∈[10,20]）、條片 S(1) [0,0.06]（寬 6 cm ＞ 5 cm）
           ⇒ A 0／0.589715、S 30／0.410286（⛔ A 以其刺得 10）；P14 刺寬 0.03 mm ⇒ A 10／0.723049、S 20／0.276952（刺逾 0.02 mm ⇒
           其所臨照計）；P15、P16 ＝ P13、P14 之旋轉 37°·鏡射·TWD97 ⇒ 同（期值皆手算：跨占 A ＝ 3.44×30 ＋ 0.06w ＋ w(10 − w)）；
           P17 合法之淺角楔形：W1(1)（原位次先）＝ [0,4]×[20.1,30] ∪ 其下沿端線之楔（端線與自 E (0,20) 起夾 0.5° 之邊之間·
           y∈[20,20.1]·寬 ≤ 0.87 mm）、W2(1) ＝ 其餘（[0,4]×[0,20] ∪ 楔之右）⇒ W1 10／0.331334、W2 20／0.668666（楔之尖寬不及
           0.02 mm 之長唯 2.3 mm ⇒ 小段 [20,20.1] 仍歸 W1·⛔ 以 1 mm 之開運算去全楔 ⇒ W1 9.9、W2 20.1）；P18 ＝ P17 之旋轉鏡射 TWD97 ⇒ 同。
           丙（`k960_idx_rank`）：R1 合併群合計（g1：0.3＋0.2 ＞ B 0.45）；R2 平手（4 位同）⇒ 首列先者先（⛔ 依暫編地號）；
           R3 非未達之列⛔ 計；R4 無歸戶之片自成一單位；R5 未達之列之指數 None ⇒ 停機。
           丁（`k960_idx_key`／`k960_idx_first`）：K1 有第 1 名者先於皆無者（⛔ 先比名次之和）；K2 第 1 名之端數多者先；K3 皆一端
           第 1 ⇒ 面積大者先；K4 面積同 ⇒ 指數之和大者先；K5 皆同 ⇒ 暫編地號小者先（⛔ 置之於面積之前）；K6 皆無第 1 名 ⇒ 名次之和
           小者先（⛔ 先比面積）；K7 唯計共同之端（一方獨有之端之第 1 名⛔ 計）；K8 同一片見於二共同之端 ⇒ 面積計一次；
           K9 缺評選 ⇒ 停機；K10 無共同之端 ⇒ 停機。
           戊（`end_block_merge_run`〔其內 `k6b_stage3_run` 為真〕·玩具同 F39 之 `_w2`：BE、BF 隔道路 RX）：
           M1 V1 之地（G 之和 戊 81 ＞ 丁 63）而丁於二端皆第 1 名 ⇒ 丁先：丁得 E、戊得 F（⛔ 依 G 之和〔KL 所改之「二甲」〕）；
           M2 V4 之地（G、重劃前面積皆同）而戊於二端皆第 1 名 ⇒ 戊先：戊得 E、F 強制（⛔ 依暫編地號）；
           M3 各一端第 1 名、G 同、丁之重劃前面積小（66 ＜ 72）⇒ 戊先；M4 換名（街廓名之序反之·地號改名）⇒ M1 之結果除名稱外同；
           M5 順序一致（⛔ 互相等待）而列無評選指數 ⇒ 照原位次（⛔ 停機）；M6 互相等待而列無評選指數 ⇒ 停機；
           M7 三位輪流互等·戊兩兩皆先（亦序鍵之先者）⇒ 戊先（同 F39 V5）；M8 三位輪流互等·丁兩兩皆先而序鍵之先者為戊 ⇒
           丁先（⛔ 依序鍵）；M9 三位輪流互等·兩兩比較成圈（丁勝戊、戊勝己、己勝丁）⇒ 序鍵之先者戊先（⛔ 依暫編地號〔丁之 D1〕）。
           〔補令一 ″·W-3〕M10 互相等待而一端（BE 左）之端線不可定 ⇒ 停機（訊息載「端線無從定」）；M11 順序一致（⛔ 互相等待）
           而一端之端線不可定 ⇒ 照原位次（＝ M5 之果·⛔ 停機）。
  wiring   <repo> <基準 commit>
           W1 新之頂層名 ＝ `{end_block_end_line, end_block_end_segs, end_block_end_geom, k960_idx_rank, k960_idx_key,
              k960_idx_first, END_BLOCK_LINE_TOL, END_BLOCK_IDX_W_LINE, END_BLOCK_IDX_W_AREA}`（對基準·⛔ 他增、⛔ 減）；
           W2 頂層節點之相異 ＝ W1 ∪ `{end_block_pick, end_block_apply, end_block_host, end_block_eval_rows,
              end_block_merge_run, k6b_stage3_run}`（`end_block_side_geom` ⛔ 改·其包裝之量測器〔F12、F13、F17〕照舊）；W3 `k6b_stage3_run` 之 `_ring395` 呼 `k960_idx_first`、仍取 `序鍵`；
           W4 `end_block_host` 取 `f3_manual_baseline`、呼 `_baseline_pts_from_manual`；W5 所改、所增之節點內⛔ 新增案件字面；
           W6 `verify/` 頂層之 `*.py` 對基準相異 0。
  run      <repo> [<退縮> …]
           harness 實跑本案（預設 `3.5`、`0.0`）：R1 觸發之端 4、各端之 `端線(m)` ＞ 0 且 ≤ 街廓深之 2 倍、各列之評選指數非 None、
           一端之列之指數之和 ≤ 1 ＋ 1e-6；R2 各端之當選 ＝ 主線 `bd7da4d`（`628-34(1)`、`628-34(2)`、`628-23(2)`、`628-4(1)`·
           ⛔ 變）；R3 合併再試之標的 0、競合 0。
rc：0 相符／1 不符／2 用法錯。
"""
import ast, contextlib, copy, io, math, os, re, subprocess, sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:  # noqa: BLE001
    pass

NEW = {"end_block_end_line", "end_block_end_segs", "end_block_end_geom", "k960_idx_rank", "k960_idx_key",
       "k960_idx_first", "END_BLOCK_LINE_TOL", "END_BLOCK_IDX_W_LINE", "END_BLOCK_IDX_W_AREA"}
CHG = NEW | {"end_block_pick", "end_block_apply", "end_block_host", "end_block_eval_rows",
             "end_block_merge_run", "k6b_stage3_run"}
CASE_LIT_RE = re.compile(r"^(R|RD|G)\d+$|^G\d{3}$|^\d{3}(-\d+)*(\(\d+\))?$")
MW, DEP = 3.5, 30.0
H = "住宅區"
EXP_WIN = {"R2": {"right": "628-34(1)"}, "R3": {"left": "628-34(2)"}, "R5": {"right": "628-23(2)"},
           "R6": {"left": "628-4(1)"}}


def _harvest(repo):
    sys.path.insert(0, os.path.join(repo, "verify"))
    from app_harvest import harvest
    with contextlib.redirect_stdout(io.StringIO()):
        ns, fake_st = harvest(os.path.join(repo, "app.py"))
    return ns, fake_st


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


# ───────────────────────── 甲：端線 ─────────────────────────

def _geom(ns, verts, side, frame=ID, p1=(0.0, 0.0), p2=(20.0, 0.0), bl=((-50.0, DEP), (70.0, DEP)), swap=False):
    """玩具街廓 `verts`（未轉換之座標）之一端之 `end_block_side_geom`。swap ⇒ FRONT 反向（p1 ↔ p2、d̂ 反）、端互換。"""
    from shapely.geometry import Polygon
    f, v = frame
    blk = Polygon([f(p) for p in verts])
    if swap:
        c1, c2, dh, sd = p2, p1, (-1.0, 0.0), {"left": "right", "right": "left"}[side]
    else:
        c1, c2, dh, sd = p1, p2, (1.0, 0.0), side
    cad = v((0.0, 1.0))
    blp = None if bl is None else [tuple(f(bl[0])), tuple(f(bl[1]))]
    g = ns["end_block_side_geom"](blk, v(dh), f(c1), f(c2), cad, ns["alloc_normal_axis"](cad), MW, sd, _label="BX")
    return dict(g, **ns["end_block_end_geom"](blk, v(dh), f(c1), f(c2), sd, g["r_end"], blp, _label="BX"))


RECT = [(0, 0), (20, 0), (20, DEP), (0, DEP)]
TRI = [(-5, DEP), (0, 0), (20, 0), (20, DEP)]
INS = [(0, 0), (20, 0), (20, DEP), (8, DEP)]
BENT = [(0, 0), (20, 0), (20, DEP), (0, DEP), (-2, 15)]
CHAM = [(0, 0), (18, 0), (20, 2), (20, DEP), (0, DEP)]
JOG = [(0, 0), (20, 0), (20, DEP), (-3, DEP), (-3, 15), (0, 15)]
L_TRI, L_INS, L_BENT = math.sqrt(925.0), math.sqrt(3.5 ** 2 + 13.125 ** 2), 2.0 * math.sqrt(229.0)


def _cases_e(ns):
    C = []

    def run(name, fn, exp, tol=1e-6):
        try:
            got = fn()
        except Exception as ex:  # noqa: BLE001
            got = ("例外", type(ex).__name__, str(ex)[:160])
        if isinstance(exp, tuple) and exp and exp[0] == "停機":
            ok = isinstance(got, tuple) and got[:1] == ("例外",) and exp[1] in got[2]
        elif isinstance(exp, (int, float)) and isinstance(got, (int, float)):
            ok = abs(float(got) - float(exp)) <= tol
        else:
            ok = got == exp
        C.append((name, got, exp, ok))

    L = lambda verts, side, **kw: _geom(ns, verts, side, **kw)["end_len"]
    run("E1 矩形·左之端線長 30", lambda: L(RECT, "left"), 30.0)
    run("E1′ 矩形·右之端線長 30", lambda: L(RECT, "right"), 30.0)
    run("E1″ 矩形·左之 R_end 105", lambda: _geom(ns, RECT, "left")["r_end_area"], 105.0)
    run("E2 左之未臨正街三角 ⇒ √925", lambda: L(TRI, "left"), L_TRI)
    run("E3 左端線內斜 ⇒ R_end 之端線長 13.5836（⛔ 全邊 31.0483）", lambda: L(INS, "left"), L_INS)
    run("E4 左端線二折 ⇒ 2√229", lambda: L(BENT, "left"), L_BENT)
    run("E5 右端有截角而 p2 為理論角 ⇒ 左仍 30", lambda: L(CHAM, "left"), 30.0)
    for nm, verts, sd, exp in (("E1", RECT, "left", 30.0), ("E2", TRI, "left", L_TRI), ("E3", INS, "left", L_INS),
                               ("E4", BENT, "left", L_BENT), ("E1′", RECT, "right", 30.0)):
        run(f"E6 {nm} 旋轉 37°·鏡射·TWD97", (lambda verts=verts, sd=sd: L(verts, sd, frame=FR)), exp)
        run(f"E6 {nm} FRONT 反向", (lambda verts=verts, sd=sd: L(verts, sd, swap=True)), exp)
    run("E7 BASELINE 未給 ⇒ end_segs／end_len 皆 None",
        lambda: (lambda g: (g["end_segs"], g["end_len"]))(_geom(ns, RECT, "left", bl=None)), (None, None))
    run("E8 該端點距外框 0.049 ⇒ 可", lambda: L(RECT, "left", p1=(-0.049, 0.0)), 30.0)
    run("E8′ 該端點距外框 0.051 ⇒ 停機", lambda: L(RECT, "left", p1=(-0.051, 0.0)), ("停機", "距街廓外框"))
    run("E9 BASELINE 不觸外框 ⇒ 停機", lambda: L(RECT, "left", bl=((-50.0, 40.0), (70.0, 40.0))), ("停機", "觸 BASELINE"))
    run("E10 BASELINE 過該端點 ⇒ 停機", lambda: L(RECT, "left", bl=((-50.0, 0.0), (70.0, 0.0))), ("停機", "已觸 BASELINE"))
    # 〔補令一 ″·W-2〕BASELINE 過屁股線之中點 (10,30) 而偏 a 度
    sk = lambda a: ((10.0 - 100.0, DEP - 100.0 * math.tan(math.radians(a))), (10.0 + 100.0, DEP + 100.0 * math.tan(math.radians(a))))
    T05 = DEP - 10.0 * math.tan(math.radians(0.5))
    run("E11 偏 0.5° ⇒ 右 30（⛔ 33.5）", lambda: L(RECT, "right", bl=sk(0.5)), 30.0)
    run("E11 偏 0.5° ⇒ 左 30 − 10·tan0.5°", lambda: L(RECT, "left", bl=sk(0.5)), T05)
    for sd, exp in (("right", 30.0), ("left", T05)):
        run(f"E11′ 偏 0.5°·{sd}·旋轉 37°·鏡射·TWD97", (lambda sd=sd: L(RECT, sd, bl=sk(0.5), frame=FR)), exp)
        run(f"E11′ 偏 0.5°·{sd}·FRONT 反向", (lambda sd=sd: L(RECT, sd, bl=sk(0.5), swap=True)), exp)
    run("E12 偏 −0.5° ⇒ 左 30", lambda: L(RECT, "left", bl=sk(-0.5)), 30.0)
    run("E12 偏 −0.5° ⇒ 右 30 − 10·tan0.5°", lambda: L(RECT, "right", bl=sk(-0.5)), T05)
    run("E13 偏 1.9°（未逾 2°）⇒ 右 30", lambda: L(RECT, "right", bl=sk(1.9)), 30.0)
    run("E13′ 偏 2.1°（逾 2°·依字面）⇒ 右 33.5", lambda: L(RECT, "right", bl=sk(2.1)), 33.5)

    def jog():
        from shapely.geometry import Polygon
        ln = ns["end_block_end_line"](Polygon(JOG), (0.0, 0.0), (20.0, 0.0), [(-50.0, DEP), (70.0, DEP)], _label="BX")
        return ln.length
    run("E14 端之外框有與 BASELINE 平行而遠之折 ⇒ 端線 33（⛔ 止於其折）", jog, 33.0)
    run("E15 BASELINE ∥ 屁股線而外移 0.049 ⇒ 30", lambda: L(RECT, "left", bl=((-50.0, DEP + 0.049), (70.0, DEP + 0.049))), 30.0)
    run("E15 BASELINE ∥ 屁股線而外移 0.051 ⇒ 停機",
        lambda: L(RECT, "left", bl=((-50.0, DEP + 0.051), (70.0, DEP + 0.051))), ("停機", "觸 BASELINE"))
    return C


# ───────────────────────── 乙：評選指數之列 ─────────────────────────

def _e(pid, coords, frame):
    f, _v = frame
    return {"tp": {"暫編地號": pid, "原地號": pid.split("(")[0], "polygon_coords": [list(map(float, f(c))) for c in coords]},
            "pre_position": 0, "is_corner_winner": False, "side": "中段"}


def _R(x0, x1, y0=0.0, y1=DEP):
    return [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]


def _rows(ns, parts, frame=ID, baseline=True, fy=0.0, bly=DEP, full=False):
    """長 40 之矩形·二端皆無側街·試算 G 皆 1 ⇒ 各列未達·准強制。回 (左之列, 左之紀錄)。
    〔補令一 ″〕fy ＝ FRONT 之二端點之 y（外框之 y ＝ 0）；bly ＝ BASELINE 之 y；full ⇒ 回 (左之列, 左之紀錄, cache)。"""
    from shapely.geometry import Polygon
    f, v = frame
    blk = Polygon([f(p) for p in _R(0, 40)])
    cad = v((0.0, 1.0))
    cache = {}
    ns["end_block_apply"]([_e(p, c, frame) for p, c in parts], blk_label="BX", block_poly=blk, d_hat=v((1.0, 0.0)),
                          corner_pt=f((0, fy)), front_p2=f((40, fy)), cad_alloc=cad,
                          allocation_dir=ns["alloc_normal_axis"](cad), min_width=MW,
                          has_side_pk={"left": False, "right": False}, has_side_cad={"left": False, "right": False},
                          corner_range_polys={}, trial=lambda tp, s, w: (1.0, 5.0), cache=cache,
                          allow_forced=lambda s: True,
                          baseline_pts=([tuple(f((-50, bly))), tuple(f((90, bly)))] if baseline else None))
    rec = cache["BX"]["left"]
    out = {r["暫編地號"]: (r.get("臨端線(m)"), r.get("評選指數"), r.get("結果")) for r in rec["候選"]}
    return (out, rec, cache) if full else (out, rec)


P1 = [("A(1)", _R(0, 2)), ("X(1)", _R(2, 10)), ("B(1)", _R(10, 40))]
P2 = [("A1(1)", _R(0, 5, 0, 10)), ("A2(1)", _R(0, 5, 10, DEP)), ("B(1)", _R(5, 40))]
P6 = [("S(1)", _R(0, 0.04)), ("A(1)", _R(0.04, 4)), ("B(1)", _R(4, 40))]
P8 = [("S(1)", _R(0, 0.03)), ("A(1)", _R(0.03, 4)), ("B(1)", _R(4, 40))]


def P13(w):
    """〔補令二 ‴〕A(1)（原位次先）＝ [0.06,4]×[0,30] ∪ 寬 w 之 L 形之刺（[0,0.06]×[20 − w,20] ∪ [0,w]×[10,20]）；S(1) ＝ [0,0.06]。"""
    a = [(0.06, 0), (4, 0), (4, DEP), (0.06, DEP), (0.06, 20), (0, 20), (0, 10), (w, 10), (w, 20 - w), (0.06, 20 - w)]
    return [("A(1)", a), ("S(1)", _R(0, 0.06)), ("B(1)", _R(4, 40))]


_TW = 0.1 * math.tan(math.radians(0.5))
# 〔補令二 ‴〕合法之分割：W1(1)（原位次先）之楔沿端線而下至 E (0,20)（其右邊自 E 與端線夾 0.5° 而上至 F (_TW, 20.1)）；
#   W2(1) ＝ [0,4]×[0,20] ∪ 楔之右（臨端線 [0,20]）
P17 = [("W1(1)", [(0, 20), (_TW, 20.1), (4, 20.1), (4, DEP), (0, DEP)]),
       ("W2(1)", [(0, 0), (4, 0), (4, 20.1), (_TW, 20.1), (0, 20)]), ("B(1)", _R(4, 40))]


def _cases_p(ns):
    C = []

    def run(name, fn, exp):
        try:
            got = fn()
        except Exception as ex:  # noqa: BLE001
            got = ("例外", type(ex).__name__, str(ex)[:160])
        C.append((name, got, exp, got == exp))

    run("P1 A 臨端線 30、指數 0.742857；X 0、0.257143",
        lambda: {k: v for k, v in _rows(ns, P1)[0].items() if k in ("A(1)", "X(1)")},
        {"A(1)": (30.0, 0.742857, "未達"), "X(1)": (0.0, 0.257143, "未達")})
    run("P2 依深切分 ⇒ A1 10／0.333333、A2 20／0.666667",
        lambda: {k: v for k, v in _rows(ns, P2)[0].items() if k in ("A1(1)", "A2(1)")},
        {"A1(1)": (10.0, 0.333333, "未達"), "A2(1)": (20.0, 0.666667, "未達")})
    run("P3 紀錄之端線(m) ＝ 30.0", lambda: _rows(ns, P1)[1].get("端線(m)"), 30.0)
    run("P4 旋轉 37°·鏡射·TWD97 ⇒ P1 之值同",
        lambda: {k: v for k, v in _rows(ns, P1, frame=FR)[0].items() if k in ("A(1)", "X(1)")},
        {"A(1)": (30.0, 0.742857, "未達"), "X(1)": (0.0, 0.257143, "未達")})
    run("P5 未給 BASELINE ⇒ 列之臨端線、評選指數皆 None",
        lambda: {k: v[:2] for k, v in _rows(ns, P1, baseline=False)[0].items() if k in ("A(1)", "X(1)")},
        {"A(1)": (None, None), "X(1)": (None, None)})
    # 〔補令一 ″·W-1〕條片：S 之二長邊皆距端線 5 cm 內、A 之左邊亦然 ⇒ 每一小段唯歸原位次最先者（S）
    E6 = {"S(1)": (30.0, 0.406857, "未達"), "A(1)": (0.0, 0.593143, "未達")}
    run("P6 條片 S 居端 ⇒ S 30／0.406857、A 0／0.593143",
        lambda: {k: v for k, v in _rows(ns, P6)[0].items() if k in ("S(1)", "A(1)")}, E6)
    run("P7 P6 之旋轉 37°·鏡射·TWD97 ⇒ 同",
        lambda: {k: v for k, v in _rows(ns, P6, frame=FR)[0].items() if k in ("S(1)", "A(1)")}, E6)
    run("P8 條片 0.9 ㎡（⛔ 跨占）⇒ A 30／0.994857", lambda: _rows(ns, P8)[0].get("A(1)"), (30.0, 0.994857, "未達"))
    run("P9 P6 之臨端線之和 30、指數之和 1.0（≤ 端線 30、≤ 1）",
        lambda: (lambda o: (round(sum(x[0] for x in o.values()), 6), round(sum(x[1] for x in o.values()), 6)))(_rows(ns, P6)[0]),
        (30.0, 1.0))

    def w3(**kw):
        o, rec = _rows(ns, P1, **kw)
        o0, rec0 = _rows(ns, P1, baseline=False, fy=kw.get("fy", 0.0))
        return (rec.get("端線(m)"), any(t in str(rec.get("端線之誤")) for t in ("距街廓外框", "未觸 BASELINE")),
                {k: x[1] for k, x in o.items()}, {k: x[2] for k, x in o.items()} == {k: x[2] for k, x in o0.items()},
                rec.get("當選") == rec0.get("當選"))
    EW3 = (None, True, {"A(1)": None, "X(1)": None}, True, True)
    run("P10 FRONT 之端點距外框 0.08 ⇒ 照行·端線 None·載其由·指數 None·結果與當選同未給 BASELINE", lambda: w3(fy=-0.08), EW3)
    run("P11 BASELINE 畫於屁股線外 0.08 ⇒ 同 P10", lambda: w3(bly=DEP + 0.08), EW3)

    def disp():
        ev10 = _rows(ns, P1, fy=-0.08, full=True)[2]
        ev1 = _rows(ns, P1, full=True)[2]
        l10 = [x for x in ns["end_block_eval_rows"](ev10)["lines"] if x.startswith("BX 左端")]
        l1 = [x for x in ns["end_block_eval_rows"](ev1)["lines"] if x.startswith("BX 左端")]
        return (len(l10) == 1 and "端線 — m（無從定：" in l10[0], len(l1) == 1 and "端線 30.0 m；" in l1[0])
    run("P12 顯示：端線不可定 ⇒「端線 — m（無從定：」；可定 ⇒「端線 30.0 m；」", disp, (True, True))
    # 〔補令二 ‴·審查 WARNING-1〕寬不及 0.02 mm 之刺⛔ 臨端線（A 原位次先·條片 S 寬 6 cm ⇒ A 之本體之左邊距端線逾 5 cm）
    E13 = {"A(1)": (0.0, 0.589715, "未達"), "S(1)": (30.0, 0.410286, "未達")}
    E14 = {"A(1)": (10.0, 0.723049, "未達"), "S(1)": (20.0, 0.276952, "未達")}
    run("P13 A 之刺寬 0.01 mm ⇒ A 0／0.589715、S 30／0.410286",
        lambda: {k: v for k, v in _rows(ns, P13(0.00001))[0].items() if k in ("A(1)", "S(1)")}, E13)
    run("P14 A 之刺寬 0.03 mm ⇒ A 10／0.723049、S 20／0.276952",
        lambda: {k: v for k, v in _rows(ns, P13(0.00003))[0].items() if k in ("A(1)", "S(1)")}, E14)
    run("P15 P13 之旋轉 37°·鏡射·TWD97 ⇒ 同",
        lambda: {k: v for k, v in _rows(ns, P13(0.00001), frame=FR)[0].items() if k in ("A(1)", "S(1)")}, E13)
    run("P16 P14 之旋轉 37°·鏡射·TWD97 ⇒ 同",
        lambda: {k: v for k, v in _rows(ns, P13(0.00003), frame=FR)[0].items() if k in ("A(1)", "S(1)")}, E14)
    E17 = {"W1(1)": (10.0, 0.331334, "未達"), "W2(1)": (20.0, 0.668666, "未達")}
    run("P17 淺角楔形（0.5°）之尖屬原位次先之 W1 ⇒ W1 10／0.331334、W2 20／0.668666（⛔ W1 9.9、W2 20.1）",
        lambda: {k: v for k, v in _rows(ns, P17)[0].items() if k in ("W1(1)", "W2(1)")}, E17)
    run("P18 P17 之旋轉 37°·鏡射·TWD97 ⇒ 同",
        lambda: {k: v for k, v in _rows(ns, P17, frame=FR)[0].items() if k in ("W1(1)", "W2(1)")}, E17)
    return C


# ───────────────────────── 丙：名次 ─────────────────────────

def _cases_r(ns):
    C = []
    rk = ns["k960_idx_rank"]

    def run(name, fn, exp):
        try:
            got = fn()
        except Exception as ex:  # noqa: BLE001
            got = ("例外", type(ex).__name__, str(ex)[:160])
        if isinstance(exp, tuple) and exp and exp[0] == "停機":
            ok = isinstance(got, tuple) and got[:1] == ("例外",) and exp[1] in got[2]
        else:
            ok = got == exp
        C.append((name, got, exp, ok))

    r = lambda pid, idx, res="未達": {"暫編地號": pid, "評選指數": idx, "結果": res}
    nm = lambda out: {str(k): (v["名次"], v["指數"]) for k, v in out.items()}
    G1 = {"a(1)": ("群", 0), "c(1)": ("群", 0), "b(1)": ("群", 1)}
    run("R1 合併群合計（g1 0.3＋0.2 ＝ 0.5 ＞ B 0.45）",
        lambda: nm(rk([r("a(1)", 0.3), r("b(1)", 0.45), r("c(1)", 0.2)], G1)),
        {str(("群", 0)): (1, 0.5), str(("群", 1)): (2, 0.45)})
    run("R2 平手（4 位同 0.40001／0.40004）⇒ 首列先者先（⛔ 依暫編地號：z 在前）",
        lambda: nm(rk([r("z(1)", 0.40001), r("a(1)", 0.40004)], {})),
        {str(("單", "z(1)")): (1, 0.40001), str(("單", "a(1)")): (2, 0.40004)})
    run("R3 非未達之列（歸街角側、歸他端）⛔ 計",
        lambda: nm(rk([r("a(1)", 0.9, "跨占街角規定範圍·歸街角側"), r("b(1)", 0.2), r("c(1)", 0.8, "歸他端")], {})),
        {str(("單", "b(1)")): (1, 0.2)})
    run("R4 無歸戶之片自成一單位（同群之 a、c 合計 0.5 ＞ 單 d 0.45）",
        lambda: nm(rk([r("d(1)", 0.45), r("a(1)", 0.25), r("c(1)", 0.25)], G1)),
        {str(("群", 0)): (1, 0.5), str(("單", "d(1)")): (2, 0.45)})
    run("R5 未達之列之指數 None ⇒ 停機", lambda: rk([r("a(1)", None)], {}), ("停機", "評選指數取不到"))
    return C


# ───────────────────────── 丁：K-9-28 之序 ─────────────────────────

def _c(p, ev):
    return {"p": p, "評選": {k: {"名次": v[0], "指數": v[1], "片": list(v[2])} for k, v in ev.items()}}


def _cases_k(ns):
    C = []
    kf = ns["k960_idx_first"]

    def run(name, fn, exp):
        try:
            got = fn()
        except Exception as ex:  # noqa: BLE001
            got = ("例外", type(ex).__name__, str(ex)[:160])
        if isinstance(exp, tuple) and exp and exp[0] == "停機":
            ok = isinstance(got, tuple) and got[:1] == ("例外",) and exp[1] in got[2]
        else:
            ok = got == exp
        C.append((name, got, exp, ok))

    E, F, G = ("BE", "左"), ("BF", "左"), ("BG", "左")
    pa = {"x1": 10.0, "x2": 10.0, "x3": 10.0, "y1": 30.0, "y2": 30.0, "y3": 30.0}
    first = lambda X, Y, a=pa: kf(X, Y, a)[0]["p"]
    run("K1 有第 1 名者（X：1、3）先於皆無者（Y：2、2·名次和 4 ＝ X·面積 Y 大）",
        lambda: first(_c("x1", {E: (1, 0.5, ["x1"]), F: (3, 0.1, ["x2"])}),
                      _c("y1", {E: (2, 0.3, ["y1"]), F: (2, 0.3, ["y2"])})), "x1")
    run("K2 第 1 名之端數多者先（X 二端、Y 一端·面積 Y 大）",
        lambda: ns["k960_idx_key"](_c("x1", {E: (1, 0.5, ["x1"]), F: (1, 0.5, ["x2"]), G: (2, 0.1, ["x3"])}), [E, F, G], pa)
        < ns["k960_idx_key"](_c("y1", {E: (2, 0.3, ["y1"]), F: (2, 0.3, ["y2"]), G: (1, 0.6, ["y3"])}), [E, F, G], pa), True)
    run("K3 皆一端第 1 ⇒ 面積大者（Y 60 ＞ X 20）先",
        lambda: first(_c("x1", {E: (1, 0.9, ["x1"]), F: (2, 0.4, ["x2"])}),
                      _c("y1", {E: (2, 0.1, ["y1"]), F: (1, 0.5, ["y2"])})), "y1")
    pq = {"x1": 30.0, "x2": 30.0, "y1": 30.0, "y2": 30.0}
    run("K4 面積同（60）⇒ 指數之和大者（X 1.3 ＞ Y 0.6）先",
        lambda: first(_c("y1", {E: (2, 0.1, ["y1"]), F: (1, 0.5, ["y2"])}),
                      _c("x1", {E: (1, 0.9, ["x1"]), F: (2, 0.4, ["x2"])}), pq), "x1")
    run("K5 皆同 ⇒ 暫編地號小者（x1）先（⛔ 置暫編地號於面積之前：y 面積大而後）",
        lambda: (first(_c("y1", {E: (2, 0.5, ["y1"]), F: (1, 0.5, ["y2"])}),
                       _c("x1", {E: (1, 0.5, ["x1"]), F: (2, 0.5, ["x2"])}), pq),
                 first(_c("x1", {E: (1, 0.5, ["x1"]), F: (2, 0.5, ["x2"])}),
                       _c("y1", {E: (2, 0.5, ["y1"]), F: (1, 0.5, ["y2"])}), pa)), ("x1", "y1"))
    run("K6 皆無第 1 名 ⇒ 名次之和小者（X 2＋2 ＜ Y 2＋3）先（⛔ 先比面積：Y 大）",
        lambda: first(_c("y1", {E: (3, 0.2, ["y1"]), F: (2, 0.2, ["y2"])}),
                      _c("x1", {E: (2, 0.1, ["x1"]), F: (2, 0.1, ["x2"])})), "x1")
    run("K7 唯計共同之端（X 於 G 第 1 而 G 非共同 ⇒ ⛔ 計；E、F 皆無第 1 ⇒ 名次和 X 6 ＞ Y 5 ⇒ Y 先）",
        lambda: first(_c("x1", {E: (3, 0.2, ["x1"]), F: (3, 0.2, ["x2"]), G: (1, 0.9, ["x3"])}),
                      _c("y1", {E: (2, 0.3, ["y1"]), F: (3, 0.2, ["y2"])})), "y1")
    run("K8 同一片 x1 見於二共同之端 ⇒ 面積計一次（X 10 ＜ Y 15 ⇒ Y 先）",
        lambda: first(_c("x1", {E: (1, 0.5, ["x1"]), F: (2, 0.5, ["x1"])}),
                      _c("y1", {E: (2, 0.5, ["y1"]), F: (1, 0.5, ["y2"])}), {"x1": 10.0, "y1": 7.5, "y2": 7.5}), "y1")
    run("K9 缺評選 ⇒ 停機", lambda: first({"p": "x1", "評選": None}, _c("y1", {E: (1, 0.5, ["y1"])})),
        ("停機", "缺末端塊評選指數"))
    run("K10 無共同之端 ⇒ 停機", lambda: first(_c("x1", {E: (1, 0.5, ["x1"])}), _c("y1", {F: (1, 0.5, ["y1"])})),
        ("停機", "無共同跨占之端"))
    return C


# ───────────────────────── 戊：end_block_merge_run ─────────────────────────

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
                ok = g(by[c]) >= cfg["thr"]
                rows.append({"暫編地號": c, "原地號": by[c]["原地號"], "跨占R_end(㎡)": 10.0,
                             "評選指數": (cfg["idx"].get(c) if "idx" in cfg else None),
                             "試算G(㎡)": round(g(by[c]), 2), "臨正街寬(m)": 5.0, "結果": "當選" if ok else "未達"})
                if ok:
                    win = c
                    break
            out.setdefault(blk, {})[sd] = {"觸發": True, "R_end(㎡)": cfg["thr"], "候選": rows, "當選": win}
            if cfg.get("err"):          # 〔補令一 ″·W-3〕該端之端線不可定
                out[blk][sd]["端線之誤"] = cfg["err"]
        return out

    def alloc_state(temp, build):
        kept = {}
        for b in build:
            kept.setdefault(b["所屬街廓"], set()).add(b["暫編地號"])
        return {"kept": kept, "bad_pools": {}, "err": None, "G": {b["暫編地號"]: g(b) for b in build}}
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


def _w2(a, area=None, nm=None):
    """同 F39 之 `_w2`：BE（y∈[0,30]）、BF（y∈[-40,-10]）隔道路 RX（中心線 y ＝ -5）。丁：D1(1) BE [0,5]、Dr(1) RX、
    D2(1) BF；戊：U1(1)、Ur(1)、U2(1) 於 [5,10]；他人 P／R0／Q 於 [10,40]。"""
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
    return t, own, blocks, {RX: [(-10.0, -5.0), (50.0, -5.0)]}


def _t2(order_e, order_f, idx_e=None, idx_f=None, nm=None, err_e=None):
    nm = nm or {}
    n = lambda s: nm.get(s, s)
    e = dict(thr=90, cands=[n(x) for x in order_e])
    if err_e:
        e["err"] = err_e
    f = dict(thr=180, cands=[n(x) for x in order_f])
    if idx_e is not None:
        e["idx"] = {n(k): v for k, v in idx_e.items()}
    if idx_f is not None:
        f["idx"] = {n(k): v for k, v in idx_f.items()}
    return {(n("BE"), "left"): e, (n("BF"), "left"): f}


def _w3():
    """同 F39 之 `_w3`：BE、BF（BE 之下·直接相鄰）、BG（右·直接相鄰）；無道路。丁：D1(1) BE、Dg(1) BG；戊：U1(1) BE、
    U2(1) BF；己：J2(1) BF、Jg(1) BG。"""
    t = [_tp("U1(1)", "BE", H, [(0, 0), (10, 0), (10, 30), (0, 30)], 30),
         _tp("D1(1)", "BE", H, [(30, 0), (40, 0), (40, 30), (30, 30)], 20),
         _tp("U2(1)", "BF", H, [(0, -30), (10, -30), (10, 0), (0, 0)], 30),
         _tp("J2(1)", "BF", H, [(30, -30), (40, -30), (40, 0), (30, 0)], 25),
         _tp("Dg(1)", "BG", H, [(40, 0), (50, 0), (50, 30), (40, 30)], 20),
         _tp("Jg(1)", "BG", H, [(40, -30), (50, -30), (50, 0), (40, 0)], 25)]
    own = {"D1": "g丁", "Dg": "g丁", "U1": "g戊", "U2": "g戊", "J2": "g己", "Jg": "g己"}
    blocks = {"BE": {"category": H}, "BF": {"category": H}, "BG": {"category": H}}
    return t, own, blocks, {}


V1A = dict(D1=36, D2=27, Dr=60, U1=45, U2=36, Ur=150)
V4A = dict(D1=36, D2=36, Dr=60, U1=36, U2=36, Ur=150)
# 期值（手算·見本單附錄之示範街廓）：丁先 ⇒ 丁：① D1 36／D2 27 未成；切半 Dr 30／30 ⇒ 66／57 未成；整片 D1＋Dr 96 ≥ 90 成、
#   D2＋Dr 87 ＜ 180 未成 ⇒ 丁得 E；戊之競合消滅：U1「略·已定案」、U2 ＋ Ur 186 ≥ 180 ⇒ 戊得 F。
EXP_D = ([("D1(1)", "K-9-60 ③", "互相等待 ⇒ 先處理"), ("D1(1)", "②", "成"), ("D2(1)", "②", "未成"),
          ("U1(1)", "—", "略·已定案"), ("U2(1)", "②", "成")], [("BE", "左", "D1(1)"), ("BF", "左", "U2(1)")], {})
# 戊先（V4 之地）⇒ 戊：① 未成；切半 Ur 75／75 ⇒ U1 111 ≥ 90 成、U2 111 ＜ 180 未成 ⇒ 戊得 E（U2 依原位次而其半併之）；
#   丁：D1「略·已定案」、D2 ＋ Dr 96 ＜ 180 未成 ⇒ F 皆未達。
EXP_U = ([("U2(1)", "K-9-60 ③", "互相等待 ⇒ 先處理"), ("U1(1)", "②半", "成"), ("U2(1)", "②半", "未成"),
          ("D1(1)", "—", "略·已定案"), ("D2(1)", "②", "未成")], [("BE", "左", "U1(1)")], {"BF": ["left"]})
NM = {"BE": "Z9", "BF": "A1", "RX": "M5", "D1(1)": "77(4)", "D2(1)": "77(9)", "Dr(1)": "77(6)", "U1(1)": "31(2)",
      "U2(1)": "31(8)", "Ur(1)": "31(5)", "P(1)": "50(1)", "R0(1)": "51(1)", "Q(1)": "52(1)",
      "D1": "77", "D2": "77", "Dr": "77", "U1": "31", "U2": "31", "Ur": "31", "P": "50", "R0": "51", "Q": "52"}


def _cases_m(ns):
    C = []

    def run(name, fn, exp):
        try:
            got = fn()
        except Exception as ex:  # noqa: BLE001
            got = ("例外", type(ex).__name__, str(ex)[:160])
        if isinstance(exp, tuple) and exp and exp[0] == "停機":
            ok = isinstance(got, tuple) and got[:1] == ("例外",) and exp[1] in got[2]
        else:
            ok = got == exp
        C.append((name, got, exp, ok))

    D_TOP = dict(idx_e={"D1(1)": 0.6, "U1(1)": 0.3}, idx_f={"U2(1)": 0.3, "D2(1)": 0.6})
    U_TOP = dict(idx_e={"D1(1)": 0.3, "U1(1)": 0.6}, idx_f={"U2(1)": 0.6, "D2(1)": 0.3})
    run("M1 V1 之地（G 之和 戊 81 ＞ 丁 63）而丁於二端皆第 1 ⇒ 丁先：丁得 E、戊得 F",
        lambda: _go(ns, _w2(V1A), _t2(["D1(1)", "U1(1)"], ["U2(1)", "D2(1)"], **D_TOP)), EXP_D)
    run("M2 V4 之地（G、重劃前面積皆同·丁之暫編地號小）而戊於二端皆第 1 ⇒ 戊先：戊得 E、F 皆未達",
        lambda: _go(ns, _w2(V4A), _t2(["D1(1)", "U1(1)"], ["U2(1)", "D2(1)"], **U_TOP)), EXP_U)
    run("M3 各一端第 1、G 同（72）、丁之重劃前面積 66 ＜ 戊 72 ⇒ 戊先",
        lambda: _go(ns, _w2(dict(D1=30, D2=36, Dr=60, U1=36, U2=36, Ur=150), area={"D1": 6.0}),
                    _t2(["D1(1)", "U1(1)"], ["U2(1)", "D2(1)"], idx_e={"D1(1)": 0.6, "U1(1)": 0.3},
                        idx_f={"U2(1)": 0.6, "D2(1)": 0.3})), EXP_U)
    inv = {v: k for k, v in NM.items() if "(" in k or k in ("BE", "BF", "RX")}

    def m4():
        m, wn, fl = _go(ns, _w2(V1A, nm=NM), _t2(["D1(1)", "U1(1)"], ["U2(1)", "D2(1)"], nm=NM, **D_TOP))
        b = lambda s: inv.get(s, s)
        return (sorted((b(c), l, r) for c, l, r in m), sorted((b(x), e, b(c)) for x, e, c in wn),
                {b(k): v for k, v in (fl or {}).items()})
    run("M4 換名（街廓名之序反之·地號改名）⇒ M1 之結果除名稱外同", m4, (sorted(EXP_D[0]), EXP_D[1], EXP_D[2]))
    run("M5 順序一致（E、F 皆丁先·⛔ 互相等待）而列無評選指數 ⇒ 照原位次（丁得 E、戊得 F）",
        lambda: _go(ns, _w2(V1A), _t2(["D1(1)", "U1(1)"], ["D2(1)", "U2(1)"])),
        ([("D1(1)", "②", "成"), ("D2(1)", "②", "未成"), ("U1(1)", "—", "略·已定案"), ("U2(1)", "②", "成")],
         [("BE", "左", "D1(1)"), ("BF", "左", "U2(1)")], {}))
    run("M6 互相等待而列無評選指數 ⇒ 停機",
        lambda: _go(ns, _w2(V1A), _t2(["D1(1)", "U1(1)"], ["U2(1)", "D2(1)"])), ("停機", "缺末端塊評選指數"))
    big = 10 ** 6
    # 三位：G 之和 丁 40／戊 60／己 50 ⇒ 序鍵之先者 ＝ 戊（同 F39 V5）
    T3 = lambda ie, i_f, ig: {("BE", "left"): dict(thr=big, cands=["D1(1)", "U1(1)"], idx=ie),
                              ("BF", "left"): dict(thr=big, cands=["U2(1)", "J2(1)"], idx=i_f),
                              ("BG", "left"): dict(thr=big, cands=["Jg(1)", "Dg(1)"], idx=ig)}
    EXP5 = ([("U2(1)", "K-9-60 ③", "互相等待 ⇒ 先處理"), ("U2(1)", "—", "未成"), ("U1(1)", "—", "未成"),
             ("Jg(1)", "—", "未成"), ("J2(1)", "—", "未成"), ("D1(1)", "—", "未成"), ("Dg(1)", "—", "未成")],
            [], {"BE": ["left"], "BF": ["left"], "BG": ["left"]})
    # 戊於其二端（E、F）皆第 1、勝丁（共同之端 E）、勝己（共同之端 F）⇒ 兩兩皆勝 ＝ 戊（亦序鍵之先者）
    run("M7 三位輪流互等·戊兩兩皆先（亦序鍵之先者）⇒ 戊先、其餘依原位次",
        lambda: _go(ns, _w3(), T3({"D1(1)": 0.3, "U1(1)": 0.6}, {"U2(1)": 0.6, "J2(1)": 0.3},
                                  {"Jg(1)": 0.5, "Dg(1)": 0.4})), EXP5)
    # 丁於 E、G 皆第 1 ⇒ 勝戊（E）、勝己（G）⇒ 兩兩皆勝 ⇒ 丁先（序鍵之先者戊⛔ 用）。期值（手算·本單附錄丁之二）：
    #   環成於 Dg 之至；丁先 ⇒ 持丁之夥伴之列 Dg 之己之競合延後（Jg 退至 Dg 之後）⇒ Dg 至 ⇒ 丁之競合（D1、Dg·皆未成）⇒
    #   U1 回列 ⇒ 戊之競合（U2、U1）⇒ J2 回列而為己之首列 ⇒ Jg 至 ⇒ 己之競合（J2、Jg）。
    EXP8 = ([("D1(1)", "K-9-60 ③", "互相等待 ⇒ 先處理"), ("D1(1)", "—", "未成"), ("Dg(1)", "—", "未成"),
             ("U2(1)", "—", "未成"), ("U1(1)", "—", "未成"), ("J2(1)", "—", "未成"), ("Jg(1)", "—", "未成")],
            [], {"BE": ["left"], "BF": ["left"], "BG": ["left"]})
    run("M8 三位輪流互等·丁兩兩皆先（序鍵之先者為戊）⇒ 丁先",
        lambda: _go(ns, _w3(), T3({"D1(1)": 0.6, "U1(1)": 0.3}, {"U2(1)": 0.6, "J2(1)": 0.3},
                                  {"Jg(1)": 0.3, "Dg(1)": 0.6})), EXP8)
    # 成圈：丁勝戊（E）、戊勝己（F）、己勝丁（G）⇒ 無兩兩皆先者 ⇒ 序鍵（G 之和 丁 40／戊 60／己 50）⇒ 戊先（＝ EXP5）
    run("M9 三位輪流互等·兩兩比較成圈 ⇒ 序鍵之先者（戊）先（⛔ 依暫編地號）",
        lambda: _go(ns, _w3(), T3({"D1(1)": 0.6, "U1(1)": 0.3}, {"U2(1)": 0.6, "J2(1)": 0.3},
                                  {"Jg(1)": 0.6, "Dg(1)": 0.3})), EXP5)
    # 〔補令一 ″·W-3〕
    ERR = "🔴 end_block_end_line[BE·left]：FRONT 之該端點距街廓外框 0.0800 m，逾容差 0.05 m"
    run("M10 互相等待而 BE 左之端線不可定 ⇒ 停機（載「端線無從定」）",
        lambda: _go(ns, _w2(V1A), _t2(["D1(1)", "U1(1)"], ["U2(1)", "D2(1)"], err_e=ERR, **D_TOP)), ("停機", "端線無從定"))
    run("M11 順序一致（⛔ 互相等待）而 BE 左之端線不可定 ⇒ 照原位次（＝ M5）",
        lambda: _go(ns, _w2(V1A), _t2(["D1(1)", "U1(1)"], ["D2(1)", "U2(1)"], err_e=ERR, **D_TOP)),
        ([("D1(1)", "②", "成"), ("D2(1)", "②", "未成"), ("U1(1)", "—", "略·已定案"), ("U2(1)", "②", "成")],
         [("BE", "左", "D1(1)"), ("BF", "左", "U2(1)")], {}))
    return C


def selftest(repo):
    ns, _fst = _harvest(repo)
    red, n_all = [], 0
    for grp, fn in (("甲", _cases_e), ("乙", _cases_p), ("丙", _cases_r), ("丁", _cases_k), ("戊", _cases_m)):
        try:
            cs = fn(ns)
        except Exception as ex:  # noqa: BLE001
            print(f"  🔴 {grp} 例外 {type(ex).__name__}：{str(ex)[:200]}")
            red.append(f"{grp}·例外")
            continue
        for name, got, exp, ok in cs:
            n_all += 1
            print(("  ✅ " if ok else "  🔴 ") + f"{grp} {name}" + ("" if ok else f"｜得 {got!r}｜期 {exp!r}"))
            if not ok:
                red.append(name.split()[0])
    print(f"  P0 判式自驗 {n_all - len(red)}／{n_all}")
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


# ───────────────────────── wiring ─────────────────────────

def _top(src):
    t = ast.parse(src)
    out = {}
    for n in t.body:
        if isinstance(n, (ast.FunctionDef, ast.ClassDef)):
            out[n.name] = ast.dump(n)
        elif isinstance(n, ast.Assign):
            for tg in n.targets:
                for nm in ([tg] if isinstance(tg, ast.Name) else list(getattr(tg, "elts", []))):
                    if isinstance(nm, ast.Name):
                        out[nm.id] = ast.dump(n)
    return out


def _git(repo, *a):
    r = subprocess.run(["git", "-C", repo] + list(a), capture_output=True)
    return r.stdout.decode("utf-8", "replace") if r.returncode == 0 else None


def _fn(src, name):
    for n in ast.parse(src).body:
        if isinstance(n, ast.FunctionDef) and n.name == name:
            return n
    return None


def _lits(node):
    s = set()
    for x in ast.walk(node):
        if isinstance(x, ast.Constant) and isinstance(x.value, str) and CASE_LIT_RE.match(x.value):
            s.add(x.value)
    return s


def wiring(repo, base):
    red = []

    def rep(k, ok, msg):
        print(("  ✅ " if ok else "  🔴 ") + f"{k} {msg}")
        if not ok:
            red.append(k)
    cur = open(os.path.join(repo, "app.py"), encoding="utf-8").read()
    old = _git(repo, "show", f"{base}:app.py")
    if old is None:
        print(f"  🔴 W0 取不到基準 {base}:app.py")
        print("⇒ 紅 ['W0']；rc 1")
        return 1
    tc, to = _top(cur), _top(old)
    add, gone = set(tc) - set(to), set(to) - set(tc)
    rep("W1", add == NEW and not gone, f"新之頂層名 {sorted(add)}（期 {sorted(NEW)}）、去者 {sorted(gone)}（期 []）")
    dif = {k for k in set(tc) | set(to) if tc.get(k) != to.get(k)}
    rep("W2", dif == CHG, f"頂層節點之相異 {sorted(dif)}（期 {sorted(CHG)}）")
    st = _fn(cur, "k6b_stage3_run")
    ring = None
    for x in ast.walk(st) if st is not None else ():
        if isinstance(x, ast.FunctionDef) and x.name == "_ring395":
            ring = x
    calls = {getattr(c.func, "id", None) for c in ast.walk(ring) if isinstance(c, ast.Call)} if ring is not None else set()
    strs = {c.value for c in ast.walk(ring) if isinstance(c, ast.Constant) and isinstance(c.value, str)} if ring else set()
    rep("W3", ring is not None and "k960_idx_first" in calls and "序鍵" in strs,
        f"`_ring395` 呼 k960_idx_first {'k960_idx_first' in calls}、取 序鍵 {'序鍵' in strs}")
    hs = _fn(cur, "end_block_host")
    hstr = {c.value for c in ast.walk(hs) if isinstance(c, ast.Constant) and isinstance(c.value, str)} if hs else set()
    hcal = {getattr(c.func, "id", None) for c in ast.walk(hs) if isinstance(c, ast.Call)} if hs else set()
    rep("W4", "f3_manual_baseline" in hstr and "_baseline_pts_from_manual" in hcal,
        f"`end_block_host` 取 f3_manual_baseline {'f3_manual_baseline' in hstr}、呼 _baseline_pts_from_manual "
        f"{'_baseline_pts_from_manual' in hcal}")
    newlits = {}
    for k in sorted(CHG):
        nc = _fn(cur, k)
        no = _fn(old, k)
        if nc is None:
            continue
        d = _lits(nc) - (_lits(no) if no is not None else set())
        if d:
            newlits[k] = sorted(d)
    rep("W5", not newlits, f"所改、所增之節點內新增之案件字面 {newlits}（期 {{}}）")
    out = _git(repo, "diff", "--name-only", base, "--", ":(glob)verify/*.py")
    chg = [x for x in (out or "").split("\n") if x]
    rep("W6", out is not None and not chg, f"verify/ 頂層之 *.py 對基準相異 {chg}（期 []）")
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


# ───────────────────────── run ─────────────────────────

def _one(repo, sb):
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
        bad = []
        for b, s in trig:
            r = ev[b][s]
            el = r.get("端線(m)")
            rows = r.get("候選") or []
            tot = sum(float(x["評選指數"]) for x in rows if x.get("評選指數") is not None)
            if not (isinstance(el, (int, float)) and 0 < float(el) <= 2 * 60.0) or \
                    any(x.get("評選指數") is None for x in rows) or tot > 1.0 + 1e-6:
                bad.append((b, s, el, tot))
            print(f"     {b} {s}：端線 {el} m；列 {[(x['暫編地號'], x.get('臨端線(m)'), x.get('評選指數')) for x in rows]}")
        ok1 = len(trig) == 4 and not bad and res.get("err") is None
        print(("  ✅ " if ok1 else "  🔴 ") + f"R1@{sb} 觸發之端 {len(trig)}（期 4）、端線或指數之不合 {bad}（期 []）、"
              f"err {res.get('err')!r}")
        if not ok1:
            red.append(f"R1@{sb}")
        wins = {b: {s: ev[b][s].get("當選")} for b, s in trig}
        ok2 = wins == EXP_WIN
        print(("  ✅ " if ok2 else "  🔴 ") + f"R2@{sb} 各端之當選 {wins}（期 {EXP_WIN}）")
        if not ok2:
            red.append(f"R2@{sb}")
        ok3 = isinstance(mr, dict) and mr.get("標的") == [] and not mr.get("競合")
        print(("  ✅ " if ok3 else "  🔴 ") + f"R3@{sb} 合併再試之標的 {(mr or {}).get('標的')!r}（期 []）、競合 "
              f"{(mr or {}).get('競合')!r}（期 無）")
        if not ok3:
            red.append(f"R3@{sb}")
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
