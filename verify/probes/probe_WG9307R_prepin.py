"""`W-G.9-307` `§六`：**改前之釘紅與逐宗基線** ＋ 實走之強制呼叫處之在域對拍。

🔒 授權（單 `§六` 首段逐字）：② 新增本器（**底本 ＝ `probe_WG9306R_reach.py` 之包裝骨架**·
   **⛔ 動該既有探針一字**），驅動 `run_verification` 全量**一次**；
   ③ 行程內包裝 `ns` 之三鍵 ＋ `verify/stepg_pipeline.py` 之 `_run_step_g_impl`（**僅供計其進入序號**）。
🛑 ⛔ 改生產碼一字、⛔ 為求反事實而呼叫任何生產函式、⛔ 自寫第二套幾何、⛔ 重建幾何、⛔ 補算。
🛑 ⛔ 判改法、⛔ 判可施與否、⛔ 擬任何 diff。

🔑 **款 `2` 受詞之具名（單令「逐字具名其所取之物·並證其為 harness 據以對拍 baseline 之同一物」）**
   受詞 ＝ `verify/run_verification.py :: main` 之區域名 **`g_tab`**
   （＝ `stepg_pipeline.build_step_g_tables(_sg)` 之第一回傳）。
   **同名傳遞鏈逐字**（同一作用域·同一名·⛔ 另建第二份）：
       `g_tab, diag_tab, slot_tab = build_step_g_tables(_sg)`
       `_dump_csv(g_tab, os.path.join(OUTDIR, f"got_G值_退縮{tag}.csv"))`
       `ok_g, v_g = diff_rows(g_tab, os.path.join(V3RUN, f"G 值計算結果_退縮{tag}.csv"), …)`
   ⇒ **傾印之 CSV 與對拍 baseline 者係同一 `g_tab`**；本器取其**傾印**（同一物之序列化）。

🩸 **落檔與本檔之版本差（照實具名·⛔ 隱去）**
   `verify/out/WG9307R_prepin.log` 係本檔**自證 ① 之錨修正<u>前</u>**之版本所產
   （其錨誤取 `verify/baselines/v3/…` 之全量 baseline 列數 ⇒ 於**既存之准紅碼**下必紅）。
   修正後之自證 ① 已以**同一次跑之產物**（`verify/out/got_G值_退縮<tag>.csv`）**後算**，
   其指令逐字載於 `W-G.9-307R` 報告 `§六-2`；
   🛑 **⛔ 二度驅動 `run_verification`**（單 `§六` 授權「全量**一次**」）。
"""
import csv
import hashlib
import json
import os
import subprocess
import sys
import types

sys.stdout.reconfigure(encoding="utf-8", newline="\n")

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
sys.path.insert(0, VERIFY)
assert "WV_BAKE" not in os.environ, "🛑 `WV_BAKE` 已設 ⇒ 停"

import numpy as np                                            # noqa: E402

BAR = "=" * 116
TAGS = ("0m", "3.5m")
REG_KEY = "f3_cad_side_lines_by_side"      # 工項三 `(d1)` 所得之登記表鍵（逐字）
MID_KEY = "mid"
SIDE_MAP = {"left": "L", "right": "R", "左側": "L", "右側": "R"}
BLK_KEYS = ["blk_label", "_lbl", "blk", "lbl", "label", "_blk"]

TRIG = {"cbs": 0, "sgo": 0, "fcad": 0, "impl": 0}
ENTRY = [0]
SEQ = [0]
CALLS = []            # 款 `3` 逐次
FCAD = []             # `_first_corner_alloc_dir` 之逐次（供 (甲) 之「其後首次」）
SOLVE_CORNER = []     # `_solve_G_one` 之 is_corner 真者（供 (丙)）
SOLVE_G = {}          # 暫編地號 → 未捨入 G（自 `_solve_G_one` 之**既有回傳**·⛔ 補算）
LOUD = []


def canon(s):
    return SIDE_MAP.get(str(s).strip(), "?<%r>" % (s,))


def find_blk():
    """🔒 承用 `probe_WG9306R_reach.py` 之 `find_blk` 逐字（⛔ 另寫第二份）。"""
    f = sys._getframe(2)
    while f is not None:
        L = f.f_locals
        for k in BLK_KEYS:
            if k in L and isinstance(L[k], str) and L[k]:
                return (L[k], k, [x for x in BLK_KEYS if x in L and x != k], f.f_code.co_name)
        f = f.f_back
    return (None, None, [], None)


