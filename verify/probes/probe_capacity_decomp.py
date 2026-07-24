# -*- coding: utf-8 -*-
"""W-G.4 §4 容量拆解探針——**forced 角落鎖定是否吃掉增配空間**（KL 診斷問題）。

## 存在理由

KL 診斷：達½之 9 戶有 2 戶落不下（3.5m E2 容量不可行），是否因**街角 forced 鎖定之抵費地**
吃掉增配空間。倉內既有基線不足以回答——`池流向 CSV` 只有池總量與 E1 後殘池，**未拆不可達量**
（`unreach` 之「碎片」vs「forced 角落鎖定」）。本探針即時計算並拆項。

## 取數路徑（**即時計算·非讀 CSV**·誠實載明）

注入 `verify/wf_f4.py` 之 `_e2_optimal`（`cost` 迴圈前·`_canon_G`/`_elig`/`mw_by`/`reachable`
已定義），dump 逐塊拆解。以 `WV_BAKE=<tmp>` 跑 `verify/run_verification.py` 使 F.0–F.3 存在性
守衛過、**F.4 trunk-E 實跑**。0m（E2 可行）與 3.5m（E2 不可行）兩情境各觸發一次。

⚠️ **基線為波前產物·待重烤**：F.4 之輸入（F.0–F.3 baseline）係波前烤、且 F.0 六格錨過期
（§11.3）。故 `pool`／`reachable`／`consume` 反映「當前碼 ＋ WV_BAKE 側錄」態，數值可能過期；
**結構性結論**（拆項來源、forced 鎖定佔比）不受過期錨影響、**絕對數值**則待波末重烤複核。

## 三分類出處（**禁自行分類**）

拆項一律走 `wf_f1._classify_fragments` 之「碎片」／「forced角落鎖定」／「池主體」三分類
（KL 明令）。`unreach[b] = 碎片Σ + forced角落鎖定Σ`（`wf_f4._s0_unreachable`·:284-286）。

## 反事實（純試算·不改治理碼·不改裁定）

| 情境 | reachable | 測 |
|---|---|---|
| 甲 現況 | `pool − 碎片 − forced鎖定`（＝治理碼 `reachable`） | 基準 |
| 乙 釋 forced | `pool − 碎片`（forced 鎖定改計入 reachable） | forced 吃掉多少 |
| 丙 釋碎片 | `pool − forced鎖定`（僅碎片計入 reachable） | 對照 |

⚠️ **一階近似**：`consume`（宗需要之池量·solo canonical G）為**幾何性質**、與池釋不釋 forced
無關，故反事實**僅放大容量約束、不重算幾何**（釋出 forced 後真實 consume 可能微調）。
「可容筆數上界」＝各塊**最小** consume 貪心填（與指派組合無關之必要條件）；
「可行指派」＝窮舉 `itertools.product` ＋容量剪枝（充分·找到即輸出一組）。

## 重跑
    WV_CAPDECOMP=1 python verify/probes/probe_capacity_decomp.py

（~15–25 分鐘；F.4 慢·兩情境各 ~36 次額外 `_canon_G`。輸出
`verify/out/probe_capacity_decomp.log`＋`.csv`。探針暫時注入純 print 再逐位還原原檔·引擎零常駐改動。）
"""
import argparse
import atexit
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
TARGET = os.path.join(VERIFY, "wf_f4.py")
OUTDIR = os.path.join(VERIFY, "out")

MARK = "# WV_CAP"

