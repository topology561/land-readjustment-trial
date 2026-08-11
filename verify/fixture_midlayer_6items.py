# -*- coding: utf-8 -*-
r"""`W-G.9-13`：**中間層 6 項**之獨立立閘（需 CAD 管線、⛔ 不需 `run_step_g`）。

## 為何（【裁定 B】·`docs/驗證裁定登記表.md`）

該 6 項之主判定寫在 `run_verification.py` 之財務段／`F.2`／`F.4` 段，
與**需 `run_step_g`** 之判定**同處一個 `try`**；上游結構閘另案一破，
整個 `try` 落入 `except` ⇒ **這 6 個命題從此不再被評估**（**考古 70**）。
本夾具把它們**獨立出來守**——自建 CAD 管線至其所需之層，⛔ **全程不經 `run_step_g`**。

## 🔒 判準之**四型**（⛔ 現查所得·⛔ 非假設同構）

| 型 | 判準來源 | 名目 |
|---|---|---|
| ① **內嵌數值字面** | 判準式內之數值常數 | `v3 率分項錨`／`v3 率用 DXF 公設實值` |
| ② **`_anc` 字典查值** | 自 `snapshot["財務接線_v3"]["斷言錨"]` 之**同一鍵**讀取 | `v3 重劃總負擔率錨`／`v3 reverse-test③` |
| ③ **自參照·無外部錨** | 期望值由被測函式**自己回傳** | `F.2 跨區段 fixture` |
| ④ **名單型** | 判準式內之字串 tuple | `F.4 模式二 p_avg` |

🔴 **第三種碼面形狀**（本批現查）：`W-G.9-10` 之 `G-2` 受詞為**內嵌式**
（`results.append((f"…", <expr>, …))`）；本 6 項之第二元素**皆為 `Name`**
（`_ok_rate`／`_ok_bd`／`_ok_dxf`／`_ok_rt3`／`_ok_fx`／`_m2ok`），
須**再解析其 `Assign`** 才取得判準式。⛔ 照 `G-2` 之形狀外推**會抽到一個變數名**、
其自由名與常數皆為空 ⇒ **受詞為空 ⇒ 恆綠**。此即 `W-G.9-12` 之 `F.2` 陷阱之本批版本。

## 🔒 同源（⛔ 夾具內不抄寫任何判準值·`#20` 族）

本檔**不持有**任何錨值：判準式**自 `verify/run_verification.py` 原碼 AST 抽取後
＜就地求值＞**（`_eval_criterion`）——⛔ 非「抄下常數再自己比一次」。
⇒ 原碼一改，本夾具**跟著改**；⛔ 無漂移空間。

⚠️ **唯一之明示例外（型③）**：`F.2` 無外部錨 ⇒ 依施工單 §2-2 之型③作法，
另存**原式之正規化原始碼文字**作同源自證（原式一變即 **loud 紅**）。
🔒 該文字**不含任何外部錨值**（`0.01` 為容差；期望值 `expect_m1` 由被測函式自己回傳）。
此係 `fixture_g3_static_guards.py` 之 `G-2` 已立之同型手段。

## 🔒 四項聲明（`W-G.9-10` §2-4·⛔ 逐條·第 2、4 項不得留空）

### 1. 本閘守的是原命題之哪個子集？

**六項之判準式全部**——⛔ 未縮受詞。每項皆以**原式就地求值**，
其自由名（`_anc`／`_rate_live`／`_bd`／`_rate3`／`_fx`／`_pavg`）
由本夾具**自建之真管線**產生，⛔ 非合成、⛔ 非快照抄錄。

### 2. 🔴 放棄了哪個子集？其後果是什麼？

| 放棄 | 後果（**本閘不看**） |
|---|---|
| 該六項所在 `try` 內**其餘**主判定（`v3 財務錨 B`／`C`／`中繼錨`／`C 兩形等價`／`A 逐宗全查`／`reverse-test①②`） | **完全未守**。其中 `A 逐宗全查`／`reverse-test①②` **實需** `run_step_g`（走 `stepg_ctx`／`_rerun_fin`）⇒ 現況**不可能**由本夾具覆蓋；`B`／`C`／`中繼錨`／`C 兩形等價` 則**在上游 raise 之前即已執行**（見 `W-G.9-11` 全掃）⇒ 非本批受詞 |
| `F.2`／`F.4` 段內其餘主判定（守恆、位次序、正交、雙模式並列錨…） | **完全未守**——皆吃 `run_step_g` 之產物 |

⇒ 本閘守 **6 個**主判定之命題；**其餘仍無人守**（清單見 `W-G.9-11` 報告之守備移交清單）。

### 3. 本閘之受詞與既有 `except` 分支是否重疊？

**⛔ 不重疊。** 既有 `except` 分支（`v3 財務接線閘`／`W-F F.2`／`W-F F.4`）之受詞
＝ **compute 失敗之訊息**（已由 `W-G.9-7` 之對帳凍存）；
本閘之受詞 ＝ **命題本身之真偽**。⇒ 二者為**不同述詞**。

### 4. 另案修好之後，本閘會怎樣？

**仍綠、且應併同檢討退場。** 本閘之受詞與 `run_step_g` **無關**
（自建層 A/B/C 即足）⇒ ⛔ **不會假紅**。
⚠️ 屆時 `run_verification` 內之原判定亦將復活 ⇒ 同一命題兩處判定，
**惟二者同源**（本夾具就地求值原式）⇒ ⛔ 不會出現「兩處判準分歧」，
但**應併同檢討本夾具是否退場**（與 `fixture_g3_static_guards.py` 同）。

## 重跑
    python verify/fixture_midlayer_6items.py       # rc=0 ⇒ 綠
"""
import ast
import builtins
import copy
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, HERE)

