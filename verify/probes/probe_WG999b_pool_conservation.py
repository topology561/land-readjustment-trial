# -*- coding: utf-8 -*-
r"""`W-G.9-99 補正①`：入池數之**守恆式更正** ＋ 藍影門檻**空洞**之分層。

## 受詞

`W-G.9-99` 之 `入池合計` 係 `Σ(被踢除宗之基線 G)`，**⛔ 未扣除存活宗因重排而增長之 `ΣΔ`**
（`probe_WG999_yi_chain.py` 之 `pool += rel`）。依正典守恆式應扣之。

**正典逐字**：

- `K-6:1697`（節標 `K-6:1695` ＝「🔒 抵費地池之面積採「量」而非「算」」）：
  「池（配餘地／調配池／抵費地池）之面積 ＝ **街廓多邊形扣除各宗配地多邊形後之幾何剩餘**，」
- `K-6:2363`：「`ΣG + 調配池 = 街廓 DXF 面積` **恆成立** ⇒ 未配之地**依定義即池**、⛔ 非選擇」

**由守恆式導出**：

    池_終態 ＝ 街廓面積 − ΣG_新(終態宗)
    池_基線 ＝ 街廓面積 − ΣG_舊(全宗)
    ⇒ 池增量 ＝ ΣG_舊(全宗) − ΣG_新(終態宗)
            ＝ Σ(被踢除宗之基線 G) − Σ(存活宗之 Δ)

## 資料源（⛔ 不重跑管線）

`verify/out/probe_WG999_yi_chain_23a63d3.log` 之**已入倉 blob**（⛔ 非工作區檔）。
⇒ 本檔**只解析、不量測**；一切數皆指得回該 log 之**行號**。

⛔ **不得修改 `probe_WG999_yi_chain.py`** 或任何既有探針（常規一 `②`）。

## 解析之自證（考古：解析自己的 log 會靜默丟列）

每一表皆出艙 `母體 ／ 納入 ／ 未解析`；且**逐側**以 log 自身之
「`Δ ≠ 0` 之宗數 ＝ **N**／M」之 `M` 與解析所得之列數**對拍**。

## 重跑

    python verify/probes/probe_WG999b_pool_conservation.py

`rc` **恆 `0`**；停機以**逐字具名**表示。
log 落 `verify/out/probe_WG999b_pool_conservation_<基座短碼>.log`（檔名綁**基座**·考古節 `122`）。
"""
import hashlib
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)

OUTDIR = os.path.join(VERIFY, "out")
BASE_REF = "02964ba"
SRC_LOG = "verify/out/probe_WG999_yi_chain_23a63d3.log"
BLUE_EPS = 1e-6                      # 🔒 「門檻近零」之判準（其來源與反例見 §二）
WIDTH = 108

PROD_FILES = ["app.py", "verify/stepg_pipeline.py", "verify/selection_pipeline.py",
              "verify/run_verification.py", "verify/wd4_tier_list.py",
              "verify/wf_f0.py", "verify/wf_f1.py", "verify/wf_f2.py",
              "verify/wf_f3.py", "verify/wf_f4.py"]

SELF = ["verify/probes/probe_WG999b_pool_conservation.py",
        "verify/out/probe_WG999b_pool_conservation_%s.log" % BASE_REF,
        "docs/reports/W-G.9-99_乙之遞補鏈shim.md（【更正】段）",
        "docs/驗證裁定登記表.md（`VR-054`）"]

L, STOPS = [], []


def P(s=""):
    print(s)
    L.append(s)


def hdr(s):
    P("")
    P("=" * WIDTH)
    P(s)
    P("=" * WIDTH)


def stop(tag, text):
    STOPS.append((tag, text))
    P("  🛑 **停機 %s**：%s" % (tag, text))


def git1(a):
    return subprocess.run(["git"] + a, cwd=REPO, capture_output=True,
                          check=True).stdout.decode("utf-8").strip()


