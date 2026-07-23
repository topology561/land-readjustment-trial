# -*- coding: utf-8 -*-
"""W-G.4 探針：R1@3.5m 推進序列（原位次 vs 池內遞補混排）逐宗 run-time dump。

**存在理由（驗證紀律·claude.ai 複驗 2026-07-23 必辦①）**：
3.5m bisect（`docs/reports/W-G.4_§4_628-37_3.5m情境再定位_§3首破.md`）與混排坐實
（`docs/reports/W-G.4_§4_兩階段落位_坐實.md`）兩次關鍵實證，其 instrumentation 皆為
拋棄式臨時注入 → **不可復現**，違反「只信倉·可由建構複驗」。本檔將該兩次探針收斂為
**入倉腳本**：往後凡作為裁定依據之實證，探針一律入倉、附重跑指令。

**預設不影響 `run_all`**：本檔為獨立 script，`run_all.py`／`run_verification.py` 均不 import；
且未設 `WV_PROBE=1` 時**拒跑**（loud）。零 gate、零 baseline、零引擎常駐改動。

## 重跑指令
    python verify/probes/probe_stage_order.py --setback 3.5 --block R1 --lot "628-37(1)"
（環境需 `WV_PROBE=1`；script 會自帶。加 `--no-break` 可跑完整輪不早停。）

## 機制
1. 對 `verify/stepg_pipeline.py` 之 `run_step_g` 左/右推進迴圈**暫時**注入純 print 探針
   （三個 anchor·idempotent·標記 `# WV_PROBE`）；原檔 bytes 先備份。
2. 以 `WV_BAKE=<tmp>` 跑 `verify/run_verification.py`——`diff_rows` 於 WV_BAKE 時寫 got 並
   return 綠（run_verification.py:274-278）→ F.0–F.3 存在性守衛過 → **F.4 trunk-E 實跑**
   （否則 F.0 六格錨紅級聯、F.4 skip、探針量不到池內遞補宗）。
3. `--break-tol`（預設 1.0）：目標宗於目標 setback 首次 |G−幾何|>tol → 記錄 BREAK 並
   `os._exit(66)` 早停（界 runtime；完整輪約 30+ 分鐘）。
4. **finally 一律還原**原檔 bytes 並逐位比對；另掛 atexit 保險。引擎**不留任何常駐改動**。

## 輸出
- `verify/out/probe_stage_order_<block>_<setback>.log`：逐宗 `[WVPROBE] k=v …`
- `verify/out/probe_stage_order_<block>_<setback>.csv`：同資料表格化（欄見 FIELDS）
- stdout：破世代推進序列摘要表（左組／右組·含 pos／cumS／S_remain／|Δ|）

## 欄位語意
- `pos`＝`_spatial_order_parcels_v2` 之 `pre_position`（投影位次）；`idx`＝`_ov2_idx`。
- `reg`＝`分攤登記面積_m2`。**原地主宗 reg>0；`wf_f4.add_syn` 生成之池內遞補合成宗 reg==0**
  （wf_f4.py:183 硬寫 0.0）——分類**資料驅動**，不以 `74·` 名稱前綴判別（泛用紀律）。
- `Srem`＝`S_remain`＝`actual_max_proj − left_cum_S − right_cum_S`（stepg:618 右／:547 左）。
- `smax`＝右組 `actual_max_proj`（`_oblique_s_max`）／左組 `S_block_max`。
"""
import argparse
import atexit
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
TARGET = os.path.join(VERIFY, "stepg_pipeline.py")
OUTDIR = os.path.join(VERIFY, "out")

MARK = "# WV_PROBE"

FIELDS = ["sb", "side", "k", "pos", "idx", "reg", "a", "G", "geom", "dev",
          "cumS", "Sraw", "S", "Srem", "smax", "bpt", "dhat"]

