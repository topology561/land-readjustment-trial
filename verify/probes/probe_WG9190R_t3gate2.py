# -*- coding: utf-8 -*-
r"""**`W-G.9-190R` 次一 commit·受詞 `1`**：`[T3-GATE]` 之**二情境**補跑驅動器

## 由來（逐字）

`W-G.9-190R` 收工閘 `5`（「`[T3-GATE]` 期末仍為 `39` 列」）於本波**⛔ 未辦**——
其產生端 `verify/probes/probe_WG9187_t3gate.py` 之情境硬寫為 `SB = 0.0 m`，
而該波全部量測係 `SB = 3.5 m`，二情境**⛔ 不可互代**（該檔 `:33` 逐字已戒）。
發單側 `2026-08-31` 放行裁 逐字：「🛑 須於次一零生產碼 commit 補跑，且
`SB = 0.0 m` 與 `3.5 m`【二情境各跑一次】、逐宗具名其變動。⛔ 不得只跑一情境結案。」

## 本檔之作法

🔒 **⛔ 未複製 `probe_WG9187_t3gate.py` 之任何一行**，亦**⛔ 未改該檔一字**
（其為 `W-G.9-187R` 之既有證據鏈，改之即動既有判定路徑）。
本檔以 `import` 取該模組，僅覆寫其**模組級** `SB`，再呼叫其 `main()`——
其 `drive()`／`main()` 皆以模組全域查 `SB`，故覆寫即生效（覆寫後即刻自驗，未生效則 raise）。

- 情境自環境變數 `WV_T3_SB` 取；預設 `0.0`（＝原檔之值）。⛔ 非數即 raise（no-silent-fallback）。
- 輸出檔名自 `WV_OUT_NAME` 取（原檔既有之機制）。

## 🛑 本檔之限（⛔ 不得省）

- `SB = 3.5 m` 時，原檔之 `REF_BLUE`（【倉】`K-9-23-a` 八格）係 **`0m` 情境之錨**
  ⇒ 其「`M-L-5 ①` 跨態不符格」**必然具名**，係**期望事實**、⛔ 非本批之紅。
- 原檔 `:155-156` 之表頭字串硬寫「（⛔ 非 X-T 之 3.5m）」，係為 `SB = 0.0` 而寫；
  於 `3.5m` 情境下**已成偽述** ⇒ 本檔於**檔尾以尾記具名之**（⛔ 不留偽述於倉、
  ⛔ 不改原檔既有任何一列）。
- 本檔**⛔ 不改** `REF_BLUE`、⛔ 不調容差、⛔ 不為求綠而略過任何格。
- `rc` 逕採原檔之回傳（`X-3` 觸發 ⇒ `1`），⛔ 不吞、⛔ 不改判。

⛔ 不改生產碼一字。⛔ 不跑 `run_all`。⛔ 不寫死本機絕對路徑。
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
sys.path.insert(0, VERIFY)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(VERIFY, "fixtures"))

BAR = "=" * 132


def _append_trailer(sb, rc):
    """🔧 尾記：更正原檔硬寫之表頭字串，⛔ 不改其既有任何一列（末端追加）。"""
    name = os.environ.get("WV_OUT_NAME") or "probe_WG9187_t3gate.log"
    path = os.path.join(VERIFY, "out", name)
    t = ["", BAR,
         "🔧 **驅動器尾記**（`verify/probes/probe_WG9190R_t3gate2.py`·⛔ 非 "
         "`probe_WG9187_t3gate.py` 之輸出·⛔ 未改其既有任何一列）", BAR,
         "  🔒 本趟之情境 ＝ **SB = %.1f m**（由 `WV_T3_SB` 覆寫模組級 `SB`；原檔之值 ＝ `0.0`）。" % sb]
    if abs(sb - 3.5) < 1e-12:
        t += ["  🔴 **上文表頭之「（⛔ 非 X-T 之 3.5m）」係原檔 `:155-156` 之<u>硬寫字串</u>**，",
              "     其為 `SB = 0.0` 情境而寫 ⇒ **於本趟（`3.5m`）已成偽述**，⛔ 非本趟之事實。",
              "     🔒 本趟之情境**正是** `3.5 m`（與 `W-G.9-190R` 全部量測、【倉】`177R` 同情境）。",
              "  🔴 **`M-L-5 ①` 之【倉】`K-9-23-a` 八格錨係 `0m` 情境之值**（原檔 `:32` 逐字：",
              "     「與【倉】`K-9-23-a` 同情境（該表逐字：『情境 `0m`／`STEP0=on`』）」）",
              "     ⇒ 本趟之「跨態不符格」係**期望事實**、⛔ 非本批之紅；",
              "     🔒 ⛔ 未改 `REF_BLUE`、⛔ 未調容差、⛔ 未略過任何格。"]
    else:
        t += ["  🔒 本趟與原檔同情境（`0.0 m`）⇒ 表頭字串與 `REF_BLUE` 之錨**皆合**。"]
    t += ["  🔒 `rc` ＝ %d（逕採原檔之回傳·⛔ 未吞、⛔ 未改判）。" % rc, BAR]
    with open(path, "a", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(t) + "\n")
    print("  ✅ 尾記已附：%s" % path, file=sys.stderr)


def main():
    import probe_WG9187_t3gate as t3

    raw = os.environ.get("WV_T3_SB", "0.0")
    try:
        sb = float(raw)
    except ValueError:
        raise RuntimeError("🔴 WV_T3_SB ⛔ 非數：%r（no-silent-fallback：⛔ 不以預設兜底）" % raw)
    old = t3.SB
    t3.SB = sb
    print("  🔒 情境覆寫：probe_WG9187_t3gate.SB  %.1f → %.1f m（WV_OUT_NAME=%s）"
          % (old, t3.SB, os.environ.get("WV_OUT_NAME") or "(預設)"), file=sys.stderr)
    if t3.SB != sb:
        raise RuntimeError("🔴 覆寫未生效 ⇒ ⛔ 不得續跑（否則二情境將得同一結果之假綠）")
    rc = t3.main()
    _append_trailer(sb, rc)
    return rc


if __name__ == "__main__":
    sys.exit(main())
