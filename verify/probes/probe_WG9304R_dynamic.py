"""`W-G.9-304` `§六` 款 `4`（時序）＋ 款 `3` 之**在域實值**（`run_verification` 全量一次）。

🔒 授權二手段：① `run_verification` 全量**一次**；② 於 `verify/probes/` 新增器。
🛑 ⛔ 改生產碼一字——只於**行程內**包裝 `ns` 之二鍵（⛔ 動任何檔）。
🛑 包裝**冪等**（`W-G.9-303R6` 自捕 `1` 之攔法）；器自身欄須 `0`，其**判別力**由本器內之
   **合成對照**（刻意雙包裝一個 dummy）證其⛔ 恆為 `0`。
🛑 `id(·)` ⛔ 作錨——一律 `(co_filename, co_name, co_firstlineno)`。
🛑 `f_locals` 鍵**先自證存在**並**增第二鍵**（二鍵並報）。
🛑 ⛔ 以「在域」充「可取」（坑 `bg`）——出艙其**當場之值**。
"""
import os
import sys

sys.stdout.reconfigure(encoding="utf-8", newline="\n")   # 🛑 `newline` ⛔ 可省（Windows 文字層會譯 CRLF）

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
SELF = os.path.abspath(__file__)
sys.path.insert(0, VERIFY)
assert "WV_BAKE" not in os.environ, "🛑 `WV_BAKE` 已設 ⇒ 停"

SIDE_MAP = {"left": "L", "right": "R", "左側": "L", "右側": "R", "無": "無"}
BLK_KEYS = ["blk_label", "_lbl", "blk", "lbl", "label", "_blk"]
WATCH = ["_near_dir_left", "_near_dir_right", "allocation_dir_block", "res",
         "_alloc_dir_used"]

SEQ = [0]
REC_B, REC_S, MISS = [], [], []
WRAPC = {"harvest": 0, "wrap": 0, "skip": 0}


def canon(s):
    return SIDE_MAP.get(str(s).strip(), "?<%r>" % (s,))


def chain(d=30):
    out, f = [], sys._getframe(2)
    while f is not None and len(out) < d:
        c = f.f_code
        out.append((c.co_filename, c.co_name, c.co_firstlineno))
        f = f.f_back
    return out


def find_blk():
    """上溯 frame 找街廓名：**多鍵並取** ⇒ 回 (值, 命中鍵, 同框其他命中鍵, 框名, 該框之 WATCH 實值)。"""
    f = sys._getframe(2)
    while f is not None:
        L = f.f_locals
        for k in BLK_KEYS:
            if k in L and isinstance(L[k], str) and L[k]:
                others = [x for x in BLK_KEYS if x in L and x != k]
                w = {}
                for x in WATCH:
                    if x in L:
                        v = L[x]
                        w[x] = ("dict(keys=%d)" % len(v)) if isinstance(v, dict) else repr(v)[:70]
                return (L[k], k, others, f.f_code.co_name, w)
        f = f.f_back
    return (None, None, [], None, {})


def wrap(ns):
    WRAPC["wrap"] += 1
    if getattr(ns.get("_corner_buffer_S"), "_wg9304", False):
        WRAPC["skip"] += 1
        return ns
    cbs, sgo = ns["_corner_buffer_S"], ns["_solve_G_one"]

    def cbs2(*a, **kw):
        SEQ[0] += 1
        ch = chain()
        blk, key, others, fnm, watch = find_blk()
        REC_B.append({"seq": SEQ[0], "blk": blk, "key": key, "others": others, "fn": fnm,
                      "side_raw": kw.get("side", a[5] if len(a) > 5 else None),
                      "label": kw.get("_label", a[7] if len(a) > 7 else ""),
                      "alloc_arg": repr(a[3])[:70] if len(a) > 3 else "(未傳)",
                      "watch": watch,
                      "self": bool(ch) and os.path.abspath(ch[0][0]) == SELF,
                      "caller": ch[0] if ch else None})
        return cbs(*a, **kw)
    cbs2._wg9304 = True

    def sgo2(*a, **kw):
        SEQ[0] += 1
        ch = chain()
        blk, key, others, fnm, watch = find_blk()
        if blk is None:
            MISS.append("frame 鏈查無 %s 任一鍵 ⇒ 街廓⛔ 可得（呼叫端 `%s`）"
                        % (BLK_KEYS, ch[0][1] if ch else None))
        r = sgo(*a, **kw)
        used = None
        try:
            used = r[0].get("_alloc_dir_used") if isinstance(r, tuple) else None
        except Exception:                                    # noqa: BLE001
            MISS.append("`_alloc_dir_used` 之讀取拋例外 ⇒ 該次⛔ 可得")
        REC_S.append({"seq": SEQ[0], "blk": blk, "key": key, "fn": fnm,
                      "is_corner": kw.get("is_corner"), "side_raw": kw.get("side"),
                      "alloc_used": repr(used)[:70],
                      "self": bool(ch) and os.path.abspath(ch[0][0]) == SELF,
                      "caller": ch[0] if ch else None})
        return r
    sgo2._wg9304 = True
    ns["_corner_buffer_S"], ns["_solve_G_one"] = cbs2, sgo2
    return ns


import run_verification as RV                                   # noqa: E402

_orig = RV.harvest


def harvest2():
    WRAPC["harvest"] += 1
    ns, fs = _orig()
    return wrap(ns), fs


