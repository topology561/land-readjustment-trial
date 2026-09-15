"""`W-G.9-303`　`§四` 款 `3`／`4` 之**動態**量測器（`run_verification` 全量一次·零生產碼）。

🔒 **明文授權之二手段**（單 `§四` 首段）：① `run_verification` 全量**一次**；② 於 `verify/probes/` 新增器。
🔒 **⛔ 改生產碼一字**——本器只於**行程內**以包裝取代 `ns` 之二鍵（⛔ 動任何檔）。
🛑 **`id(·)` ⛔ 作錨**——呼叫端一律以 `(co_filename, co_name, co_firstlineno)` 序辨。
🛑 **量測器之母體⛔ 含其自身輸出**——生產錄／器自身**二欄分列**，後者須 `0`。
🛑 `f_locals` 之鍵須**自證存在**並**增第二鍵**。
🛑 **(乙) 若取法不可得，一律 loud 具名其<u>不可得之分項成因</u>·⛔ 判為零、⛔ 判為空**。

用法：python verify/probes/probe_WG9303R6_dynamic.py
"""
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
SELF = os.path.abspath(__file__)
sys.path.insert(0, VERIFY)

assert "WV_BAKE" not in os.environ, "🛑 `WV_BAKE` 已設 ⇒ 停（單 ⛔ 之）"

REC_BUF = []          # `_corner_buffer_S` 之逐次錄
REC_SOL = []          # `_solve_G_one` 之逐次錄
MISS = []             # 🛑 不可得之分項成因（⛔ 判為零）


def caller_chain(depth=24):
    """回 [(co_filename, co_name, co_firstlineno)]（⛔ `id(·)`）。"""
    out, f = [], sys._getframe(2)
    while f is not None and len(out) < depth:
        c = f.f_code
        out.append((c.co_filename, c.co_name, c.co_firstlineno))
        f = f.f_back
    return out


def find_blk(first_key="blk_label", second_key="_side"):
    """自呼叫端 frame 鏈上溯 `blk_label`；**自證該鍵存在** ＋ **併取第二鍵**。"""
    f = sys._getframe(2)
    while f is not None:
        L = f.f_locals
        if first_key in L:
            return (L.get(first_key), (second_key in L), L.get(second_key),
                    f.f_code.co_name, f.f_code.co_filename)
        f = f.f_back
    return (None, False, None, None, None)


def wrap(ns):
    cbs, sgo = ns["_corner_buffer_S"], ns["_solve_G_one"]

    def cbs2(*a, **kw):
        ch = caller_chain()
        lab = kw.get("_label", a[7] if len(a) > 7 else "")
        side = kw.get("side", a[5] if len(a) > 5 else None)
        blk, ok2, v2, fnm, ffile = find_blk()
        REC_BUF.append({
            "_label": lab, "side": side, "caller": ch[0] if ch else None,
            "chain": [c[1] for c in ch[:5]],
            "frame_blk": blk, "second_key_present": ok2, "second_key_val": v2,
            "frame_fn": fnm, "frame_file": ffile,
            "self": (ch[0][0] == SELF) if ch else False,
        })
        return cbs(*a, **kw)

    def sgo2(*a, **kw):
        ch = caller_chain()
        ic, sd = kw.get("is_corner"), kw.get("side")
        if "is_corner" not in kw:
            MISS.append("`_solve_G_one` 之 `is_corner` **非以關鍵字傳入** ⇒ 該次⛔ 可得")
        blk, ok2, v2, fnm, ffile = find_blk()
        if blk is None:
            MISS.append("frame 鏈上溯**查無** `blk_label` ⇒ 該次之街廓⛔ 可得（呼叫端 %r）"
                        % (ch[0][1] if ch else None))
        REC_SOL.append({
            "is_corner": ic, "side": sd, "blk": blk,
            "second_key_present": ok2, "second_key_val": v2,
            "caller": ch[0] if ch else None,
            "self": (ch[0][0] == SELF) if ch else False,
        })
        return sgo(*a, **kw)

    ns["_corner_buffer_S"] = cbs2
    ns["_solve_G_one"] = sgo2
    return ns


import run_verification as RV                                 # noqa: E402

_orig = RV.harvest


def harvest2():
    ns, fs = _orig()
    return wrap(ns), fs


RV.harvest = harvest2

BAR = "=" * 116
print(BAR)
print("【`W-G.9-303` `§四` 款 `3` 動態量測器】`run_verification` 全量**一次**")
print(BAR)
sys.stdout.flush()

rc = None
try:
    rc = RV.main()
except SystemExit as e:                                        # noqa: PERF203
    rc = e.code
except Exception as e:                                         # noqa: BLE001
    rc = "EXC: %r" % (e,)

print("\n" + BAR)
print("`run_verification.main()` 之 rc = %r" % (rc,))
print(BAR)


def side_of(x):
    return x if x in ("left", "right") else "(%r)" % (x,)


def blk_of_label(lab):
    """自 `_label` 取街廓：四形 ＝ 裸 `blk_label` ／ `f'{lbl}·F.1'` ／ `f'{blk}·E3'` ／ 空。"""
    s = str(lab or "")
    return s.split("·")[0] if s else "(空)"


