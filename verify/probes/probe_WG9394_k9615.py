# -*- coding: utf-8 -*-
"""W-G.9-394 量測器（發單端擬·檔 F38·⛔ 由受單側改一字）：`K-9-61` ⑤（已收受道路、公設地上之土地之宗最後未配得者，已併入之
土地回原狀）與 `GB-205`（受併宗含非其成員之受併之土地而須依手冊部分併出 ⇒ 停機）之試算之內之處置。

所量之性質：受併宗含非其成員之受併之土地而於某試算之入池閘中須依手冊部分併出（`GB-205` 之形）⇒ 該試算所代表之配地依
`K-9-61` ⑤（回到收受之前·`K-6` 典「`K-9-65` 之落地之讀法」之讀法九·【工】丑）與 `K-9-48` 其三⛔ 可採——
  ① 候選之試算（併入後）⇒ 該候選不過（段三之「不影響原位次」之判、手冊先行、第一趟皆然）；
  ② 現態、併入前、定案之試算 ⇒ 照舊停機（⛔ 記為試算中止而續辦·末端塊合併再試之現態之試算亦然）；
  ③ 他之帶號之停機（`GB-104` 等、【未裁】）照舊上拋（`W-G.9-389`）。
本案二退縮⛔ 觸 `GB-205` 之形；最後之配地中，段三、末端塊合併再試、手冊先行、第一趟之受併宗皆配得（`K-9-61` ⑤ 之受詞為空）。

子命令（一律 python3 verify/probes/probe_WG9394_k9615.py <子命令> …）：
  selftest <repo>
           合成對照（⛔ 讀本案資料·`harvest(app.py)` 取諸函式·期值皆手算或取自既有之器之手算之註）。
           T1 新登記唯 `GB-205` ⇒ `k6_trial_raise_since` 回 None（⛔ 上拋）；T1b 同而 `adopted=True` ⇒ 上拋 `GB-205`；
           T1c `adopted=True` 而無新登記 ⇒ None；T2 `GB-205` 繼以 `GB-104` ⇒ 上拋 `GB-104` 之全文；
           T3 `GB-104` 繼以 `GB-205` ⇒ 上拋 `GB-104`；T4 `GB-2050`（號之邊界）⇒ 上拋；T5 【未裁】⇒ 上拋；T6 無新登記 ⇒ None；
           T7 mark 之前之登記（`GB-104`）⛔ 計 ⇒ None；
           T8 入池閘（`k929_6_fixpoint`·`F29` K56 之玩具：單片 U 含非其成員之土地 15 而部分併入街角第 1 宗 C 過檢核）於候選之
              試算之殼之內（mark → 試算 → 中止 → `k6_trial_raise_since`）⇒ 中止之訊息含「GB-205」、登記恰增一、殼⛔ 上拋；
           T9 段三（`k6b_stage3_run`·`F34` 之 L2 之玩具·門檻 150）：A1(1) 之 ②（＋道路片 A9(1) ⇒ 160）之併入後之試算以
              `GB-205` 中止 ⇒ A1(1) 未成（檢核 不過）、B1(1) 之 ①（＋B2(1) ⇒ 155）成、⛔ 停機；T9b 同而其中止為 `GB-104` ⇒ 停機（訊息含 GB-104）；T9c 同而其中止
              無號 ⇒ 停機（「無從判定」·照舊）；T9d 併入前之試算以 `GB-205` 中止 ⇒ 停機（「無從判定」）；T9e 併入前、後之
              試算皆以 `GB-205` 中止 ⇒ 停機（其訊息含「不影響原位次」與「無從判定」·⛔ 判為不過）；
           T10 末端塊合併再試（`end_block_merge_run`）之現態之試算以 `GB-205` 中止 ⇒ 停機（訊息含「末端塊合併再試·現態之試算」與 GB-205）；
               T10b 其中止無號 ⇒ ⛔ 停機（記「試算中止」而回·照舊）；
           T11 T9 之換名、左右鏡射、旋轉 37° 並移至 TWD97 之尺度 ⇒ 同 T9。
           🔧 `W-G.9-394` 補令一（審查之 W-1／W-2·`K-6` 典 `W-G.9-394` 補令一之節）：
           T12 段三 `K-9-50` 題一 4（`F34` 之 L6／L14 之玩具·門檻 145）：只 F1(1) 之端成（150）而 A1(1) 連同其半（140）⛔ 能依
               原位次配地 ⇒ 其「連同其半併入已取得之一端」（併入 F1(1)）之試算以 `GB-205` 中止（F1(1) 之 G ＞ 200）⇒ 不過（⛔ 停機）
               ⇒ `K-9-66`（題一 4 之列）：建地 A1(1) 按比例部分併入 50（＝ 200 − 150）、道路片 D(1) 未成；F1(1) 之 G ＝ 200；
           T12b T12 之換名、左右鏡射、旋轉 37° 並移至 TWD97 之尺度 ⇒ 同 T12；
           T13 段三後處理 (b)（`F34` 之 L7 之玩具）：A1(1) 之 ①（160）成後，同一地主之道路片 A9(1)（40）之併入之試算以
               `GB-205` 中止（A1(1) 之 G ＞ 180）⇒ 不過 ⇒ `K-9-66` 按比例部分併入 20（＝ 180 − 160）；A1(1) 之 G ＝ 180；
           T13b 同而觸發 ＝ G ＞ 200（全併恰 200·門檻上）⇒ 全併（成·40）；T13c 同而觸發 ＝ G ＞ 160（任一格即觸）⇒ 未成（0）；
           T14 手冊先行（`F27` 之 K16 之玩具·其中止改以 `GB-205` 之登記致·其結果之形 ＝ `F27` K16〔`F27` 唯斷言其形〕·其量為本器之手算）：整批不過 ⇒ 建地 X1(1)
               成（60）、道路片 R1(1) 按比例部分併入 40（＝ 100 − 60）、其餘入合併單位。
           （判別力之證 ＝ 單之突變之表〔發單端施於其原型〕與主線 `5d2a283` 之紅·本器⛔ 含突變。）
  wiring   <repo> <基準 commit>
           W1 `app.py` 之頂層之名⛔ 增減；頂層節點之相異 ＝ `{k6_trial_raise_since, k6b_stage3_run, end_block_merge_run,
              k953_manual_run}`；
           W2 `k6_trial_raise_since` 內（docstring 除外）之 `GB-` 之號之字面恰 `{GB-205}`（⛔ 他號免於上拋）；
           W3 `k6b_stage3_run` 之巢狀 `_noaff`：二 `alloc_state` 之呼叫之間有 `<名> = k6_trial_mark()`，且有 `if`（其判引
              `K6_PROGRAM_STOPS`）之體為 `return False`；
           W4 `end_block_merge_run` 內有 `k6_trial_raise_since(…, adopted=True)` 之呼叫（現態之試算 ⇒ 停機）；
           W5 `k929_6_fixpoint` 對基準⛔ 變、其內 `raise k6_program_stop(…)` 而其訊息含「GB-205」者恰一；
           W6 所改之頂層節點內⛔ 新增案件字面；W7 `verify/` 頂層之 `*.py` 對基準相異 0；
           W8 `k953_manual_run` 內有 `k6_trial_raise_since(…, adopted=True)` 之呼叫（R-5 之取代之試算·非候選 ⇒ 停機）。
  run      <repo> [<退縮> …]
           harness 實跑本案（預設退縮 `3.5`、`0.0`·`run_corner_pk_k6b` ＋ `run_step_g`）：
           R1 `err` 為 None；`k965_part_split` 之回 None（宗含非其成員之土地）之次數 ＝ 0；程式之停機之登記之增 ＝ 0；
           R2 段三、末端塊合併再試、手冊先行、第一趟之受併宗（切片之 `段三併出` 之列與 `段三部分併出` 之鍵·其數出艙）⛔ 空，
              且皆為最後之配地之保留之宗（`驗_總判` ＝ 保留）——`K-9-61` ⑤ 之受詞於本案為空。
🔧 `W-G.9-395`（`K-9-60` ①③·⛔ 上列一字不刪）：其後之單所改之頂層節點 `end_block_apply` 亦許（W1 之相異 ＝ 上之四 ∪
  `{end_block_apply}`·其行為與接線由 F39 量之）。
rc：0 相符／1 不符／2 用法錯。
"""
import ast, contextlib, copy, io, os, re, subprocess, sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:  # noqa: BLE001
    pass

