# -*- coding: utf-8 -*-
"""W-G.9-344 補令一 之量測器（發單側窗四十擬·檔 F3·⛔ 由受單側改一字）。
版次：補令二修正版（F3′）——排除後 temp 之比較改為逐元素（保留重號）；自檢增重號二造。

受詞：段三所併出之片之標記（鍵 `段三併出`）與公設地調配用 temp 之排除
（`verify/selection_pipeline.py` 之 `k6b_stage3_pool_temp`）。

用法：
  python verify/probes/probe_WG9344p1_pooltemp.py run <repo> <退縮> <on|off>
  python verify/probes/probe_WG9344p1_pooltemp.py selftest

rc：0 相符／1 不符（判定為偽）／3 無從判定（受詞缺或執行中止）／2 用法錯。
「無從判定」與「判定為偽」⛔ 共用出艙碼。
"""
import collections
import contextlib
import importlib.util
import io
import os
import subprocess
import sys
import types

ENV = "WV_K6B_STAGE3"
KEY = "段三併出"

# 期（KL 放行之改後配地·W-G.9-344 附錄乙·發單側窗四十依補令一 裁 3 之定義轉寫）：
# 被段三「成」所消耗之片 → 其受併宗（相異·字典序）
EXPECT_35_ON = {
    "628-30(3)": ["628-45(2)"],
    "628-30(2)": ["628-45(2)"],
    "628-20(2)": ["628-45(1)"],
    "628-30(1)": ["628-45(1)"],
    "628-41(2)": ["628-41(1)"],
    "628-41(3)": ["628-41(1)"],
    "628-45(5)": ["628-45(1)", "628-45(2)"],
    "628-30(4)": ["628-45(1)", "628-45(2)"],
    "628-45(3)": ["628-45(1)", "628-45(2)"],
    "628-45(4)": ["628-45(1)", "628-45(2)"],
}


def expect_for(sb, mode):
    if mode == "on" and abs(sb - 3.5) < 1e-9:
        return EXPECT_35_ON, False          # 段二序非空 ⇒ 回傳深拷貝（⛔ 同一物件）
    return {}, True                          # 段三不動 ⇒ 回傳原物件（原單 §三-3 第 2 款）


def missing_entries(sp):
    return [n for n in ("run_corner_pk_k6b", "k6b_stage3_pool_temp") if not hasattr(sp, n)]


def judge(mark_items, expect, all_ids, pool_ids, want_pool_ids, pool_is_new, pool_same_elems,
          same_obj_required, same_obj, input_ok):
    """純判式。回傳 (rc, 訊息列)。rc 0 相符／1 不符。

    mark_items    : [(暫編地號, 標記值), …]——回傳之 temp 中帶標記之元素，依序（保留重號）
    all_ids       : 回傳之 temp 之暫編地號，依序（保留重號）
    pool_ids      : k6b_stage3_pool_temp 之回傳之暫編地號，依序（保留重號）
    want_pool_ids : 回傳之 temp 中未帶標記之元素之暫編地號，依序（保留重號）
    """
    msg, bad = [], 0
    cnt = collections.Counter(k for k, _ in mark_items)
    dup = sorted(k for k, n in cnt.items() if n > 1)
    if dup:
        bad += 1
        msg.append(f"  🔴 帶標記之暫編地號重複：{dup}")
    marks = dict(mark_items)
    for k in sorted(set(marks) | set(expect)):
        got, exp = marks.get(k), expect.get(k)
        ok = (got == exp)
        bad += (not ok)
        msg.append(f"  {'✅' if ok else '🔴'} {k}：期 {exp} ／ 實 {got}")
    if not expect and not marks:
        msg.append("  ✅ 期與實皆無標記")
    ok = (list(pool_ids) == list(want_pool_ids)) and pool_same_elems
    bad += (not ok)
    msg.append(f"  {'✅' if ok else '🔴'} 排除後之 temp：{len(pool_ids)} 片（期 {len(want_pool_ids)} ＝ 全 {len(all_ids)} − 帶標記 {len(mark_items)}；"
               f"逐元素依序比對·保留重號；元素為同一物件 {pool_same_elems}）")
    bad += (not pool_is_new)
    msg.append(f"  {'✅' if pool_is_new else '🔴'} k6b_stage3_pool_temp 回傳新 list")
    ok = (same_obj == same_obj_required)
    bad += (not ok)
    msg.append(f"  {'✅' if ok else '🔴'} 回傳之 temp 與輸入同一物件：期 {same_obj_required} ／ 實 {same_obj}")
    bad += (not input_ok)
    msg.append(f"  {'✅' if input_ok else '🔴'} 輸入之 temp 未被改寫（面積四欄與 `{KEY}` 鍵·逐元素依序）")
    return (0 if bad == 0 else 1), msg


def _fp(tp):
    return [(t["暫編地號"], t.get("面積_m2"), t.get("分攤登記面積_m2"), t.get("登記面積_m2"),
             t.get("幾何面積_m2"), KEY in t) for t in tp]


