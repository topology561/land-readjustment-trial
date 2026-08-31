# -*- coding: utf-8 -*-
r"""**`W-G.9-187` `M-L-2`**：`K-9-12` 矩形容納判定式之**三造判別力**（⛔ 全係合成案）

## 受詞（施工單 `§一 N-2 M-L-2` 逐字）

> 以**合成案**（⛔ 非真資料·置於 `verify/fixtures/`）證其三造：
> ① **明顯可容納** ⇒ `True`；② **明顯不可容納**（面積 < `W×D`）⇒ `False`；
> ③ 🔴 **軸對齊不過、旋轉後可過** ⇒ `True`——**此造係本函式存在之全部理由**
> （`GB-74` 之受詞：剪移吃掉可用寬度·僅在矩形受方向約束時發生）。
> 🛑 **③ 若得 `False` ⇒ 停機上呈**：表示實作實際上仍是軸對齊，與 `K-9-12-c` 不符。

併辦規格書 `§4 ⑤` 之二向注入：
> ① 取一個**已知不可建築**之狹長宗，其容納結果須為 `False`；
> ② 取一個**恰好容納**之合成矩形宗，令 `W` 增 `+0.01 m` ⇒ 須翻為 `False`（**邊界之單調性**）。
> 🔴 **⛔ 不得硬編 `3.5`／`14`**——**驗收須含一個「換路寬級距」之合成案**，證其值隨參數改變。

## 🔒 夾具來源之聲明（`fixture-provenance`）

🔴 **本檔之期望值⛔ 非由新碼現跑回填**——全部係**由構造推導**之封閉解，逐案於註解載其算式：
`③` 之「軸對齊必不過」由「`45°` 帶寬 `t` 內之軸對齊矩形須滿足 `(a+b)/√2 ≤ t`」推得；
`⑤` 之邊界由矩形自身之邊長推得；`⑦` 之 L 形由其臂寬推得。⛔ 無一項係「跑一次看結果再寫進來」。

## ⛔ 本檔不做

⛔ 不改生產碼一字。⛔ 不掛入 `run_all`（其發現機制係**明列 tuple**·⛔ 非 glob ⇒ 本檔
之新增對 `run_all` 之名目集合**零影響**）。⛔ 不寫死本機絕對路徑。⛔ 不用真資料。
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
sys.path.insert(0, VERIFY)
sys.path.insert(0, HERE)

from app_harvest import harvest                                       # noqa: E402

FAILS = []
NOTES = []


def chk(name, got, want, extra=""):
    ok = (got == want)
    if not ok:
        FAILS.append((name, got, want))
    print("  %s %-58s 得 %-6s 期 %-6s %s"
          % ("✅" if ok else "🔴", name, got, want, extra))
    return ok


def main():                                                          # noqa: C901
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8")
        except Exception:                                            # noqa: BLE001
            pass
    from shapely.geometry import Polygon, box
    from shapely import affinity

    print("=" * 104)
    print("【W-G.9-187 M-L-2】K-9-12 矩形容納判定式之判別力（⛔ 全係合成案·⛔ 非真資料）")
    print("=" * 104)

    ns, _ = harvest()
    fit = ns["_rect_fits_free_pose"]
    erode = ns["_rect_fit_erode_axis"]
    sweep = ns["_rect_fit_sweep"]
    gmls = ns["get_min_lot_size"]
    TOL = ns["_RECT_FIT_TOL"]
    print("  取得符號：_rect_fits_free_pose／_rect_fit_erode_axis／_rect_fit_sweep／"
          "get_min_lot_size；_RECT_FIT_TOL = %g" % TOL)
    print()

    # ══ 零、`W`／`D` 一律查表（⛔ 不硬編 3.5／14）══════════════════════════
    print("── 零、`W`／`D` 之來源 ＝ 查表（`K-9-12 二`·⛔ 不硬編）──")
    t10 = gmls("住宅區", 10.0)
    print("  get_min_lot_size('住宅區', 10.0) = %s" % t10)
    W0, D0 = float(t10["min_width"]), float(t10["min_depth"])
    # 換級距之合成案：掃各路寬，取出**與 10.0 m 級距相異**之第一組（⛔ 不硬編級距界）
    alt = None
    for _w in (3.0, 5.0, 6.0, 7.0, 8.0, 12.0, 15.0, 16.0, 20.0, 25.0, 30.0, 40.0):
        _t = gmls("住宅區", _w)
        if (float(_t["min_width"]), float(_t["min_depth"])) != (W0, D0):
            alt = (_w, _t)
            break
    if alt is None:
        FAILS.append(("換級距案不存在", None, "須存在"))
        print("  🔴 掃遍候選路寬皆與 10.0 m 同值 ⇒ **無從分辨「讀表」與「巧合於本案」**")
    else:
        _w, _t = alt
        W1, D1 = float(_t["min_width"]), float(_t["min_depth"])
        print("  get_min_lot_size('住宅區', %.1f) = %s" % (_w, _t))
        chk("換路寬級距 ⇒ (W,D) 確實改變", (W1, D1) != (W0, D0), True,
            "（%.2f×%.2f vs %.2f×%.2f）" % (W0, D0, W1, D1))
        # 同一宗地，兩級距之判定相異 ⇒ 證判定確實隨查表值走
        _p = box(0.0, 0.0, max(W0, W1) + 0.5, max(D0, D1) - 0.5)
        _r0 = fit(_p, W0, D0, _label="tier10")
        _r1 = fit(_p, W1, D1, _label="tier%s" % _w)
        print("     同一合成宗（%.2f×%.2f）之判定：級距10m ⇒ %s ／ 級距%.1fm ⇒ %s"
              % (_p.bounds[2], _p.bounds[3], _r0, _w, _r1))
    print()

    # ══ 一、明顯可容納 ⇒ True ═════════════════════════════════════════════
    print("── 一、明顯可容納（`M-L-2 ①`）──")
    big = box(0.0, 0.0, 20.0, 20.0)          # 20×20 遠大於 W0×D0
    chk("① 20×20 方形容納 %.2f×%.2f" % (W0, D0), fit(big, W0, D0, _label="c1"), True)
    print()

    # ══ 二、明顯不可容納（面積 < W×D）⇒ False ═════════════════════════════
    print("── 二、明顯不可容納（`M-L-2 ②`·面積 < W×D）──")
    small = box(0.0, 0.0, 3.0, 3.0)          # 面積 9 < 3.50×14.00 = 49
    d2 = {}
    chk("② 3×3 方形（面積 %.2f < 需 %.2f）" % (small.area, W0 * D0),
        fit(small, W0, D0, _label="c2", _detail=d2), False, "｜理由：" + str(d2.get("reason")))
    print()

    # ══ 三、🔴 軸對齊不過、旋轉後可過 ⇒ True（本函式存在之全部理由）═══════
    print("── 三、🔴 軸對齊不過／旋轉後可過（`M-L-2 ③`·🛑 停機款 `X-2`）──")
    # 構造：把 4.60 × 1.15 之走廊**整體旋轉 45°**。目標矩形 W=1.00／D=4.00。
    #   ▸ 旋轉後（θ=45°）：1.00 ≤ 1.15 且 4.00 ≤ 4.60 ⇒ **必**可容納。
    #   ▸ 軸對齊（θ=0）：45° 帶之法向寬 t=1.15；軸對齊 a×b 內接於該帶
    #     ⇒ 其在帶法向之投影 (a+b)/√2 ≤ t ⇒ a+b ≤ 1.15×√2 = 1.6263。
    #     而 1.00+4.00 = 5.00 ≫ 1.6263 ⇒ **必**不可容納。（⛔ 封閉解·非跑出來的）
    CW, CD = 1.00, 4.00
    corridor = affinity.rotate(box(0.0, 0.0, 4.60, 1.15), 45.0, origin="centroid")
    bound_axis = 1.15 * math.sqrt(2.0)
    print("  構造：4.60×1.15 走廊旋轉 45°；目標 %.2f×%.2f" % (CW, CD))
    print("  封閉解：軸對齊之上界 a+b ≤ 1.15×√2 = %.4f，而 %.2f+%.2f = %.2f ⇒ 軸對齊必不過"
          % (bound_axis, CW, CD, CW + CD))
    e_axis = erode(corridor, CW - TOL, CD - TOL)
    chk("③-a 軸對齊侵蝕為空（＝軸對齊不過）", bool(e_axis.is_empty), True)
    d3 = {}
    got3 = fit(corridor, CW, CD, _label="c3", _detail=d3)
    ok3 = chk("③-b 🔴 自由姿態可容納（旋轉後可過）", got3, True,
              "｜命中角度 %s" % d3.get("hit_angle_deg"))
    if not ok3:
        print("  🛑🛑 `X-2` 停機款觸發：③ 得 False ⇒ 實作實際上仍是軸對齊，與 `K-9-12-c` 不符")
    # 判別力之反向：把走廊加寬到軸對齊也過 ⇒ ③-a 須轉綠（證 ③-a 非恆真）
    wide = box(0.0, 0.0, 4.60, 4.60)
    chk("③-c 對照組：4.60×4.60 之軸對齊侵蝕**非**空（證 ③-a 非恆真）",
        bool(erode(wide, CW - TOL, CD - TOL).is_empty), False)
    print()

    # ══ 四、已知不可建築之狹長宗 ⇒ False（規格書 §4 ⑤ 判別力 ①）═══════════
    print("── 四、狹長宗（規格書 `§4 ⑤` 注入 ①）──")
    # 170°/10° 狹長地族之合成代表：長 90 m、寬 0.80 m 之細長四邊形（⛔ 非真資料）
    #   🔒 **長度之選定係為使面積 72.00 > W×D = 49.00**——否則其 False 只是「面積必要條件
    #     不成立」之提前否決，**⛔ 證不到幾何判定本身**（本夾具首版即犯此：60×0.80 ＝ 48.00
    #     < 49.00，而輸出仍宣稱「非提前否決」⇒ 敘述與其自身數字矛盾·CC 於入倉前自捕）。
    sliver = Polygon([(0.0, 0.0), (90.0, 0.0), (90.0, 0.80), (0.0, 0.80)])
    d4 = {}
    chk("④ 90×0.80 狹長宗容納 %.2f×%.2f" % (W0, D0),
        fit(sliver, W0, D0, _label="c4", _detail=d4), False)
    _pre = (sliver.area + 1e-12 < W0 * D0)
    chk("④-b 其 False 係**真幾何判定**（⛔ 非面積提前否決）", _pre, False,
        "｜面積 %.2f vs 需 %.2f ／ 理由：%s" % (sliver.area, W0 * D0, d4.get("reason")))
    print()

    # ══ 五、邊界單調性（規格書 §4 ⑤ 注入 ②）════════════════════════════════
    print("── 五、邊界之單調性（規格書 `§4 ⑤` 注入 ②）──")
    exact = box(0.0, 0.0, W0, D0)            # 恰好容納
    chk("⑤-a 恰好 %.2f×%.2f 之宗地容納 %.2f×%.2f" % (W0, D0, W0, D0),
        fit(exact, W0, D0, _label="c5a"), True, "｜（`fit_tol` 使相切判 True）")
    chk("⑤-b 同宗地容納 (W+0.01)×D ⇒ 須翻 False",
        fit(exact, W0 + 0.01, D0, _label="c5b"), False)
    chk("⑤-c 同宗地容納 W×(D+0.01) ⇒ 須翻 False",
        fit(exact, W0, D0 + 0.01, _label="c5c"), False)
    print()

    # ══ 六、凸／非凸二路（證分支非裝飾）═══════════════════════════════════
    print("── 六、凸路與通路之對拍（證分支**非裝飾**·`常規八 二 ②`）──")
    # L 形（非凸）：兩臂寬皆 2.0 ⇒ 其內⛔ 不可能容納 6×6；然其凸包**可以** ⇒ 若誤用
    #   凸路之四頂點交集公式，將得 True（錯）。（⛔ 封閉解：臂寬 2.0 < 6）
    L = Polygon([(0, 0), (10, 0), (10, 2), (2, 2), (2, 10), (0, 10)])
    hull = L.convex_hull
    print("  L 形面積 %.2f ／ 其凸包面積 %.2f ⇒ 非凸（差 %.2f）"
          % (L.area, hull.area, hull.area - L.area))
    chk("⑥-a L 形（臂寬 2.0）容納 6×6", fit(L, 6.0, 6.0, _label="c6a"), False)
    chk("⑥-b 對照：其**凸包**容納 6×6（⇒ 誤用凸路必得 True）",
        fit(hull, 6.0, 6.0, _label="c6b"), True)
    # 凸例上二路須恆等：以 sweep 自行走通路，與 _rect_fit_erode_axis（走凸路）對拍
    from shapely.geometry import box as _bx

    def _erode_general(q, w, d):
        _minx, _miny, _maxx, _maxy = q.bounds
        _m = w + d + 1.0
        _B = _bx(_minx - _m, _miny - _m, _maxx + _m, _maxy + _m)
        return q.difference(sweep(sweep(_B.difference(q), (-w, 0.0)), (0.0, -d)))

    agree = True
    for i, (poly, w, d) in enumerate([
            (box(0, 0, 8, 8), 3.0, 5.0),
            (Polygon([(0, 0), (9, 0), (11, 6), (3, 7)]), 2.0, 4.0),
            (Polygon([(0, 0), (6, -1), (10, 4), (4, 8), (-1, 4)]), 3.0, 3.0)], 1):
        a = erode(poly, w, d)
        b = _erode_general(poly, w, d)
        same = (a.is_empty == b.is_empty) and abs(a.area - b.area) <= 1e-9
        agree &= same
        print("     凸例 %d：凸路面積 %.9f ／ 通路面積 %.9f ⇒ %s"
              % (i, a.area, b.area, "一致 ✅" if same else "🔴 相異"))
    chk("⑥-c 凸例上凸路 ≡ 通路（三例）", agree, True)
    print()

    print("=" * 104)
    if FAILS:
        print("🔴 FAIL %d 項：" % len(FAILS))
        for n, g, w in FAILS:
            print("   - %s：得 %s ／ 期 %s" % (n, g, w))
        return 1
    print("✅ 全部通過（三造 ＋ 二向注入 ＋ 換級距 ＋ 凸/非凸分支）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
