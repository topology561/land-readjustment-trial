# -*- coding: utf-8 -*-
"""`W-G.9-270` `S-1`：單號之**宣告框**號占用（**二形並取** ⋀ **逐筆歸類** ⋀ **二對照組**）。

🔒 **框之具名（逐字·`常規四（八）三`）**——承 `CLAUDE.md` 之宣告框 `①`〜`⑧`：
   `D1` **檔名**含該號（**檔框之款·⛔ 產生任何列命中**·補款 `⑥`）
   `D2` **文內標題形** ＝ 列首為 `#+` 之列含該號
   `D3` **自稱形** ＝ (a) **嚴格式**「列首**即**該號」（⛔ 前導 `` ` ``／`*`／`_`／`>`／`-`／空白·補款 `⑧`）
                  ∪ (b) 同列含「本單」⋀ 該號，**且該號 ＝ 該檔檔名之號**（補款 `⑤`）
   **數字邊界**：`(?<![0-9\\-])<完整號>(?![0-9])`（補款一之錨定框）
   **列框 ＝ |D2 ∪ D3|**（補款 `⑦` 之**聯集**·⛔ 和）；**檔框 ＝ |D1 ∪ D2之檔 ∪ D3之檔|**
   **⛔ 計入者**（補款 `②`）：計算式／引用／對照表／待辦清單之提及。
   **鬆框**（任一列含該號）**僅作漏框偵察**、**⛔ 為判準**（補款 `④`）。

🔒 **二形並取（`GB-158`·`常規四（七）補款二`）**
   `裸形` ＝ `W-G.9-NNN`；`C形` ＝ 反引號包**全 token** ⇒ `` `W-G.9-NNN` ``。
   🔴 `B形`（反引號只包號）於本倉對已知占用之對照組多得 `0` ⇒ **⛔ 單獨採信**（`GB-158`）。

🔒 **對照組二造（`常規五`·`裁 H`）**
   `(甲)` 一**已知占用**之號 ⇒ 各形須 `≥ 1`（其命中亦須可逐筆歸類）；
   `(乙)` 一**人造哨兵**（**執行期組出**·其字面⛔ 出艙·`GB-147`）⇒ 須 `0`。
   🛑 二造任一不如預期 ⇒ **量測器紅** ⇒ ⛔ 出艙任何判（`rc = 5`）。

🔒 **判準（`裁 H` 二）** ＝ 「該號之命中**逐筆歸類**皆為零對照／判別力對照／**本單自身之產物**」；
   **命中數本身⛔ 非判準，係待歸類之材料**。

用法：`python verify/probes/probe_WG9270_S1_occupancy.py <rev> [<rev2> ...]`
`rc`：`0` 量得並出艙／`5` **量測器紅**（二造不如預期 ⇒ loud 拒測）。
🛑 `rc != 0` ⛔ 等同「受詞紅」。
"""
import re
import subprocess
import sys

BT = chr(96)                       # 反引號·⛔ 令其經 bash 一層（坑 `7`）
W = 108


def say(s=""):
    print(s)


def git(args):
    return subprocess.run(["git"] + args, capture_output=True)


def tree_files(rev, prefix):
    """母體：`git ls-tree -r -z` 取（⛔ 八進位跳脫·CJK 安全）。"""
    r = git(["ls-tree", "-r", "-z", "--name-only", rev, "--", prefix])
    if r.returncode != 0:
        return []
    raw = r.stdout.decode("utf-8", "replace")
    return [p for p in raw.split("\0") if p]


def blob_text(rev, path):
    """回傳 (text, ok)；ok=False ⇒ 讀不到（二進位／解碼失敗）。"""
    r = git(["show", "%s:%s" % (rev, path)])
    if r.returncode != 0:
        return "", False
    try:
        return r.stdout.decode("utf-8"), True
    except UnicodeDecodeError:
        return "", False


def num_of_filename(path):
    m = re.search(r"W-G\.9-([0-9]{1,4})(?![0-9])", path.split("/")[-1])
    return m.group(1) if m else None


