# -*- coding: utf-8 -*-
"""`W-G.9-270` `p3`：`GB-162` 條件 `(a)` —— 格差之**逐項歸因** ＋ `(b)(c)` 所需之物 ＋ `§四-2` 三戶表。

🛑 **三禁令維持**：⛔ 覆寫 `verify/baselines`／⛔ 設 `WV_BAKE`／⛔ 併線 `p3a`。本器**全唯讀**。

🔑 **母體之來源** ＝ `probe_WG9270_p3_spy.py` 之產物 `verify/out/WG9270R_p3_viol.tsv`
   （`diff_rows` 之**全量**違規列·間諜法所錄）。
   🩸 **何以⛔ 自 log 取**：`run_verification.py:1497-1505` 逐字只印 `viol[:12]`。

🔑 **歸因之法（單 `§四-1`）**
   `(i)` **已為現行紅項所涵蓋**：該格所屬之 `label` 可對到一個**判為 `🔴 FAIL`** 之名目；
   `(ii)` **未涵蓋**：其 `label` 對不到任何 `FAIL` 名目（⇒ 該格之差**不會使任何閘紅**）
          ⇒ 逐格具名其**檔・列鍵・欄・二端之值**。
   🔒 **對應之機械依據**：名目所印之前 `12` 列違規逐字含 `[label]` ⇒ 以之建 `label → 名目` 之映射，
      並以「該 `label` 之全量列數 ＝ 該名目所報之總計數」為**自我驗證閘**。

🔒 **判別力（款 `3`）**：一**已知必屬 `(i)`** 之 `label` ⋀ 一**人造之 `label`**（執行期組出）
   ⇒ 二者須異類，證該歸因法**⛔ 恆歸一類**。

用法：`python <本器> <spy log> <viol tsv> [倉根]`
`rc`：`0`／`3` 母體為 `0`／`5` 量測器紅。
"""
import csv
import io
import os
import re
import sys
import time

