# -*- coding: utf-8 -*-
"""`W-G.9-296` `§三`：`W_0` 重建式之**對生產態驗證**（窄批）。

🔑 **受詞**：以**現行 `buf`** 餵**與 `W_0′` 完全同一**之重建式，須**逐位重現生產態之 `W_0`**。
   🛑 本器**⛔ 判路丙成立與否**——只證**重建式可信**（單 `§三-1` 逐字）。

🔒 **重建式 ＝ 同一份**（⛔ 另寫第二份·單 `§六`）：
   `probe_WG9295_joint._w0`（其為 `verify/stepg_pipeline.py:1023-1036` `_mp_base_W0` 之**純委派式**複刻），
   由本器 `import` 而來；⛔ 於本檔重寫。

🔒 **生產態 `W_0` 之二通道**（⛔ 單靠包裹·`W-G.9-295` 自捕之族）
   **通道②（主）** ＝ `sys.settrace` 攔 `_mp_base_W0`（`co_name` 比對）之 **`return` 事件**，
       取其 `f_locals`（`_gs`／`_buf`／`_dv`／`_mp`／`_adir`）與**回傳值**，並自 `f_back`
       （＝ `_run_step_g_impl`）取 `blk` 與 `_left_buffer_S`／`_right_buffer_S` 以定側。
       🔒 其**⛔ 倚賴 `ns` 之包裹** ⇒ 縱使包裹漏抓亦可得。
   **通道①（佐）** ＝ `probe_WG9292_pathC.drive()` 所置之 `k956_W_from_mp` 包裹之**生產期前綴**。
   🛑 二通道之數**須交叉對拍**；相異即 loud 具名。
   🔒 `stepg:394` `_k956_W_from_mp = ns["k956_W_from_mp"]` 位於 `_run_step_g_impl`（`277`-`1643`）
      ⇒ 係**呼叫期**綁定 ⇒ 包裹確能攔到（本器另以通道② 覆核之）。

🔒 **母體⛔ 含本器自身之輸出**（`§零` 新附款 `(c)`）：通道① 一律限 `drive()` 期間之**前綴**；
   通道② 之 `settrace` 僅於 `drive()` 期間掛載 ⇒ 本器其後之重建呼叫**⛔ 入母體**。

`rc`：`0` 全綠／`5` **量測器紅**（判別力三造不成立）／`6` **受詞紅**（款 `3` 逐位差 `≠ 0`）。
🛑 `rc ≠ 0` ⛔ 等同「受詞紅」；`N = 0` 之格一律 **loud 具名「不可驗／不可得」**。
用法：python verify/probes/probe_WG9296_w0rec.py
"""
import math
import os
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)

import probe_WG9292_pathC as P                      # noqa: E402
import probe_WG9295_joint as J                      # noqa: E402  （重建式 `_w0` 之唯一來源）

W = 132
TAG = "【設計驗算·⛔ 非實測】"
_LOG = []
RED = [0]
BAD = [0]


def say(s=""):
    print(s)
    _LOG.append(s)


def red(s):
    RED[0] = 5
    say("🔴 **量測器紅**：" + s)


def bad(s):
    BAD[0] = 6
    say("🛑 **受詞紅**：" + s)


def ulp_dist(a, b):
    """二 `float` 之 ULP 距離（同號·IEEE754 位元序）。"""
    if a == b:
        return 0
    ia = struct.unpack("<q", struct.pack("<d", a))[0]
    ib = struct.unpack("<q", struct.pack("<d", b))[0]
    if ia < 0:
        ia = -(ia & 0x7FFFFFFFFFFFFFFF) if ia != 0 else 0
    if ib < 0:
        ib = -(ib & 0x7FFFFFFFFFFFFFFF) if ib != 0 else 0
    return abs(ia - ib)