prod_b = [r for r in REC_BUF if not r["self"]]
self_b = [r for r in REC_BUF if r["self"]]
prod_s = [r for r in REC_SOL if not r["self"]]
self_s = [r for r in REC_SOL if r["self"]]

print("\n── 母體二欄分列（量測器之母體⛔ 含其自身輸出）──")
print("| 受詞 | 生產錄 | 器自身（須 `0`） |")
print("|---|---|---|")
print("| `_corner_buffer_S` 呼叫次數 | %d | %d |" % (len(prod_b), len(self_b)))
print("| `_solve_G_one` 呼叫次數 | %d | %d |" % (len(prod_s), len(self_s)))

print("\n── (甲) `_corner_buffer_S` 實走之**呼叫端 × 街廓 × 側**（全量·⛔ 只報基數）──")
if not prod_b:
    print("   🛑 **loud**：本跑中該函式**零次呼叫**（⛔ 讀為『無此路徑』·見下之不可得清單）")
seenA = {}
for r in prod_b:
    cf, cn, cl = r["caller"]
    key = (os.path.relpath(cf, REPO) if cf.startswith(REPO) else cf, cn,
           blk_of_label(r["_label"]), side_of(r["side"]))
    seenA[key] = seenA.get(key, 0) + 1
print("| 呼叫端檔 | 呼叫端函式 | 街廓 | 側 | 次數 |")
print("|---|---|---|---|---|")
for k in sorted(seenA):
    print("| %s | %s | %s | %s | %d |" % (k[0], k[1], k[2], k[3], seenA[k]))
A = {(k[2], k[3]) for k in seenA}
print("\n(甲) ＝ %s   （基數 %d）" % (sorted(A), len(A)))
print("`_label` 之相異值（全量）= %s" % sorted({str(r["_label"]) for r in prod_b}))
print("`side` 之相異值（全量）  = %s" % sorted({str(r["side"]) for r in prod_b}))
print("frame 上溯 `blk_label` 之自證：命中 %d ／ 未命中 %d；第二鍵 `_side` 存在 %d"
      % (len([r for r in prod_b if r["frame_blk"] is not None]),
         len([r for r in prod_b if r["frame_blk"] is None]),
         len([r for r in prod_b if r["second_key_present"]])))

print("\n── (乙) `is_corner` 為**真**之**街廓 × 側**（全量）──")
B = {(r["blk"], side_of(r["side"])) for r in prod_s if r["is_corner"]}
if not prod_s:
    print("   🛑 **loud**：`_solve_G_one` 本跑中**零次呼叫** ⇒ (乙) **⛔ 可得**（⛔ 判為空）")
elif not B:
    print("   🛑 **loud**：`_solve_G_one` 被呼叫 %d 次，其中 `is_corner` 為真者 **0** 次"
          % len(prod_s))
print("(乙) ＝ %s   （基數 %d）" % (sorted(B, key=str), len(B)))
print("`is_corner` 值之分布（全量）= 真 %d ／ 偽 %d ／ None %d"
      % (len([r for r in prod_s if r["is_corner"] is True]),
         len([r for r in prod_s if r["is_corner"] is False]),
         len([r for r in prod_s if r["is_corner"] is None])))
seenB = {}
for r in prod_s:
    if r["is_corner"]:
        seenB[(r["blk"], side_of(r["side"]))] = seenB.get((r["blk"], side_of(r["side"])), 0) + 1
print("| 街廓 | 側 | `is_corner` 為真之次數 |")
print("|---|---|---|")
for k in sorted(seenB, key=str):
    print("| %s | %s | %d |" % (k[0], k[1], seenB[k]))

print("\n── (丙) 差集**逐項列舉** ──")
print("(甲) ∖ (乙) = %s   （基數 %d）" % (sorted(A - B, key=str), len(A - B)))
print("(乙) ∖ (甲) = %s   （基數 %d）" % (sorted(B - A, key=str), len(B - A)))

print("\n── 款 `4`：**三態分列**（🛑 ⛔ 判其對土地之後果·⛔ 擬 fallback·⛔ 呈 KL）──")
if not prod_s:
    st = "③ **(乙) 不可得**"
elif A <= B:
    st = "① **(甲) ⊆ (乙)**"
else:
    st = "② **(甲) ⊄ (乙)**"
print("判 = %s" % st)
print("  ① (甲) ⊆ (乙) ? %s" % (A <= B))
print("  ② (甲) ∖ (乙) 之逐格 = %s" % sorted(A - B, key=str))
print("  ③ (乙) 是否不可得 ? %s" % (not prod_s))

print("\n── 🛑 不可得之**分項成因**（⛔ 判為零、⛔ 判為空）──")
if not MISS:
    print("   （本跑無記錄）⛔ 讀為「無不可得之分項」——其僅表本器所設之二探點未觸發該分支")
for m in sorted(set(MISS)):
    print("   - %s   ×%d" % (m, MISS.count(m)))

print("\n" + BAR)
print("【本器⛔ 判其對土地之後果·⛔ 擬任何 fallback·⛔ 改生產碼一字】")
print(BAR)