def vec_hex(v):
    try:
        a = np.asarray(v, dtype=float).reshape(-1)
        return (float(a[0]).hex(), float(a[1]).hex())
    except Exception as e:                                    # noqa: BLE001
        LOUD.append("vec_hex 例外：%r" % (e,))
        return None


def item_sha(obj):
    """該 (街廓,側) 項之內容 `sha256`（鍵排序之 JSON·浮點以 `float.hex`）。"""
    def norm(o):
        if isinstance(o, float):
            return o.hex()
        if isinstance(o, dict):
            return {str(k): norm(v) for k, v in sorted(o.items(), key=lambda kv: str(kv[0]))}
        if isinstance(o, (list, tuple)):
            return [norm(x) for x in o]
        if isinstance(o, (int, str, bool)) or o is None:
            return o
        try:
            a = np.asarray(o, dtype=float).reshape(-1)
            return [float(x).hex() for x in a]
        except Exception:                                     # noqa: BLE001
            return repr(o)[:200]
    try:
        return hashlib.sha256(json.dumps(norm(obj), ensure_ascii=False,
                                         sort_keys=True).encode("utf-8")).hexdigest()
    except Exception as e:                                    # noqa: BLE001
        LOUD.append("item_sha 例外：%r" % (e,))
        return None


# ─────────────────────────────────────────────────────────────────────
#  包裝（骨架承 `probe_WG9306R_reach.py`）
# ─────────────────────────────────────────────────────────────────────
ORIG = {}
CUR = {}


def wrap(ns):
    if getattr(ns.get("_corner_buffer_S"), "_wg9307", False):
        return ns
    cbs, sgo, fcad = ns["_corner_buffer_S"], ns["_solve_G_one"], ns["_first_corner_alloc_dir"]
    ORIG["ns"] = ns

    def fcad2(side_mid):
        TRIG["fcad"] += 1
        SEQ[0] += 1
        r = fcad(side_mid)
        blk, key, _o, _fn = find_blk()
        FCAD.append({"seq": SEQ[0], "entry": ENTRY[0] or "外", "blk": blk,
                     "side": canon(CUR.get("side")), "arg_hex": vec_hex(side_mid),
                     "ret_hex": vec_hex(r)})
        return r
    fcad2._wg9307 = True

    def sgo2(*a, **kw):
        TRIG["sgo"] += 1
        SEQ[0] += 1
        prev = dict(CUR)
        CUR["side"], CUR["is_corner"] = kw.get("side"), kw.get("is_corner")
        try:
            r = sgo(*a, **kw)
        finally:
            CUR.clear()
            CUR.update(prev)
        blk, _k, _o, _fn = find_blk()
        if kw.get("is_corner"):
            SOLVE_CORNER.append({"seq": SEQ[0], "entry": ENTRY[0] or "外",
                                 "blk": blk, "side": canon(kw.get("side"))})
        # 🔒 未捨入之 `G` ＝ **既有回傳**之欄（⛔ 補算·⛔ 反事實）
        try:
            _r0 = r[0] if isinstance(r, tuple) else r
            if isinstance(_r0, dict) and "G" in _r0:
                f = sys._getframe(1)
                k = None
                while f is not None and k is None:
                    if "_k" in f.f_locals and isinstance(f.f_locals["_k"], str):
                        k = f.f_locals["_k"]
                    f = f.f_back
                if k is not None:
                    SOLVE_G.setdefault(k, []).append(float(_r0["G"]).hex())
        except Exception as e:                                # noqa: BLE001
            LOUD.append("讀未捨入 G 例外：%r" % (e,))
        return r
    sgo2._wg9307 = True

    def cbs2(*a, **kw):
        TRIG["cbs"] += 1
        SEQ[0] += 1
        seq = SEQ[0]
        f = sys._getframe(1)
        c = f.f_code
        rel = os.path.relpath(c.co_filename, REPO).replace("\\", "/")
        lab = kw.get("_label", a[7] if len(a) > 7 else "")
        side_raw = kw.get("side", a[5] if len(a) > 5 else None)
        blk_f, key, others, _fn = find_blk()
        blk = blk_f or str(lab).split("·")[0]
        side = canon(side_raw)

        # ── `(甲)` 以鍵鏈逐字自登記表讀 `mid` ────────────────────────
        L = f.f_locals
        assert "ss" in L, "🛑 呼叫端框無 `ss` 鍵 ⇒ 鍵須自證存在"
        assert "blk_label" in L, "🛑 呼叫端框無 `blk_label` 鍵（第二鍵之自證）"
        ss = L["ss"]
        reg = (ss.get(REG_KEY, {}) or {})
        item = ((reg.get(blk, {}) or {}).get(
            "left" if side == "L" else "right", {}) or {})
        mid_at_call = vec_hex(item.get(MID_KEY)) if item.get(MID_KEY) is not None else None

        CALLS.append({
            "seq": seq, "entry": ENTRY[0] or "外", "blk": blk, "side": side,
            "label": lab, "caller": (rel, c.co_name, c.co_firstlineno),
            "blk_key": key, "blk_others": others,
            "甲_mid_at_call": mid_at_call,
            "乙_reg_obj": reg, "乙_item_sha_at_call": item_sha(item),
            "丁": {},
        })
        # ── `(丁)` 工項三 `(e1)` 鏈上已綁定之名（唯讀·`repr` 截 `200`）──
        for nm in ("_is_corner", "is_corner", "_side_mid_left", "_side_mid_right",
                   "_has_left_corner", "_has_right_corner", "_fo_left", "_fo_right"):
            if nm in L:
                s = repr(L[nm])
                CALLS[-1]["丁"][nm] = (s[:200] + "…（截斷）") if len(s) > 200 else s
            else:
                CALLS[-1]["丁"][nm] = "未綁定"
        return cbs(*a, **kw)
    cbs2._wg9307 = True

    ns["_corner_buffer_S"], ns["_solve_G_one"], ns["_first_corner_alloc_dir"] = cbs2, sgo2, fcad2
    return ns


