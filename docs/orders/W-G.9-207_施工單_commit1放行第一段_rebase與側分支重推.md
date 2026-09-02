# 🧾 `W-G.9-207` 施工單　`W-G.9-198R` `commit 1` 之放行（第一段：rebase ＋ 側分支重推 ＋ **停機**）

> **性質**：🔴 **含生產碼**（其物件即 `commit 1`）⇒ **⛔ 推 `wip/s1-endpart`**。本單只辦 rebase 與**側分支**之重推，主線之推進另由 `§三` 於發單側驗畢後為之。
> **開工態**：`wip/s1-endpart` ＝ `90f9d2cc65d4e6dbd548d8287eeecd497bf44f1c`；側分支 `verify/W-G.9-198R-c1` ＝ `48bad3c2e480349944bee5bf29100a261dd5e98b`
> **通則逐字**：**只有真觸及域邊界才停機上呈、純技術自行做完。**

🔒 **KL 已放行（`2026-09-02`·逐字）**

> 「是 放行 `commit 1` 進主線」

🛑 **放行之受詞 ＝ 發單側已自側分支逐位元組復驗之<u>內容</u>**（三檔／`numstat` 三值／三 blob），**⛔ 是某一個 SHA**。rebase 後之 `48bad3c′` 須先過 `§一` 之等值判準，經發單側逐字確認等值，主線方得推進（`W-G.9-206 §八`）。

---

## §零　開工閘

| 閘 | 判準 |
|---|---|
| `S-0a` | `git ls-remote origin refs/heads/wip/s1-endpart` ＝ `90f9d2cc65d4e6dbd548d8287eeecd497bf44f1c`。🔒 若已前進，僅在 `git rev-parse <新頭>:app.py` 仍 ＝ `b9a50a2e58ad46ac3d4288bad978c17e87b8fb27` 且 `verify/stepg_pipeline.py`／`verify/run_all.py`／`verify/run_verification.py` 三檔 blob 亦未變時，閘綠；否則**停機上呈** |
| `S-0b` | `git ls-remote origin refs/heads/verify/W-G.9-198R-c1` ＝ `48bad3c2e480349944bee5bf29100a261dd5e98b` |
| `S-0c` | 本單 `SELF_SHA256` 自驗相符 |
| `S-0d` | `PYTHONIOENCODING=utf-8 python verify/probes/probe_order_preflight.py <本單>`；🟡 逐項以**字樣錨**具名（⛔ 用行號）並依裁 `H` 歸類 |

🔒 **行尾（`GB-139`）**：`clone` 用 `-c core.autocrlf=false -c core.quotepath=false`；`add` 既有檔一律常規 `add`；**閘之受詞一律取倉側 `git cat-file blob`**。

---

## §一　工項 `1`：rebase ＋ 等值自證

1. 將 `48bad3c2e480349944bee5bf29100a261dd5e98b` **rebase 至當時之主線頭**，得 `48bad3c′`。
   🛑 **⛔ 動 payload 一字**——⛔ `amend` 訊息、⛔ 併入任何新變更、⛔ 順手修任何觀察項。
2. 🔴 **等值判準（四項全須成立·⛔ 得省·任一不符 ⇒ 停機上呈，⛔ 自行歸因）**

| # | 判準 | 命令 |
|---|---|---|
| `E-1` | `48bad3c′` 之父 ＝ **`S-0a` 所實查之主線頭全 `40` 碼** | `git rev-parse 48bad3c′^` |
| `E-2` | `git show --name-only --format= 48bad3c′` **恰三檔** ＝ `app.py`／`verify/run_verification.py`／`verify/selection_pipeline.py` | 同左 |
| `E-3` | `numstat` 逐檔 ＝ `app.py 110/1`／`verify/run_verification.py 3/0`／`verify/selection_pipeline.py 11/0` | `git show --numstat --format= 48bad3c′` |
| `E-4` | 🔴 **三檔之 blob 逐檔與 `48bad3c` 相同**（**全 `40` 碼**·⛔ 用短碼）：`app.py` ＝ `6f0317e47ef92c7e06d6d904ecf2d129656bd331`／`verify/run_verification.py` ＝ `d07955c58e67ec06260971a74b5aabe5e846f106`／`verify/selection_pipeline.py` ＝ `10f90c509ae13c77c83e3e5c76fe3c09ca675b14` | `git rev-parse 48bad3c′:<檔>` 三次 |

