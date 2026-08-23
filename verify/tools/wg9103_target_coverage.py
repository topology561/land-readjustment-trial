# -*- coding: utf-8 -*-
r"""`W-G.9-101`　**涵蓋閘**：純追加稽核器之受詞母體自證（`VR-059 二`）。

## 判準（逐字）

    本批變更之 M(.md) 受詞　⊆　TARGETS 涵蓋　∪　具名排除集

🔒 **受詞 ＝ 本批**（`base` vs **工作區**·同 `wg942_append_audit` 之語意），
⛔ **非歷史**（`VR-059 四`：既往 commit 之缺口只入登記、⛔ 不追溯為紅）。

## 🔒 單一真相源

`TARGETS` **自同目錄之 `wg942_append_audit.py` 動態載入**（`importlib`），
⛔ **不得複製一份清單**——否則二清單漂移時本閘反成偽綠。

## 🔒 `core.quotepath`

一切 `git` 呼叫**明綁 `-c core.quotepath=false`**（`VR-059 三`）。
git 預設 `quotepath=true` 會把非 ASCII 路徑作 C-style 轉義並加引號 ⇒
以 `endswith(".md")` 過濾者，**中文檔名一律落空** ⇒ 母體歸零而閘仍綠。
`SELFTEST-2` 即**性質直檢**該框已生效（⛔ 不綁版本字串·家法 `4`）。

## 🔒 判別力自檢（⛔ 不得省）

`SELFTEST-1` 注入合成路徑 ⇒ 須判為**未涵蓋**；否則本閘無鑑別力、⛔ 不得計為證據。

## ⛔ 本批不掛 `run_all`

掛載涉 `run_all` 之 `rc` 語意與期望 FAIL 名單（`GB-52`／`GB-61`）之耦合，
須同批裁決（`GB-88 五`）⇒ 指定為下一單之受詞。

## 用法

    python verify/tools/wg9103_target_coverage.py [base]

`rc` ＝ `0`（全數受涵蓋）／`1`（有未涵蓋項）。
"""
import importlib.util
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)

AUDIT_FILE = os.path.join(HERE, "wg942_append_audit.py")
SYNTHETIC = "docs/reports/__WG9103_SYNTHETIC_UNCOVERED__.md"

# 🔒 **具名排除集**（`VR-059 二`：⛔ 不得以「其餘沿用」「已在上列」一句帶過）。
EXCLUDE = [
    ("verify/",
     "碼與 log：本器受詞係『純追加之受詞』，而 `verify/` 下之碼係**就地改**的"
     "（`W-G.9-70` 所立之判準）"),
]


# 🔒 `ARGV_LOG` ＝ **實際執行之 argv** 之記錄（`VR-062 一`·載體級直檢）。
#   ⛔ 記的是 `subprocess.run` 真正收到的那一串，⛔ 非「打算執行什麼」。
ARGV_LOG = []


def git(args, quotepath=False):
    pre = ["git", "-C", REPO, "-c",
           "core.quotepath=%s" % ("true" if quotepath else "false")]
    ARGV_LOG.append(pre + args)
    return subprocess.run(pre + args, stdout=subprocess.PIPE,
                          check=True).stdout.decode("utf-8")


def git_z(args):
    """🔒 `-z`（NUL 分隔）之輸出**⛔ 不受 `core.quotepath` 支配**（本器於 `z_imm` 自證）。
    ⇒ 供「母體是否含非 ASCII 檔名」之**獨立**判定（`VR-062 二`）。"""
    out = subprocess.run(["git", "-C", REPO] + args,
                         stdout=subprocess.PIPE, check=True).stdout
    return [x.decode("utf-8") for x in out.split(b"\x00") if x]