CASE_LIT_RE = re.compile(r"^(R|RD|G)\d+$|^G\d{3}$|^\d{3}(-\d+)*(\(\d+\))?$")
GB_RE = re.compile(r"(?<![0-9A-Za-z\-])GB-\d+(?![0-9])")
CHG_TOP = {"k6_trial_raise_since", "k6b_stage3_run", "end_block_merge_run", "k953_manual_run"}
W395 = {"end_block_apply"}      # 🔧 `W-G.9-395`：其後之單所改之頂層節點（F39 量之·⛔ 新名）
NEW398, W398 = {"RW_TABLE_25"}, {"rw_from_width"}   # 🔧 `W-G.9-398`：其後之單之新常數與所改之函式（側面道路負擔百分率之附表 25·F41 量之）
NEED = ["k6_program_stop", "k6_trial_mark", "k6_trial_raise_since", "K6_PROGRAM_STOPS", "k929_6_fixpoint",
        "k6b_stage3_run", "end_block_merge_run"]
TWD = (37.0, True, (302512.0, 2650318.0))
# 🔧 補令一：玩具之觸發之容差（㎡）——TWD97 之尺度之旋轉使道路片之切半之面積之浮點之差約 1.3e-9（發單端實量）；
#   K-9-66 之格 0.01 ≫ 1e-6 ≫ 其差 ⇒ 格之判⛔ 受影響
EPS12 = 1e-6


def _harvest(repo):
    sys.path.insert(0, os.path.join(repo, "verify"))
    probes = os.path.join(repo, "verify", "probes")
    if probes not in sys.path:
        sys.path.insert(0, probes)
    from app_harvest import harvest
    with contextlib.redirect_stdout(io.StringIO()):
        ns, fake_st = harvest(os.path.join(repo, "app.py"))
    return ns, fake_st


# ───────────────────────── selftest ─────────────────────────

def _since(ns, regs, pre=(), **kw):
    """mark 前登記 pre、mark 後登記 regs ⇒ `k6_trial_raise_since` 之果：None 或 ('上拋', 全文)。"""
    for m in pre:
        ns["k6_program_stop"](m)
    mk = ns["k6_trial_mark"]()
    for m in regs:
        ns["k6_program_stop"](m)
    try:
        return ns["k6_trial_raise_since"](mk, "合成", **kw)
    except RuntimeError as e:
        return ("上拋", str(e))


