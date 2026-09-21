# -*- coding: utf-8 -*-
r"""`W-G.9-324` 工項一：造 **`δ′`** 之補測（逐宗 `W` 軸**增量**）。

受詞（逐字·單 `§二` 工項一 `一`）：
  「理論側 `_select_pool_slot` 所餵之 `widths` 向量，於造 **`δ′`**（逐宗 `W` 軸增量）下
   重算其 `table[k*]` 之 `ΣRw_L`／`ΣRw_R` 與 `k*`，並與 `α₀`／`γ′` 二造及**實跑側**同
   （態·情境·街廓·側）之階段 `1` 負擔和對拍；並逐格出艙其飽和之判與證據力之母體。」

🔒 **`δ′` 之來源與粒度（`恆常附款 m④`／`m⑤`：每一造須以碼面之產生式逐字定之）**
   `app.py:10359` `'W_far_raw': W_conv,`（未捨入之本宗遠側 `W`）
   `app.py:10361` `'W_rw_start_raw': _rw_start,`（未捨入之鏈起點）
   `app.py:10258` `_rw_start = _W_near if (is_corner or is_chain_head) else float(W_prev)`
   `app.py:10259` `Rw = rw_increment(_rw_start, W)`
   ⇒ `δ′_i` ＝ **實跑側該宗 `Rw` 所用之二端之差**；其結構上可產出之證 ＝ **自證閘 `3`**。

🛑 **量綱（`m⑤`）**：`_select_pool_slot` 之 `widths` 逐字為「單筆宗地寬度 `w_i`」
   （`app.py:7898`），其群和 `sL = sum(w[:k])`（`:7933`）係**逐宗量之和**
   ⇒ `δ′` 取**逐宗增量**（⛔ 累積量）；其自證 ＝ **自證閘 `4`**，判別力[必破] ＝ 以 `γ′` 施同閘。
🛑 **語意（`m⑤`）**：無側街之推進側，`app.py:10202` 之條件⛔ 成立 ⇒ `:10262` 之**佔位 `0.0`**
   ⇒ 該分支之索引**⛔ 施替身**、沿 `α₀` 並**逐項具名**。

🔒 **復用（`恆常附款 k②`·⛔ 重寫第二份判準）**：`theo`／`real`／`build_vectors`／`ENV`／`CASES`／
   `NEED` 一律自 `probe_WG9320_stageb` **`import` 並呼叫**；`drive2`／`γ′` 之取法／`max|R'|` 之
   掃描式一律自 `probe_WG9323_gprime` **`import` 或逐字複刻**。
🛑 **本器⛔ 動下列四檔一字、⛔ 重生其落檔、⛔ 呼叫其 `main()`**：
   `probe_WG9320_stageb.py`／`probe_WG9323_gprime.py`／`WG9320_stageb.md`／`WG9323_gprime.md`。
🔒 **`drive3()` ＝ `probe_WG9323_gprime.drive2` 之逐字複本 ＋ 恰二處增補**
   （`pairs[...]` 多二鍵 `"S0_raw"`／`"Rw_raw"`）；其逐行差於 `main()` 內機械比對並出艙
   （**原始／正規化二數並報**），差之集合⛔ 為所令者即 `rc=5`。
🔒 **落檔之字樣紀律（`k③`）**：本檔與其落檔**⛔ 含 `W-G.9-324` 以外之任何取號字樣**；
   自檢於 `main()` 末逐類出艙（樣式**執行期組出**·⛔ 使其字面落入受掃之母體）。

🛑 **出艙即止**——⛔ 判孰為正典、⛔ 判「孰為 `Δ` 之成因」或其否定、⛔ 提修法主張、
   ⛔ 判任何阻塞項應否解除。

`rc`：`0` 全綠／`2` 自證閘或判別力破／`3` 判定集為空／`4` `ns[...]` 取不得／
      `5` `drive3()` 之逐行差不合。
🛑 `rc ≠ 0` **⛔ 等同「受詞紅」**。

用法：`PYTHONIOENCODING=utf-8 python verify/probes/probe_WG9324_dprime.py`
"""
import contextlib
import difflib
import inspect
import io
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(REPO, "verify"))
sys.path.insert(0, HERE)

import probe_WG9320_stageb as S                                     # noqa: E402
import probe_WG9323_gprime as GP                                    # noqa: E402

ENV = S.ENV
CASES = S.CASES
NEED = S.NEED
OUT = os.path.join(REPO, "verify", "out", "WG9324_dprime.md")
PREV_LOG = os.path.join(REPO, "verify", "out", "WG9323_gprime.md")
_BUF = []

# ── 常數因子之逐字（單 `§二` 工項一 `七`·**每表必載**）────────────────────────
CONST = ("🛑 **式之形在全部造中仍為常數**：理論側 `R(b + Σw) − R(b)`（telescoping）／"
         "實跑側 `Σ_宗 max(0, R(W_i) − R(W_{i−1}))`（逐宗鉗零後求和）"
         "⇒ **任何造之數⛔ 讀為殘差之全部歸因**。")


def say(s=""):
    print(s)
    _BUF.append(s)


