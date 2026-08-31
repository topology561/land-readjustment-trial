# -*- coding: utf-8 -*-
r"""**`W-G.9-190R` 次一 commit·受詞 `2`**：`[T2-DIAG]` 之**未截斷**逐街廓整列 ＋ 前後逐位對拍

## 由來（逐字）

`W-G.9-190R` 之 `probe_WG9190R_fam3.py:200` 以 `T2[blk][0][:110]` **硬截斷至 `110` 字元**後
才落檔，致倉內之**切換後** `[T2-DIAG]` **⛔ 非整列**（`R4` 整列 `235` 字元 ⇒ 截去 `125`）。
發單側 `2026-08-31` 放行裁 逐字：「`[T2-DIAG]` 未截斷版落檔【准】，同一 commit 辦。
🔒 併登 `GB`（次號 `128`）：`probe_WG9190R_fam3.py:200` 之 `[:110]` 係 `GB-115` 族第四度。」

## 本檔之作法

量法**逐字同** `probe_WG9190R_fam3.py:157-171`（`run_step_g` 逐街廓·`redirect_stdout` 擷取），
**僅移除其 `:200` 之 `[:110]` 顯示截斷**。⛔ 未改該檔一字（其為既有證據鏈）。

並就【倉】`verify/out/probe_WG9190_baseline_25857aa.log`（`S-5` 基準量·**切換前**·未截斷）
之五列做**逐位對拍**，附**判別力對照**（注入一字元須判不同）。

## 🛑 本檔之限（⛔ 不得省·`§七` 之射程限）

- `[T2-DIAG]` 係 **shim 側**（harness 走 `verify/stepg_pipeline.py` 之複本）
  ⇒ 其對 `app.py` 之族②③ 切換**結構上不敏感**；本對拍所證者 ＝
  **⛔ 無任何街廓因本批而變動**，⛔ **非**「切換有後果」之證據。殘餘風險歸 `GB-123`。
- `R5` **⛔ 無 `[T2-DIAG]`** 係**期望事實**（`②-宗 圍堵閘破[R5]`），⛔ 非量測失敗。

⛔ 不改生產碼一字。⛔ 不跑 `run_all`。⛔ 不寫死本機絕對路徑。
"""
import contextlib
import io
import os
import platform
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
sys.path.insert(0, VERIFY)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(VERIFY, "fixtures"))

OUTDIR = os.path.join(VERIFY, "out")
BASELINE = os.path.join(OUTDIR, "probe_WG9190_baseline_25857aa.log")
BLKS = ["R1", "R2", "R3", "R4", "R5", "R6"]
SB = 3.5
BAR = "=" * 122
L = []


def say(s=""):
    L.append(s)
    print(s, file=sys.stderr)


def pick(text):
    """自任意文字取 {街廓: 整列}（框 ＝ 含 `[T2-DIAG]` 之整列·自標記起）。"""
    d = {}
    for line in text.splitlines():
        if "[T2-DIAG]" not in line:
            continue
        s = line[line.index("[T2-DIAG]"):]
        m = re.match(r"\[T2-DIAG\] 街廓 (\S+?)｜", s)
        if m:
            d.setdefault(m.group(1), s)
    return d


def measure():
    from app_harvest import harvest
    import run_verification as rv
    from selection_pipeline import run_corner_pk
    from stepg_pipeline import run_step_g

    ns, fake_st = harvest()
    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp_p, build_p, _sw = rv.build_build_parcels(
        ns, fake_st, v6, list(cb_by.values()), snapshot)
    cb_all = list(cb_by.values())
    params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, SB)
    _d0, _s2, _o2, wins, forced = run_corner_pk(
        ns, fake_st, cb_all, cad, params, temp_p, build_p, SB, snapshot=snapshot)
    out = {}
    for blk in BLKS:
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            try:
                run_step_g(ns, fake_st, cb_all, cad, snapshot, params,
                           [tp for tp in build_p if tp.get("所屬街廓") == blk],
                           wins, forced, SB)
            except Exception:                                    # noqa: BLE001
                pass
        out[blk] = [x for x in buf.getvalue().splitlines() if "[T2-DIAG]" in x]
    return out