# ── 注入片段（三 anchor·與 stepg_pipeline.py 現行結構對齊）────────────────────
HELPER = r'''def _wv_probe(k, sb, side, ent, tp, a, res, sremain, smax, cumS):  # WV_PROBE
    import os as _o, sys as _s
    try:
        _blk = _o.environ.get('WV_PROBE_BLOCK', '')
        _out = _o.environ.get('WV_PROBE_OUT', '')
        if not _out:
            return
        g = float(res.get('G', 0) or 0); geom = float(res.get('area_geom', 0) or 0)
        sraw = float(res.get('S_raw', res.get('S', 0)) or 0); s = float(res.get('S', 0) or 0)
        reg = float(tp.get('分攤登記面積_m2', 0) or 0)
        bpt = res.get('_wv_bpt'); dh = res.get('_wv_dh')
        line = ("[WVPROBE] sb=%s side=%s k=%s pos=%s idx=%s reg=%.2f a=%.1f G=%.2f geom=%.2f "
                "dev=%.2f cumS=%.3f Sraw=%.4f S=%.4f Srem=%.3f smax=%.3f bpt=%s dhat=%s"
                % (sb, side, k, ent.get('pre_position'), ent.get('_ov2_idx'), reg, a, g, geom,
                   abs(g - geom), cumS, sraw, s, sremain, smax, bpt, dh))
        with open(_out, 'a', encoding='utf-8') as _f:
            _f.write(line + "\n")
        _tolz = _o.environ.get('WV_PROBE_BREAK', '')
        _lot = _o.environ.get('WV_PROBE_LOT', '')
        _sbz = _o.environ.get('WV_PROBE_SB', '')
        if (_tolz and _lot and k == _lot and abs(g - geom) > float(_tolz)
                and (not _sbz or abs(float(sb) - float(_sbz)) < 0.01)):
            with open(_out, 'a', encoding='utf-8') as _f:
                _f.write("[WVPROBE-BREAK] " + line + "\n")
            _s.stderr.write("[WVPROBE] break hit -> early stop (exit 66)\n"); _s.stderr.flush()
            _o._exit(66)
    except SystemExit:
        raise
    except Exception as _e:
        try:
            _s.stderr.write("[WVPROBE-ERR] %r\n" % (_e,)); _s.stderr.flush()
        except Exception:
            pass


def compute_total_burden_rate(ns, cb, snapshot):'''

ANCHOR_HELPER = "def compute_total_burden_rate(ns, cb, snapshot):"

ANCHOR_L = "                res['_alloc_cum_S'] = left_cum_S\n"
INJECT_L = ANCHOR_L + (
    "                if blk_label == __import__('os').environ.get('WV_PROBE_BLOCK', ''):  " + MARK + "\n"
    "                    res['_wv_bpt'] = (None if baseline_pt is None else\n"
    "                                      '(%.4f,%.4f)' % (baseline_pt[0], baseline_pt[1]))  " + MARK + "\n"
    "                    res['_wv_dh'] = (None if d_hat is None else\n"
    "                                     '(%.5f,%.5f)' % (d_hat[0], d_hat[1]))  " + MARK + "\n"
    "                    _wv_probe(k, setback, 'L', entry, tp, a_m2, res, S_remain, S_block_max, left_cum_S)  " + MARK + "\n")

ANCHOR_R = "                res['_alloc_cum_S'] = right_cum_S\n"
INJECT_R = ANCHOR_R + (
    "                if blk_label == __import__('os').environ.get('WV_PROBE_BLOCK', ''):  " + MARK + "\n"
    "                    try:  " + MARK + "\n"
    "                        _wv_smax = actual_max_proj  " + MARK + "\n"
    "                    except NameError:  " + MARK + "\n"
    "                        _wv_smax = S_block_max  " + MARK + "\n"
    "                    res['_wv_bpt'] = (None if baseline_pt is None else\n"
    "                                      '(%.4f,%.4f)' % (baseline_pt[0], baseline_pt[1]))  " + MARK + "\n"
    "                    res['_wv_dh'] = (None if d_hat_rev is None else\n"
    "                                     '(%.5f,%.5f)' % (d_hat_rev[0], d_hat_rev[1]))  " + MARK + "\n"
    "                    _wv_probe(k, setback, 'R', entry, tp, a_m2, res, S_remain, _wv_smax, right_cum_S)  " + MARK + "\n")


