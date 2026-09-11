#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""`W-G.9-269` 本體階　`c2` 前置 `2`：**`628-27(1)` 之歸戶**（於<u>管線跑畢之態</u>取之）。

🩸 **本器之存在理由**（補令七 `§四-2` 款 `2`·逐字）
   「**`628-27(1)` 之歸戶須具名**（發單側查其歸戶對映於 `harvest()` 時為空
     ⇒ 須於**管線跑畢之態**取之）。」
   ⇒ 本器於 `rv.build_ownership` **已跑畢**之態取 `t8_ownership_map`，**⛔ 於 `harvest()` 時取**。

🔒 **⛔ 另寫第二份定義**（`GB-48` 族）
   歸戶查找一律用生產碼之 `_resolve_ownership`（`app.py` 之四層查找·自 `ns` 取）；
   正規化用生產碼之 `_normalize_landno_module`。本器**⛔ 自寫任何查找邏輯**。

🔒 **三造對照**（`坑 13`：只備「必不命中」與「必非零」者⛔ 足以證框撈得到本類）
   `(甲)` **必非零** ＝ `628-42(1)`（其歸戶為**已知**：`G011`·出處 `W-G.9-269R_前置階.md §戊` 項 `5`）
   `(乙)` **人造哨兵** ＝ 一必不存在之暫編地號（**執行期組出**·其字面⛔ 落入 log·`GB-147`）⇒ 須得空
   `(丙)` **必命中之本類已知成員** ＝ `628-53(2)`（已知 `G025`·同上出處）
   🛑 `(甲)`／`(丙)` 係**已知答案**之造 ⇒ 其相符方證本器之查找確實有鑑別力；
   三造任一不成立 ⇒ **loud 拒測**（`rc = 2`·**量測器紅**·⛔ 受詞紅）。

🔒 **外部錨**（`常規八 二` ①：原始量須另備外部錨·⛔ 以 `N/N` 自證）
   受詞三宗之 `a 面積(㎡)`／`G(㎡)`／`宗地寬度(m)` 須與 `docs/orders/W-G.9-269_補令七_…md` `§四-1`
   之表**逐值相符**（`628-42(1)` `8.34`／`0.23`／`0.18`；`628-53(2)` `2.78`／`0.00`／`0.02`；
   `628-27(1)` `51.32`／`29.26`／`0.65`）。不符即 `rc = 5`（**受詞紅**）。

🔒 **態宣告二值並報**（`坑 r`·單之硬準則）
   `git rev-parse HEAD:app.py`（committed）⋀ `git hash-object app.py`（工作區·**以後者為實**）。

🛑 **本器⛔ 觸 `os.environ`、⛔ 翻旗標**——其於旗標**預設 `off`** 之態量測
   （`628-27(1)` 於 `on` 態已被級聯剔除 ⇒ 其歸戶只能於 `off` 態之配地母體內取得）。

用法：`python verify/probes/probe_WG9269_c2_owner.py`
`rc`：`0` 全綠／`2` **量測器紅**（三造不成立 ⇒ loud 拒測）／`5` 受詞紅（外部錨不符）／
      `3` **判定集為空**（loud 拒測·⛔ 與「量得為零」共用出艙碼）。
