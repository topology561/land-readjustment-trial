# -*- coding: utf-8 -*-
"""`W-G.9-167` 探針：`VR-074` 落地**前置**量測（⛔ 只讀·⛔ 零生產碼）。

產出：`M-1`（三判準 vs `_is_ghost_sliver` 之差集·逐層逐街廓）／
`M-2a`（位次變動）／`M-2b`（PK winner 是否變動·**二態實跑對拍**）／
`M-2c`（預測 diff 集合·機器可讀 JSON）／`M-2d`（`_GHOST` 於 CSV 之命中）／
`M-3`（`_PROJ_POP_DECL` 之 14 tag 現況）。

🔒 `VR-074` 態之模擬 ＝ **執行期層疊**：把 `ns["_projection_order"]` 包一層，
   於排序**之前**濾掉三判準合取為真者。⛔ 不改任何生產碼一字。
"""
import collections
import csv
import io
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
OUTDIR = os.path.join(VERIFY, "out")
BASE_REF = "6b77b4a"                      # 🔒 基座（log 檔名綁此·⛔ 不綁 HEAD）
sys.path.insert(0, VERIFY)

L = []


def say(s=""):
    print(s)
    L.append(s)


def git1(a):
    import subprocess
    return subprocess.run(["git"] + a, cwd=REPO, capture_output=True,
                          check=True).stdout.decode("utf-8").strip()


# ── `VR-074` 之三判準合取（`K-9-19 一`·⛔ 不綁名稱、⛔ 不綁 `_is_ghost_sliver`）──
def c1(tp):
    return str(tp.get("原地號", "")) == "_GHOST"


def c2(tp):
    return float(tp.get("G(㎡)", 0) or 0) == 0.0


def c3(tp):
    return float(tp.get("a 面積(㎡)", 0) or 0) == 0.0


def ghost3(tp):
    return c1(tp) and c2(tp) and c3(tp)