def _first(r):
    if isinstance(r, tuple) and r[0] == "上拋":
        return ("上拋", [g for g in GB_RE.findall(r[1])] + (["【未裁】"] if "【未裁】" in r[1] else []))
    return r


def _k56(ns):
    # 取自 `F29`（`probe_WG9375_k965.py`）K56 之玩具（其註之手算：單片 U〔分攤 60·段三部分併出 20〕之 面積_m2 −5 ⇒ 含受併之
    #   土地 15；整筆不過、部分 v ≤ 48.33 ⇒ 過檢核 ⇒ GB-205）
    import probe_WG9375_k965 as F29
    mk, BLK = F29.mk, F29.BLK
    own56 = {"ou": "GA", "o9": "GZ", "o5": "GA"}
    u = dict(mk("U", "ou", "A", 60, 0, 10), 面積_m2=-5.0, 段三部分併出={"s": 20.0})
    tp = [dict(mk("U", "ou", "A", 60, 0, 10), 段三部分併出={"s": 20.0}), mk("Z9", "o9", "A", 400, 10, 20),
          mk("C", "o5", "A", 300, 20, 30)]
    b = [u, mk("Z9", "o9", "A", 400, 10, 20), mk("C", "o5", "A", 300, 20, 30)]
    return F29._fx_raw(ns, b, own56, {"A": BLK(split_x=20.0, corner={"C"}, cap=260.003 + 240.0)}, temp=tp)


def _t8(ns):
    n0 = len(ns["K6_PROGRAM_STOPS"])
    mk = ns["k6_trial_mark"]()
    err = None
    try:
        _k56(ns)
    except RuntimeError as e:
        err = str(e).split("\n")[0]
    try:
        ns["k6_trial_raise_since"](mk, "合成·候選之試算")
        shell = "⛔ 上拋"
    except RuntimeError:
        shell = "上拋"
    new = ns["K6_PROGRAM_STOPS"][n0:]
    return (bool(err and "GB-205" in err), len(new), bool(new and "GB-205" in new[0]), shell)


def _go394(ns, kind, *, before=False, T=(0.0, False, (0.0, 0.0)), names=None):
    """`F34` 之 `_go` 之變體（其 L2 之玩具：BA 之 g1 之 A1(1)[0,10]〔100〕與其道路片 A9(1)〔RD·x∈[0,10]·60〕、g2 之
    B1(1)[10,20]〔100〕／B2(1)[20,30]〔55〕、g3 之 C1(1)[30,50]〔300〕；門檻 150）：alloc_state 於「A1(1) 之 G ＞ 150」（A1(1) 之 ②
    之併入後）〔before ⇒「A1(1)、B1(1) 之 G 皆 ＝ 100 而 B2(1) 在 build」（併入前）〕之試算以 kind（'GB-205'／'GB-104'／
    None〔無號〕）中止——其殼同畫面與 harness（mark → 中止 → raise_since）。"""
    import probe_WG9390_k961r as F34
    nm = names or {}
    inv = {v: k for k, v in nm.items()}
    H, RDC, R = F34.H, F34.RDC, F34._R
    p1 = [("A1(1)", "BA", H, R(0, 10, 0, 30), 100), ("A9(1)", "RD", RDC, R(0, 10, -10, 0), 60),
          ("B1(1)", "BA", H, R(10, 20, 0, 30), 100), ("B2(1)", "BA", H, R(20, 30, 0, 30), 55),
          ("C1(1)", "BA", H, R(30, 50, 0, 30), 300)]
    own1 = {"A1": "g1", "A9": "g1", "B1": "g2", "B2": "g2", "C1": "g3"}
    od1 = F34._O(("BA", "左", "A1(1)"), ("BA", "左", "B1(1)"))
    temp, own2, blocks, cl = F34._world(p1, own1, T, names)
    build = [t for t in temp if t["街廓分類"] == F34.H]

    def back(pid):
        base, _, rest = pid.partition("(")
        return inv.get(base, base) + "(" + rest

    def hit(gm):
        if before == "always":
            return True
        if before:
            return abs(gm.get("A1(1)", 0.0) - 100.0) < 1e-9 and abs(gm.get("B1(1)", 0.0) - 100.0) < 1e-9 and "B2(1)" in gm
        return gm.get("A1(1)", 0.0) > 150.0

    def alloc_state(temp_, build_):
        gm = {back(b["暫編地號"]): F34._g(b) for b in build_}
        if hit(gm):
            mk = ns["k6_trial_mark"]()
            if kind is None:
                err = "合成之配地中止"
            else:
                try:
                    raise ns["k6_program_stop"](f"🔴 合成之停機（{kind}）⇒ 停機")
                except RuntimeError as e:
                    err = str(e)
            ns["k6_trial_raise_since"](mk, "合成·段三之試算")
            return {"kept": {}, "bad_pools": {}, "err": err, "G": {}}
        kept, G = {}, {}
        for b in build_:
            kept.setdefault(b["所屬街廓"], set()).add(b["暫編地號"])
            G[b["暫編地號"]] = F34._g(b)
        return {"kept": kept, "bad_pools": {}, "err": None, "G": G}

    def trial_winner(temp_, build_, blk, end, cand):
        by = {b["暫編地號"]: b for b in build_}
        gg = F34._g(by[cand]) if cand in by else 0.0
        return (cand if gg >= 150.0 else None), round(gg, 2), 150.0

    od = [dict(r, 街廓=nm.get(r["街廓"], r["街廓"]),
               暫編地號=nm.get(r["暫編地號"].partition("(")[0], r["暫編地號"].partition("(")[0]) + "(" + r["暫編地號"].partition("(")[2])
          for r in od1]
    try:
        _t2, _b2, log = ns["k6b_stage3_run"](od, set(), own2, temp, build, blocks, cl, lambda s, d: F34._g(s), trial_winner,
                                             alloc_state, log_print=lambda *x: None, blk5=lambda: {})
    except RuntimeError as e:
        return ("停機", str(e))
    return tuple((back(r["候選"]), r["結果"], r.get("層級"), r.get("檢核")) for r in log if r.get("序") != "後處理")


