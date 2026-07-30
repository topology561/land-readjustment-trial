# -*- coding: utf-8 -*-
# ══════════════════════════════════════════════════════════════════════════════
# 🗄️ **封存（DEPRECATED）**：K-4-3／M-5 街角救援機制
#     **K-6 段三取代，KL 裁 2026-07-30 作廢。**
#     · 作廢範圍：M-5 ①②③、來源母體 (a)(b)(c)、A4 `ConsumedRegistry` U₀ 硬閘。
#     · 取代者：`docs/rulings/K-6_街角地分配程序與可分配判準.md` §二 段三
#       （跨街廓同歸戶「小往較大集中」一律歸七級調配 F.0／F.2；**街角不再有專屬救援機制**）。
#     · 本檔**已自 `run_verification` 之呼叫鏈移除**，僅留供考古；**禁再接線**。
# ══════════════════════════════════════════════════════════════════════════════
"""W-G.4 裁定 M · M-5 — 同歸戶合併規劃（帶優先序）＝ P-D/P-E 之決策層。

## canonical（`docs/specs/W-G.4_KL域裁M_原位次小往大_街角winner更正.md` §七·KL 2026-07-25）

**(1) 概念更正**：forced 街角解鎖 **≠ 抵費地減少**——該面積**回歸中央調配池**
（抵費地總量不變·位置由街角移回中間·既鎖「池置中」則可及容量上升）。**禁「釋回／減少抵費地」語。**

**(2) 合併目標優先序**（未達 MinA 之同歸戶土地得以**部分面積**併入同歸戶較大應分配面積土地）：
  ① 同歸戶「**跨占街角規定範圍但未達街角規定面積**」者**優先**，補至該街角地應分配面積
     ＝**街角規定面積**（**以補足為度**·只取所需）；
  ② 餘額再併其他「**較大但未達該街廓 MinA**」土地（**至達 MinA**）；
  ③ 目標皆達標而仍有餘額 ⇒ 餘額併入**該街角地**（街角＝**最後歸宿**）。
此序**凌駕 F.0 級0 之既有集中結果**（前態係**未帶優先序之中間態**·非被推翻之裁定）。
**🆕 K-4-3（KL 裁 2026-07-27）：M-2「其他可建築街廓」要件於 ①（街角救援）排除適用。**
  來源須**同時**滿足 (a) 同歸戶 (b) **未達**其所在街廓可分配面積
  (c) 其應分配面積 **<** 該街角地候選之應分配面積（「小往較大集中」）；**街廓別不設限**。
  反面（KL 原話）：「本身已達可分配面積，就要在那原位次位置辦理分配，**分配後面積不能再分出去**」
  ⇒ 已達可分配面積者**恆不得為來源**。併鎖：**K-4 第 3 條 ≡ 本 ①，禁另建第二套機制**。
  ⚠️ **連動（reviewer 活抓·勿再寫成「②③不受影響」）**：
    · **③ 之來源集 ≡ ① 之來源集**（`_rest ⊆ aw["srcs"]`）⇒ (a)(b)(c) **自動及於 ③**。
    · **② 碼中本無街廓要件**（`_t2` 只看 gid／is_source／is_target／`_src_pids`／`G < MinA`）
      ⇒「M-2 於②不變」是在描述一個**碼裡不存在的要件**；②為**目標側**、非來源側。
  ⚠️ **適用界**：本條只及於 M-5 ①③ 之來源述詞。`wf_f2` 之級1/2/3 塊級鄰接邏輯
    （`grep -n "frozenset((sblk, tgt_blk))" verify/wf_f2.py`）**屬另一機制·不受影響**。

## 技術詮釋（§7.2）
- **T-2**：M-5 **非**「PK 自救→registry 拿回 F.0」，而是**同歸戶合併整體規劃帶優先序重跑**
  ⇒ 同一 gid 之合併為**單一規劃**（①②③）·**結構上無雙重消費**。
- **T-3（Q-M6）**：**per-candidate**——每個「跨占∧真G<街角規定面積」候選各自嘗試①；
  合格者 ≥2 → **三指數定 winner**（現行 v12 第二關）；**winner 定案才實體化**、非 winner 規劃丟棄。
- **T-4**：①之補足量以**重跑迭代**求最小 a′（禁比率折算·G 對 a 次線性）；消費序依 **Q3**
  （保住原位次分配處數最大化·tie 救較大者）。
- **T-5**：**全 data-driven**（跨占＝E-1.7 真交集>1.0㎡；未達＝`G<MinA[blk]`／`<街角規定面積`；
  同歸戶＝`gid`）·**禁 G007／塊名／常數入碼**·換案成立。

## 兩趟定點（循環相依之解）
    趟0：run_corner_pk(rescue=None) → run_step_g → trunk A₀
         U₀ = {宗: G(A₀) < MinA[blk]}；Corner₀ = {forced 端之跨占-未達候選}
    趟1：build_plan → 物化 parcels₁ → run_corner_pk(rescue) → run_step_g → trunk A₁
"""
import copy