def cmd_run(repo, sb, mode):
    if mode not in ("on", "off"):
        return 2
    os.environ[ENV] = mode
    spec = importlib.util.spec_from_file_location(
        "f2", os.path.join(repo, "verify", "probes", "probe_WG9344_k6s3.py"))
    f2 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(f2)
    try:
        head = subprocess.run(["git", "-C", repo, "rev-parse", "HEAD"], capture_output=True,
                              text=True).stdout.strip()
    except Exception:                                        # noqa: BLE001
        head = "?"
    print(f"【F3′ run】態 {head}·退縮 {sb}·{ENV}={mode}")
    ns, fst, snap, cb_by, cad, tp, bp, params = f2._boot(repo, sb)
    import selection_pipeline as sp
    miss = missing_entries(sp)
    if miss:
        print(f"🔴 受詞缺：verify/selection_pipeline.py 無 {miss} ⇒ 無從判定")
        return 3
    before = _fp(tp)
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            ret = sp.run_corner_pk_k6b(ns, fst, list(cb_by.values()), cad, params, tp, bp, sb,
                                       snapshot=snap)
        tp_out = ret[5]
        pool = sp.k6b_stage3_pool_temp(tp_out)
    except Exception as e:                                   # noqa: BLE001
        print(f"🔴 執行中止：{type(e).__name__}: {str(e)[:300]} ⇒ 無從判定")
        return 3
    mark_items = [(t["暫編地號"], t[KEY]) for t in tp_out if KEY in t]
    unmarked = [t for t in tp_out if KEY not in t]
    same_elems = (len(pool) == len(unmarked)) and all(a is b for a, b in zip(pool, unmarked))
    expect, same_req = expect_for(sb, mode)
    rc, msg = judge(mark_items, expect, [t["暫編地號"] for t in tp_out], [t["暫編地號"] for t in pool],
                    [t["暫編地號"] for t in unmarked], pool is not tp_out, same_elems,
                    same_req, tp_out is tp, _fp(tp) == before)
    print("\n".join(msg))
    print(f"⇒ rc {rc}")
    return rc


def cmd_selftest():
    E = {"a": ["x"], "b": ["x", "y"]}
    M = [("a", ["x"]), ("b", ["x", "y"])]
    ids = ["a", "b", "c", "x", "y"]
    rest = ["c", "x", "y"]
    G = ["a", "b", "g", "g", "c"]                       # 含重號 g（仿零面積 ghost 之同名二片）
    cases = [
        ("完全相符（必綠）", judge(M, E, ids, rest, rest, True, True, False, False, True)[0], 0),
        ("缺一片（必紅）", judge([("a", ["x"])], E, ids, ["b", "c", "x", "y"], ["b", "c", "x", "y"], True, True, False, False, True)[0], 1),
        ("受併宗未依字典序（必紅）", judge([("a", ["x"]), ("b", ["y", "x"])], E, ids, rest, rest, True, True, False, False, True)[0], 1),
        ("排除後仍含標記片（必紅）", judge(M, E, ids, ["a", "c", "x", "y"], rest, True, True, False, False, True)[0], 1),
        ("輸入被改寫（必紅）", judge(M, E, ids, rest, rest, True, True, False, False, False)[0], 1),
        ("段三不動而回傳非原物件（必紅）", judge([], {}, ids, ids, ids, True, True, True, False, True)[0], 1),
        ("段三不動且無標記（必綠）", judge([], {}, ids, ids, ids, True, True, True, True, True)[0], 0),
        ("pool 非新 list（必紅）", judge(M, E, ids, rest, rest, False, True, False, False, True)[0], 1),
        ("含重號而無標記·全數保留（必綠·F3 原版於此誤紅）", judge([], {}, G, G, G, True, True, True, True, True)[0], 0),
        ("含重號而排除時漏掉其一（必紅）", judge([], {}, G, ["a", "b", "g", "c"], G, True, True, True, True, True)[0], 1),
        ("元素非同一物件（必紅）", judge(M, E, ids, rest, rest, True, False, False, False, True)[0], 1),
        ("帶標記之暫編地號重複（必紅）", judge([("a", ["x"]), ("a", ["x"]), ("b", ["x", "y"])], E, ids, rest, rest, True, True, False, False, True)[0], 1),
    ]
    n_ok = 0
    for name, got, exp in cases:
        ok = (got == exp)
        n_ok += ok
        print(f"  {'✅' if ok else '🔴'} {name}：期 rc {exp} ／ 實 rc {got}")
    stub = types.SimpleNamespace()
    ok = (missing_entries(stub) == ["run_corner_pk_k6b", "k6b_stage3_pool_temp"])
    n_ok += ok
    print(f"  {'✅' if ok else '🔴'} 受詞缺之偵出（⇒ rc 3·⛔ 判為不符）")
    n = len(cases) + 1
    print(f"selftest {n_ok}/{n} ⇒ {'✅' if n_ok == n else '🔴'}")
    return 0 if n_ok == n else 1


def main(argv):
    if len(argv) == 2 and argv[1] == "selftest":
        return cmd_selftest()
    if len(argv) == 5 and argv[1] == "run":
        try:
            sb = float(argv[3])
        except ValueError:
            return 2
        return cmd_run(argv[2], sb, argv[4])
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