def _halt(r, *must):
    return (r[0], all(m in r[1] for m in must)) if isinstance(r, tuple) and r and r[0] == "停機" else r


def _t10(ns, kind):
    def alloc_eval(temp_, build_):
        if kind is None:
            raise RuntimeError("合成之配地中止")
        raise ns["k6_program_stop"](f"🔴 合成之停機（{kind}）⇒ 停機")
    try:
        _t, _b, _l, rec = ns["end_block_merge_run"]([], [], {}, set(), set(), {}, {}, lambda s, d: 0.0, alloc_eval,
                                                    lambda t, b: {}, log_print=lambda *x: None, blk5=lambda: {})
    except RuntimeError as e:
        return ("停機", "末端塊合併再試·現態之試算" in str(e) and (kind is None or kind in str(e)))
    return ("回", rec.get("標的"), bool(rec.get("試算中止")))


def _stop205(ns, where):
    """試算之殼之替身（同畫面與 harness：mark → 帶 `GB-205` 之登記 → raise_since）·回中止之訊息。"""
    mk = ns["k6_trial_mark"]()
    try:
        raise ns["k6_program_stop"]("🔴 合成之停機（GB-205）⇒ 停機")
    except RuntimeError as e:
        err = str(e)
    ns["k6_trial_raise_since"](mk, where)
    return err


def _s3go(ns, parcels, own, od1, thr, drop, trig, *, contests=None, T=(0.0, False, (0.0, 0.0)), names=None):
    """🔧 補令一：`F34` 之 `_go` 之變體——alloc_state 於 trig(G 之表) 為真時以 `GB-205` 之登記中止（其殼同畫面與 harness）；
    drop(pid, G) 為真者⛔ 保留。回 (後處理之列 (候選, 層級, 結果, 受併宗, 併入量 2 位), {宗: G})；停機 ⇒ ('停機', 訊息)。"""
    import probe_WG9390_k961r as F34
    nm = names or {}
    inv = {v: k for k, v in nm.items()}
    temp, own2, blocks, cl = F34._world(parcels, own, T, names)
    build = [t for t in temp if t["街廓分類"] == F34.H]

    def back(pid):
        base, _, rest = pid.partition("(")
        return inv.get(base, base) + "(" + rest

    def alloc_state(temp_, build_):
        gm = {back(b["暫編地號"]): F34._g(b) for b in build_}
        if trig(gm):
            return {"kept": {}, "bad_pools": {}, "err": _stop205(ns, "合成·段三之試算"), "G": {}}
        kept, G = {}, {}
        for b in build_:
            if drop(back(b["暫編地號"]), F34._g(b)):
                continue
            kept.setdefault(b["所屬街廓"], set()).add(b["暫編地號"])
            G[b["暫編地號"]] = F34._g(b)
        return {"kept": kept, "bad_pools": {}, "err": None, "G": G}

    def trial_winner(temp_, build_, blk, end, cand):
        by = {b["暫編地號"]: b for b in build_}
        gg = F34._g(by[cand]) if cand in by else 0.0
        return (cand if gg >= thr else None), round(gg, 2), thr

    def fw(p):
        base, _, rest = p.partition("(")
        return nm.get(base, base) + "(" + rest
    od = [dict(r, 街廓=nm.get(r["街廓"], r["街廓"]), 暫編地號=fw(r["暫編地號"])) for r in od1]
    ct = None
    if contests:
        ct = [{"形": c["形"], "列": [(nm.get(b, b), e, fw(p), a) for b, e, p, a in c["列"]]} for c in contests]
    try:
        t2, _b2, log = ns["k6b_stage3_run"](od, set(), own2, temp, build, blocks, cl, lambda s, d: F34._g(s), trial_winner,
                                            alloc_state, log_print=lambda *x: None, blk5=lambda: {}, contests=ct)
    except RuntimeError as e:
        return ("停機", str(e).split("\n")[0][:300])
    post = []
    for r in log:
        if r.get("序") != "後處理":
            continue
        rv = r.get("受併宗")
        post.append((back(r["候選"]), r.get("層級"), r.get("結果"), back(rv) if isinstance(rv, str) and rv != "—" else rv,
                     round(sum(float(v) for v in (r.get("併入量") or {}).values()), 2)))
    return post, {back(t["暫編地號"]): round(F34._g(t), 2) for t in t2}