def flush():
    try:
        with io.open(OUT, "w", encoding="utf-8", newline="\n") as f:
            f.write("\n".join(_BUF) + "\n")
    except OSError as e:                                            # noqa: BLE001
        sys.stderr.write("🔴 落檔失敗：%r\n" % (e,))
        raise


def drive3(sb, mode):
    """一（態·情境）之驅動。回 dict。`mode` ＝ None（態甲·現行預設）／'off'（態乙）。"""
    if mode is None:
        os.environ.pop(ENV, None)
    else:
        os.environ[ENV] = mode
    for m in ("app_harvest", "run_verification", "selection_pipeline",
              "stepg_pipeline", "probe_WG9269_c4_gamma"):
        sys.modules.pop(m, None)
    from app_harvest import harvest
    import run_verification as rv
    from selection_pipeline import run_corner_pk
    from stepg_pipeline import run_step_g
    import probe_WG9269_c4_gamma as G4

    ns, fake_st = harvest()
    missing = [k for k in NEED if k not in ns]
    if missing:
        say("🔴 `ns[...]` 取不得：%s ⇒ **`rc=4`**（⛔ 靜默回空）" % missing)
        flush()
        raise SystemExit(4)
    _orig_slot = ns["_select_pool_slot"]
    slots = []

    def _spy_slot(widths, left, right):
        out = _orig_slot(widths, left, right)
        try:
            f = sys._getframe(1).f_locals
        except Exception:                                   # noqa: BLE001
            raise                                           # 🛑 ⛔ 靜默吞
        adv = f.get("_adv_base")
        pairs = {}
        if isinstance(adv, dict):
            for tag in ("left_results", "right_results"):
                for entry, res in (adv.get(tag) or []):
                    if not isinstance(entry, dict) or not isinstance(res, dict):
                        continue
                    pairs[entry.get("_ov2_idx")] = {
                        "id": (entry.get("tp") or {}).get("暫編地號"),
                        "w": res.get("_宗地寬度"), "W": res.get("W"),
                        "W_raw": res.get("W_far_raw"),
                        "S0_raw": res.get("W_rw_start_raw"),
                        "Rw_raw": res.get("Rw_raw"),
                        "side": tag[:-len("_results")]}
        slots.append({"blk": f.get("blk_label"), "widths": list(widths or []),
                      "left": dict(left or {}), "right": dict(right or {}),
                      "res": out, "pairs": pairs, "adv_ok": isinstance(adv, dict)})
        return out
    ns["_select_pool_slot"] = _spy_slot

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
    g_rows, err = [], None
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            _sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot,
                             params, build_p, wins, forced, sb,
                             eff_min_build_by_blk={})
        g_rows = _sg["g_rows"]
    except RuntimeError as e:
        err = str(e).split("\n")[0][:180]
        g_rows = (getattr(e, "partial", None) or {}).get("g_rows") or []
    rows, _sk = G4.to_csv_like(g_rows)
    return {"ns": ns, "orig_slot": _orig_slot, "slots": slots, "g_rows": g_rows,
            "rows": rows, "build_p": build_p, "err": err}


# ══ `drive3()` 之逐行差（停機款 `4`·**二數並報**）══════════════════════════
def line_diff(fa, fb, old, new):
    """回 (原始差之列, 原始差數, 正規化後之差之列, 正規化後之差數)。

    🔒 **正規化之逐字**：僅把 `old` 換為 `new`——函式名之別係**命名**、⛔ 受詞之別。
    """
    a = inspect.getsource(fa).split("\n")
    b = inspect.getsource(fb).split("\n")
    raw = [x for x in difflib.unified_diff(a, b, lineterm="", n=0)
           if x[:1] in "+-" and x[:3] not in ("+++", "---")]
    bn = [x.replace(old, new) for x in b]
    norm = [x for x in difflib.unified_diff(a, bn, lineterm="", n=0)
            if x[:1] in "+-" and x[:3] not in ("+++", "---")]
    return raw, len(raw), norm, len(norm)


WANT3 = ['+                        "S0_raw": res.get("W_rw_start_raw"),',
         '+                        "Rw_raw": res.get("Rw_raw"),']


# ══ 既有落檔之 `γ′` 之抽取（自證閘 `2`）═══════════════════════════════════
def prev_gprime():
    """自 `WG9323_gprime.md` 抽 (態, 退縮, 街廓, 側) → (`γ′` 之 `ΣRw`, `k*`)。

    🛑 **逐字抽取·⛔ 重算**（單 `§二` 工項一 `三` 閘 `2`）。
    """
    out = {}
    if not os.path.exists(PREV_LOG):
        return out
    tag, side = None, None
    rx_h = re.compile(r"^### 態(.)·`([0-9.]+)` m·街廓 `([^`]+)`")
    rx_s = re.compile(r"^#### 側 `([a-z]+)`")
    rx_g = re.compile(r"^\| `γ′` \|[^|]*\|[^|]*\| `([0-9.\-]+)` \| `([^`]*)` \|")
    for ln in io.open(PREV_LOG, encoding="utf-8"):
        m = rx_h.match(ln)
        if m:
            tag = (m.group(1), float(m.group(2)), m.group(3))
            continue
        m = rx_s.match(ln)
        if m:
            side = m.group(1)
            continue
        m = rx_g.match(ln)
        if m and tag and side:
            out[(tag[0], tag[1], tag[2], side)] = (float(m.group(1)), m.group(2))
    return out