RV = os.path.join(HERE, "run_verification.py")
# 🔒 母體自證（考古 69 修法 ①）：⛔ 指錯檔即全綠假象
assert os.path.exists(os.path.join(REPO, "CLAUDE.md")), f"🔴 REPO 不是倉根：{REPO}"
assert os.path.exists(RV), f"🔴 母體檔不存在：{RV}"
_RV_SRC = open(RV, encoding="utf-8").read()
_RV_AST = ast.parse(_RV_SRC)
RC = [0]
_BI = set(dir(builtins))


def red(msg):
    print(f"  🔴 {msg}")
    RC[0] = 1


# ══════════════════════════════════════════════════════════════════════════
# 同源抽取：**一份邏輯**（⛔ 不為每型各寫一份·`#20` 族）
# ══════════════════════════════════════════════════════════════════════════
_PAR = {}
for _n in ast.walk(_RV_AST):
    for _c in ast.iter_child_nodes(_n):
        _PAR[_c] = _n


def _name_lit(node):
    a0 = node.args[0]
    t = a0.elts[0] if isinstance(a0, (ast.Tuple, ast.List)) and a0.elts else a0
    if isinstance(t, ast.Constant) and isinstance(t.value, str):
        return t.value
    if isinstance(t, ast.JoinedStr):
        return "".join(v.value if isinstance(v, ast.Constant) and isinstance(v.value, str)
                       else "{…}" for v in t.values)
    return None


def orig_criterion(prefix):
    """回 `(名目字面, 判準式節點, 正規化原始碼, 所屬 try 節點)`——自原碼 AST 抽取。

    🔒 **一份邏輯吃兩種形狀**：
      ① `results.append((f"…", <inline expr>, …))`（`W-G.9-10` 之 `G-2`）
      ② `results.append((f"…", <Name>, …))` ⇒ **再解析該 `Name` 於同一 `try` 內之 `Assign`**
         （本批 6 項**皆屬此形**·⛔ 照 ① 外推會抽到變數名 ⇒ 受詞為空 ⇒ 恆綠）
    """
    site = None
    for n in ast.walk(_RV_AST):
        if (isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)
                and n.func.attr == "append" and isinstance(n.func.value, ast.Name)
                and n.func.value.id == "results"
                and isinstance(n.args[0], (ast.Tuple, ast.List)) and len(n.args[0].elts) >= 2
                and (_name_lit(n) or "").startswith(prefix)):
            site = n
    if site is None:
        raise RuntimeError(f"🔴 同源抽取失敗：找不到 `{prefix}` 之站點")
    tr = _PAR.get(site)
    while tr is not None and not isinstance(tr, ast.Try):
        tr = _PAR.get(tr)
    if tr is None:
        raise RuntimeError(f"🔴 同源抽取失敗：`{prefix}` 不在任何 `try` 內")
    node = site.args[0].elts[1]
    if isinstance(node, ast.Name):
        found = None
        for st in ast.walk(tr):
            if (isinstance(st, ast.Assign)
                    and any(getattr(t, "id", "") == node.id for t in st.targets)):
                found = st.value
        if found is None:
            raise RuntimeError(f"🔴 同源抽取失敗：`{prefix}` 之 `{node.id}` 於其 `try` 內無賦值")
        node = found
    src = " ".join((ast.get_source_segment(_RV_SRC, node) or "").split())
    if not src:
        raise RuntimeError(f"🔴 同源抽取失敗：`{prefix}` 之判準式原始碼為空")
    return _name_lit(site), node, src, tr


