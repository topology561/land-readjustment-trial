# `W-G.9-385R`　入主線　執行報告（`W-G.9-385` 補令三·主線快轉至 `8d0a990`）

> **受單** ＝ CC 窗（`2026-10-17`·續 `W-G.9-385` 之窗）。**來源檔** ＝ KL 主 checkout 之根（第二處·二進位複製·入倉後 `git cat-file blob` 與來源 `cmp` 同）；KL 之訊唯貼檔之路徑、⛔ 載 bytes／`sha256` ⇒ 以 `SELF_SHA256` 為據（`d6d8dd0d…bb23934e` 相符）。
> context 餘量（開場自報）：約 `14.98M` tokens。
> 收工閘之實測值與工項二⁗、三⁗ 之出艙於對話（⛔ 寫入本檔·自指）。

---

## ① 逐 `commit` 之 hash 與工項

| 工項 | `commit` | 內容 |
|---|---|---|
| 工項零′⁗ 主線快轉 | （無 `commit`） | 遠端 `refs/heads/wip/s1-endpart`：`158f7fe959697571d8179988cd4c192c0016ead9` → `8d0a99091b848bd33637f94ed8323c276ce81f74`（`git push origin 8d0a99091b848bd33637f94ed8323c276ce81f74:refs/heads/wip/s1-endpart`·首推即成·`158f7fe..8d0a990`） |
| 工項零⁗ | `fac7e04438db5813bad80c7119ddaa84f536f048` | `docs/orders/W-G.9-385_補令三.md` `161`／`0`·`8d0a990..fac7e04` |
| 工項一⁗ | （本檔之 `commit`） | 本檔 |

## ② 停機款（款·期·實）

| 款 | 期 | 實 |
|---|---|---|
| `1⁗` | 主線 `158f7fe`·側支 `8d0a990`·heads `45`·追蹤檔⛔ 變·`§零` 項 `3`·旗標 | 皆符（四簿 自誤 `608`／`623`、`GB` `197`／`205`、`VR` `80`／`95`、`K-9` `76`／`79`·缺號 ＝ 期；旗標 `[None×5]`；`<O>\heads_before_385p3.txt` `45` 列） |
| `2⁗` | `SELF_SHA256`·入倉之 blob | 皆符（`24188` B·全檔 `sha256` `c708514d…92aa5109`·`161` 列·CR `0`·`P-5` 受詞 `24110` B） |
| `3⁗` | 工項零′⁗ 前置 | 皆符（下開③） |
| `4⁗` | 快轉之推⛔ 被拒 | 皆符（首推即成·⛔ `--force`） |
| `5⁗` | 快轉後 ①〜④ | 皆符（下開③） |
| `6⁗` | 工項零⁗、一⁗ 之推之目標唯 `wip/s1-endpart`·⛔ 推側支 | 皆符 |
| `7⁗` | 收工閘 | 出艙於對話 |
| `8⁗` | 工項二⁗ | 出艙於對話（於收工閘之後） |
| `9⁗` | 工項三⁗ 前置 | 出艙於對話 |
| `10⁗` | ⛔ 自判·⛔ 改器·新檔⛔ ignore | 皆符（本補令、本檔之 `git check-ignore -v --no-index` 無命中） |

## ③ 工項零′⁗ 之前置與快轉後之出艙（全出艙存 `<O>\p3pre\` ＝ `C:\Users\admin\w385o\p3pre\`）

