# -*- coding: utf-8 -*-
r"""**D-2b-9 §A′-2**：`run_step_g` 之 `raise` 清單**自生成** ＋ 具名更正 D-2b-8【B】閘位。

## 為何需要本檔

`verify/out/probe_D2b8_guard.log`【B】段之七道閘行號與標籤**皆誤**：其行號係**人手抄自**
D-2b-8【A】**修改之前**之 grep，而【A】自身之插入使其後全部位移。現查（commit `f8674de`）：
`:1276` 實為 `if _nrm_a < 1e-9:`、`:1323` 實為 `if _pool_total_blk is not None:`
——**兩者皆非 `raise`**；且標籤整體位移，把「範圍守衛」誤標成「telescoping 總量段」。
閘族數亦非 7。

🔒 **`probe_D2b8_guard.log` 為已入庫實料，⛔ 一字不刪、不覆寫**；本檔以**具名更正**取代其【B】段。

## 手法（⛔ 人手抄一律禁止）

清單由**原始碼解析**產生：讀 `verify/stepg_pipeline.py`，自 `def run_step_g` 起、
至**下一個頂層 `def`** 止，列出每一個 `raise` 之行號與訊息首行實文。
閘族由**訊息內容**歸併，⛔ 不預設族數。
🔒 **母體為空即失敗**（解析 0 筆 ⇒ raise，⛔ 不得靜默輸出空表）。
"""
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
SRC = os.path.join(VERIFY, "stepg_pipeline.py")
OUTDIR = os.path.join(VERIFY, "out")
# 🔴 **D-2b-10 §前-1**：本檔之 `_family()` 已修（去萬用桶）⇒ 輸出改寫**新檔**，
#   ⛔ **不覆寫** `probe_D2b9_guard_degen.log`（已入庫實料·D-2b-9 之歷史證據）。
LOG = os.path.join(OUTDIR, "probe_D2b10_family.log")
W = 200

# D-2b-8【B】之錯誤值（供具名更正對照·⛔ 非重新抄寫閘位，係記錄「被取代者」）
D2B8_WRONG = [
    (972, "抵費地計算失敗（含覆蓋閘/②-宗）"), (990, "§N3-0 逐宗主閘"),
    (1164, "telescoping 總量段"), (1198, "階段2 telescoping 段"),
    (1241, "â 定向雙判準"), (1276, "理論＝實跑"), (1323, "停機③ 守恆-帳幾何級"),
]


def _extract():
    """自 `run_step_g` 函式體解析全部 `raise`。回傳 list[(lineno, first_line_text)]。"""
    src = io.open(SRC, encoding="utf-8").read().splitlines()
    start = None
    for i, ln in enumerate(src):
        if re.match(r"^def run_step_g\b", ln):
            start = i
            break
    if start is None:
        raise RuntimeError("🔴 解析失敗：找不到 `def run_step_g`（⛔ 不得靜默輸出空表）")
    end = len(src)
    for i in range(start + 1, len(src)):
        if re.match(r"^def\s+\w+", src[i]):        # 下一個**頂層** def
            end = i
            break
    out = []
    for i in range(start, end):
        if re.match(r"^\s*raise\b", src[i]):
            # 訊息首行實文：往下找第一個含引號之行（`raise X(` 常換行）
            msg = ""
            for j in range(i, min(i + 4, end)):
                m = re.search(r'f?"(.*)', src[j])
                if m and ('"' in src[j]):
                    msg = src[j].strip()
                    break
            out.append((i + 1, msg or src[i].strip()))
    if not out:
        raise RuntimeError("🔴 解析母體為空（0 筆 `raise`）⇒ 視為失敗（⛔ 不得靜默輸出空表）")
    return out, start + 1, end


# ══ 🆕 **D-2b-10 §前-1**：去萬用桶、改「骨架正規化 ＋ 明列登記表 ＋ 雙向對帳」══
#
# 🔴 **舊 `_family()` 之病（已刪·⛔ 不得復活）**：先比一組**硬編八鍵**，落空走 regex
#    `🔴\s*(...)`，再落空回傳 **`（其他）`**。而 `:575`（`條件③ J 非零看守破`）與
#    `:819`（`停機②（J 下降）`）之訊息**不帶 🔴 前綴** ⇒ regex 落空 ⇒
#    **兩個結構上不同之閘被併入同一桶** ⇒ 桶數 14 之中有一桶含兩族、**實際族數 15**。
#    更要緊者：`（其他）` 會**靜默吸收未來任何新閘** ——
#    一支為根除「以固定 regex 代窮舉」而寫之探針，**自己犯了同一個病**（失敗考古節 53）。
#
# **骨架規則**（決定性·⛔ 無回退鏈）：取字串字面 → 去 f-string 佔位符 `{...}`
#    → 去前導 `🔴` 與空白 → 取至**第一個 `：`** 或行末 → 壓縮連續空白。
#    骨架為空 ⇒ 列入「無法正規化」殘差（⛔ 不得靜默丟棄）。