# ── 讀取器（⛔ 皆讀**同一次抽取**之節點·非另做抽取） ───────────────────────
def free_names(node):
    """判準式之自由名（⛔ 扣除 builtins 與 comprehension 綁定名）。"""
    bound = set()
    for x in ast.walk(node):
        for g in getattr(x, "generators", []) or []:
            for t in ast.walk(g.target):
                if isinstance(t, ast.Name):
                    bound.add(t.id)
    return sorted({x.id for x in ast.walk(node) if isinstance(x, ast.Name)} - _BI - bound)


def numbers(node):
    """判準式內之數值常數（型①之受詞）。"""
    return [c.value for c in ast.walk(node)
            if isinstance(c, ast.Constant) and isinstance(c.value, (int, float))
            and not isinstance(c.value, bool)]


def keys_under(node, base):
    """判準式內 `base[...]` 之字串鍵（型②之受詞）。"""
    out = []
    for x in ast.walk(node):
        if (isinstance(x, ast.Subscript) and isinstance(x.value, ast.Name)
                and x.value.id == base and isinstance(x.slice, ast.Constant)
                and isinstance(x.slice.value, str)):
            out.append(x.slice.value)
    return out


def string_tuple(node):
    """判準式內之字串 tuple（型④之受詞）。"""
    for x in ast.walk(node):
        if (isinstance(x, (ast.Tuple, ast.List)) and x.elts
                and all(isinstance(e, ast.Constant) and isinstance(e.value, str)
                        for e in x.elts)):
            return tuple(e.value for e in x.elts)
    return ()


def setup_const(try_node, key):
    """同一 `try` 內對 `…[key]` 之賦值常數（**擾動設定**·⛔ 非判準值）。"""
    for st in ast.walk(try_node):
        if isinstance(st, ast.Assign):
            for t in st.targets:
                if (isinstance(t, ast.Subscript) and isinstance(t.slice, ast.Constant)
                        and t.slice.value == key and isinstance(st.value, ast.Constant)):
                    return st.value.value
    raise RuntimeError(f"🔴 同源抽取失敗：`try` 內找不到對 `{key}` 之賦值常數")


def eval_criterion(node, ns):
    """**就地求值**原判準式（⛔ 不抄常數、⛔ 不自己重寫比較式）。

    🔒 自由名若有一個未綁定 ⇒ `NameError` **loud 紅**（⛔ 不靜默當偽）。

    🔴 **命名空間須以 `globals` 傳入**（`W-G.9-13` 實跑抓到）：型④ 之
    `all(b in _pavg for b in (…))` 內含 **genexp**，其於 `eval` 中**另開 scope**，
    自由名只查 `globals`、⛔ **不查傳入之 `locals`** ⇒ 若分傳 `globals/locals`
    會得 `NameError: _pavg`。⛔ 此處**不得**以 `except: return False` 吞掉
    ——那會把「求值機制壞掉」偽裝成「命題為偽」而誤觸 `A-2`。
    """
    miss = [n for n in free_names(node) if n not in ns]
    if miss:
        raise RuntimeError(f"🔴 就地求值失敗：自由名未綁定 {miss}")
    g = {"__builtins__": builtins}
    g.update(ns)
    return bool(eval(compile(ast.Expression(body=node), "<原判準式>", "eval"), g))


# 🔒 型③（`F.2`）無外部錨 ⇒ 依施工單 §2-2 存**原式之正規化原始碼文字**作同源自證。
#    ⚠️ 該文字⛔ 不含任何外部錨值（容差 `0.01`；期望值由被測函式自己回傳）。
_F2_EXPR_FROZEN = ('_fx["ratio_ne_1"] and abs(_fx["mode1_a_to_b"] - _fx["expect_m1"]) < 0.01 '
                   'and _fx["mode1_a_to_b"] > _fx["a"]')


