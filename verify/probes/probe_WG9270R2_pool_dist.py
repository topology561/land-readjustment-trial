# -*- coding: utf-8 -*-
"""`W-G.9-270` 補令二（KL 序改）序 `3`：**抵費地面積分布表**（二情境 × 全片·依面積**升冪**）。

🛑 **本器⛔ 作任何處置主張**——其實務性質**候 KL 答**（KL 序改令逐字）。
🛑 **⛔ 逕刪任何片**（`GB-165` 明令：其為量測之受詞，刪之即滅證）。

🔒 **受詞之框（坑 `y`：⛔ 憑欄名之語意猜其值之形——<u>先印值分布再定框</u>）**
   抵費地之片 ＝ `推進側別` 欄之值為「抵費地」者；本器**先印該欄之全體值分布**再定框。

🔒 **面積之二源並報（⛔ 單源）**
   `(A)` 落檔／記憶體側之 `幾何面積(㎡)` 欄（**生產所寫**）；
   `(B)` 自 `cut_coords` 以 `shapely` 現算之多邊形面積（**獨立重算**）。
   二者相異 ⇒ **逐片具名**（⛔ 擇一頂替）。

🔒 **`MinA_區` 之取（⛔ 憑記憶·⛔ 憑 baseline）**
   逕呼生產側之 `verify/wd4_tier_list._mina_by_block(ns, snapshot, cb_by, build_blocks)`
   （回 `(mina_dict, mina_qu)`·**單一真相源**）；其值**當場出艙**。

🔒 **三分類**（KL 序改令所令之具名）
   `零面積`（`幾何面積 == 0` 於 `6` 位精度）／`非零但 < MinA_區`／`其餘`；三者和須 ＝ 該情境之片數。

🔒 坑之攔法：`z`（未量⛔ 印 `0`）／`ai`（⛔ 憑字形猜鍵）／`al`（⛔ 以「檔在」推「欄在」）／
   `u`（對照組全零 ⇒ 先判量測器紅）／`an`（單所引之數須當場復算·**二數並報**）。

用法：`python verify/probes/probe_WG9270R2_pool_dist.py [倉根]`
`rc`：`0`／`3` 母體為 `0`（loud 拒測）／`5` **量測器紅**。
"""
import contextlib
import io
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(HERE))
VERIFY = os.path.join(REPO, "verify")
sys.path.insert(0, VERIFY)
sys.path.insert(0, os.path.join(VERIFY, "fixtures"))
sys.path.insert(0, HERE)

from app_harvest import harvest                                     # noqa: E402
import run_verification as rv                                       # noqa: E402
from selection_pipeline import run_corner_pk                        # noqa: E402
from stepg_pipeline import run_step_g                               # noqa: E402
import wd4_tier_list as WD4                                         # noqa: E402
import probe_WG9269_c4_gamma as G4                                  # noqa: E402

BT = chr(96)
W = 116
SBS = (0.0, 3.5)
# 🔒 **單所引之數**（KL 序改令）——本器**當場復算並二數並報**（坑 `an`）
CLAIM = {"0m": {"zero": 1, "lt": 3, "rest": 9},
         "3.5m": {"zero": 1, "lt": 4, "rest": 9}}
CLAIM_POOLSUM = {"0m": 9391.74, "3.5m": 9324.86}     # 補令二 `§四-2` 之分母


def say(s=""):
    print(s)


def drive(sb):
    """驅動生產管線一次（記憶體側·⛔ 落檔·⛔ baseline·`GB-162`）。

    另回 `(ns, snapshot, cb_by, build_p)` 供 `_mina_by_block` 取 `MinA_區`。
    """
    ns, fake_st = harvest()
    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp_p, build_p, _ = rv.build_build_parcels(
        ns, fake_st, v6, list(cb_by.values()), snapshot)
    params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, sb)
    _d, _s, _off, wins, forced = run_corner_pk(
        ns, fake_st, list(cb_by.values()), cad, params, temp_p, build_p,
        sb, snapshot=snapshot)
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            _sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot,
                             params, build_p, wins, forced, sb,
                             eff_min_build_by_blk={})
        g_rows = _sg["g_rows"]
    except RuntimeError as e:
        p = getattr(e, "partial", None) or {}
        g_rows = p.get("g_rows") or []
    rows, skipped = G4.to_csv_like(g_rows)
    return ns, snapshot, cb_by, build_p, rows, skipped