def ids(seq):
    return sorted(str(t.get("暫編地號", "")) for t in seq)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    say("=" * 100)
    say("【W-G.9-167】`VR-074` 落地前置量測（⛔ 只讀）")
    say("=" * 100)
    say("  HEAD = %s" % git1(["rev-parse", "HEAD"]))
    say("  app.py blob = %s" % git1(["rev-parse", "HEAD:app.py"]))
    say("  WV_K6_STEP0 = %s" % os.environ.get("WV_K6_STEP0", "<未設·倉內預設>"))
    say("")

    from app_harvest import harvest
    import run_verification as rv
    from selection_pipeline import build_ownership, build_build_parcels, run_corner_pk

    snapshot = rv.load_snapshot()
    ns, fake_st = harvest()
    PO_ORIG = ns["_projection_order"]

    # ── 量測器自檢⓪：`ns` 是否即 app 之 module globals（決定層疊之射程）──
    import app_harvest as _ah
    say("  🔒 自檢⓪　`ns` 之型別 = %s／`_projection_order` in ns = %s"
        % (type(ns).__name__, "_projection_order" in ns))
    say("      `ns is PO_ORIG.__globals__` = **%s**（True ⇒ 層疊亦及於 app 內部直呼）"
        % (ns is PO_ORIG.__globals__))

    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    param_by_tag = {}
    for setback, tag in ((0.0, "0m"), (3.5, "3.5m")):
        param_by_tag[tag] = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
    build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp, build, _sw = build_build_parcels(
        ns, fake_st, v6, list(cb_by.values()), snapshot)
    say("  ✅ 建置完成：temp_parcels = %d 宗／build_parcels = %d 宗" % (len(temp), len(build)))
    say("  🔒 `build_build_parcels` 之簽章⛔ 不含 setback ⇒ **二層之內容與情境無關**"
        "（`grep -n \"def build_build_parcels\" verify/selection_pipeline.py`）")

    # ═══════════════════════ M-1 ═══════════════════════
    say("")
    say("=" * 100)
    say("§M-1　三判準合取 vs `_is_ghost_sliver`（逐層·逐街廓）")
    say("=" * 100)
    for lname, layer in (("TEMP_LAYER（temp_parcels）", temp), ("BUILD_LAYER（build_parcels）", build)):
        b = [t for t in layer if ghost3(t)]
        c = [t for t in layer if t.get("_is_ghost_sliver")]
        sb, sc = set(ids(b)), set(ids(c))
        say("")
        say("  ── %s ──" % lname)
        say("     a  該層總列數（**對照組**·必然非零） = **%d**" % len(layer))
        say("     b  三判準合取為真 = **%d** ⇒ %s" % (len(b), ids(b)))
        say("     c  `_is_ghost_sliver` 為真 = **%d** ⇒ %s" % (len(c), ids(c)))
        say("     d  **對稱差** = %s ⇒ **%s**"
            % (sorted(sb ^ sc), "空" if not (sb ^ sc) else "*** 非空 ***"))
        n1 = sum(1 for t in layer if c1(t))
        n2 = sum(1 for t in layer if c2(t))
        n3 = sum(1 for t in layer if c3(t))
        say("     e  三判準之**單獨**命中：① 原地號=='_GHOST' = **%d**／② G(㎡)==0 = **%d**"
            "／③ a 面積(㎡)==0 = **%d**" % (n1, n2, n3))
        say("        ⇒ 合取(%d) 是否比任一單項更嚴？ vs① %s／vs② %s／vs③ %s"
            % (len(b), len(b) < n1, len(b) < n2, len(b) < n3))
        say("        🔴 ②③ 於本層之鍵**存在性**：有 `G(㎡)` 鍵者 = %d ／ 有 `a 面積(㎡)` 鍵者 = %d"
            % (sum(1 for t in layer if "G(㎡)" in t), sum(1 for t in layer if "a 面積(㎡)" in t)))
        # 逐街廓
        by = collections.OrderedDict()
        for t in layer:
            by.setdefault(t.get("所屬街廓"), []).append(t)
        for blk in sorted(by, key=lambda x: str(x)):
            rows = by[blk]
            bb = [t for t in rows if ghost3(t)]
            cc = [t for t in rows if t.get("_is_ghost_sliver")]
            if bb or cc:
                say("        街廓 %-8s a=%-4d b=%d %s c=%d %s"
                    % (blk, len(rows), len(bb), ids(bb), len(cc), ids(cc)))

    # ═══════════════════════ M-2a ═══════════════════════
    say("")
    say("=" * 100)
    say("§M-2a　位次之變動（BUILD_LAYER·逐街廓·現況 vs `VR-074` 態）")
    say("=" * 100)
    say("  ⚠️ **受詞更正**：`_rank_by_tpid` 係 **per-block**（`verify/selection_pipeline.py:339`"
        "／`app.py:19135`），⛔ **非 per-side** ⇒ 單 `§三 M-2a` 之「逐街廓逐側」於碼面無受詞，"
        "本節逐**街廓**報。")
    by_blk = collections.OrderedDict()
    for t in build:
        by_blk.setdefault(t.get("所屬街廓"), []).append(t)
    rank_cur, rank_new = {}, {}
    changed_all = []
    for blk in sorted(by_blk, key=lambda x: str(x)):
        BASE = by_blk[blk]
        fl = (cad.get("front_lines") or {}).get(blk) or {}
        p1, p2 = fl.get("p1"), fl.get("p2")
        if p1 is None or p2 is None:
            say("  ── %-8s ⛔ 無 FRONT_LINE ⇒ 跳過（**具名**·⛔ 非靜默）" % blk)
            continue
        sa = [t.get("暫編地號") for t in PO_ORIG(BASE, p1, p2)]
        sb = [t.get("暫編地號") for t in PO_ORIG([t for t in BASE if not ghost3(t)], p1, p2)]
        ra = {x: i + 1 for i, x in enumerate(sa)}
        rb = {x: i + 1 for i, x in enumerate(sb)}
        rank_cur.update({(blk, k): v for k, v in ra.items()})
        rank_new.update({(blk, k): v for k, v in rb.items()})
        ch = [(x, ra[x], rb[x]) for x in sb if ra[x] != rb[x]]
        changed_all += [(blk,) + t for t in ch]
        say("  ── 街廓 %-8s n(現況)=%2d n(VR-074)=%2d ⇒ 位次改變 **%d** 筆"
            % (blk, len(sa), len(sb), len(ch)))
        for x, a, b in ch:
            say("        %-16s 現況 rank %2d → VR-074 rank %2d（差 %+d）" % (x, a, b, b - a))
    say("")
    say("  🔴 **全區 `差 ≠ 0` 之真實宗地 = %d 筆**；差值集合 = %s"
        % (len(changed_all), sorted({t[3] - t[2] for t in changed_all})))
    say("  🔒 逐筆具名：%s" % [t[1] for t in changed_all])
    say("  🔒 **對照錨（⛔ 非判準）** `W-G.9-148R M-3`：`R1` n−r=4 ／ `R4` n−r=1（合計 5）")
    per_blk = collections.Counter(t[0] for t in changed_all)
    say("     本批逐街廓實測：%s" % dict(per_blk))

    # ═══════════════════════ M-2b／M-2c ═══════════════════════
    say("")
    say("=" * 100)
    say("§M-2b／M-2c　PK 二態實跑對拍（逐情境）")
    say("=" * 100)
    stat = {"calls": 0, "dropped": 0}

    def PO_VR074(parcels, p1, p2):
        src = list(parcels or [])
        keep = [t for t in src if not ghost3(t)]
        stat["calls"] += 1
        stat["dropped"] += len(src) - len(keep)
        return PO_ORIG(keep, p1, p2)

    predicted = {"base": BASE_REF, "scenarios": {}, "unchanged_files": [], "changed_files": [], "roles": {}}
    for setback, tag in ((0.0, "0m"), (3.5, "3.5m")):
        say("")
        say("  ════ 情境 %s ════" % tag)
        ns["_projection_order"] = PO_ORIG
        dA, sA, oA, wA, fA = run_corner_pk(
            ns, fake_st, list(cb_by.values()), cad, param_by_tag[tag],
            temp, build, setback, snapshot=snapshot)
        before = dict(stat)
        ns["_projection_order"] = PO_VR074
        dB, sB, oB, wB, fB = run_corner_pk(
            ns, fake_st, list(cb_by.values()), cad, param_by_tag[tag],
            temp, build, setback, snapshot=snapshot)
        ns["_projection_order"] = PO_ORIG
        say("     🔒 **層疊之咬到計數**（反靜默退路）：本情境呼叫 %d 次／濾掉 %d 列"
            % (stat["calls"] - before["calls"], stat["dropped"] - before["dropped"]))
        if stat["dropped"] - before["dropped"] == 0:
            say("     🛑 濾掉 0 列 ⇒ **層疊未咬到**，⛔ 結論不得出艙")

        # ── M-2b ──
        say("     ── M-2b　winner ──")
        kA = {(r.get("街廓"), r.get("端")): r for r in sA}
        kB = {(r.get("街廓"), r.get("端")): r for r in sB}
        say("        指配列數：現況 %d ／ VR-074 %d ／ 鍵集相同 = %s"
            % (len(sA), len(sB), set(kA) == set(kB)))
        wdiff = [(k, kA[k].get("選中地號", kA[k].get("候選地號")),
                  kB[k].get("選中地號", kB[k].get("候選地號")))
                 for k in sorted(set(kA) & set(kB), key=lambda x: (str(x[0]), str(x[1])))
                 if kA[k] != kB[k]]
        say("        🔴 **指配列有差異之鍵 = %d**" % len(wdiff))
        for k, a, b in wdiff:
            say("           %s：現況 %r → VR-074 %r" % (k, a, b))

        # PK 群之候選數／4dp 同分／相對序
        gA = collections.OrderedDict()
        for r in dA:
            gA.setdefault((r.get("街廓"), r.get("端")), []).append(r)
        ties_tot = 0
        for k in sorted(gA, key=lambda x: (str(x[0]), str(x[1]))):
            rows = gA[k]
            pis = [round(float(r.get("優先權指數", r.get("priority_index", 0)) or 0), 4) for r in rows]
            dup = [p for p, n in collections.Counter(pis).items() if n > 1]
            ties_tot += len(dup)
            if dup:
                say("        群 %s：候選 %d ・**4dp 同分值 %s**" % (k, len(rows), dup))
                for p in dup:
                    tied = [r.get("候選地號") for r, q in zip(rows, pis) if q == p]
                    ordA = sorted(tied, key=lambda x: rank_cur.get((k[0], x), 10 ** 9))
                    ordB = sorted(tied, key=lambda x: rank_new.get((k[0], x), 10 ** 9))
                    say("           同分組 %s ⇒ 現況序 %s ／ VR-074 序 %s ⇒ **%s**"
                        % (tied, ordA, ordB, "未翻轉" if ordA == ordB else "*** 翻轉 ***"))
        say("        群數 = %d ・ 含 4dp 同分之群 = %d" % (len(gA), ties_tot))

        # ── M-2c ──
        say("     ── M-2c　診斷列之 `原位次(投影序)` 差 ──")
        KEY = ["街廓", "端", "候選地號"]
        mA = {tuple(str(r.get(c, "")) for c in KEY): r for r in dA}
        mB = {tuple(str(r.get(c, "")) for c in KEY): r for r in dB}
        say("        診斷列數：現況 %d ／ VR-074 %d ／ 鍵集相同 = %s"
            % (len(dA), len(dB), set(mA) == set(mB)))
        colset = set()
        diffs = []
        for k in sorted(set(mA) & set(mB)):
            for col in mA[k]:
                va, vb = mA[k].get(col), mB[k].get(col)
                if va != vb:
                    colset.add(col)
                    diffs.append({"列鍵": list(k), "欄名": col, "現值": va, "預測新值": vb})
        say("        🔴 **有差之格 = %d**；涉及欄 = %s" % (len(diffs), sorted(colset)))
        for d in diffs:
            say("           %s｜%s：%r → %r" % ("·".join(d["列鍵"]), d["欄名"], d["現值"], d["預測新值"]))
        predicted["scenarios"][tag] = diffs

    say("")
    say("  🔒 層疊總計：呼叫 %d 次／濾掉 %d 列（⇒ **確有咬到**）" % (stat["calls"], stat["dropped"]))

    # ── M-2c：映射至 baseline CSV ──
    say("")
    say("=" * 100)
    say("§M-2c　映射至 baseline CSV（**窮舉**·含判為不變者）")
    say("=" * 100)
    CSVS = []
    for dp, dn, fns in os.walk(os.path.join(VERIFY, "baselines")):
        for fn in fns:
            if fn.endswith(".csv"):
                CSVS.append(os.path.join(dp, fn))
    rel = lambda p: os.path.relpath(p, REPO).replace("\\", "/")
    with_col, without_col = [], []
    for p in sorted(CSVS):
        try:
            head = io.open(p, encoding="utf-8-sig", newline="").readline()
        except Exception:
            without_col.append(rel(p))
            continue
        (with_col if "原位次(投影序)" in head else without_col).append(rel(p))
    say("  baselines 下 CSV 總數 = **%d**（對照組·必然非零）" % len(CSVS))
    say("  含 `原位次(投影序)` 欄者 = **%d**：" % len(with_col))
    for p in with_col:
        say("     %s" % p)
    say("  ⛔ 不含該欄者 = **%d**（⇒ 本批判為**不變**）" % len(without_col))

    for p in with_col:
        ap = os.path.join(REPO, p)
        tag = "3.5m" if "3.5m" in os.path.basename(p) else "0m"
        rows = list(csv.DictReader(io.open(ap, encoding="utf-8-sig", newline="")))
        dmap = {tuple(d["列鍵"]): d for d in predicted["scenarios"][tag]
                if d["欄名"] == "原位次(投影序)"}
        ch = []
        for r in rows:
            k = (str(r.get("街廓", "")), str(r.get("端", "")), str(r.get("候選地號", "")))
            if k in dmap:
                ch.append({"檔名": p, "列鍵": list(k), "欄名": "原位次(投影序)",
                           "現值": r.get("原位次(投影序)"),
                           "預測新值": str(dmap[k]["預測新值"])})
        # 🔒 角色以 run_verification 之**常數**判（⛔ 不以字串猜測）
        _dirn = os.path.dirname(ap)
        if os.path.normcase(_dirn) == os.path.normcase(rv.V3RUN):
            role = "對拍靶·全欄逐格（run_verification.py:606）"
        elif os.path.normcase(_dirn) == os.path.normcase(rv.BASELINES):
            role = "對拍靶·無串聯（run_verification.py:613·skip_cols 對本欄失效）"
        else:
            role = "凍存·⛔ 非對拍靶"
        say("  %-62s 列=%3d ⇒ 預測有差之格 = **%d**｜%s" % (p, len(rows), len(ch), role))
        predicted["roles"][p] = role
        if ch:
            for _c in ch:
                _c["角色"] = role
            predicted["changed_files"] += ch
        else:
            predicted["unchanged_files"].append(p)
    predicted["unchanged_files"] += without_col

    # ── M-2d ──
    say("")
    say("=" * 100)
    say("§M-2d　`_GHOST` 於 CSV 之命中（框 ＝ 子字串·母體具名）")
    say("=" * 100)
    for label, root in (("verify/baselines/**/*.csv", os.path.join(VERIFY, "baselines")),
                        ("verify/out/**/*.csv", os.path.join(VERIFY, "out"))):
        n_files = n_hit = 0
        hits = []
        ctrl = 0
        for dp, dn, fns in os.walk(root):
            for fn in fns:
                if not fn.endswith(".csv"):
                    continue
                n_files += 1
                try:
                    s = io.open(os.path.join(dp, fn), encoding="utf-8-sig", newline="").read()
                except Exception:
                    continue
                if "_GHOST" in s:
                    n_hit += 1
                    hits.append(rel(os.path.join(dp, fn)))
                if "街廓" in s:
                    ctrl += 1
        say("  %-28s 檔數 = %d ／ 含 `_GHOST` 之檔 = **%d** %s"
            % (label, n_files, n_hit, hits[:5]))
        say("       **對照組**（必然非零之字樣 `街廓`）＝ %d 檔" % ctrl)

    # ── M-3 ──
    say("")
    say("=" * 100)
    say("§M-3　`_PROJ_POP_DECL` 之 14 tag（⛔ 只列不寫）")
    say("=" * 100)
    DECL = ns["_PROJ_POP_DECL"]
    say("  tag 總數 = **%d**" % len(DECL))
    say("  %-26s %-18s %-14s %s" % ("tag", "kind", "source", "filter"))
    fcnt = collections.Counter()
    for k, v in DECL.items():
        fcnt[v.get("filter")] += 1
        say("  %-26s %-18s %-14s %s" % (k, v.get("kind"), v.get("source"), v.get("filter")))
    say("  filter 之相異值 = %d ⇒ %s" % (len(fcnt), dict(fcnt)))

    out = os.path.join(OUTDIR, "probe_WG9167_vr074_pre_%s.log" % BASE_REF)
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(L) + "\n")
    jp = os.path.join(OUTDIR, "WG9167_predicted_diff.json")
    with open(jp, "w", encoding="utf-8", newline="\n") as f:
        json.dump(predicted, f, ensure_ascii=False, indent=1, sort_keys=True)
    print("")
    print("log  ⇒ %s" % out)
    print("json ⇒ %s" % jp)
    return 0


if __name__ == "__main__":
    sys.exit(main())
