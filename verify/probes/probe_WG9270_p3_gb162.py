# -*- coding: utf-8 -*-
"""`W-G.9-270` `p3`：`GB-162` 條件 `(a)` —— `verify/baselines` 與**當次實跑**輸出之格差**逐項歸因**
   ＋ `§四-2` 之**三戶表**（三項必載）。

🛑 **`GB-162` 三禁令（本批維持·⛔ 一字放寬）**
   ⛔ 覆寫 `verify/baselines` 任一檔／⛔ 設 `WV_BAKE` 任何值／⛔ 併線 `verify/W-G.9-269-p3a`。
   🔒 本器**只讀** `verify/baselines`（`open(..., 'r')`），**⛔ 任何寫入路徑**。

🔑 **歸因之法（單 `§四-1`）**
   `(i)` **已為現行紅項所涵蓋** ⇒ 逐格指出其對應之**紅名目**；
   `(ii)` **未涵蓋** ⇒ 逐格具名其**檔・列・欄・二端之值**。
   🔒 **對應之機械依據**：`run_verification.diff_rows` 之每一違規列皆冠 `[label]`，
      而 `label` 即該閘之**名目**；名目之 `PASS`／`FAIL` 自 `S-4` 之 log 取
      （字面 `✅ PASS`／`🔴 FAIL`·**自碼面取**·`run_verification.py:1497`·坑 `ak-1`）。

🛑 **母體之可證（坑 `aj`）**：`got_*` 係本窗 `S-4` **跑前 `rm -f verify/out/got_*`** 後所生
   （`18` 支·mtime 皆晚於起跑）——本器**⛔ 重跑**，只讀該批落檔並出艙其 `mtime`。

🔒 **判別力（單 `§四-1` 款 `3`）**：取一**已知必屬 `(i)`** 之格 ⋀ 一**人造**之格，
   證該歸因法**⛔ 恆歸一類**。

用法：`python verify/probes/probe_WG9270_p3_gb162.py <S-4 log> [倉根]`
`rc`：`0`／`3` 母體為 `0`（loud 拒測）／`5` **量測器紅**（判別力不如預期）。
"""
import csv
import io
import os
import re
import sys

S4LOG = sys.argv[1]
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(os.path.dirname(HERE))
OUT = os.path.join(REPO, "verify", "out")
BASE = os.path.join(REPO, "verify", "baselines")
sys.path.insert(0, os.path.join(REPO, "verify"))

import run_verification as rv                                       # noqa: E402

BT = chr(96)
W = 118

# 🔒 **正規化逕用生產碼之單一真相源** `rv._norm`（⛔ 另寫第二份定義·`GB-48` 族）。
#    🩸 **本器初稿曾憑記憶寫 `6dp`，而其實作為 `2dp`**（`verify/run_verification.py:307`
#       逐字「能轉 float 就比到 2dp」）⇒ 若未對照，格差之數必偏大。坑 `2`／`ak-1` 之族。
norm = rv._norm


def say(s=""):
    print(s)


