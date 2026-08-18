#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""【W-G.9-69】**乙式耦合斷言**（`K-9-5-14`／`K-9-5-15` 之機械載體）⛔ 零生產碼

**受詞（不變式·⛔ 不得改寫）**：對每一街角格，
  **平移後側界與 SIDELINE 之垂距 ＝ `max(_seg_P0Ps · sinθ, T)`**，
  `T = setback + 畸零地最小寬`。

🔒 **為何需要這支**（`Z-1`／`Z-2`·KL 裁 2026-08-19 之**耦合條款**）：
  `K-9-5-15 二`「街角第 1 宗之寬度不另量、面積夠即算過」之豁免、與 `GB-84` 之結案，
  **其前提是構造為乙式**。構造若被回退為甲式（沿 `d̂` 平移·路平行距），
  **碼面不會有任何一處報錯**——因為「不設閘」本身沒有可紅之物。
  ⇒ **本檔即那個「可紅之物」**；🔴 **本檔轉紅 ⇒ `GB-84` 之結案自動回復為未結。**

🔒 **異源（⛔ 非套套邏輯·`fixture-provenance`）**：
  · 左式（**實測**）＝ 自 `_build_corner_range_v3` **所產之範圍多邊形**還原之垂距
    （`probe_WG960_fitcore.perp_width`·量的是**輸出幾何**）；
  · 右式（**期望**）＝ `probe_WG960_fitcore.geom()` **自 CAD 獨立重導**之
    `_seg_P0Ps`／`sinθ`（其自 FRONT_LINE／SIDE_LINE／截角三角形重算 `P0`／`Ps`，
    ⛔ **未讀**生產碼內之 `S1_perp`／`S1_par`）＋ 快照之 `min_width`。
  ⇒ 二側**不共用被測之那一段程式** ⇒ 構造回退時左式變、右式不變 ⇒ **會咬**。

🔒 **判別力自檢（施工單 `A-2`·⛔ 缺之則本閘不計為證據）**：`_selfcheck_bites()` 於
  tempdir 造 `app.py` **複本**並就地回退構造（**每處先斷言命中恰 1**·⛔ 禁靜默），
  以該複本重跑同一斷言 ⇒ **須有格不成立**並**具名**。⛔ 倉內 `app.py` 全程未動；
  複本用畢即刪。**二式並試**（⛔ 不得只試一式）：

  | 變異 | 改動 | 所得垂距 |
  |---|---|---|
  | `A`（施工單 `A-2` 之**逐字**）| `S1_perp = max(seg·sinθ, T)` → `max(seg, T)` | `max(seg, T)` |
  | `B`（`Z-1` 耦合條款所稱之**真甲式**：沿 `d̂` 平移·路平行距）| 併改 `S1_par = S1_perp / _sin_t` → `S1_par = S1_perp` | `max(seg, T)·sinθ` |

  🔴 **實測所得之分工（`W-G.9-69` §B·⛔ 與施工單 `P3` 之預測不同·照實載）**：
  · `B`（真甲式）**咬在更上游**——`app.py` 自身之**構造自檢**先行 `_stop`
    （`垂距 獨立覆算 ≠ S1_perp`）⇒ 該回退**建不出多邊形**、⛔ **非靜默**。
  · `A` 則**繞過**該自檢：其保留 `S1_par = S1_perp / sinθ`，而自檢之 `_Tp` 正由
    `S1_par` 所造 ⇒ `垂距 ＝ S1_par·sinθ ＝ S1_perp` **恆成立**（閉式自證）
    ⇒ 🔴 **`A` 才是真正「碼面不會有任何一處報錯」之靜默回退** ⇒ **本閘即其可紅之物**。
  🔒 **由是**：`Z-1`／`Z-2` 之「無可紅之物」，其成立域 ＝ **`A` 類**（`B` 類已有閘）。
  ⚠️ `A` 於 `setback = 3.5`（`T` 全支配）**判別力恰為 0**（`max(seg,T) = T = 期望`）
  ⇒ **`SETBACKS` 之二情境、`MUTANTS` 之二變異，皆⛔ 不得省。**

🔒 **儀器沿用既有者**（`build_ctx`／`build_range`／`geom`／`perp_width`／`EIGHT`）
  ——⛔ 未新增第二份判定原語（`GB-8`）。
