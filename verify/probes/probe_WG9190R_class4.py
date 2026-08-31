# -*- coding: utf-8 -*-
r"""**`W-G.9-190R` commit `5`**：`S-6` 四分分類器之**驅動檔**（⛔ 零生產碼）

## 為何另立驅動檔（⛔ 非另寫一份分類器）

單 `§十` 令「於 `probe_WG9189_s6_replica.py` **末端追加**（⛔ 不改既有判定路徑）」。
🔒 **分類器之本體確已末端追加於該檔**（`classify4` ／ `classify4_main`），
且其**置於 `if __name__ == "__main__":` <u>之後</u>** ⇒ 以腳本執行該檔時
`sys.exit(main())` 已先終止 ⇒ **既有判定路徑逐位未動、且⛔ 不受影響**
（機檢：`deletions = 0` ＋ 嚴格前綴 `True`）。

⇒ 其**入口**須由外部 `import` 後呼叫；本檔即該入口，**⛔ 未複製分類器之任何一行**。

## 出艙

`verify/out/probe_WG9190R_class4.log`。`rc` ＝ 判別力造未判甲 ⇒ `1`
（`§十一-1` 停機款 `10`）；**類甲數本身⛔ 非停機款**（`§十` 逐字：預測·⛔ 非停機款）。
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
sys.path.insert(0, VERIFY)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(VERIFY, "fixtures"))

import probe_WG9189_s6_replica as R                              # noqa: E402


def main():
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8")
        except Exception:                                        # noqa: BLE001
            pass
    R.L.clear()
    rc = R.classify4_main()
    out = os.path.join(VERIFY, "out",
                       os.environ.get("WV_OUT_NAME") or "probe_WG9190R_class4.log")
    if os.path.exists(out) and os.environ.get("WV_ALLOW_OVERWRITE") != "1":
        raise RuntimeError("拒絕覆寫既有 log：" + out)
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(R.L) + "\n")
    print("\n  ✅ 已落檔：%s" % out)
    return rc


if __name__ == "__main__":
    sys.exit(main())
