import json,sys
A,B=sys.argv[1],sys.argv[2]
def key(r): return (r["所屬街廓"],r["推進側別"],r["暫編地號"])
for n in ["A_0","A_35","B_0","B_35"]:
    a=json.load(open(f"{A}_{n}.json")); b=json.load(open(f"{B}_{n}.json"))
    ra={key(r):r for r in a["rows"]}; rb={key(r):r for r in b["rows"]}
    print(f"== {n}  rows {len(ra)}→{len(rb)}  cbs {[round(x['buf'],6) for x in a['cbs']]}→{[round(x['buf'],6) for x in b['cbs']]}  slot-b {[ (s['blk'],round(s['bL'],4)) for s in a['slot'] if s['bL']]}→{[ (s['blk'],round(s['bL'],4)) for s in b['slot'] if s['bL']]}  k {[s['k'] for s in a['slot']]}→{[s['k'] for s in b['slot']]}")
    only_a=sorted(set(ra)-set(rb)); only_b=sorted(set(rb)-set(ra))
    if only_a: print("   只在前:",only_a)
    if only_b: print("   只在後:",[(k, rb[k]["G(㎡)"]) for k in only_b])
    ch=0
    for k in sorted(set(ra)&set(rb)):
        x,y=ra[k],rb[k]
        d={f:(x[f],y[f]) for f in ["G(㎡)","S(m)","W(m)","Rw(%)","負擔比率","累積S(m)"] if str(x[f])!=str(y[f])}
        cc = x.get("cut_coords")!=y.get("cut_coords")
        if d or cc:
            ch+=1; print("   ",k,d, "幾何變" if cc else "")
    print(f"   變動宗數 {ch}／共同 {len(set(ra)&set(rb))}")