class ConsumedRegistry:
    """跨階段單一結算帳（PK→F.0→F.2→F.4）。

    **源→target 對稱凍結**（reviewer B-6′）：已為源者不得再當 target；已為 target 者不得再當源
    ⇒ 根絕「A 端 target 被 B 端當源」之幻影雙重消費。
    """

    def __init__(self):
        self._u0 = None          # 🆕 K-4-3 結算層硬閘之母體（未注入即呼 claim ⇒ loud）
        self._consumed = {}      # pid → 已消費之 a（源口徑㎡）
        self._orig_a = {}        # pid → 原 a
        self._as_source = set()
        self._as_target = set()

    def set_u0(self, u0):
        """🆕 **K-4-3 結算層硬閘**（KL 2026-07-27）：注入 U₀（未達其街廓可分配面積之宗）。

        ⚠️ **本閘現為恆真**（reviewer 實證：`claim` 之全部呼叫點——①補足／③餘額——之來源
        皆已由 `_source_ok` 之 (b) 濾過；② 完全不呼叫 `claim`）。
        **其值不在「已驗之閘」**，而在**凍結未來新增之 `claim` 呼叫點**：
        任何日後繞過 `_source_ok` 而直接 `claim` 者，於結算層被咬。
        ⛔ **不得**把本條當作 (b) 之獨立佐證（那是 `rot90(rot90(x))∥x` 同族）。
        """
        self._u0 = set(u0)

    def set_orig(self, pid, a):
        self._orig_a[pid] = float(a)

    def remaining(self, pid):
        return round(self._orig_a.get(pid, 0.0) - self._consumed.get(pid, 0.0), 6)

    def claim(self, pid, amount, *, stage, target):
        """源宗出資 amount（源口徑）。超額／已為 target／**非 U₀ 成員** ⇒ loud raise。"""
        if self._u0 is None:
            raise RuntimeError(
                "🔴 M-5 registry：未注入 U₀ 即呼 claim（`set_u0` 漏呼）"
                "——K-4-3 結算層硬閘不可定義·禁預設放行（no-silent-fallback）")
        if pid not in self._u0:
            raise RuntimeError(
                f"🔴 M-5 registry：{pid} **已達其所在街廓可分配面積**，不得為來源"
                f"（K-4-3 題二：「本身已達可分配面積，就要在那原位次位置辦理分配，"
                f"分配後面積不能再分出去」）·{stage}→{target}")
        if pid in self._as_target:
            raise RuntimeError(
                f"🔴 M-5 registry：{pid} 已為 target（受贈宗）·不得再當源（源→target 對稱凍結·{stage}）")
        _rem = self.remaining(pid)
        if float(amount) - _rem > 1e-6:
            raise RuntimeError(
                f"🔴 M-5 registry：{pid} 超額消費 {amount:.4f} > 餘 {_rem:.4f}（{stage}→{target}）")
        self._consumed[pid] = round(self._consumed.get(pid, 0.0) + float(amount), 6)
        self._as_source.add(pid)

    def freeze_target(self, pid, *, stage):
        if pid in self._as_source:
            raise RuntimeError(
                f"🔴 M-5 registry：{pid} 已為源·不得再當 target（對稱凍結·{stage}）")
        self._as_target.add(pid)

    def is_target(self, pid):
        return pid in self._as_target

    def is_source(self, pid):
        return pid in self._as_source

    def consumed(self, pid):
        return self._consumed.get(pid, 0.0)

    def frozen(self):
        """全額消費之源（下游母體須排除）。部分消費者留下、a 已扣減。"""
        return {p for p in self._as_source if self.remaining(p) <= 1e-6}

    def summary(self):
        return {"sources": sorted(self._as_source), "targets": sorted(self._as_target),
                "consumed": {p: round(v, 2) for p, v in self._consumed.items() if v > 0}}