# ── 注入片段一：dump helper（module 級·插於 `def _e2_optimal(` 前）─────────────────
CAP_HELPER = r'''def _cap_decomp_dump(tag, ns, snap, cb_by, cad, eng, forced, mina, mw_by,
                     reachable, unreach, households, elig_fn, canon_fn, blocks):  # WV_CAP
    """容量拆解 dump（純計算＋輸出·零 state 改動；canon_fn 內 add_syn→remove 復原）。"""
    import os as _o, collections as _c, itertools as _it
    import numpy as _np
    out = _o.environ.get("WV_CAPDECOMP_OUT")
    if not out:
        return
    L = []
    pool = {b: float(eng.pool(b)) for b in blocks}
    # 三分類拆項（禁自行分類·出處 wf_f1._classify_fragments）
    frags = wf_f1._classify_fragments(ns, snap, cb_by, cad, eng.sg()["g_rows"], forced)
    frag_a = _c.defaultdict(float); lock_a = _c.defaultdict(float); lock_detail = []
    for f in frags:
        b, cat, ar = f["街廓"], f["三分類"], float(f["面積"])
        if cat == "碎片":
            frag_a[b] += ar
        elif cat == "forced角落鎖定":
            lock_a[b] += ar
            s_rel = f.get("s")
            side = "左" if (s_rel is not None and s_rel < 0.5) else "右"
            _fl = (cad.get("front_lines") or {}).get(b) or {}
            sr = None
            try:
                p1 = _np.array(_fl["p1"], float); p2 = _np.array(_fl["p2"], float)
                dh = (p2 - p1) / (float(_np.linalg.norm(p2 - p1)) or 1.0)
                aa = ns["alloc_normal_axis"]((cad.get("alloc_dir_by_block") or {}).get(b))
                sr = ns["_strip_s_range"](f["poly"], dh, p1, aa)
            except Exception:
                sr = None
            fo = (forced or {}).get(b, {}) or {}
            src = ("left_forced_offset" if (fo.get("left_forced_offset") and side == "左")
                   else "right_forced_offset" if (fo.get("right_forced_offset") and side == "右")
                   else "?")
            lock_detail.append((b, side, round(ar, 2),
                                (round(float(sr[0]), 3), round(float(sr[1]), 3)) if sr else None,
                                round(float(s_rel), 3) if s_rel is not None else None, src))
    # 完整 consume matrix（重算·**不受現況 reachable 過濾**·canonical G 與池釋不釋無關）
    full_c = {}
    for h in households:
        el, _w = elig_fn(h)
        for b in el:
            G, W, af = canon_fn(h, b)
            if G is None:
                continue
            gt = _valid_G(G, W, mw_by[b], mina[b])
            full_c[(h["gid"], b)] = round(max(G, gt), 2)

    def _ub(reach_fn):
        rows, tot = [], 0
        for b in blocks:
            cap = reach_fn(b) - mina[b] + 0.5
            items = sorted(v for (g, bb), v in full_c.items() if bb == b)
            s = n = 0
            for x in items:
                if s + x <= cap + 1e-9:
                    s += x; n += 1
                else:
                    break
            tot += n
            rows.append((b, n, items[0] if items else None, round(cap, 2)))
        return rows, tot

    def _feas(reach_fn, cap_space=300000):
        gids = [h["gid"] for h in households]
        opts = [[b for (g, b) in full_c if g == gg] for gg in gids]
        if any(not o for o in opts):
            return "某戶無候選", None
        sp = 1
        for o in opts:
            sp *= len(o)
        if sp > cap_space:
            return f"space {sp}>{cap_space}·未窮舉", None
        for combo in _it.product(*opts):
            by = _c.defaultdict(float)
            for g, b in zip(gids, combo):
                by[b] += full_c[(g, b)]
            if all(cs <= reach_fn(b) - mina[b] + 0.5 for b, cs in by.items()):
                return "可行", list(zip(gids, combo))
        return "窮舉無可行", None

    reach = {"甲現況": (lambda b: reachable[b]),
             "乙釋forced": (lambda b: max(pool[b] - frag_a[b], 0.0)),
             "丙釋碎片": (lambda b: max(pool[b] - lock_a[b], 0.0))}
    need = len(households)

    L.append("=" * 96)
    L.append(f"[CAPDECOMP] tag={tag}  戶數(需求群)={need}  塊={blocks}")
    L.append("-" * 96)
    L.append("塊    pool    碎片Σ  forced鎖Σ unreach自檢  reachable   MinA   容量  最小cons 可容上界")
    for b in blocks:
        _un_self = frag_a[b] + lock_a[b]
        _un_chk = float(unreach.get(b, 0.0))
        _reach = reachable[b]; _cap = _reach - mina[b] + 0.5
        _items = sorted(v for (g, bb), v in full_c.items() if bb == b)
        _s = _n = 0
        for x in _items:
            if _s + x <= _cap + 1e-9:
                _s += x; _n += 1
            else:
                break
        _flag = "" if abs(_un_self - _un_chk) < 0.01 else f" ⚠️自檢≠{_un_chk:.2f}"
        L.append(f"{b:4} {pool[b]:8.2f} {frag_a[b]:7.2f} {lock_a[b]:8.2f} "
                 f"{_un_self:9.2f}{_flag:>2} {_reach:9.2f} {mina[b]:7.2f} {_cap:6.2f} "
                 f"{(_items[0] if _items else 0):8.2f} {_n:6d}")
    L.append("-" * 96)
    L.append("forced 角落鎖定片明細（塊·側·面積·s區間·s_rel·來源規則）：")
    if lock_detail:
        for b, side, ar, sr, s_rel, src in lock_detail:
            L.append(f"  {b} {side}  {ar:8.2f}㎡  s∈{sr}  s_rel={s_rel}  ←{src}")
    else:
        L.append("  （無 forced 角落鎖定片）")
    # §3 街角帶 236.9 對數（R2左／R5左／R3右·毛短計）
    _t = {("R2", "左"): 0.0, ("R5", "左"): 0.0, ("R3", "右"): 0.0}
    for b, side, ar, sr, s_rel, src in lock_detail:
        if (b, side) in _t:
            _t[(b, side)] += ar
    _sum3 = sum(_t.values())
    L.append(f"§3 對數（R2左 {_t[('R2','左')]:.2f} ＋ R5左 {_t[('R5','左')]:.2f} ＋ "
             f"R3右 {_t[('R3','右')]:.2f}） = {_sum3:.2f}㎡  vs 235~237 毛短計 "
             f"→ {'落在拆項內' if 230 <= _sum3 <= 243 else 'NOT·差 %.1f' % (_sum3 - 236.9)}")
    L.append("-" * 96)
    for nm, rf in reach.items():
        rows, tot = _ub(rf)
        verdict, assign = _feas(rf)
        L.append(f"[{nm}] 可容筆數上界 逐塊 {[(b, n) for b, n, mn, cap in rows]} "
                 f"｜和={tot} vs 需求={need} ｜窮舉={verdict}")
        if assign:
            L.append(f"        指派：{assign}")
    L.append("完整 consume matrix（重算·不受現況 reachable 過濾）：")
    L.append("  " + "；".join(f"{g}@{b}={v}" for (g, b), v in sorted(full_c.items())))
    L.append("=" * 96)
    with open(out, "a", encoding="utf-8") as fp:
        fp.write("\n".join(L) + "\n")


def _e2_optimal('''