# ══════════════════════════════════════════════════════════════════════════
# 管線層（**setup·⛔ 非判準**）：A ＝ harvest＋快照｜B ＝ build_pipeline｜C ＝ build_parcels
#   🔒 全程 ⛔ 不呼叫 `run_step_g`（本夾具存在之全部理由）。
# ══════════════════════════════════════════════════════════════════════════
_S = {}


def stage_A():
    if "A" not in _S:
        from app_harvest import harvest
        import run_verification as rv
        snap = rv.load_snapshot()
        ns, fake_st = harvest()
        _S["A"] = {"rv": rv, "snap": snap, "ns": ns, "fake_st": fake_st}
    return _S["A"]


def stage_B():
    if "B" not in _S:
        a = stage_A()
        cb_by, cad = a["rv"].build_pipeline(a["ns"], a["fake_st"], a["snap"])
        _S["B"] = {"cb_by": cb_by, "cad": cad}
    return _S["B"]


def stage_C():
    """⚠️ `W-G.9-13` 實跑判定：`build_build_parcels` **不需** `build_ownership` 先行。"""
    if "C" not in _S:
        a, b = stage_A(), stage_B()
        from selection_pipeline import build_build_parcels
        with open(a["rv"].V6DXF, "rb") as f:
            v6 = f.read()
        _, bp, _sw = build_build_parcels(a["ns"], a["fake_st"], v6,
                                         list(b["cb_by"].values()), a["snap"])
        _S["C"] = {"build_parcels": bp}
    return _S["C"]


# ══════════════════════════════════════════════════════════════════════════
# 六項之命名空間建置（⛔ 自由名一律由**真管線**產生）
# ══════════════════════════════════════════════════════════════════════════
def ns_rate(try_node=None):
    a, _ = stage_A(), stage_B()
    ss = a["fake_st"].session_state
    return {"_anc": a["snap"]["財務接線_v3"]["斷言錨"],
            "_rate_live": float(ss["f3_total_burden_rate_from_finance"]),
            "_bd": ss["_v3_burden_rate_breakdown"]}


def ns_rt3(try_node):
    """型② `reverse-test③`：擾動幅度**自同一 `try` 同源抽取**（⛔ 不寫死）。"""
    from stepg_pipeline import compute_total_burden_rate
    a, b = stage_A(), stage_B()
    key = "單位工程費_元每m2"          # ⚠️ 設定之**定位鍵**（⛔ 非判準值）
    mag = setup_const(try_node, key)
    s3 = copy.deepcopy(a["snap"])
    s3["財務接線_v3"][key] = mag
    rate3, _ = compute_total_burden_rate(a["ns"], list(b["cb_by"].values()), s3)
    d = ns_rate()
    d["_rate3"] = rate3
    d["_擾動幅度"] = mag
    return d


def ns_f2(try_node=None):
    import wf_f2
    a, c = stage_A(), stage_C()
    return {"_fx": wf_f2.fixture_cross_zone(a["snap"], c["build_parcels"])}


def ns_f4(try_node=None):
    import wf_f4
    a, c = stage_A(), stage_C()
    _pre, pavg = wf_f4.fixture_mode2_hand(a["snap"], c["build_parcels"])
    return {"_pavg": pavg}


# ── 竄改態（⛔ 每閘皆須·兩態皆印） ─────────────────────────────────────────
def t_rate(ns):
    d = dict(ns)
    d["_rate_live"] = ns["_rate_live"] + 1.0
    return d, "`_rate_live` +1.0"


def t_bd(ns, key):
    d = dict(ns)
    bd = dict(ns["_bd"])
    bd[key] = bd[key] * 2.0
    d["_bd"] = bd
    return d, f"`_bd[{key!r}]` ×2"


def t_rt3(ns):
    d = dict(ns)
    d["_rate3"] = ns["_rate_live"]          # 率「未隨動」＝原式所欲抓之失效態
    return d, "`_rate3` 改為與 `_rate_live` 相同（＝率未隨動）"


def t_f2(ns):
    d = dict(ns)
    fx = dict(ns["_fx"])
    fx["mode1_a_to_b"] = fx["expect_m1"] + 1.0
    d["_fx"] = fx
    return d, "`_fx['mode1_a_to_b']` 改為 `expect_m1`+1.0（超出容差）"


