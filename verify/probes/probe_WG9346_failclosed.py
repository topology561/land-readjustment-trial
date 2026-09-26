# -*- coding: utf-8 -*-
"""W-G.9-346 量測器（發單側窗四十二擬·檔 F6·⛔ 由受單側改一字）：段三畫面入口之「中斷即停機」（fail-closed）。

受詞：`app.py` 模組層之 `f3_screen_k6b_stage3`／`k6b_stage3_selected`（`W-G.9-345 §三-2`）。
量法：以 harvest 載入 app.py（⛔ 執行 main()），輸入之組裝借檔 F4（`verify/probes/probe_WG9345_screen.py`）之
`_screen_inputs`；於 `ns`（＝ 模組函式之 `__globals__`）上替換函式以注入失敗，逐情形量段三入口「之後」之 session：
其後之配地／七級調配／步驟 M 皆經 `k6b_stage3_selected` 取宗地 ⇒ 本器以之為判。

子命令（一律 python verify/probes/probe_WG9346_failclosed.py <子命令> …）：
  run <repo> [<退縮>]   七情形（退縮預設 3.5；旗標 WV_K6B_STAGE3 由本器於行程內自設）：
    C0 正常                 ：ran True；session 無停機訊息；k6b_stage3_selected 回 (temp, build)。
    C1 段三本體丟非 RuntimeError（KeyError）      ：其後 k6b_stage3_selected 須 raise 且訊息含「請重跑」。
    C2 終趟（真 st 之街角選位）中止                  ：同 C1 之判。
    C3 無歸戶 ＋ session 殘留前次之段二序            ：k6b_stage3_run 呼叫數 0；ran False；k6b_stage3_selected 回 None。
    C4 試算趟之街角選位無產出（首趟照跑·其後代理趟皆不寫 session）：session 之停機訊息含「未產出」；k6b_stage3_selected 須 raise。
    C5 旗標 off              ：ran False；session 無停機訊息、無指紋；k6b_stage3_selected 回 None。
    C6 首趟（代理）中止        ：其後 k6b_stage3_selected 須 raise 且訊息含「請重跑」。
  （判別力：於 `W-G.9-345` 之態〔b0c9edc〕跑，須恰 C1／C2／C3／C4／C6 紅、C0／C5 綠 ⇒ 本器非恆綠亦非恆紅。）
  （退縮須使段三實際執行〔段二序非空〕；本案 3.5 m 是、0 m 否〔段二序 0 列 ⇒ rc 3〕。）
rc：0 七情形皆如期／1 有不如期者／2 用法錯／3 無從判定（受詞缺、C0 未能跑畢或其段三未執行·⛔ 等同相符）。
"""
import contextlib, copy, importlib.util, io, os, subprocess, sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:  # noqa: BLE001
    pass

ENV = "WV_K6B_STAGE3"
NEED = ("f3_screen_k6b_stage3", "k6b_stage3_selected", "k6b_stage3_run", "f3_screen_corner_pk_run",
        "_K6BTrialSt", "_K6BTrialStop", "K917_DROPPED")
ERR_KEY = "f3_k6b_stage3_error"