def grp_sum(w, k, side, total=None):
    """群和（`app.py:7933`／`:7934` 之式·⛔ 器內另寫）。"""
    tot = sum(w) if total is None else total
    sL = sum(w[:k])
    return sL if side == "left" else (tot - sL)


def main():                                                          # noqa: C901
    rc = 0
    say("# `W-G.9-324` 工項一／二：造 `δ′` 之補測（**唯讀·零生產碼**）")
    say()
    say("> 🛑 **出艙即止**——本檔⛔ 判孰為正典、⛔ 判「孰為 `Δ` 之成因」或其否定、⛔ 提修法主張。")
    say("> 🔒 `γ′`／`δ′` 一律為**替身·非忠實·⛔ 確值**；"
        "`α₀` 為**碼面現況·忠實**之自證造。")
    say("> 🛑 **`_宗地寬度` 軸：本波⛔ 測**（⛔ 寫為「碼面不存在」·`m④`）。")
    say()

    # ── `§零` 態之宣告 ──
    say("## `§零`　態之宣告（二值並報·以 `hash-object` 為實）")
    FOUR = ["verify/probes/probe_WG9320_stageb.py",
            "verify/probes/probe_WG9323_gprime.py",
            "verify/out/WG9320_stageb.md",
            "verify/out/WG9323_gprime.md"]
    try:
        h1 = subprocess.run(["git", "rev-parse", "HEAD:app.py"], cwd=REPO,
                            capture_output=True, check=True).stdout.decode().strip()
        h2 = subprocess.run(["git", "hash-object", "app.py"], cwd=REPO,
                            capture_output=True, check=True).stdout.decode().strip()
        fb = []
        for p in FOUR:
            a = subprocess.run(["git", "rev-parse", "HEAD:" + p], cwd=REPO,
                               capture_output=True, check=True).stdout.decode().strip()
            b = subprocess.run(["git", "hash-object", p], cwd=REPO,
                               capture_output=True, check=True).stdout.decode().strip()
            fb.append((p, a, b))
    except (OSError, subprocess.CalledProcessError) as e:            # noqa: BLE001
        say("🔴 態之宣告取不得：%r（⛔ 靜默回空）" % (e,))
        flush()
        return 4
    say()
    say("| 量 | 值 |")
    say("|---|---|")
    say("| `git rev-parse HEAD:app.py` | `%s` |" % h1)
    say("| `git hash-object app.py`（**以此為實**） | `%s` |" % h2)
    say("| 二值相符 | %s |" % ("🟢 是" if h1 == h2 else "🔴 否"))
    say()
    say("**本器⛔ 動之四檔**（停機款 `2`·`HEAD` ／ 工作區）")
    say()
    say("| 檔 | `HEAD:` | 工作區 | 相符 |")
    say("|---|---|---|---|")
    ok4 = True
    for p, a, b in fb:
        ok4 = ok4 and (a == b)
        say("| `%s` | `%s` | `%s` | %s |"
            % (p, a, b, "🟢" if a == b else "🔴 **停機款 `2`**"))
    say()

    # ── `§一` `drive3()` 之逐行差 ──
    raw, n_raw, norm, n_norm = line_diff(GP.drive2, drive3, "def drive3(", "def drive2(")
    say("## `§一`　`drive3()` 與既有 `drive2()` 之逐行差（停機款 `4`·**二數並報**）")
    say()
    say("| 量 | 值 |")
    say("|---|---|")
    say("| **原始**逐行差 | **`%d`** |" % n_raw)
    say("| **正規化後**（僅把 `def drive3(` 換為 `def drive2(`）逐行差 | **`%d`** |" % n_norm)
    say()
    say("原始差之逐列（逐字）：")
    say()
    say("```")
    for x in raw:
        say(x)
    say("```")
    say()
    say("正規化後之差之**有序串列**（逐字）：")
    say()
    say("```")
    for x in norm:
        say(x)
    say("```")
    say()
    ok_diff = (norm == WANT3)
    say("🔒 **判**：正規化後之差之有序串列**逐字等於**單 `§二` 工項一 `四` 所載之集合 ⇒ %s"
        % ("🟢" if ok_diff else "🔴 **`rc=5`**"))
    say()
    say("**`n③` 之施行**（必過／必破二實例·**本器當批實跑**）")
    say()
    say("| 實例 | 受詞 | 原始 | 正規化 | 逐字等於所令之集合 | 判 |")
    say("|---|---|---|---|---|---|")
    say("| 必過 | `drive3` 對 `drive2` | `%d` | `%d` | `%s` | %s |"
        % (n_raw, n_norm, norm == WANT3, "🟢" if norm == WANT3 else "🔴"))
    r2, n2r, m2, n2n = line_diff(S.drive, GP.drive2, "def drive2(", "def drive(")
    say("| 必破 | `drive2` 對 `probe_WG9320_stageb.drive` | `%d` | `%d` | `%s` | %s |"
        % (n2r, n2n, m2 == WANT3, "🟢 該閘⛔ 恆綠" if m2 != WANT3 else "🔴 **器紅**"))
    say()
    if not ok_diff or m2 == WANT3:
        flush()
        return 5

    # ── `§二` `max|R'|` 之當態重跑 ──
    say("## `§二`　`max|R'|` 之**當態重跑**（`恆常附款 w②`：⛔ 引他態落檔之數）")
    say()
    d0 = drive3(0.0, None)
    RW = d0["ns"]["rw_from_width"]
    RINC = d0["ns"]["rw_increment"]
    mx, at, w = 0.0, 0.0, 0.0
    while w < 18.0:
        s = (RW(w + 1e-6) - RW(w)) / 1e-6
        if s > mx:
            mx, at = s, w
        w += 0.001
    say("| 量 | **本態重跑** | 既有落檔所載（**繫其態**·⛔ 引為本態之值） | 判 |")
    say("|---|---|---|---|")
    say("| `max\\|R'\\|` | **`%.4f` %%/m**（@`W≈%.3f` m·數值掃描 `1e-3` 步長） | `17.4000` %%/m | %s |"
        % (mx, at, "🟢 相符" if abs(mx - 17.4) < 5e-5 else "🩸 相異·二值並列"))
    say()
    say("🔒 **上界式（復用 `probe_D2b5_attrib` 之驗法·⛔ 引其數）**：")
    say("`|ΣRw − [R(W_n) − R(W_0)]| ≤ (n−1)·0.005·max|R'| ＋ n·0.005`")
    say()
    say("🔒 **碼面之飽和點（逐字）**：`app.py:5725` `RW_SATURATION_WIDTH_M = 18.0`／"
        "`:5743` `if W >= RW_SATURATION_WIDTH_M:`／`:5744` `return 100.0`"
        "（本器之飽和判準**直接呼叫** `ns[\"rw_from_width\"]`·⛔ 另寫門檻）。")
    say()
    PG = prev_gprime()
    say("🔒 **自證閘 `2` 之對照來源**：`verify/out/WG9323_gprime.md`，"
        "自其**逐字抽取** `γ′` 之格 **`%d`** 個（⛔ 重算）。" % len(PG))
    say()

    # ── `§三` 逐（態·情境·街廓）──
    tot = 0
    fail1, fail2, fail3, fail4 = [], [], [], []
    ok2 = ok3 = ok4c = 0
    br2 = br3 = 0
    br4 = []
    chains = 0
    empty = []
    cls = {"無側街": 0, "移位": 0, "飽和遮蔽": 0, "單側飽和": 0, "證據格": 0}
    bite_tot = 0
    idx_tot = 0
    appl_tot = 0
    two_way = {"趨近": 0, "趨遠": 0, "相等": 0}
    zero_bite_blk = []
    for ci, (tag, mode, sb) in enumerate(CASES):
        d = d0 if (ci == 0) else drive3(sb, mode)
        say("## `§三`　態%s（`%s`）·退縮 `%.1f` m"
            % (tag, "未設·現行預設" if mode is None else ENV + "=off", sb))
        say()
        blks = []
        for r in d["g_rows"]:
            if r.get("所屬街廓") not in blks:
                blks.append(r.get("所屬街廓"))
        say("母體：`g_rows` **`%d`** 列／可達街廓（出現序）＝ `%s`／理論側之呼叫 **`%d`** 次"
            % (len(d["g_rows"]), blks, len(d["slots"])))
        if d["err"]:
            say()
            say("🩸 **管線中止**（逐字）：`%s`" % d["err"])
        say()
        by_blk = {}
        for s in d["slots"]:
            by_blk.setdefault(s["blk"], []).append(s)
        if not by_blk:
            empty.append("態%s·%.1fm" % (tag, sb))
            say("🛑 **判定集為空**（理論側⛔ 被呼叫）⇒ 本（態·情境）⛔ 出艙任何造之數。")
            say()
            continue
        for blk in sorted(by_blk, key=lambda x: str(x)):
            s = by_blk[blk][-1]
            vecs, diag = S.build_vectors(s)                # 🔒 復用·⛔ 重寫
            n = diag["n"]
            idx_tot += n
            # ── `γ′`（逐字複刻 `probe_WG9323_gprime.py:308`–`:318`）──
            gp = list(vecs["α₀"])
            for i in range(n):
                p = s["pairs"].get(i) or {}
                v = p.get("W_raw")
                if v is None:
                    continue
                gp[i] = float(v)
            vecs["γ′"] = gp
            # ── `δ′` ──
            dp = list(vecs["α₀"])
            appl, skip = [], []
            for i in range(n):
                p = s["pairs"].get(i) or {}
                sd = p.get("side")
                hs = bool((s["left"] if sd == "left" else s["right"]).get("has")) \
                    if sd in ("left", "right") else False
                wf, s0 = p.get("W_raw"), p.get("S0_raw")
                if hs and wf is not None and s0 is not None:
                    dp[i] = float(wf) - float(s0)
                    appl.append(i)
                else:
                    skip.append((i, sd, hs, wf is None, s0 is None))
            vecs["δ′"] = dp
            appl_tot += len(appl)
            bite = [i for i in appl if dp[i] != gp[i]]
            bite_tot += len(bite)
            rec = s["res"] or {}
            rec_k = rec.get("k")
            rec_t = {x.get("k"): x for x in (rec.get("table") or [])}.get(rec_k) or {}
            say("### 態%s·`%.1f` m·街廓 `%s`" % (tag, sb, blk))
            say()
            say("- 母體：宗數 **`%d`**／`k*`（實跑所錄）＝ `%s`／`_adv_base` 可得 ＝ `%s`"
                % (n, rec_k, s["adv_ok"]))
            say("- 宗序（`_ov2_idx` → 暫編地號）：`%s`"
                % [(s["pairs"].get(i) or {}).get("id") for i in range(n)])
            say("- 施 `δ′` 之索引 **`%d`**／沿 `α₀` **`%d`**"
                "（逐項 ＝ `%s`·欄序 ＝ (索引, 側, `has`, `W_far_raw` 缺, `W_rw_start_raw` 缺)）"
                % (len(appl), len(skip), skip))
            say()
            say("| `_ov2_idx` | 暫編地號 | 推進側 | `has` | `α₀` | "
                "`γ′`（`W_far_raw`） | `W_rw_start_raw` | **`δ′`** | `δ′` 施或沿 |")
            say("|---|---|---|---|---|---|---|---|---|")
            for i in range(n):
                p = s["pairs"].get(i) or {}
                sd = p.get("side")
                hs = bool((s["left"] if sd == "left" else s["right"]).get("has")) \
                    if sd in ("left", "right") else False
                s0 = p.get("S0_raw")
                say("| `%d` | `%s` | `%s` | `%s` | `%.10f` | `%.10f` | %s | `%.10f` | %s |"
                    % (i, p.get("id"), sd, hs, vecs["α₀"][i], gp[i],
                       ("`%.10f`" % float(s0)) if s0 is not None else "**缺**",
                       dp[i], "**施**" if i in appl else "沿 `α₀`"))
            say()
            # ── 自證閘 `1` ──
            L0, R0, k0 = S.theo(d["orig_slot"], vecs["α₀"], s["left"], s["right"])
            okL = (L0 is not None and rec_t.get("ΣRw_L") is not None
                   and float(rec_t["ΣRw_L"]) == L0)
            okR = (R0 is not None and rec_t.get("ΣRw_R") is not None
                   and float(rec_t["ΣRw_R"]) == R0)
            g1 = bool(okL and okR and k0 == rec_k)
            say("**自證閘 `1`**（`α₀` vs 未施替身之當次實跑所錄之 `table[k*]`·**逐位**·⛔ 容差）："
                "`k*` `%s`／`%s`·`ΣRw_L` `%s`／`%s`·`ΣRw_R` `%s`／`%s` ⇒ %s"
                % (rec_k, k0, rec_t.get("ΣRw_L"), L0, rec_t.get("ΣRw_R"), R0,
                   "🟢" if g1 else "🔴"))
            say()
            if not g1:
                fail1.append("態%s·%.1fm·%s" % (tag, sb, blk))
                say("🔴 **自證閘 `1` 破 ⇒ `rc=2` loud 拒測**·**⛔ 據 `δ′` 之任何數**。")
                say()
                continue
            # ── 自證閘 `3`（單位 ＝ 索引）──
            say("**自證閘 `3`**（單位 ＝ 索引）：每一施 `δ′` 之索引，"
                "`rw_increment(W_rw_start_raw, W_far_raw) * 100.0` 對同字典之 `Rw_raw`·**逐位相等**（`==`·⛔ 容差）")
            say()
            say("| `_ov2_idx` | `rw_increment(S0, W_far)·100` | `Rw_raw` | 判 | "
                "**必破對照**（起點誤取 `0.0`） | 其判 |")
            say("|---|---|---|---|---|---|")
            g3 = True
            for i in appl:
                p = s["pairs"].get(i) or {}
                lhs = RINC(float(p["S0_raw"]), float(p["W_raw"])) * 100.0
                rhs = p.get("Rw_raw")
                good = (rhs is not None and lhs == float(rhs))
                bad = RINC(0.0, float(p["W_raw"])) * 100.0
                bad_eq = (rhs is not None and bad == float(rhs))
                if good:
                    ok3 += 1
                else:
                    g3 = False
                    fail3.append("態%s·%.1fm·%s·idx%d" % (tag, sb, blk, i))
                if not bad_eq:
                    br3 += 1
                say("| `%d` | `%.12f` | %s | %s | `%.12f` | %s |"
                    % (i, lhs, ("`%.12f`" % float(rhs)) if rhs is not None else "**缺**",
                       "🟢" if good else "🔴", bad, "🟢 破" if not bad_eq else "⚪ 同（起點 `0.0`）"))
            say()
            if not g3:
                say("🔴 **自證閘 `3` 破 ⇒ `rc=2` loud 拒測**。")
                say()
            # ── 自證閘 `4`（量綱閘·單位 ＝ 鏈）──
            say("**自證閘 `4`（量綱閘·`m⑤` 之自證）**：每一 `has` 為 `True` 之推進側之鏈，"
                "`|Σδ′ − (max W_far_raw − min W_rw_start_raw)| ≤ (n_鏈 − 1)·0.005 + 1e-9`")
            say()
            say("| 鏈（側） | `n_鏈` | `Σδ′` | `max W_far_raw − min W_rw_start_raw` | 差 | 容許 | 判 | "
                "**必破對照** `Σγ′` | 其差 | 其判 |")
            say("|---|---|---|---|---|---|---|---|---|---|")
            for sd in ("left", "right"):
                hs = bool((s["left"] if sd == "left" else s["right"]).get("has"))
                if not hs:
                    continue
                mem = [i for i in range(n)
                       if (s["pairs"].get(i) or {}).get("side") == sd
                       and (s["pairs"].get(i) or {}).get("W_raw") is not None
                       and (s["pairs"].get(i) or {}).get("S0_raw") is not None]
                if not mem:
                    continue
                chains += 1
                nc = len(mem)
                sd_sum = sum(dp[i] for i in mem)
                span = (max(float((s["pairs"][i]).get("W_raw")) for i in mem)
                        - min(float((s["pairs"][i]).get("S0_raw")) for i in mem))
                dif = abs(sd_sum - span)
                tol = max(nc - 1, 0) * 0.005 + 1e-9
                good = dif <= tol
                gsum = sum(gp[i] for i in mem)
                gdif = abs(gsum - span)
                gbad = gdif > tol
                if good:
                    ok4c += 1
                else:
                    fail4.append("態%s·%.1fm·%s·%s" % (tag, sb, blk, sd))
                if gbad:
                    br4.append("態%s·%.1fm·%s·%s" % (tag, sb, blk, sd))
                say("| `%s` | `%d` | `%.10f` | `%.10f` | `%.3e` | `%.3e` | %s | `%.10f` | `%.3e` | %s |"
                    % (sd, nc, sd_sum, span, dif, tol, "🟢" if good else "🔴",
                       gsum, gdif,
                       "🟢 破" if gbad else ("⚪ ⛔ 破（`n_鏈 = 1`·結構上不可破）"
                                            if nc == 1 else "🔴 **⛔ 破**")))
            say()
            if len(bite) == 0:
                allz = all(float((s["pairs"].get(i) or {}).get("S0_raw") or 0.0) == 0.0
                           for i in appl)
                zero_bite_blk.append(("態%s·%.1fm·%s" % (tag, sb, blk), len(appl), allz))
            say("**判別力 `A`[必非零]**（本格）：施 `δ′` 之索引中 `δ′ ≠ γ′` 者 ＝ "
                "**`%d`**／`%d` ⇒ %s"
                % (len(bite), len(appl),
                   "🟢" if bite else "🟡 為 `0`（須其施替身之索引之起點皆 `0.0`·見結語之逐項具名）"))
            say()
            # ── 逐側 ──
            res = {}
            for nm in ("α₀", "γ′", "δ′"):
                res[nm] = S.theo(d["orig_slot"], vecs[nm], s["left"], s["right"])
            for sd, key in (("left", 0), ("right", 1)):
                hs = bool((s["left"] if sd == "left" else s["right"]).get("has"))
                rv_, used = S.real(d, blk, sd)
                b = float((s["left"] if sd == "left" else s["right"]).get("b", 0.0) or 0.0)
                say("#### 側 `%s`（`has` ＝ `%s`）" % (sd, hs))
                say()
                # 自證閘 `2`
                pv = PG.get((tag, sb, blk, sd))
                gv, gk = res["γ′"][key], res["γ′"][2]
                if pv is None:
                    g2 = False
                    fail2.append("態%s·%.1fm·%s·%s（對照格缺）" % (tag, sb, blk, sd))
                else:
                    g2 = (gv is not None and abs(pv[0] - gv) < 5e-11
                          and str(gk) == str(pv[1]))
                    if g2:
                        ok2 += 1
                    else:
                        fail2.append("態%s·%.1fm·%s·%s" % (tag, sb, blk, sd))
                a0v = res["α₀"][key]
                a0k = res["α₀"][2]
                bad2 = (pv is not None and a0v is not None
                        and abs(pv[0] - a0v) < 5e-11 and str(a0k) == str(pv[1]))
                if pv is not None and not bad2:
                    br2 += 1
                say("**自證閘 `2`**（本器之 `γ′` vs 既有落檔同格之 `γ′`·**逐字抽取**·"
                    "`|Δ| < 5e-11` ⋀ `k*` 相等）：本器 `%s`／`k* %s`；落檔 `%s`／`k* %s` ⇒ %s"
                    % ("%.10f" % gv if gv is not None else "—", gk,
                       "%.10f" % pv[0] if pv is not None else "**缺**",
                       pv[1] if pv is not None else "—",
                       "🟢" if g2 else ("🛑 對照格缺" if pv is None else "🔴")))
                say()
                say("　**必破對照**（以 `α₀` 施同閘）：`%s`／`k* %s` 對落檔之 `γ′` ⇒ %s"
                    % ("%.10f" % a0v if a0v is not None else "—", a0k,
                       "🟢 破" if (pv is not None and not bad2)
                       else ("⚪ 同（結構上不可破）" if pv is not None else "🛑 對照格缺")))
                say()
                say("| 造 | 來源·粒度 | 標 | `ΣRw_%s` | `k*` | 實跑(階段1) | `Δ(造)` |"
                    % ("L" if sd == "left" else "R"))
                say("|---|---|---|---|---|---|---|")
                dv = {}
                for nm, src in (("α₀", "`_宗地寬度`·未捨入"),
                                ("γ′", "`W_far_raw`（`app.py:10359`）·未捨入·**累積量**"),
                                ("δ′", "**`W_far_raw − W_rw_start_raw`（`:10359`−`:10361`）·逐宗增量**")):
                    v = res[nm][key]
                    mark = ("**忠實·自證造**" if nm == "α₀"
                            else "替身·非忠實·⛔ 確值")
                    if v is None:
                        say("| `%s` | %s | %s | 🔴 鍵缺 | `%s` | `%.2f` | — |"
                            % (nm, src, mark, res[nm][2], rv_))
                        continue
                    dv[nm] = v - rv_
                    say("| `%s` | %s | %s | `%.10f` | `%s` | `%.2f` | `%+.10f` |"
                        % (nm, src, mark, v, res[nm][2], rv_, dv[nm]))
                say()
                # 飽和與分類
                sat = {}
                for nm in ("α₀", "δ′"):
                    kk = res[nm][2]
                    gs = grp_sum(vecs[nm], kk if kk is not None else 0, sd)
                    sat[nm] = (RW(b + gs) == 100.0, b + gs)
                shift = (res["δ′"][2] != res["α₀"][2])
                if not hs:
                    cl = "無側街"
                elif shift:
                    cl = "移位"
                elif sat["α₀"][0] and sat["δ′"][0]:
                    cl = "飽和遮蔽"
                elif sat["α₀"][0] or sat["δ′"][0]:
                    cl = "單側飽和"
                else:
                    cl = "證據格"
                cls[cl] += 1
                say("| 量 | 值 |")
                say("|---|---|")
                say("| `b`（該側 `'b'`） | `%.10f` |" % b)
                say("| 飽和(`α₀`)：`R(b + Σw_群) == 100.0` | `%s`（`b + Σw_群` ＝ `%.10f`） |"
                    % (sat["α₀"][0], sat["α₀"][1]))
                say("| 飽和(`δ′`)：同式 | `%s`（`b + Σw_群` ＝ `%.10f`） |"
                    % (sat["δ′"][0], sat["δ′"][1]))
                say("| 移位：`k*(δ′) ≠ k*(α₀)` | `%s`（`%s` vs `%s`） |"
                    % (shift, res["δ′"][2], res["α₀"][2]))
                say("| **分類**（依序判·先中者為準） | **`%s`** |" % cl)
                say()
                nn = len(used)
                ub = (max(nn - 1, 0) * 0.005 * mx + nn * 0.005) if nn else 0.0
                say("| 量 | 值 |")
                say("|---|---|")
                say("| 本格之宗數 `n`（實跑側之受詞宗） | **`%d`** |" % nn)
                say("| 上界式之值 `(n−1)·0.005·max\\|R'\\| ＋ n·0.005` | **`%.4f` %%** |" % ub)
                for nm in ("δ′", "α₀", "γ′"):
                    say("| `Δ(%s)` | %s |"
                        % (nm, ("`%+.10f`" % dv[nm]) if nm in dv else "—"))
                for nm in ("δ′", "α₀", "γ′"):
                    say("| `\\|Δ(%s)\\| ≤ 上界`？ | `%s` |"
                        % (nm, (abs(dv[nm]) <= ub) if nm in dv else "—"))
                say()
                if cl not in ("無側街", "飽和遮蔽") and "δ′" in dv and "α₀" in dv:
                    a, bq = abs(dv["δ′"]), abs(dv["α₀"])
                    tw = "相等" if a == bq else ("趨近" if a < bq else "趨遠")
                    two_way[tw] += 1
                    say("**兩向並列（`恆常附款 i②`·⛔ 只列有利之一向）**："
                        "`|Δ(δ′)|` ＝ **`%.10f`**／`|Δ(α₀)|` ＝ **`%.10f`**／"
                        "`|Δ(γ′)|` ＝ **`%s`** ⇒ **`%s`**"
                        % (a, bq,
                           ("%.10f" % abs(dv["γ′"])) if "γ′" in dv else "—", tw))
                    say()
                say("- 實跑側之受詞宗 ＝ `%s`" % [(a, round(b2, 4)) for a, b2 in used])
                say("- %s" % CONST)
                say()
                tot += 1
            say()

    # ── `§四` 結語 ──
    say("## `§四`　結語（**⛔ 判**）")
    say()
    say("- 出艙之（態·情境·街廓·側）格數 ＝ **`%d`**" % tot)
    say("- 判定集為空之（態·情境）＝ **`%d`**（逐項 ＝ `%s`）" % (len(empty), empty or "[]"))
    say()
    say("**五類之數（互斥·依序判）**")
    say()
    say("| 類 | 數 |")
    say("|---|---|")
    for k2 in ("無側街", "移位", "飽和遮蔽", "單側飽和", "證據格"):
        say("| `%s` | **`%d`** |" % (k2, cls[k2]))
    say("| **和** | **`%d`**（須 ＝ 出艙之格數 `%d` ⇒ %s） |"
        % (sum(cls.values()), tot, "🟢" if sum(cls.values()) == tot else "🔴"))
    say()
    say("🔒 **證據力之母體 ＝ 證據格之數 ＝ `%d`**"
        "（`has` ∧ ⛔ 移位 ∧ 二造皆⛔ 飽和）。" % cls["證據格"])
    say()
    say("**兩向之三數**（母體 ＝ **非**`無側街`／`飽和遮蔽` 之格）")
    say()
    say("| 向 | 數 |")
    say("|---|---|")
    for k2 in ("趨近", "趨遠", "相等"):
        say("| `%s` | **`%d`** |" % (k2, two_way[k2]))
    say()
    say("**閘與判別力之全母體實得**")
    say()
    say("| 道 | 單位 | 過／母體 | 破之逐項 | 必破對照之實得 |")
    say("|---|---|---|---|---|")
    say("| 閘 `1` | 街廓格 | `%d`／`%d` | `%s` | （以 `γ′` 施同閘·見既有落檔） |"
        % (tot // 2 - len(fail1) if tot else 0, tot // 2, fail1 or "[]"))
    say("| 閘 `2` | 側格 | `%d`／`%d` | `%s` | 以 `α₀` 施同閘：破 **`%d`**／`%d` |"
        % (ok2, ok2 + len(fail2), fail2 or "[]", br2, len(PG)))
    say("| 閘 `3` | 索引 | `%d`／`%d` | `%s` | 起點誤取 `0.0`：破 **`%d`**／`%d` |"
        % (ok3, appl_tot, fail3 or "[]", br3, appl_tot))
    say("| 閘 `4` | 鏈 | `%d`／`%d` | `%s` | 以 `γ′` 施同閘：破 **`%d`**／`%d` |"
        % (ok4c, chains, fail4 or "[]", len(br4), chains))
    say("| 判別力 `A`[必非零] | 全母體之咬到 | `δ′ ≠ γ′` ＝ **`%d`**／施 `%d`（全索引 `%d`） | — | 以 `γ′` 對自身 ＝ `0` |"
        % (bite_tot, appl_tot, idx_tot))
    say("| 判別力 `B`[必破] | 閘 `4` 之必破 | 破鏈數 ＝ **`%d`** | — | 須 `≥ 1` |" % len(br4))
    say()
    if zero_bite_blk:
        say("🩸 **判別力 `A` 逐格為 `0` 之格（逐項具名·單所容之唯一情形 ＝ 其施替身之索引之起點皆 `0.0`）**")
        say()
        say("| 格 | 施替身之索引數 | 其起點皆 `0.0`？ | 判 |")
        say("|---|---|---|---|")
        for nm2, na, az in zero_bite_blk:
            say("| `%s` | `%d` | `%s` | %s |"
                % (nm2, na, az, "🟢 容" if az else "🔴 **`rc=2`**"))
        say()
    say()
    bad_zero = [x for x in zero_bite_blk if not x[2]]
    if fail1 or fail2 or fail3 or fail4 or bite_tot == 0 or len(br4) < 1 or bad_zero \
            or br2 < 1 or br3 < 1:
        rc = 2
    elif tot == 0:
        rc = 3
    say("- `rc` ＝ **`%d`**（`0` 全綠／`2` 自證閘或判別力破／`3` 判定集為空／"
        "`4` `ns[...]` 取不得／`5` `drive3()` 之逐行差不合）" % rc)
    say("🛑 `rc ≠ 0` **⛔ 等同「受詞紅」**。")
    say()
    say("🛑 **出艙即止**——本檔⛔ 判孰為正典、⛔ 判「孰為 `Δ` 之成因」或其否定、"
        "⛔ 提修法主張、⛔ 判任何阻塞項應否解除。")
    say()

    # ── `k③` 落檔之字樣自檢 ──
    body = "\n".join(_BUF)
    pats = [("單號", "W-G.9-" + r"(\d{1,4})"),
            ("自" + "誤號", "自" + "誤 " + r"`?(\d{1,4})"),
            ("阻塞項號", "G" + "B-" + r"(\d{1,4})"),
            ("裁定號", "V" + "R-" + r"(\d{1,4})"),
            ("裁號", "K-" + "9-" + r"(\d{1,3})")]
    say("- **落檔之字樣自檢**（`k③`·樣式執行期組出·⛔ 使其字面落入本檔）")
    say()
    say("| 類 | 相異命中 | 判 |")
    say("|---|---|---|")
    for lab, p in pats:
        st = sorted(set(re.findall(p, body)))
        allowed = (lab == "單號" and st == ["324"])
        say("| %s | `%s` | %s |"
            % (lab, st, "🟢 僅本單之號" if allowed else ("🟢 空" if not st else "🩸 非空·須具名")))
    say()
    flush()
    return rc


if __name__ == "__main__":
    sys.exit(main())