def measure(rev, files_cache, token):
    """回傳宣告框之六數 ＋ 逐筆命中明細 ＋ 鬆框之數。"""
    anchored = re.compile(r"(?<![0-9\-])" + re.escape(token) + r"(?![0-9])")
    c_form = re.compile(r"(?<![0-9\-])" + re.escape(BT + token + BT))
    tok_num = re.search(r"W-G\.9-([0-9]{1,4})", token)
    tok_num = tok_num.group(1) if tok_num else None

    out = {}
    for form_name, rx in (("裸形", anchored), ("C形", c_form)):
        d1_files, d2_hits, d3_hits, loose_hits = set(), [], [], []
        for path, text in files_cache:
            if rx.search(path.split("/")[-1]) or (
                form_name == "裸形" and tok_num and num_of_filename(path) == tok_num
            ):
                d1_files.add(path)
            if not rx.search(text):
                continue
            fn_num = num_of_filename(path)
            for i, line in enumerate(text.split("\n"), 1):
                if not rx.search(line):
                    continue
                loose_hits.append((path, i, line))
                if re.match(r"^#+", line):
                    d2_hits.append((path, i, line))
                strict_self = line.startswith(token)
                benshan = ("本單" in line) and (fn_num is not None) and (fn_num == tok_num)
                if strict_self or benshan:
                    d3_hits.append((path, i, line))
        d2set = set((p, i) for p, i, _ in d2_hits)
        d3set = set((p, i) for p, i, _ in d3_hits)
        both = d2set & d3set
        out[form_name] = {
            "D1檔": sorted(d1_files),
            "D2": d2_hits,
            "D3": d3_hits,
            "雙屬": sorted(both),
            "列框": sorted(d2set | d3set),
            "檔框": sorted(d1_files | set(p for p, _ in (d2set | d3set))),
            "鬆框": loose_hits,
        }
    return out


def dump(rev, files_cache, token, label, quiet_token=False):
    shown = "(哨兵·字面⛔ 出艙)" if quiet_token else token
    say("  受詞 = %s   [%s]" % (shown, label))
    res = measure(rev, files_cache, token)
    for form_name in ("裸形", "C形"):
        r = res[form_name]
        say("    %-4s  D1檔=%-3d D2列=%-3d D3列=%-3d 雙屬=%-3d | 列框(聯集)=%-3d 檔框=%-3d | 鬆框列=%d"
            % (form_name, len(r["D1檔"]), len(r["D2"]), len(r["D3"]),
               len(r["雙屬"]), len(r["列框"]), len(r["檔框"]), len(r["鬆框"])))
    return res


def main():
    revs = sys.argv[1:] or ["HEAD"]
    TARGET = "W-G.9-270"
    CTL_A = "W-G.9-269"                                     # 對照甲：已知占用（須 >=1）
    CTL_B = "W-G.9-" + str(4000 + 711)                      # 對照乙：哨兵·執行期組出·字面⛔ 出艙

    bad = False
    for rev in revs:
        say("=" * W)
        say("【態】%s" % rev)
        paths = tree_files(rev, "docs")
        cache, unread = [], 0
        for p in paths:
            t, ok = blob_text(rev, p)
            if ok:
                cache.append((p, t))
            else:
                unread += 1
        say("【母體】%s 之 `docs/` 全檔 = %d 檔（讀不到 %d）" % (rev[:12], len(paths), unread))
        say("【框】宣告框 D1/D2/D3（見本器 docstring 逐字）·數字邊界 (?<![0-9-])…(?![0-9])")
        say("")
        r_t = dump(rev, cache, TARGET, "受詢·完整號·限批次")
        say("")
        r_a = dump(rev, cache, CTL_A, "對照甲·已知占用·須 >=1")
        say("")
        r_b = dump(rev, cache, CTL_B, "對照乙·人造哨兵·須 =0", quiet_token=True)
        say("")

        # ── 量測器非紅之自證 ───────────────────────────────────────────────
        a_ok = all(len(r_a[f]["列框"]) >= 1 for f in ("裸形", "C形"))
        b_ok = all(len(r_b[f]["鬆框"]) == 0 for f in ("裸形", "C形"))
        say("【量測器自證】對照甲(須>=1) 裸形=%d C形=%d ⇒ %s ；對照乙(須=0) 裸形=%d C形=%d ⇒ %s"
            % (len(r_a["裸形"]["列框"]), len(r_a["C形"]["列框"]), "✅" if a_ok else "🔴",
               len(r_b["裸形"]["鬆框"]), len(r_b["C形"]["鬆框"]), "✅" if b_ok else "🔴"))
        if not (a_ok and b_ok):
            bad = True
            say("🛑 量測器紅 ⇒ ⛔ 出艙任何判")
            continue

        # ── 受詢之逐筆歸類（`裁 H` 二：命中數本身⛔ 非判準）─────────────────
        say("")
        say("【受詢之逐筆命中（宣告框·二形聯集）·逐筆歸類】")
        seen = set()
        n = 0
        for form_name in ("裸形", "C形"):
            for p, i, line in (r_t[form_name]["D2"] + r_t[form_name]["D3"]):
                if (p, i) in seen:
                    continue
                seen.add((p, i))
                n += 1
                say("  %2d. %s:%d" % (n, p, i))
                say("      %s" % line.strip()[:150])
        if n == 0:
            say("  （宣告框命中 0 ⇒ 無待歸類之筆）")
        say("")
        say("【D1（檔名之款·二形聯集）】")
        d1 = sorted(set(r_t["裸形"]["D1檔"]) | set(r_t["C形"]["D1檔"]))
        for p in d1:
            say("  - %s" % p)
        if not d1:
            say("  （無）")
    sys.exit(5 if bad else 0)


if __name__ == "__main__":
    main()