def read_csv(p):
    with io.open(p, "r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def main():
    say("=" * W)
    say("【`W-G.9-270` `p3`】`GB-162` 條件 `(a)`：格差之逐項歸因 ＋ `§四-2` 三戶表")
    say("=" * W)
    say("🛑 三禁令維持：⛔ 覆寫 `verify/baselines`／⛔ 設 `WV_BAKE`／⛔ 併線 `p3a`")
    say("🔒 本器**只讀** `verify/baselines`（`open(..., 'r')`）")
    say("")

    # ── 名目之 PASS／FAIL（字面自碼面取·坑 `ak-1`）────────────────────
    with io.open(S4LOG, "r", encoding="utf-8", errors="replace") as f:
        log = f.read()
    verdict = {}
    for m in re.finditer(r"^  (✅ PASS|🔴 FAIL)  (.+)$", log, re.M):
        verdict[m.group(2).strip()] = ("PASS" if "PASS" in m.group(1) else "FAIL")
    n_p = sum(1 for v in verdict.values() if v == "PASS")
    n_f = sum(1 for v in verdict.values() if v == "FAIL")
    say("🔒 名目集合（自 `%s`·字面 `✅ PASS`／`🔴 FAIL`）＝ **%d**（PASS %d／FAIL %d）"
        % (os.path.basename(S4LOG), len(verdict), n_p, n_f))
    if not verdict:
        say("🛑 名目集合為 `0` ⇒ **loud 拒測**（⛔ 靜默綠）")
        sys.exit(3)

    # ── 違規之逐列（自 log·**⛔ 全量**·`run_verification.py:1505` 只印 12 列）──
    trunc = re.findall(r"另 (\d+) 列未顯示.*?本閘違規總計 (\d+) 列", log)
    say("🔒 log 內被**截斷**之閘 ＝ **%d** 個；其違規總計之 Σ ＝ **%d** 列"
        % (len(trunc), sum(int(b) for _a, b in trunc)))
    say("   🛑 ⇒ **逐格歸因⛔ 得自 log 取**（其只印 12 列·`run_verification.py:1505`）"
        "⇒ 本器改自 `verify/baselines` ⋀ `got_*` **直接重算格差**")
    say("")

    # ── baseline ↔ got 之配對（正面列舉·⛔ 全倉排除式）────────────────
    say("─" * W)
    say("【一】母體：`verify/baselines` ↔ `verify/out/got_*` 之配對（正面列舉）")
    say("─" * W)
    pairs = []
    for dp, _dn, fns in os.walk(BASE):
        for fn in sorted(fns):
            if not fn.endswith(".csv"):
                continue
            bp = os.path.join(dp, fn)
            gp = os.path.join(OUT, "got_" + fn)
            pairs.append((os.path.relpath(bp, REPO).replace("\\", "/"), bp,
                          os.path.relpath(gp, REPO).replace("\\", "/"), gp,
                          os.path.exists(gp)))
    say("   `verify/baselines` 之 `.csv` ＝ **%d** 支；其中有對應 `got_` 者 ＝ **%d** 支"
        % (len(pairs), sum(1 for p in pairs if p[4])))
    import time as _t
    for rb, _bp, rg, gp, ok in pairs:
        say("   %-58s ↔ %-46s %s"
            % (rb, rg, ("✅ mtime " + _t.strftime("%m-%d %H:%M:%S",
                                                 _t.localtime(os.path.getmtime(gp))))
               if ok else "🔴 got_ 不存在"))
    live = [p for p in pairs if p[4]]
    if not live:
        say("🛑 母體 `0` ⇒ **loud 拒測**")
        sys.exit(3)
    say("")

    # ── 逐格差（鍵以**全欄**定位·⛔ 猜 key_cols）─────────────────────
    say("─" * W)
    say("【二】逐格差之重算（框逐字：`_norm(base[col]) != _norm(got[col])`·比 baseline 之欄）")
    say("─" * W)
    KEY = ["暫編地號", "所屬街廓", "推進側別", "街廓", "端", "歸戶鍵Gxxx", "情境"]
    cells = []
    per_file = []
    for rb, bp, _rg, gp, _ok in live:
        base = read_csv(bp)
        got = read_csv(gp)
        if not base:
            per_file.append((rb, 0, 0, 0, "baseline 無列"))
            continue
        bh = list(base[0].keys())
        kc = [k for k in KEY if k in bh] or bh[:1]

        def keyof(r):
            return tuple(str(r.get(k, "")).strip() for k in kc)
        bby = {keyof(r): r for r in base}
        gby = {keyof(r): r for r in got}
        n_cell = n_miss = n_extra = 0
        for k in bby:
            if k not in gby:
                n_miss += 1
                cells.append((rb, k, "(缺列)", "", "", kc))
                continue
            b, g = bby[k], gby[k]
            for col in bh:
                if col not in g:
                    n_cell += 1
                    cells.append((rb, k, "(缺欄)" + col, b.get(col, ""), "", kc))
                elif norm(b[col]) != norm(g[col]):
                    n_cell += 1
                    cells.append((rb, k, col, b[col], g[col], kc))
        for k in gby:
            if k not in bby:
                n_extra += 1
                cells.append((rb, k, "(多列)", "", "", kc))
        per_file.append((rb, len(base), n_cell, n_miss + n_extra,
                         "鍵欄 ＝ %s" % kc))
    say("   %-58s %-8s %-10s %-10s %s" % ("baseline 檔", "列數", "格差", "缺／多列", "鍵欄"))
    tot_cell = tot_row = 0
    for rb, nb, nc, nr, note in per_file:
        tot_cell += nc
        tot_row += nr
        say("   %-58s %-8d %-10d %-10d %s" % (rb, nb, nc, nr, note))
    say("   " + "-" * (W - 3))
    say("   %-58s %-8s %-10d %-10d" % ("Σ", "", tot_cell, tot_row))
    say("")
    say("   🔑 **當場復算之格差 ＝ %d**（＋ 缺／多列 %d）" % (tot_cell, tot_row))
    say("   🛑 **與單所引之 `1137` 二數並報**（坑 `an`：⛔ 逕採單所引之數充本窗之當次實跑）：")
    say("      單所引 `1137` ＝ `GB-162` 所載之 **`B vs A`**（**側烤產物 ↔ baseline** 之檔對檔格差）；")
    say("      本窗 **%d** ＝ **`verify/baselines` ↔ 當次實跑 `got_*`** 之格差。")
    say("      ⇒ **二數之框相異**（前者之比較端為**側烤**·後者為**原始落檔**）"
        "——本窗⛔ 側烤（`GB-162` 禁 `WV_BAKE`）⇒ ⛔ 復現 `1137` 之框。" % tot_cell)
    say("")

    # ── 歸因 ────────────────────────────────────────────────────────
    say("─" * W)
    say("【三】逐格歸因：`(i)` 已為現行紅項所涵蓋 ／ `(ii)` 未涵蓋")
    say("─" * W)
    # baseline 檔 → 名目：以名目字串含該檔之 basename（去 `.csv`）為之
    def name_of(rb):
        stem = os.path.basename(rb)[:-4]
        hits = [n for n in verdict if stem in n]
        return hits
    cls_i, cls_ii = [], []
    byfile = {}
    for c in cells:
        byfile.setdefault(c[0], []).append(c)
    say("   %-58s %-8s %-10s %s" % ("baseline 檔", "格差", "類", "對應之名目（及其判）"))
    for rb in sorted(byfile):
        hits = name_of(rb)
        fails = [n for n in hits if verdict.get(n) == "FAIL"]
        n = len(byfile[rb])
        if fails:
            cls_i.extend(byfile[rb])
            say("   %-58s %-8d %-10s %s" % (rb, n, "(i) 涵蓋",
                                            "／".join("%s[%s]" % (x, verdict[x]) for x in fails)))
        else:
            cls_ii.extend(byfile[rb])
            say("   %-58s %-8d %-10s %s" % (rb, n, "🔴 (ii) 未涵蓋",
                                            ("／".join("%s[%s]" % (x, verdict[x]) for x in hits)
                                             if hits else "⛔ 無任何名目含該檔名")))
    say("")
    say("   🔑 **`(i)` 已涵蓋 ＝ %d 格 ／ `(ii)` 未涵蓋 ＝ %d 格**（和 ＝ %d %s）"
        % (len(cls_i), len(cls_ii), len(cls_i) + len(cls_ii),
           "✅ ＝ 總格差" if len(cls_i) + len(cls_ii) == len(cells) else "🔴"))
    if cls_ii:
        say("")
        say("   ── `(ii)` **未涵蓋者逐格具名**（檔・列・欄・二端之值·單 `§四-1` 明令）──")
        for rb, k, col, bv, gv, kc in cls_ii[:200]:
            say("      檔 %s" % rb)
            say("         列鍵(%s) ＝ %s" % ("·".join(kc), k))
            say("         欄 ＝ %s ｜ baseline ＝ %r ｜ got ＝ %r" % (col, bv, gv))
        if len(cls_ii) > 200:
            say("      …（另 %d 格未顯示·**本類總計 %d 格**）" % (len(cls_ii) - 200, len(cls_ii)))
    say("")

    # ── 判別力（款 `3`）────────────────────────────────────────────
    say("   ── 判別力（款 `3`：證該歸因法**⛔ 恆歸一類**）──")
    known_i = cls_i[0][0] if cls_i else None
    say("      造甲［已知必屬 `(i)` 之格］＝ %s ⇒ 歸 %s"
        % (known_i if known_i else "⛔ 可得",
           "`(i)`" if known_i else "⛔ 可得"))
    fake = "verify/baselines/__人造之檔__.csv"
    fake_hits = name_of(fake)
    fake_cls = "(i)" if [n for n in fake_hits if verdict.get(n) == "FAIL"] else "🔴 (ii)"
    say("      造乙［人造之檔（其名⛔ 在任何名目內·**執行期組出**）］⇒ 歸 %s（命中名目 %d 個）"
        % (fake_cls, len(fake_hits)))
    if known_i and fake_cls.endswith("(ii)"):
        say("      ⇒ **器非紅**（二造異類 ⇒ 本歸因法⛔ 恆歸一類）✅")
    else:
        say("      🛑 二造同類 ⇒ **量測器紅** ⇒ ⛔ 出艙上開歸因")
        sys.exit(5)
    say("")

    # ── `§四-2` 三戶表 ────────────────────────────────────────────
    say("─" * W)
    say("【四】`§四-2` 三戶表（**三項必載**：估算性質／時態錨／二式併陳）")
    say("─" * W)
    say("🛑 `GB-159` 之「⛔ 對外」**不受 `§四-2` 之更正影響**——下表**⛔ 對外**，僅得內部呈報。")
    say("🔒 其數**全自當次實跑**（`GB-162` 之禁⛔ 及於當次實跑·單 `§四-2` 逐字）")
    say("")
    tgt = ["G011", "G025", "G030"]
    for tag in ("0m", "3.5m"):
        p = os.path.join(OUT, "got_W-D.4_清單_退縮%s.csv" % tag)
        if not os.path.exists(p):
            say("   🛑 `%s` ⛔ 存在 ⇒ 該情境之數 **⛔ 可得**（坑 `z`：⛔ 印 `0`）"
                % os.path.basename(p))
            continue
        rr = read_csv(p)
        hdr = list(rr[0].keys()) if rr else []
        say("   ── 情境 `退縮 %s` ── 時態錨：檔 `%s`／`mtime %s`／`%d` B"
            % (tag, os.path.basename(p),
               _t.strftime("%Y-%m-%d %H:%M:%S", _t.localtime(os.path.getmtime(p))),
               os.path.getsize(p)))
        cols = [c for c in hdr if any(w in c for w in
                                      ("歸戶", "梯次", "增配", "§52-1", "§53-2",
                                       "本文式", "但書式", "估算性質"))]
        for g in tgt:
            row = next((r for r in rr if (r.get("歸戶鍵Gxxx") or "").strip() == g), None)
            if row is None:
                say("      %s ⇒ **⛔ 可得**（該情境之清單無此歸戶）" % g)
                continue
            say("      %s" % g)
            for c in cols:
                v = (row.get(c) or "").strip()
                say("         %-22s %s" % (c, v if v else "⛔ 可得"))
        say("")
    say("🛑 **二式併陳·⛔ 擇一**——其**適用式之裁屬 KL**；CC ⛔ 主張、發單側⛔ 自裁（單 `§四-2` 逐字）。")
    say("=" * W)
    sys.exit(0)


if __name__ == "__main__":
    main()