GATE_FAMILIES = {
    "財務鋪底未完成":              ["f3_total_burden_rate_from_finance 未鋪底"],
    "BASELINE 圖層未解析/配對全失敗": ["run_step_g"],
    "結構閘 ⊥":                   ["結構閘 ⊥ 破"],
    "P2-a 退化序卻有階段2宗":       ["P2-a"],
    "結構閘 位次＝投影序":           ["結構閘 位次＝投影序 破"],
    "條件③ J 非零看守":            ["條件③ J 非零看守破"],          # ← 舊版被 `（其他）` 吸收
    "停機②（J 下降）":             ["停機②（J 下降）街廓"],          # ← 舊版被 `（其他）` 吸收
    "抵費地計算失敗（覆蓋閘/②-宗 之外層）": ["街廓 抵費地計算失敗"],
    "§N3-0 逐宗主閘":              ["§N3-0 逐宗主閘破"],
    "K-9-5-5 範圍守衛":            ["K-9-5-5 範圍守衛破（退化側）", "K-9-5-5 範圍守衛破"],
    "結構閘 telescoping 總量段":    ["結構閘 telescoping 破（鏈斷·`K-9-5-6`）",
                                   "結構閘 telescoping 破"],
    "結構閘 階段2 telescoping 段":  ["結構閘 階段2 telescoping 破（鏈斷·`K-9-5-6`）",
                                   "結構閘 階段2 telescoping 破"],
    "â 定向雙判準":                ["â 定向雙判準不一致（補丁八 §三）"],
    "結構閘 理論＝實跑":            ["結構閘 理論＝實跑 破（鏈斷·`K-9-5-6`）",
                                   "結構閘 理論＝實跑 破"],
    "停機③ 守恆-帳幾何級":          ["停機③（守恆-帳幾何級破）街廓"],
}


def _skeleton(msg):
    """訊息 → 正規化骨架（⛔ 無回退鏈·空骨架須由呼叫端列入殘差）。"""
    m = re.search(r'"(.*)"', msg)
    inner = m.group(1) if m else msg
    inner = re.sub(r'\{[^{}]*\}', '', inner)          # 去 f-string 佔位符
    inner = inner.lstrip().lstrip('🔴').strip()        # 去前導 🔴
    inner = inner.split('：')[0]                       # 取至第一個 `：`
    return re.sub(r'\s+', ' ', inner).strip()


def _reconcile(rows):
    """**雙向**對帳。回傳 (族→行號, 殘差甲, 殘差乙, 空骨架)。

    🔒 **兩種「空」方向相反·⛔ 不得混淆**：
      · **母體**（`raise` 枚舉）為空 ⇒ **失敗**（解析壞了）——由 `_extract` 負責 raise。
      · **殘差**（對帳未命中）為空 ⇒ **通過**，但仍須逐字印出「（無）」，⛔ 不得以不印代表無。
    """
    _skel2fam = {}
    for fam, sks in GATE_FAMILIES.items():
        for sk in sks:
            _skel2fam[sk] = fam
    byfam, resid_a, empty = {}, [], []
    hit = set()
    for ln, msg in rows:
        sk = _skeleton(msg)
        if not sk:
            empty.append((ln, msg))
            continue
        fam = _skel2fam.get(sk)
        if fam is None:
            resid_a.append((ln, sk))                  # 方向甲：骨架無對應登記族
            continue
        byfam.setdefault(fam, []).append(ln)
        hit.add(sk)
    resid_b = [(fam, sk) for fam, sks in GATE_FAMILIES.items()
               for sk in sks if sk not in hit]        # 方向乙：登記族無對應 raise（登記表過期）
    return byfam, resid_a, resid_b, empty