def _t12(ns, T=(0.0, False, (0.0, 0.0)), names=None):
    # `F34` 之 L6／L14 之地：BA 之 g1 之 A1(1)[0,10]（100）、他人 M(1)；BB 之 g1 之 F1(1)（110）、他人 N(1)；g1 之道路片 D(1)
    #   （RD·x∈[0,10]·80·依中心線分北半、南半各 40）；競合（題一）
    import probe_WG9390_k961r as F34
    H, RDC, R = F34.H, F34.RDC, F34._R
    p = [("A1(1)", "BA", H, R(0, 10, 0, 30), 100), ("M(1)", "BA", H, R(10, 50, 0, 30), 500),
         ("D(1)", "RD", RDC, R(0, 10, -10, 0), 80),
         ("F1(1)", "BB", H, R(0, 10, -40, -10), 110), ("N(1)", "BB", H, R(10, 50, -40, -10), 500)]
    own = {"A1": "g1", "D": "g1", "F1": "g1", "M": "g9", "N": "g8"}
    ct = [{"形": "一", "列": [("BA", "左", "A1(1)", 30.0), ("BB", "左", "F1(1)", 20.0)]}]
    r = _s3go(ns, p, own, F34._O(("BA", "左", "A1(1)"), ("BB", "左", "F1(1)")), 145.0,
              lambda pid, g: pid == "A1(1)" and g > 100.0 + EPS12, lambda gm: gm.get("F1(1)", 0.0) > 200.0 + EPS12,
              contests=ct, T=T, names=names)
    if r and r[0] == "停機":
        return r
    post, G = r
    return [x for x in post if x[1] == "題一 4"], G.get("F1(1)")


def _t13(ns, t):
    # `F34` 之 L7 之地：g1 之 A1(1)[0,10]（100）／A2(1)[10,20]（60）、道路片 A9(1)（RD·x∈[0,10]·40）、他人 M(1)
    import probe_WG9390_k961r as F34
    H, RDC, R = F34.H, F34.RDC, F34._R
    p = [("A1(1)", "BA", H, R(0, 10, 0, 30), 100), ("A2(1)", "BA", H, R(10, 20, 0, 30), 60),
         ("A9(1)", "RD", RDC, R(0, 10, -10, 0), 40), ("M(1)", "BA", H, R(20, 50, 0, 30), 500)]
    own = {"A1": "g1", "A2": "g1", "A9": "g1", "M": "g9"}
    r = _s3go(ns, p, own, F34._O(("BA", "左", "A1(1)")), 150.0, lambda pid, g: False,
              lambda gm: gm.get("A1(1)", 0.0) > t + EPS12)
    if r and r[0] == "停機":
        return r
    post, G = r
    return [x for x in post if x[1] == "後處理(b)"], G.get("A1(1)")


def _t14(ns):
    # `F27` 之 K16 之玩具（世界一·`own_upd={"C1": "gC1"}`·去 P1(1)·BB 之受併 ＞ 100 ⇒ 中止），其中止改為 `GB-205` 之登記
    import probe_WG9363_k953 as F27
    F27._NS["fn"] = F27._fn384(ns[F27.FN])
    orig = F27._cbs

    def cbs205(*a, **k):
        ap, st = orig(*a, **k)

        def st2(temp, build):
            r = st(temp, build)
            if r.get("err"):
                r = dict(r, err=_stop205(ns, "合成·手冊先行之試算"))
            return r
        return ap, st2
    F27._cbs = cbs205
    try:
        return F27._rows(F27._go(F27._w1, own_upd={"C1": "gC1"}, rm=("P1(1)",), err_cap={"BB": 100.0}))
    except RuntimeError as e:
        return ("停機", str(e).split("\n")[0][:300])
    finally:
        F27._cbs = orig


