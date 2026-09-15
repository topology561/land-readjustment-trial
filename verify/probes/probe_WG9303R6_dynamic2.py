"""`W-G.9-303`　`§四` 款 `3`／`4` 之動態量測器 **v2（器紅之修）**。

🩸 **v1 之二紅（自捕·⛔ 頂替·⛔ 覆寫 `verify/out/WG9303R6_dynamic.log`）**
  紅① **重複包裝**：`RV.harvest` 被呼叫**多次**（`main()` 與 `n19p_depth_by_block()` 各一），
      而 v1 之 `wrap()` 每次都再包一層 ⇒ 每次呼叫被錄**兩次**，外層錄真呼叫端、內層錄
      `cbs2`／`sgo2`（＝本器）⇒ 「器自身」欄由 `0` 變成與生產錄**等量**（`21/21`・`2065/2065`）。
      **修**：以屬性旗標令包裝**冪等**。
  紅② 🔴 **二受詞之 `side` 口徑不同**：`_corner_buffer_S` 之 `side` ＝ `left`／`right`；
      `_solve_G_one` 之 `side` ＝ `左側`／`右側`。v1 直接以原值作集合比較
      ⇒ `(甲) ∖ (乙)` **恆為全量**、`(甲) ⊆ (乙)` **恆偽** ⇒ 款 `4` 之判為**假象**。
      **修**：二者各**正規化**至同一詞彙，且**原值與正規值並報**。

🔒 ⛔ 改生產碼一字（本器只於行程內包裝 `ns` 之二鍵）；⛔ 動任何既有探針一字。
🛑 `id(·)` ⛔ 作錨；量測器之母體⛔ 含其自身輸出；`f_locals` 鍵須自證存在並增第二鍵。
🛑 (乙) 不可得者一律 **loud 具名其分項成因**·⛔ 判為零、⛔ 判為空。
"""
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
SELF = os.path.abspath(__file__)
sys.path.insert(0, VERIFY)

assert "WV_BAKE" not in os.environ, "🛑 `WV_BAKE` 已設 ⇒ 停"

REC_BUF, REC_SOL, MISS = [], [], []
WRAP_CALLS = {"harvest": 0, "wrap": 0, "skipped": 0}

# 🔒 側別之正規化（**二詞彙並存係碼面事實·⛔ 本器所造**）
SIDE_MAP = {"left": "L", "right": "R", "左側": "L", "右側": "R",
            "左": "L", "右": "R"}
BLK_KEYS = ["blk_label", "_lbl", "blk", "lbl", "label", "_blk"]


def canon(s):
    return SIDE_MAP.get(str(s).strip(), "?<%r>" % (s,))


def caller_chain(depth=30):
    out, f = [], sys._getframe(2)
    while f is not None and len(out) < depth:
        c = f.f_code
        out.append((c.co_filename, c.co_name, c.co_firstlineno))
        f = f.f_back
    return out


def find_blk():
    """上溯 frame 鏈找街廓之名：**多鍵並取**，回 (值, 命中之鍵, 同框之其他命中鍵, 框名)。"""
    f = sys._getframe(2)
    while f is not None:
        L = f.f_locals
        for k in BLK_KEYS:
            if k in L and isinstance(L[k], str) and L[k]:
                others = [x for x in BLK_KEYS if x in L and x != k]
                return (L[k], k, others, f.f_code.co_name)
        f = f.f_back
    return (None, None, [], None)


