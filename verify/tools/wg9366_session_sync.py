#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""`W-G.9-366`：開工自動對齊（Claude Code 之 SessionStart hook·⛔ 零生產碼）。

緣由：桌面版新開之 worktree 有時建於舊版本（例：主線已至 `3c0c59c`，新工作區仍為 `0e0edb3`），
致開工時讀不到 `.claude/rules/` 之最新規則。本器於開工（`startup`／`clear`）時檢查工作區，
合於下列全部條件者，以 `git merge --ff-only` 快轉至主線之端，並告知 Claude 重讀規則：

  1. 工作區之遠端 `origin` 之網址以 `land-readjustment-trial`（或其 `.git`）結尾（他專案一律不動）；
  2. 工作區為 linked worktree（主 checkout 一律不動）；
  3. 所在分支名以 `claude/` 起首（桌面版所建者；detached 與他分支一律不動）；
  4. 追蹤檔無變動（`git status --porcelain --untracked-files=no` 為空）；
  5. `HEAD` 為主線之端之祖先而不等於之（即無主線所無之 commit、且確實落後）；
  6. 主線之端所新增之檔，於工作區皆不存在（⛔ 覆蓋未追蹤或被忽略之檔）。

落後而不合 4〜6 者，只出通知、不動；不落後者（含只超前者）無聲。快轉而常設規則索引於開工時係舊版或缺者，
另於該工作區之 git 管理目錄記一狀態檔；其後 context 壓縮（`compact`）時再提醒重讀，`/clear` 或新開工後解除
（狀態係逐工作區、⛔ 逐工作階段：同一工作區另開之工作階段開工時亦解除之）。
⛔ push、⛔ 動他分支、⛔ 刪任何檔。一切例外皆以 `rc 0` 結束（SessionStart 不得擋開工），其訊息照實出艙。

用法：
  hook（stdin 為 Claude Code 之 JSON，取其 `cwd`、`source`）：python wg9366_session_sync.py
  手動：python wg9366_session_sync.py --cwd <工作區路徑>
  模擬 hook（以子程序經 stdin 餵 JSON）：python wg9366_session_sync.py --hook-sim <工作區路徑> <source>
  自驗：python wg9366_session_sync.py --selftest          ⇒ 末列 `⇒ 紅 []；rc 0`
  判別力：python wg9366_session_sync.py --selftest-mutant ⇒ 末列 `⇒ 紅 ['T3', 'T4', 'T12']；rc 1`