def _inject(src):
    for a, n in ((ANCHOR_HELPER, "helper"), (ANCHOR_L, "left"), (ANCHOR_R, "right")):
        if src.count(a) != 1:
            raise RuntimeError(
                f"🔴 探針 anchor『{n}』於 stepg_pipeline.py 出現 {src.count(a)} 次（需恰 1）"
                "——引擎結構已變，請更新本探針 anchor（no-silent-fallback）")
    src = src.replace(ANCHOR_HELPER, HELPER, 1)
    src = src.replace(ANCHOR_L, INJECT_L, 1)
    src = src.replace(ANCHOR_R, INJECT_R, 1)
    return src


def _parse(path):
    rows = []
    if not os.path.exists(path):
        return rows
    with open(path, encoding="utf-8") as f:
        for ln in f:
            if not ln.startswith("[WVPROBE]"):
                continue
            d = {}
            for tok in ln.split()[1:]:
                if "=" in tok:
                    kk, vv = tok.split("=", 1)
                    d[kk] = vv
            if d:
                rows.append(d)
    return rows


def _summary(rows, lot):
    """破世代（含目標宗最後一次出現之該輪）推進序列摘要。"""
    if not rows:
        return "（無資料）"
    idxs = [i for i, r in enumerate(rows) if r.get("k") == lot]
    end = idxs[-1] if idxs else len(rows) - 1
    start = end
    seen = set()
    while start > 0:                      # 回溯至本輪起點（k 重複即跨輪）
        kk = rows[start - 1].get("k")
        if kk in seen:
            break
        seen.add(kk)
        start -= 1
    gen = rows[start:end + 1]
    out = ["", "破世代推進序列（左組 L 自 p1 往內／右組 R 自 p2 往內）", "-" * 104,
           f"{'side':<4}{'seq':<4}{'暫編地號':<18}{'類別':<8}{'pos':<5}{'cumS':>9}{'Srem':>9}{'smax':>9}{'|Δ|':>8}"]
    cnt = {"L": 0, "R": 0}
    for r in gen:
        sd = r.get("side", "?")
        cnt[sd] = cnt.get(sd, 0) + 1
        kind = "原地主" if float(r.get("reg", 0) or 0) > 0 else "池內遞補"
        flag = "  🔴" if float(r.get("dev", 0) or 0) > 1.0 else ""
        out.append(f"{sd:<4}{cnt[sd]:<4}{r.get('k',''):<18}{kind:<8}{r.get('pos',''):<5}"
                   f"{r.get('cumS',''):>9}{r.get('Srem',''):>9}{r.get('smax',''):>9}"
                   f"{r.get('dev',''):>8}{flag}")
    out.append("-" * 104)
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description="W-G.4 推進序列探針（原位次 vs 池內遞補混排）")
    ap.add_argument("--block", default="R1", help="目標街廓 label（預設 R1）")
    ap.add_argument("--lot", default="628-37(1)", help="目標宗暫編地號（破偵測用）")
    ap.add_argument("--setback", default="3.5", help="目標情境退縮 m（破偵測用；0.0 或 3.5）")
    ap.add_argument("--break-tol", default="1.0", help="|G−幾何| 破門檻（預設 1.0）")
    ap.add_argument("--no-break", action="store_true", help="不早停，跑完整輪（慢，30+ 分鐘）")
    args = ap.parse_args()

    # Windows 主控台預設 cp950 → emoji/中文 UnicodeEncodeError（同 run_all.py:14 之對策）
    for _st in (sys.stdout, sys.stderr):
        try:
            _st.reconfigure(encoding="utf-8")
        except Exception:
            pass

    if os.environ.get("WV_PROBE") != "1":
        print("🔴 本探針須 WV_PROBE=1 明示啟用（避免誤入 run_all／CI）。"
              "\n   例：WV_PROBE=1 python verify/probes/probe_stage_order.py --setback 3.5")
        return 2

    with open(TARGET, "rb") as f:
        original = f.read()
    if MARK.encode() in original or b"_wv_probe" in original:
        print(f"🔴 {TARGET} 已含探針標記（前次異常中止？）。請先 `git checkout -- verify/stepg_pipeline.py` 再跑。")
        return 2

    os.makedirs(OUTDIR, exist_ok=True)
    tag = f"{args.block}_{args.setback}"
    logp = os.path.join(OUTDIR, f"probe_stage_order_{tag}.log")
    csvp = os.path.join(OUTDIR, f"probe_stage_order_{tag}.csv")
    import tempfile
    bake = tempfile.mkdtemp(prefix="wv_probe_bake_")   # 拋棄式：勿落 verify/out 污染倉
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
            print("↩️  已還原 verify/stepg_pipeline.py（探針零殘留）")
        except Exception as e:                                  # pragma: no cover
            print(f"🔴 還原失敗：{e} → 請立即 `git checkout -- verify/stepg_pipeline.py`")
    atexit.register(_restore)

    rc = 1
    try:
        # ⚠️ 工作區於 Windows 為 CRLF（git autocrlf）；binary 讀不做 universal-newlines，
        #    故先正規化為 LF 再比對 anchor（否則 anchor 恆 0 次）。還原走 original bytes、逐位無損。
        src = original.decode("utf-8").replace("\r\n", "\n")
        with open(TARGET, "w", encoding="utf-8", newline="\n") as f:
            f.write(_inject(src))
        subprocess.run([sys.executable, "-m", "py_compile", TARGET], check=True)

        env = dict(os.environ)
        env["WV_BAKE"] = bake                    # → diff_rows 綠 → F.0-F.3 過 → F.4 trunk-E 實跑
        env["WV_PROBE_BLOCK"] = args.block
        env["WV_PROBE_LOT"] = args.lot
        env["WV_PROBE_SB"] = args.setback
        env["WV_PROBE_OUT"] = logp
        env["WV_PROBE_BREAK"] = "" if args.no_break else args.break_tol
        env["PYTHONIOENCODING"] = "utf-8"

        print(f"▶️  跑 run_verification（WV_BAKE→F.4 實跑）；block={args.block} lot={args.lot} "
              f"sb={args.setback} break_tol={'off' if args.no_break else args.break_tol}")
        proc = subprocess.run([sys.executable, os.path.join(VERIFY, "run_verification.py")],
                              cwd=REPO, env=env,
                              stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
        rc = 0 if proc.returncode in (0, 1, 66) else proc.returncode
        print(f"   run_verification exit={proc.returncode}"
              + ("（66＝探針早停·已命中破）" if proc.returncode == 66 else ""))
    finally:
        _restore()

    rows = _parse(logp)
    if rows:
        import csv as _csv
        with open(csvp, "w", encoding="utf-8-sig", newline="") as f:
            w = _csv.DictWriter(f, fieldnames=FIELDS, extrasaction="ignore")
            w.writeheader()
            w.writerows(rows)
    print(f"\n📄 {logp}  ({len(rows)} 列)\n📄 {csvp}")
    print(_summary(rows, args.lot))
    brk = [ln for ln in open(logp, encoding="utf-8")] if os.path.exists(logp) else []
    for ln in brk:
        if ln.startswith("[WVPROBE-BREAK]"):
            print("🔴 BREAK:", ln.split("] ", 1)[-1].strip())
    return rc


if __name__ == "__main__":
    sys.exit(main())
