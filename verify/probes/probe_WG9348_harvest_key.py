# -*- coding: utf-8 -*-
"""W-G.9-348 量測器（發單側窗四十四擬·檔 F7·⛔ 由受單側改一字）：`verify/app_harvest.py` 之快取鍵正規化（`自誤 479`）。

受詞：`app_harvest.harvest(p)` 對「同一檔之不同寫法」是否回傳**同一物件**（⇒ 只 harvest 一次、
`sys.modules['streamlit']` 只被換一次）。
量法：於本行程以 `<repo>/verify` 載入 `app_harvest`，先清其 `_CACHE`，再以同一 `app.py` 之諸寫法逐一呼叫：
  W0 ＝ `os.path.abspath(<repo>/app.py)`（正規形）
  W1 ＝ `<repo>/./app.py`（含 `.` 段；以 `os.sep` 串接）
  W2 ＝ `<repo>/verify/../app.py`（含 `..` 段）
  W3 ＝ 分隔符互換之形（`os.sep` 與 `os.altsep` 互換；`os.altsep` 為 None 之平台〔POSIX〕⇒ 本項記「不適用」、⛔ 計入判）
判：諸寫法之回傳，其二元素（`ns`／`fake_st`）皆 `is` W0 所回者（回傳之 tuple 每次新建·⛔ 以 tuple 比）；`_CACHE` 之鍵數 ＝ `1`；`sys.modules['streamlit']` 自 W0 之後⛔ 被換。
另判（受詞之對照·⛔ 可省）：以同一 `app.py` 之**位元相同之複本**（另一目錄）呼叫 ⇒ 須**非**同一物件、鍵數 ＋1
（證本器所判者為「路徑之同一」、⛔ 為「一律回同一物件」之恆綠）。

用法：python verify/probes/probe_WG9348_harvest_key.py <repo>
  （判別力：於 `57c4623`〔改前〕跑 ⇒ 須 `rc 1`〔W1／W2 各成一鍵〕；改後 ⇒ `rc 0`。）
rc：0 皆如期／1 有不如期者／2 用法錯／3 無從判定（受詞缺）。
"""
import importlib.util
import os
import shutil
import sys
import tempfile

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:  # noqa: BLE001
    pass


def main(argv):
    if len(argv) != 2:
        print(__doc__)
        return 2
    repo = os.path.abspath(argv[1])
    ah_path = os.path.join(repo, "verify", "app_harvest.py")
    app0 = os.path.join(repo, "app.py")
    if not (os.path.isfile(ah_path) and os.path.isfile(app0)):
        print(f"🔴 受詞缺：{ah_path} 或 {app0} ⇒ rc 3")
        return 3
    spec = importlib.util.spec_from_file_location("app_harvest_F7", ah_path)
    ah = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ah)
    if not (hasattr(ah, "harvest") and isinstance(getattr(ah, "_CACHE", None), dict)):
        print("🔴 受詞缺：app_harvest 無 harvest 或 _CACHE ⇒ rc 3")
        return 3
    ah._CACHE.clear()

    forms = [
        ("W0 正規形", app0),
        ("W1 含 . 段", repo + os.sep + "." + os.sep + "app.py"),
        ("W2 含 .. 段", os.path.join(repo, "verify") + os.sep + ".." + os.sep + "app.py"),
    ]
    if os.altsep:
        forms.append(("W3 分隔符互換", app0.replace(os.sep, os.altsep)))
    else:
        print("  ℹ️ W3 分隔符互換：本平台 os.altsep 為 None ⇒ 不適用（⛔ 計入判）")

    bad = []
    base = ah.harvest(forms[0][1])
    st0 = sys.modules.get("streamlit")
    print(f"  W0 正規形：{forms[0][1]} ⇒ 鍵數 {len(ah._CACHE)}")
    for name, p in forms[1:]:
        got = ah.harvest(p)
        same = (got[0] is base[0]) and (got[1] is base[1])   # 回傳之 tuple 每次新建 ⇒ 逐元素比
        st_same = sys.modules.get("streamlit") is st0
        print(f"  {'✅' if (same and st_same) else '🔴'} {name}：{p} ⇒ 同一物件 {same}·"
              f"streamlit 未被換 {st_same}·鍵數 {len(ah._CACHE)}")
        if not (same and st_same):
            bad.append(name)
    n_keys = len(ah._CACHE)
    ok_keys = (n_keys == 1)
    print(f"  {'✅' if ok_keys else '🔴'} 鍵數 ＝ {n_keys}（期 1）")
    if not ok_keys:
        bad.append("鍵數")

    # 對照：位元相同之複本（另一目錄）⇒ 須非同一物件
    tmpd = tempfile.mkdtemp(prefix="wg9348_")
    try:
        cp = os.path.join(tmpd, "app.py")
        shutil.copyfile(app0, cp)
        other = ah.harvest(cp)
        _nb = other[0] is not base[0]
        diff_ok = _nb and (len(ah._CACHE) == n_keys + 1)
        print(f"  {'✅' if diff_ok else '🔴'} 對照（複本 {cp}）⇒ 非同一物件 {_nb}·"
              f"鍵數 {len(ah._CACHE)}（期 {n_keys + 1}）")
        if not diff_ok:
            bad.append("對照")
    finally:
        shutil.rmtree(tmpd, ignore_errors=True)

    print(f"⇒ 紅 {bad}；rc {1 if bad else 0}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
