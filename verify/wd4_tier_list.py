# -*- coding: utf-8 -*-
"""
W-D.4 清單波 — 四梯分級清單（消費 22 畸零旗標 → 歸戶級四梯分流；git 錨定）。

**零幾何移動、零回饋**：動的只有診斷/報表輸出；不搬地、不呼叫三廢函式、
**禁碰禁擴 build_ownership 指紋**。

🆕 **v3 半實算（KL 裁定 2026-07-09）**：增配 a′／差額地價(§52-1)／放棄改領(§53-2)／
補償兩式(§53-1 本文式=Σa_i×原位置**後**地價；但書式=Σa_i×原位置**前**地價) 一律吃
快照 `財務接線_v3` 真值地價（廢舊 Tab4 99,424 系）。**仍屬試分配、非正式**。
**零回饋圍欄（裁定二）**：上列金額/面積僅入報表，永不回饋 G/守恆/位次/J/k*/池。

⚠️ 梯次判定吃 ΣG_戶（價格相依）→ v3 換真值地價後**梯次合法變動**，
「梯次零 flip」斷言已由 KL 解除（2026-07-09）。

🆕 **F.0-pre 雙軌（KL 裁定 2026-07-10，W-F 缺口D）**：四梯之**值域＝有可建築宗之歸戶**。
無可建築宗者（純公設地歸戶，ΣG_戶 恆 0）舊碼被 `else` 分支靜默吞入「梯3 現金補償」，
與 §7-2/7-3/7-4 之公設地調配路徑對同一批 8 群兩處指派。改：
- 新增 `軌別` 欄：建地軌（有可建築宗）／公設軌（無可建築宗但持公設地）／無地軌（fixture）。
- **公設軌不判梯次**（`梯次="—"`）、撤出梯3；達標門檻＝**區標準 MinA_區**（手冊 宗地分配原則(三)）；
  ½線測試延至 **F.4** 以 **G(a′)** 施作。
- **補償取值停機條款**：公設軌之 §53 補償欄一律留空（舊碼會算出假 0，因 lots 空、清單不吃公設地 a）。
- 梯3 由 10 群縮為 **2 群**（G025 1.84㎡、G030 55.64㎡）＝F.0 唯一釋池對象。
（教訓入 failure-archaeology #15：報表層分類器之輸入域 ≠ 引擎作用域）

歸戶主體＝**Gxxx 指紋群**（KL 撤銷改判 2026-07-08；指紋已含持分＋他項權利內容）；
ΣG_戶＝群內 G **直加**；四梯走群組。詳 `docs/W-D.4_合併分配規格.md`＋`docs/W-D.4_域裁鎖定.md`。

護欄：
- WARNING-A：持分和檢核**逐宗**（分別共有 per-parcel Σ持分≈1.0，非群級加總）。
- WARNING-B：MinA 斷言用**未 round 原始乘積**（abs<0.01；round(114.065,2)=114.06 會 FAIL）。
- 他項權利/查封 signal 由本檔**獨立讀 U_LAND**（設定義務人/權利種類），不碰 build_ownership 指紋。
- 第4梯 fixture 完全在本層合成（永不入 build_ownership xlsx/parcel_fp，保 6 Gxxx 靶＋byte-identity）。

用法：python verify/wd4_tier_list.py   # 算＋寫 CSV＋斷言，exit 0=一致
"""
import os
import sys
import csv
import json

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from app_harvest import harvest                       # noqa: E402
import run_verification as rv                         # noqa: E402
from selection_pipeline import (                      # noqa: E402
    build_ownership, build_build_parcels, run_corner_pk)
from stepg_pipeline import run_step_g                 # noqa: E402
import wd3_fragment_geom as wd3                        # noqa: E402（碎片三分類單一真相源）