ANCHOR_HELPER = "def _e2_optimal("

# ── 注入片段二：呼叫（插於 `cost, elig_map, why_map = {}, {}, {}` 前）──────────────
ANCHOR_CALL = "    cost, elig_map, why_map = {}, {}, {}\n"
INJECT_CALL = (
    "    if __import__('os').environ.get('WV_CAPDECOMP_OUT'):  " + MARK + "\n"
    "        try:  " + MARK + "\n"
    "            _cap_decomp_dump(tag, ns, snapE, cb_by, cad, eng, forced, mina, mw_by,  " + MARK + "\n"
    "                             reachable, unreach, households, _elig, _canon_G, blocks)  " + MARK + "\n"
    "        except Exception as _ce:  " + MARK + "\n"
    "            __import__('sys').stderr.write('[CAPDUMP-ERR] %r\\n' % (_ce,))  " + MARK + "\n"
    + ANCHOR_CALL)


def _inject(src):
    for a, n in ((ANCHOR_HELPER, "helper"), (ANCHOR_CALL, "call")):
        if src.count(a) != 1:
            raise RuntimeError(
                f"🔴 探針 anchor『{n}』於 wf_f4.py 出現 {src.count(a)} 次（需恰 1）"
                "——引擎結構已變，請更新本探針 anchor（no-silent-fallback）")
    src = src.replace(ANCHOR_HELPER, CAP_HELPER, 1)
    src = src.replace(ANCHOR_CALL, INJECT_CALL, 1)
    return src