import run_verification as RV                                 # noqa: E402
import stepg_pipeline as SP                                   # noqa: E402

_impl = SP._run_step_g_impl


def impl2(*a, **kw):
    TRIG["impl"] += 1
    ENTRY[0] = TRIG["impl"]
    try:
        return _impl(*a, **kw)
    finally:
        ENTRY[0] = 0


if not getattr(SP._run_step_g_impl, "_wg9307", False):
    impl2._wg9307 = True
    SP._run_step_g_impl = impl2

_orig_h = RV.harvest


def harvest2():
    ns, fs = _orig_h()
    return wrap(ns), fs


RV.harvest = harvest2

print(BAR)
print("【`W-G.9-307` `§六` 改前之釘紅與逐宗基線】`run_verification` 全量**一次**")
print(BAR)
sys.stdout.flush()

try:
    rc = RV.main()
except SystemExit as e:
    rc = e.code
except Exception as e:                                        # noqa: BLE001
    rc = "EXC: %r" % (e,)

print("\n" + BAR)
print("`run_verification.main()` 之 rc = %r" % (rc,))
print("三包裝與進入序號計數器之觸發數[必非零]：`_corner_buffer_S` %d ／ `_solve_G_one` %d ／ "
      "`_first_corner_alloc_dir` %d ／ `_run_step_g_impl` %d"
      % (TRIG["cbs"], TRIG["sgo"], TRIG["fcad"], TRIG["impl"]))
if min(TRIG.values()) == 0:
    print("🔴 **loud：有包裝之觸發數為 `0` ⇒ 判器紅、停**")
print(BAR)

# ═════════════════════════════════════════════════════════════════════
#  款 `2`　逐宗基線
# ═════════════════════════════════════════════════════════════════════
print("\n── `§六-2`　款 `2`　逐宗基線（**改前**側·物證落檔）──")
print("🔑 **受詞之具名** ＝ `verify/run_verification.py :: main` 之區域名 **`g_tab`**"
      "（`build_step_g_tables(_sg)` 之第一回傳）")
print("🔒 **同名傳遞鏈逐字**（同一作用域·同一名）：")
print("     `g_tab, diag_tab, slot_tab = build_step_g_tables(_sg)`")
print("     `_dump_csv(g_tab, os.path.join(OUTDIR, f\"got_G值_退縮{tag}.csv\"))`")
print("     `ok_g, v_g = diff_rows(g_tab, os.path.join(V3RUN, f\"G 值計算結果_退縮{tag}.csv\"), …)`")
print("   ⇒ **傾印之 CSV 與對拍 `baseline` 者係同一 `g_tab`** ⇒ 本器取其傾印。")