def blob_of(p, ref=BASE_REF):
    return subprocess.run(["git", "cat-file", "blob", "%s:%s" % (ref, p)],
                          cwd=REPO, capture_output=True, check=True).stdout


def prod_hashes():
    return {f: git1(["hash-object", f]) for f in PROD_FILES}


# ── log 之樣式（🔒 逐條具名·⛔ 不得只給計數）────────────────────────────────
RE_SIDE = re.compile(r"── 街廓 `([^`]+)`／側 `([^`]+)`（n=(\d+)·第 0 宗 ＝ `([^`]+)`）──")
RE_ROUND = re.compile(r"第 (\d+) 輪：候選第 1 宗 ＝ `([^`]+)`｜`G₁` ＝ ([\d.]+)｜藍影 ＝ ([\d.eE+-]+)｜")
RE_G = re.compile(r"^\s+(\S+)\s+W_prev=([-\d.]+)\s+G_舊=([-\d.]+)\s+→ G_新=([-\d.]+)\s+Δ=([+-][\d.]+)\s*$")
RE_SUM = re.compile(r"`Δ ≠ 0` 之宗數 ＝ \*\*(\d+)\*\*／(\d+)｜.*?入池合計 ＝ ([\d.]+) ㎡")
RE_KICK = re.compile(r"`([^`]+)`\((\d+\.\d+)㎡\)")