def _load_f4(repo):
    spec = importlib.util.spec_from_file_location("f4", os.path.join(repo, "verify", "probes", "probe_WG9345_screen.py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


class _Injected(Exception):
    pass


def cmd_run(repo, sb):
    os.environ[ENV] = "on"
    f4 = _load_f4(repo)
    f2 = f4._load_f2(repo)
    head = subprocess.run(["git", "-C", repo, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    print(f"【F6 run】態 {head}·退縮 {sb}")
    ns, fst, snap, cb_by, cad, tp, bp, params = f2._boot(repo, sb)
    miss = [n for n in NEED if n not in ns]
    if miss:
        print(f"🔴 受詞缺：app.py 模組層無 {miss} ⇒ 無從判定")
        return 3
    if ns["f3_screen_k6b_stage3"].__globals__ is not ns:
        print("🔴 注入無從生效（f3_screen_k6b_stage3.__globals__ ≠ ns）⇒ 無從判定")
        return 3
    cb = list(cb_by.values())
    ss = fst.session_state
    t0, b0 = f4._copy_pair(tp, bp)
    pk0, g0 = f4._screen_inputs(ns, fst, snap, cb, cad, params, t0, b0, sb)
    ss0 = copy.deepcopy(dict(ss))
    k0 = copy.deepcopy(ns["K917_DROPPED"])
    orig = {n: ns[n] for n in ("k6b_stage3_run", "f3_screen_corner_pk_run")}
    TrialSt, TrialStop = ns["_K6BTrialSt"], ns["_K6BTrialStop"]
    state = {}

    def reset(flag="on"):
        ns.update(orig)
        os.environ[ENV] = flag
        ss.clear()
        ss.update(copy.deepcopy(ss0))
        ns["K917_DROPPED"].clear()
        ns["K917_DROPPED"].update(copy.deepcopy(k0))
        t, b = f4._copy_pair(tp, bp)
        return dict(pk0, temp_parcels=t, build_parcels=b), b

    def call(pk):
        qs = f4.QuietSt(ss)
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                ret = ns["f3_screen_k6b_stage3"](qs, pk_kwargs=pk, g_kwargs=g0)
            return ret, None
        except BaseException as e:  # noqa: BLE001  （含注入之例外與 st.stop 之 _Stop）
            return None, e

    def selected(b):
        try:
            r = ns["k6b_stage3_selected"](ss, b, ss.get("f3L_setback_default"))
            return ("tuple" if isinstance(r, tuple) else repr(r)), None
        except RuntimeError as e:
            return "raise", str(e)

    rows = []

    def judge(cid, desc, ok, got):
        rows.append((cid, ok))
        print(f"  {'✅' if ok else '🔴'} {cid} {desc}：{got}")

    # C0 正常
    pk, b = reset()
    ret, exc = call(pk)
    sel, msg = selected(b)
    if exc is not None or ret is None:
        print(f"🔴 C0 未能跑畢：{type(exc).__name__}: {str(exc)[:200]} ⇒ 無從判定")
        return 3
    if ret.get("ran") is not True:
        print(f"🔴 C0 之段三未執行（ran={ret.get('ran')}·段二序 {len(ss.get('f3_k6b_stage3_order_used') or [])} 列）"
              "⇒ 本退縮無從量段三之中斷 ⇒ 無從判定")
        return 3
    state["order"] = copy.deepcopy(ss.get("f3_k6b_stage3_order_used") or [])
    judge("C0", "正常", ret.get("ran") is True and ERR_KEY not in ss and sel == "tuple",
          f"ran={ret.get('ran')}·停機訊息={ss.get(ERR_KEY)!r}·selected={sel}·段二序 {len(state['order'])} 列")

    # C1 段三本體丟 KeyError
    pk, b = reset()

    def _boom(*a, **k):
        raise KeyError("W-G.9-346 注入")
    ns["k6b_stage3_run"] = _boom
    ret, exc = call(pk)
    sel, msg = selected(b)
    judge("C1", "段三本體丟 KeyError", sel == "raise" and "請重跑" in (msg or ""),
          f"例外={type(exc).__name__ if exc else None}·selected={sel}·訊息={(msg or '')[:70]!r}")

    # C2 終趟中止
    pk, b = reset()

    def _pk_final_stop(st, **kw):
        if not isinstance(st, TrialSt):
            raise f4._Stop("W-G.9-346 注入：終趟中止")
        return orig["f3_screen_corner_pk_run"](st, **kw)
    ns["f3_screen_corner_pk_run"] = _pk_final_stop
    ret, exc = call(pk)
    sel, msg = selected(b)
    judge("C2", "終趟中止", sel == "raise" and "請重跑" in (msg or ""),
          f"例外={type(exc).__name__ if exc else None}·selected={sel}·訊息={(msg or '')[:70]!r}")

    # C3 無歸戶 ＋ 殘留段二序
    pk, b = reset()
    ss["t8_ownership_map"] = {}
    ss["f3_k6b_stage2_order"] = copy.deepcopy(state["order"])
    n_calls = [0]

    def _count(*a, **k):
        n_calls[0] += 1
        raise _Injected("W-G.9-346 注入：k6b_stage3_run 被呼叫")
    ns["k6b_stage3_run"] = _count
    ret, exc = call(pk)
    sel, msg = selected(b)
    ran = ret.get("ran") if ret else None
    judge("C3", "無歸戶＋殘留段二序", n_calls[0] == 0 and ran is False and sel == "None",
          f"k6b_stage3_run 呼叫 {n_calls[0]}·ran={ran}·例外={type(exc).__name__ if exc else None}·selected={sel}")

    # C4 試算趟之街角選位無產出
    pk, b = reset()
    seen = [0]

    def _pk_trial_silent(st, **kw):
        if isinstance(st, TrialSt):
            seen[0] += 1
            if seen[0] > 1:
                return None                      # 試算趟：⛔ 寫 session（模擬本體之「無結果」分支）
        return orig["f3_screen_corner_pk_run"](st, **kw)
    ns["f3_screen_corner_pk_run"] = _pk_trial_silent
    ret, exc = call(pk)
    sel, msg = selected(b)
    em = str(ss.get(ERR_KEY) or "")
    judge("C4", "試算趟無產出", "未產出" in em and sel == "raise",
          f"代理趟 {seen[0]}·例外={type(exc).__name__ if exc else None}·停機訊息={em[:60]!r}·selected={sel}")

    # C5 旗標 off
    pk, b = reset("off")
    ret, exc = call(pk)
    sel, msg = selected(b)
    ran = ret.get("ran") if ret else None
    judge("C5", "旗標 off", exc is None and ran is False and ERR_KEY not in ss
          and "f3_k6b_stage3_fp" not in ss and sel == "None",
          f"ran={ran}·停機訊息={ss.get(ERR_KEY)!r}·指紋={'f3_k6b_stage3_fp' in ss}·selected={sel}")

    # C6 首趟中止
    pk, b = reset()

    def _pk_first_stop(st, **kw):
        if isinstance(st, TrialSt):
            raise TrialStop("W-G.9-346 注入：首趟中止")
        raise f4._Stop("W-G.9-346 注入：真 st 之重跑亦中止")
    ns["f3_screen_corner_pk_run"] = _pk_first_stop
    ret, exc = call(pk)
    sel, msg = selected(b)
    judge("C6", "首趟中止", sel == "raise" and "請重跑" in (msg or ""),
          f"例外={type(exc).__name__ if exc else None}·selected={sel}·訊息={(msg or '')[:70]!r}")

    ns.update(orig)
    bad = [c for c, ok in rows if not ok]
    print(f"⇒ 紅 {bad}；rc {1 if bad else 0}")
    return 1 if bad else 0


def main(argv):
    if len(argv) >= 3 and argv[1] == "run":
        sb = float(argv[3]) if len(argv) >= 4 else 3.5
        return cmd_run(os.path.abspath(argv[2]), sb)
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