def _cases(ns):
    out = []

    def run(name, fn, exp):
        try:
            got = fn()
        except Exception as ex:  # noqa: BLE001
            got = ("例外", type(ex).__name__, str(ex)[:200])
        out.append((name, got, exp))

    G205, G104 = "🔴 合成（GB-205）⇒ 停機", "🔴 合成（GB-104）⇒ 停機"
    run("T1 新登記唯 GB-205 ⇒ None", lambda: _first(_since(ns, [G205])), None)
    run("T1b 新登記唯 GB-205 而 adopted ⇒ 上拋 GB-205", lambda: _first(_since(ns, [G205], adopted=True)), ("上拋", ["GB-205"]))
    run("T1c adopted 而無新登記 ⇒ None", lambda: _first(_since(ns, [], adopted=True)), None)
    run("T2 GB-205 繼以 GB-104 ⇒ 上拋 GB-104", lambda: _first(_since(ns, [G205, G104])), ("上拋", ["GB-104"]))
    run("T3 GB-104 繼以 GB-205 ⇒ 上拋 GB-104", lambda: _first(_since(ns, [G104, G205])), ("上拋", ["GB-104"]))
    run("T4 GB-2050 ⇒ 上拋", lambda: _first(_since(ns, ["🔴 合成（GB-2050）⇒ 停機"])), ("上拋", ["GB-2050"]))
    run("T5 【未裁】⇒ 上拋", lambda: _first(_since(ns, ["🔴 合成【未裁】⇒ 停機"])), ("上拋", ["【未裁】"]))
    run("T6 無新登記 ⇒ None", lambda: _first(_since(ns, [])), None)
    run("T7 mark 之前之登記⛔ 計 ⇒ None", lambda: _first(_since(ns, [], pre=[G104])), None)
    run("T8 入池閘之 GB-205 於候選之試算之殼 ⇒ 中止之訊息含 GB-205·登記增一·殼⛔ 上拋", lambda: _t8(ns), (True, 1, True, "⛔ 上拋"))
    # 手算：A1(1) 之 ② ＝ 100 ＋ 60 ＝ 160 ≥ 150 而其併入後之試算以 GB-205 中止 ⇒ 未成（檢核 不過·K-9-61 ⑤ 回到收受之前）；
    #   次名 B1(1) 之 ① ＝ 100 ＋ 55 ＝ 155 ≥ 150 ⇒ 成（同街廓相鄰之 ① 免檢核）
    exp9 = (("A1(1)", "未成", "②", "不過"), ("B1(1)", "成", "①", "免"))
    run("T9 段三：A1(1) 之 ② 之併入後之試算以 GB-205 中止 ⇒ A1(1) 未成（不過）、B1(1) 成", lambda: _go394(ns, "GB-205"), exp9)
    run("T9b 其中止為 GB-104 ⇒ 停機", lambda: _halt(_go394(ns, "GB-104"), "GB-104"), ("停機", True))
    run("T9c 其中止無號 ⇒ 停機（無從判定·照舊）", lambda: _halt(_go394(ns, None), "無從判定"), ("停機", True))
    run("T9d 併入前之試算以 GB-205 中止 ⇒ 停機（無從判定）", lambda: _halt(_go394(ns, "GB-205", before=True), "不影響原位次", "無從判定", "GB-205"),
        ("停機", True))
    run("T9e 併入前、後之試算皆以 GB-205 中止 ⇒ 停機（無從判定·⛔ 判為不過）",
        lambda: _halt(_go394(ns, "GB-205", before="always"), "不影響原位次", "無從判定", "GB-205"), ("停機", True))
    run("T10 末端塊合併再試之現態之試算以 GB-205 中止 ⇒ 停機", lambda: _t10(ns, "GB-205"), ("停機", True))
    run("T10b 其中止無號 ⇒ 記試算中止而回（照舊）", lambda: _t10(ns, None), ("回", None, True))
    nm = {"A1": "QX7", "A9": "QX9", "B1": "PW3", "B2": "PW4", "C1": "ZZ1", "BA": "街甲", "BB": "街乙", "RD": "路丙",
          "g1": "主一", "g2": "主二", "g3": "主三"}
    run("T11 T9 之換名、鏡射、旋轉 37°、TWD97 ⇒ 同 T9", lambda: _go394(ns, "GB-205", T=TWD, names=nm), exp9)
    # 🔧 補令一：手算——F1(1) 之 ②半 ＝ 110 ＋ 40 ＝ 150 ≥ 145（成）、A1(1) 之 ②半 ＝ 100 ＋ 40 ＝ 140 ＜ 145（未成）；題一 4：A1(1)
    #   連同其半（140）⛔ 保留 ⇒ 併入 F1(1)（150 ＋ 140 ＝ 290 ＞ 200 ⇒ GB-205 ⇒ 不過）⇒ K-9-66：建地 A1(1) 全量（250）不過、
    #   按比例（0.01 之格）之最大 ＝ 200 − 150 ＝ 50.00（200 ⛔ ＞ 200）、道路類⛔ 併（建地類已按比例）⇒ D(1) 未成；F1(1) ＝ 200
    exp12 = ([("A1(1)", "題一 4", "部分成", "F1(1)", 50.0), ("D(1)", "題一 4", "未成", "F1(1)", 0.0)], 200.0)
    run("T12 題一 4 之「連同其半併入已取得之一端」之試算以 GB-205 中止 ⇒ 不過 ⇒ K-9-66 按比例（⛔ 停機）",
        lambda: _t12(ns), exp12)
    nm12 = {"A1": "KQ3", "D": "KQ8", "F1": "LW5", "M": "MM9", "N": "NN9", "BA": "街丙", "BB": "街丁", "RD": "路戊",
            "g1": "主四", "g8": "主八", "g9": "主九"}
    run("T12b T12 之換名、鏡射、旋轉 37°、TWD97 ⇒ 同 T12", lambda: _t12(ns, T=TWD, names=nm12), exp12)
    # 手算：A1(1) 之 ① ＝ 100 ＋ 60 ＝ 160（成·免）；後處理 (b) 道路片 A9(1)（40）⇒ A1(1)：觸發 G ＞ t；t ＝ 180 ⇒ 最大 20.00；
    #   t ＝ 200 ⇒ 全併 40（200 ⛔ ＞ 200）；t ＝ 160 ⇒ 0.01 即觸 ⇒ 未成
    run("T13 段三後處理 (b) 之道路片之併入以 GB-205 中止 ⇒ 不過 ⇒ K-9-66 按比例 20",
        lambda: _t13(ns, 180.0), ([("A9(1)", "後處理(b)", "部分成", "A1(1)", 20.0)], 180.0))
    run("T13b 觸發 ＝ G ＞ 200（全併恰在門檻上）⇒ 全併 40", lambda: _t13(ns, 200.0),
        ([("A9(1)", "後處理(b)", "成", "A1(1)", 40.0)], 200.0))
    run("T13c 觸發 ＝ G ＞ 160（任一格即觸）⇒ 未成", lambda: _t13(ns, 160.0),
        ([("A9(1)", "後處理(b)", "未成", "A1(1)", 0.0)], 160.0))
    # 結果之形 ＝ `F27`（`probe_WG9363_k953.py`）K16（`F27` 唯斷言其形）；其量之手算：BB 之受併 ＞ 100 ⇒ 中止；X1(1) 60 ＋ R1(1) 100 ＝ 160 ⇒ 整批不過；
    #   建地 X1(1) 60（成）；道路 R1(1) 全量 160 ＞ 100 ⇒ 按比例最大 40.00；其餘 60 ⇒ K-9-51 ⇒ 無 ⇒ 入合併單位
    run("T14 手冊先行之候選之併入後之試算以 GB-205 中止 ⇒ 不過 ⇒ K-9-66（＝ F27 K16 之形·⛔ 停機）", lambda: _t14(ns),
        ([("手冊", "X1(1)", "a", "X1(2)", (("X1(2)", 60.0),), "成"),
          ("手冊", "R1(1)", "b", "X1(2)", (("X1(2)", 40.0),), "部分成"),
          ("K-9-51", "R1(1)", "b", "—", (), "入合併單位")]))
    return out