def main():                                                      # noqa: C901
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8")
        except Exception:                                        # noqa: BLE001
            pass
    os.makedirs(OUTDIR, exist_ok=True)
    name = os.environ.get("WV_OUT_NAME") or "probe_WG9190R_t2diag_full.log"
    path = os.path.join(OUTDIR, name)
    if os.path.exists(path) and os.environ.get("WV_ALLOW_OVERWRITE") != "1":
        raise RuntimeError("拒絕覆寫既有 log：" + path)

    say(BAR)
    say("【W-G.9-190R 次一 commit·受詞 2】[T2-DIAG] 未截斷整列 ＋ 切換前後逐位對拍 — ⛔ 本檔零生產碼")
    say(BAR)
    say("  環境：python %s ｜ 情境 SB = %.1f m（與 W-G.9-190R 全部量測、【倉】177R 同情境）"
        % (platform.python_version(), SB))
    say("  🔒 量法逐字同 `probe_WG9190R_fam3.py:157-171`，**僅移除其 `:200` 之 `[:110]` 截斷**")
    say("")

    T2 = measure()
    say("── 一、逐街廓 `[T2-DIAG]` **整列逐位**（⛔ 無截斷·框 ＝ 含該標記之整列） ──")
    tot = 0
    for blk in BLKS:
        n = len(T2[blk])
        tot += n
        if n == 0:
            say("  %-3s ｜ %d 列｜🔴 ⛔ 無（**期望事實**：②-宗 圍堵閘破[R5]）" % (blk, n))
        else:
            for x in T2[blk]:
                s = x[x.index("[T2-DIAG]"):]
                say("  %-3s ｜ %d 列｜%s" % (blk, n, s))
    say("  ── 總列數 = %d ／ 逐街廓 = %s" % (tot, {b: len(T2[b]) for b in BLKS}))
    say("")

    say("── 二、與【倉】`S-5` 基準量（**切換前**·未截斷）之逐位對拍 ──")
    say("  🔒 母體：%s" % os.path.relpath(BASELINE, REPO).replace("\\", "/"))
    if not os.path.exists(BASELINE):
        raise RuntimeError("🔴 基準量不存在 ⇒ ⛔ 不得以「查無」代之：" + BASELINE)
    base = pick(open(BASELINE, encoding="utf-8").read())
    now = pick("\n".join(x for v in T2.values() for x in v))
    say("  切換前 街廓集 = %s ／ 切換後 街廓集 = %s" % (sorted(base), sorted(now)))
    ok = sorted(base) == sorted(now)
    if not ok:
        say("  🔴 街廓集不同 ⇒ 逐字具名：僅前有 %s ／ 僅後有 %s"
            % (sorted(set(base) - set(now)), sorted(set(now) - set(base))))
    say("  %-4s %-10s %-10s %s" % ("街廓", "前(字元)", "後(字元)", "逐位相同"))
    for k in sorted(set(base) & set(now)):
        same = base[k] == now[k]
        ok = ok and same
        say("  %-4s %-10d %-10d %s" % (k, len(base[k]), len(now[k]), same))
        if not same:
            say("     前：%s" % base[k])
            say("     後：%s" % now[k])
    say("  🔒 五列全數逐位相同 = %s" % ok)

    inj = dict(now)
    if "R2" in inj:
        inj["R2"] = inj["R2"].replace("33.0811", "33.0812", 1)
    disc = all(base[k] == inj[k] for k in set(base) & set(inj))
    say("  🔒 判別力對照（`R2` 之 `33.0811`→`33.0812`·須 `False`）= %s %s"
        % (disc, "✅" if not disc else "🔴 恆綠"))
    say("")

    say("── 三、🛑 射程限（`§七`·⛔ 不得省） ──")
    say("  `[T2-DIAG]` 係 **shim 側**（harness 走 `verify/stepg_pipeline.py` 之複本）")
    say("  ⇒ 其對 `app.py` 之族②③ 切換**結構上不敏感**；本對拍所證者 ＝")
    say("     **⛔ 無任何街廓因本批而變動**，⛔ **非**「切換有後果」之證據。")
    say("  🔒 殘餘風險歸 `GB-123`（app 路徑 `main()` 從未被任何自動測試執行），本檔⛔ 不解除。")
    say("  🔒 `run_all` 主幹因 `GB-118` 於 `②-宗 圍堵閘破[R2]` 中止 ⇒ 其 `[T2-DIAG]` 僅涵蓋 `R1`／`R2`；")
    say("     本檔走**逐街廓 `run_step_g`** 之通道 ⇒ 涵蓋 `R1`／`R2`／`R3`／`R4`／`R6`，`R5` `0` 列。")
    say("")

    allok = ok and (not disc)
    say(BAR)
    say("🛑 總判：整列落檔 ✅ ／ 前後逐位對拍 %s ／ 判別力 %s ⇒ %s"
        % ("✅" if ok else "🛑", "✅" if not disc else "🛑",
           "✅ 全過" if allok else "🛑 **有不過項 ⇒ 停機**"))
    say(BAR)

    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(L) + "\n")
    print("\n  ✅ 已落檔：%s" % path, file=sys.stderr)
    return 0 if allok else 1


if __name__ == "__main__":
    sys.exit(main())