def main():                                                          # noqa: C901
    log_path = os.path.join(OUTDIR, "probe_WG999b_pool_conservation_%s.log" % BASE_REF)
    H_BEFORE = prod_hashes()

    hdr("【W-G.9-99 補正①】入池數之守恆式更正 ＋ 藍影門檻空洞之分層（⛔ 零生產碼·⛔ 不重跑管線）")
    P("  基座（log 檔名所綁）＝ **%s**" % BASE_REF)
    P("  HEAD ＝ %s" % git1(["rev-parse", "HEAD"]))
    P("  `app.py` blob ＝ %s" % git1(["rev-parse", "HEAD:app.py"]))

    # ── §零　資料源之逐位自證 ───────────────────────────────────────────────
    hdr("【§零】資料源（⛔ 不重跑管線·取**已入倉之 blob**、⛔ 非工作區檔）")
    raw = blob_of(SRC_LOG)
    lines = raw.decode("utf-8").split("\n")
    P("  來源 ＝ `%s`＠`%s`" % (SRC_LOG, BASE_REF))
    P("  逐位：**%d** 行／**%d** B／`sha256` ＝ %s"
      % (raw.count(b"\n"), len(raw), hashlib.sha256(raw).hexdigest()))
    P("  🔒 工作區同檔之 `sha256` ＝ %s ⇒ %s"
      % (hashlib.sha256(open(os.path.join(REPO, SRC_LOG), "rb").read()
                        .replace(b"\r\n", b"\n")).hexdigest()[:16] + "…",
         "（僅供對帳·本檔一律用 blob）"))

    # ── §一　解析（自證母體／未解析）─────────────────────────────────────────
    hdr("【§一】解析 log（🔒 每表出艙 `母體 ／ 納入 ／ 未解析`·考古：解析自己的 log 會靜默丟列）")
    sides, cur = [], None
    unparsed_g = 0
    for i, ln in enumerate(lines, 1):
        m = RE_SIDE.search(ln)
        if m:
            cur = {"lbl": m.group(1), "slot": m.group(2), "n": int(m.group(3)),
                   "j0": m.group(4), "line": i, "rounds": [], "grows": [],
                   "sum": None, "kicked": []}
            sides.append(cur)
            continue
        if cur is None:
            continue
        m = RE_ROUND.search(ln)
        if m:
            cur["rounds"].append({"r": int(m.group(1)), "cand": m.group(2),
                                  "g1": float(m.group(3)), "blue": float(m.group(4)),
                                  "line": i})
            continue
        m = RE_G.match(ln)
        if m:
            cur["grows"].append({"name": m.group(1), "wprev": float(m.group(2)),
                                 "g_old": float(m.group(3)), "g_new": float(m.group(4)),
                                 "delta": float(m.group(5)), "line": i})
            continue
        m = RE_SUM.search(ln)
        if m:
            cur["sum"] = {"nd": int(m.group(1)), "m": int(m.group(2)),
                          "pool_reported": float(m.group(3)), "line": i}
            cur["kicked"] = [(a, float(b)) for a, b in RE_KICK.findall(ln)]
            continue
        # 🔒 候選標記 ＝ `G_舊=`（**含等號**）。首版以 `G_舊` 為標記 ⇒ 把 8 條段標題
        #    （`` `段五` 逐宗 `G_舊 → G_新` ``·無等號）與 1 句結語誤計為「未解析」⇒ 假停機。
        #    ⇒ 改正者為**候選之定義**、⛔ 非資料。
        if "G_舊=" in ln and not RE_G.match(ln):
            unparsed_g += 1

    P("  側 母體 ＝ **%d**；輪 母體 ＝ **%d**；`段五` 列 母體 ＝ **%d**；含 `G_舊` 而**未解析**之行 ＝ **%d**"
      % (len(sides), sum(len(s["rounds"]) for s in sides),
         sum(len(s["grows"]) for s in sides), unparsed_g))
    if unparsed_g:
        stop("解析", "有 %d 行含 `G_舊` 卻未被 `RE_G` 解析 ⇒ ⛔ 不得以剩餘之自洽充作完整" % unparsed_g)

    P("")
    P("  逐側對拍（🔒 以 log **自身**之「`Δ≠0` 之宗數 ＝ N／M」之 `M` 對解析所得之列數）：")
    P("  %-4s %-8s %-5s %-7s %-9s %-9s %s" % ("街廓", "側", "n", "輪數", "解析列數", "log 之 M", "判"))
    ok_parse = True
    for s in sides:
        m = s["sum"]["m"] if s["sum"] else -1
        good = (len(s["grows"]) == m)
        ok_parse = ok_parse and good
        P("  %-4s %-8s %-5d %-7d %-9d %-9d %s"
          % (s["lbl"], s["slot"], s["n"], len(s["rounds"]), len(s["grows"]), m,
             "✅" if good else "🔴"))
    if not ok_parse:
        stop("解析", "解析列數與 log 自載之 `M` 不符 ⇒ ⛔ 不得續用本解析")
        return finish(log_path, H_BEFORE)
    # 🔒 判別力：對一條人造之「壞行」，`RE_G` 須**不**命中
    bad_line = "           628-XX(9)        W_prev=1.0000     G_舊=1.0000   → G_新=BAD   Δ=+0.000000"
    P("  🔒 解析器之判別力：對人造壞行（`G_新=BAD`）`RE_G` 命中 ＝ **%d**（須 `0`）"
      % (1 if RE_G.match(bad_line) else 0))

    # ── §二　入池之守恆式更正 ───────────────────────────────────────────────
    hdr("【§二】更正一：入池 ＝ `Σ被踢除G − ΣΔ存活`（`K-6:1697`／`:2363` 之符合性更正）")
    P("  🔒 正典逐字（本批現查·見 §五 之錨檢）：")
    P("     `K-6:1697`「池…之面積 ＝ **街廓多邊形扣除各宗配地多邊形後之幾何剩餘**，」")
    P("     `K-6:2363`「`ΣG + 調配池 = 街廓 DXF 面積` **恆成立** ⇒ 未配之地**依定義即池**、⛔ 非選擇」")
    P("  🔒 導出：`池增量 ＝ ΣG_舊(全宗) − ΣG_新(終態宗) ＝ Σ被踢除G − ΣΔ存活`")
    P("")
    P("  %-4s %-8s %-8s %-11s %-11s %-13s %-11s %s"
      % ("街廓", "側", "終態宗", "Σ被踢除G", "ΣΔ存活", "**正典池增量**", "log 所報", "差"))
    tot_kick = tot_delta = tot_corr = tot_rep = 0.0
    detail = []

    def nd_hint():
        return sum(sum(g["delta"] for g in s["grows"]) for s in sides if not s["kicked"])

    for s in sides:
        kick = sum(v for _n, v in s["kicked"])
        dsum = sum(g["delta"] for g in s["grows"])
        corr = kick - dsum
        rep = s["sum"]["pool_reported"]
        tot_kick += kick
        tot_delta += dsum
        tot_corr += corr
        tot_rep += rep
        detail.append((s, [g for g in s["grows"] if abs(g["delta"]) > 1e-9]))
        P("  %-4s %-8s %-8d %-11.4f %-11.4f %-13.4f %-11.4f %+.4f"
          % (s["lbl"], s["slot"], len(s["grows"]), kick, dsum, corr, rep, rep - corr))
    P("  %-4s %-8s %-8s %-11.4f %-11.4f %-13.4f %-11.4f %+.4f"
      % ("合計", "", "", tot_kick, tot_delta, tot_corr, tot_rep, tot_rep - tot_corr))
    corr_kicked = sum(sum(v for _n, v in s["kicked"]) - sum(g["delta"] for g in s["grows"])
                      for s in sides if s["kicked"])
    P("")
    P("  🔴 **二種射程之數（⛔ 不得混用·逐字具名）**：")
    P("     (甲) **限有遞補之側**（發單側之射程）＝ `%.4f ㎡`" % corr_kicked)
    P("          ＝ `R2|右 %.4f` ＋ `R5|右 %.4f`"
      % tuple(sum(v for _n, v in s["kicked"]) - sum(g["delta"] for g in s["grows"])
              for s in sides if s["kicked"]))
    P("     (乙) **字面套用於全 8 側** ＝ `%.4f ㎡`（含無遞補側之 `ΣΔ ＝ %.4f`）"
      % (tot_corr, nd_hint()))
    P("     🔒 log 所報 ＝ `%.4f ㎡`（＝ `Σ被踢除G`·**未扣任何 `Δ`**）" % tot_rep)
    P("     ⇒ 甲 較 log 低 `%.4f`；乙 較 log 低 `%.4f`。"
      % (tot_rep - corr_kicked, tot_rep - tot_corr))
    P("")
    P("  **每一 `Δ ≠ 0` 之逐筆（🔒 皆指得回 log 行號·⛔ 非新量測）**：")
    P("  %-4s %-8s %-16s %-11s %-11s %-11s %s"
      % ("街廓", "側", "宗", "G_舊", "G_新", "Δ", "log 行"))
    n_delta_rows = 0
    for s, rows in detail:
        for g in rows:
            n_delta_rows += 1
            P("  %-4s %-8s %-16s %-11.4f %-11.4f %+-11.4f `%s:%d`"
              % (s["lbl"], s["slot"], g["name"], g["g_old"], g["g_new"], g["delta"],
                 SRC_LOG, g["line"]))
    P("  POPULATION=%d PRINTED=%d SUPPRESSED=0  # `Δ≠0` 之宗（全列）"
      % (n_delta_rows, n_delta_rows))
    P("  🔒 **⛔ 併須具名之受詞落差**：`入調配池` 於正典 ＝ **幾何剩餘（量）**；")
    P("     本數 ＝ **守恆式導出（算）**。停機⑦ 未解前幾何剩餘**取不到**")
    P("     ⇒ 一律表述為「**遞補致之池增量（依守恆式導出·⛔ 非幾何實量）**」。")

    # ── §二-b　`ΣΔ` 之分層：有遞補側 vs 無遞補側 ─────────────────────────────
    hdr("【§二-b】🔴 `ΣΔ` 之分層——**無遞補之側亦有 `ΔΣ ≠ 0`** ⇒ 重播非 baseline-faithful")
    P("  🔒 判準：該側之 `被踢除宗` ＝ 空 ⇒ 序列**未變** ⇒ 若重播忠實，其逐宗 `Δ` **應恆 `0`**。")
    P("     ⛔ **會使本判為否之輸入**：無遞補側之 `ΣΔ ＝ 0`（則重播忠實）。")
    P("")
    P("  %-4s %-8s %-9s %-11s %-11s %s" % ("街廓", "側", "有遞補?", "Σ被踢除G", "ΣΔ", "判"))
    kd = nd_ = 0.0
    for s in sides:
        kick = sum(v for _n, v in s["kicked"])
        dsum = sum(g["delta"] for g in s["grows"])
        has = bool(s["kicked"])
        if has:
            kd += dsum
        else:
            nd_ += dsum
        P("  %-4s %-8s %-9s %-11.4f %-11.4f %s"
          % (s["lbl"], s["slot"], "✅ 有" if has else "⛔ 無", kick, dsum,
             "" if has else ("✅ 忠實" if abs(dsum) < 1e-9 else "🔴 **非忠實**")))
    P("")
    P("  有遞補側之 `ΣΔ` ＝ **%.4f**；**無遞補側之 `ΣΔ` ＝ %.4f**" % (kd, nd_))
    if abs(nd_) > 1e-9:
        stop("忠實性", "無遞補側之 `ΣΔ` ＝ %.4f ≠ 0 ⇒ 本批之重播**非 baseline-faithful** ⇒ "
                        "`ΣΔ` 一項⛔ 不得逕充作「因遞補而增長」" % nd_)

    # ── §二-c　決定性內部矛盾：同宗於兩側之 `G_新` 相異 ──────────────────────
    hdr("【§二-c】🔴 決定性佐證：**同一宗於同街廓之兩側**，`G_新` 相異（該街廓零遞補）")
    P("  🔒 若重播忠實，同一宗於同街廓之 `G_新` **與鏈方向無關**。")
    byblk = {}
    for s in sides:
        if s["kicked"]:
            continue
        byblk.setdefault(s["lbl"], []).append(s)
    P("  %-4s %-16s %-13s %-13s %-13s %-13s %s"
      % ("街廓", "宗", "側A G_新", "側A W_prev", "側B G_新", "側B W_prev", "判"))
    n_conf = n_pair = 0
    for lbl, ss in sorted(byblk.items()):
        if len(ss) != 2:
            continue
        a = {g["name"]: g for g in ss[0]["grows"]}
        b = {g["name"]: g for g in ss[1]["grows"]}
        for nm in sorted(set(a) & set(b)):
            n_pair += 1
            diff = abs(a[nm]["g_new"] - b[nm]["g_new"]) > 1e-9
            if diff:
                n_conf += 1
                P("  %-4s %-16s %-13.4f %-13.4f %-13.4f %-13.4f %s"
                  % (lbl, nm, a[nm]["g_new"], a[nm]["wprev"],
                     b[nm]["g_new"], b[nm]["wprev"], "🔴 **相異**"))
    P("  POPULATION=%d PRINTED=%d SUPPRESSED=%d  # 零遞補街廓之雙側共同宗（只印相異者）"
      % (n_pair, n_conf, n_pair - n_conf))
    P("  ⇒ 相異 ＝ **%d**／%d ⇒ %s" % (n_conf, n_pair,
        "🔴 **重播結果與鏈方向相關** ⇒ 非忠實（決定性）" if n_conf else "✅ 與鏈方向無關"))
    P("  🔒 **機制對應物**：生產碼有 `_W_prev_left` 與 `_W_prev_right` **二條**鏈"
      "（`verify/stepg_pipeline.py`），")
    P("     而本批之重播把整條 `ordered_v2` 壓成**一條**鏈 ⇒ 餵入之 `W_prev` 與捕獲值不符。")

    # ── §三　藍影門檻空洞之分層 ─────────────────────────────────────────────
    hdr("【§三】更正二：「達標」之藍影門檻分層（`< %g` ⇒ 判定**空洞**）" % BLUE_EPS)
    P("  🔒 判準 `%g` 之來源：`probe_WG992_blue.py` 檔頭逐字載「藍影之 `intersection` 於**楔形空集**時"
      % BLUE_EPS)
    P("     回傳 `~1e-14㎡` 之噪訊」⇒ 該量級為**空集之數值噪訊**、⛔ 非真門檻。")
    P("     ⛔ **會使本判為否之輸入**：藍影 ≥ %g ⇒ 判「門檻有實值」（本批之 `4` 側即是）。" % BLUE_EPS)
    P("")
    P("  %-4s %-8s %-7s %-16s %-14s %-16s %-9s %s"
      % ("街廓", "側", "終輪", "候選第 1 宗", "G₁", "藍影", "分層", "log 行"))
    hollow, solid = [], []
    for s in sides:
        last = s["rounds"][-1] if s["rounds"] else None
        if last is None:
            continue
        h = last["blue"] < BLUE_EPS
        (hollow if h else solid).append((s, last))
        P("  %-4s %-8s %-7d %-16s %-14.4f %-16.6e %-9s `%s:%d`"
          % (s["lbl"], s["slot"], last["r"], last["cand"], last["g1"], last["blue"],
             "🩸 空洞" if h else "✅ 有實值", SRC_LOG, last["line"]))
    P("  POPULATION=%d PRINTED=%d SUPPRESSED=0  # 「達標」之終輪（全列）"
      % (len(sides), len(hollow) + len(solid)))
    P("")
    P("  ⇒ **達標 `%d` 側中，門檻近零（空洞）＝ `%d` 側、有實值 ＝ `%d` 側。**"
      % (len(sides), len(hollow), len(solid)))
    P("     空洞側：%s" % "、".join("`%s|%s`" % (s["lbl"], s["slot"]) for s, _ in hollow))
    P("     🔒 空洞側之 `G₁` 雖大（%s），**但對零門檻之通過⛔ 不攜帶任何資訊**"
      % "／".join("%.2f" % r["g1"] for _s, r in hollow))
    P("     ⇒ 其收斂⛔ 不得單獨採信；**有內容之收斂 ＝ `%d` 側**。" % len(solid))
    P("  🩸 `W-G.9-99` 之上呈 ② 只具名 `R6|左` **1** 側 ⇒ 本批更正為 **%d** 側。" % len(hollow))

    return finish(log_path, H_BEFORE)