def _a_prime(a_src, z_src, z_tgt, pre_price):
    """模式一 a′＝a×p(源)/p(目標)（`wf_f2.a_prime_mode1` 同式·單一真相源之語意複用）。"""
    ps = float(pre_price.get(z_src, 0.0) or 0.0)
    pt = float(pre_price.get(z_tgt, 0.0) or 0.0)
    if ps <= 0 or pt <= 0:
        raise RuntimeError(f"🔴 M-5 a′ 換算：zone 單價缺（源 {z_src}={ps}／目標 {z_tgt}={pt}）")
    return a_src * ps / pt


def _a_src_from_prime(a_prime_v, z_src, z_tgt, pre_price):
    """`_a_prime` 之**精確逆**：a_src ＝ a′ × p(目標)/p(源)（registry 記帳走源口徑）。"""
    ps = float(pre_price.get(z_src, 0.0) or 0.0)
    pt = float(pre_price.get(z_tgt, 0.0) or 0.0)
    if ps <= 0 or pt <= 0:
        raise RuntimeError(f"🔴 M-5 a_src 反算：zone 單價缺（源 {z_src}={ps}／目標 {z_tgt}={pt}）")
    return a_prime_v * pt / ps


def min_a_prime_for_corner(*, g_fn, a_base, threshold, supply_prime, tol=0.01, max_iter=40):
    """①「補足為度」：二分求**最小 a′（目標 zone 口徑）**使 `G(a_base+a′) ≥ threshold`。

    **禁比率折算**（W-2·G 對 a 次線性）——每次評估**重呼 `g_fn`**（＝`_corner_first_lot_G`·
    與閘/實配同一 solver）。回 `(a_prime|None, G_at)`；`None`＝供給全上仍不足（**guard·不 raise**·
    B-3′：canonical「街角強制抵費地為最後手段」仍是**合法終局**）。
    """
    g_full = g_fn(a_base + supply_prime)
    if g_full < threshold:
        return None, g_full                      # 供給不足 ⇒ 該端維持 forced（guard）
    if g_fn(a_base) >= threshold:
        return 0.0, g_fn(a_base)                 # 本已達標（不應進①·防禦）
    lo, hi = 0.0, float(supply_prime)
    for _ in range(max_iter):
        mid = (lo + hi) / 2.0
        if g_fn(a_base + mid) >= threshold:
            hi = mid
        else:
            lo = mid
        if hi - lo < tol:
            break
    return round(hi, 2), g_fn(a_base + hi)


def _q3_source_order(cands):
    """Q3 消費序：保住原位次分配處數最大化·tie → **救較大者**。
    操作化＝`(a ↓, 暫編地號 ↑)`——先取大者以**減少被拆宗數**（處數保全最大化之貪婪）。"""
    return sorted(cands, key=lambda s: (-float(s["a"]), s["pid"]))