def load_targets():
    """🔒 動態載入同目錄之 `wg942_append_audit.TARGETS`（單一真相源·⛔ 不複製清單）。"""
    spec = importlib.util.spec_from_file_location("_wg942_audit_src", AUDIT_FILE)
    if spec is None or spec.loader is None:
        raise RuntimeError("🔴 無法載入 `%s` ⇒ ⛔ 禁靜默兜底"
                           % os.path.relpath(AUDIT_FILE, REPO).replace(os.sep, "/"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    if not getattr(mod, "TARGETS", None):
        raise RuntimeError("🔴 `TARGETS` 為空或不存在 ⇒ ⛔ 禁靜默兜底")
    return mod.TARGETS


def subjects(base, quotepath=False):
    """本批之受詞 ＝ `base` vs **工作區** 之狀態 `M` 且尾綴 `.md` 者。"""
    out = git(["diff", "--no-renames", "--diff-filter=M", "--name-status", base],
              quotepath=quotepath)
    got = []
    for line in out.splitlines():
        if not line.strip():
            continue
        parts = line.split("\t")
        if len(parts) < 2:
            continue
        if parts[1].endswith(".md"):
            got.append(parts[1])
    return got


def uncovered(paths, cover):
    """未涵蓋者 ＝ ⛔ 不在 `TARGETS` 涵蓋、且⛔ 不落入任一具名排除前綴。"""
    bad = []
    for p in paths:
        if p in cover:
            continue
        if any(p.startswith(pref) for pref, _r in EXCLUDE):
            continue
        bad.append(p)
    return bad


def main():
    base = sys.argv[1] if len(sys.argv) > 1 else "HEAD"
    print("=" * 96)
    print("  `W-G.9-101` 涵蓋閘：本批受詞 ⊆ `TARGETS` 涵蓋 ∪ 具名排除集（`VR-059 二`）")
    print("=" * 96)
    print("  基座（`base`）＝ %s ；受詞之態 ＝ **工作區**（⛔ 非歷史·`VR-059 四`）" % base)

    T = load_targets()
    cover = {t[0] for t in T}
    print("  `TARGETS` 動態載入自 `verify/tools/wg942_append_audit.py`："
          "項數 %d ／ **涵蓋相異檔 %d**" % (len(T), len(cover)))
    print("  🔒 具名排除集（逐項具名理由·⛔ 不得一句帶過）：")
    for pref, why in EXCLUDE:
        print("     `%s` —— %s" % (pref, why))

    # ── SELFTEST-2：`core.quotepath` 之**雙獨立判準**（`VR-062`）──────────
    # 🩸 舊式 `st2 = (raw_t != raw_f)` 敗於：退化與否取自**受該綁定支配之輸出**
    #   ⇒ 綁定未生效時輸出已被轉義為純 ASCII ⇒「未生效」偽裝成「母體退化」⇒ 不紅。
    # 🔒 本版改為二**互相獨立**之判準，任一為 `False` 即紅：
    #   `2a` 載體級：該次呼叫**實際執行之 argv** 須含 `core.quotepath=false`（⛔ 與輸出無關·永不退化）。
    #   `2b` 經驗級：以 `-z`（**免疫**）取得之真檔名，須逐字現於 `false` 側、⛔ 不現於 `true` 側（三值）。
    P2 = ["ls-tree", "-r", "--name-only", "HEAD", "--", "docs/rulings/"]
    _n0 = len(ARGV_LOG)
    raw_t = git(P2, quotepath=True)          # 對照組（**刻意** true）
    raw_f = git(P2, quotepath=False)
    _argv_f = ARGV_LOG[_n0 + 1]
    st2a = ("core.quotepath=false" in _argv_f)

    zn = git_z(["ls-tree", "-r", "-z", "--name-only", "HEAD", "--", "docs/rulings/"])
    zna = [x for x in zn if any(ord(c) > 127 for c in x)]

    def _st2b(f_side, t_side):
        if not zna:
            return None                       # 真退化：母體無非 ASCII 檔名
        nm = zna[0]
        return (nm in f_side) and (nm not in t_side)
    st2b = _st2b(raw_f, raw_t)
    st2b_disc = _st2b(raw_t, raw_t)           # 判別力：以 true 輸出充 false 側 ⇒ 須 False

    def _z(qp):
        return subprocess.run(["git", "-C", REPO, "-c", "core.quotepath=%s" % qp,
                               "ls-tree", "-r", "-z", "--name-only", "HEAD",
                               "--", "docs/rulings/"],
                              stdout=subprocess.PIPE, check=True).stdout
    z_imm = (_z("true") == _z("false"))       # `-z` 免疫性之自證（⛔ 不假定）

    print("")
    print("  🔒 `SELFTEST-2`（`core.quotepath`·**雙獨立判準**·`VR-062`）：")
    print("     `2a` 載體級：`false` 側實際 argv ＝ %r" % (" ".join(_argv_f[2:5]),))
    print("        ⇒ 含 `core.quotepath=false` ＝ **%s**（須 `True`·⛔ 永不退化）" % st2a)
    print("     `-z` 免疫性自證：二框之 `-z` 輸出逐位相同 ＝ **%s**（須 `True`）" % z_imm)
    print("     `2b` 母體（自 `-z`·⛔ 不受綁定支配）：檔名 %d 條／含非 ASCII **%d** 條"
          % (len(zn), len(zna)))
    if st2b is None:
        print("     ⇒ `2b` ＝ **略過**（真退化·⛔ 不計為證據亦⛔ 不計為反證·家法 9）")
    else:
        print("     ⇒ `2b` ＝ **%s**（錨 %r 逐字現於 `false` 側 ∧ ⛔ 不現於 `true` 側）"
              % (st2b, zna[0]))
    print("     `2b` 判別力自檢（以 `true` 輸出充 `false` 側）＝ **%s**（須 `False`）" % st2b_disc)
    print("     併呈（**僅供參**·⛔ 不作判準）：本批受詞於 `quotepath=true` ＝ %d ／ `false` ＝ %d"
          % (len(subjects(base, quotepath=True)), len(subjects(base, quotepath=False))))

    subs = subjects(base)
    print("")
    print("  本批受詞（狀態 `M` ∧ 尾綴 `.md`）＝ **%d** 筆：" % len(subs))
    for p in subs:
        mark = "✅ 已涵蓋" if p in cover else (
            "⚪ 具名排除" if any(p.startswith(x) for x, _ in EXCLUDE) else "🔴 **未涵蓋**")
        print("     %s  %s" % (mark, p))

    # ── SELFTEST-1：判別力（⛔ 不得省）────────────────────────────────────
    st1 = (uncovered([SYNTHETIC], cover) == [SYNTHETIC])
    print("")
    print("  🔒 `SELFTEST-1`（判別力·注入合成路徑）：`%s` ⇒ 判為未涵蓋 ＝ **%s**（須 `True`）"
          % (SYNTHETIC, st1))

    bad = uncovered(subs, cover)
    if bad:
        print("")
        print("  🔴 **未涵蓋逐項 ＋ 應補之 `TARGETS` 列逐字**（可直接貼入 `wg942_append_audit.py`）：")
        for p in bad:
            print('    ("%s", "檔", None, None),' % p)
    print("")
    # 🔒 `2a`／`z_imm` 永不退化 ⇒ 須 `True`；`2b` 三值 ⇒ 只對 `False` 紅、`None` 略過（家法 9）。
    # 🔒 `2b` 退化（`None`）時，其判別力自檢亦必為 `None` ⇒ 一併略過，
    #   ⛔ 不得因「判別力自檢非 False」而紅（否則真退化又被判成失敗·同一病之第三型）。
    if ((st1 is not True) or (st2a is not True) or (z_imm is not True)
            or (st2b is False)
            or (st2b is not None and st2b_disc is not False)):
        print("  🛑 **自檢未過**：`SELFTEST-1` ＝ %s ／ `2a` ＝ %s ／ `-z` 免疫 ＝ %s"
              " ／ `2b` ＝ %s ／ `2b` 判別力 ＝ %s"
              " ⇒ 本閘⛔ 無鑑別力、其綠⛔ 不得計為證據。"
              % (st1, st2a, z_imm, st2b, st2b_disc))
        print("  結論：🔴 自檢未過")
        return 1
    if bad:
        print("  結論：🔴 %d 項未涵蓋" % len(bad))
        return 1
    print("  結論：✅ 本批受詞全數受涵蓋")
    return 0


if __name__ == "__main__":
    sys.exit(main())