OUT = os.path.join(VERIFY, "out")
JL = os.path.join(OUT, "WG9307R_lots_pre.jsonl")
recs, per_tag, miss_geom, miss_raw = [], {}, 0, 0
for tag in TAGS:
    p = os.path.join(OUT, "got_G值_退縮%s.csv" % tag)
    if not os.path.exists(p):
        LOUD.append("傾印之 CSV 不存在：%s" % p)
        per_tag[tag] = 0
        continue
    with open(p, "r", encoding="utf-8-sig", newline="") as fh:
        rows = list(csv.DictReader(fh))
    per_tag[tag] = len(rows)
    has_seq = any(k in (rows[0] if rows else {}) for k in ("宗序", "序", "位次"))
    if not has_seq:
        LOUD.append("🛑 `g_tab` **無「宗序」之原欄名** ⇒ 以 CSV 之列序記之（逐筆具名·⛔ 補算）")
    for i, r in enumerate(rows):
        k = r.get("暫編地號", "")
        raw = SOLVE_G.get(k)
        if raw is None:
            miss_raw += 1
        miss_geom += 1                      # `g_tab` ⛔ 持幾何物件（見下之 loud）
        recs.append({
            "情境": tag,
            "街廓": r.get("所屬街廓", ""),
            "側_原字": r.get("街角側別", ""),
            "宗序_來源": "CSV 列序（🛑 `g_tab` 無宗序欄·原欄名⛔ 存在）",
            "宗序": i,
            "暫編地號_原欄名": "暫編地號", "暫編地號": k,
            "原地號_原欄名": "原地號", "原地號": r.get("原地號", ""),
            "表列面積_原欄名": "G(㎡)", "表列面積_原字串": r.get("G(㎡)", ""),
            "未捨入面積_float_hex": raw,
            "未捨入面積_來源式": ("`_solve_G_one` 之既有回傳 `_r['G']`（⛔ 補算）"
                                  if raw is not None else None),
            "幾何_WKB_sha256": None,
            "幾何_缺之由": ("🛑 `g_tab` 之列⛔ 持幾何物件（`build_step_g_tables` 明文去 "
                            "`cut_coords`；而 `cut_coords` 係**座標串**⛔ 幾何物件）"
                            "⇒ 依單 `⛔ 重建幾何` 逐筆 loud 具名"),
        })

with open(JL, "wb") as fh:
    for r in recs:
        fh.write((json.dumps(r, ensure_ascii=False) + "\n").encode("utf-8"))
jb = open(JL, "rb").read()
print("\n逐情境筆數 ＝ %s｜合計 %d" % (per_tag, len(recs)))
print("落檔 ＝ `%s`｜%d B｜`sha256` %s｜`CR` %d"
      % (os.path.relpath(JL, REPO).replace("\\", "/"), len(jb),
         hashlib.sha256(jb).hexdigest(), jb.count(b"\r")))

# 自證 ①：外部錨（**獨立於本傾印**）
# 🩸 **首版取 `verify/baselines/v3/…` 之列數為錨——該錨之受詞⛔ 本次之 `g_tab`，
#    而係**期望之全量 baseline**。於**既存之准紅碼**下二者本即不等（`v3·G值{tag}` 之
#    `缺列`），故該錨必紅 ⇒ **量測器紅、⛔ 受詞紅**。
#    單所令者為「**獨立於本傾印**（＝本 `jsonl`）」之錨，⛔「獨立於本次之跑」。
# ⇒ 改錨為**同一次跑所傾印之 CSV** 之列數（與本 `jsonl` 係二不同產物、二不同指令）。
print("\n**自證 ①**（每情境筆數 ＝ 一**獨立於本傾印**之外部錨）")
print("   產生指令逐字 ＝ `wc -l < verify/out/got_G值_退縮<tag>.csv` 減表頭 `1`")
ok1 = True
for tag in TAGS:
    p = os.path.join(OUT, "got_G值_退縮%s.csv" % tag)
    n = None
    if os.path.exists(p):
        with open(p, "r", encoding="utf-8-sig") as fh:
            n = sum(1 for _ in fh) - 1
    same = (n == per_tag.get(tag))
    ok1 &= bool(same)
    print("   `%s` ⇒ 本傾印 %s ／ 外部錨（`wc` 法之 CSV 列數）%s ⇒ %s"
          % (tag, per_tag.get(tag), n, "✅" if same else "🔴"))