def wrap(ns):
    WRAP_CALLS["wrap"] += 1
    if getattr(ns.get("_corner_buffer_S"), "_wg9303_wrapped", False):
        WRAP_CALLS["skipped"] += 1              # 🔒 冪等（紅① 之修）
        return ns
    cbs, sgo = ns["_corner_buffer_S"], ns["_solve_G_one"]

    def cbs2(*a, **kw):
        ch = caller_chain()
        blk, key, others, fnm = find_blk()
        REC_BUF.append({
            "_label": kw.get("_label", a[7] if len(a) > 7 else ""),
            "side_raw": kw.get("side", a[5] if len(a) > 5 else None),
            "caller": ch[0] if ch else None, "frame_blk": blk,
            "frame_key": key, "frame_others": others, "frame_fn": fnm,
            "self": bool(ch) and os.path.abspath(ch[0][0]) == SELF,
        })
        return cbs(*a, **kw)
    cbs2._wg9303_wrapped = True

    def sgo2(*a, **kw):
        ch = caller_chain()
        if "is_corner" not in kw:
            MISS.append("`_solve_G_one` 之 `is_corner` **非關鍵字傳入** ⇒ 該次⛔ 可得")
        blk, key, others, fnm = find_blk()
        if blk is None:
            MISS.append("frame 鏈**查無** %s 任一鍵 ⇒ 該次之街廓⛔ 可得（呼叫端 `%s`）"
                        % (BLK_KEYS, ch[0][1] if ch else None))
        REC_SOL.append({
            "is_corner": kw.get("is_corner"), "side_raw": kw.get("side"),
            "blk": blk, "frame_key": key, "frame_others": others, "frame_fn": fnm,
            "caller": ch[0] if ch else None,
            "self": bool(ch) and os.path.abspath(ch[0][0]) == SELF,
        })
        return sgo(*a, **kw)
    sgo2._wg9303_wrapped = True

    ns["_corner_buffer_S"], ns["_solve_G_one"] = cbs2, sgo2
    return ns


import run_verification as RV                                  # noqa: E402

_orig = RV.harvest


def harvest2():
    WRAP_CALLS["harvest"] += 1
    ns, fs = _orig()
    return wrap(ns), fs


RV.harvest = harvest2

BAR = "=" * 116
print(BAR)
print("【`W-G.9-303` `§四` 款 `3` 動態量測器 **v2**】`run_verification` 全量")
print(BAR)
sys.stdout.flush()

try:
    rc = RV.main()
except SystemExit as e:
    rc = e.code
except Exception as e:                                          # noqa: BLE001
    rc = "EXC: %r" % (e,)

print("\n" + BAR)
print("`run_verification.main()` 之 rc = %r" % (rc,))
print("包裝之冪等自證：`RV.harvest` 被呼叫 %d 次／`wrap()` 進入 %d 次／**因已包裝而跳過 %d 次**"
      % (WRAP_CALLS["harvest"], WRAP_CALLS["wrap"], WRAP_CALLS["skipped"]))
print(BAR)

pb = [r for r in REC_BUF if not r["self"]]
sb = [r for r in REC_BUF if r["self"]]
ps = [r for r in REC_SOL if not r["self"]]
ss_ = [r for r in REC_SOL if r["self"]]

print("\n── 母體二欄分列（量測器之母體⛔ 含其自身輸出）──")
print("| 受詞 | 生產錄 | 器自身（**須 `0`**） | 判 |")
print("|---|---|---|---|")
print("| `_corner_buffer_S` | %d | %d | %s |" % (len(pb), len(sb), "✅" if not sb else "🔴"))
print("| `_solve_G_one` | %d | %d | %s |" % (len(ps), len(ss_), "✅" if not ss_ else "🔴"))
print("🔑 判別力：v1（**同一受詞·未冪等**）之器自身欄為 `21`／`2065`（非零）"
      "⇒ 本欄**⛔ 恆為 `0`**，其歸零係**修**之效")

print("\n── 二受詞之 `side` **原值詞彙**（🔴 碼面事實·⛔ 本器所造）──")
print("`_corner_buffer_S` 之 `side` 相異原值 = %s" % sorted({str(r["side_raw"]) for r in pb}))
print("`_solve_G_one`     之 `side` 相異原值 = %s" % sorted({str(r["side_raw"]) for r in ps}))
print("⇒ 二者**詞彙不同** ⇒ 集合比較**必須先正規化**（v1 未正規化 ⇒ 其差集為假象）")

print("\n── (甲) `_corner_buffer_S` 實走之**呼叫端 × 街廓 × 側**（全量·⛔ 只報基數）──")
if not pb:
    print("   🛑 **loud**：本跑零次呼叫")
agg = {}
for r in pb:
    cf = r["caller"][0]
    cf = os.path.relpath(cf, REPO) if os.path.abspath(cf).startswith(REPO) else cf
    k = (cf.replace("\\", "/"), r["caller"][1], str(r["_label"]).split("·")[0],
         str(r["side_raw"]), canon(r["side_raw"]))
    agg[k] = agg.get(k, 0) + 1