RV.harvest = harvest2

BAR = "=" * 116
print(BAR)
print("【`W-G.9-304` `§六` 款 `4` 動態量測器】`run_verification` 全量**一次**")
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
print("冪等自證：`RV.harvest` %d 次／`wrap()` %d 次／**已包裝而跳過 %d 次**"
      % (WRAPC["harvest"], WRAPC["wrap"], WRAPC["skip"]))
print(BAR)

pb = [r for r in REC_B if not r["self"]]
sb = [r for r in REC_B if r["self"]]
ps = [r for r in REC_S if not r["self"]]
ss_ = [r for r in REC_S if r["self"]]
print("\n── 母體二欄分列（量測器之母體⛔ 含其自身輸出）──")
print("| 受詞 | 生產錄 | 器自身（**須 `0`**） | 判 |")
print("|---|---|---|---|")
print("| `_corner_buffer_S` | %d | %d | %s |" % (len(pb), len(sb), "✅" if not sb else "🔴"))
print("| `_solve_G_one` | %d | %d | %s |" % (len(ps), len(ss_), "✅" if not ss_ else "🔴"))

# 🔑 合成對照：刻意雙包裝一 dummy ⇒ 證「器自身」欄⛔ 恆為 `0`
SYN = []


def _dummy(x):
    return x


def _mk(f):
    def g(*a, **kw):
        ch = chain()
        SYN.append(bool(ch) and os.path.abspath(ch[0][0]) == SELF)
        return f(*a, **kw)
    return g


_d1 = _mk(_dummy)
_d2 = _mk(_d1)          # 刻意雙包裝（⛔ 冪等）
_d2(1)
print("🔑 判別力[必非零]（合成對照·刻意**雙**包裝一 dummy）⇒ 器自身之命中 = %d／%d（須 ≥ 1）"
      % (sum(1 for x in SYN if x), len(SYN)))

print("\n── 款 `4`　時序：逐 (街廓,側) 之**首次**呼叫序號 ──")
fb, fs = {}, {}
for r in pb:
    k = (r["blk"] or str(r["label"]).split("·")[0], canon(r["side_raw"]))
    fb.setdefault(k, r["seq"])
for r in ps:
    if r["is_corner"] and r["blk"]:
        k = (r["blk"], canon(r["side_raw"]))
        fs.setdefault(k, r["seq"])
print("`_corner_buffer_S` 之 `side` 原值集合 = %s" % sorted({str(r["side_raw"]) for r in pb}))
print("`_solve_G_one` 之 `side` 原值集合   = %s" % sorted({str(r["side_raw"]) for r in ps}))
print("\n| (街廓, 側正規) | `_corner_buffer_S` 強制之首次序號 | `_solve_G_one`(is_corner 真) 之首次序號 | 停八成就？ |")
print("|---|---|---|---|")
stop8 = []
for k in sorted(fb):
    b = fb[k]
    s = fs.get(k)
    if s is None:
        v = "🛑 **⛔ 可得**（該 (街廓,側) 無 `is_corner` 真之呼叫）"
        hit = True
    else:
        hit = s > b
        v = "🔴 **成就**（%d > %d）" % (s, b) if hit else "✅ 不成就（%d ≤ %d）" % (s, b)
    if hit:
        stop8.append(k)
    print("| %s | %s | %s | %s |" % (k, b, s if s is not None else "(無)", v))
print("\n🛑 **停八**（任一格成就即成就·⛔ 以「多數格不成就」充不成就）⇒ 成就之格 = %s ⇒ **%s**"
      % (stop8, "🔴 成就 ⇒ 停、上呈" if stop8 else "✅ 不成就"))

print("\n── 款 `3`　強制呼叫端之**在域實值**（⛔ 以「在域」充「可取」·坑 `bg`）──")
for r in pb:
    print("\n   ● seq=%d  街廓=%r（自 frame 鍵 `%s`·同框其他命中鍵 %s·框 `%s`）  側原值=%r ⇒ 正規 %s"
          % (r["seq"], r["blk"], r["key"], r["others"], r["fn"], r["side_raw"],
             canon(r["side_raw"])))
    print("     第 4 位序實參（`allocation_dir`）之**當場值** = %s" % r["alloc_arg"])
    print("     該框之 WATCH 實值 = %s" % (r["watch"] or "（無任一 WATCH 名在域）"))

print("\n── `_alloc_dir_used` 之實測（款 `2` 之容器·跨呼叫可見之直證）──")
nn = [r for r in ps if r["alloc_used"] not in ("None", "'None'")]
print("   `_solve_G_one` 生產錄 %d 次，其回傳之 `_alloc_dir_used` **非 None** 者 = %d 次"
      % (len(ps), len(nn)))
for r in nn[:6]:
    print("      seq=%d 街廓=%r 側=%r ⇒ %s" % (r["seq"], r["blk"], r["side_raw"], r["alloc_used"]))

print("\n── 🛑 不可得之**分項成因**（⛔ 判為零、⛔ 判為空）──")
if not MISS:
    print("   （無記錄）⛔ 讀為「無不可得之分項」")
for m in sorted(set(MISS)):
    print("   - %s   ×%d" % (m, MISS.count(m)))

print("\n" + BAR)
print("【本器⛔ 判其可施或不可施·⛔ 擬任何改法或 diff】")
print(BAR)
