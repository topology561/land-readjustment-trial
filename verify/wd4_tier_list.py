# -*- coding: utf-8 -*-
"""
W-D.4 清單波 — 四梯分級清單（消費 22 畸零旗標 → 歸戶級四梯分流；git 錨定）。

**清單波：零幾何移動、零財務實算**。動的只有新診斷輸出；不算 a′/增配/補償/拆單實算、
不搬地、不呼叫三廢函式、**禁碰禁擴 build_ownership 指紋**。run_all 既有 20 閘綠＝零移動之證。

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
    temp, build, _sw = build_build_parcels(ns, fake_st, v6, list(cb_by.values()))
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
    tab4 = {k: float(v["地價_元每m2"]) for k, v in
            snapshot["財務接線_重劃後街廓地價_Tab4"].items() if isinstance(v, dict)}
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
            # 步2 群組級梯次（阻卻→仍原位，梯次仍計；第4梯前置以 阻卻 欄呈現）
            if all_qual:
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
            # 參考估算（帶標籤；不進 G/守恆——裁定二圍欄）
            ref = ""
            if tier == "2":
                _tgt = min(mina, key=mina.get)   # R4 最淺
                ref = f"增配≈{round(mina[_tgt]-sumG,2)}·差額≈{round((mina[_tgt]-sumG)*tab4.get(_tgt,0),0):.0f}(參考,a′待v3)"
            elif tier == "3":
                _a = round(sum(float(r.get('a 面積(㎡)', 0) or 0) for r in lots), 2)
                _bk = lots[0]["所屬街廓"] if lots else "R4"
                ref = f"補償本文≈{round(_a*tab4.get(_bk,0),0):.0f}(參考,a′待v3)"
            group_rows.append({
                "情境": tag, "歸戶鍵Gxxx": gid, "宗數": len(lots),
                "宗清單": ";".join(r["暫編地號"] for r in lots),
                "ΣG_戶(㎡)": sumG, "含旗標宗數": len(flagged),
                "梯次": tier, "對應v3級": lvl,
                "阻卻": ("是" if blocked else "否"),
                "路徑標註": ("查封宗自成一群·不得聯合" if (is_fixture_grp or blocked)
                             else lvl),
                "持分和檢核": ("✅" if not bad_share else f"🔴異常{bad_share}"),
                "參考估算": ref,
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
        #   域裁§四錨：R6 85.66→628-1(2)，跳過 628(2)(S=0.19)。有效＝S≠0 且 宗地寬度≥min_width。
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
        out[tag] = {"groups": group_rows, "recomp": recomp_rows, "frag": frag_rows,
                    "mina_qu": mina_qu, "half_disp": half_disp, "flagged_ct": sum(
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
        # 斷言：MinA_區/½線（未 round，容差<0.01，WARNING-B）
        ok_m = (d["mina_qu"] == MINA_QU_EXPECT) and (d["half_disp"] == HALF_EXPECT)
        # 22 旗標全消費
        consumed = sum(int(g["含旗標宗數"]) for g in d["groups"])
        ok_f = (d["flagged_ct"] == 22) and (consumed == 22)
        print(f"[{tag}] MinA_區={d['mina_qu']}(期114.07) ½顯示={d['half_disp']}(期57.04) "
              f"{'✅' if ok_m else '🔴'} | 旗標 {d['flagged_ct']}→消費 {consumed} "
              f"{'✅' if ok_f else '🔴'} | 群組 {len(d['groups'])}")
        allok = allok and ok_m and ok_f
    print("RESULT:", "W-D.4 CLEAN" if allok else "W-D.4 FAIL")
    return 0 if allok else 1


if __name__ == "__main__":
    sys.exit(main())
