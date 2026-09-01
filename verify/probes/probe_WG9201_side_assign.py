# -*- coding: utf-8 -*-
r"""`W-G.9-201` 歸側實算探針（⛔ 唯讀·⛔ 零生產碼）

## 受詞

`K-9-24` **二**之四分支需知「`M`（步驟 0 合併後同時跨占同街廓左右兩街角規定範圍者）
在左右兩側各自**拿不拿得下**」。本探針以真資料實算之，⛔ 不以推定代之。

## 三態（同一次執行內產生·`R-7`）

| 態 | 構造 | 用 |
|---|---|---|
| `A` | 現行倉態（`k6_step0_block_locked` 之保守替代**照舊生效**） | **對照組**（未合併態） |
| `B` | `K-9-24` **一**：步驟 0 **無條件** ⇒ 層疊 `ns["k6_step0_block_locked"] → False` | 受詞 |
| `C(M)` | 態 `B` ＋ 於 `v12` 之 `candidates` 中扣除該 `M`（`K-9-24` **二·5**） | 另一側之評選 |

🔒 **層疊點之依據**：`k6_step0_merge` 以**全域查找**呼叫 `k6_step0_block_locked`
（`grep -n "if k6_step0_block_locked(side_lines_by_side, _lbl):" app.py`），而 `harvest()` 之
`ns` **即 app 模組之 `globals()`**（本檔以 `ns is _projection_order.__globals__` 自證）
⇒ 覆寫 `ns[...]` 即生效。`run_corner_pk` 亦以 `ns["select_corner_lots_both_sides_v12"]` 取值
（`grep -n 'v12 = ns\["select_corner_lots_both_sides_v12"\]' verify/selection_pipeline.py`）。

## 自我驗證閘（⛔ 得省·`CLAUDE.md`「探針還原內部幾何時…」之第一觸發點）

1. **層疊生效**：態 `A` 之 `f3_k6_step0_diag.blocks_locked_k921` 須**非空**、態 `B` 須**空**；
   且態 `B` 之 `groups_merged` ＞ 態 `A`。（＝反靜默退路之「咬到」計數器）
2. **扣除之獨立性**：態 `C(M)` 中**其餘**候選之 `總分`／`達標`／`真G` 須與態 `B` **逐格相同**。
   碼面保證 ＝ 三指數之分母皆取自 **range 自身**（`_corner_cut_den`／`_side_line_den`／
   `_corner_range_area`），⛔ 候選集之極值（`grep -n "score_corner_cut = 0.4 \* min" app.py`）。
   **此閘不過 ⇒ ⛔ 不得據以下任何結論。**

## 🛑 限

- 本探針之數 **⛔ 得逕作為任何裁之依據**（單 `§三` 逐字）——係診斷，須經發單側獨立復驗、
  KL 認可，方得進入 `K-9-24` 之實例段或任何生產碼。
- 情境參數 `退縮(setback)` 由 **`WV_SB` 環境變數**供（⛔ 硬編·`R-1`）；缺值 loud raise。
- ⛔ 改 `app.py` 一字；⛔ 改任何既有 `verify/**.py` 一字；⛔ 被任何既有流程呼叫。
"""
import contextlib
import io
import os
import platform
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
sys.path.insert(0, VERIFY)
sys.path.insert(0, HERE)

OUTDIR = os.path.join(VERIFY, "out")

# 🔒 側鍵之**唯一來源** ＝ `verify/selection_pipeline.py` 之診斷列構造逐字
#    （`grep -n "for _dg_side, _dg_res in ((.左., _l_v13), (.右., _r_v13)):" verify/selection_pipeline.py`）
#    ⇒ 此二值係**引擎之欄位契約**（案無關），⛔ 本案資料；下方另設閘自證觀測到之端值集恰為此二者。
SIDE_OF_P1 = "左"      # ＝ `p1_end`（FRONT_LINE 起點側·`CLAUDE.md` CAD 圖層規範「p1＝左」）
SIDE_OF_P2 = "右"      # ＝ `p2_end`
SIDES = (SIDE_OF_P1, SIDE_OF_P2)
# 🔒 `f3_corner_range_areas` 之側鍵（同屬引擎欄位契約·案無關）
#    源逐字 ＝ `grep -n "_corner_poly_p1_B4 = _corner_range_left" app.py`（left→p1→左）
RANGE_KEY = {SIDE_OF_P1: "left", SIDE_OF_P2: "right"}