OUTDIR = os.path.join(HERE, "out")
MINA_QU_EXPECT = 114.07   # R4 round(32.59×3.5,2)=114.07（正典 rounded，WARNING-1 裁定；全等斷言）
HALF_EXPECT = 57.04       # ½線顯示：Decimal ROUND_HALF_UP(114.07/2=57.035)=57.04（禁 float round=57.03）
# 🆕 v3：畸零旗標數（宗地寬度<法定最小寬）。v2=22 → v3=31（+9，無消失）：配地寬隨真值地價
#   縮約 24%、跌破 min_width 3.5m，屬合法隨價變（歸因見 baselines/v3/PROVENANCE_v3.md 註⑤）。
FLAGGED_EXPECT = 31
# 🆕 F.0-pre 雙軌錨（KL 裁定 2026-07-10，缺口D）：33 群＝建地軌 25 ＋ 公設軌 8。
#   公設軌不判梯次（"—"），撤出舊「梯3 現金補償」；梯3 由 10 群縮為 2 群
#   （G025 ΣG=1.84㎡、G030 ΣG=55.64㎡，此二群方為 F.0 釋池對象）。
TRACK_EXPECT = {"建地軌": 25, "公設軌": 8}
TIER_EXPECT = {"—": 8, "0": 13, "1": 7, "2": 3, "3": 2}   # W-G Y 波比率更新（2026-07-14）：一群自梯 2 降至梯 0（新單價使 G 增·門檻改變）；舊值 {"—":8,"0":12,"1":7,"2":4,"3":2}
PUB_TRACK_GROUPS = ["G003", "G012", "G013", "G015", "G016", "G024", "G028", "G031"]
# 公設地實盤（F.3 母數，取代規格作廢之「30 筆/4,428㎡」）：59 筆 / 28 群持有 / 12,130.83㎡
PUB_PARCELS_EXPECT = 59
PUB_HOLDER_GROUPS_EXPECT = 28
FLAG = "⚠️移出/第1調配順位"
# 禁止移轉/查封類 權利種類（U_LAND；本案全空，fixture 用「查封」觸發）
_LOCK_KINDS = ("查封", "假扣押", "假處分", "破產", "預告登記")


def _mina_by_block(ns, snapshot, cb_by, build_blocks):
    """MinA_i = round(分配深度_i × min_width_i, 2)＝正典 `f3_min_alloc_area_by_label` 同式
    （WARNING-1 裁定 2026-07-08：辦法 §3「面積計算至小數點以下二位、第三位四捨五入」，
    rounded 為法定慣例；R4=round(32.59×3.5,2)=114.07）。回傳 (mina dict, mina_qu)。"""
    gm = ns["get_min_lot_size"]
    SB = snapshot["blocks"]
    mina = {}
    for b in build_blocks:
        lbl = b["label"]
        depth = float(SB[lbl]["街廓分配深度_m"])
        mw = float(gm(b["category"], float(SB[lbl]["正面"]["路寬_m"]))["min_width"])
        mina[lbl] = round(depth * mw, 2)   # 正典 rounded
    return mina, min(mina.values())


def _half_display(mina_qu):
    """½線**顯示值**：辦法 §3 第三位四捨五入（ROUND_HALF_UP），**禁用 float round()**
    （Python round(57.035,2)=57.03 之 banker's/float 刀口；MinA_區 114.07→½ 顯示 57.04）。
    判定式一律用 `2×ΣG ≥ MinA_區`（整數倍、無除法無二次 round），本值僅供顯示。"""
    from decimal import Decimal, ROUND_HALF_UP
    return float((Decimal(str(mina_qu)) / Decimal(2)).quantize(
        Decimal("0.01"), rounding=ROUND_HALF_UP))


def _blocking_signal_by_parent(anon_xlsx, fixture_parents=None):
    """獨立讀 U_LAND（不碰 build_ownership 指紋）→ {原地號: (has他項權利, has查封)}。
    本案全 False。fixture_parents: {原地號: '查封'} 之合成注入（僅本層）。"""
    import pandas as pd
    xl = pd.ExcelFile(anon_xlsx, engine="openpyxl")
    u = pd.read_excel(xl, "U_LAND", header=0, engine="openpyxl")
    rz = pd.read_excel(xl, "重劃區地籍", header=0, engine="openpyxl")
    u["段名"] = u["段小段"].astype(str).str.replace(r"^\d+", "", regex=True)
    u["地號int"] = pd.to_numeric(u["地號"], errors="coerce")

    def _conv(s):
        s = str(s).strip()
        if "-" in s:
            p = s.split("-", 1)
            return int(p[0]) * 10000 + int(p[1])
        return int(s) * 10000
    sig = {}
    for _, r in rz.iterrows():
        landno = str(r["地號"]).strip()
        try:
            m = u[(u["段名"] == str(r["地段"]).strip())
                  & (u["地號int"] == _conv(landno))]
        except Exception:
            m = u.iloc[0:0]
        has_mort = bool(m["設定義務人"].notna().any())
        kinds = m["權利種類"].dropna().astype(str)
        has_lock = bool(any(any(k in v for k in _LOCK_KINDS) for v in kinds))
        sig[landno] = (has_mort, has_lock)
    for _p, _k in (fixture_parents or {}).items():
        sig[_p] = (sig.get(_p, (False, False))[0],
                   any(_lk in _k for _lk in _LOCK_KINDS))
    return sig


