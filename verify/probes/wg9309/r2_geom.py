# 發單側原型檢核（scratch）：R2 左強制帶（P2·雙線）與 P1 業主宗之逐宗重疊；首宗之頂點數
# 用法：python3 r2_geom.py cap_乙_3.5_R2.pkl p1_B_35.json
import pickle, json, sys
from shapely.geometry import Polygon
lbl, biz, fb, bp = pickle.load(open(sys.argv[1], 'rb'))
band = fb[0]
d = json.load(open(sys.argv[2]))
own = {r['暫編地號']: Polygon(r['cut_coords']) for r in d['rows'] if r['所屬街廓'] == lbl and r['推進側別'] == 'left'}
for k, p in own.items():
    print(k, round(p.area, 4), 'band∩', round(p.intersection(band).area, 4))
for k, p in own.items():
    print(k, '頂點數', len(p.exterior.coords) - 1)
print('band', round(band.area, 4))