def drive_traced(sb):
    """於 `P.drive(sb)` 期間掛 `settrace`，攔 `_mp_base_W0` 之 `return`。"""
    PROD = []

    def _loc(frame, event, arg):
        if event == "return":
            fl = frame.f_locals
            bk = frame.f_back
            bl = bk.f_locals if bk is not None else {}
            buf = fl.get("_buf")
            side = None
            try:
                if buf is not None and bl.get("_left_buffer_S") is not None \
                        and float(buf) == float(bl.get("_left_buffer_S")):
                    side = "left"
                elif buf is not None and bl.get("_right_buffer_S") is not None \
                        and float(buf) == float(bl.get("_right_buffer_S")):
                    side = "right"
            except Exception:                                    # noqa: BLE001
                side = None
            # 🩸 **自捕**：`_run_step_g_impl` 之街廓變數名為 `blk_label`（⛔ `blk`）；
            #    以 `blk` 取之恆得 `None` ⇒ 逐格比對必失配 ⇒ 偽「不可得」。
            #    ⇒ 取 `blk_label`，並另以 `_buf` 之逐位相等為**第二鍵**交叉對拍。
            PROD.append({"blk": bl.get("blk_label", bl.get("_blk_label")), "side": side,
                         "_gs": fl.get("_gs"), "_buf": buf, "_dv": fl.get("_dv"),
                         "_mp": fl.get("_mp"), "_adir": fl.get("_adir"), "out": arg,
                         "caller": bk.f_code.co_name if bk is not None else None})
        return _loc

    def _glob(frame, event, arg):
        if event == "call" and frame.f_code.co_name == "_mp_base_W0":
            return _loc
        return None

    old = sys.gettrace()
    sys.settrace(_glob)
    try:
        d = P.drive(sb)
    finally:
        sys.settrace(old)
    d["PROD"] = PROD
    d["n_k956_prod"] = len(d["K956"])          # `drive()` 畢之前綴長 ＝ 生產錄
    return d