def selftest(repo):
    ns, _ = _harvest(repo)
    miss = [n for n in NEED if n not in ns]
    if miss:
        print(f"  🔴 受詞缺 {miss}")
        print("⇒ 紅 ['受詞缺']；rc 1")
        return 1
    red = []
    for name, got, exp in _cases(ns):
        ok = got == exp
        print(("  ✅ " if ok else "  🔴 ") + name)
        if not ok:
            print(f"       得 {got!r}"[:700])
            print(f"       期 {exp!r}"[:700])
            red.append(name.split()[0])
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


# ───────────────────────── wiring ─────────────────────────

def _git(repo, *a):
    r = subprocess.run(["git", "-C", repo, *a], capture_output=True)
    return r.stdout if r.returncode == 0 else None


def _fn_node(tree, name):
    for n in tree.body:
        if isinstance(n, ast.FunctionDef) and n.name == name:
            return n
    return None


def _top(src):
    out = {}
    for n in ast.parse(src).body:
        if isinstance(n, (ast.FunctionDef, ast.ClassDef, ast.AsyncFunctionDef)):
            out[n.name] = ast.dump(n)
        elif isinstance(n, ast.Assign):
            for t in n.targets:
                if isinstance(t, ast.Name):
                    out[t.id] = ast.dump(n)
    return out


def _strs(node):
    return [c.value for c in ast.walk(node) if isinstance(c, ast.Constant) and isinstance(c.value, str)]


def _names(node):
    return {x.id for x in ast.walk(node) if isinstance(x, ast.Name)}


def _callname(c):
    return getattr(c.func, "id", None) if isinstance(c, ast.Call) else None


def _adopted(fn):
    if fn is None:
        return -1
    return sum(1 for x in ast.walk(fn) if isinstance(x, ast.Call) and _callname(x) == "k6_trial_raise_since"
               and any(k.arg == "adopted" and isinstance(k.value, ast.Constant) and k.value.value is True for k in x.keywords))


def wiring(repo, base):
    src = open(os.path.join(repo, "app.py"), encoding="utf-8").read()
    old_b = _git(repo, "show", f"{base}:app.py")
    if not old_b:
        print(f"  🔴 基準 {base} 之 app.py 取不到")
        print("⇒ 紅 ['基準缺']；rc 1")
        return 1
    old = old_b.decode("utf-8")
    ta = ast.parse(src)
    red = []

    def rep(tag, ok, msg):
        print(("  ✅" if ok else "  🔴") + f" {tag} {msg}")
        if not ok:
            red.append(tag)
    # W1
    tb, tn = _top(old), _top(src)
    add, rem = set(tn) - set(tb), set(tb) - set(tn)
    chg = {k for k in tn if k in tb and tn[k] != tb[k]}
    rep("W1", add in (set(), NEW398) and not rem and chg in (CHG_TOP, CHG_TOP | W395, CHG_TOP | W395 | W398), f"頂層之名之增 {sorted(add)}·減 {sorted(rem)}·相異之節點 {sorted(chg)}")   # 🔧 `W-G.9-398`：其後之單之許
    # W2
    rs = _fn_node(ta, "k6_trial_raise_since")
    gb2 = None
    if rs:
        body2 = rs.body[1:] if (rs.body and isinstance(rs.body[0], ast.Expr) and isinstance(rs.body[0].value, ast.Constant)
                                and isinstance(rs.body[0].value.value, str)) else rs.body
        gb2 = sorted({g for st in body2 for s in _strs(st) for g in re.findall(r"GB-\d+", s)})
    rep("W2", gb2 == ["GB-205"], f"k6_trial_raise_since 內之號之字面 {gb2}")
    # W3
    s3 = _fn_node(ta, "k6b_stage3_run")
    na = None
    ok3 = False
    if s3:
        for d in ast.walk(s3):
            if isinstance(d, ast.FunctionDef) and d.name == "_noaff":
                na = d
        if na is not None:
            seq = []
            for st in na.body:
                for x in ast.walk(st):
                    if isinstance(x, ast.Call) and _callname(x) in ("alloc_state", "k6_trial_mark"):
                        seq.append((x.lineno, x.col_offset, _callname(x)))
            seq.sort()
            kinds = [k for _, _, k in seq]
            mid = len(kinds) >= 3 and kinds[0] == "alloc_state" and "k6_trial_mark" in kinds[1:kinds.index("alloc_state", 1)] \
                if kinds.count("alloc_state") >= 2 else False
            ret = any(isinstance(x, ast.If) and "K6_PROGRAM_STOPS" in _names(x.test)
                      and any(isinstance(b, ast.Return) and isinstance(b.value, ast.Constant) and b.value.value is False
                              for b in x.body) for x in ast.walk(na))
            ok3 = bool(mid and ret)
    rep("W3", ok3, f"_noaff 之二試算之間之 mark 與「新登記 ⇒ return False」（_noaff {'有' if na is not None else '無'}）")
    # W4
    eb = _fn_node(ta, "end_block_merge_run")
    n4 = _adopted(eb)
    rep("W4", n4 >= 1, f"end_block_merge_run 之 `k6_trial_raise_since(…, adopted=True)` {n4}")
    # W8
    km = _fn_node(ta, "k953_manual_run")
    n8 = _adopted(km)
    rep("W8", n8 >= 1, f"k953_manual_run 之 `k6_trial_raise_since(…, adopted=True)` {n8}")
    # W5
    fx = _fn_node(ta, "k929_6_fixpoint")
    hits = [x for x in ast.walk(fx) if isinstance(x, ast.Raise) and _callname(x.exc) == "k6_program_stop"
            and any("GB-205" in s for s in _strs(x.exc))] if fx else []
    ok5 = len(hits) == 1 and tn.get("k929_6_fixpoint") == tb.get("k929_6_fixpoint")
    rep("W5", ok5, f"k929_6_fixpoint 之 `raise k6_program_stop(…GB-205…)` {len(hits)}（期 1）·對基準⛔ 變 {ok5}")
    # W6
    tbo = ast.parse(old)
    lits = []
    for nm in sorted(chg):
        nn, ob = _fn_node(ta, nm), _fn_node(tbo, nm)
        if nn is None:
            continue
        newc = {s for s in _strs(nn) if CASE_LIT_RE.match(s)}
        oldc = {s for s in _strs(ob) if CASE_LIT_RE.match(s)} if ob is not None else set()
        lits += sorted((nm, x) for x in newc - oldc)
    rep("W6", not lits, f"所改之頂層節點內新增之案件字面 {lits}")
    # W7
    vb = _git(repo, "ls-tree", "--name-only", base, "verify/")
    names = sorted(x for x in (vb or b"").decode("utf-8").split("\n") if x.endswith(".py"))
    diff7 = []
    for p in names:
        ob = _git(repo, "show", f"{base}:{p}")
        try:
            nb = open(os.path.join(repo, p), "rb").read()
        except OSError:
            nb = None
        if ob != nb:
            diff7.append(p)
    rep("W7", bool(names) and not diff7, f"verify/ 頂層之 *.py（{len(names)}）對基準相異 {diff7}")
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