def t_f4(ns, tup):
    d = dict(ns)
    pavg = {k: v for k, v in ns["_pavg"].items() if k != tup[-1]}
    d["_pavg"] = pavg
    return d, f"`_pavg` 移除 {tup[-1]!r}"


# ══════════════════════════════════════════════════════════════════════════
ITEMS = (
    ("v3 重劃總負擔率錨 ==", "②", ns_rate, t_rate),
    ("v3 率分項錨 公設負擔比", "①", ns_rate, lambda n: t_bd(n, "公設負擔比")),
    ("v3 率用 DXF 公設實值", "①", ns_rate, lambda n: t_bd(n, "公設共同負擔_DXF")),
    ("v3 reverse-test③ 單位工程費", "②", ns_rt3, t_rt3),
    ("F.2 跨區段 fixture（a→b 模式一", "③", ns_f2, t_f2),
    ("F.4 模式二 p_avg 母體", "④", ns_f4, None),
)


def main():
    print("=" * 100)
    print("【`W-G.9-13`】中間層 6 項獨立閘（需 CAD 管線·⛔ 不需 `run_step_g`）")
    print("=" * 100)
    done = 0
    for prefix, kind, mkns, tamper in ITEMS:
        try:
            lit, node, src, tr = orig_criterion(prefix)
        except Exception as e:
            red(f"{prefix}｜{e}")
            continue
        fn = free_names(node)
        if not fn:
            red(f"{prefix}｜🔴 抽出之受詞**自由名為空** ⇒ 恆綠風險（`A-4`）")
            continue
        print(f"  ▸ 型{kind}｜`{prefix}`")
        print(f"      判準式（同源·就地求值）＝ {src}")
        if kind == "①":
            print(f"      受詞（數值常數）＝ {numbers(node)}")
        elif kind == "②":
            ks = keys_under(node, "_anc")
            print(f"      受詞（`_anc` 之鍵·同源讀取⛔ 非抄值）＝ {ks}")
            if not ks:
                red(f"{prefix}｜型② 之 `_anc` 鍵抽取為空（`A-4`）")
                continue
        elif kind == "③":
            if src != _F2_EXPR_FROZEN:
                red(f"{prefix}｜🔴 同源自證破：原式已改\n       凍存：{_F2_EXPR_FROZEN}\n"
                    f"       現況：{src}")
                continue
            print("      受詞（型③ 無外部錨）＝ 原式之正規化原始碼 ✅ 與凍存逐字相同")
        elif kind == "④":
            tup = string_tuple(node)
            print(f"      受詞（字串 tuple）＝ {tup}")
            if not tup:
                red(f"{prefix}｜型④ 之 tuple 抽取為空（`A-4`）")
                continue
            tamper = (lambda n, _t=tup: t_f4(n, _t))
        try:
            ns = mkns(tr)
            ok = eval_criterion(node, ns)
        except Exception as e:
            red(f"{prefix}｜實跑失敗（`A-1`）：{type(e).__name__}: {e}")
            continue
        done += 1
        print(f"      自由名 {fn} ⇒ 皆由真管線綁定")
        print(f"      原態 ⇒ {'✅ 綠' if ok else '🔴 **紅**'}")
        if not ok:
            red(f"{prefix}｜現況為紅 ⇒ `A-2`：⛔ 不得調錨／縮受詞／放寬容差，停機上呈 KL")
        # 🔒 竄改自檢（考古 69 修法 ④·兩態皆印）
        tns, what = tamper(ns)
        tok = eval_criterion(node, tns)
        print(f"      竄改態（{what}）⇒ {'🔴 仍綠（**無鑑別力**）' if tok else '✅ 轉紅 ⇒ 具鑑別力'}")
        if tok:
            red(f"{prefix}｜竄改自檢無鑑別力（`A-3`）⇒ 本閘不得計入交付")
    print("-" * 100)
    # 🔒 受詞必被執行之現查（⛔ 不以「沒報錯」代替）
    print(f"  已求值之判準式 ＝ {done}／{len(ITEMS)}")
    if done != len(ITEMS):
        red(f"僅 {done}／{len(ITEMS)} 之判準式被求值 ⇒ 其餘**未被執行**（⛔ 不得計為守住）")
    print(f"{'✅ 夾具 PASS（rc=0）' if RC[0] == 0 else '🔴 夾具 FAIL（rc=1）'}")
    return RC[0]


if __name__ == "__main__":
    sys.exit(main())