def main():
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8")
        except Exception:
            pass
    os.makedirs(OUTDIR, exist_ok=True)
    rows, fn_start, fn_end = _extract()

    L = []
    L.append("=" * W)
    L.append("【D-2b-9 §A′-2】`run_step_g` 之 `raise` 清單（**自原始碼解析生成**·⛔ 非人手抄）")
    L.append("=" * W)
    L.append("🔧 **具名更正**：本表**取代** `verify/out/probe_D2b8_guard.log`【B】段之閘位對應。")
    L.append("   被取代者（該檔所載·**錯誤**）：" +
             "／".join(f":{n} {t}" for n, t in D2B8_WRONG))
    L.append("   錯因：行號係人手抄自 D-2b-8【A】**修改之前**之 grep，【A】之插入使其後全部位移；")
    L.append("   現查（本 commit 之父 `f8674de`）`:1276` 實為 `if _nrm_a < 1e-9:`、")
    L.append("   `:1323` 實為 `if _pool_total_blk is not None:` ——**兩者皆非 `raise`**。")
    L.append("   ⛔ `probe_D2b8_guard.log` **一字未刪未改**（已入庫實料）。")
    L.append(f"   ⚠️ 本表行號係**本 commit** 之值；D-2b-9【A′-1】已於 `_guard_auth_scope` 內"
             f"新增一個 `raise` ⇒ 其後行號較 `f8674de` 位移。")
    L.append("")
    L.append(f"🔒 解析範圍：`verify/stepg_pipeline.py` 之 `def run_step_g`"
             f"（行 {fn_start}）至下一頂層 `def`（行 {fn_end}）")
    L.append(f"🔒 **解析母體 ＝ {len(rows)} 筆 `raise`**（⛔ 非空·空即 raise 失敗）")
    L.append("")
    L.append(f"{'#':>3}  {'行號':>6}  訊息首行實文")
    L.append("-" * W)
    for i, (ln, msg) in enumerate(rows, 1):
        L.append(f"{i:>3}  {ln:>6}  {msg[:170]}")

    L.append("")
    L.append("【閘族歸併】🆕 **D-2b-10 §前-1**：骨架正規化 ＋ 明列登記表 ＋ **雙向對帳**")
    L.append("-" * W)
    L.append("  🔴 舊 `_family()` 之 `（其他）` **萬用桶已刪**——其曾把 `:575`（條件③ J 非零看守破）")
    L.append("     與 `:819`（停機②（J 下降））**兩個不同族併為一桶** ⇒ 舊載「閘族數 14」**應為 15**。")
    fam, resid_a, resid_b, empty = _reconcile(rows)
    for k in GATE_FAMILIES:
        v = fam.get(k)
        _cov = "　🔑 **覆蓋閘之外層**" if "抵費地計算失敗" in k else ""
        L.append(f"  {k:<34} 行號 {v if v else '（無對應 raise）'}{_cov}")
    L.append(f"  ⇒ **閘族數 ＝ {len(GATE_FAMILIES)}**（登記表明列·⛔ 非回退鏈推得）")
    L.append("")
    L.append("  🔒 **雙向對帳**（⛔ 兩方向殘差**皆須逐字印出**·含「（無）」）")
    L.append(f"    **殘差甲**（`raise` 之骨架無對應登記族）："
             + ("（無）" if not resid_a else ""))
    for ln, sk in resid_a:
        L.append(f"        🔴 :{ln}  骨架 |{sk}|")
    L.append(f"    **殘差乙**（登記族無對應 `raise`＝登記表過期）："
             + ("（無）" if not resid_b else ""))
    for f_, sk in resid_b:
        L.append(f"        🔴 族「{f_}」之骨架 |{sk}| 查無對應 raise")
    L.append(f"    **無法正規化**（骨架為空）：" + ("（無）" if not empty else ""))
    for ln, msg in empty:
        L.append(f"        🔴 :{ln}  {msg[:120]}")
    if resid_a or resid_b or empty:
        raise RuntimeError(
            f"🔴 閘族雙向對帳破：殘差甲 {len(resid_a)} 筆／殘差乙 {len(resid_b)} 筆／"
            f"空骨架 {len(empty)} 筆 ——⛔ 不得以新增鍵或放寬正規化「修掉」，停機上呈。"
            f"　甲={resid_a}　乙={resid_b}　空={[l for l, _ in empty]}")
    L.append("    ⇒ ✅ 兩方向殘差**皆空**（母體 "
             f"{len(rows)} 筆 `raise` ⇒ **非空**·⛔ 與殘差之空方向相反）")

    # ══════ 驗收 1／2：零行為變更（原文並列）＋ 退化命中實值列舉 ══════
    import contextlib
    sys.path.insert(0, VERIFY)
    from app_harvest import harvest                                 # noqa: E402
    import run_verification as rv                                   # noqa: E402
    from selection_pipeline import run_corner_pk                    # noqa: E402
    from stepg_pipeline import run_step_g                           # noqa: E402

    def _base(path, marker):
        """自已入庫 log 解析 `[情境] 街廓 … 終止例外` 之基準（⛔ 不改原檔）。"""
        out = {}
        try:
            body = io.open(path, encoding="utf-8").read().split(marker, 1)[1]
        except Exception:
            return out
        for ln in body.splitlines():
            if ln.lstrip().startswith("【"):
                break                      # 🔴 停在**下一個節標題**（否則後節同鍵會覆寫·D-2b-9 自查）
            m = re.match(r"\s*\[(0m|3\.5m)\]\s+(R\d)\s", ln)
            if not m or "｜" not in ln:
                continue
            out[(m.group(1), m.group(2))] = ln.split("｜", 1)[1].strip()
        return out

    B6 = _base(os.path.join(OUTDIR, "probe_D2b6_split.log"), "【III】")
    B8 = _base(os.path.join(OUTDIR, "probe_D2b8_guard.log"), "【A-3】")

    ns, fake_st = harvest()
    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp_p, build_p, _ = rv.build_build_parcels(
        ns, fake_st, v6, list(cb_by.values()), snapshot)
    cb_all = list(cb_by.values())
    _blks = []
    for tp in build_p:
        _l = tp.get("所屬街廓")
        if _l and _l not in _blks:
            _blks.append(_l)

    CUR, DEGEN = {}, []
    for setback in (0.0, 3.5):
        sb = f"{setback:g}m"
        params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
        _d0, _s2, _o2, wins, forced = run_corner_pk(
            ns, fake_st, cb_all, cad, params, temp_p, build_p, setback, snapshot=snapshot)
        for lbl in _blks:
            buf = io.StringIO(); err = ""
            with contextlib.redirect_stdout(buf):
                try:
                    run_step_g(ns, fake_st, cb_all, cad, snapshot, params,
                               [tp for tp in build_p if tp.get("所屬街廓") == lbl],
                               wins, forced, setback)
                except Exception as e:
                    err = f"{type(e).__name__}: {e}"
            CUR[(sb, lbl)] = err
            for ln in buf.getvalue().splitlines():
                if ln.startswith("[K-9-5-8]"):
                    DEGEN.append((sb, ln))

    L.append("")
    L.append("【驗收 1】零行為變更 —— **原文並列**（⛔ 不得只寫「相同」）")
    L.append("-" * W)
    _diff = 0
    for sb in ("0m", "3.5m"):
        for lbl in _blks:
            _c = CUR.get((sb, lbl), "")
            _b8 = B8.get((sb, lbl), "（基準未解析到）")
            _c_n = ("✅ 跑完（無例外）" if not _c else "🔴 " + _c)
            # 🔴 **前綴比對**（D-2b-9 自查）：已入庫基準之例外文於寫入時已被 `[:140]/[:150]`
            #   **截斷**（log 之格式限制）⇒ 直接全字串比對會把「截斷」誤判為「行為變更」。
            #   故比**共同前綴**，並要求重疊長度 ≥ 40 字（⛔ 太短之重疊不足以判同）。
            _n = min(len(_c_n), len(_b8))
            _same = (_n >= 40 and _c_n[:_n] == _b8[:_n]) or (_c_n == _b8)
            if not _same:
                _diff += 1
            L.append(f"  [{sb}] {lbl}　（比對法：共同前綴 {_n} 字·基準已截斷）")
            L.append(f"      基準(D-2b-8【A-3】)：{_b8[:165]}")
            L.append(f"      本批            ：{_c_n[:165]}")
            L.append(f"      ⇒ {'✅ 前綴逐字相同' if _same else '🔴 **不同**'}")
    L.append(f"  ⇒ 不同者 **{_diff}** 格／母體 **{len(_blks) * 2}** 格"
             + ("　✅ 零行為變更" if _diff == 0 else "　🛑 **停機**"))

    L.append("")
    L.append("【驗收 2】`K-9-5-8` 退化命中之**實值列舉**（⛔ 不得以「未觸發」代替列舉）")
    L.append("-" * W)
    if not DEGEN:
        L.append("  🔴 **無任何退化命中 ⇒ 新斷言所在分支從未執行·⛔ 結論不可據**")
    for sb, ln in DEGEN:
        L.append(f"  [{sb}] {ln[:180]}")
    L.append(f"  ⇒ 命中 **{len(DEGEN)}** 次。其中 `方向判準所得` 欄即 `_auth_lots` 實值、"
             f"`街角第 1 宗` 欄即 `_expect` 實值。")
    L.append("  🔒 **本批未取得任何新證據**：現行六街廓下 `_auth_lots` 為空 ⇒ 新斷言"
             "**預期不觸發**且實測未觸發。⛔ **不得**寫成「已驗證」「得佐證」或任何等價說法；")
    L.append("     本批之價值 ＝ **恢復守衛涵蓋範圍**（退化側不再被整條豁免），⛔ 非發現新事實。")

    L.append("")
    L.append("=" * W)
    txt = "\n".join(L)
    with io.open(LOG, "w", encoding="utf-8") as f:
        f.write(txt + "\n")
    print(txt)
    print(f"\n[written] {LOG}")


if __name__ == "__main__":
    main()