"""
import json
import os
import re
import shutil
import stat
import subprocess
import sys
import tempfile
import time

MAINLINE = "wip/s1-endpart"
REMOTE = "origin"
PROJECT_KEY = "land-readjustment-trial"
INDEX = ".claude/rules/常設規則索引.md"
DOMAIN = ".claude/rules/配地碼之領域指引.md"
TAG = "【開工自動對齊·W-G.9-366】"
STATE = "wg9366_state"          # 置於該工作區之 git 管理目錄（.git/worktrees/<名>/）·⛔ 在工作樹內
FETCH_LIMIT = 20                # 秒
MERGE_DEADLINE = 40             # 秒：自本器開始逾此即⛔ 快轉（hook 之限時為 60 秒）
_URL_RE = re.compile(r"[/\\:]" + re.escape(PROJECT_KEY) + r"(\.git)?[/\\]?$")
_ENV = dict(os.environ, GIT_TERMINAL_PROMPT="0", GCM_INTERACTIVE="never")


_NOGC = ["-c", "gc.auto=0", "-c", "maintenance.auto=false"]   # Windows 下 gc 無法背景執行 ⇒ 關之


def _git(cwd, *args, timeout=30):
    r = subprocess.run(["git", *_NOGC, "-C", cwd, *args], capture_output=True, timeout=timeout, env=_ENV,
                       stdin=subprocess.DEVNULL)
    return r.returncode, r.stdout.decode("utf-8", "replace").strip(), r.stderr.decode("utf-8", "replace").strip()


def _fetch(cwd):
    """取主線之端；輸出一律丟棄（⛔ 管線 ⇒ 逾時之子程序不致卡住本器）。"""
    try:
        subprocess.run(["git", *_NOGC, "-c", "http.lowSpeedLimit=1000", "-c", "http.lowSpeedTime=10", "-C", cwd,
                        "fetch", "--quiet", REMOTE, MAINLINE], stdin=subprocess.DEVNULL,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=FETCH_LIMIT, env=_ENV)
    except subprocess.TimeoutExpired:
        pass                                    # 連不上則以本機之遠端追蹤 ref 為準


def _blob(cwd, rev, path):
    rc, out, _ = _git(cwd, "rev-parse", "--verify", "--quiet", f"{rev}:{path}")
    return out if rc == 0 else None


def _ours(cwd, need_branch=True):
    """合於條件 1〜3（need_branch=False 時只 1〜2）者回 (工作樹頂, 分支或空字串)，否則 None。"""
    rc, url, _ = _git(cwd, "remote", "get-url", REMOTE)
    if rc != 0 or not _URL_RE.search(url.strip()):
        return None
    rc, top, _ = _git(cwd, "rev-parse", "--show-toplevel")
    if rc != 0 or not os.path.isfile(os.path.join(top, ".git")):
        return None                             # 主 checkout（.git 為目錄）或非 git
    rc, branch, _ = _git(cwd, "symbolic-ref", "--quiet", "--short", "HEAD")
    if need_branch and (rc != 0 or not branch.startswith("claude/")):
        return None                             # detached 或非桌面版所建之分支
    return top, (branch if rc == 0 else "")


def _state_path(cwd):
    rc, gd, _ = _git(cwd, "rev-parse", "--absolute-git-dir")
    return os.path.join(gd, STATE) if rc == 0 and gd else None


def _set_state(cwd, value):
    """記狀態；寫不成者回 False（⛔ 擋開工、⛔ 吞訊息）。"""
    try:
        p = _state_path(cwd)
        if not p:
            return False
        with open(p, "w", encoding="utf-8", newline="\n") as f:
            f.write(value + "\n")
        return True
    except OSError:
        return False


def _get_state(cwd):
    p = _state_path(cwd)
    if p and os.path.isfile(p):
        return open(p, encoding="utf-8").read().strip()
    return None


def _occupied(top, rel):
    """主線所新增之 rel，於工作區已有同名之檔，或其上層路徑已為檔（快轉將覆蓋或移除之）。"""
    parts = rel.split("/")
    for k in range(1, len(parts)):
        q = os.path.join(top, *parts[:k])
        if os.path.lexists(q) and not os.path.isdir(q):
            return True
    return os.path.lexists(os.path.join(top, *parts))


def align(cwd, mutate=False, fetch=True):
    """回 (訊息或空字串, 動作)。動作 ∈ {"skip", "current", "ff", "notice", "error"}。"""
    t0 = time.monotonic()
    ours = _ours(cwd)
    if ours is None:
        return "", "skip"
    top, branch = ours
    tip_ref = f"{REMOTE}/{MAINLINE}"
    if fetch:
        _fetch(cwd)
    rc, tip, _ = _git(cwd, "rev-parse", "--verify", "--quiet", tip_ref)
    if rc != 0:
        return f"{TAG}找不到 `{tip_ref}`，未對齊；施工前請依單之開場核對主線之端。", "error"
    _, head, _ = _git(cwd, "rev-parse", "HEAD")
    _, n_behind, _ = _git(cwd, "rev-list", "--count", f"HEAD..{tip_ref}")
    if head == tip or n_behind == "0":
        return "", "current"                    # 已在主線之端，或只超前（無可快轉）
    behind = _git(cwd, "merge-base", "--is-ancestor", "HEAD", tip_ref)[0] == 0
    _, n_ahead, _ = _git(cwd, "rev-list", "--count", f"{tip_ref}..HEAD")
    _, dirty, _ = _git(cwd, "status", "--porcelain", "--untracked-files=no")
    rc, added, _ = _git(cwd, "diff", "--name-only", "--diff-filter=AR", "-z", "HEAD", tip_ref)
    if rc != 0:
        clash = ["（無從比對主線所新增之檔）"]
    else:
        clash = [p for p in added.split("\0") if p and _occupied(top, p)]
    if not mutate and (dirty or not behind or clash):
        if dirty:
            why = "追蹤檔有未提交之變動"
        elif not behind:
            why = f"含主線所無之 commit {n_ahead} 筆（自己之成果，或建於他分支）"
        else:
            why = f"主線所新增之檔已存在於工作區（{'、'.join(clash[:3])}{' 等' if len(clash) > 3 else ''}）"
        return (f"{TAG}本工作區（分支 `{branch}`·`{head[:7]}`）落後主線 `{MAINLINE}`（`{tip[:7]}`）{n_behind} 筆，"
                f"但{why}，未自動快轉。施工前請依單之開場核對主線之端。"), "notice"
    if time.monotonic() - t0 > MERGE_DEADLINE:
        return (f"{TAG}本工作區（分支 `{branch}`·`{head[:7]}`）落後主線 `{MAINLINE}` {n_behind} 筆，"
                f"但取主線之端逾時，未自動快轉。施工前請依單之開場核對主線之端。"), "notice"
    old_idx = _blob(cwd, "HEAD", INDEX)
    rc, _, err = _git(cwd, "merge", "--ff-only", "--quiet", tip_ref)
    if rc != 0:
        return f"{TAG}快轉失敗（`{head[:7]}` → `{tip[:7]}`）：{err[:300]}。施工前請依單之開場核對主線之端。", "error"
    new_idx = _blob(cwd, "HEAD", INDEX)
    msg = (f"{TAG}本工作區（分支 `{branch}`）建於 `{head[:7]}`，落後主線 `{MAINLINE}` {n_behind} 筆；"
           f"已以 `git merge --ff-only` 快轉至 `{tip[:7]}`（工作區之檔已更新為主線之最新版；快轉前本工作區無未提交之變動、無自己之 commit）。")
    if new_idx and new_idx != old_idx:
        msg += (f"開工時所載入之常設規則係舊版或缺：請先以 Read 讀 `{INDEX}`；"
                f"讀寫 `app.py` 或 `verify/` 之 Python 檔以前，另讀 `{DOMAIN}`。")
        if not _set_state(cwd, "stale"):
            msg += "（狀態檔未能寫入：context 壓縮後之再提醒將缺。）"
    else:
        msg += "常設規則索引未變。"
    return msg, "ff"


def on_compact(cwd):
    """context 壓縮後：本工作階段若係快轉而來（狀態 ＝ stale），再提醒重讀。"""
    if _ours(cwd, need_branch=False) is None or _get_state(cwd) != "stale":
        return ""
    return (f"{TAG}本工作階段開工時常設規則索引係舊版或缺（其後已自動快轉）；context 已壓縮，"
            f"若 context 中未見 `{INDEX}` 之全文，請再以 Read 讀之；讀寫 `app.py` 或 `verify/` 之 Python 檔以前，另讀 `{DOMAIN}`。")


def dispatch(cwd, source, mutate=False, fetch=True):
    """依 SessionStart 之來源分派；回訊息（可為空）。"""
    if source == "compact":
        return on_compact(cwd)
    if source not in (None, "startup", "clear"):
        return ""                               # resume、fork 等：不動
    if _ours(cwd, need_branch=False) is not None and _get_state(cwd) == "stale":
        _set_state(cwd, "fresh")                # 新開工或 /clear ⇒ 規則自磁碟重新載入
    msg, _ = align(cwd, mutate, fetch)
    return msg


def _emit(text):
    if text:
        sys.stdout.buffer.write((text + "\n").encode("utf-8"))


def _hook():
    cwd, source = os.getcwd(), None
    try:
        data = json.loads(sys.stdin.buffer.read().decode("utf-8") or "{}")
        source = data.get("source")
        cwd = data.get("cwd") or cwd
    except Exception:
        pass
    try:
        msg = dispatch(cwd, source)
    except Exception as e:  # SessionStart ⛔ 擋開工
        msg = f"{TAG}本器例外（{type(e).__name__}），未對齊；施工前請依單之開場核對主線之端。"
    _emit(msg)
    return 0


def _hook_sim(cwd, source):
    """以子程序執行本器之 hook 模式（stdin ＝ JSON），照實出艙其 stdout 與 rc。"""
    payload = json.dumps({"cwd": cwd, "source": source, "hook_event_name": "SessionStart"}, ensure_ascii=False)
    r = subprocess.run([sys.executable, os.path.abspath(__file__)], input=payload.encode("utf-8"), capture_output=True)
    out = r.stdout.decode("utf-8", "replace")
    sys.stdout.write(out)
    print(f"（hook 子程序 rc {r.returncode}·stdout {len(r.stdout)} B·stderr {len(r.stderr)} B）")
    return 0


def _rm(path):
    """刪暫存目錄（Windows 下 git 之物件檔為唯讀，先去唯讀）；回是否刪盡。"""
    for root, dirs, files in os.walk(path):
        for n in dirs + files:
            try:
                os.chmod(os.path.join(root, n), stat.S_IWRITE | stat.S_IREAD | stat.S_IEXEC)
            except OSError:
                pass
    shutil.rmtree(path, ignore_errors=True)
    return not os.path.exists(path)


# ── 自驗（暫存目錄內建倉·⛔ 觸及本倉·⛔ 連網）──────────────────────────────────
def _selftest(mutate=False):
    tmp = tempfile.mkdtemp(prefix="wg9366_")
    cfg = ["-c", "user.name=wg9366", "-c", "user.email=wg9366@test", "-c", "core.autocrlf=false",
           "-c", "init.defaultBranch=main", "-c", "commit.gpgsign=false"]

    def run(cwd, *a):
        r = subprocess.run(["git", *cfg, "-C", cwd, *a], capture_output=True)
        if r.returncode != 0:
            raise RuntimeError(f"git {' '.join(a)}: {r.stderr.decode('utf-8', 'replace')}")
        return r.stdout.decode().strip()

    def write(path, text):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(text)

    red, lines = [], []

    def check(name, ok, detail):
        lines.append(f"  {'✅' if ok else '🔴'} {name} {detail}")
        if not ok:
            red.append(name)

    try:
        def make(proj):
            bare = os.path.join(tmp, proj + ".git")
            main = os.path.join(tmp, proj + "_main")
            subprocess.run(["git", *cfg, "init", "--bare", "-q", bare], check=True)
            subprocess.run(["git", *cfg, "clone", "-q", bare, main], check=True, capture_output=True)
            run(main, "checkout", "-q", "-b", MAINLINE)
            write(os.path.join(main, "a.txt"), "A\n")
            write(os.path.join(main, "sub", "s.txt"), "S\n")
            run(main, "add", "a.txt", "sub"); run(main, "commit", "-q", "-m", "A")
            a = run(main, "rev-parse", "HEAD")
            write(os.path.join(main, INDEX), "索引 B\n")
            run(main, "add", INDEX); run(main, "commit", "-q", "-m", "B")
            b = run(main, "rev-parse", "HEAD")
            run(main, "push", "-q", "origin", MAINLINE)
            return main, a, b

        main, a, b = make(PROJECT_KEY)

        def wt(name, base, branch=True):
            p = os.path.join(tmp, "wt_" + name)
            if branch:
                run(main, "worktree", "add", "-q", "-b", f"claude/{name}" if branch is True else branch, p, base)
            else:
                run(main, "worktree", "add", "-q", "--detach", p, base)
            return p

        def head(p):
            return run(p, "rev-parse", "HEAD")

        # T1：落後、乾淨、claude/ ⇒ 快轉，並令重讀索引（索引於 A 無、於 B 有）；記狀態 stale
        p = wt("t1", a); msg, act = align(p, mutate)
        check("T1", act == "ff" and head(p) == b and "已以 `git merge --ff-only` 快轉" in msg and "請先以 Read 讀" in msg
              and _get_state(p) == "stale", f"act={act} head={'tip' if head(p) == b else head(p)[:7]} state={_get_state(p)}")
        # T2：已在主線之端 ⇒ 無聲
        p = wt("t2", b); msg, act = align(p, mutate)
        check("T2", act == "current" and msg == "" and head(p) == b, f"act={act}")
        # T3：有自己之 commit（與主線分叉）⇒ 只通知、不動
        p = wt("t3", a); write(os.path.join(p, "own.txt"), "own\n")
        run(p, "add", "own.txt"); run(p, "commit", "-q", "-m", "own"); h0 = head(p)
        msg, act = align(p, mutate)
        check("T3", act == "notice" and head(p) == h0 and "含主線所無之 commit 1 筆" in msg, f"act={act}")
        # T4：追蹤檔有變動 ⇒ 只通知、不動
        p = wt("t4", a); write(os.path.join(p, "a.txt"), "A dirty\n"); msg, act = align(p, mutate)
        check("T4", act == "notice" and head(p) == a and "追蹤檔有未提交之變動" in msg, f"act={act}")
        # T5：主 checkout ⇒ 無聲、不動
        run(main, "checkout", "-q", "--detach", a); run(main, "checkout", "-q", "-B", "claude/t5main", a)
        msg, act = align(main, mutate)
        check("T5", act == "skip" and head(main) == a and msg == "", f"act={act}")
        # T6：非 claude/ 之分支 ⇒ 無聲、不動
        p = wt("t6", a, branch="feature/t6"); msg, act = align(p, mutate)
        check("T6", act == "skip" and head(p) == a and msg == "", f"act={act}")
        # T7：detached ⇒ 無聲、不動
        p = wt("t7", a, branch=False); msg, act = align(p, mutate)
        check("T7", act == "skip" and head(p) == a and msg == "", f"act={act}")
        # T8：他專案、名稱相近之他專案（遠端網址不以專案名結尾）⇒ 無聲、不動
        res = []
        for proj in ("other-project", PROJECT_KEY + "-archive"):
            main2, a2, _ = make(proj)
            p8 = os.path.join(tmp, "wt_t8_" + proj); run(main2, "worktree", "add", "-q", "-b", "claude/t8", p8, a2)
            msg, act = align(p8, mutate)
            res.append(act == "skip" and run(p8, "rev-parse", "HEAD") == a2 and msg == "")
        check("T8", all(res), f"res={res}")
        # T9：落後但索引未變 ⇒ 快轉，訊息載「常設規則索引未變」，⛔ 記 stale
        write(os.path.join(main, "c.txt"), "C\n")
        run(main, "checkout", "-q", MAINLINE)
        run(main, "add", "c.txt"); run(main, "commit", "-q", "-m", "C"); c = run(main, "rev-parse", "HEAD")
        run(main, "push", "-q", "origin", MAINLINE)
        p = wt("t9", b); msg, act = align(p, mutate)
        check("T9", act == "ff" and head(p) == c and "常設規則索引未變" in msg and "請先以 Read 讀" not in msg
              and _get_state(p) is None, f"act={act}")
        # T10：主線之端由他處推進（本機之遠端追蹤 ref 仍舊）⇒ 須經 fetch 方知落後
        other = os.path.join(tmp, "other_clone")
        subprocess.run(["git", *cfg, "clone", "-q", "-b", MAINLINE, os.path.join(tmp, PROJECT_KEY + ".git"), other],
                       check=True, capture_output=True)
        write(os.path.join(other, "d.txt"), "D\n")
        run(other, "add", "d.txt"); run(other, "commit", "-q", "-m", "D"); d = run(other, "rev-parse", "HEAD")
        run(other, "push", "-q", "origin", MAINLINE)
        p = wt("t10a", c); msg, act = align(p, mutate, fetch=False)
        check("T10a", act == "current" and head(p) == c, f"act={act}（⛔ fetch ⇒ 不知落後·對照）")
        p = wt("t10", c); msg, act = align(p, mutate)
        check("T10", act == "ff" and head(p) == d and "落後主線 `wip/s1-endpart` 1 筆" in msg,
              f"act={act} head={'D' if head(p) == d else head(p)[:7]}")
        # T11：只超前（有自己之 commit、⛔ 落後）⇒ 無聲、不動
        p = wt("t11", d); write(os.path.join(p, "own.txt"), "own\n")
        run(p, "add", "own.txt"); run(p, "commit", "-q", "-m", "own"); h0 = head(p)
        msg, act = align(p, mutate)
        check("T11", act == "current" and msg == "" and head(p) == h0, f"act={act}")
        # T12：主線所新增之檔已以「被忽略之檔」存在於工作區（git 於快轉時會逕行覆蓋之）⇒ 只通知、⛔ 覆蓋
        p = wt("t12", c); write(os.path.join(p, ".gitignore"), "d.txt\n"); write(os.path.join(p, "d.txt"), "local\n")
        msg, act = align(p, mutate)
        ok12a = act == "notice" and head(p) == c and "d.txt" in msg and \
            open(os.path.join(p, "d.txt"), encoding="utf-8").read() == "local\n"
        # 上層路徑已為被忽略之檔（主線新增 sub2/e.txt，工作區有被忽略之檔 sub2）
        run(main, "merge", "-q", "--ff-only", d)
        write(os.path.join(main, "sub2", "e.txt"), "E\n")
        run(main, "add", "sub2"); run(main, "commit", "-q", "-m", "E")
        run(main, "push", "-q", "origin", MAINLINE)
        q = wt("t12b", d); write(os.path.join(q, ".gitignore"), "sub2\n"); write(os.path.join(q, "sub2"), "local\n")
        msg2, act2 = align(q, mutate)
        ok12b = act2 == "notice" and head(q) == d and "sub2/e.txt" in msg2 and os.path.isfile(os.path.join(q, "sub2"))
        check("T12", ok12a and ok12b, f"act={act}/{act2}")
        # T13：hook 之分派——resume 不動；工作階段之目錄為子目錄亦快轉；壓縮後再提醒；/clear 後解除
        p = wt("t13", a)
        r1 = dispatch(p, "resume", mutate)
        ok1 = r1 == "" and head(p) == a
        r2 = dispatch(os.path.join(p, "sub"), "startup", mutate)
        ok2 = ("已以 `git merge --ff-only` 快轉" in r2 and head(p) == run(p, "rev-parse", f"{REMOTE}/{MAINLINE}")
               and _get_state(p) == "stale")
        r3 = dispatch(p, "compact", mutate)
        ok3 = "context 已壓縮" in r3 and "請再以 Read 讀之" in r3
        r4 = dispatch(p, "clear", mutate)
        ok4 = r4 == "" and _get_state(p) == "fresh"
        r5 = dispatch(p, "compact", mutate)
        ok5 = r5 == ""
        # 開工快轉後轉為 detached（各單之開場即如此）⇒ 壓縮時仍提醒、/clear 時仍解除
        q = wt("t13d", a); dispatch(q, "startup", mutate); run(q, "checkout", "-q", "--detach")
        ok6 = "context 已壓縮" in dispatch(q, "compact", mutate)
        ok7 = dispatch(q, "clear", mutate) == "" and _get_state(q) == "fresh" and dispatch(q, "compact", mutate) == ""
        check("T13", ok1 and ok2 and ok3 and ok4 and ok5 and ok6 and ok7,
              f"resume={ok1} startup(子目錄)={ok2} compact={ok3} clear={ok4} compact′={ok5} detached={ok6 and ok7}")
        # T14：遠端追蹤 ref 不存在 ⇒ 錯誤之通知（⛔ 擋開工）
        run(main, "update-ref", "-d", f"refs/remotes/{REMOTE}/{MAINLINE}")
        p = wt("t14", a); msg, act = align(p, mutate, fetch=False)
        check("T14", act == "error" and "找不到" in msg and head(p) == a, f"act={act}")
    except Exception as e:
        lines.append(f"  🔴 例外 {type(e).__name__}: {e}")
        red.append("EXC")
    finally:
        if not _rm(tmp):
            print(f"⚠️ 暫存目錄未能全刪（⛔ 影響判定）：{tmp}", file=sys.stderr)
    print("\n".join(lines))
    rc = 1 if red else 0
    print(f"⇒ 紅 {red}；rc {rc}")
    return rc


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    a = sys.argv[1:]
    if a[:1] == ["--selftest"]:
        return _selftest(False)
    if a[:1] == ["--selftest-mutant"]:
        return _selftest(True)
    if a[:1] == ["--cwd"] and len(a) == 2:
        msg, act = align(a[1])
        print(msg or f"（無訊息·{act}）")
        return 0
    if a[:1] == ["--hook-sim"] and len(a) == 3:
        return _hook_sim(a[1], a[2])
    return _hook()


if __name__ == "__main__":
    sys.exit(main())