````text
is-ancestor rc=0
count 158f7fe..8d0a990 = 11
count 8d0a990..158f7fe = 0
merges = []
diff name-only:
app.py
app.py cfd66e889f23a502792bec3ddf0fb9c875ec7524
selection_pipeline d197f222076529c700a770915248790e316ce259
stepg_pipeline 2bb2f56ecf9423a99c522ddfbdfb55f314854e27
per-commit:
8d0a99091b848bd33637f94ed8323c276ce81f74 [] lines=0
95c37d6d71e20b963cbc3818dad70b744c8bb956 [] lines=0
1a5ed5710eb248a96d895ba2cfd285abd6fdb074 [app.py] lines=1
f6c9a3a688589b56aa338cca2911ee5f23e3aa2b [] lines=0
98bb2e4ae062bb73f95323c273ac8e2a3fdcbbf7 [] lines=0
c781e6fff64b3dbe2367c74cc4f5a4ee2763640f [] lines=0
01ad480b221fe80bcfc4edd04c997d5569d3eba1 [] lines=0
b248f350f2467a591b7d1056d84c6b9a6802c528 [] lines=0
32bb289f5fe1c44945d20686e34f295fedbf3b54 [] lines=0
e6a22894d5197a4fe16dcbc2dfe5163468130908 [] lines=0
0fc214fe6ed847604ac04ec4ba7e87f6382281c6 [] lines=0
````

（上 ＝ `<O>\p3pre\preconditions.txt` 之全文：前置 `1`、`2`、`3`〔逐筆之判·空輸出者 `[]`／`lines=0`·命中者恰 `1a5ed5710eb248a96d895ba2cfd285abd6fdb074` ＝ `§二⁗` 之放行清單〕；下 ＝ `<O>\p3pre\after_ff.txt` 之全文：快轉後之 ①〜④。）

````text
① 8d0a99091b848bd33637f94ed8323c276ce81f74	refs/heads/wip/s1-endpart
② heads 45
③ prod files: 33 + app.py; vs 8d0a990: 0; vs 158f7fe: app.py 
④ branches containing 1a5ed57:
  origin/verify/W-G.9-385-k974
  origin/wip/s1-endpart
````

## ④ 放行（`§二⁗`·KL 之逐字）

> 執行端保留了兩個本地暫存支（`hold/W-G.9-385-c2`、`hold/W-G.9-385p1-c2`），內容都已併入側支。入主線後可以刪除，下一張補令可以順手處理。
> 確認入主線

（KL `2026-10-16 23:59`·`Asia/Taipei`；發單側讀為工項零′⁗、二⁗、三⁗ 之放行·以發單側之復驗皆符為條件〔`§一⁗` 項 `2`·已符〕；本補令由 KL 貼予 CC 即其確認。）

逐筆放行清單：`1a5ed5710eb248a96d895ba2cfd285abd6fdb074`（首列「`W-G.9-385 補令二 工項二‴：K-9-74 之落地與 K-9-62 二欄之讀取與檢核（補令一之碼〔hold/W-G.9-385p1-c2〕＋ R-16 重疊之容差 0.01 ㎡·R-17 缺表之錯誤）🔴 生產碼（新側支）`」·`app.py`·土地後果：本案配地⛔ 變）——前置 `3` 之逐筆判之命中恰此一筆。

## ⑤ pre-flight

`python verify/probes/probe_order_preflight.py <本補令>`（態 `8d0a990`）⇒ `rc 0`：🔴 機械 `0` 項；🟡 提示 `1` 項——`P-2` `:44`（`§一⁗` 項 `1` 之計數皆 git 之物件之計數）⇒ 本補令 `§五⁗` 項 `3` 之**具名豁免**，照之；ℹ️ `P-5` 相符（受詞 `24110` B）、`P-3` 之 `app.py` `def main` 區間（AST）＝ `23351`–`31093`（`8d0a990` 之 `app.py`·本補令⛔ 用）。

## ⑥ CC 之自捕與自解

⛔ 有（諸前置與快轉後之出艙皆首試即符）。🔒 前置 `2`／`3` 之 `:(glob)verify/*.py` 唯及 `verify/` 之頂層（`e6a2289` 改 `verify/probes/` 之四器而判 `0`·合單之期）。

## ⑦ 各段耗時

開場（`issuer_anchor`·preflight）約 `1` 分；前置 `1`〜`3` ＜ `10` s；快轉與快轉後之出艙 ＜ `10` s；工項零⁗ ＜ `10` s；本檔 約 `5` 分。⛔ 長跑之器（收工閘 `8⁗` 之十呼叫於本檔之後跑之·出艙於對話）。
