# -*- coding: utf-8 -*-
"""`W-G.9-168` `M-C` 探針：四份對拍靶之**逐格違規全集**（🛑 繞開 `12` 列顯示上限·⛔ 只讀）。

🔒 **比較式⛔ 未自寫**——直接 `import run_verification` 並呼叫其 `diff_rows`
   （`verify/run_verification.py:406`）⇒ `_norm`／`key_cols`／三階段順序／列序欄序
   **逐字同源**（單 `C-1` 之拘束）。`diff_rows` 之回傳 `viol` **未截斷**（截斷發生於
   `:1454` 之列印端）⇒ 本探針即「不截斷之通道」。
"""
import copy
import csv
import io
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
OUTDIR = os.path.join(VERIFY, "out")
BASE_REF = "a98a99f"
sys.path.insert(0, VERIFY)

L = []


def say(s=""):
    print(s)
    L.append(s)


def git1(a):
    import subprocess
    return subprocess.run(["git"] + a, cwd=REPO, capture_output=True,
                          check=True).stdout.decode("utf-8").strip()


KEY = ["街廓", "端", "候選地號"]
SKIP_V1 = {"原位次(距角序·暫行)", "G估(㎡)"}


def read_csv(p):
    with io.open(p, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    import run_verification as rv
    assert not os.environ.get("WV_BAKE"), "🛑 WV_BAKE 已設 ⇒ diff_rows 會早退、⛔ 不比對"

    say("=" * 100)
    say("【W-G.9-168 M-C】四份對拍靶之逐格違規**全集**（⛔ 不截斷）")
    say("=" * 100)
    say("  HEAD = %s" % git1(["rev-parse", "HEAD"]))
    say("  app.py blob = %s" % git1(["rev-parse", "HEAD:app.py"]))
    say("  🔒 比較式來源 ＝ `run_verification.diff_rows`（**import 複用**·⛔ 未自寫）")
    say("  🔒 `WV_BAKE` 未設 ＝ %s（設之則 `diff_rows` 早退回綠·必須為 True）"
        % (not os.environ.get("WV_BAKE")))
    say("")

    # ── 受詞：本趟 run_all 所產之 got_診斷 ──
    TARGETS = []
    for tag in ("0m", "3.5m"):
        got_p = os.path.join(OUTDIR, "got_診斷_退縮%s.csv" % tag)
        TARGETS.append((("v3·診斷%s" % tag),
                        os.path.join(rv.V3RUN, "W-D.1.2 診斷_退縮%s.csv" % tag),
                        got_p, set(), tag))
        TARGETS.append((("無串聯%s" % tag),
                        os.path.join(rv.BASELINES, "W-D.1.2 診斷_退縮%s.csv" % tag),
                        got_p, SKIP_V1, tag))
    for _, bp, gp, _, _ in TARGETS:
        for p in (bp, gp):
            if not os.path.exists(p):
                say("  🛑 受詞不存在：%s ⇒ ⛔ 結論不得出艙" % p)
                return 1

    # ── 預測集合（`167R`）──
    pred = json.load(io.open(os.path.join(OUTDIR, "WG9167_predicted_diff.json"),
                             encoding="utf-8"))
    say("  🔒 預測集合 ＝ `WG9167_predicted_diff.json`：scenarios %s"
        % {k: len(v) for k, v in pred["scenarios"].items()})

    out = {"base": BASE_REF, "gates": {}, "C4": {}}

    # ═════ C-1／C-2 ═════
    say("")
    say("=" * 100)
    say("§`C-1`／`C-2`　期初之違規全集（逐閘）＋ 外部錨")
    say("=" * 100)
    ANCHOR = {"v3·診斷0m": 68, "無串聯0m": 68, "v3·診斷3.5m": 60, "無串聯3.5m": 60}
    got_cache = {}
    for label, bp, gp, skip, tag in TARGETS:
        if gp not in got_cache:
            got_cache[gp] = read_csv(gp)
        ok, viol = rv.diff_rows(got_cache[gp], bp, KEY, label, skip_cols=skip)
        a = ANCHOR[label]
        say("  %-14s 全集 = **%d** ／ 外部錨（基座 log「本閘違規總計」）= **%d** ⇒ **%s**"
            % (label, len(viol), a, "相符" if len(viol) == a else "*** 不符 ***"))
        out["gates"][label] = {"baseline": os.path.relpath(bp, REPO).replace("\\", "/"),
                               "skip_cols": sorted(skip), "total": len(viol),
                               "anchor": a, "viol": viol}

    # ═════ C-3 ═════
    say("")
    say("=" * 100)
    say("§`C-3`　全集之前 `12` 列（供與基座 log 顯示列逐位對拍）")
    say("=" * 100)
    for label in ANCHOR:
        say("  ── %s ──" % label)
        for x in out["gates"][label]["viol"][:12]:
            say("        %s" % x)

    # ═════ C-5 判別力自檢 ═════
    say("")
    say("=" * 100)
    say("§`C-5`　判別力自檢（於**複本**上人造改一格 baseline 值）")
    say("=" * 100)
    lbl, bp, gp, skip, tag = TARGETS[0]
    base_rows = read_csv(bp)
    tam = [dict(r) for r in base_rows]
    col = "真交集(㎡)"
    old_v = tam[0][col]
    tam[0][col] = "999.99"
    import tempfile
    fd, tmp = tempfile.mkstemp(suffix=".csv")
    os.close(fd)
    with io.open(tmp, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(base_rows[0].keys()))
        w.writeheader()
        w.writerows(tam)
    ok2, viol2 = rv.diff_rows(got_cache[gp], tmp, KEY, lbl, skip_cols=skip)
    os.remove(tmp)
    n0 = out["gates"][lbl]["total"]
    key0 = tuple(str(base_rows[0].get(k, "")).strip() for k in KEY)
    hit = [v for v in viol2 if str(key0) in v and col in v]
    say("  受測閘 = %s；人造改 `%s` 之首列（%r → '999.99'）" % (lbl, col, old_v))
    say("  總數：%d → **%d**（Δ = %+d·須 `+1`）⇒ **%s**"
        % (n0, len(viol2), len(viol2) - n0, len(viol2) - n0 == 1))
    say("  該格是否出現於集合內：**%s** %s" % (bool(hit), hit[:1]))
    say("  🔒 **本探針⛔ 不會抹平什麼**：其比較式 ＝ `diff_rows` 本體，⛔ 無任何 `skip`／容差／取樣；")
    say("     人造反例（上開一格）即令總數 `+1` 且逐字出現 ⇒ 證其**⛔ 非恆綠**。")
    say("  （複本已刪除；`%s` 之原檔⛔ 未動）" % os.path.basename(bp))

    # ═════ C-4 ═════
    say("")
    say("=" * 100)
    say("§`C-4`　`169` 之期末預算（⛔ 不改任何碼·以預測集合模擬 got 側）")
    say("=" * 100)
    for label, bp, gp, skip, tag in TARGETS:
        cells = [d for d in pred["scenarios"][tag] if d["欄名"] == "原位次(投影序)"]
        dmap = {tuple(d["列鍵"]): str(d["預測新值"]) for d in cells}
        got2 = copy.deepcopy(got_cache[gp])
        applied = 0
        for r in got2:
            k = tuple(str(r.get(c, "")) for c in KEY)
            if k in dmap:
                r["原位次(投影序)"] = dmap[k]
                applied += 1
        ok3, viol3 = rv.diff_rows(got2, bp, KEY, label, skip_cols=skip)
        n0 = out["gates"][label]["total"]
        say("  ── %s ──" % label)
        say("     套用之預測格數 = **%d**（期望 `4`）⇒ %s" % (applied, applied == 4))
        say("     新總數 = **%d**（期初 %d·Δ = %+d）" % (len(viol3), n0, len(viol3) - n0))
        before12 = out["gates"][label]["viol"][:12]
        after12 = viol3[:12]
        say("     前 `12` 列是否變動 = **%s**" % (before12 != after12))
        for i, (a, b) in enumerate(zip(before12, after12), 1):
            if a != b:
                say("        第 %d 顯示列｜期初 %s" % (i, a))
                say("                    ｜期末 %s" % b)
        say("     截斷通知列：期初「另 %d 列未顯示·本閘違規總計 %d 列」"
            " ⇒ 期末「另 %d 列未顯示·本閘違規總計 %d 列」"
            % (n0 - 12, n0, len(viol3) - 12, len(viol3)))
        out["C4"][label] = {"期初總數": n0, "期末總數": len(viol3),
                            "套用格數": applied,
                            "前12列變動": before12 != after12,
                            "期初前12": before12, "期末前12": after12,
                            "期末viol": viol3}

    n_disp = sum(1 for k in out["C4"] if out["C4"][k]["前12列變動"])
    n_chg_lines = sum(sum(1 for a, b in zip(out["C4"][k]["期初前12"], out["C4"][k]["期末前12"])
                          if a != b) for k in out["C4"])
    say("")
    say("  🔴 **log 應變更列合計** = 顯示列 **%d** ＋ 截斷通知列 **%d** = **%d**"
        % (n_chg_lines, len(out["C4"]), n_chg_lines + len(out["C4"])))
    say("     （發單側預測 ＝ `6` 列：`0m` 二閘各 `1` 顯示列 ＋ 四條截斷通知列）")
    out["C4"]["_summary"] = {"顯示列變更數": n_chg_lines, "截斷通知列數": len(out["C4"]) - 0,
                             "合計": n_chg_lines + 4}

    with open(os.path.join(OUTDIR, "probe_WG9168_viol_full_%s.log" % BASE_REF),
              "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(L) + "\n")
    with open(os.path.join(OUTDIR, "WG9168_viol_full_%s.json" % BASE_REF),
              "w", encoding="utf-8", newline="\n") as f:
        json.dump(out, f, ensure_ascii=False, indent=1, sort_keys=True)
    print("")
    print("log ⇒ %s" % os.path.join(OUTDIR, "probe_WG9168_viol_full_%s.log" % BASE_REF))
    return 0


if __name__ == "__main__":
    sys.exit(main())
