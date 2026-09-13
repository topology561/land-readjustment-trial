# -*- coding: utf-8 -*-
"""`W-G.9-271` `§二-4`：**步驟 D 分母之二態量**（零生產碼·**⛔ 動任何碼**）。

🔒 **受詞之逐字錨**（`app.py`·⛔ 行號·`自誤 372`＋`374`）

    all_original_parcels = sorted({tp['原地號'] for tp in temp_parcels

🔒 **共用性之逐字根據**（`app.py` 註解）：「本函式係 app `main()` 與 harness
   `verify/selection_pipeline.build_build_parcels` **共用之最後一道 app 側轉換**」。

🔒 **辦法**：以 harness 之 `build_build_parcels` 取 `temp_parcels`，二態各量
   `{tp['原地號'] for tp if not _is_ghost_sliver}` 之**大小**與**成員**。

   | 態 | 環境 |
   |---|---|
   | 甲 | `WV_K6_STEP0` **未設**（＝預設 `on`·**現行生產態**） |
   | 乙 | `WV_K6_STEP0=off` |

🔒 **出艙**：二態之大小、**差集之逐筆原地號**、
   `snap["財務接線_v3"]["原地號_區段"]` 之筆數（**第三方對照**），
   以及步驟 `0` 之 `_diag` 四欄 `parcels_in`／`parcels_absorbed`／`parcels_out`／`groups_merged`。

🛑 **準據**：二態之大小須**相異**；⛔ 相異 ⇒ **loud 停**（`rc != 0`），⛔ 靜默續。
🛑 本項**僅以環境變數驅動既有出口**——**⛔ 落地 `K-9-29` 任何子項、
   ⛔ 動 `k6_step0_enabled` 之預設一字**。

用法：`PYTHONIOENCODING=utf-8 python verify/probes/probe_WG9271_stepD_denom.py [倉根]`
`rc`：`0` 二態相異（如期）／`6` 二態**⛔ 相異**（loud 停）／`5` 量測器紅。
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(REPO, "verify"))

ENV = "WV_K6_STEP0"          # ＝ `app.py` 之 `K6_STEP0_ENV`（逐字）
W = 112


def say(s=""):
    print(s)


def one(mode):
    """`mode` ＝ `None`（未設·態甲）／`"off"`（態乙）。回 (原地號集合, diag, temp 筆數)。"""
    if mode is None:
        os.environ.pop(ENV, None)
    else:
        os.environ[ENV] = mode
    # 🔒 每態重新 `harvest()`——`k6_step0_enabled()` 於**呼叫時**讀 env，
    #    惟為免任何模組級快取，一律重建。
    for m in ("app_harvest", "run_verification", "selection_pipeline", "stepg_pipeline"):
        sys.modules.pop(m, None)
    from app_harvest import harvest
    import run_verification as rv
    ns, fake_st = harvest()
    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp_p, _build, _sw = rv.build_build_parcels(
        ns, fake_st, v6, list(cb_by.values()), snapshot)
    # 🔒 逐字複製受詞之式（⛔ 另寫第二份判準）
    ids = sorted({tp["原地號"] for tp in temp_p
                  if not tp.get("_is_ghost_sliver", False)})
    diag = dict(fake_st.session_state.get("_k6_step0_diag") or {})
    if not diag:
        for k, v in list(fake_st.session_state.items()):
            if isinstance(v, dict) and "parcels_absorbed" in v:
                diag = dict(v)
                break
    return ids, diag, len(temp_p), snapshot


def main():
    say("=" * W)
    say("【`W-G.9-271` `§二-4`】**步驟 D 分母之二態量**（⛔ 動任何碼）")
    say("=" * W)
    say("🛑 **僅以環境變數驅動既有出口**——⛔ 落地 `K-9-29` 任何子項、"
        "⛔ 動 `k6_step0_enabled` 之預設一字。")
    say("🔒 受詞之逐字錨 ＝ `all_original_parcels = sorted({tp['原地號'] for tp in temp_parcels`")

    say("")
    say("── 態 甲（`%s` **未設** ＝ 預設 `on`·現行生產態）" % ENV)
    a_ids, a_diag, a_tp, snap = one(None)
    say("   `temp_parcels` 筆數 ＝ **%d**｜分母（去 ghost sliver 之原地號相異）＝ **%d**"
        % (a_tp, len(a_ids)))

    say("")
    say("── 態 乙（`%s=off`）" % ENV)
    b_ids, b_diag, b_tp, _ = one("off")
    say("   `temp_parcels` 筆數 ＝ **%d**｜分母 ＝ **%d**" % (b_tp, len(b_ids)))
    os.environ.pop(ENV, None)               # 🔒 還原（⛔ 遺留於後續量測）

    say("")
    say("── 差集（逐筆原地號·⛔ 只報數）")
    only_b = [x for x in b_ids if x not in set(a_ids)]
    only_a = [x for x in a_ids if x not in set(b_ids)]
    say("   乙∖甲（`off` 有而預設無）＝ **%d** 筆：%s" % (len(only_b), only_b))
    say("   甲∖乙（預設有而 `off` 無）＝ **%d** 筆：%s" % (len(only_a), only_a))

    say("")
    say("── 第三方對照：`snap[\"財務接線_v3\"][\"原地號_區段\"]` 之筆數")
    fz = ((snap or {}).get("財務接線_v3") or {}).get("原地號_區段")
    if fz is None:
        say("   🛑 該鍵**不存在**（`財務接線_v3` 之鍵 ＝ %s）⇒ 具名為**不可得**，⛔ 以他物代之"
            % sorted((snap or {}).get("財務接線_v3", {}).keys())[:12])
    else:
        say("   筆數 ＝ **%d**（型 ＝ %s）" % (len(fz), type(fz).__name__))
        say("   與態甲之分母差 ＝ %+d｜與態乙之分母差 ＝ %+d"
            % (len(fz) - len(a_ids), len(fz) - len(b_ids)))

    say("")
    say("── 步驟 `0` 之 `_diag` 四欄")
    say("   | 欄 | 態甲（預設 `on`） | 態乙（`off`） |")
    say("   |---|---|---|")
    for k in ("parcels_in", "parcels_absorbed", "parcels_out", "groups_merged"):
        say("   | `%s` | %s | %s |"
            % (k, a_diag.get(k, "（不可得）"), b_diag.get(k, "（不可得）")))
    if not a_diag:
        say("   🛑 態甲之 `_diag` **不可得** ⇒ 具名（⛔ 以 `0` 代之）")
    if not b_diag:
        say("   🛑 態乙之 `_diag` **不可得** ⇒ 具名（⛔ 以 `0` 代之）")

    say("")
    say("── 🛑 準據：二態之大小須**相異**")
    ok = len(a_ids) != len(b_ids)
    say("   態甲 %d vs 態乙 %d ⇒ %s"
        % (len(a_ids), len(b_ids), "🟢 **相異**（如期）" if ok else "🔴 **⛔ 相異**"))
    if not ok:
        say("   🛑 **loud 停**（`rc = 6`）——⛔ 靜默續。")
        return 6
    return 0


if __name__ == "__main__":
    sys.exit(main())