def source_g_a0(sr, spid):
    """來源宗之**應分配面積**（**趟0 trunk A₀ 口徑**·與 U₀ 同源）。

    缺值 ⇒ **loud raise**（no-silent-fallback）。
    ⚠️ 與 `U0` 建構式之對稱性（reviewer NOTE-4）：`U0` 舊以 `float(r.get("G(㎡)",0) or 0)`
    取值 ⇒ **缺值靜默作 0** ⇒ 必然落入 U₀（(b) 放行）而 (c) 停機，**兩條口徑相反**。
    本波已把 `U0` 之建構改走同一函式 ⇒ 兩條**同一口徑、同時 loud**。
    """
    _v = (sr or {}).get("G(㎡)")
    if _v is None or _v == "":
        raise RuntimeError(
            f"🔴 M-5 K-4-3：{spid} 無 `G(㎡)`（趟0 trunk A₀ 應分配面積）"
            f"——(b)/(c) 皆不可判·禁靜默作 0（no-silent-fallback）")
    return float(_v)


def _source_ok(spid, sr, *, pid, gid, gid_of, u0, reg, gtrue):
    """**K-4-3 來源述詞**（KL 裁 2026-07-27）——module 級，供探針以**自建替代述詞**做變體對照。

    ⚠️ **非 feature flag**（reviewer WARNING-5）：本函式**只有一個行為**，
    且**不接受任何切換參數**（尤其**不含 `tgt_blk`**——同塊排除已刪，留該參數即參數式 flag）。
    變體量測由探針**各自提供完整替代述詞閉包**達成。

    (a) 同歸戶（`gid`）／(b) `spid ∈ U0`（未達其所在街廓可分配面積）／
    (c) `G_A₀(spid) < gtrue`（「小往較大集中」）。
    ＋ registry 可用性（非 target、尚有餘量）。

    🚩 **(c) 之右式為「街角第 1 槽試算 G」`gtrue`**（KL K-4 第 3 條原文：
    「判**該試算 G** 是否為同歸戶中**應分配面積**最小者」⇒ 左式原位次、右式街角槽·**跨口徑係原文如此**）。
    **已上呈之副作用（U-K3）**：`_corner_first_lot_G` 只吃 `a` ⇒ 同 `a` 之同歸戶宗 `gtrue` 相同
    ⇒ 二者**互為合格來源**、(c) 於該對**喪失反對稱性**（實測 R3 右 `628-28(1)`／`628-29(1)`
    皆 a=114.00、gtrue=65.61）。改以 `G_A₀` 為右式則恢復嚴格序。**兩讀法之差異已由探針逐格量出**。
    """
    if spid == pid or gid_of.get(spid, "") != gid:
        return False                                    # (a)
    if spid not in u0:
        return False                                    # (b)
    if not (source_g_a0(sr, spid) < float(gtrue)):
        return False                                    # (c)
    return not reg.is_target(spid) and reg.remaining(spid) > 1e-6


