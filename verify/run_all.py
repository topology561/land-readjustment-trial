# -*- coding: utf-8 -*-
"""W-V 單一命令：手冊圖8 golden ＋ headless 雙情境對拍 baselines。exit 0＝全綠。
用法：python verify/run_all.py"""
import ast
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(REPO, "tests"))


def _candidates_append_keys(pyfile):
    """🆕 P-C（裁定M·B-3）：AST 取該檔內 `_candidates.append({...})` dict literal 之鍵集
    （app.py main() PK 與 selection_pipeline.run_corner_pk 各一）。app 段在 main() 內·靜態解析
    不執行碼。回 frozenset|None。"""
    tree = ast.parse(open(pyfile, encoding="utf-8").read())
    for n in ast.walk(tree):
        if (isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)
                and n.func.attr == "append"
                and isinstance(n.func.value, ast.Name)
                and n.func.value.id == "_candidates"
                and n.args and isinstance(n.args[0], ast.Dict)):
            keys = []
            for k in n.args[0].keys:
                if isinstance(k, ast.Constant):
                    keys.append(k.value)
            return frozenset(keys)
    return None


def _check_candidates_keyset():
    """app _candidates 欄集 == selection_pipeline _candidates 欄集（B-3 鏡射結構閘）。"""
    _app = _candidates_append_keys(os.path.join(REPO, "app.py"))
    _sel = _candidates_append_keys(os.path.join(HERE, "selection_pipeline.py"))
    if _app is None or _sel is None:
        return False, f"取不到 _candidates.append 字面（app={_app is not None}·sel={_sel is not None}）"
    if _app != _sel:
        return False, (f"欄集不等：app∖sel={sorted(_app - _sel)}·sel∖app={sorted(_sel - _app)}")
    return True, f"{len(_app)} 鍵一致"


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    rc = 0

    print("### [1/3] golden 單測（手冊圖8 ＋ W-D.2 滑池槽 8 案 ＋ B-3 欄集結構閘）")
    _ok_ks, _msg_ks = _check_candidates_keyset()
    print(f"  {'✅' if _ok_ks else '🔴'} B-3 欄集結構閘（app==sel _candidates 鍵集）：{_msg_ks}")
    if not _ok_ks:
        rc = 1
    try:
        import test_corner_priority_golden as g
        g.test_fig8_golden()
        print("  ✅ 圖8 golden PASS（1地號=0.6685、2地號=0.3315、winner=1地號）")
    except Exception as e:
        print(f"  🔴 圖8 golden FAIL: {e}")
        rc = 1
    try:
        import test_pool_slot as ps
        _n_ps = ps.run_all_cases()
        print(f"  ✅ 滑池槽 golden PASS（{_n_ps}/8：KL例 J=1.80/1.50㎡＋E1-E7）\n")
    except Exception as e:
        print(f"  🔴 滑池槽 golden FAIL: {e}\n")
        rc = 1

    # ── 🆕 甲-1(c)（KL 裁 2026-07-25）：**禁寫死本機絕對路徑**之全倉機檢 ──────────────────
    #   案由：`verify/fixture_end_fallback.py` 曾寫死 `REPO = r"<本機絕對路徑>"`
    #   ⇒ 自 `e45bbb2` 起 `run_all` 在**任何非本機機器**上必 FAIL（claude.ai 他機實跑 rc=1·
    #   FileNotFoundError；另二夾具 rc=0）。此為泛用化直接違例，故立永久機檢。
    #   ⚠️ 樣式以**片段串接**構成——否則本閘會咬到自己（自我匹配·假紅）。
    _ok_abs, _abs_hits = True, []
    _ABS_PAT = ["C:" + "/", "C:" + "\\", "/" + "Users" + "/",
                "Desktop" + "/land", "Desktop" + "\\land"]
    for _root, _dirs, _files in os.walk(REPO):
        _dirs[:] = [d for d in _dirs if not d.startswith(".")
                    and d not in ("__pycache__", "node_modules")]
        for _fn in _files:
            if not _fn.endswith(".py"):
                continue
            _fp = os.path.join(_root, _fn)
            try:
                _txt = open(_fp, encoding="utf-8").read().splitlines()
            except Exception:
                continue
            for _i, _ln in enumerate(_txt, 1):
                if any(_pt in _ln for _pt in _ABS_PAT):
                    _abs_hits.append(f"{os.path.relpath(_fp, REPO)}:{_i}: {_ln.strip()[:90]}")
    if _abs_hits:
        _ok_abs = False
        rc = 1
    print(f"  {'✅' if _ok_abs else '🔴'} 禁寫死絕對路徑閘（全倉 *.py）："
          + ("0 命中" if _ok_abs else f"{len(_abs_hits)} 命中"))
    for _h in _abs_hits[:12]:
        print("     " + _h)

    # ── 🆕 F-2（KL 裁 2026-07-25）：**末端機制三夾具納入 run_all** ──────────────────────
    #   覆蓋率洞：三檔存在於 `verify/` 卻**不在任何自動流程內**——「沒人檢查 ≠ 相符」
    #   （交接文 §5.2）。以 **subprocess** 起（`fixture_end_fallback` 於 import 期即
    #   `sys.exit()`，直接 import 會把 harness 一併帶走）。
    #   ⚠️ 本段屬 run_all `[1/3]` golden 段、**不進** `run_verification.results`
    #      ⇒ 不動 PASS/FAIL 計數，亦不動 P-H 之「161 名目」母體。
    import subprocess
    for _fx, _what in (("fixture_cad_binding_order.py", "🆕 C-6 CAD 線層綁定·順序不變性(3 置換)"),
                       ("fixture_baseline_candidates.py", "🆕 C-5 BASELINE 候選三分支＋R1 共線 golden"),
                       ("fixture_n14_min_width.py", "🆕 N-14/N-15 宗地最小寬度·深度帶內取 min"),
                       # 🆕 K-6-A2 段五(c)-2 之**合成案**：`baseline_pts` 餵值鏈在 `main()` 內
                       #   ⇒ `run_all` 從不執行之（`CLAUDE.md:56`）。掛入本清單之由 ＝ 上方
                       #   同一段註解所指之**覆蓋率洞**（「檔存在於 verify/ 卻不在任何自動流程內」）。
                       ("fixture_n14_feed_chain.py",
                        "🆕 K-9-6-b 餵值鏈合成案·逐街廓路由＋查無 BASELINE 停機"),
                       ("fixture_block_depth_n19p.py",
                        "🆕 K-8 §二 N-19′ 街廓平均深度·app 真符號 vs 裁定靶(六塊+region_min)"),
                       ("fixture_corner_range_k8.py",
                        "🆕 K-8 §三〜§五 街角規定範圍新構造·構造/單調性自檢＋判別力反例"),
                       ("fixture_end_reserve.py", "P2-f 末端保留·窗位移(左右)"),
                       ("fixture_end_fallback.py", "§4 無勝者 fallback·守恆真檢(左右)"),
                       ("fixture_end_winner.py", "末端 gate 判別力·_unfront_area＋咬合反例"),
                       # 🆕 `W-G.9-4b`：app `_WF_NS_NAMES` ↔ 引擎 `ns[...]` 接線守護。
                       #   掛入本清單之由 ＝ 該缺陷本應由 `run_verification` 之 **W-8 反向閘**
                       #   攔下，惟該閘所在之「W-G G.1 接線層 ctx-builder 同源」於到達差集
                       #   檢查**之前**即以 `KeyError: '0m'` 崩（見 `out/WG94_runall.log`
                       #   之 `[G.1] '0m'`）⇒ **閘在、但為死閘**。本夾具**繞過**它、**不修**它
                       #   （上游屬另案·`W-G.9-4b` §3 明文不修）。
                       ("fixture_wf_ns_wiring.py",
                        "🆕 W-G.9-4b app 接線清單↔引擎 ns[] 消費（AST 靜態＋_wf_ns() 實跑＋竄改自檢）"),
                       # 🆕 `W-G.9-8`：三支**真 app 路徑端到端複本**（`wg_g1_smoke`／
                       #   `wg_g2_smoke`／`wg_g3`——後者為 `CLAUDE.md` 所訂 W-G 收官判準 ①
                       #   之終驗工具）此前**皆不在任何自動流程內**（`W-G.9-6` §6）＝上方
                       #   同一段註解所指之覆蓋率洞。
                       #   🔒 **受詞非「跑不跑得通」**（⛔ 那會新增三個永紅項＝把
                       #      `W-G.9-6`／`W-G.9-7` 剛修好的病再造一次），而是
                       #      **「終止點 ＋ 終止原因，與凍存者相符」**（考古 65 第四層）。
                       #   ⚠️ **設計意圖**：結構閘另案修好後三支會跑得更遠 ⇒ 終止點改變
                       #      ⇒ 本夾具**轉紅**⇒ 逼人來看並更新凍存。**這是特性，不是缺陷。**
                       ("fixture_e2e_termination.py",
                        "🆕 W-G.9-8/9-9 三支端到端複本·終止點凍存對帳（受詞已投影去呈現層＋wv_reconcile R1/R2 三分類）"),
                       # 🆕 `W-G.9-10`：`G3` 三項（`W-D.3 碎片`／`W-F F.3`／`W-G G.2`）之
                       #   主判定站點共 **15 個、一個都沒登記過**（`verify/tools/wg910_g3_dissect.py`）
                       #   ——名單上者皆為 `except` 分支之名目 ⇒ **原命題從未被正面驗證**。
                       #   🔒 本夾具只守其中**經現查證實不依賴管線**之 3 個；
                       #      其餘 12 個之**守備移交清單**見 `W-G.9-10` 報告。
                       #   ⛔ 判準常數一律自 `run_verification.py` 之 AST 抽取（⛔ 不抄寫·`#20` 族）。
                       ("fixture_g3_static_guards.py",
                        "🆕 W-G.9-10/9-12 不依賴管線之主判定（F.2/F.3/F.4 靜態閘＋F.3 跨區段 fixture＋G.2 只寫不讀）"),
                       # 🆕 `W-G.9-13`：**中間層 6 項**（需 CAD 管線·⛔ 不需 `run_step_g`）。
                       #   案由與上一列同族——該 6 個命題與**實需** `run_step_g` 之判定
                       #   **同處一個 `try`**，上游一破即全落入 `except`（**考古 70**）
                       #   ⇒ 自 `W-G.9-11` 全掃起確認其**不再被評估**。
                       #   🔒 本夾具**自建管線至其所需之層**（`harvest`→`build_pipeline`
                       #      →`build_build_parcels`），⛔ **全程不經** `run_step_g`。
                       #   ⛔ 判準一律自 `run_verification.py` 之 AST 抽取後**就地求值**
                       #      （⛔ 不抄常數·`#20` 族）；其判準**共四型**、碼面**第二元素皆為
                       #      `Name`** ⇒ 須再解析其 `Assign`，⛔ 照 `G-2` 之內嵌式外推會得
                       #      **6 個空閘**（實證見 `out/probe_WG913_gate_selfcheck.log`）。
                       ("fixture_midlayer_6items.py",
                        "🆕 W-G.9-13 中間層 6 項（v3 率錨三項＋reverse-test③＋F.2 跨區段 fixture＋F.4 模式二 p_avg；四型判準同源就地求值）"),
                       # 🆕 `W-G.9-69`：**乙式耦合斷言**（KL 裁 2026-08-19 之耦合條款·`Z-1`／`Z-2`）。
                       #   🔒 **掛入本清單之由 ＝ 該耦合若無機械載體，豁免會<u>靜默</u>失效**——
                       #      `K-9-5-15 二`「街角第 1 宗寬度不另量、面積夠即算過」與 `GB-84` 之結案，
                       #      **其前提是構造為乙式**；構造若被回退，**「不設閘」本身沒有可紅之物**。
                       #      ⇒ 本夾具即**那個可紅之物**；**其轉紅 ⇒ `GB-84` 之結案自動回復為未結**。
                       #   ⚠️ **判別力已實證二式並試**（`W-G.9-69` §B）：變異 `A`（只改 `S1_perp`
                       #      取值）**繞得過** `app.py` 自身之構造自檢（該自檢為閉式自證）⇒ **本夾具
                       #      是它唯一的可紅之物**；變異 `B`（真甲式）則由生產碼自檢先行 `_stop`。
                       #   🔒 **純加性**：⛔ 未取代任何既有閘；本清單 13 → **14** 支。
                       ("fixture_yi_construction.py",
                        "🆕 W-G.9-69 乙式耦合斷言（垂距＝max(_seg_P0Ps·sinθ,T)·八格×二情境＋二式變異判別力）"),
                       # 🆕 `W-G.9-73`：**登記表完整性稽核**（`GB-N` 之定義列）。
                       #   🔒 **掛入本清單之由 ＝ 該家法此前只存在於人的注意力裡**——
                       #      `W-G.9-72` 以**單式**量定義列得「86 中 74 懸空」（量測器偽影），
                       #      改二式得殘數 2，而**該殘數未再受同一懷疑**（考古 97）。
                       #      三式並取 ＋ 缺號**自登記表現讀**後，真懸空 ＝ 0。
                       #   ⚠️ **路徑含 `tools/`**：本迴圈以 `os.path.join(HERE, _fx)` 起 subprocess
                       #      ⇒ 相對路徑可用；⛔ 未改本迴圈一行。
                       #   🔒 **純加性**：⛔ 未取代任何既有閘；本清單 14 → **15** 筆。
                       # 🆕 `W-G.9-184`：**`GB-123` 之守備**（`M-E-4` 候選 (a)·發單側裁 `§六 四`）。
                       #   🔒 掛入本清單之由 ＝ **生產路徑（app）之池⛔ 無任何自動守備**——
                       #      `run_all` 所掛各項之 `got` 端經 `app.py:main()` 產生者 ＝ **`0`**
                       #      （`CLAUDE.md`：「`main()` 內之敘述**從不被 `run_all` 執行**」）；
                       #      而 `W-G.9-183R` 已判「本波所尋之**覆蓋自檢實不存在**」（式(ii) 構造恆真）
                       #      ⇒ 覆蓋類自檢**結構上⛔ 不可能**偵測之 ⇒ **唯一可行者係值之直接對拍**。
                       #   ⚠️ **射程外**（`VR-082`·詳見該檔 docstring）：① 只守**已入倉之那一趟**
                       #      （KL 下次實跑須**人工入倉**⇒ 仍非全自動·`GB-123` **⛔ 未消滅**）；
                       #      ② 該 log 之態⛔ 不可自證（`GB-119`）；③ 守**變動**⛔ 非守**正確**。
                       #   🔒 **純加性**：⛔ 未取代任何既有閘；本清單 15 → **16** 筆。
                       ("fixture_klui_t2diag.py",
                        "🆕 W-G.9-184 GB-123 守備·KL UI [T2-DIAG] 整列凍存對拍（R5 缺席為期望事實＋判別力自檢七造）"),
                       ("tools/wg973_gb_integrity.py",
                        "🆕 W-G.9-73 登記表完整性稽核（GB-N 定義列·三式並取＋缺號現讀＋懸空逐項列名）")):
        try:
            _r = subprocess.run([sys.executable, os.path.join(HERE, _fx)],
                                capture_output=True, text=True, encoding="utf-8", timeout=600)
            _ok_fx = (_r.returncode == 0)
        except Exception as _e_fx:
            _r, _ok_fx = None, False
            print(f"  🔴 末端夾具 {_fx} 執行失敗：{_e_fx}")
        if _r is not None:
            print(f"  {'✅' if _ok_fx else '🔴'} 末端夾具 {_fx}（{_what}）rc={_r.returncode}")
            if not _ok_fx:
                for _ln in ((_r.stdout or "") + (_r.stderr or "")).strip().splitlines()[-10:]:
                    print("     " + _ln)
        # ── 🆕 K-8 前置 A（KL 裁 U-K8-1 ＝ 乙）：**引擎 ↔ 快照 脫鉤清單·每趟必顯**──
        #   案由：快照留到 K-8 全案完成後一次換 ⇒ 引擎側深度已是 N-19′、harness 仍吃舊值。
        #   `130 PASS / 2 FAIL` ＋ 名目雙向 diff 為 0 **證明的是「舊輸入下什麼都沒變」**，
        #   不是「段二正確」。該誤讀必須由機器擋住，不能靠讀報告。**不判紅**（脫鉤係 KL 授權）。
        #   🆕 **K-8 §三 commit A 後：執行期深度脫鉤已解除**（`load_snapshot()` 記憶體注入
        #     ＋ `stepg_pipeline.assert_depth_same_source` loud 閘）⇒ 本清單自此顯示
        #     「制度甲＝檔案仍凍結、執行期已同源」。**殘餘脫鉤項＝檔案本體與 v3 baseline
        #     尚未重烤**（U-K8-1＝乙），故本清單**續留**、續不判紅。
        if _fx == "fixture_block_depth_n19p.py" and _r is not None:
            _t10 = []
            _on = False
            for _ln in (_r.stdout or "").splitlines():
                if "【T10】" in _ln:
                    _on = True
                if _on:
                    # ⚠️ T10 標題後緊接一條分隔線 ⇒ 須跨過它；只在**已收到表身**後才收段
                    #   （初版於首條分隔線即 break，導致清單只印出標題一行）
                    if _ln.startswith("---") and len(_t10) > 2:
                        break
                    _t10.append(_ln)
            print("     ┌─ 引擎↔快照 脫鉤清單（K-8 前置 A·不判紅）"
                  + "─" * 30)
            for _ln in _t10 or ["     （T10 段未取得——夾具輸出格式已變？）"]:
                print("     │ " + _ln.rstrip())
            print("     └" + "─" * 68)
        if not _ok_fx:
            rc = 1

    # ── 🆕 BLOCKED-3（claude.ai 2026-07-27·**二度指認**）：E 系列實測快照比對閘 ──────────
    #   案由：E 系列之全部實測依據（45/59 之 µm 級距離／R3 0.7655／R4 −1.48e-2／R3 頂點）
    #   先前**只存在於聊天與註解**，`verify/probes/` 無對應檔 ⇒ **倉內不可重現**。
    #   本閘＝逐宗快照 diff ＋ **T1–T6 獨立真值斷言**（後者才是正確性舉證；
    #   快照本身之身分為**回歸快照**、非真值錨——見探針 docstring）。
    #   ⚠️ 同 F-2：本段屬 `[1/3]` golden 段、**不進** `run_verification.results`
    #      ⇒ **不動 PASS/FAIL 計數**，亦不動 P-H 之名目母體。
    _probe = os.path.join(HERE, "probes", "probe_ruling_N_e1_touch.py")
    try:
        _rp = subprocess.run([sys.executable, _probe],
                             capture_output=True, text=True, encoding="utf-8", timeout=900)
        _ok_pr = (_rp.returncode == 0)
    except Exception as _e_pr:
        _rp, _ok_pr = None, False
        print(f"  🔴 E 系列實測快照閘 執行失敗：{_e_pr}")
    if _rp is not None:
        print(f"  {'✅' if _ok_pr else '🔴'} E 系列實測快照閘"
              f"（E-1′雙向/E-2′/E-8a凸性/E-8b單點/E-9起點/E-10解析弦·兩情境逐宗）"
              f"rc={_rp.returncode}")
        if not _ok_pr:
            for _ln in ((_rp.stdout or "") + (_rp.stderr or "")).strip().splitlines()[-14:]:
                print("     " + _ln)
    if not _ok_pr:
        rc = 1

    # ── 🆕 K-4 第 5 條（KL 裁 2026-07-27）：街角第 1 宗之 S 起算點 ──────────────────
    #   閘內容：①FRONT_LINE 端點 ≡ FRONT×SIDE 無限直線交點（八側·1e-6）
    #          ②`s(p2) ≡ |FRONT|` 恆等式（斜交軸可比性之前提）
    #          ③三變體衝擊表（含 **patch 載具自檢**：以 patch 重現未 patch 語意須逐格全等）
    #   ⚠️ 同 F-2：走 `[1/3]` golden 段 ⇒ **不動 PASS/FAIL 計數**。
    _probe_k4 = os.path.join(HERE, "probes", "probe_ruling_K4_s_origin.py")
    try:
        _rk = subprocess.run([sys.executable, _probe_k4],
                             capture_output=True, text=True, encoding="utf-8", timeout=1800)
        _ok_k4 = (_rk.returncode == 0)
    except Exception as _e_k4:
        _rk, _ok_k4 = None, False
        print(f"  🔴 K-4 S 起算點閘 執行失敗：{_e_k4}")
    if _rk is not None:
        print(f"  {'✅' if _ok_k4 else '🔴'} K-4 S 起算點閘"
              f"（FRONT 端點≡理論角/恆等式/三變體衝擊·patch 載具自檢）rc={_rk.returncode}")
        if not _ok_k4:
            for _ln in ((_rk.stdout or "") + (_rk.stderr or "")).strip().splitlines()[-14:]:
                print("     " + _ln)
    if not _ok_k4:
        rc = 1

    # ── 🆕 K-8 段一（KL 裁 2026-07-31）：BASELINE↔街廓 配對之**驗證** ＋ N-19′ 對照靶 ──
    #   ⚠️ 驗證**既有** C-1/C-2/C-3/C-5 機制之正確性，**非新機制**——配對碼不動。
    #   併看守 K-8 不變式（BASELINE 一律以**無限直線**參與量測）。
    #   ⚠️ 同 F-2：走 `[1/3]` golden 段 ⇒ **不動 PASS/FAIL 計數**。
    # ── 🆕 K-8 前置 B：SIDE_LINE↔街廓／側別 配對之**驗證**（既有 C-6·非新機制）──
    #   ⚠️ 施工單原稱此處為「貪婪式 1:1」——係 Phase 11 陳舊註解；C-6 已改結構判準。
    _probe_sl = os.path.join(HERE, "probes", "probe_ruling_K8_sideline_pairing.py")
    try:
        _rsl = subprocess.run([sys.executable, _probe_sl],
                              capture_output=True, text=True, encoding="utf-8", timeout=900)
        _ok_sl = (_rsl.returncode == 0)
    except Exception as _e_sl:
        _rsl, _ok_sl = None, False
        print(f"  🔴 K-8 SIDE_LINE 配對驗證閘 執行失敗：{_e_sl}")
    if _rsl is not None:
        print(f"  {'✅' if _ok_sl else '🔴'} K-8 SIDE_LINE 配對驗證閘"
              f"（8 實體／8 街角側／勝差>1.0m 無共用／app 輸出逐格對拍）rc={_rsl.returncode}")
        if not _ok_sl:
            for _ln in ((_rsl.stdout or "") + (_rsl.stderr or "")).strip().splitlines()[-14:]:
                print("     " + _ln)
    if not _ok_sl:
        rc = 1

    _probe_k8 = os.path.join(HERE, "probes", "probe_ruling_K8_baseline_pairing.py")
    try:
        _r8 = subprocess.run([sys.executable, _probe_k8],
                             capture_output=True, text=True, encoding="utf-8", timeout=900)
        _ok_k8 = (_r8.returncode == 0)
    except Exception as _e_k8:
        _r8, _ok_k8 = None, False
        print(f"  🔴 K-8 配對驗證閘 執行失敗：{_e_k8}")
    if _r8 is not None:
        print(f"  {'✅' if _ok_k8 else '🔴'} K-8 配對驗證閘"
              f"（既有 C-2/C-5 配對·集合斷言 R1/R4∈{{#0,#2}}·N-19′ 六塊對照靶）"
              f"rc={_r8.returncode}")
        if not _ok_k8:
            for _ln in ((_r8.stdout or "") + (_r8.stderr or "")).strip().splitlines()[-14:]:
                print("     " + _ln)
    if not _ok_k8:
        rc = 1

    # 🗄️ **K-4-3 來源母體閘已隨 M-5 封存移除**（K-6 §四·KL 裁 2026-07-30 作廢）
    #   探針移至 `verify/archive/probe_ruling_K4_3_source.py`；禁再掛回。
    print()

    print("### [2/3] diff 引擎自檢（竄改必咬＋Gxxx 分流；證綠非虛）")
    import run_verification as v
    if not v.self_check_diff_engine():
        print("  🔴 diff 引擎自檢 FAIL → 對拍結果不可信，停")
        rc = 1
    print()

    print("### [3/3] W-V headless 對拍（verify/run_verification.py）")
    # 🆕 `W-G.9-7`（KL 2026-08-11 裁：驗收改「**名稱＋原因一併比對**」）：
    #   對帳須於**每次 `run_all` 中自動發生**——⛔ 不得再造一個「檔存在於 `verify/`
    #   卻不在任何自動流程內」之洞（見上方 F-2 段之覆蓋率洞註解；`W-G.9-6` §6 同族）。
    #   **做法**：`run_verification.main()` 之 `results` 為函式內區域變數（`:502`）、
    #   且只回 `0/1` ⇒ 對帳器取不到結構化結果物件。故以 **tee**（寫穿至真 stdout
    #   ＋ 同時累積）擷取其輸出後餵給 `wv_reconcile`。
    #   ⛔ **零修改 `run_verification.py`、⛔ 不觸 `results`、⛔ 不新增任何
    #      `results.append`** ⇒ **PASS/FAIL 層不變**。
    import contextlib as _ctxlib
    import wv_reconcile as _wvr

    class _Tee:
        """寫穿 ＋ 累積；未知屬性委派真 stdout（`run_verification:497` 之 `reconfigure`）。"""

        def __init__(self, real):
            self._real, self.buf = real, []

        def write(self, s):
            self.buf.append(s)
            return self._real.write(s)

        def flush(self):
            self._real.flush()

        def __getattr__(self, n):
            return getattr(self._real, n)

    _tee = _Tee(sys.stdout)
    with _ctxlib.redirect_stdout(_tee):
        rc2 = v.main()
    rc = rc or rc2
    print()
    _rc_recon = _wvr.reconcile_text("".join(_tee.buf))
    # 🔒 併入 `rc` 之由（`W-G.9-7` 前置登記 §3-2·已登記其代價）：若**只印不併**，
    #   即新造一道**永遠不能使任何東西變紅**之閘 ＝ 本波所修之病灶本身（考古 65／66）。
    #   ⚠️ 本分支為「准紅碼」、`rc` 本即為 `1` ⇒ **今日之可觀測影響為零**；
    #      未來全綠時，`ALL GREEN` 一行將受對帳左右。**已知並接受。**
    rc = rc or _rc_recon

    print("\n" + "#" * 60)
    print("W-V run_all:", "ALL GREEN" if rc == 0 else "FAIL")
    return rc


if __name__ == "__main__":
    sys.exit(main())
