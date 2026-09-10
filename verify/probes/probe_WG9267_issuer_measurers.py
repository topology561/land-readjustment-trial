#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
probe_WG9267_issuer_measurers.py — 發單側（claude.ai）之三套自擬量測器·原封入倉（自誤 331 之落地）

🔒 地位：此係發單側於 W-G.9-263〜-267 各輪出艙之數所用之器·**自擬框·⛔ 正典**。
   入倉之唯一目的 ＝ 使 CC 於「發單側之數 vs CC 實測」相異時**可歸因**（框之別／母體之別／態之別／器之瑕）。
   ⛔ 以本器之輸出為任何閘之通過條件；正典框見 VR-091 補款二 ①／VR-092／VR-093／宣告框 ①–⑦ 及其補款。
🔒 唯讀。⛔ 寫入任何 tracked 檔。不 import 生產路徑。
用法：python verify/probes/probe_WG9267_issuer_measurers.py [registry|occupancy N [N...]|coverage]
"""
import re, sys, subprocess, itertools, hashlib

def _ls(prefix):
    out = subprocess.run(['git', '-c', 'core.quotepath=false', 'ls-files', '-z', '--', prefix],
                         capture_output=True).stdout.decode('utf-8', 'replace')
    return [f for f in out.split('\0') if f]

def _read(f):
    try:
        return open(f, encoding='utf-8').read().split('\n')
    except Exception:
        return None

# ───────────── 一　三簿＋K-9 計數（發單側自擬框·於 -262 復現輪所用之最終版·四版調校之末版）─────────────
RE_ZW_RNG = re.compile(r'^#{1,6} [^\w`]{0,6}`?自誤 `?(\d+)`?〜`?(\d+)`?|登記：自誤 `?(\d+)`?〜`?(\d+)`?')
RE_ZW_BAT = re.compile(r'登記：自誤 `?(\d+)`?（')
RE_ZW_DEF = re.compile(r'^#{1,6} [^\w`]{0,6}`?自誤 `?(\d+)`?`?\s*[｜（　:：]')
RE_GB_F1  = re.compile(r'^#{2,4} [^\w`]{0,8}`?GB-(\d{1,3})`?(?![0-9])')
RE_GB_F2  = re.compile(r'^\| *\*\*`?GB-(\d{1,3})`?\*\*')
RE_GB_F3  = re.compile(r'^#{1,6} .*?`?GB-(\d{1,3})`?(?![0-9])')
RE_VR     = re.compile(r'^#{1,6} `?VR-(\d{1,3})`?(?![0-9])')
RE_K9_H   = re.compile(r'^#{2,4} ')
RE_K9     = re.compile(r'`?K-9-(\d{1,2})`?(?![0-9])')

def _summ(S, sentinel=None):
    S = set(S) - ({sentinel} if sentinel else set())
    if not S: return dict(相異=0, MAX=None, MIN=None, 缺號=[])
    lo, hi = min(S), max(S)
    return dict(相異=len(S), MAX=hi, MIN=lo, 缺號=[i for i in range(lo, hi+1) if i not in S])

def registry():
    zw = _read('docs/reports/W-G.9波_claude.ai側自誤登記.md') or []
    s, e = set(), set()
    for l in zw:
        if not (re.match(r'^#{1,6} ', l) and '自誤' in l): continue
        m = RE_ZW_RNG.search(l)
        if m:
            g = [x for x in m.groups() if x]; e |= set(range(int(g[0]), int(g[1])+1)); continue
        m = RE_ZW_BAT.search(l)
        if m: s.add(int(m.group(1))); continue
        m = RE_ZW_DEF.match(l)
        if m: s.add(int(m.group(1)))
    gb = _read('docs/reports/W-G.4_泛用阻塞項登記表.md') or []
    U = ({int(m.group(1)) for l in gb if (m := RE_GB_F1.match(l))}
         | {int(m.group(1)) for l in gb if (m := RE_GB_F2.match(l))}
         | {int(m.group(1)) for l in gb if (m := RE_GB_F3.match(l))})
    vr = _read('docs/驗證裁定登記表.md') or []
    V = {int(m.group(1)) for l in vr if (m := RE_VR.match(l))}
    k6 = _read('docs/rulings/K-6_街角地分配程序與可分配判準.md') or []
    K = {int(m.group(1)) for l in k6 if RE_K9_H.match(l) for m in RE_K9.finditer(l)}
    print("【發單側自擬框·單檔母體·缺號 [MIN..MAX]】")
    print("  自誤 :", _summ(s | e))
    print("  GB   :", _summ(U, 997), "  （997 在聯集內？", 997 in U, "⇒ 扣哨兵為空操作：", 997 not in U, "）")
    print("  VR   :", _summ(V, 999), "  （999 在定義框內？", 999 in V, "）")
    print("  K-9  :", _summ(K))

# ───────────── 二　宣告框六數（D1／D2／D3·補款⑤·二 D3 框並列）─────────────
def occupancy(nums):
    files = _ls('docs/')
    unread = 0
    for n in nums:
        tok = f'W-G.9-{n}'; pat = re.compile(re.escape(tok) + r'(?![0-9])')
        D1 = {f for f in files if pat.search(f)}
        for mode in ('嚴格式(列首即該號·⛔ 前導標記)', '寬式(允前導 `·空白)'):
            D2, D3 = set(), set(); unread = 0
            for f in files:
                L = _read(f)
                if L is None: unread += 1; continue
                fn = bool(pat.search(f.split('/')[-1]))
                for i, l in enumerate(L, 1):
                    if not pat.search(l): continue
                    if re.match(r'^#+', l): D2.add((f, i))
                    head = l.startswith(tok) if mode.startswith('嚴') else bool(re.match(r'^\s*`?' + re.escape(tok), l))
                    if head or ('本單' in l and fn): D3.add((f, i))
            lf = len(D2 | D3); ff = len(D1 | {f for f, _ in D2} | {f for f, _ in D3})
            print(f"  {tok} [{mode}] D1 {len(D1)}／D2 {len(D2)}／D3 {len(D3)}／雙屬 {len(D2 & D3)}／列框 {lf}／檔框 {ff}")
    print(f"  母體 全 docs/ {len(files)} 檔·讀不到 {unread}")

# ───────────── 三　覆蓋帳（軸自由面積交集·13 組）─────────────
def coverage():
    import ast, pandas as pd
    from shapely.geometry import Polygon
    for tag in ('0m', '3.5m'):
        p = f'verify/out/got_G值_退縮{tag}_partial.csv'
        try: d = pd.read_csv(p)
        except Exception as ex: print("  落檔不可讀：", p, ex); continue
        for (blk, side), sub in d.groupby(['所屬街廓', '推進側別'], sort=False):
            if side == '抵費地': continue
            P = {}
            for _, r in sub.iterrows():
                cc = r['cut_coords']
                if not isinstance(cc, str) or not cc.strip(): continue
                pts = ast.literal_eval(cc)
                if len(pts) < 3: continue
                g = Polygon(pts); g = g if g.is_valid else g.buffer(0)
                P[r['暫編地號']] = (g, r['驗_宗序'], r['W(m)'])
            tot = 0.0; pairs = []
            for a, b in itertools.combinations(P, 2):
                ov = P[a][0].intersection(P[b][0]).area
                if ov > 1e-6: tot += ov; pairs.append((a, b, ov))
            corner = [k for k, v in P.items() if v[1] == '街角第1宗']
            dw = ''
            if corner:
                wc = P[corner[0]][2]; o = sorted(v[2] for k, v in P.items() if k != corner[0])
                dw = f"ΔW={o[0]-wc:+.2f}" if o else "次宗:無"
            print(f"  {tag:5s} {blk} {side:5s} 宗數{len(P):2d} 重疊合計 {tot:9.4f} {dw}  " + ("；".join(f"{a}×{b}={v:.4f}" for a, b, v in pairs)))
    # 判別力對照
    A = Polygon([(0,0),(2,0),(2,1),(0,1)]); B = Polygon([(1,0),(3,0),(3,1),(1,1)]); C = Polygon([(5,0),(6,0),(6,1),(5,1)])
    print("  對照：人造相疊 Σ−∪ =", round(A.area + B.area - A.union(B).area, 6), "（須 1.0）／人造相離 =", round(A.area + C.area - A.union(C).area, 6), "（須 0.0）")

if __name__ == '__main__':
    a = sys.argv[1:] or ['registry']
    if a[0] == 'registry': registry()
    elif a[0] == 'occupancy': occupancy([int(x) for x in a[1:]] or [267])
    elif a[0] == 'coverage': coverage()
    else: print(__doc__)