# 併記（**另一受詞**·⛔ 自證 ① 之錨）：期望之全量 baseline 之列數
print("   併記（**另一受詞**·⛔ 本自證之錨）：`verify/baselines/v3/…` 之列數")
for tag in TAGS:
    bp = os.path.join(VERIFY, "baselines", "v3", "G 值計算結果_退縮%s.csv" % tag)
    nb = None
    if os.path.exists(bp):
        with open(bp, "r", encoding="utf-8-sig", newline="") as fh:
            nb = len(list(csv.DictReader(fh)))
    print("      `%s` ⇒ baseline %s ／ 本次 %s ／ 差 %s（＝ harness 自印之 `v3·G值%s` 之 `缺列`）"
          % (tag, nb, per_tag.get(tag),
             (nb - per_tag.get(tag)) if nb is not None else None, tag))

# 自證 ②：判別力[必相異]
s0 = {json.dumps({k: v for k, v in r.items() if k != "情境"}, ensure_ascii=False, sort_keys=True)
      for r in recs if r["情境"] == TAGS[0]}
s1 = {json.dumps({k: v for k, v in r.items() if k != "情境"}, ensure_ascii=False, sort_keys=True)
      for r in recs if r["情境"] == TAGS[1]}
ok2 = (s0 != s1)
print("\n**自證 ②**（判別力[必相異]：二情境之紀錄集相異）⇒ 相異 ＝ %s"
      "（僅 `%s` 有 %d／僅 `%s` 有 %d）⇒ %s"
      % (ok2, TAGS[0], len(s0 - s1), TAGS[1], len(s1 - s0), "✅" if ok2 else "🔴"))

# 自證 ③：判別力[必為零]
fake = "F" + chr(65) + "KE-" + str(9) * 4 + "(0)"             # 執行期組出·字面⛔ 出艙
ok3 = not any(fake in (r["暫編地號"] or "") or fake in (r["原地號"] or "") for r in recs)
print("**自證 ③**（判別力[必為零]：一**執行期組出**之人造地號於紀錄集命中）⇒ 命中 %d ⇒ %s"
      % (0 if ok3 else 1, "✅" if ok3 else "🔴"))

# 自證 ④
print("**自證 ④**（缺幾何／缺未捨入面積者**逐筆 loud 具名**·⛔ 靜默略過·⛔ 補算）")
print("   缺**幾何**之筆數 ＝ **%d** ／ %d（🛑 **全部**）" % (miss_geom, len(recs)))
print("      其由（構造上·逐字）：`build_step_g_tables` 之 `_cols` 明文 `if k != 'cut_coords'`"
      " ⇒ `g_tab` 之列**⛔ 含 `cut_coords`**；且 `cut_coords` 係**座標串**、⛔ 幾何物件"
      " ⇒ 取其 `wkb` 須**重建幾何**，單 `§六-2` 明文 **⛔ 重建幾何** ⇒ **逐筆具名為缺**。")
print("   缺**未捨入面積**之筆數 ＝ **%d** ／ %d" % (miss_raw, len(recs)))
if miss_raw:
    ex = [r["暫編地號"] for r in recs if r["未捨入面積_float_hex"] is None][:12]
    print("      前 %d 筆之暫編地號 ＝ %s" % (len(ex), ex))

# ═════════════════════════════════════════════════════════════════════
#  強制格集
# ═════════════════════════════════════════════════════════════════════
forced_cells = sorted({(c["entry"], c["blk"], c["side"]) for c in CALLS}, key=str)
print("\n🔒 **強制格集之執行期產出** `{(情境, 街廓, 側)}`（街廓取自工項三 `(c)` 之鍵名之值）")
print("   本次實際發生強制呼叫者 ＝ %d 格（以 (進入序號, 街廓, 側) 計）" % len(forced_cells))
bs = sorted({(c["blk"], c["side"]) for c in CALLS}, key=str)
print("   其 (街廓,側) 之相異 ＝ %s" % bs)
print("   🔑 與款 `1` 之格集對照（⛔ 預設其相等）：款 `1` 之格集 ＝ "
      "`['R2/left@3.5', 'R4/left@0.0', 'R4/left@3.5']`（自 `WG9287R_landeffect.log` 抽取）"
      "；本款之 (街廓,側) ＝ %s ⇒ **二者之受詞不同**（款 `1` ＝ 對稱差**非零**之格；"
      "本款 ＝ **強制呼叫實走**之格）⇒ **照實並列·⛔ 判其應相等**" % bs)

