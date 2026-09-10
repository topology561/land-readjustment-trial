# -*- coding: utf-8 -*-
"""`W-G.9-268′` `c2`：`V-1′` 之**記憶體側**新器（補令八 `§二` 序 `1`）。

🩸 **本器之存在理由（自毀式之第二例·補令七 `§四` 所診）**
   `verify/probes/probe_WG9266_V1prime_3groups.py` 之母體 ＝ 二態之落檔
   `verify/out/got_G值_退縮3.5m_partial.csv`；而 `_partial` **只在管線<u>中止</u>時產生**。
   `c2` 之受詞正是「**使管線⛔ 再中止**」⇒ 該檔於 `c2` 態⛔ 存在 ⇒ 舊器**結構上量不到 `c2` 態**。
   🔒 **通則（補令五 `§三-1` 逐字）**：**凡驗收條件所繫之量測管道，其存在本身若取決於
   「缺陷仍在」，該條件即為自毀式，⛔ 立。**

🔑 **本器之作法 ＝ <u>只換資料源</u>，⛔ 另寫第二份定義**（`GB-48` 族）
   對倉內既有器 `probe_WG9266_V1prime_3groups`（下稱 `V1`）**只 monkeypatch 其 `load()`**
   （＝ 讀 CSV 之那一支），其餘 `shared_edge`／`s_of_line`／`measure`／`gates`／`run`
   ——**含 `V-1′` 五款之全部判準與 `1e-6`**——**逐字沿用、一字不動**。
   🔒 ⇒ 本器**⛔ 改 `V-1′` 五款之判準一字**（`VR-094` 末端追加 明令）。

🔒 **二態之取得**：於**同一 process** 內以**顯式旗標值**各驅動一次
   （`off` ＝ `WG9268P_ANCHOR_GEOM='0'`／`on` ＝ `'1'`）
   ——🩸 **⛔ 以 `os.environ.pop` 取 `off`**：`c2` 後預設為 `'1'`，`pop` 所得者為 `on`（自毀式）。

🩸 **`cut_coords` 之二形（坑 `1`）**：記憶體側為 `list`、落檔側為**字串**；
   `V1.measure()` 走 `ast.literal_eval` ⇒ 本器於轉檔時將其**還原為字串形**，
   使 `V1` 之下游一字不動；並**同格印母體基數**（母體為 `0` ⇒ ⛔ 靜默綠）。

🔒 **`FRONT_LINE` 之來源** ＝ 生產解析器之 `cad['front_lines']`（⛔ 質心導出·⛔ 自寫第二份解析）。

用法：`python verify/probes/probe_WG9268p_c2_v1prime_mem.py [倉根]`
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

import probe_WG9266_V1prime_3groups as V1                           # noqa: E402

FLAG = "WG9268P_ANCHOR_GEOM"
SB = 3.5                     # 🔒 三組之受詞逐字皆為 `3.5m`（`VR-094` 末端追加 二）
TAG = "3.5m"
GROUPS = [("陽性", "R2", "left"),
          ("真陰性", "R1", "right"),
          ("第三類（`G` 於 2dp 不變而 `cut_coords` 逐位相異之組）", "R2", "right")]

ROWS = {}


def _load(root):
    """monkeypatch `V1.load`：回本器所備之記憶體側列（形同 CSV 之 `DictReader` 輸出）。"""
    return ROWS[root]


def to_csv_like(g_rows):
    """記憶體側 → CSV 形（`cut_coords` 還原為**字串**·其餘轉 `str`）。⛔ 靜默丟列。"""
    out, skipped = [], 0
    for r in g_rows:
        cc = r.get("cut_coords")
        if isinstance(cc, str):
            s = cc
        elif cc:
            s = repr([[float(a), float(b)] for a, b in cc])
        else:
            s = ""
            skipped += 1
        d = {}
        for k, v in r.items():
            d[k] = s if k == "cut_coords" else ("" if v is None else str(v))
        out.append(d)
    return out, skipped


def drive(setback, mode, ns, fake_st, snapshot, cb_by, cad, build_p, temp_p):
    if mode == "on":
        os.environ[FLAG] = "1"
    else:
        os.environ[FLAG] = "0"      # 🔒 顯式 off（⛔ pop ＝ 取預設）
    try:
        params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
        _d, _s, _off, wins, forced = run_corner_pk(
            ns, fake_st, list(cb_by.values()), cad, params, temp_p, build_p,
            setback, snapshot=snapshot)
        g_rows, aborted = [], None
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                _sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot,
                                 params, build_p, wins, forced, setback,
                                 eff_min_build_by_blk={})
            g_rows = _sg["g_rows"]
        except RuntimeError as e:
            p = getattr(e, "partial", None) or {}
            g_rows = p.get("g_rows") or []
            aborted = p.get("aborted_blk")
    finally:
        os.environ.pop(FLAG, None)
    return g_rows, aborted


def main():                                                         # noqa: C901
    print("=" * 116)
    print("【`W-G.9-268′` `c2`】`V-1′` 三組對照（**記憶體側**·補令八 `§二` 序 `1`）")
    print("=" * 116)
    print("🔒 判準之來源 ＝ 倉內既有 `probe_WG9266_V1prime_3groups`（**只換資料源**·五款一字不動）")
    print("🔒 `1e-6` ⛔ 放寬：`V1.TOL_K1` ＝ %g／`V1.TOL_K3` ＝ %g（自該模組現讀）"
          % (V1.TOL_K1, V1.TOL_K3))
    print()

    ns, fake_st = harvest()
    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp_p, build_p, _ = rv.build_build_parcels(
        ns, fake_st, v6, list(cb_by.values()), snapshot)
    fl = cad["front_lines"]
    print("🔒 管線已建：街廓 `%d`／宗 `%d`；`FRONT_LINE` ＝ 生產解析器 `cad['front_lines']`（`%d` 街廓）"
          % (len(cb_by), len(build_p), len(fl)))
    print()

    for mode in ("off", "on"):
        g, ab = drive(SB, mode, ns, fake_st, snapshot, cb_by, cad, build_p, temp_p)
        rows, skipped = to_csv_like(g)
        ROWS[mode.upper()] = rows
        print("🔒 [%-4s／%-3s] `g_rows` **%d** 列（母體基數）／中止 %s／⛔ `cut_coords` 之列 %d"
              % (TAG, mode, len(rows), ab or "無", skipped))
    print()
    if not ROWS["OFF"] or not ROWS["ON"]:
        print("🛑 一態之母體為 **0** 列 ⇒ **loud 拒測**（⛔ 靜默綠）")
        return 3

    V1.load = _load                     # 🔑 只換資料源

    # ── 診斷：本批實際動到哪些側（供「三組同色」時之歸因·⛔ 判準）──
    print("=" * 116)
    print("〔診斷·⛔ 判準〕`off → on` 逐側之 `cut_coords` 逐位相異宗數（`%s`）" % TAG)
    print("=" * 116)
    A = {}
    B = {}
    for tag, src in (("OFF", A), ("ON", B)):
        for r in ROWS[tag]:
            k = ((r.get("所屬街廓") or "").strip(), (r.get("推進側別") or "").strip())
            src.setdefault(k, {})[(r.get("暫編地號") or "").strip()] = r.get("cut_coords")
    for k in sorted(set(A) | set(B)):
        if k[1] == "抵費地":
            continue
        a, b = A.get(k, {}), B.get(k, {})
        both = sorted(set(a) & set(b))
        diff = [i for i in both if a[i] != b[i]]
        print("   %-14s 共同宗 %2d｜`cut_coords` 相異 **%2d** 宗 %s"
              % ("%s·%s" % k, len(both), len(diff), "🔴 已動" if diff else "✅ 未動"))
    print()

    res = {}
    for role, blk, side in GROUPS:
        res[role] = V1.run("OFF", "ON", blk, side, fl, role)
        print()

    print("=" * 116)
    print("【三組並列之判】")
    print("=" * 116)
    print("  %-46s %-4s %-5s %-5s %-4s %-5s %-4s %-6s"
          % ("組（受詞逐字）", "n", "(1a)", "(1b)", "(2)", "(3)", "(4)", "(5)"))
    for role, blk, side in GROUPS:
        r = res[role]
        if r.get("refuse"):
            print("  %-46s %-4d 🛑 loud 拒測" % ("%s·%s·%s〔%s〕" % (TAG, blk, side, role), r["n"]))
            continue
        print("  %-46s %-4d %-5s %-5s %-4s %-5s %-4s %d 宗"
              % ("%s·%s·%s〔%s〕" % (TAG, blk, side, role[:3]), r["n"],
                 "✅" if r["k1a"] else "🔴", "✅" if r["k1b"] else "🔴",
                 "✅" if r["k2"] else "🔴", "✅" if r["k3"] else "🔴",
                 "✅" if r["k4"] else "🔴", r["n5"]))
    pos, neg, thr = res[GROUPS[0][0]], res[GROUPS[1][0]], res[GROUPS[2][0]]
    if any(x.get("refuse") for x in (pos, neg, thr)):
        print("🛑 有組 loud 拒測 ⇒ **停機**（補令八 `§二`：任一組 `n = 0` ⇒ 停機上呈）")
        return 8
    ok_pos = (pos["n5"] > 0) and (not pos["k1b"]) and (not pos["k3"])
    ok_neg = (neg["n5"] == 0) and neg["k1b"] and neg["k3"]
    ok_thr = (thr["n5"] == 0) and (not thr["k1b"]) and (not thr["k3"])
    print()
    print("  判別力（`VR-094` 末端追加 三·逐字）：")
    print("    陽性　　須 `(5) > 0` 且 `(1b)`／`(3)` 紅 ⇒ %s" % ("✅" if ok_pos else "🔴"))
    print("    真陰性　須 `(5) = 0` 且 `(1b)`／`(3)` **綠** ⇒ %s" % ("✅" if ok_neg else "🔴"))
    print("    第三類　須 `(5) = 0` 而 `(1b)`／`(3)` 紅 ⇒ %s" % ("✅" if ok_thr else "🔴"))
    same_color = ((pos["k1b"] == neg["k1b"] == thr["k1b"])
                  and (pos["k3"] == neg["k3"] == thr["k3"]))
    print("    三者同色？ %s ⇒ %s"
          % (same_color, "🔴 **閘失能·停機**" if same_color else "✅ **閘⛔ 失能**"))
    # ── 診斷（⛔ 判準·⛔ 改任何判準·⛔ 取代三組）─────────────────
    #   三組同色時，其歸因須可查：本節以**同一支 `V1.run`** 量本批**實際動到**之側，
    #   使「三組是否選錯」成為**已量**而非斷言。🛑 其結果**⛔ 進入判別力之判**。
    if same_color and len(sys.argv) > 2:
        print()
        print("=" * 116)
        print("〔診斷·🛑 ⛔ 判準·⛔ 取代三組〕本批**實際動到**之側之逐款")
        print("=" * 116)
        for spec in sys.argv[2:]:
            b, _, s = spec.partition(":")
            print()
            V1.run("OFF", "ON", b, s, fl, "診斷·⛔ 判準")

    print()
    print("=" * 116)
    if same_color:
        print("🛑 **停機上呈**（補令八 `§二`：三組同色 ⇒ 停機）")
        return 9
    if not (ok_pos and ok_neg and ok_thr):
        print("🛑 **停機上呈**（補令八 `§二`：`V-1′` 任一款轉紅 ⇒ 停機）")
        return 9
    print("✅ `V-1′` 三組於 `c2` 態**逐款如期**、三者⛔ 同色 ⇒ 閘⛔ 失能")
    print("=" * 116)
    return 0


if __name__ == "__main__":
    sys.exit(main())