def analyse(sb, d):
    ns, crp = d["ns"], d["crp"]
    n_k956_0 = d["n_k956_prod"]
    say("")
    say("=" * W)
    say("【`SB` ＝ %s m·態甲】`_mp_base_W0` 之**生產呼叫**（通道②·`settrace`）＝ **%d** 次"
        % (repr(sb), len(d["PROD"])))
    say("　`k956_W_from_mp` 之**生產錄**（通道①·包裹之前綴）＝ **%d** 筆" % n_k956_0)
    say("　`_build_corner_range_v3` **%d** 次（段 **%d**）／`_corner_buffer_S` **%d** 次（段內 **%d**）"
        % (len(d["RNG"]), len(d["RNG"]) - d["n_rng0"], len(d["BUF"]), len(d["BUF"]) - d["n_buf0"]))
    say("　`run_step_g` 之終局 ＝ %s" % (d["err"] or "（未拋）"))
    for i, r in enumerate(d["PROD"]):
        say("　　通道② 錄 `%d`：`blk` ＝ `%r`／側 ＝ `%r`／呼叫者 ＝ `%r`／`_buf` ＝ `%r`／**回傳 ＝ `%r`**"
            % (i, r["blk"], r["side"], r["caller"], r["_buf"], r["out"]))
    say("=" * W)

    grids = []
    for b in P.BLKS:
        L, R = d["fo"][b]
        if L:
            grids.append((b, "left"))
        if R:
            grids.append((b, "right"))
    say("🔒 `forced` 格 ＝ **%d**（%s）" % (len(grids), "、".join("%s/%s" % g for g in grids)))

    rows = []
    for blk, side in grids:
        say("")
        say("─" * W)
        say("### `%s`／`%s`＠`SB = %s`" % (blk, side, repr(sb)))
        br, nb = P._pick(d["BUF"], blk, side)
        rr, nr = P._pick(d["RNG"], blk, side)
        cp = crp.get((blk, side))
        if br is None or rr is None or cp is None:
            red("`%s/%s`：`_corner_buffer_S` 錄 %d／`_build_corner_range_v3` 錄 %d／`corner_range_polys` %s"
                " ⇒ **loud 拒測**" % (blk, side, nb, nr, "有" if cp is not None else "無"))
            continue
        loc = rr["loc"]
        S1_perp = float(loc.get("S1_perp"))
        Tp = tuple(float(x) for x in loc.get("_Tp"))
        su = (float(loc.get("sux")), float(loc.get("suy")))
        bp_, dh_, fp_ = br["block_poly"], br["d_hat"], br["front_p1"]
        ad1, ra, tol, buf1 = br["allocation_dir"], float(br["range_area"]), br["tol"], br["buf"]
        sl = ((d["st"].session_state.get("f3_cad_side_lines_by_side", {}) or {})
              .get(blk, {}) or {}).get(side, {}) or {}
        side_mid = sl.get("mid")

        # ══ 款 5（先出艙·其為款 1 之母體）════════════════════════════════════
        by_lbl = [r for r in d["PROD"] if r["blk"] == blk and r["side"] == side]
        by_buf = [r for r in d["PROD"]
                  if r["_buf"] is not None and float(r["_buf"]) == float(buf1)]
        hits2 = by_lbl or by_buf
        say("  **款 `5`**　包裹之錄（母體⛔ 含本器自身之輸出）")
        say("      通道②（`settrace` `_mp_base_W0`）：本格之生產呼叫 ＝ **%d** 次"
            "（**二鍵並報**：鍵甲 `blk_label`＋側 ＝ **%d**／鍵乙 `_buf` 逐位相等 ＝ **%d**·一致 ＝ %s）"
            % (len(hits2), len(by_lbl), len(by_buf), len(by_lbl) == len(by_buf)))
        if len(by_lbl) != len(by_buf):
            say("      🟡 **二鍵不一致（loud）**——採其**非空者**；鍵甲所見之 `blk_label` ＝ %r"
                % sorted({r["blk"] for r in d["PROD"]}))
        say("      通道①（`k956_W_from_mp` 包裹）：生產錄 ＝ **%d** 筆／本器自身追加 ＝ **%d** 筆"
            "（**後者⛔ 入母體**）" % (n_k956_0, len(d["K956"]) - n_k956_0))

        # ══ 款 1：生產態之 W_0 ═══════════════════════════════════════════════
        say("  **款 `1`**　**生產態**之 `W_0`（自生產路徑當場重得·⛔ 轉引前批）")
        if not hits2:
            say("      🟡 **不可得（loud）**——本格於生產路徑**⛔ 呼叫** `_mp_base_W0`"
                "（其定義處 `verify/stepg_pipeline.py:1023`-`1036` 位於 `else` 分支內，"
                "即 `not _degenerate_order and _N > 1` 方進）⇒ **生產態之 `W_0` 於本格不存在**。")
            w0_prod = None
        else:
            r2 = hits2[-1]
            w0_prod = float(r2["out"])
            say("      通道 ＝ `settrace` 攔 `_mp_base_W0` 之 `return`（呼叫者 ＝ `%r`）；"
                "式 ＝ `_bp0 = _gs + _buf·_du`，`W_0 = k956_W_from_mp(_bp0, _mp, _adir, _dv)`"
                % r2["caller"])
            say("      **生產態 `W_0` ＝ `%r`**" % w0_prod)
            say("      其實參：`_gs` ＝ `%r`／`_buf` ＝ `%r`／`_dv` ＝ `%r`"
                % (tuple(float(x) for x in r2["_gs"]) if r2["_gs"] is not None else None,
                   r2["_buf"],
                   tuple(float(x) for x in r2["_dv"]) if r2["_dv"] is not None else None))
            # 通道① 之佐證
            import numpy as _np
            _du = _np.asarray(r2["_dv"], dtype=float)
            _du = _du / float(_np.linalg.norm(_du))
            _bp0 = _np.asarray(r2["_gs"], dtype=float) + float(r2["_buf"]) * _du
            m = [r for r in d["K956"][:n_k956_0]
                 if float(_np.max(_np.abs(_np.asarray(r["point"], dtype=float)[:2] - _bp0[:2]))) <= 1e-12]
            if m:
                dv = min(abs(float(r["out"]) - w0_prod) for r in m)
                say("      通道① 之交叉對拍：命中 %d 筆·最小差 ＝ `%r` ⇒ %s"
                    % (len(m), dv, "✅ 二通道逐位相同" if dv == 0.0 else "🔴 **二通道相異**"))
                if dv != 0.0:
                    red("`%s/%s`：二通道之生產 `W_0` 相異 ⇒ 量測器紅" % (blk, side))
            else:
                say("      通道① 之交叉對拍：🟡 **無對應之錄**（生產錄 %d 筆）⇒ 只得通道② 之值"
                    % n_k956_0)

        # ══ 款 2：以現行 buf 餵同一重建式 ════════════════════════════════════
        say("  **款 `2`**　以**現行 `buf`** 餵**同一重建式**（`probe_WG9295_joint._w0`·⛔ 另寫第二份）")
        if side_mid is None:
            red("`%s/%s`：`side_mid` ⛔ 可達 ⇒ **loud 拒測**" % (blk, side))
            continue
        w0_rec = J._w0(ns, fp_, buf1, dh_, side_mid, ad1)
        say("      呼叫式 ＝ `J._w0(ns, front_p1, buf, d_hat, side_mid, allocation_dir)`")
        say("      其實參：`front_p1` ＝ `%r`／`buf` ＝ `%r`／`d_hat` ＝ `%r`"
            % (tuple(float(x) for x in fp_), buf1, tuple(float(x) for x in dh_)))
        say("      **`W_0^rec` ＝ `%r`**" % w0_rec)
        if hits2:
            r2 = hits2[-1]
            say("      實參之逐位對拍（重建 vs 生產）：`buf` %s／`_gs`(＝`front_p1`) %s／`_dv`(＝`d_hat`) %s"
                % (float(buf1) == float(r2["_buf"]),
                   tuple(float(x) for x in fp_) == tuple(float(x) for x in r2["_gs"]),
                   tuple(float(x) for x in dh_) == tuple(float(x) for x in r2["_dv"])))

        # ══ 款 3：逐位差 ════════════════════════════════════════════════════
        say("  **款 `3`**　款 `1` 與款 `2` 之**逐位差**（期 ＝ `0.0`）")
        if w0_prod is None:
            say("      🟡 **不可得**——款 `1` 於本格不存在 ⇒ **⛔ 判其為 `0`、⛔ 判其為非 `0`**"
                "（「無從回測」⛔ 等同「回測不過」）")
            k3 = None
        else:
            k3 = w0_rec - w0_prod
            say("      `W_0^rec − W_0^prod` ＝ `%r`／ULP 距離 ＝ `%d` ⇒ %s"
                % (k3, ulp_dist(w0_rec, w0_prod), "✅ 逐位相同" if k3 == 0.0 else "🛑 **相異**"))
            if k3 != 0.0:
                bad("`%s/%s`＠`SB=%s`：款 `3` ＝ `%r`（ULP `%d`）⇒ **停、上呈**·⛔ 放寬"
                    % (blk, side, repr(sb), k3, ulp_dist(w0_rec, w0_prod)))

        # ══ 款 4：路丙之 buf′ → W_0′ ═════════════════════════════════════════
        ad2 = ns["_first_corner_alloc_dir"](side_mid)
        try:
            buf2 = ns["_corner_buffer_S"](bp_, dh_, fp_, ad2, ra, side,
                                          tol=tol, _label="WG9296設計驗算·" + blk)
        except Exception as e:                                   # noqa: BLE001
            red("`%s/%s`：%s `_corner_buffer_S` 拋出 ⇒ %s" % (blk, side, TAG, e))
            continue
        w0_new = J._w0(ns, fp_, buf2, dh_, side_mid, ad2)
        dW = abs(w0_new - S1_perp)
        L_su = J._span(cp, su)
        er, dr = P.far_range_edge(cp, Tp, su)
        L_edge = None if er is None else P._elen(er)
        L = max(x for x in (L_su, L_edge) if x is not None)
        A_lim = 0.005 / L
        okA = dW <= A_lim
        say("  **款 `4`**　%s 路丙之 `buf′` ＝ `%r`（現行 `buf` ＝ `%r`·差 ＝ `%r`）" % (TAG, buf2, buf1, buf2 - buf1))
        say("      %s `W_0′` ＝ `%r`／`S1_perp` ＝ `%r`／**`|W_0′ − S1_perp|` ＝ `%r`**"
            % (TAG, w0_new, S1_perp, dW))
        say("      跨距（`L_su` `%r`／`L_edge` `%r`·取較嚴 ＝ 較大者）＝ `%r`；"
            "`A′` 界 ＝ `0.005 ÷ %r` ＝ `%r`；比值 ＝ `%r` ⇒ %s"
            % (L_su, L_edge, L, L, A_lim, dW / A_lim, "✅" if okA else "🛑 **逾界**"))

        rows.append({"sb": sb, "blk": blk, "side": side, "w0_prod": w0_prod, "w0_rec": w0_rec,
                     "k3": k3, "buf1": buf1, "buf2": buf2, "w0_new": w0_new,
                     "S1_perp": S1_perp, "dW": dW, "A_lim": A_lim, "okA": okA,
                     "n2": len(hits2), "ns_": ns, "fp": fp_, "dh": dh_, "sm": side_mid, "ad1": ad1})
    return rows


