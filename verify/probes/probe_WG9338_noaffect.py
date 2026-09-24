# 「不影響原位次」檢核之原型（發單側·倉外）：K-9-48 其三之定義·二項
#  （甲）併入前可原位次配得之宗（驗_總判＝保留），併入後仍保留；
#  （乙）併入後，街廓之配餘地（調配池）仍容納內接矩形。
# 輸入 ＝ 二份物化器落檔（併入前／併入後）；受檢街廓 ＝ 二者之被併入宗所在街廓（由參數給）。
import json, sys
pre = json.load(open(sys.argv[1], encoding='utf-8')); post = json.load(open(sys.argv[2], encoding='utf-8')); BLKS = sys.argv[3].split(',')
def kept(d, b): return {r['暫編地號'] for r in d['rows'] if r['所屬街廓'] == b and r.get('驗_總判') == '保留'}
def pools(d, b): return [p for p in d['pools'] if p['池'].startswith(b + '-')]
for b in BLKS:
    k0, k1 = kept(pre, b), kept(post, b)
    lost = sorted(k0 - k1)
    p1 = pools(post, b)
    main = max(p1, key=lambda p: p['面積']) if p1 else None
    print(f'== {b}  （甲）併入前保留 {len(k0)}／併入後保留 {len(k1)}／失去 {lost} ⇒ {"✅" if not lost else "🔴"}')
    for p in p1: print(f'     池 {p["池"]:<14} {p["面積"]:>9}  容納內接矩形 {p["容納內接矩形"]}')
    print(f'     （乙）最大池 {main["池"] if main else None} 容納 {main["容納內接矩形"] if main else None}；全部池皆容納 {all(p["容納內接矩形"] for p in p1)}')
print('err', pre['err'], post['err'])