def build_plan(*, tag, gA_rows, mina_by_blk, gid_of, corner_ctx, zone_of, pre_price,
               true_g_fn, diag_rows):
    """M-5 單一規劃（①②③·per-candidate·假設帳面）。

    參數（全 data-driven·無塊名/常數）：
      gA_rows      trunk A₀ 之 g_rows（宗 → G/所屬街廓/a）
      mina_by_blk  {blk: MinA}
      gid_of       pid → 歸戶鍵
      corner_ctx   {(blk,side): {'threshold':街角規定面積, 'cands':[pid…]（E-1.7 已濾）,
                                 'true_g':{pid:真G}, 'score':{pid:三指數總分}, 'rank':{pid:投影序}}}
                   —— 僅 **forced 端**（該端無地主 winner）入列。
      true_g_fn    (blk, side, pid) → callable(a)→G（假設第 1 宗真 G·重跑迭代用）
      diag_rows    PK 診斷（三指數總分來源·G 無關）

    回 {'awards': [...], 'registry': ConsumedRegistry, 'log': [...]}
    """
    L = []
    reg = ConsumedRegistry()
    A = {r["暫編地號"]: r for r in gA_rows if r.get("推進側別") in ("left", "right")}
    for pid, r in A.items():
        _a = float(r.get("a 面積(㎡)", 0) or 0)
        reg.set_orig(pid, _a)

    # U₀＝未達所屬街廓 MinA 之宗（＝可出資之「未達地」母體）
    # 🆕 NOTE-4（reviewer）：與 (c) **同一口徑、同時 loud**——舊式 `float(r.get("G(㎡)",0) or 0)`
    #   缺值靜默作 0 ⇒ 必然落入 U₀（(b) 放行）而 (c) 停機，兩條相反。改走 `source_g_a0`。
    U0 = {pid for pid, r in A.items()
          if source_g_a0(r, pid) < mina_by_blk.get(r.get("所屬街廓"), 0.0)}
    reg.set_u0(U0)                       # 🆕 K-4-3 結算層硬閘之母體
    L.append(f"[{tag}] U₀（未達 MinA·可出資）＝{len(U0)} 宗")

    awards = []
    # ── ① per-candidate：每個 forced 端之每個跨占-未達候選各自嘗試補足（Q-M6） ──
    #   端序＝(缺口 ↑, blk ↑, side ↑)：缺口小者先（forced 端數最小化＝上位精神「最後手段」操作化）
    _ends = []
    for (blk, side), c in corner_ctx.items():
        _best = min((c["threshold"] - c["true_g"].get(p, 0.0)) for p in c["cands"]) \
            if c["cands"] else float("inf")
        _ends.append((_best, blk, side))
    for _gap0, blk, side in sorted(_ends):
        c = corner_ctx[(blk, side)]
        thr = c["threshold"]
        qualified = []          # 本端「經①補足後可達門檻」之候選（假設帳面·未實體化）
        for pid in c["cands"]:
            gid = gid_of.get(pid, "")
            if not gid:
                continue
            gtrue = c["true_g"].get(pid)
            if gtrue is None:
                continue
            if gtrue >= thr:
                continue        # 本已達標（非①母體·由既有 PK 處理）
            # 救援源（**K-4-3**·KL 裁 2026-07-27）：(a) 同歸戶 ∧ (b) ∈U₀（未達其街廓可分配面積）
            #   ∧ (c) 其應分配面積 < 該候選之應分配面積 ∧ registry 可用。**街廓別不設限**。
            #   ⛔ 舊之同塊排除（M-2「其他可建築街廓」）**已刪**——K-4-3 明令於 ① 排除適用。
            srcs = []
            for spid, sr in A.items():
                if not _source_ok(spid, sr, pid=pid, gid=gid, gid_of=gid_of,
                                  u0=U0, reg=reg, gtrue=gtrue):
                    continue
                srcs.append({"pid": spid, "a": reg.remaining(spid),
                             "blk": sr.get("所屬街廓"), "zone": zone_of.get(spid, "")})
            if not srcs:
                L.append(f"  ① {blk}{side} {pid}：救援池 ∅"
                         f"（同歸戶內無滿足 (b) 未達地 ∧ (c) 應分配面積 < {gtrue:.2f} 者）⇒ 跳過")
                continue
            srcs = _q3_source_order(srcs)
            z_tgt = zone_of.get(pid, "")
            supply_p = sum(_a_prime(s["a"], s["zone"], z_tgt, pre_price) for s in srcs)
            a_base = float(A[pid].get("a 面積(㎡)", 0) or 0)
            _gfn = true_g_fn(blk, side, pid)
            need_p, g_at = min_a_prime_for_corner(
                g_fn=_gfn, a_base=a_base, threshold=thr, supply_prime=supply_p)
            if need_p is None:
                L.append(f"  ① {blk}{side} {pid}：供給 {supply_p:.2f} 全上仍 G={g_at:.2f}<{thr:.2f}"
                         f" ⇒ 該候選不可救（guard·不 raise）")
                continue
            qualified.append({"pid": pid, "gid": gid, "need_p": need_p, "g_at": g_at,
                              "srcs": srcs, "z_tgt": z_tgt, "a_base": a_base,
                              "score": c["score"].get(pid, 0.0), "rank": c["rank"].get(pid, 1e9)})
            L.append(f"  ① {blk}{side} {pid}：真G {gtrue:.2f}<{thr:.2f}·需 a′={need_p:.2f}"
                     f"（供給 {supply_p:.2f}）→ G={g_at:.2f} ✅ 取得候選資格（帳面）")
        if not qualified:
            L.append(f"  {blk}{side}：無候選可經①補足 ⇒ **維持強制抵費地**（canonical 最後手段）")
            continue
        # 合格者 ≥2 → 三指數定 winner（canonical·G 無關）；tie → 投影序小者
        win = sorted(qualified, key=lambda q: (-float(q["score"]), float(q["rank"])))[0]
        L.append(f"  ⇒ {blk}{side} winner＝{win['pid']}"
                 f"（合格 {len(qualified)} 位·三指數 {win['score']:.4f}）**實體化**"
                 + ("；非 winner 規劃丟棄" if len(qualified) > 1 else ""))
        awards.append({"blk": blk, "side": side, "winner": win["pid"], "gid": win["gid"],
                       "threshold": thr, "need_p": win["need_p"], "g_at": win["g_at"],
                       "z_tgt": win["z_tgt"], "a_base": win["a_base"],
                       "srcs": win["srcs"], "allocs": [], "stage3": 0.0,
                       # F-2(d) 稽核：合格候選數／丟棄之非 winner 規劃數（Q-M6 per-candidate）
                       "n_qualified": len(qualified)})
        reg.freeze_target(win["pid"], stage=f"①{blk}{side}")
        # 依 Q3 序逐源扣至補足量（只取所需）
        _need_left = win["need_p"]
        for s in win["srcs"]:
            if _need_left <= 1e-6:
                break
            _avail_p = _a_prime(reg.remaining(s["pid"]), s["zone"], win["z_tgt"], pre_price)
            _take_p = min(_avail_p, _need_left)
            _take_src = _a_src_from_prime(_take_p, s["zone"], win["z_tgt"], pre_price)
            reg.claim(s["pid"], min(_take_src, reg.remaining(s["pid"])),
                      stage=f"①{blk}{side}", target=win["pid"])
            awards[-1]["allocs"].append({"src": s["pid"], "a_src": round(_take_src, 2),
                                         "a_prime": round(_take_p, 2), "stage": "①補足"})
            _need_left = round(_need_left - _take_p, 6)
        if _need_left > 1e-6:
            raise RuntimeError(f"🔴 M-5 ①：{blk}{side} 補足量未配足（餘 {_need_left:.4f}）")

    # ── ②餘額他併 → ③餘額回街角（逐 award·單一規劃內·無雙重消費） ──
    for aw in awards:
        gid = aw["gid"]
        _rest = [s for s in aw["srcs"] if reg.remaining(s["pid"]) > 1e-6]
        if not _rest:
            continue
        # ② 目標＝同歸戶「較大但未達該塊 MinA」之宗。
        #   **排除**：已為源/target 者 ＋ **本 award 之出資者**（`aw['srcs']`）——出資宗係「較小者」，
        #   不得同時為受贈之「較大者」（canonical：小往大·給者≠受者）。
        _src_pids = {s["pid"] for s in aw["srcs"]}
        _t2 = []
        for pid2, r2 in A.items():
            if (gid_of.get(pid2, "") != gid or reg.is_source(pid2) or reg.is_target(pid2)
                    or pid2 in _src_pids):
                continue
            _blk2 = r2.get("所屬街廓")
            if float(r2.get("G(㎡)", 0) or 0) < mina_by_blk.get(_blk2, 0.0):
                _t2.append({"pid": pid2, "blk": _blk2,
                            "gap": mina_by_blk.get(_blk2, 0.0) - float(r2.get("G(㎡)", 0) or 0)})
        if _t2:
            # 🔴 **loud 停機·禁靜默跳過**（no-silent-fallback）：②之「至達 MinA」需**非街角宗**之 G，
            #   而非街角 G **位置相依**（由整條推進序列決定）⇒ 須 plan v4 E-3 之**批次外迭代**
            #   （注入→run_step_g→量 G→割線修正·6 趟不收斂即 raise）。本案 UC9898 之 ② 母體為空
            #   （見下方 else 分支實測）故未觸；一旦觸發即**停機上呈**，**不得**默默把餘額全轉③
            #   （那會跳過 canonical 明定之②順位）。
            raise RuntimeError(
                f"🔴 M-5 ②（{aw['blk']}{aw['side']}·{gid}）：存在「較大但未達 MinA」目標 "
                f"{[t['pid'] for t in _t2]}——②之補足需 E-3 批次外迭代（非街角 G 位置相依），"
                f"本波未實作 ⇒ **停機上呈**（禁靜默轉③·跳過 canonical ②順位）。")
        L.append(f"  ② {aw['blk']}{aw['side']}·{gid}：無「較大但未達 MinA」目標（給者≠受者）⇒ 全額轉③")
        # ③ 目標皆達標（或無②目標）而仍有餘額 ⇒ 餘額併入該街角地（街角＝最後歸宿）
        _s3 = 0.0
        for s in _rest:
            _rem_src = reg.remaining(s["pid"])
            if _rem_src <= 1e-6:
                continue
            _rem_p = _a_prime(_rem_src, s["zone"], aw["z_tgt"], pre_price)
            reg.claim(s["pid"], _rem_src, stage=f"③{aw['blk']}{aw['side']}", target=aw["winner"])
            aw["allocs"].append({"src": s["pid"], "a_src": round(_rem_src, 2),
                                 "a_prime": round(_rem_p, 2), "stage": "③餘額回街角"})
            _s3 += _rem_p
        aw["stage3"] = round(_s3, 2)
        if _s3 > 0:
            L.append(f"  ③ {aw['blk']}{aw['side']}：餘額 {_s3:.2f}㎡(目標口徑) 併入街角地 {aw['winner']}")
    return {"awards": awards, "registry": reg, "log": L}