def main():
    allrows = []
    for sb in P.SBS:
        allrows += analyse(sb, drive_traced(sb))

    say("")
    say("=" * W)
    say("## 款 `6`　判別力三造之判（母體 ＝ 上開全部 `forced` 格）")
    say("=" * W)
    n = len(allrows)
    say("   | 造 | 判準 | 實測 | 判 |")
    say("   |---|---|---|---|")
    say("   | （母體） | `forced` 格數 `≥ 1` | **%d** | %s |" % (n, "✅" if n >= 1 else "🔴"))

    # [必為零]：同一 `buf` 餵二次須得同值（**先自證可滿足**）
    twice = []
    for r in allrows:
        a = J._w0(r["ns_"], r["fp"], r["buf1"], r["dh"], r["sm"], r["ad1"])
        b = J._w0(r["ns_"], r["fp"], r["buf1"], r["dh"], r["sm"], r["ad1"])
        twice.append(a - b)
    ok0 = (n >= 1) and all(x == 0.0 for x in twice)
    say("   | **[必為零]·自證可滿足** | 同一 `buf` 餵二次之差 ＝ `0.0` | %s | %s |"
        % ("／".join(repr(x) for x in twice), "✅" if ok0 else "🔴"))
    k3s = [r["k3"] for r in allrows]
    got = [x for x in k3s if x is not None]
    # 🩸 **自捕**：`all(...)` 於**空集**恆真 ⇒ 三格皆「不可得」時會靜默判綠
    #    （`W-G.9-226` 通則 `二`：受詞缺漏須 **loud 拒測**、⛔ 靜默綠）。
    if not got:
        verdict = "🟡 **不可判（loud）**——判定組為空（三格皆不可得）·⛔ 以「全數成立」充綠"
    elif all(x == 0.0 for x in got):
        verdict = "✅（判定組 **%d**／%d 格）" % (len(got), len(k3s))
    else:
        verdict = "🛑 **相異**（判定組 **%d**／%d 格）" % (len(got), len(k3s))
    say("   | **[必為零]·受詞** | 款 `3` ＝ `0.0`（`None` ＝ 不可得·**⛔ 計入判定組**） | %s | %s |"
        % ("／".join("不可得" if x is None else repr(x) for x in k3s), verdict))
    # [必相異]：以 buf′ 餵之所得須異於款 2
    ok1 = (n >= 1) and all(r["w0_new"] != r["w0_rec"] for r in allrows)
    say("   | **[必相異]** | 以 `buf′` 餵之所得 **異於**款 `2`（證重建式非恆值） | %s | %s |"
        % ("／".join("%r vs %r" % (r["w0_new"], r["w0_rec"]) for r in allrows), "✅" if ok1 else "🔴"))
    ok2 = (n >= 1) and all(abs(r["buf2"] - r["buf1"]) > 0 for r in allrows)
    # 🔒 帶號與絕對值**並列**（`CLAUDE.md`：二者所偵之錯不相交）
    say("   | **[必非零]** | `\\|buf′ − buf\\|` `> 0`（帶號／絕對值**並列**） | %s ／ %s | %s |"
        % ("／".join(repr(r["buf2"] - r["buf1"]) for r in allrows),
           "／".join(repr(abs(r["buf2"] - r["buf1"])) for r in allrows), "✅" if ok2 else "🔴"))
    if not (n >= 1 and ok0 and ok1 and ok2):
        red("判別力三造未全數成立 ⇒ **判器紅、停、上呈**")

    say("")
    say("=" * W)
    say("## 總表")
    say("=" * W)
    say("   | `SB` | 格 | 通道② 生產呼叫 | 款 `1` `W_0^prod` | 款 `2` `W_0^rec` | **款 `3` 逐位差** | "
        "%s `W_0′` | `\\|W_0′−S1_perp\\|` | `A′` 界 | `A′` |" % TAG)
    say("   |---|---|---|---|---|---|---|---|---|---|")
    for r in allrows:
        say("   | `%s` | `%s/%s` | `%d` | %s | `%r` | %s | `%r` | `%r` | `%r` | %s |"
            % (repr(r["sb"]), r["blk"], r["side"], r["n2"],
               "🟡 不可得" if r["w0_prod"] is None else "`%r`" % r["w0_prod"],
               r["w0_rec"],
               "🟡 不可得" if r["k3"] is None else ("**`%r`**" % r["k3"]),
               r["w0_new"], r["dW"], r["A_lim"], "✅" if r["okA"] else "🛑"))
    say("")
    say("🛑 **出艙即止**：本器⛔ 判路丙成立與否、⛔ 判餘量之成因、⛔ 擬實作、⛔ 改碼一字、")
    say("   ⛔ 開分支、⛔ 動用 KL 之放行、⛔ 鑄任何號、⛔ 解除或收窄 `GB-170`、⛔ 調任何界、⛔ 呈 KL。")
    rc = RED[0] or BAD[0]
    say("🔒 `rc` ＝ `%d`（`5` ＝ **量測器紅**／`6` ＝ **受詞紅**·二者⛔ 同義）" % rc)
    say("=" * W)

    out = os.path.join(REPO, "verify", "out", "WG9296R_w0rec.log")
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(_LOG) + "\n")
    print("\n落檔 ⇒ %s" % out)
    return rc


if __name__ == "__main__":
    sys.exit(main())
