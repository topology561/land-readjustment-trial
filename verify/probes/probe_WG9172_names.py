# -*- coding: utf-8 -*-
"""`W-G.9-172` `M-B-2`／`M-B-4` 探針：`temp_parcels` 鍵之流向 ＋ 八個合併名之波及面。

⛔ 只讀·⛔ 零生產碼。
`M-B-2`　現查 `temp_parcels` 之鍵，哪些出現於**被對拍之輸出**（`verify/baselines/**` 之欄集）。
`M-B-4`　全倉（⛔ 非僅 `.md`）搜八個現行合併名，逐處具名並出**三數 ＋ 母體 ＋ 態**。
"""
import csv
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
OUTDIR = os.path.join(VERIFY, "out")
sys.path.insert(0, VERIFY)
L = []
EXT = (".md", ".py", ".csv", ".log", ".json", ".txt")
NAMES = ["628-40(1)+", "628-30(3)+", "628-47(1)+", "628-29(1)+",
         "628-21(2)+", "628-45(1)+", "628(2)+", "628-23(1)+"]


def say(s=""):
    print(s)
    L.append(s)


def git1(a):
    import subprocess
    return subprocess.run(["git"] + a, cwd=REPO, capture_output=True,
                          check=True).stdout.decode("utf-8").strip()


#: 🔒 **量測器須自母體扣除自身**（`SKILL §Z-8` 補款②／`自誤 207` 同族）——
#:   本探針之原始碼與其 log 皆含八個受詞名之**字面**與對照組之字面；
#:   若不扣除，對照組（人造不存在之名）必得非 `0` ⇒ 量測器紅。
SELF = {os.path.abspath(__file__),
        os.path.join(OUTDIR, "probe_WG9172_names.log"),
        os.path.join(OUTDIR, "WG9172_names.json")}


def walk():
    for root, dirs, files in os.walk(REPO):
        dirs[:] = [d for d in dirs if d != ".git"]
        for fn in files:
            if fn.endswith(EXT):
                fp = os.path.join(root, fn)
                if os.path.abspath(fp) in SELF:
                    continue
                yield fp


def main():
    head = git1(["rev-parse", "HEAD"])
    say("=" * 100)
    say("【W-G.9-172 M-B-2／M-B-4】`temp_parcels` 鍵之流向 ＋ 八合併名之波及面")
    say("=" * 100)
    say("  母體之態（`VR-058 三`）= %s" % head)

    # ── M-B-2 ──
    import run_verification as rv
    from app_harvest import harvest
    from selection_pipeline import build_ownership, build_build_parcels
    ns, fake_st = harvest()
    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    build_ownership(ns, fake_st, rv.ANON_XLSX)
    raw = open(rv.V6DXF, "rb").read()
    temp, build, _sw = build_build_parcels(ns, fake_st, raw, list(cb_by.values()),
                                           snapshot)
    tkeys = sorted({k for tp in temp for k in tp})
    bl = os.path.join(VERIFY, "baselines")
    cols = {}
    for root, dirs, files in os.walk(bl):
        for fn in files:
            if fn.endswith(".csv"):
                p = os.path.join(root, fn)
                try:
                    with open(p, encoding="utf-8-sig", newline="") as f:
                        hdr = next(csv.reader(f))
                except Exception:                                  # noqa: BLE001
                    continue
                cols[os.path.relpath(p, REPO).replace("\\", "/")] = hdr
    allcols = sorted({c for h in cols.values() for c in h})
    say()
    say("── `M-B-2`　`temp_parcels` 之鍵（%d 個）vs `verify/baselines/**` 之欄集 ──"
        % len(tkeys))
    say("   baseline CSV = %d 檔 ／ 相異欄名 = %d" % (len(cols), len(allcols)))
    hit = [k for k in tkeys if k in allcols]
    miss = [k for k in tkeys if k not in allcols]
    say("   🔴 **流入**被對拍輸出之鍵（%d）：%s" % (len(hit), hit))
    say("   ⛔ **未流入**之鍵（%d）：%s" % (len(miss), miss))
    und = [k for k in tkeys if k.startswith("_")]
    say("   `_` 前綴之既有鍵（%d）：%s" % (len(und), und))
    say("   ⇒ `_` 前綴者流入 baseline 欄集之數 = **%d**（先例之判別力）"
        % len([k for k in und if k in allcols]))

    # ── M-B-4 ──
    say()
    say("── `M-B-4`　八個現行合併名之波及面（母體 ＝ 全倉 %s·⛔ 非僅 .md）──"
        % "/".join(EXT))
    files = list(walk())
    say("   母體檔數 = **%d**（🔒 已自母體**扣除本探針自身**之 3 檔：其原始碼／log／json）"
        % len(files))
    texts = {}
    for p in files:
        try:
            texts[p] = open(p, encoding="utf-8", errors="replace").read()
        except Exception:                                          # noqa: BLE001
            pass
    tot = {}
    for nm in NAMES:
        rx = re.compile(re.escape(nm))
        rows = occ = fl = 0
        where = {}
        for p, t in texts.items():
            c = len(rx.findall(t))
            if c:
                occ += c
                fl += 1
                r = sum(1 for ln in t.splitlines() if rx.search(ln))
                rows += r
                where[os.path.relpath(p, REPO).replace("\\", "/")] = (r, c)
        tot[nm] = {"rows": rows, "occ": occ, "files": fl, "where": where}
        say("   `%s`　命中列數 **%d** ／ 出現次數 **%d** ／ 檔數 **%d**"
            % (nm, rows, occ, fl))
        for k in sorted(where):
            say("        %-62s 列 %d ／ 次 %d" % (k[-62:], where[k][0], where[k][1]))
    # 判別力對照
    neg = re.compile(re.escape("628-99(9)+"))
    say("   🔒 對照組（人造不存在之名 `628-99(9)+`）⇒ 出現次數 = **%d**（須 0）"
        % sum(len(neg.findall(t)) for t in texts.values()))
    pos = re.compile(re.escape("628-30(3)"))
    say("   🔒 對照組（已知非 0 之 `628-30(3)`·⛔ 不含 `+`）⇒ 出現次數 = **%d**（須 > 0）"
        % sum(len(pos.findall(t)) for t in texts.values()))

    p = os.path.join(OUTDIR, "WG9172_names.json")
    with open(p, "w", encoding="utf-8", newline="") as f:
        json.dump({"head": head, "temp_keys": tkeys, "baseline_cols": allcols,
                   "hit": hit, "names": {k: {kk: vv for kk, vv in v.items()
                                             if kk != "where"} for k, v in tot.items()},
                   "where": {k: v["where"] for k, v in tot.items()}},
                  f, ensure_ascii=False, indent=1)
    say()
    say("  證據檔：verify/out/%s" % os.path.basename(p))
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    rc = main()
    with open(os.path.join(OUTDIR, "probe_WG9172_names.log"),
              "w", encoding="utf-8", newline="") as f:
        f.write("\n".join(L) + "\n")
    sys.exit(rc)