L = []


def say(s=""):
    L.append(s)
    print(s)


def loud(msg):
    """🔒 `R-6` 反靜默：取不到值一律具名報錯停機，⛔ 預設值、⛔ 跳過。"""
    raise RuntimeError("🔴 [W-G.9-201] " + msg)


def git1(args):
    p = subprocess.run(["git"] + args, cwd=REPO, capture_output=True)
    if p.returncode != 0:
        loud("git %r rc=%d：%s" % (args, p.returncode, p.stderr[:200]))
    return p.stdout.decode("utf-8").strip()


def get_sb():
    raw = os.environ.get("WV_SB")
    if raw is None or str(raw).strip() == "":
        loud("情境參數 `WV_SB`（退縮 m）未設 ⇒ 停機。`R-1` 禁硬編本案常數、"
             "`R-6` 禁靜默兜底。用法：`WV_SB=<m> python verify/probes/probe_WG9201_side_assign.py`")
    try:
        return float(raw)
    except (TypeError, ValueError):
        loud("`WV_SB`=%r ⛔ 非數 ⇒ 停機" % raw)


# ════════════════════════════════════════════════════════════════════
#  一趟量測
# ════════════════════════════════════════════════════════════════════

def run_state(setback, *, unconditional_step0, drop_pids=frozenset()):
    """跑一趟完整管線，回傳量測包。

    unconditional_step0 : True ⇒ 層疊 `k6_step0_block_locked` → 恆 False（`K-9-24` 一）
    drop_pids           : 於 `v12` 之 `candidates` 中扣除之暫編地號集（`K-9-24` 二·5）
    """
    from app_harvest import harvest
    import run_verification as rv
    from selection_pipeline import build_ownership, build_build_parcels, run_corner_pk

    ns, fake_st = harvest()
    self_check = (ns is ns["_projection_order"].__globals__)
    if not self_check:
        loud("`ns is _projection_order.__globals__` ＝ False ⇒ 層疊⛔ 生效，結論不得出艙")

    locked_calls = {"n": 0, "forced_false": 0}
    if unconditional_step0:
        _orig_lock = ns.get("k6_step0_block_locked")
        if _orig_lock is None:
            loud("`ns` 內查無 `k6_step0_block_locked` ⇒ 層疊點失據")

        def _no_lock(side_lines_by_side, label):
            locked_calls["n"] += 1
            if _orig_lock(side_lines_by_side, label):
                locked_calls["forced_false"] += 1     # 🔒 咬到計數器（反靜默）
            return False
        ns["k6_step0_block_locked"] = _no_lock

    v12_calls = {"n": 0, "dropped": 0}
    if drop_pids:
        _orig_v12 = ns.get("select_corner_lots_both_sides_v12")
        if _orig_v12 is None:
            loud("`ns` 內查無 `select_corner_lots_both_sides_v12` ⇒ 層疊點失據")

        def _v12_drop(*a, **kw):
            cands = kw.get("candidates")
            if cands is None:
                loud("`v12` 之 `candidates` 非具名傳入 ⇒ 扣除層疊失據（⛔ 靜默略過）")
            keep = [c for c in cands if c.get("暫編地號") not in drop_pids]
            v12_calls["n"] += 1
            v12_calls["dropped"] += len(cands) - len(keep)
            kw["candidates"] = keep
            return _orig_v12(*a, **kw)
        ns["select_corner_lots_both_sides_v12"] = _v12_drop

    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    # 🔇 app 側於本段會 print 大量診斷；⛔ 混入本探針之出艙（`R-9` 全文可存檔）
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        temp_p, build_p, _sw = rv.build_build_parcels(
            ns, fake_st, v6, list(cb_by.values()), snapshot)
        params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
        cand_diag, sel_rows, off_rows, wins, forced = run_corner_pk(
            ns, fake_st, list(cb_by.values()), cad, params, temp_p, build_p,
            setback, snapshot=snapshot)

    k6diag = fake_st.session_state.get("f3_k6_step0_diag")
    if k6diag is None:
        loud("`f3_k6_step0_diag` 未產生 ⇒ 步驟 0 之通道未走到（⛔ 靜默視為未合併）")

    fcb = ns["F3_CATEGORY_BURDEN"]
    cb_all = list(cb_by.values())
    blocks_all = [b.get("label") for b in cb_all]
    blocks_build = [b.get("label") for b in cb_all
                    if fcb.get(b.get("category", ""), "") == "可建築土地"]
    return {
        "self_check": self_check,
        "temp": temp_p, "build": build_p, "diag": cand_diag,
        "sel": sel_rows, "off": off_rows, "wins": wins, "forced": forced,
        "k6": k6diag, "blocks_all": blocks_all, "blocks_build": blocks_build,
        "locked_calls": dict(locked_calls), "v12_calls": dict(v12_calls),
        "noise_chars": len(buf.getvalue()),
        # 🔒 街角規定範圍面積（塊×側級·⛔ 依候選集）——供「扣除後候選集空」時仍能報其範圍面積
        "crange": dict(fake_st.session_state.get("f3_corner_range_areas") or {}),
    }