🛑 `rc ≠ 0` ⛔ 等同「受詞紅」——須讀其逐項（`坑 9`）。
"""
import contextlib
import io
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)          # 🔒 自 `__file__` 上溯·⛔ 硬編他樹（`GB-161`）
sys.path.insert(0, VERIFY)
sys.path.insert(0, os.path.join(VERIFY, "fixtures"))
sys.path.insert(0, HERE)

from app_harvest import harvest                                     # noqa: E402
import run_verification as rv                                       # noqa: E402
from selection_pipeline import run_corner_pk                        # noqa: E402
from stepg_pipeline import run_step_g                               # noqa: E402

W = 118
SCEN = (("0m", 0.0), ("3.5m", 3.5))

# 受詞（**逐情境分列**·`坑 e`：本案之一切量皆情境相依·⛔ 以一情境之處置冠於另一情境）
#   已知歸戶（`W-G.9-269R_前置階.md §戊` 項 `5`）
KNOWN_GID = {"628-42(1)": "G011", "628-53(2)": "G025", "628-27(1)": None}
#   `0m` 之外部錨（`docs/orders/W-G.9-269_補令七_…md` `§四-1` 之表·⛔ 摘要）
ANCHOR_0M = {
    "628-42(1)": (8.34, 0.23, 0.18),
    "628-53(2)": (2.78, 0.00, 0.02),
    "628-27(1)": (51.32, 29.26, 0.65),
}
#   處置（**逐 (宗, 情境)**·出處 ＝ `c1` 側支之實跑落檔 `verify/out/WG9269R_c1_on_drop.log`
#   〔`0m` 消失 `3` 宗／`3.5m` 消失 `1` 宗〕＋ 補令七 `§四-1` 之二分類·⛔ 本器所量）
DISPOSAL = {
    ("628-42(1)", "0m"): "閘一直接剔除",
    ("628-42(1)", "3.5m"): "⛔ 剔除（留於配地）",
    ("628-53(2)", "0m"): "閘一直接剔除",
    ("628-53(2)", "3.5m"): "閘一直接剔除",
    ("628-27(1)", "0m"): "🔴 級聯剔除",
    ("628-27(1)", "3.5m"): "⛔ 剔除（留於配地）",
}
SUBJ = ("628-42(1)", "628-53(2)", "628-27(1)")


def _state():
    """態宣告**二值並報**（`坑 r`）。"""
    def g(*a):
        r = subprocess.run(["git", "-C", REPO] + list(a),
                           capture_output=True, text=True)
        return r.stdout.strip() if r.returncode == 0 else "⛔ 可得"
    return (g("rev-parse", "HEAD"),
            g("rev-parse", "HEAD:app.py"),
            g("hash-object", os.path.join(REPO, "app.py")),
            g("status", "--porcelain"))


def _sentinel(own_map):
    """人造哨兵：**執行期組出**一必不存在之暫編地號（其字面⛔ 出艙·`GB-147`）。"""
    base = "".join(chr(c) for c in (57, 57, 57, 57, 57, 57))      # 六個 '9'
    for k in range(100):
        cand = "%s-%d(%d)" % (base, k, k)
        if cand not in own_map:
            return cand
    raise RuntimeError("哨兵組出失敗（母體異常）")


def measure():
    """跑畢管線（`off` 態）。回 (own_map, rows_by_tag, ns)。"""
    ns, fake_st = harvest()
    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    own = rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    own_map = dict(fake_st.session_state["t8_ownership_map"])
    print("🔒 `rv.build_ownership` **已跑畢**："
          "歸戶群組 **%d** 組／`t8_ownership_map` 鍵 **%d**／對應失敗 **%d**"
          % (own["n_groups"], len(own_map), own["n_fail"]))
    print("   靶組核對（`OWNERSHIP_TARGETS` 三環定理鏈 tripwire）＝ %s"
          % ("✅ 全符" if own["targets_ok"] else "🔴 不符"))

    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp_p, build_p, _ = rv.build_build_parcels(
        ns, fake_st, v6, list(cb_by.values()), snapshot)
    print("🔒 記憶體側管線已建：街廓 **%d**／`temp_parcels` **%d**／`build_parcels` **%d**"
          % (len(cb_by), len(temp_p), len(build_p)))

    rows = {}
    for tag, sb in SCEN:
        params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, sb)
        _d0, _s2, _o2, wins, forced = run_corner_pk(
            ns, fake_st, list(cb_by.values()), cad, params, temp_p, build_p,
            sb, snapshot=snapshot)
        g_rows, ab = [], None
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                _sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot,
                                 params, build_p, wins, forced, sb,
                                 eff_min_build_by_blk={})
            g_rows = _sg["g_rows"]
        except RuntimeError as e:
            p = getattr(e, "partial", None) or {}
            g_rows = p.get("g_rows") or []
            ab = p.get("aborted_blk")
        rows[tag] = g_rows
        print("   情境 %-5s ⇒ `g_rows` **%3d** 列／中止街廓 %s"
              % (tag, len(g_rows), ab or "（無·跑完）"))
    return own_map, rows, ns, temp_p


def main():                                                         # noqa: C901
    head, appblob, appwork, porcelain = _state()
    print("=" * W)
    print("【`W-G.9-269` `c2` 前置 `2`】`628-27(1)` 之歸戶（管線跑畢之態）")
    print("=" * W)
    print("🔒 **態宣告二值並報**（`坑 r`·**以工作區之值為實**）")
    print("   `commit`                        ＝ %s" % head)
    print("   `app.py` `rev-parse HEAD:app.py`（committed）＝ %s" % appblob)
    print("   `app.py` `hash-object`（**工作區·實**）      ＝ %s" % appwork)
    print("   二值 %s" % ("**相同** ✅（工作區與 `HEAD` 同步）" if appblob == appwork
                          else "🔴 **相異** ⇒ 工作區與 `HEAD` 不同步（須具名）"))
    print("   `git status --porcelain` ＝ %s"
          % ("（空·乾淨）" if not porcelain else "🟡 非空（%d 列）" % len(porcelain.splitlines())))
    print()

    own_map, rows, ns, temp_p = measure()
    resolve = ns["_resolve_ownership"]
    print()

    # ── 三造對照（`坑 13`·`坑 u`：對照組全零 ⇒ 先判量測器紅）────────────────
    print("── 三造對照（**先跑**·未全成立則 loud 拒測·⛔ 出艙受詞之值）" + "─" * 40)
    ctl = []
    # 由 g_rows（`0m`）取各宗之原地號——⛔ 自寫對映
    by_pid = {}
    for tag in rows:
        for r in rows[tag]:
            pid = str(r.get("暫編地號", "") or "")
            if pid:
                by_pid.setdefault(pid, r)
    for tp in (temp_p or []):
        pid = str(tp.get("暫編地號", "") or "")
        if pid and pid not in by_pid:
            by_pid[pid] = tp

    for pid, exp in (("628-42(1)", "G011"), ("628-53(2)", "G025")):
        r = by_pid.get(pid)
        orig = str((r or {}).get("原地號", "") or "")
        gid = resolve(orig, own_map) if orig else ""
        ok = (gid == exp)
        ctl.append(("造%s [必非零·已知答案] `%s` → 歸戶"
                    % ("甲" if pid == "628-42(1)" else "丙", pid),
                    "原地號 `%s` ⇒ `%s`" % (orig or "（空）", gid or "（空）"),
                    "`%s`" % exp, ok))
    sen = _sentinel(own_map)
    gid_s = resolve(sen, own_map)
    ctl.append(("造乙 [必為空] 人造哨兵（**執行期組出**·字面⛔ 出艙）",
                "⇒ `%s`" % (gid_s or "（空）"), "（空）", gid_s == ""))
    for name, got, exp, ok in ctl:
        print("  %s %-58s 得 %-34s 期 %-8s" % ("✅" if ok else "🔴", name, got, exp))
    if not all(o for *_x, o in ctl):
        print()
        print("🔴 **三造未全成立 ⇒ 量測器紅 ⇒ loud 拒測**（⛔ 出艙受詞之值·`坑 u`）")
        return 2
    print("  ⇒ **器非紅** ✅（已知答案二造相符 ⋀ 哨兵歸零）")
    print()

    # ── 受詞（三宗·逐宗·⛔ 以「受詞二宗」呈之）────────────────────────────
    print("── 受詞：`c2` 之剔除宗（`0m` **`3` 宗**〔直接 `2` ＋ **級聯 `1`**〕／"
          "`3.5m` **`1` 宗**〔直接 `1` ＋ 級聯 `0`〕）" + "─" * 10)
    print("  🛑 `0m` 實為 **`3` 宗**——**⛔ 以「受詞二宗」呈之**（補令七 `§四-2` 款 `4`）")
    print("  🔒 「處置」欄**逐 (宗, 情境)**·⛔ 本器所量——其出處 ＝ `c1` 側支之實跑落檔")
    print("     `verify/out/WG9269R_c1_on_drop.log`（`0m` 消失 `3` 宗／`3.5m` 消失 `1` 宗·"
          "二情境之終態皆⛔ 再有閘一不合格者）＋ 補令七 `§四-1` 之二分類。")
    print("  🔒 **本器所量者** ＝ 歸戶 ⋀ `a 面積` ⋀ `G` ⋀ `宗地寬度`（皆 `off` 態·管線跑畢）。")
    print()
    hdr = ("宗地", "情境", "歸戶", "a 面積(㎡)", "原分配 G(㎡)", "宗地寬度(m)", "處置")
    print("  | %-12s | %-5s | %-6s | %-11s | %-13s | %-12s | %-14s |" % hdr)
    print("  |%s|%s|%s|%s|%s|%s|%s|" % ("-" * 14, "-" * 7, "-" * 8, "-" * 13,
                                        "-" * 15, "-" * 14, "-" * 16))
    bad, n_judged = [], 0
    out_rows = []
    for pid in SUBJ:
        known = KNOWN_GID[pid]
        a_exp, g_exp, w_exp = ANCHOR_0M[pid]
        for tag in ("0m", "3.5m"):
            disp = DISPOSAL[(pid, tag)]
            r = None
            for rr in rows.get(tag, []):
                if str(rr.get("暫編地號", "") or "") == pid:
                    r = rr
                    break
            if r is None:
                continue
            n_judged += 1
            orig = str(r.get("原地號", "") or "")
            gid = resolve(orig, own_map)
            a = float(r.get("a 面積(㎡)", 0) or 0)
            g = float(r.get("G(㎡)", 0) or 0)
            wd = float(r.get("宗地寬度(m)", 0) or 0)
            print("  | %-12s | %-5s | %-6s | %11.2f | %13.2f | %12.2f | %-14s |"
                  % (pid, tag, gid or "（空）", a, g, wd, disp))
            out_rows.append((pid, tag, gid, a, g, wd, disp))
            if tag == "0m":
                # 外部錨（`常規八 二` ①）
                for nm, got, exp in (("a 面積", a, a_exp), ("G", g, g_exp),
                                     ("宗地寬度", wd, w_exp)):
                    if abs(got - exp) > 0.005:
                        bad.append("%s·%s 得 %.4f ≠ 補令七 §四-1 之 %.2f"
                                   % (pid, nm, got, exp))
                if known is not None and gid != known:
                    bad.append("%s·歸戶 得 %s ≠ 已知 %s" % (pid, gid or "（空）", known))
    print()
    if n_judged == 0:
        print("🔴 **判定集為空 ⇒ loud 拒測**（「未量」⛔ 與「量得為零」共用出艙碼）")
        return 3
    print("  判定集基數 ＝ **%d** 格（宗 × 情境）" % n_judged)
    print()

    print("── 外部錨之判（`常規八 二` ①·⛔ 以 `N/N` 自證）" + "─" * 52)
    if bad:
        for b in bad:
            print("  🔴 %s" % b)
        print()
        print("🔴 **受詞紅**：實測與補令七 `§四-1` 之表不符 ⇒ ⛔ 據本表下任何結論")
        return 5
    print("  ✅ 三宗之 `a 面積`／`G`／`宗地寬度` 與補令七 `§四-1` 之表逐值相符（`0m`）")
    print("  ✅ 二宗之歸戶與 `W-G.9-269R_前置階.md §戊` 項 `5` 之已知值相符")
    print()

    tgt = [r for r in out_rows if r[0] == "628-27(1)"]
    print("── 🔴 **本器之受詞**：`628-27(1)` 之歸戶" + "─" * 60)
    for pid, tag, gid, a, g, wd, disp in tgt:
        print("  情境 `%s`：歸戶 ＝ **`%s`**（`a 面積 %.2f ㎡`／原分配 `G %.2f ㎡`／"
              "宗地寬度 `%.2f m`·**%s**）" % (tag, gid or "（空）", a, g, wd, disp))
    print()
    print("🔒 **其量級**：`628-27(1)` 之原分配 `G ＝ %.2f ㎡`，較 `628-42(1)`（`0.23`）與"
          % (tgt[0][4] if tgt else float("nan")))
    print("   `628-53(2)`（`0.00`）**大二個數量級** ⇒ `c2` 之土地後果大於補令三 `§零-1` 之受詞表。")
    print("🛑 **`GB-159` 仍有效**：受影響之宗（**今為三宗**）之配地圖與負擔表 **⛔ 對外**。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
