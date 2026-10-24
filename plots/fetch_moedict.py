# -*- coding: utf-8 -*-
"""
W-P.002 §二 0：取教育部《重編國語辭典修訂本》之 JSON（筆劃與部首之資料）。

命令列：python plots/fetch_moedict.py <目錄>
  以標準庫下載 npm 之 tarball、驗其 sha256、以 tarfile 唯取 package/dict-revised.json 一員
  寫至 <目錄>/dict-revised.json、驗其 sha256；任一不合即報錯停。
  ⛔ npm install、⛔ 執行套件內之任何程式。<目錄> ⛔ 在倉內（辭典內容之授權 CC BY-ND 3.0 TW ⇒ ⛔ 入倉）。
所據：出圖線/orders/W-P.002_歸戶號與附表26.md §一 3。
"""
import hashlib
import io
import os
import sys
import tarfile
import urllib.request

TARBALL_URL = ("https://registry.npmjs.org/@leonsilicon/moedict-data/-/"
               "moedict-data-0.202603.0.tgz")
TARBALL_BYTES = 20509261
TARBALL_SHA256 = "daf8e17ecd728bbdf4fe72ca9aa9912a01c05b34ca306a6b1cf2a6a07dcefe6d"
MEMBER = "package/dict-revised.json"
JSON_BYTES = 63298941
JSON_SHA256 = "f68fc3df140a64d8de6eb905ff6576bfd9d260eed0bbf5cc9c41aba5a131a7ad"
OUT_NAME = "dict-revised.json"

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class FetchError(RuntimeError):
    """下載或驗證不合 ⇒ 停。"""


def _inside_repo(path):
    a, r = os.path.realpath(path), os.path.realpath(REPO)
    return a == r or a.startswith(r + os.sep)


def fetch(out_dir):
    if _inside_repo(out_dir):
        raise FetchError(f"輸出之目錄在倉內（⛔）：{out_dir}")
    with urllib.request.urlopen(TARBALL_URL, timeout=300) as resp:
        raw = resp.read()
    sha = hashlib.sha256(raw).hexdigest()
    if len(raw) != TARBALL_BYTES or sha != TARBALL_SHA256:
        raise FetchError(f"tarball 不合：{len(raw)} bytes·sha256 {sha}")
    with tarfile.open(fileobj=io.BytesIO(raw), mode="r:gz") as tf:
        info = tf.getmember(MEMBER)
        if not info.isfile():
            raise FetchError(f"{MEMBER} 非一般檔")
        data = tf.extractfile(info).read()
    sha = hashlib.sha256(data).hexdigest()
    if len(data) != JSON_BYTES or sha != JSON_SHA256:
        raise FetchError(f"{MEMBER} 不合：{len(data)} bytes·sha256 {sha}")
    os.makedirs(out_dir, exist_ok=True)
    out = os.path.join(out_dir, OUT_NAME)
    with open(out, "wb") as f:
        f.write(data)
    return out, sha


def main(argv):
    if len(argv) != 1:
        print("用法：python plots/fetch_moedict.py <目錄>", file=sys.stderr)
        return 2
    out, sha = fetch(argv[0])
    print(f"輸出 {out}\t{JSON_BYTES} bytes\tsha256 {sha}")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main(sys.argv[1:]))