def range_area(state, blk, side):
    """自 `f3_corner_range_areas` 取該塊該側之街角規定範圍面積（⛔ 自候選列反推）。"""
    d = state["crange"].get(blk)
    if d is None:
        loud("`f3_corner_range_areas` 無街廓 %r ⇒ ⛔ 得編造其範圍面積（`R-6`）" % blk)
    k = RANGE_KEY[side]
    if k not in d:
        loud("`f3_corner_range_areas[%r]` 無側鍵 %r（有 %r）⇒ 停機" % (blk, k, sorted(d)))
    v = d[k]
    if v is None:
        loud("街廓 %r 之 %r 側範圍面積 ＝ None（該側無街角?）⇒ 停機，⛔ 靜默視為 0" % (blk, side))
    return float(v)


# ════════════════════════════════════════════════════════════════════
#  診斷列之索引
# ════════════════════════════════════════════════════════════════════

def index_diag(rows):
    """{(街廓, 端): {暫編地號: row}}；並自證端值集恰為引擎契約之二者。"""
    seen_sides = sorted({str(r.get("端", "")) for r in rows})
    if seen_sides and seen_sides != sorted(SIDES):
        loud("觀測到之端值集 = %r ⛔ 引擎契約 %r ⇒ 側鍵失據（⛔ 靜默續辦）"
             % (seen_sides, sorted(SIDES)))
    d = {}
    for r in rows:
        k = (str(r.get("街廓", "")), str(r.get("端", "")))
        pid = str(r.get("候選地號", ""))
        if not pid:
            loud("診斷列缺 `候選地號`：%r" % (r,))
        d.setdefault(k, {})[pid] = r
    return d


def cell(row, key):
    if key not in row:
        loud("診斷列缺欄 %r（母體 ＝ `run_corner_pk` 之 `_corner_cand_diag`）：%r" % (key, sorted(row)))
    return row[key]


def score_of(row):
    v = cell(row, "總分")
    if v == "—" or v is None or v == "":
        loud("候選 %r 於 %r 端之 `總分` ＝ %r（⛔ 數）⇒ 停機，⛔ 靜默視為 0"
             % (cell(row, "候選地號"), cell(row, "端"), v))
    return float(v)