def _share_sum_by_parent(rows_out):
    """逐宗持分和（WARNING-A：per-parcel Σ(分子/分母)，分別共有≈1.0）。回傳 {原地號: Σ持分}。"""
    acc = {}
    for row in rows_out:
        ln = row.get("地號", "")
        try:
            d = float(row.get("持分分母", 0) or 0)
            n = float(row.get("持分分子", 0) or 0)
            s = (n / d) if d else 0.0
        except Exception:
            s = 0.0
        acc[ln] = acc.get(ln, 0.0) + s
    return acc


def compute(fixture=False):
    snapshot = json.load(open(rv.SNAPSHOT, encoding="utf-8"))
    ns, fake_st = harvest()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    own = build_ownership(ns, fake_st, rv.ANON_XLSX)
    rows_out = own["rows_out"]
    groups = dict(fake_st.session_state["t8_ownership_groups"])   # Gxxx→[原地號]
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp, build, _sw = build_build_parcels(ns, fake_st, v6, list(cb_by.values()), snapshot)
    fcb = ns["F3_CATEGORY_BURDEN"]
    build_blocks = [b for b in cb_by.values()
                    if fcb.get(b.get("category", ""), "") == "可建築土地"]
    mina, mina_qu = _mina_by_block(ns, snapshot, cb_by, build_blocks)
    half_disp = _half_display(mina_qu)   # 僅顯示；判定式用 2×ΣG≥MinA_區
    share_sum = _share_sum_by_parent(rows_out)
    # fixture：合成查封宗自成一群（本層，不入 build_ownership）
    fixture_parent = "FIXTURE-查封" if fixture else None
    sig = _blocking_signal_by_parent(
        rv.ANON_XLSX, {fixture_parent: "查封"} if fixture else None)
    # 🆕 v3 財務接線：真值地價（廢舊 Tab4 99,424 系；換新查估組 75,551 系）
    _fin3 = snapshot["財務接線_v3"]
    post_price = {k: float(v["單價_元每m2"]) for k, v in _fin3["後街廓_面積單價"].items()}
    pre_price = {z: float(v["單價_元每m2"]) for z, v in _fin3["重劃前區段_面積單價"].items()}
    zone_of = _fin3["原地號_區段"]
    # 🆕 F.0-pre 雙軌（KL 裁定 2026-07-10，缺口D）：逐原地號之公設地（共同負擔）持有量。
    #   ghost sliver 幾何面積恆 0、不入計；其真面積另存 _ghost_area_m2（已落池）。
    pub_cnt, pub_area = {}, {}
    for tp in temp:
        if (fcb.get(tp["街廓分類"], "") != "共同負擔") or tp.get("_is_ghost_sliver"):
            continue
        _p = tp["原地號"]
        pub_cnt[_p] = pub_cnt.get(_p, 0) + 1
        pub_area[_p] = pub_area.get(_p, 0.0) + float(tp.get("幾何面積_m2", 0) or 0)
    # 碎片三分類（W-D.3 單一真相源）：{(情境,暫編): (cat3, 沿街s)}——只有「碎片」需遞補
    _geom, _ = wd3.compute()
    frag_cls = {(g["情境"], g["暫編地號"]): (g["三分類"],
                (float(g["沿街s"]) if g["沿街s"] != "" else None)) for g in _geom}

    out = {}
    for setback, tag in ((0.0, "0m"), (3.5, "3.5m")):
        params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
        _pk = run_corner_pk(ns, fake_st, list(cb_by.values()), cad,
                            params, temp, build, setback)
        sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot,
                        params, build, _pk[3], _pk[4], setback)
        g_rows = [r for r in sg["g_rows"] if r.get("推進側別") != "抵費地"]
        # 原地號 → [暫編 g_row]
        by_parent = {}
        for r in g_rows:
            by_parent.setdefault(r["原地號"], []).append(r)

        group_rows = []
        _groups_iter = dict(groups)
        if fixture:
            _groups_iter["G_FIXTURE"] = [fixture_parent]   # 查封宗自成一群
        for gid in sorted(_groups_iter):
            parents = _groups_iter[gid]
            # 展開群內 原地號 → 暫編（NOTE-5）
            lots = [r for p in parents for r in by_parent.get(p, [])]
            is_fixture_grp = (gid == "G_FIXTURE")
            sumG = round(sum(float(r.get("G(㎡)", 0) or 0) for r in lots), 2)
            flagged = [r["暫編地號"] for r in lots if str(r.get("畸零地旗標", "")).strip()]
            # 步0.5 阻卻（任一宗 他項權利 或 查封）
            blocked = any(sig.get(p, (False, False))[0] or sig.get(p, (False, False))[1]
                          for p in parents)
            # 步1 逐宗達標（G_i≥MinA_街廓 且 無畸零旗標）
            def _qual(r):
                return (float(r.get("G(㎡)", 0) or 0) >= mina.get(r["所屬街廓"], 1e9)
                        and not str(r.get("畸零地旗標", "")).strip())
            all_qual = bool(lots) and all(_qual(r) for r in lots)

            # ── 🆕 F.0-pre 軌別（KL 裁定 2026-07-10，缺口D）──
            #   **四梯之值域＝有可建築宗之歸戶**。無可建築宗者（純公設地歸戶）ΣG_戶 恆 0，
            #   舊碼被 else 分支靜默吞入「梯3 現金補償」，與 §7-2/7-3/7-4 之公設地調配路徑
            #   直接衝突（同一批 8 群兩處指派）。改**顯式標軌別、不判梯次**（failure-archaeology #15）。
            _n_pub = sum(pub_cnt.get(p, 0) for p in parents)
            _a_pub = round(sum(pub_area.get(p, 0.0) for p in parents), 2)
            if lots:
                track = "建地軌"
            elif _n_pub > 0:
                track = "公設軌"
            else:
                track = "無地軌"          # 本案僅 fixture 合成群落此

            # 步2 群組級梯次（阻卻→仍原位，梯次仍計；第4梯前置以 阻卻 欄呈現）
            if track == "公設軌":
                # 不判梯次：達標門檻＝區標準 MinA_區（手冊 宗地分配原則(三)，無「原街廓」可言）；
                # ½線測試延至 F.4、以 G(a′) 施作（KL 裁定）。
                tier, lvl = "—", "公設地歸戶·待 F.3/F.4 調配"
            elif all_qual:
                tier, lvl = "1", "級0 逐宗個別"
            elif any(sumG >= mina[l] for l in mina):
                tier, lvl = "0", "級0 集中合併/級0′弱弱聯合"
            elif 2 * sumG >= mina_qu:   # ½線判定：整數倍、無除法無二次 round（WARNING-1 裁定）
                tier, lvl = "2", "級1-4 增配(雙出口)"
            else:
                tier, lvl = "3", "現金補償(兩式)"
            # 持分和檢核（逐宗，WARNING-A）
            bad_share = [p for p in parents
                         if p in share_sum and abs(share_sum[p] - 1.0) > 0.01]
            # 🆕 v3 半實算（真值地價；**仍屬試分配、非正式**）。零回饋圍欄：
            #   本區所有金額/面積僅入報表，永不回饋 G/守恆/位次/J/k*/池（裁定二圍欄）。
            _inc_a = _diff_price = _waive = _comp_main = _comp_proviso = ""
            _est_kind = "半實算(試分配·非正式)"
            if track == "公設軌":
                # **補償取值停機條款（KL 裁定）**：G(a′) 未算前禁取補償值。
                #   舊碼於此會算出 Σa_i=0 → 補償額 0（因 lots 空、清單不吃公設地 a），
                #   該 0 為假值。一律留空並標停機條款，待 F.4 以 G(a′) 施作。
                _est_kind = "待 F.4·G(a′) 未算前禁取補償值（停機條款）"
            elif tier == "2":
                # 出口a：增配（§31-1-2 後段＋§52-1）。目標＝最淺深度街廓（MinA 最小者）
                _tgt = min(mina, key=mina.get)
                _inc = round(mina[_tgt] - sumG, 2)
                _inc_a = _inc
                _diff_price = round(_inc * post_price[_tgt])           # §52-1 差額地價
                # 出口b：按標準配後申請放棄改領現金（§53-2）＝ΣG_戶 × 分配位置後地價
                _pos = max(lots, key=lambda r: float(r.get("G(㎡)", 0) or 0))["所屬街廓"]
                _waive = round(sumG * post_price[_pos])
            elif tier == "3":
                # 兩式（§31-1-2 前段＋§53-1）。逐宗 a_i × 原位置地價（非以單一街廓近似）
                _comp_main = round(sum(                                # 本文式：後地價
                    float(r.get("a 面積(㎡)", 0) or 0) * post_price[r["所屬街廓"]]
                    for r in lots))
                _comp_proviso = round(sum(                             # 但書式：前地價（v3 首次可實算）
                    float(r.get("a 面積(㎡)", 0) or 0) * pre_price[zone_of[r["原地號"]]]
                    for r in lots)) if all(r["原地號"] in zone_of for r in lots) else ""
            if is_fixture_grp or blocked:
                _path = "查封宗自成一群·不得聯合"
            elif track == "公設軌":
                _path = ("公設軌·達標門檻＝區標準 " + f"{mina_qu}" +
                         "(手冊(三))；½線測試延至 F.4 以 G(a′) 施作")
            else:
                _path = lvl
            group_rows.append({
                "情境": tag, "歸戶鍵Gxxx": gid, "軌別": track, "宗數": len(lots),
                "宗清單": ";".join(r["暫編地號"] for r in lots),
                "公設宗數": _n_pub, "公設面積(㎡)": _a_pub,
                "ΣG_戶(㎡)": sumG, "含旗標宗數": len(flagged),
                "梯次": tier, "對應v3級": lvl,
                "阻卻": ("是" if blocked else "否"),
                "路徑標註": _path,
                "持分和檢核": ("✅" if not bad_share else f"🔴異常{bad_share}"),
                "增配a′(㎡)": _inc_a,
                "差額地價(元)§52-1": _diff_price,
                "放棄改領(元)§53-2": _waive,
                "補償_本文式(元)§53-1": _comp_main,
                "補償_但書式(元)": _comp_proviso,
                "估算性質": _est_kind,
                "備註": ("第4梯前置·阻卻" if blocked else ""),
            })

        # 步1.5 同宗跨占分配線（§31-1-3）：同原地號多街廓暫編
        recomp_rows = []
        for parent, lots in by_parent.items():
            blks = {r["所屬街廓"] for r in lots}
            if len(blks) < 2:
                continue
            big = max(lots, key=lambda r: float(r.get("G(㎡)", 0) or 0))
            for r in lots:
                gi = float(r.get("G(㎡)", 0) or 0)
                if gi < mina.get(r["所屬街廓"], 0) or str(r.get("畸零地旗標", "")).strip():
                    recomp_rows.append({
                        "情境": tag, "原地號": parent, "暫編地號": r["暫編地號"],
                        "所屬街廓": r["所屬街廓"], "G(㎡)": round(gi, 2),
                        "該側MinA(㎡)": round(mina.get(r["所屬街廓"], 0), 2),
                        "跨線併大側→": big["暫編地號"],
                        "大側G(㎡)": round(float(big.get("G(㎡)", 0) or 0), 2),
                    })

        # 步3 S=0 碎片遞補標註（僅 W-D.3「碎片」；**沿分配序往前找第一筆有效宗**、跳過失格中間筆）
        #   域裁§四錨（v3 重錨·run_verification:707 為權威閘）：R6 85.66→**628-4(1)**（v2 之標的 628-1(2)
        #   於 v3 自身入畸零旗標〔寬<3.5m〕→ 續往內遞補），跳過 628(2);628-1(2);628-23(1)。
        #   （舊註「→628-1(2)·跳過 628(2)」係 v2 過期標的·#26a·KL 2026-07-20 更正。）有效＝S≠0 且 宗地寬度≥min_width。
        frag_rows = []
        for r in sg["g_rows"]:
            if r.get("推進側別") != "抵費地":
                continue
            key = (tag, r["暫編地號"])
            cat, s_frag = frag_cls.get(key, ("", None))
            if cat != "碎片":
                continue   # 池主體/forced角落鎖定 不遞補
            lbl = r["所屬街廓"]
            mw = _mw(ns, snapshot, cb_by, lbl)
            side = "left" if (s_frag is not None and s_frag < 0.5) else "right"
            # 該側宗地沿分配序（累積S 由角落遞增）；自碎片端往內走第一筆有效、跳過失格
            seq = sorted([x for x in g_rows if x["所屬街廓"] == lbl
                          and x.get("推進側別") == side],
                         key=lambda x: float(x.get("累積S(m)", 0) or 0))
            target = "—"; skipped = []
            for x in seq:
                if (float(x.get("S(m)", 0) or 0) > 0.01
                        and float(x.get("宗地寬度(m)", 0) or 0) >= mw):
                    target = x["暫編地號"]; break
                skipped.append(x["暫編地號"])
            frag_rows.append({
                "情境": tag, "碎片": r["暫編地號"],
                "面積(㎡)": round(float(r.get("幾何面積(㎡)", 0) or 0), 2),
                "沿街s": (round(s_frag, 2) if s_frag is not None else ""), "側": side,
                "遞補標的宗": target, "跳過失格筆": ";".join(skipped),
                "定序註": "先解失格業主(域裁C)",
            })
        _tracks, _tiers = {}, {}
        for r in group_rows:
            _tracks[r["軌別"]] = _tracks.get(r["軌別"], 0) + 1
            _tiers[r["梯次"]] = _tiers.get(r["梯次"], 0) + 1
        out[tag] = {"groups": group_rows, "recomp": recomp_rows, "frag": frag_rows,
                    "mina_qu": mina_qu, "half_disp": half_disp,
                    "tracks": _tracks, "tiers": _tiers,
                    "flagged_ct": sum(
                        1 for r in g_rows if str(r.get("畸零地旗標", "")).strip())}
    return out