def main():
    ap = argparse.ArgumentParser(description="W-G.4 §4 容量拆解探針（forced 鎖定吃空間？）")
    args = ap.parse_args()

    for _st in (sys.stdout, sys.stderr):
        try:
            _st.reconfigure(encoding="utf-8")
        except Exception:
            pass

    if os.environ.get("WV_CAPDECOMP") != "1":
        print("🔴 本探針須 WV_CAPDECOMP=1 明示啟用（避免誤入 run_all／CI）。"
              "\n   例：WV_CAPDECOMP=1 python verify/probes/probe_capacity_decomp.py")
        return 2

    with open(TARGET, "rb") as f:
        original = f.read()
    if MARK.encode() in original or b"_cap_decomp_dump" in original:
        print(f"🔴 {TARGET} 已含探針標記（前次異常中止？）。請先 `git checkout -- verify/wf_f4.py` 再跑。")
        return 2

    os.makedirs(OUTDIR, exist_ok=True)
    logp = os.path.join(OUTDIR, "probe_capacity_decomp.log")
    csvp = os.path.join(OUTDIR, "probe_capacity_decomp.csv")
    import tempfile
    bake = tempfile.mkdtemp(prefix="wv_capdecomp_bake_")
    for p in (logp, csvp):
        if os.path.exists(p):
            os.remove(p)

    def _restore():
        try:
            with open(TARGET, "rb") as fh:
                if fh.read() == original:
                    return
            with open(TARGET, "wb") as fh:
                fh.write(original)
            print("↩️  已還原 verify/wf_f4.py（探針零殘留）")
        except Exception as e:                                  # pragma: no cover
            print(f"🔴 還原失敗：{e} → 請立即 `git checkout -- verify/wf_f4.py`")
    atexit.register(_restore)

    rc = 1
    try:
        # 工作區 CRLF（git autocrlf）：先正規化 LF 再比對 anchor（否則恆 0 次）。還原走 original bytes 無損。
        src = original.decode("utf-8").replace("\r\n", "\n")
        with open(TARGET, "w", encoding="utf-8", newline="\n") as f:
            f.write(_inject(src))
        subprocess.run([sys.executable, "-m", "py_compile", TARGET], check=True)

        env = dict(os.environ)
        env["WV_BAKE"] = bake                    # F.0-F.3 存在性守衛過 → F.4 trunk-E 實跑
        env["WV_CAPDECOMP_OUT"] = logp
        env["PYTHONIOENCODING"] = "utf-8"

        print("▶️  跑 run_verification（WV_BAKE→F.4 實跑）·容量拆解 dump（0m＋3.5m 兩情境）")
        proc = subprocess.run([sys.executable, os.path.join(VERIFY, "run_verification.py")],
                              cwd=REPO, env=env,
                              stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
        rc = 0 if proc.returncode in (0, 1) else proc.returncode
        print(f"   run_verification exit={proc.returncode}")
        _err = (proc.stderr or b"").decode("utf-8", "replace")
        for ln in _err.splitlines():
            if "CAPDUMP-ERR" in ln:
                print("   " + ln)
    finally:
        _restore()

    if os.path.exists(logp):
        print(f"\n📄 {logp}\n")
        print(open(logp, encoding="utf-8").read())
    else:
        print("🔴 無 dump 輸出——注入未觸發或 _e2_optimal 未被呼叫（0m/3.5m 皆提前 return？）")
        return 1
    return rc


if __name__ == "__main__":
    sys.exit(main())