def is_pass(row):
    v = str(cell(row, "達標"))
    if v not in ("達標", "未達標"):
        loud("`達標` 欄值 %r ⛔ 於 {達標, 未達標} ⇒ 停機" % v)
    return v == "達標"


def is_winner(row):
    return str(cell(row, "選中")) == "✅"


def pick_winner(rows):
    """扣除後之「照常評選」：達標者中 `總分`(4dp) 最大，平手取 `原位次(投影序)` 小者。
    🔒 鍵序逐字同 `_pk_one_side_v12` 之 `qualified.sort`
    （`grep -n "qualified.sort(key=lambda c: (" app.py`）。"""
    q = [r for r in rows if is_pass(r)]
    if not q:
        return None, q
    q2 = sorted(q, key=lambda r: (-round(score_of(r), 4),
                                  float(cell(r, "原位次(投影序)"))))
    return q2[0], q


# ════════════════════════════════════════════════════════════════════
#  主
# ════════════════════════════════════════════════════════════════════

def main():                                                   # noqa: C901
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8")
        except Exception:                                      # noqa: BLE001
            pass
    os.makedirs(OUTDIR, exist_ok=True)
    SB = get_sb()
    head = git1(["rev-parse", "--short=8", "HEAD"])
    BAR = "=" * 118

    say(BAR)
    say("【W-G.9-201】歸側實算探針 — `K-9-24` 二之四分支（⛔ 唯讀·⛔ 零生產碼）")
    say(BAR)
    say("  態      ＝ %s（`git rev-parse --short=8 HEAD`）" % head)
    say("  app.py  ＝ %s（blob）" % git1(["rev-parse", "HEAD:app.py"]))
    say("  python  ＝ %s ／ 情境 退縮 SB ＝ %.2f m（源 ＝ 環境變數 `WV_SB`·⛔ 硬編）"
        % (platform.python_version(), SB))
    say("  🛑 本探針之數 **⛔ 得逕作為任何裁之依據**——係診斷，須經發單側獨立復驗、KL 認可。")
    say("")

    say("── §一　三態之建立（`R-7`：二態於**同一次執行**內產生·⛔ 跨執行拼接） ──")
    A = run_state(SB, unconditional_step0=False)
    B = run_state(SB, unconditional_step0=True)
    say("  態 A（現行·對照組）：ns 自證 = %s ／ app 側診斷噪音 %d 字元（已隔離）"
        % (A["self_check"], A["noise_chars"]))
    say("  態 B（K-9-24 無條件）：ns 自證 = %s ／ app 側診斷噪音 %d 字元（已隔離）"
        % (B["self_check"], B["noise_chars"]))
    say("")

    say("── §二　🔒 自我驗證閘 ①：層疊生效（反靜默退路之「咬到」計數器） ──")
    lockedA = list(A["k6"].get("blocks_locked_k921") or [])
    lockedB = list(B["k6"].get("blocks_locked_k921") or [])
    say("  態 A｜`blocks_locked_k921` = %r（%d【街廓】·須**非空**）" % (lockedA, len(lockedA)))
    say("  態 B｜`blocks_locked_k921` = %r（%d【街廓】·須**空**）" % (lockedB, len(lockedB)))
    say("  態 B｜層疊被呼叫 %d【次】／其中原判為「鎖」而被強制放行 = **%d**【次】"
        % (B["locked_calls"]["n"], B["locked_calls"]["forced_false"]))
    for tag, S in (("A", A), ("B", B)):
        k = S["k6"]
        say("  態 %s｜groups_found=%d／groups_merged=%d／parcels_absorbed=%d／"
            "parcels_in=%d／parcels_out=%d／blocks_buildable=%d／anomalies=%d"
            % (tag, k.get("groups_found", -1), k.get("groups_merged", -1),
               k.get("parcels_absorbed", -1), k.get("parcels_in", -1),
               k.get("parcels_out", -1), k.get("blocks_buildable", -1),
               len(k.get("anomalies") or [])))
    gate1 = (len(lockedA) > 0 and len(lockedB) == 0
             and B["locked_calls"]["forced_false"] > 0
             and B["k6"].get("groups_merged", 0) > A["k6"].get("groups_merged", 0))
    say("  ⇒ 🔒 **閘 ① = %s**（A 非空 ∧ B 空 ∧ 強制放行非零 ∧ B 之合併群數 > A）" % gate1)
    if not gate1:
        loud("自我驗證閘 ① 不過 ⇒ ⛔ 結論不得出艙")
    say("")
    say("  態 B 之合併宗（逐筆·%d【群】）：" % len(B["k6"].get("merged") or []))
    for m in (B["k6"].get("merged") or []):
        say("    ・街廓 %s｜命名 %s｜成員 %s｜gid %s｜Σ幾何面積 %.4f ㎡｜聯集 %s"
            % (m.get("街廓"), m.get("命名"), m.get("成員"), m.get("gid"),
               m.get("Σ幾何面積_m2", 0.0), m.get("聯集 geom_type")))
    nameA = {m.get("命名") for m in (A["k6"].get("merged") or [])}
    nameB = {m.get("命名") for m in (B["k6"].get("merged") or [])}
    say("  🔒 **`k6_step0_block_locked` 實際所擋之群**（＝ 僅態 B 有者）= %r"
        % sorted(nameB - nameA))
    say("     僅態 A 有者 = %r（須空）" % sorted(nameA - nameB))
    say("     🔑 上鎖之**街廓** = %r（%d 個），惟其中**有可合併之群**者僅 = %r"
        % (lockedA, len(lockedA),
           sorted({m.get("街廓") for m in (B["k6"].get("merged") or [])
                   if m.get("命名") in (nameB - nameA)})))
    say("     ⇒ 🛑 「**上鎖之街廓數**」與「**實際被擋之群數**」係**二量**，⛔ 互代——"
        "上鎖之街廓中可無任何可合併之群。二數已於上二列分別具名。")
    say("")

    dA, dB = index_diag(A["diag"]), index_diag(B["diag"])

    say("── §三　`R-3`／`R-8`　全域覆蓋與跨占判定（⛔ 得只報有 M 者） ──")
    say("  街廓總數 = **%d**【街廓】／可建築街廓數 = **%d**【街廓】（母體 ＝ `classified_blocks`·"
        "框 ＝ 街廓；可建築 ＝ `F3_CATEGORY_BURDEN[category] == '可建築土地'`）"
        % (len(B["blocks_all"]), len(B["blocks_build"])))
    say("  🔒 **跨占之定義**（碼面·⛔ 本探針自訂）＝ 該宗進入該端之 PK 組，其充要條件為")
    say("     `_corner_intersection_area > 1.0 ㎡`（`E-1.7` 絕對地板·"
        "`grep -n \"_has_p1 = _inter_p1_area > 1.0\" app.py`）")
    say("")
    say("  %-6s %-8s %-10s %-10s %s" % ("街廓", "有無左", "左跨占數", "右跨占數", "同時跨占兩側之宗（＝ M）"))
    Ms = []
    for blk in B["blocks_build"]:
        left = dB.get((blk, SIDE_OF_P1), {})
        right = dB.get((blk, SIDE_OF_P2), {})
        both = sorted(set(left) & set(right))
        for pid in both:
            Ms.append((blk, pid))
        say("  %-6s %-8s %-10d %-10d %s"
            % (blk, ("有" if left else "無"), len(left), len(right),
               (both if both else "⛔ 無 M")))
    say("")
    say("  ⇒ **M 之個數 = %d**【宗】（母體 ＝ 態 B 之可建築街廓 %d 個·框 ＝ 宗）"
        % (len(Ms), len(B["blocks_build"])))
    if not Ms:
        loud("`V-4`：`M` 之個數 ＝ 0 ⇒ 探針未咬到任何受詞 ⇒ 停機上呈（⛔ 自行歸因）")
    say("")

    say("── §四　`R-4`　逐 M 逐側之實算（分別以左／右街角第 1 宗位置試算） ──")
    COLS = ["真交集(㎡)", "整筆幾何(㎡)", "範圍面積(㎡)", "門檻(㎡)", "真G(㎡)",
            "正街角分(0.4)", "側街分(0.2)", "跨占分(0.4)", "總分", "原位次(投影序)"]
    verdicts = []
    for blk, pid in Ms:
        say("")
        say("  ▎街廓 %s ｜ M = %s" % (blk, pid))
        say("    %-16s %-22s %-22s" % ("欄", "【%s】" % SIDE_OF_P1, "【%s】" % SIDE_OF_P2))
        rowL = dB[(blk, SIDE_OF_P1)][pid]
        rowR = dB[(blk, SIDE_OF_P2)][pid]
        for c in COLS:
            say("    %-16s %-22s %-22s" % (c, cell(rowL, c), cell(rowR, c)))
        hold = {}
        for side, row in ((SIDE_OF_P1, rowL), (SIDE_OF_P2, rowR)):
            p, w = is_pass(row), is_winner(row)
            hold[side] = (p and w)
            say("    %-16s %s｜達標 = %s ／ 該側 winner = %s ⇒ **拿得下 = %s**"
                % ("判定", side, p, w, p and w))
        say("    🛑 「拿得下」＝ 達標 ∧ 為該側全部達標候選中指數最大者（＝ winner）；"
            "⛔ 得以「第 1 名」單獨代之")
        verdicts.append((blk, pid, hold, rowL, rowR))

    say("")
    say("── §五　🔒 自我驗證閘 ②：扣除 M 之獨立性（態 C(M) vs 態 B 逐格） ──")
    Cs = {}
    for blk, pid, hold, rowL, rowR in verdicts:
        C = run_state(SB, unconditional_step0=True, drop_pids=frozenset({pid}))
        Cs[(blk, pid)] = C
        dC = index_diag(C["diag"])
        say("  ▎M = %s｜v12 被呼叫 %d【次】／實際扣除 %d【列候選】"
            % (pid, C["v12_calls"]["n"], C["v12_calls"]["dropped"]))
        if C["v12_calls"]["dropped"] < 1:
            loud("扣除層疊未咬到（dropped=%d）⇒ ⛔ 得視為「無其他候選」"
                 % C["v12_calls"]["dropped"])
        ndiff, nsame = 0, 0
        for (kblk, kside), rows in dB.items():
            for kpid, rb in rows.items():
                if kpid == pid:
                    continue
                rc = dC.get((kblk, kside), {}).get(kpid)
                if rc is None:
                    ndiff += 1
                    say("    🔴 態 C 缺格：%s／%s／%s" % (kblk, kside, kpid))
                    continue
                for c in ("總分", "達標", "真G(㎡)"):
                    if cell(rb, c) != cell(rc, c):
                        ndiff += 1
                        say("    🔴 逐格不同：%s／%s／%s／%s：B=%r C=%r"
                            % (kblk, kside, kpid, c, cell(rb, c), cell(rc, c)))
                    else:
                        nsame += 1
        say("    ⇒ 其餘候選之（總分／達標／真G）逐格相同 %d【格】／相異 **%d**【格】" % (nsame, ndiff))
        if ndiff != 0:
            loud("自我驗證閘 ② 不過（相異 %d 格）⇒ 三指數之分母竟依候選集而變 ⇒ "
                 "⛔ 結論不得出艙，停機上呈" % ndiff)
        if nsame == 0:
            loud("自我驗證閘 ② 之對照母體為空（相同 0 格）⇒ **先判量測器紅**（常規五）")
    say("  ⇒ 🔒 **閘 ② 全數通過**（碼面保證：三指數之分母皆取自 range 自身·⛔ 候選集之極值）")

    say("")
    say("── §六　`R-5`　四分支之判讀 ＋ 另一側扣除 M 後之評選 ──")
    for blk, pid, hold, rowL, rowR in verdicts:
        hL, hR = hold[SIDE_OF_P1], hold[SIDE_OF_P2]
        sL, sR = score_of(rowL), score_of(rowR)
        if hL and hR:
            if round(sL, 4) > round(sR, 4):
                br, side_to, why = "2", SIDE_OF_P1, "兩側皆拿得下 ⇒ 歸指數大者"
            elif round(sR, 4) > round(sL, 4):
                br, side_to, why = "2", SIDE_OF_P2, "兩側皆拿得下 ⇒ 歸指數大者"
            else:
                br, side_to, why = "2", SIDE_OF_P1, "兩側皆拿得下且指數並列(4dp) ⇒ 取前緣線 p1 側（決定性·禁隨機）"
        elif hL or hR:
            side_to = SIDE_OF_P1 if hL else SIDE_OF_P2
            br, why = "3", "僅一側拿得下 ⇒ 歸該側（⛔ 論該側指數是否較小）"
        else:
            br, side_to, why = "4", None, "兩側皆拿不下 ⇒ 兩側皆不歸；M 辦原位次"
        say("")
        say("  ▎街廓 %s｜M = %s" % (blk, pid))
        say("    總分：%s = %.6f ／ %s = %.6f（差 %+.6f）" % (SIDE_OF_P1, sL, SIDE_OF_P2, sR, sR - sL))
        say("    拿得下：%s = %s ／ %s = %s" % (SIDE_OF_P1, hL, SIDE_OF_P2, hR))
        say("    ⇒ **分支 %s**：%s ⇒ **歸屬 = %s**"
            % (br, why, (side_to if side_to else "⛔ 歸任一側（辦原位次）")))
        dC = index_diag(Cs[(blk, pid)]["diag"])
        for side in SIDES:
            other = (side != side_to)
            rows = list(dC.get((blk, side), {}).values())
            w, q = pick_winner(rows)
            say("    ── 扣除 M 後之【%s】側（%s）：其餘跨占者 %d【宗】／達標 %d【宗】"
                % (side, ("**operative**：另一側" if (side_to and other) else
                          ("歸屬側·⛔ operative" if side_to else "分支 4 ⇒ 二側皆⛔ operative")),
                   len(rows), len(q)))
            for r in sorted(rows, key=lambda x: -score_of(x)):
                say("        %-14s 真G=%-10s 門檻=%-10s 達標=%-6s 總分=%-10s 原位次=%s"
                    % (cell(r, "候選地號"), cell(r, "真G(㎡)"), cell(r, "門檻(㎡)"),
                       cell(r, "達標"), cell(r, "總分"), cell(r, "原位次(投影序)")))
            if w is None:
                rng = range_area(Cs[(blk, pid)], blk, side)
                thr = float(cell(dB[(blk, side)][pid], "門檻(㎡)"))
                say("        ⇒ **無 winner（含候選集合為空）⇒ 強制留設抵費地**"
                    "，範圍嚴格等於該街角規定範圍：**範圍面積 = %.2f ㎡**（門檻 = %.2f ㎡）"
                    % (rng, thr))
                say("        🔒 範圍面積之源 ＝ `f3_corner_range_areas[%r][%r]`（塊×側級·"
                    "⛔ 依候選集）；與態 B 之 M 列 `範圍面積(㎡)` = %s 對拍 ⇒ **相符 = %s**"
                    % (blk, RANGE_KEY[side], cell(dB[(blk, side)][pid], "範圍面積(㎡)"),
                       abs(rng - float(cell(dB[(blk, side)][pid], "範圍面積(㎡)"))) < 5e-3))
            else:
                say("        ⇒ **winner = %s**（總分 %s·原位次 %s）"
                    % (cell(w, "候選地號"), cell(w, "總分"), cell(w, "原位次(投影序)")))

    say("")
    say("── §七　`R-7`　對照組：態 A（未合併·現行）vs 態 B（無條件合併） ──")
    keysA, keysB = set(dA), set(dB)
    say("  診斷列總數：態 A = %d【列】／態 B = %d【列】（母體 ＝ `_corner_cand_diag`·框 ＝ 列）"
        % (len(A["diag"]), len(B["diag"])))
    say("  (街廓,端) 鍵集：僅 A 有 %r ／ 僅 B 有 %r" % (sorted(keysA - keysB), sorted(keysB - keysA)))
    ndiff_ab = 0
    for k in sorted(keysA & keysB):
        pa, pb = set(dA[k]), set(dB[k])
        onlyA, onlyB = sorted(pa - pb), sorted(pb - pa)
        chg = []
        for pid in sorted(pa & pb):
            for c in ("真G(㎡)", "達標", "總分", "選中", "原位次(投影序)"):
                if cell(dA[k][pid], c) != cell(dB[k][pid], c):
                    chg.append("%s.%s：A=%r→B=%r"
                               % (pid, c, cell(dA[k][pid], c), cell(dB[k][pid], c)))
        ndiff_ab += len(onlyA) + len(onlyB) + len(chg)
        if onlyA or onlyB or chg:
            say("  ▎%s／%s：僅 A 有 %r ／ 僅 B 有 %r" % (k[0], k[1], onlyA, onlyB))
            for s in chg:
                say("       %s" % s)
    say("  ⇒ **合併前 vs 合併後之相異總格數 = %d**（`V-4` 判準：須 **⛔ 為 0**）" % ndiff_ab)
    if ndiff_ab == 0:
        loud("`V-4`：合併前後逐格全同 ⇒ 合併⛔ 改變任何量 ⇒ 停機上呈（⛔ 自行歸因）")

    say("")
    say("── §八　態 A／態 B 之各側指配（`run_corner_pk` 之 `_corner_select_results`） ──")
    for tag, S in (("A", A), ("B", B)):
        say("  ▎態 %s" % tag)
        for r in S["sel"]:
            say("    %-4s 候選數=%-4s ｜【%s】最小面積=%-10s 達資格=%-4s 指配=%-46s 指數=%s"
                % (r.get("街廓"), r.get("候選數"), SIDE_OF_P1,
                   r.get("【左】最小面積(㎡)"), r.get("【左】達資格候選"),
                   r.get("【左】第1宗指配"), r.get("【左】優先權指數")))
            say("    %-4s %-9s ｜【%s】最小面積=%-10s 達資格=%-4s 指配=%-46s 指數=%s"
                % ("", "", SIDE_OF_P2,
                   r.get("【右】最小面積(㎡)"), r.get("【右】達資格候選"),
                   r.get("【右】第1宗指配"), r.get("【右】優先權指數")))

    say("")
    say(BAR)
    say("🛑 總判：閘 ① 層疊生效 = %s ／ 閘 ② 扣除之獨立性 = 全數通過 ／ M 個數 = %d ／ "
        "合併前後相異格數 = %d" % (gate1, len(Ms), ndiff_ab))
    say("🛑 **本探針之數⛔ 得逕作為任何裁之依據**——須經發單側獨立復驗、KL 認可，"
        "方得進入 `K-9-24` 之實例段或任何生產碼。")
    say(BAR)

    name = os.environ.get("WV_OUT_NAME") or ("probe_WG9201_side_assign_%s.log" % head)
    path = os.path.join(OUTDIR, name)
    if os.path.exists(path) and os.environ.get("WV_ALLOW_OVERWRITE") != "1":
        loud("拒絕覆寫既有 log：%s（設 `WV_ALLOW_OVERWRITE=1` 方可）" % path)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(L) + "\n")
    print("\n  ✅ 已落檔：%s" % path, file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