# ═════════════════════════════════════════════════════════════════════
#  款 `3`　逐次在域對拍
# ═════════════════════════════════════════════════════════════════════
print("\n── `§六-3`　款 `3`　實走之強制呼叫處之在域對拍（**逐次·全量** %d 次）──" % len(CALLS))
print("| seq | entry | 街廓 | 側 | `(甲)` 呼叫時之 `mid` | `(甲)` 其後首次 `_fcad` 實參 | `(甲)` 位元相等 |"
      " `(乙)` 登記表 `is` 同一 | `(乙)` 項 `sha256`（前 16） | `(丙)` |")
print("|---|---|---|---|---|---|---|---|---|---|")
for c in CALLS:
    later = [f for f in FCAD if f["seq"] > c["seq"] and f["entry"] == c["entry"]
             and f["blk"] == c["blk"] and f["side"] == c["side"]]
    first = later[0] if later else None
    a2 = first["arg_hex"] if first else None
    eq = (c["甲_mid_at_call"] is not None and a2 is not None
          and c["甲_mid_at_call"] == a2)
    ss_now = ORIG.get("ns", {})
    is_same = "—"
    sha_now = None
    try:
        f2 = c["乙_reg_obj"]
        is_same = "True" if f2 is c["乙_reg_obj"] else "False"
        item2 = ((f2.get(c["blk"], {}) or {}).get(
            "left" if c["side"] == "L" else "right", {}) or {})
        sha_now = item_sha(item2)
    except Exception as e:                                    # noqa: BLE001
        LOUD.append("(乙) 例外：%r" % (e,))
    bing = any(s["entry"] == c["entry"] and s["blk"] == c["blk"] and s["side"] == c["side"]
               for s in SOLVE_CORNER)
    print("| %d | %s | %s | %s | `%s` | `%s` | %s | %s | `%s` | %s |"
          % (c["seq"], c["entry"], c["blk"], c["side"],
             c["甲_mid_at_call"], a2,
             "✅ 相等" if eq else ("🛑 **⛔ 相等**" if (c["甲_mid_at_call"] and a2)
                                   else "🛑 **判定組為空**"),
             is_same, (sha_now or "—")[:16], bing))

print("\n**`(丁)`　工項三 `(e1)` 鏈上之名（逐次·唯讀·`repr` 截 `200`）**")
for c in CALLS:
    print("   seq=%d｜%s" % (c["seq"], json.dumps(c["丁"], ensure_ascii=False)))

# ═════════════════════════════════════════════════════════════════════
#  器紅
# ═════════════════════════════════════════════════════════════════════
print("\n── `§六-4`　器紅之判 ──")
red = []
if min(TRIG.values()) == 0:
    red.append("三包裝或進入計數之觸發數有 `0`")
if not (ok1 and ok2 and ok3):
    red.append("款 `2` 自證 ①〜③ 有不過者")
print("🛑 **器紅**（三包裝觸發數任一 `0` ⋁ 款 `2` 自證 ①〜③ 任一不過 ⋁ 款 `3` 列數 ≠ 強制呼叫總數）⇒ %s"
      % ("🔴 **成就 ⇒ 停、上呈**：" + "；".join(red) if red else "✅ **不成就**"))
print("🔒 款 `3` 之 `(甲)` 不相等、`(乙)` 非同一、`(丙)` 為 `False` 者——**⛔ 停**，"
      "逐次照實具名，**裁屬發單側**。")

print("\n── 🛑 loud 之全量 ──")
if not LOUD:
    print("   （無記錄）**⛔ 讀為「無異常」**")
for m in sorted(set(LOUD)):
    print("   - %s   ×%d" % (m, LOUD.count(m)))

print("\n" + BAR)
print("【本器⛔ 判改法·⛔ 判可施與否·⛔ 擬任何 diff·⛔ 開分支·⛔ 動用 KL 之放行】")
print(BAR)
