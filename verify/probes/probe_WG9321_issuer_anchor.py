#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
probe_WG9321_issuer_anchor.py — 窗十五 §七-1 態錨重跑器（發單側·唯讀·零生產碼）
恆常附款 w②① 之落地：一支器、對開工態、逐格重跑、落檔。
用法：python probe_WG9321_issuer_anchor.py <repo> <outfile> [<簿末號> <前一MAX>]
🔒 恆常附款 k 之自檢（出單前以功能之名查既有器）：
   項4  四簿·自擬框 ＝ **復用** verify/probes/probe_WG9267_issuer_measurers.py（⛔ 重寫）
   項4′ 四簿·正典框 ＝ **復用** verify/probes/probe_WG9270_closegate.py（⛔ 重寫）
        本器另置一份獨立實作，其地位 ＝ **對拍造·自擬·⛔ 正典**；二器相異即先判器紅。
   查既有器之結果：verify/tools/wg99_anchor_audit.py（受詞 ＝ CLAUDE.md 行號錨·**新題**）／
        probe_WG9305_issuer_static.py（受詞 ＝ AST 節點普查·**新題**）／
        wg9268_gate5_tally.py（四簿取號·已由 -9267／-9270 二器取代）
⛔ 讀任何交接文之數；每格皆由本器當場量得。
"""
import re, sys, os, subprocess, hashlib, json, math

REPO = sys.argv[1]
OUT  = sys.argv[2]
L = []
def say(s=''):
    L.append(s); print(s)

def git(*a, text=True):
    r = subprocess.run(['git', '-C', REPO] + list(a), capture_output=True)
    return r.stdout.decode('utf-8', 'replace') if text else r.stdout

def gitrc(*a):
    r = subprocess.run(['git', '-C', REPO] + list(a), capture_output=True)
    return r.returncode

HEAD = git('rev-parse', 'HEAD').strip()
BR   = git('rev-parse', '--abbrev-ref', 'HEAD').strip()
say(f"### 開工態")
say(f"branch = {BR}")
say(f"HEAD   = {HEAD}")
say(f"HEAD ci= {git('log','-1','--format=%ci').strip()}")
say(f"HEAD s = {git('log','-1','--format=%s').strip()}")
say(f"core.quotePath = {git('config','--get','core.quotePath').strip() or '(unset/default=true)'}")
say()

# ── 項 2　保全分支 ──────────────────────────────────────────
say("### 項2 保全分支")
PRES = git('rev-parse', 'refs/remotes/origin/wip/W-G.9-318-preserve').strip()
say(f"origin/wip/W-G.9-318-preserve = {PRES}")
say(f"  is-ancestor(PRES, HEAD)  = {gitrc('merge-base','--is-ancestor',PRES,'HEAD')==0}")
say(f"  is-ancestor(HEAD, PRES)  = {gitrc('merge-base','--is-ancestor','HEAD',PRES)==0}")
for c in ['174b0be1841125b14ed31267aebd0d274915c10f',
          'c286a79cc6a699c57c7763306c4beae9ef7b60a3']:
    ok = gitrc('cat-file','-e',c+'^{commit}')==0
    anc = gitrc('merge-base','--is-ancestor',c,'HEAD')==0 if ok else None
    say(f"  {c[:12]} exists={ok} is-ancestor(.,HEAD)={anc}")
say()

# ── 項 3　生產碼 ────────────────────────────────────────────
say("### 項3 生產碼")
top = [f for f in git('ls-files','verify/*.py').split('\n') if f and f.count('/')==1]
sub = [f for f in git('ls-files','verify/**/*.py').split('\n') if f]
appblob = git('rev-parse','HEAD:app.py').strip()
say(f"verify/ 頂層 *.py = {len(top)}   (+ app.py = {len(top)+1})")
say(f"app.py blob = {appblob}")
say(f"判別力[必不命中] 子層 *.py = {len(sub)}")
say(f"  交叉檢：頂層+子層 = {len(top)+len(sub)} ; git ls-files 'verify/*.py' 全 = "
    f"{len([f for f in git('ls-files','verify/*.py').split(chr(10)) if f])}")
say()

# ── 項 5　baselines ─────────────────────────────────────────
say("### 項5 baselines")
p = subprocess.run(f"git -C {REPO} ls-tree -r HEAD verify/baselines | sha256sum",
                   shell=True, capture_output=True)
bl = git('ls-tree','-r','HEAD','verify/baselines')
say(f"sha256 = {p.stdout.decode().split()[0]}")
say(f"列數   = {len([x for x in bl.split(chr(10)) if x])}")
say()

# ── 項 6　refs ─────────────────────────────────────────────
say("### 項6 refs")
refs = [r.strip() for r in git('branch','-r').split('\n') if r.strip() and '->' not in r]
refs = [r.replace('origin/','',1) for r in refs]
buck = {'verify/':0,'wip/':0,'claude/':0,'main':0,'其他':0}
for r in refs:
    if r.startswith('verify/'): buck['verify/']+=1
    elif r.startswith('wip/'):  buck['wip/']+=1
    elif r.startswith('claude/'): buck['claude/']+=1
    elif r=='main': buck['main']+=1
    else: buck['其他']+=1
say(f"遠端分支總數（扣 HEAD 符號參照）= {len(refs)}")
say(f"  {buck}")
say()

# ── 項 7 / 4 / 4′　四簿 ─────────────────────────────────────
FILES = {
 '自誤簿': 'docs/reports/W-G.9波_claude.ai側自誤登記.md',
 '恆常附款簿': 'docs/reports/W-G.9波_恆常附款登記表.md',
 'GB簿': 'docs/reports/W-G.4_泛用阻塞項登記表.md',
 'K-6典': 'docs/rulings/K-6_街角地分配程序與可分配判準.md',
 'VR簿': 'docs/驗證裁定登記表.md',
}
say("### 項7 四簿／典之 blob·bytes·列數")
META = {}
for k, f in FILES.items():
    blob = git('rev-parse', f'HEAD:{f}').strip()
    raw  = subprocess.run(['git','-C',REPO,'cat-file','blob',blob],
                          capture_output=True).stdout
    txt  = raw.decode('utf-8')
    META[k] = dict(path=f, blob=blob, bytes=len(raw), lines=len(txt.split('\n')), txt=txt)
    say(f"{k:6s} {f}")
    say(f"       blob={blob}  bytes={len(raw)}  列={len(txt.split(chr(10)))}")
say()

# 正典框（逐字取自 VR-091 補款二 ① ／ VR-092 就地加註 ／ VR-093）
RE_ZW_DEF = re.compile(r'^#+[^0-9０-９（(\n]*?自誤[\s　`]*`?([0-9]{1,4})`?')
RE_ZW_RNG = re.compile(r'^#+[^\n]*?自誤[\s　`]*`?([0-9]{1,4})`?[\s　`]*[〜～\-–~]+[\s　`]*`?([0-9]{1,4})`?')
RE_GB_T   = re.compile(r'^\| *\*\*`?GB-([0-9]{1,4})`?\*\*')
RE_GB_A   = re.compile(r'^## `GB-([0-9]{1,4})`')
RE_GB_B   = re.compile(r'^### `GB-([0-9]{1,4})`')
RE_VR_D   = re.compile(r'^#+ `?VR-([0-9]{1,4})`?(?![0-9])')

def summ(S, name):
    S = set(S)
    lo, hi = min(S), max(S)
    miss = [i for i in range(lo, hi+1) if i not in S]
    return dict(簿=name, 相異=len(S), MIN=lo, MAX=hi, 缺號=miss)

say("### 項4′ 四簿·正典框（正典器 verify/probes/probe_WG9270_closegate.py·⛔ 本器重寫）")
_n  = sys.argv[3] if len(sys.argv) > 3 else '448'
_pm = sys.argv[4] if len(sys.argv) > 4 else '447'
_cg = subprocess.run([sys.executable, 'verify/probes/probe_WG9270_closegate.py', _n, _pm, '.'],
                     cwd=REPO, capture_output=True)
say(_cg.stdout.decode('utf-8','replace').rstrip())
say(f"  （正典器 rc={_cg.returncode}）")
say()
say("### 項4″ 對拍造（本器之獨立實作·**自擬·⛔ 正典**·僅供二器對拍）")
zw = META['自誤簿']['txt'].split('\n')
Sdef, Srng, both = set(), set(), 0
for l in zw:
    md, mr = RE_ZW_DEF.match(l), RE_ZW_RNG.match(l)
    if md: Sdef.add(int(md.group(1)))
    if mr: Srng |= set(range(int(mr.group(1)), int(mr.group(2))+1))
    if md and mr: both += 1
ZW = summ(Sdef | Srng, '自誤')
say(f"自誤  框＝VR-091 補款二①（定義框A ∪ 範圍框）·母體＝自誤簿單檔·列框")
say(f"      定義框列命中={sum(1 for l in zw if RE_ZW_DEF.match(l))} 重咬列={both} "
    f"純單筆列命中={sum(1 for l in zw if RE_ZW_DEF.match(l))-both}   (VR-091 補充 四：三數同格併載)")
say(f"      {ZW}")

gb = META['GB簿']['txt'].split('\n')
G = ({int(m.group(1)) for l in gb if (m:=RE_GB_T.match(l))}
   | {int(m.group(1)) for l in gb if (m:=RE_GB_A.match(l))}
   | {int(m.group(1)) for l in gb if (m:=RE_GB_B.match(l))}) - {997}
GB = summ(G, 'GB')
say(f"GB    框＝VR-093 三框聯集（式表∪式A∪式B·扣哨兵997）·母體＝GB簿單檔·列框")
say(f"      式表={len({int(m.group(1)) for l in gb if (m:=RE_GB_T.match(l))})} "
    f"式A={len({int(m.group(1)) for l in gb if (m:=RE_GB_A.match(l))})} "
    f"式B={len({int(m.group(1)) for l in gb if (m:=RE_GB_B.match(l))})}")
say(f"      {GB}")

vr = META['VR簿']['txt'].split('\n')
V = {int(m.group(1)) for l in vr if (m:=RE_VR_D.match(l))} - {999}
VR = summ(V, 'VR')
say(f"VR    框＝VR-092 就地加註所引定義框（扣哨兵999）·母體＝VR簿單檔·列框")
say(f"      {VR}   🩸 VR-1〜13 已鑄而框外（單四-2 登記·⛔ 視為缺號）")
say()

# ── 自擬框（倉內既有器·⛔ 正典） ────────────────────────────
say("### 項4 四簿·發單側自擬框（倉內既有器 verify/probes/probe_WG9267_issuer_measurers.py registry）")
r = subprocess.run([sys.executable, 'verify/probes/probe_WG9267_issuer_measurers.py', 'registry'],
                   cwd=REPO, capture_output=True)
say(r.stdout.decode('utf-8','replace').rstrip())
if r.returncode != 0:
    say(f"🔴 器非零退出 rc={r.returncode}  stderr={r.stderr.decode('utf-8','replace')[:400]}")
say()

# ── 項 8　母體 ─────────────────────────────────────────────
say("### 項8 母體")
import subprocess as _sp
_raw = _sp.run(['git','-C',REPO,'-c','core.quotepath=false','ls-files','-z'],
               capture_output=True).stdout.decode('utf-8')
allf = [f for f in _raw.split('\0') if f]
say(f"全倉追蹤      = {len(allf)}")
say(f".md           = {len([f for f in allf if f.endswith('.md')])}")
say(f"docs/         = {len([f for f in allf if f.startswith('docs/')])}")
say(f"verify/out/   = {len([f for f in allf if f.startswith('verify/out/')])}")
say()

# ── 項 9　恆常附款 ─────────────────────────────────────────
say("### 項9 恆常附款")
hc = META['恆常附款簿']['txt'].split('\n')
rows, ids = [], []
for l in hc:
    m = re.match(r'^\| *`([a-z]{1,2})` *\|', l)
    if m:
        rows.append(l); ids.append(m.group(1))
say(f"表列式款列命中 = {len(rows)}  相異款號 = {len(set(ids))}")
say(f"款號 = {sorted(set(ids), key=lambda s:(len(s),s))}")
withsrc = [l for l in rows if re.search(r'\.md[:：]\d+', l)]
say(f"其列含索引形『檔:列』者 = {len(withsrc)} / {len(rows)}")
say(f"相異款號數 = {len(set(ids))}  缺 = {[c for c in 'abcdefghijklmnopqrstuvwxyz' if c not in ids]}")
say(f"（列命中 {len(rows)} > 相異 {len(set(ids))} 之因 ＝ §三 逐字條文表二度列舉 a–i·⛔ 重複登記）")
say()

# ── 項 10　取號現查 ────────────────────────────────────────
say("### 項10 W-G.9 取號現查（全倉·含檔名與內文）")
maxn = 0
occ = {}
for f in allf:
    for m in re.finditer(r'W-G\.9-(\d{1,4})', f):
        n = int(m.group(1)); occ.setdefault(n, set()).add(f); maxn = max(maxn, n)
say(f"檔名側 MAX = {maxn}")
for n in (318, 319, 320, 321, 322, 309):
    fs = occ.get(n, set())
    say(f"  W-G.9-{n}: 檔名側命中檔數={len(fs)}")
grep = subprocess.run(
    "git -C %s grep -h -o -E 'W-G\\.9-[0-9]{1,4}' HEAD -- '*.md' | sed 's/.*-//' | sort -n | uniq -c | tail -12" % REPO,
    shell=True, capture_output=True).stdout.decode()
say("內文側 W-G.9-N 之高號尾段（count number）：")
say(grep.rstrip())
say()

# ── 項 11　角 ─────────────────────────────────────────────
say("### 項11 角：三源之逐字取值與同量級檢（⛔ 採信交接文）")
srcs = [
 ("GB-171 (GB簿:8347)", "|cos|", 0.9988785831, 'acos'),
 ("GB-170 (GB簿:7767/:8348)", "|cos|", 0.04734528804692001, 'asin'),
 ("K-9-5-8 (K-6典:1000 R4 left)", "|cross(SIDE,ALLOC_cad)|", 0.0473452131, 'asin'),
]
for nm, lab, v, op in srcs:
    ang = math.degrees(math.acos(v) if op=='acos' else math.asin(v))
    say(f"  {nm:32s} 標名={lab:24s} 值={v!r:22s} {op}→{ang:.7f}°")
A, B, C = srcs[0][2], srcs[1][2], srcs[2][2]
say(f"  畢氏檢 A²+B² = {A*A+B*B:.12f}  |1−·| = {abs(1-(A*A+B*B)):.3e}  ⇒ A,B 係同一角之 cos／sin 二形")
say(f"  畢氏檢 A²+C² = {A*A+C*C:.12f}  |1−·| = {abs(1-(A*A+C*C)):.3e}")
say(f"  B−C = {B-C:.6e}  ⇒ Δ角 = {abs(math.degrees(math.asin(B))-math.degrees(math.asin(C))):.3e}°")
say(f"  三數之角量全距 = {max(math.degrees(math.acos(A)),math.degrees(math.asin(B)),math.degrees(math.asin(C)))-min(math.degrees(math.acos(A)),math.degrees(math.asin(B)),math.degrees(math.asin(C))):.3e}°")
say("  🛑 判：三數歸於同一角量（2.7137°）係算術所得；『三者同源』之受詞係<u>幾何造之等同</u>，")
say("     ⛔ 由算術得 ⇒ 依 u⑥／u⑦ 標【未證】。且 GB簿 標 B 為『|cos|』與 K-6典 標 C 為『|cross|』⛔ 可同時為真。")
say()
say(f"### 落檔簽")
body = '\n'.join(L)
say("")
open(OUT, 'w', encoding='utf-8').write(
    f"# 窗十五 §七-1 態錨重跑落檔\n# 器 = probe_WG9321_issuer_anchor.py\n# 開工態 = {HEAD}\n\n" + body + "\n")
print(f"\n[落檔] {OUT}  sha256={hashlib.sha256(open(OUT,'rb').read()).hexdigest()}")