print("| 呼叫端檔 | 呼叫端函式 | 街廓 | 側(原值) | 側(正規) | 次數 |")
print("|---|---|---|---|---|---|")
for k in sorted(agg):
    print("| %s | %s | %s | %s | %s | %d |" % (k[0], k[1], k[2], k[3], k[4], agg[k]))
A = {(k[2], k[4]) for k in agg}
print("\n(甲)（正規化後）＝ %s   （基數 %d）" % (sorted(A), len(A)))
print("frame 自證：命中街廓 %d ／ 未命中 %d；命中之鍵分布 = %s；同框其他命中鍵 = %s"
      % (len([r for r in pb if r["frame_blk"]]), len([r for r in pb if not r["frame_blk"]]),
         sorted({r["frame_key"] for r in pb if r["frame_key"]}),
         sorted({x for r in pb for x in r["frame_others"]})))

print("\n── (乙) `is_corner` 為**真**之**街廓 × 側**（全量）──")
if not ps:
    print("   🛑 **loud**：`_solve_G_one` 零次呼叫 ⇒ (乙) ⛔ 可得")
tru = [r for r in ps if r["is_corner"]]
known = [r for r in tru if r["blk"]]
unk = [r for r in tru if not r["blk"]]
B = {(r["blk"], canon(r["side_raw"])) for r in known}
print("`is_corner` 分布：真 %d ／ 偽 %d ／ None %d"
      % (len(tru), len([r for r in ps if r["is_corner"] is False]),
         len([r for r in ps if r["is_corner"] is None])))
agg2 = {}
for r in known:
    k = (r["blk"], str(r["side_raw"]), canon(r["side_raw"]))
    agg2[k] = agg2.get(k, 0) + 1
print("| 街廓 | 側(原值) | 側(正規) | 次數 |")
print("|---|---|---|---|")
for k in sorted(agg2):
    print("| %s | %s | %s | %d |" % (k[0], k[1], k[2], agg2[k]))
print("\n(乙)（正規化後·**僅街廓可得者**）＝ %s   （基數 %d）" % (sorted(B), len(B)))
print("🛑 **街廓⛔ 可得之 `is_corner` 為真者 ＝ %d 次**（⛔ 判為零、⛔ 併入 (乙)）；"
      "其呼叫端分布 = %s" % (len(unk), sorted({r["frame_fn"] or str(r["caller"][1]) for r in unk})))

print("\n── (丙) 差集**逐項列舉**（正規化後）──")
print("(甲) ∖ (乙) = %s   （基數 %d）" % (sorted(A - B), len(A - B)))
print("(乙) ∖ (甲) = %s   （基數 %d）" % (sorted(B - A), len(B - A)))

print("\n── 款 `4`：**三態分列**（🛑 ⛔ 判其對土地之後果·⛔ 擬 fallback·⛔ 呈 KL）──")
if not ps:
    st = "③ **(乙) 不可得**"
elif unk:
    st = ("② **(甲) ⊄ (乙)**" if (A - B) else "① **(甲) ⊆ (乙)**") + \
         "　⚠️ **惟 (乙) 之 %d 次街廓⛔ 可得** ⇒ 本判之 (乙) 係**下界**" % len(unk)
else:
    st = "① **(甲) ⊆ (乙)**" if A <= B else "② **(甲) ⊄ (乙)**"
print("判 = %s" % st)
print("  ① (甲) ⊆ (乙) ? %s" % (A <= B))
print("  ② (甲) ∖ (乙) 之逐格 = %s" % sorted(A - B))
print("  ③ (乙) 是否不可得 ? %s" % (not ps))

print("\n── 🛑 不可得之**分項成因**（⛔ 判為零、⛔ 判為空）──")
if not MISS:
    print("   （無記錄）⛔ 讀為「無不可得之分項」")
for m in sorted(set(MISS)):
    print("   - %s   ×%d" % (m, MISS.count(m)))

print("\n" + BAR)
print("【本器⛔ 判其對土地之後果·⛔ 擬任何 fallback·⛔ 改生產碼一字】")
print(BAR)