def apply_plan(build_parcels, plan):
    """物化（趟1 之 parcels₁·`run_step_g` **之前**）：

    - target（街角 winner）：`面積_m2 += Σa′`（目標 zone 口徑）
    - 源宗全額消費 → **移除**；部分消費 → 扣減落 **`面積_m2`** 累加器欄
      （四欄鐵律：`分攤登記面積_m2` **唯讀**）；扣後 a ≤0 視同全額移除。
    - **硬閘**：`a` 不得 <0。
    回 (parcels₁, removed_set)。
    """
    reg = plan["registry"]
    out = copy.deepcopy(build_parcels)
    by_id = {tp.get("暫編地號"): tp for tp in out}
    for aw in plan["awards"]:
        t = by_id.get(aw["winner"])
        if t is None:
            raise RuntimeError(f"🔴 M-5 物化：winner {aw['winner']} 不在 parcels")
        _add = sum(al["a_prime"] for al in aw["allocs"])
        t["面積_m2"] = round(float(t.get("面積_m2", 0) or 0) + _add, 2)
    removed = set()
    for pid in reg.summary()["consumed"]:
        tp = by_id.get(pid)
        if tp is None:
            continue
        _cons = reg.consumed(pid)
        if reg.remaining(pid) <= 1e-6:
            removed.add(pid)
            continue
        _new = round(float(tp.get("面積_m2", 0) or 0) - _cons, 2)
        _a_after = round(float(tp.get("分攤登記面積_m2", 0) or 0) + _new, 2)
        if _a_after < 0:
            raise RuntimeError(f"🔴 M-5 物化：{pid} 扣減後 a={_a_after}<0（硬閘）")
        tp["面積_m2"] = _new
    out = [tp for tp in out if tp.get("暫編地號") not in removed]
    return out, removed