_MW_CACHE = {}


def _mw(ns, snapshot, cb_by, lbl):
    if lbl not in _MW_CACHE:
        gm = ns["get_min_lot_size"]
        fw = float(snapshot["blocks"][lbl]["正面"]["路寬_m"])
        _MW_CACHE[lbl] = float(gm(cb_by[lbl]["category"], fw)["min_width"])
    return _MW_CACHE[lbl]


def _write(path, rows):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if not rows:
        open(path, "w", encoding="utf-8-sig").close()
        return
    with open(path, "w", encoding="utf-8-sig", newline="", ) as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()), lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


def main():
    res = compute(fixture=False)
    allok = True
    for tag in ("0m", "3.5m"):
        d = res[tag]
        _write(os.path.join(OUTDIR, f"W-D.4_四梯分級清單_退縮{tag}.csv"), d["groups"])
        _write(os.path.join(OUTDIR, f"W-D.4_碎片遞補對照_退縮{tag}.csv"), d["frag"])
        _write(os.path.join(OUTDIR, f"W-D.4_跨占分配線_退縮{tag}.csv"), d["recomp"])
        # 斷言：MinA_區/½線（價格無關＝depth×min_width；未 round，容差<0.01，WARNING-B）
        ok_m = (d["mina_qu"] == MINA_QU_EXPECT) and (d["half_disp"] == HALF_EXPECT)
        # 旗標全消費（群組語意）＋ v3 旗標數錨（隨價變、非硬編 22）
        consumed = sum(int(g["含旗標宗數"]) for g in d["groups"])
        ok_f = (d["flagged_ct"] == FLAGGED_EXPECT) and (consumed == FLAGGED_EXPECT)
        # 🆕 F.0-pre 雙軌錨
        ok_t = (d["tracks"] == TRACK_EXPECT) and (d["tiers"] == TIER_EXPECT)
        _pub = sorted(g["歸戶鍵Gxxx"] for g in d["groups"] if g["軌別"] == "公設軌")
        ok_p = (_pub == PUB_TRACK_GROUPS)
        _n_pub_parcels = sum(int(g["公設宗數"]) for g in d["groups"])
        _n_pub_holders = sum(1 for g in d["groups"] if int(g["公設宗數"]) > 0)
        ok_m2 = (_n_pub_parcels == PUB_PARCELS_EXPECT
                 and _n_pub_holders == PUB_HOLDER_GROUPS_EXPECT)
        print(f"[{tag}] MinA_區={d['mina_qu']}(期114.07) ½顯示={d['half_disp']}(期57.04) "
              f"{'✅' if ok_m else '🔴'} | 旗標 {d['flagged_ct']}→消費 {consumed} "
              f"(期{FLAGGED_EXPECT}) {'✅' if ok_f else '🔴'} | 群組 {len(d['groups'])}")
        print(f"      軌別 {d['tracks']} 梯次 {d['tiers']} {'✅' if ok_t else '🔴'} | "
              f"公設軌 {len(_pub)} 群 {'✅' if ok_p else '🔴'} | "
              f"公設地 {_n_pub_parcels} 筆/{_n_pub_holders} 群持有 {'✅' if ok_m2 else '🔴'}")
        allok = allok and ok_m and ok_f and ok_t and ok_p and ok_m2
    print("RESULT:", "W-D.4 CLEAN" if allok else "W-D.4 FAIL")
    return 0 if allok else 1


if __name__ == "__main__":
    sys.exit(main())