SPYLOG = sys.argv[1]
TSV = sys.argv[2]
REPO = sys.argv[3] if len(sys.argv) > 3 else os.path.abspath(
    os.path.join(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(REPO, "verify", "out")

BT = chr(96)
W = 118


def say(s=""):
    print(s)


def main():
    say("=" * W)
    say("【`W-G.9-270` `p3`】`GB-162` 條件 `(a)` 逐項歸因 ＋ `(b)(c)` 所需之物 ＋ `§四-2` 三戶表")
    say("=" * W)
    say("🛑 三禁令維持：⛔ 覆寫 `verify/baselines`／⛔ 設 `WV_BAKE`／⛔ 併線 `p3a`（本器**全唯讀**）")
    say("")

    with io.open(SPYLOG, "r", encoding="utf-8", errors="replace") as f:
        log = f.read()

    # ── 名目之判 ＋ 其所印之前 12 列（建 label → 名目）──────────────────
    items = []          # (name, verdict, [printed viol lines], total_or_None)
    cur = None
    for line in log.split("\n"):
        m = re.match(r"^  (✅ PASS|🔴 FAIL)  (.+?)\s*$", line)
        if m:
            cur = [m.group(2).strip(), "PASS" if "PASS" in m.group(1) else "FAIL", [], None]
            items.append(cur)
            continue
        if cur is None:
            continue
        m2 = re.match(r"^        …（\*\*另 (\d+) 列未顯示\*\*·本閘違規總計 (\d+) 列）", line)
        if m2:
            cur[3] = int(m2.group(2))
            continue
        if line.startswith("        ") and line.strip():
            cur[2].append(line.strip())
    n_p = sum(1 for x in items if x[1] == "PASS")
    n_f = sum(1 for x in items if x[1] == "FAIL")
    say("🔒 名目集合（自 `%s`·字面 `✅ PASS`／`🔴 FAIL`·`run_verification.py:1497`）"
        % os.path.basename(SPYLOG))
    say("   ＝ **%d**（PASS **%d**／FAIL **%d**）" % (len(items), n_p, n_f))
    if not items:
        say("🛑 名目集合 `0` ⇒ **loud 拒測**")
        sys.exit(3)

    # ── 全量違規（間諜產物）──────────────────────────────────────────
    rows = []
    with io.open(TSV, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("#"):
                continue
            p = line.rstrip("\n").split("\t")
            if len(p) >= 4:
                rows.append((p[0], p[1], p[2], p[3]))
    say("🔒 間諜產物 `%s`：違規列 **%d**（＝ `diff_rows` 之**全量**·⛔ 截斷）"
        % (os.path.basename(TSV), len(rows)))
    if not rows:
        say("🛑 母體 `0` ⇒ **loud 拒測**（⛔ 靜默綠·坑 `al`）")
        sys.exit(3)

    bylabel = {}
    for lab, base, kc, v in rows:
        bylabel.setdefault(lab, {"base": set(), "kc": kc, "viol": []})
        bylabel[lab]["base"].add(base)
        bylabel[lab]["viol"].append(v)
    say("   其 `label` ＝ **%d** 個" % len(bylabel))
    say("")

    # ── label → 名目（自名目所印之違規列取 `[label]`）──────────────────
    say("─" * W)
    say("【一】`label` → **名目** 之映射（自名目所印之違規列取 `[label]`）＋ **自我驗證閘**")
    say("─" * W)
    lab2name, gate = {}, []
    for name, verdict, printed, total in items:
        labs = set()
        for v in printed:
            m = re.match(r"^\[([^\]]+)\]", v)
            if m:
                labs.add(m.group(1))
        for L in labs:
            lab2name.setdefault(L, set()).add(name)
        if total is not None and len(labs) == 1:
            L = list(labs)[0]
            got = len(bylabel.get(L, {}).get("viol", []))
            gate.append((name, L, total, got, total == got))
    say("   %-52s %-26s %-8s %-8s %s" % ("名目", "label", "名目報", "間諜錄", "逐位"))
    for name, L, total, got, ok in gate:
        say("   %-52s %-26s %-8d %-8d %s" % (name[:50], L[:24], total, got, "✅" if ok else "🔴"))
    n_ok = sum(1 for *_x, o in gate if o)
    say("   ⇒ 可對拍者 **%d** 項，其中逐位相同 **%d** ⇒ %s"
        % (len(gate), n_ok, "✅ 映射可信" if n_ok == len(gate) and gate else "🔴 須究"))
    say("   🛑 **⛔ 可對拍者**（名目未被截斷 ⇒ 無總計數，或其印出之 `label` 非唯一）"
        "＝ **%d** 項——其映射仍由 `[label]` 建立，惟**無計數之自證**（照實）"
        % (len(items) - len(gate)))
    say("")

    # ── 歸因 ────────────────────────────────────────────────────────
    say("─" * W)
    say("【二】逐格歸因：`(i)` 已為現行紅項所涵蓋 ／ `(ii)` 未涵蓋")
    say("─" * W)
    cls_i, cls_ii = [], []
    say("   %-26s %-8s %-10s %s" % ("label", "格數", "類", "對應之名目（及其判）"))
    for L in sorted(bylabel, key=lambda x: -len(bylabel[x]["viol"])):
        names = sorted(lab2name.get(L, []))
        fails = [n for n in names if any(i[0] == n and i[1] == "FAIL" for i in items)]
        n = len(bylabel[L]["viol"])
        if fails:
            cls_i.append((L, n))
            say("   %-26s %-8d %-10s %s" % (L[:24], n, "(i) 涵蓋",
                                            "／".join(x[:44] for x in fails)))
        else:
            cls_ii.append((L, n))
            say("   %-26s %-8d %-10s %s" % (L[:24], n, "🔴 (ii) 未涵蓋",
                                            ("／".join("%s[PASS]" % x[:40] for x in names)
                                             if names else "⛔ 無名目印出該 label")))
    n_i = sum(n for _L, n in cls_i)
    n_ii = sum(n for _L, n in cls_ii)
    say("")
    say("   🔑 **`(i)` 已涵蓋 ＝ %d 格 ／ `(ii)` 未涵蓋 ＝ %d 格**（和 ＝ %d %s）"
        % (n_i, n_ii, n_i + n_ii,
           "✅ ＝ 全量違規列數" if n_i + n_ii == len(rows) else "🔴 ≠ 全量"))
    say("   🛑 **與單所引之 `1137` 二數並報**（坑 `an`）：")
    say("      單所引 `1137` ＝ `GB-162` 所載之 **`B vs A`** ——其二端為")
    say("      **前態側烤產物**（`WV_BAKE` 所生·`11` 檔）↔ `verify/baselines`，係**檔對檔**之格差；")
    say("      本窗 **%d** ＝ `diff_rows` 於**當次實跑**所報之**全量違規列**，其二端為"
        % len(rows))
    say("      `verify/baselines` ↔ **記憶體側 `got_rows`**。")
    say("      ⇒ 🔴 **二數之框相異**（側烤 vs 原始比對·檔集亦異）——本窗⛔ 側烤"
        "（`GB-162` 禁 `WV_BAKE`）⇒ **結構上⛔ 復現 `1137` 之框**。")
    if cls_ii:
        say("")
        say("   ── `(ii)` **未涵蓋者逐格具名**（檔・列鍵・欄・二端之值·單 `§四-1` 明令）──")
        shown = 0
        for L, _n in cls_ii:
            d = bylabel[L]
            for v in d["viol"]:
                shown += 1
                if shown > 300:
                    break
                say("      [%s] 檔 ＝ %s ｜ 鍵欄 ＝ %s"
                    % (L, "／".join(sorted(d["base"])), d["kc"]))
                say("         %s" % v)
            if shown > 300:
                say("      …（另 %d 格未顯示·**本類總計 %d 格**）" % (n_ii - 300, n_ii))
                break
    else:
        say("")
        say("   🟢 `(ii)` **未涵蓋 ＝ 0 格** ⇒ **全量違規列皆已為現行紅項所涵蓋**")
    say("")

    # ── 判別力 ──────────────────────────────────────────────────────
    say("   ── 判別力（款 `3`：證該歸因法**⛔ 恆歸一類**）──")
    known = cls_i[0][0] if cls_i else None
    say("      造甲［已知必屬 `(i)` 之 `label`］＝ %s ⇒ 歸 `(i)` %s"
        % (BT + str(known) + BT if known else "⛔ 可得", "✅" if known else "🔴"))
    fake = "人造之label-" + str(7 * 11 * 13 * 17)
    fake_names = sorted(lab2name.get(fake, []))
    fake_i = [n for n in fake_names if any(i[0] == n and i[1] == "FAIL" for i in items)]
    say("      造乙［人造之 `label`（**執行期組出**·字面⛔ 出艙）］⇒ 命中名目 %d 個 ⇒ 歸 %s %s"
        % (len(fake_names), "`(i)`" if fake_i else "🔴 `(ii)`", "🔴" if fake_i else "✅"))
    if not known or fake_i:
        say("      🛑 二造同類 ⇒ **量測器紅** ⇒ ⛔ 出艙上開歸因")
        sys.exit(5)
    say("      ⇒ **器非紅**（二造異類 ⇒ 本歸因法⛔ 恆歸一類）✅")
    say("")

    # ── (c) 重烤之受詞集 ─────────────────────────────────────────────
    say("─" * W)
    say("【三】條件 `(c)` 所需之物：**重烤之受詞集**（⛔ 本批辦·只出艙其各需何物）")
    say("─" * W)
    allbase = sorted({b for _l, b, _k, _v in rows})
    say("   🔒 **重烤之受詞集 ＝ `diff_rows` 實際比較之 baseline 檔**（正面列舉·⛔ 全倉排除式）")
    say("      ＝ **%d** 支（⛔ `verify/baselines` 之 `.csv` 全集）：" % len(allbase))
    for b in allbase:
        say("      - %s" % b)
    say("")
    say("   🛑 **不可逆性之處置之候選形**（⛔ 本批擇一·候發單側）：")
    say("      `甲` 先行凍存現行 `verify/baselines` 全樹至具名之凍存目錄（倉內既有此體例："
        "`verify/baselines/PRE-S0b_S0c_幾何漏歸零_凍存/`）再覆寫；")
    say("      `乙` 側支凍存（體例 ＝ `verify/W-G.9-269-p3a`·**⛔ 併線**）；")
    say("      `丙` 側烤至 `verify/out/<具名目錄>/` 後**只對拍不覆寫**（＝ `GB-162` 之現行狀態）。")
    say("      🔒 三者之別在**凍存物之可達性**：`甲` 自主線可達／`乙` 須具名側支與 `commit`"
        "（坑 `k`／`x`）／`丙` 之產物屬 `.gitignore` 之族 ⇒ **自倉觀之無推導紀錄**（坑 `26` 款 `2`）。")
    say("")

    # ── §四-2 三戶表 ─────────────────────────────────────────────────
    say("─" * W)
    say("【四】`§四-2` 三戶表（**三項必載**：`估算性質`／時態錨／二式併陳）")
    say("─" * W)
    say("🛑 `GB-159` 之「⛔ 對外」**不受 `§四-2` 之更正影響**——下表**⛔ 對外**，僅得內部呈報。")
    say("🔒 其數**全自當次實跑**（`GB-162` 之禁⛔ 及於當次實跑·單 `§四-2` 逐字）")
    say("")
    for tag in ("0m", "3.5m"):
        p = os.path.join(OUT, "got_W-D.4_清單_退縮%s.csv" % tag)
        if not os.path.exists(p):
            say("   🛑 `%s` ⛔ 存在 ⇒ 該情境之數 **⛔ 可得**（坑 `z`：⛔ 印 `0`）"
                % os.path.basename(p))
            continue
        with io.open(p, "r", encoding="utf-8-sig", newline="") as f:
            rr = list(csv.DictReader(f))
        say("   ── 情境 `退縮 %s` ──" % tag)
        say("      🔒 **時態錨**：檔 `%s`／`mtime %s`／`%d` B（本窗當次實跑所寫）"
            % (os.path.basename(p),
               time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(os.path.getmtime(p))),
               os.path.getsize(p)))
        hdr = list(rr[0].keys()) if rr else []
        cols = [c for c in hdr if any(w in c for w in
                                      ("歸戶", "軌別", "梯次", "增配", "52-1", "53-2",
                                       "本文式", "但書式", "估算性質"))]
        for g in ("G011", "G025", "G030"):
            row = next((r for r in rr if (r.get("歸戶鍵Gxxx") or "").strip() == g), None)
            if row is None:
                say("      %s ⇒ **⛔ 可得**（該情境之清單無此歸戶）" % g)
                continue
            say("      %s" % g)
            for c in cols:
                v = (row.get(c) or "").strip()
                say("         %-24s %s" % (c, v if v else "⛔ 可得"))
        say("")
    say("🛑 **二式併陳·⛔ 擇一**——`§53-1` 本文式 ⋀ 但書式**同時出艙**；")
    say("   其**適用式之裁屬 KL**；CC ⛔ 主張、發單側⛔ 自裁（單 `§四-2` 逐字）。")
    say("=" * W)
    sys.exit(0)


if __name__ == "__main__":
    main()