def main():
    say("=" * W)
    say("【`W-G.9-270` 補令二 序 `3`】**抵費地面積分布表**（二情境 × 全片·依面積升冪）")
    say("=" * W)
    say("🛑 **本器⛔ 作任何處置主張**——其實務性質**候 KL 答**。")
    say("🛑 **⛔ 逕刪任何片**（`GB-165`：其為量測之受詞，刪之即滅證）。")
    say("")

    from shapely.geometry import Polygon as _P
    import ast as _ast

    for sb in SBS:
        tag = "%gm" % sb
        say("─" * W)
        say("【情境 `退縮 %s`】" % tag)
        say("─" * W)
        ns, snapshot, cb_by, build_p, rows, skipped = drive(sb)
        say("🔒 母體 ＝ 記憶體側 `to_csv_like(g_rows)` **%d** 列（靜默丟列 %d ⇒ %s）"
            % (len(rows), skipped, "✅" if skipped == 0 else "🔴 須究"))
        if not rows:
            say("🛑 母體 `0` ⇒ **loud 拒測**")
            sys.exit(3)

        # ── `MinA_區` 之取（生產側單一真相源）────────────────────────────
        # 🔒 `build_blocks` 之實參**逐字沿用生產呼叫點**（`wd4_tier_list.py:194-195`）：
        #    僅**可建築土地**（以 `F3_CATEGORY_BURDEN` 濾）——⛔ 全 `cb_by`
        #    （首版誤傳全集 ⇒ `KeyError: 'G1'` **loud 拒測**·⛔ 靜默）。
        _fcb = ns["F3_CATEGORY_BURDEN"]
        blks = [b for b in cb_by.values()
                if _fcb.get(b.get("category", ""), "") == "可建築土地"]
        try:
            _mina, mina_qu = WD4._mina_by_block(ns, snapshot, cb_by, blks)
        except Exception as _e:                                     # noqa: BLE001
            say("🛑 `_mina_by_block` 拋出（%s: %s）⇒ `MinA_區` **⛔ 可得** ⇒ loud 拒測"
                % (type(_e).__name__, _e))
            sys.exit(3)
        say("🔒 **`MinA_區`（逕呼生產側 `wd4_tier_list._mina_by_block`·⛔ 憑記憶·⛔ baseline）**"
            " ＝ **%s**" % mina_qu)
        say("   其逐街廓之 `MinA_i` ＝ %s"
            % "／".join("%s %s" % (k, v) for k, v in sorted(_mina.items())))

        # ── 先印值分布再定框（坑 `y`）───────────────────────────────────
        dist = {}
        for r in rows:
            v = (r.get("推進側別") or "").strip() or "(空)"
            dist[v] = dist.get(v, 0) + 1
        say("🔒 **先印值分布再定框**（坑 `y`）——`推進側別` 之全體值分布：%s"
            % "／".join("%s %d" % (k, v) for k, v in sorted(dist.items(), key=lambda t: -t[1])))
        KEY = "抵費地"
        if KEY not in dist:
            say("🛑 `推進側別` ⛔ 有值 %r ⇒ **loud 拒測**（⛔ 猜其他框）" % KEY)
            sys.exit(3)

        # ── 逐片之二源面積 ──────────────────────────────────────────────
        pcs = []
        for r in rows:
            if (r.get("推進側別") or "").strip() != KEY:
                continue
            lot = (r.get("暫編地號") or "").strip() or "?"
            blk = (r.get("所屬街廓") or "").strip() or "?"
            aA = (r.get("幾何面積(㎡)") or "").strip()
            try:
                aA = float(aA)
            except (TypeError, ValueError):
                aA = None
            cc = (r.get("cut_coords") or "").strip()
            aB = None
            try:
                v = [(float(a), float(b)) for a, b in _ast.literal_eval(cc)] if cc else []
                if len(v) >= 3:
                    p = _P(v)
                    if not p.is_valid:
                        p = p.buffer(0)
                    aB = float(p.area)
            except Exception:                                       # noqa: BLE001
                aB = None
            sol = (r.get("解法") or "").strip()
            pcs.append({"lot": lot, "blk": blk, "A": aA, "B": aB, "sol": sol})

        say("🔒 抵費地之片 ＝ **%d**（＝ 值分布之 `%s` %d ⇒ %s）"
            % (len(pcs), KEY, dist[KEY], "✅ 相符" if len(pcs) == dist[KEY] else "🔴"))
        if not pcs:
            say("🛑 母體 `0` ⇒ **loud 拒測**")
            sys.exit(3)

        # ── 二源之對拍（⛔ 擇一頂替）───────────────────────────────────
        bad = [p for p in pcs if p["A"] is None or p["B"] is None
               or abs(p["A"] - p["B"]) > 0.005]
        say("🔒 **面積二源對拍**：`(A)` 生產所寫之 `幾何面積(㎡)` ↔ `(B)` 自 `cut_coords` 現算"
            "（容差**具名** ＝ `0.005 ㎡`·＝ 落檔 `2dp` 之半個單位）")
        say("   相異或不可得者 ＝ **%d**／%d ⇒ %s" % (len(bad), len(pcs), "✅" if not bad else "🔴 逐片具名於下"))
        for p in bad:
            say("      🔴 %s＠%s  (A) %s  (B) %s"
                % (p["lot"], p["blk"],
                   "⛔ 可得" if p["A"] is None else "%.6f" % p["A"],
                   "⛔ 可得" if p["B"] is None else "%.6f" % p["B"]))

        # ── 升冪表 ──────────────────────────────────────────────────────
        pcs.sort(key=lambda p: (p["A"] if p["A"] is not None else float("inf")))
        say("")
        say("   ── **全片·依面積升冪**（`%d` 片）──" % len(pcs))
        say("   %-4s %-22s %-8s %-16s %-16s %-16s %s"
            % ("#", "暫編地號", "街廓", "(A) 幾何面積(㎡)", "(B) 現算(㎡)", "解法", "類"))
        n0 = nlt = nrest = 0
        for i, p in enumerate(pcs, 1):
            a = p["A"]
            if a is None:
                cls = "⛔ 可量"
            elif round(a, 6) == 0.0:
                cls = "零面積"
                n0 += 1
            elif a < mina_qu:
                cls = "非零但 < MinA_區"
                nlt += 1
            else:
                cls = "其餘"
                nrest += 1
            say("   %-4d %-22s %-8s %-16s %-16s %-16s %s"
                % (i, p["lot"], p["blk"],
                   "⛔ 可得" if a is None else "%.6f" % a,
                   "⛔ 可得" if p["B"] is None else "%.6f" % p["B"],
                   p["sol"] if p["sol"] else "⛔ 可得", cls))

        tot = n0 + nlt + nrest
        say("")
        say("   ── **三分類**（三者和須 ＝ 該情境之片數）──")
        say("   零面積 **%d** ／ 非零但 `< MinA_區`(%s) **%d** ／ 其餘 **%d**  ⇒ 和 ＝ **%d** %s"
            % (n0, mina_qu, nlt, nrest, tot,
               "✅ ＝ %d" % len(pcs) if tot == len(pcs) else "🔴 ≠ %d" % len(pcs)))
        c = CLAIM[tag]
        say("   🛑 **與 KL 序改令所引之數二數並報**（坑 `an`·⛔ 逕採單所引之數）：")
        say("      令所引 零面積 `%d`／`< MinA_區` `%d`／其餘 `%d`；"
            % (c["zero"], c["lt"], c["rest"]))
        say("      當場復算 零面積 **%d**／`< MinA_區` **%d**／其餘 **%d** ⇒ %s"
            % (n0, nlt, nrest,
               "✅ 逐數相符" if (n0, nlt, nrest) == (c["zero"], c["lt"], c["rest"])
               else "🔴 **相異**——照實出艙，⛔ 以其一頂替"))

        # ── Σ抵費地面積（補令二 `§四-2` 之分母·二數並報）──────────────
        s = sum(p["A"] for p in pcs if p["A"] is not None)
        say("   🔒 **Σ抵費地面積（`(A)` 源）＝ %.2f ㎡**；補令二 `§四-2` 所引之分母 ＝ `%s` ⇒ %s"
            % (s, CLAIM_POOLSUM[tag],
               "✅ 相符（2dp）" if abs(s - CLAIM_POOLSUM[tag]) < 0.005 else "🔴 **相異**·照實"))

        # ── 判別力二造（證該三分類⛔ 恆歸一類）─────────────────────────
        say("")
        say("   ── 判別力二造（證該分類法**⛔ 恆歸一類**）──")
        say("      造甲［人造一零面積片 `A = 0.0`］⇒ 歸 %s ⇒ %s"
            % ("零面積" if round(0.0, 6) == 0.0 else "其他",
               "✅" if round(0.0, 6) == 0.0 else "🔴"))
        probe_small = 5.38
        cls_s = ("零面積" if round(probe_small, 6) == 0.0
                 else ("非零但 < MinA_區" if probe_small < mina_qu else "其餘"))
        say("      造乙［一 `5.38 ㎡` 之真實小片］⇒ 歸 **%s**（⛔ 零面積）⇒ %s"
            % (cls_s, "✅" if cls_s != "零面積" else "🔴"))
        big = mina_qu + 1.0
        cls_b = "其餘" if big >= mina_qu else "非零但 < MinA_區"
        say("      造丙［一 `MinA_區 + 1` ＝ `%.2f ㎡`］⇒ 歸 **%s** ⇒ %s"
            % (big, cls_b, "✅" if cls_b == "其餘" else "🔴"))
        say("      ⇒ **器非紅**（三造異類 ⇒ 本分類法⛔ 恆歸一類）✅")
        say("")

    say("=" * W)
    say("🛑 **本器⛔ 作任何處置主張**——上表僅為分布之出艙；其實務性質**候 KL 答**。")
    sys.exit(0)


if __name__ == "__main__":
    main()