def finish(log_path, H_BEFORE):
    hdr("【§四】收工：生產檔 hash 前後對拍・`SELF` 自扣・停機逐字")
    H_AFTER = prod_hashes()
    same = [f for f in PROD_FILES if H_BEFORE.get(f) == H_AFTER.get(f)]
    P("  10 支生產檔 `git hash-object` 出艙前後**逐位相同** ＝ **%d／%d** ⇒ %s"
      % (len(same), len(PROD_FILES), "✅ 零生產碼變更" if len(same) == len(PROD_FILES) else "🔴"))
    for f in PROD_FILES:
        P("     %-34s %s %s" % (f, H_BEFORE.get(f),
                                "✅" if H_BEFORE.get(f) == H_AFTER.get(f)
                                else "🔴 → %s" % H_AFTER.get(f)))
    if len(same) != len(PROD_FILES):
        stop("①", "生產檔 hash 前後不同 ⇒ 「零生產碼」宣稱**不成立**")
    P("")
    P("  🔒 **`SELF` 自扣**：本批產物 ＝ %s" % "、".join("`%s`" % s for s in SELF))
    P("     ⇒ ⛔ 不在本檔任一母體內（母體皆為 log 之側／輪／列·⛔ 非檔案母體）。")
    P("  🔒 **⛔ 未重跑管線**：本檔之唯一資料源 ＝ `%s`＠`%s` 之 blob。" % (SRC_LOG, BASE_REF))
    P("")
    if STOPS:
        P("  🛑 **本批之停機（逐字具名·`rc` 恆 `0`）**：")
        for t, x in STOPS:
            P("     停機 %s：%s" % (t, x))
    else:
        P("  ✅ 本檔未觸任一停機條件。")
    os.makedirs(OUTDIR, exist_ok=True)
    with open(log_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(L) + "\n")
    print("")
    print("log -> %s" % os.path.relpath(log_path, REPO).replace(os.sep, "/"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