3. 🔒 **判別力自證（⛔ 省）**：對**未參與本 commit** 之一檔（建議 `docs/rulings/K-6_街角地分配程序與可分配判準.md`）報其於 `48bad3c` 與 `48bad3c′` 之 blob——**二者應<u>相異</u>**（因 `48bad3c′` 已含 `W-G.9-206` 之 `K-9-26`）。若該檔亦相同 ⇒ **rebase 未生效** ⇒ 停機。
   🛑 此項與 `E-4` 方向相反，二者並存方證「payload 不變 ∧ 基座已換」。

---

## §二　工項 `2`：強制更新側分支，然後**停機**

1. `git push --force-with-lease origin 48bad3c′:refs/heads/verify/W-G.9-198R-c1`
2. `git ls-remote origin` 復驗二 ref 並逐字回報：側分支 ＝ `48bad3c′` 全 `40` 碼；**`wip/s1-endpart` 仍 ＝ `S-0a` 所實查之值**（⛔ 前進）。
3. 🔴 **停機。⛔ 執行 `§三`。** 回報 `E-1`〜`E-4` ＋ 判別力自證 ＋ 二 ref 之 `ls-remote`，交發單側復驗。

---

## §三　工項 `3`：**⛔ 得逕行** —— 主線之推進

🛑 **本節須待發單側逐字回覆「`48bad3c′` 等值已驗·准推主線」後方得執行。** 在此之前執行本節即係違反 `-198R §三-3`。

```
git push origin 48bad3c′:refs/heads/wip/s1-endpart
```

推後須回報：
1. `git ls-remote origin refs/heads/wip/s1-endpart` ＝ `48bad3c′` 全 `40` 碼 ＋ 量測時刻。
2. `git rev-parse <新主線頭>:app.py` ＝ `6f0317e47ef92c7e06d6d904ecf2d129656bd331`（🔴 **本波第一次 `app.py` 之 blob 改變**）。
3. `left-right` ＝ `0 0`。
4. 側分支 `verify/W-G.9-198R-c1` **保留⛔ 刪**（史料·供日後對照）。

---

## §四　落地稽核與其後

1. 🔴 **`commit 2`／`3` 之開工條件**：主線確實推進至 `48bad3c′` 後方得開工，且 `commit 2` **須含 `W-G.9-206 §七 補一-3`**——`k6b_stage2_global_order` docstring 內現載為「CC 之技術判讀」之 ②③ 方向，改述為**引 `K-9-26`**（KL 裁 `2026-09-02`）。🛑 **⛔ 得為此重做或 amend `commit 1`。**
2. 🔒 **攢批（本單⛔ 辦·僅記）**
   - `自誤 261`：`W-G.9-206 §一` 令推側分支而**⛔ 載該物件與受單方本機分支之關係**，亦⛔ 明訂本機分支之處置；CC 以「本地 ref ＋ 遠端側分支」二重保全後 `reset --hard` 退回基座 ⇒ **正辦**。一般式：**凡令受單方推送某物件者，須同格載明該物件與其本機 `HEAD`／分支之關係，並明訂本機分支之處置。**
   - 🟡 **觀察（無土地後果）**：段一之平手判定取 `priority_index` **`4dp`**（`-198R R1-2`），而段二鍵 ③ 取 **`6dp`**（`app.py:13137` 之 `round(..., 6)`）⇒ 同一量於二處採不同精度。今日段二無消費端 ⇒ 無後果；**須於段三落地前收斂**。
   - 其餘在案：`GB` 定義列式之正典化（`GB-138` 處置③）。
3. 🔒 **次號現為**：自誤 `261`／`GB 140`／`VR 090`／戒 `41`／`K-9 27`。

---

## §五　停機條件

- `E-1`〜`E-4` 任一不符 ⇒ **停機上呈**，⛔ 自行 rebase 第二次、⛔ 自行歸因。
- 判別力自證顯示 `K-6` blob 於二 commit 相同 ⇒ **停機上呈**（rebase 未生效）。
- `S-0a` 發現主線之生產碼四檔任一 blob 已變 ⇒ **停機上呈**。
- `§二-2` 發現 `wip/s1-endpart` 已前進 ⇒ **停機上呈**。
- 其餘純技術事項自行做完，於回報中載明。

🛑 **本單⛔ 有「全綠即逕推主線」之款。** `§三` 之觸發權在發單側。
SELF_SHA256: 26dfe7ada49a9bf362703acf3c371aa15db3f4d4110b8d0453f69986914daf65