"""
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
for _p in (HERE, os.path.join(HERE, "probes"), os.path.join(HERE, "fixtures")):
    sys.path.insert(0, _p)

import app_harvest                                                  # noqa: E402
from probe_WG960_fitcore import build_ctx, build_range, geom, perp_width   # noqa: E402
from probe_WG963_eps_tolerance import EIGHT                         # noqa: E402

TOL = 1e-9
SETBACKS = (0.0, 3.5)
ENV_MUT = "WG969_MUTANT_APP"

# 🔒 構造回退之**逐字**受詞（`app.py` `_build_corner_range_v3` 內·K-9-5-14 落地之二行）
YI_LINE = "S1_perp = max(_seg_P0Ps * _sin_t, T)"
JIA_LINE = "S1_perp = max(_seg_P0Ps, T)"
YI_PAR = "S1_par = S1_perp / _sin_t"
JIA_PAR = "S1_par = S1_perp"

# 變異式：(代號, 說明, [(舊字樣, 新字樣), …])
MUTANTS = (
    ("A", "施工單 A-2 逐字：`S1_perp` 改回 `max(seg, T)`（垂距 ⇒ max(seg,T)）",
     ((YI_LINE, JIA_LINE),)),
    ("B", "Z-1 耦合條款之真甲式：併改 `S1_par` 不除 sinθ（垂距 ⇒ max(seg,T)·sinθ）",
     ((YI_LINE, JIA_LINE), (YI_PAR, JIA_PAR))),
)


def rows_for(ns, cb_by, cad, snapshot, wd, setback):
    """八格逐格：(街廓, 側, sinθ, seg, T, 期望 S1_perp, 實測垂距, 是否成立)。

    🔒 期望與實測**異源**（見 module docstring）；容差 `TOL`。
    """
    out = []
    for lbl, which in EIGHT:
        g = geom(ns, cb_by, cad, lbl, which)
        min_width = wd[lbl][0]
        T = setback + min_width
        want = max(g["seg"] * g["sin"], T)                  # 乙式（期望·獨立重導）
        poly = build_range(ns, cb_by, cad, snapshot, wd, lbl, which, setback)
        got = perp_width(poly, g["S1"], g["sn"])            # 實測（生產碼之輸出幾何）
        out.append((lbl, which, g["sin"], g["seg"], T, want, got,
                    abs(got - want) <= TOL))
    return out


def run_assertions(app_py=None):
    """跑全部情境之斷言。`app_py` 非 None ⇒ 以該複本之 harvest 取代預設（判別力用）。

    ⛔ **不新增第二份 ctx 組裝**：以 `app_harvest._CACHE` 就地灌注，
       使 `build_ctx()` 之 `harvest()` 命中複本 ⇒ 其後路徑**逐字沿用**既有儀器。
    """
    if app_py is not None:
        app_harvest._CACHE[app_harvest.APP_PY] = app_harvest.harvest(app_py)
    ns, cb_by, cad, snapshot, wd, _t = build_ctx()
    res = {}
    for sb in SETBACKS:
        res[sb] = rows_for(ns, cb_by, cad, snapshot, wd, sb)
    return res


def _bad_names(res):
    return [f"{lbl}/{which}@sb={sb:g}"
            for sb in sorted(res) for lbl, which, _s, _g, _T, _w, _go, ok in res[sb]
            if not ok]


def _make_mutant(dst_dir, subs):
    """造回退複本；回 (複本路徑, [每處命中數])。⛔ 任一處命中非 1 即由呼叫端停機。"""
    src = os.path.join(REPO, "app.py")
    with open(src, "r", encoding="utf-8") as f:
        txt = f.read()
    hits = [txt.count(old) for old, _new in subs]
    dst = os.path.join(dst_dir, "app.py")
    if all(h == 1 for h in hits):
        for old, new in subs:
            txt = txt.replace(old, new)
        with open(dst, "w", encoding="utf-8", newline="") as f:
            f.write(txt)
    return dst, hits


def _bite_once(code, desc, subs):
    """單一變異之判別力。回 (ok, 訊息, 具名清單)。"""
    tmp = tempfile.mkdtemp(prefix=f"wg969_{code}_")
    try:
        mut, hits = _make_mutant(tmp, subs)
        if not all(h == 1 for h in hits):
            return False, f"變異 {code} 回退點命中 {hits}（每處期 1）⇒ ⛔ 受詞已漂移、禁猜", []
        r = subprocess.run([sys.executable, os.path.abspath(__file__)],
                           capture_output=True, text=True, encoding="utf-8",
                           timeout=900, env={**os.environ, ENV_MUT: mut})
        out = (r.stdout or "").splitlines()
        stop = next((ln for ln in out if ln.startswith("#STOP ")), None)
        if stop is not None:
            # 🔒 **咬在更上游**：生產碼自身之構造自檢先行 `_stop` ⇒ 該回退**建不出多邊形**。
            #   ⛔ 不以「子行程掛掉」概括之——須具名其停機訊息，且該訊息須指向構造自檢。
            msg = stop[len("#STOP "):]
            ok = ("構造自檢不合" in msg) and ("K-9-5-14" in msg)
            return ok, (f"變異 {code}（{desc}）⇒ **生產碼構造自檢先行停機**："
                        + msg[:150]), []
        line = next((ln for ln in out if ln.startswith("#BITE ")), None)
        if line is None:
            return False, (f"變異 {code} 之複本子行程既未回報 `#BITE` 亦未回報 `#STOP`"
                           f"（rc={r.returncode}）⇒ ⛔ 不得推定其已被咬"), []
        payload = line[len("#BITE "):].strip()
        cnt = int(payload.split("|", 1)[0])
        names = [s for s in payload.split("|", 1)[1].split(",") if s]
        return (cnt > 0), f"變異 {code}（{desc}）⇒ 本閘咬中 {cnt} 格", names
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def _selfcheck_bites():
    """判別力：**二式並試**，每式皆須有格不成立。回 [(code, ok, 訊息, 具名清單)]。"""
    return [(code,) + _bite_once(code, desc, subs) for code, desc, subs in MUTANTS]


def main():                                                         # noqa: C901
    mut = os.environ.get(ENV_MUT)
    if mut:
        # 🔒 判別力子行程：回報「本閘咬到幾格」**或**「生產碼自身先行停機」；
        #   rc 恆 0（判由父行程為之）。⛔ 只接 `RuntimeError`（＝ `app.py` 之 `_stop`），
        #   ⛔ 不概括其他例外——否則任何無關崩潰都會被誤記為「已被咬」。
        try:
            res = run_assertions(mut)
        except RuntimeError as e:
            print("#STOP " + " ".join(str(e).splitlines())[:300])
            return 0
        bad = _bad_names(res)
        print(f"#BITE {len(bad)}|{','.join(bad)}")
        return 0

    res = run_assertions(None)
    rc = 0
    print("=" * 108)
    print("【W-G.9-69】乙式耦合斷言　`垂距 ＝ max(_seg_P0Ps·sinθ, T)`"
          "（`K-9-5-14`／`K-9-5-15`·KL 裁 2026-08-19 耦合條款之機械載體）")
    print("=" * 108)
    for sb in SETBACKS:
        print(f"  ── setback = {sb:g} m（T ＝ setback ＋ 畸零地最小寬）" + "─" * 52)
        print(f"  {'街廓':<5}{'側':<7}{'sinθ':>12}{'_seg_P0Ps':>12}{'seg·sinθ':>12}"
              f"{'T':>8}{'期望 S1_perp':>14}{'實測垂距':>16}{'|差|':>12}{'判':>5}")
        for lbl, which, sin, seg, T, want, got, ok in res[sb]:
            if not ok:
                rc = 1
            print(f"  {lbl:<5}{which:<7}{sin:>12.7f}{seg:>12.6f}{seg * sin:>12.6f}"
                  f"{T:>8.2f}{want:>14.6f}{got:>16.9f}{abs(got - want):>12.3e}"
                  f"{('✅' if ok else '🔴'):>4}")
    n_all = sum(len(v) for v in res.values())
    n_ok = sum(1 for v in res.values() for r in v if r[-1])
    print("-" * 108)
    print(f"  ⇒ **不變式成立 {n_ok}／{n_all} 格**（容差 {TOL:g}；八格 × {len(SETBACKS)} 情境）")
    for nm in _bad_names(res):
        print(f"      🔴 不成立：{nm}")

    print("-" * 108)
    print("  **判別力自檢（⛔ 二式並試·缺一則本閘不計為證據）**")
    for code, ok_b, msg, names in _selfcheck_bites():
        print(f"  {'✅' if ok_b else '🔴'} {msg}")
        for nm in names:
            print(f"      · 不成立：{nm}")
        if not ok_b:
            rc = 1
            print(f"     🔴 **變異 {code} 未被咬 ⇒ 本閘之綠無效力**"
                  "（`fixture-provenance`：不會咬的 fixture ＝ 假綠）")
    print("     🔒 倉內 `app.py` 全程未動；複本已刪。")
    print("=" * 108)
    print("乙式耦合斷言：" + ("✅ 綠" if rc == 0 else "🔴 紅"))
    return rc


if __name__ == "__main__":
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8")
        except Exception:                                           # noqa: BLE001
            pass
    sys.exit(main())