# ───────────────────────── run ─────────────────────────

def _one(repo, sb):
    probes = os.path.join(repo, "verify", "probes")
    if probes not in sys.path:
        sys.path.insert(0, probes)
    os.environ["WV_K6B_STAGE3"] = "on"
    import probe_WG9344_k6s3 as K
    ns, fst, snap, cb_by, cad, tp, bp, params = K._boot(repo, sb)
    orig = ns["k965_part_split"]
    cnt = [0]

    def spy(*a, **k):
        r = orig(*a, **k)
        if r is None:
            cnt[0] += 1
        return r
    ns["k965_part_split"] = spy
    n0 = len(ns["K6_PROGRAM_STOPS"])
    import selection_pipeline as sp
    with contextlib.redirect_stdout(io.StringIO()):
        _d, _s, _o, wins, forced, tp2, bp2 = sp.run_corner_pk_k6b(ns, fst, list(cb_by.values()), cad, params, tp, bp, sb,
                                                                  snapshot=snap)
    res = K._materialize(ns, fst, snap, cb_by, cad, params, tp, bp2, wins, forced, sb)
    return res, tp2, cnt[0], len(ns["K6_PROGRAM_STOPS"]) - n0


def run(repo, sbs):
    red = []
    for sb in sbs:
        try:
            res, tp2, nnone, nreg = _one(repo, sb)
        except Exception as e:  # noqa: BLE001
            print(f"  🔴 R1@{sb} 例外 {type(e).__name__}：{str(e)[:200]}")
            red.append(f"R1@{sb}")
            continue
        ok1 = res.get("err") is None and nnone == 0 and nreg == 0
        print(("  ✅" if ok1 else "  🔴") + f" R1@{sb} 中止之訊 {res.get('err')!r}·k965_part_split 之 None {nnone}·程式之停機之登記之增 {nreg}")
        if not ok1:
            red.append(f"R1@{sb}")
        rcv = set()
        for t in tp2 or []:
            rcv |= {str(x) for x in (t.get("段三併出") or [])}
            rcv |= {str(x) for x in (t.get("段三部分併出") or {})}
        kept = {str(r.get("暫編地號")) for r in (res.get("rows") or []) if r.get("驗_總判") == "保留"}
        miss = sorted(rcv - kept)
        ok2 = bool(rcv) and not miss
        print(("  ✅" if ok2 else "  🔴") + f" R2@{sb} 受併宗 {len(rcv)}·最後之配地⛔ 保留者 {miss}")
        if not ok2:
            red.append(f"R2@{sb}")
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return 2
    cmd, repo = argv[1], os.path.abspath(argv[2])
    if cmd == "selftest":
        return selftest(repo)
    if cmd == "wiring":
        if len(argv) != 4:
            print("用法：wiring <repo> <基準 commit>")
            return 2
        return wiring(repo, argv[3])
    if cmd == "run":
        sys.path.insert(0, os.path.join(repo, "verify"))
        os.chdir(repo)
        sbs = [float(x) for x in argv[3:]] or [3.5, 0.0]
        return run(repo, sbs)
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
