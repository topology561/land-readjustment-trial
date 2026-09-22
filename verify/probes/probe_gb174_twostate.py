# -*- coding: utf-8 -*-
r"""發單側量測器（窗二十四·唯讀·⛔ 零生產碼）：GB-174 之二態對拍。

用法：python probe_gb174_twostate.py <repo 絕對路徑> <出艙 json 絕對路徑>
態甲（現行）：`verify.wd4_tier_list.compute(fixture=False)` 原樣。
態乙（擬）  ：同上，惟 `run_step_g` 之回傳 `g_rows` 追加「本情境 K917_DROPPED 所記之不配地宗」，
             其 `G(㎡)` ＝ 剔除時所記之 G（原位置試配之值），`a 面積(㎡)` ＝ 該宗之 a，
             `畸零地旗標` ＝「不配地」（⛔ 使其被判為逐宗達標）。
🔒 `K917_DROPPED` 為 app 模組層之 dict、跨情境累加 ⇒ 本器於每次 `run_step_g` 前後取差、⛔ 清之以外改動。
🔒 金額與梯次一律由 `compute` 本身算（⛔ 本器另寫一份公式）。
"""
import copy, json, os, sys
REPO, OUT = sys.argv[1], sys.argv[2]
os.chdir(REPO)
sys.path.insert(0, os.path.join(REPO, "verify"))
sys.stdout.reconfigure(encoding="utf-8")
import wd4_tier_list as wd4  # noqa: E402

_orig = wd4.run_step_g
CAP = {"mode": None, "calls": []}


def _a_of(tp):
    # 🔒 逐字複刻 `verify/stepg_pipeline.py` 之 `_build_g_row` 取 a 之式（⛔ 另立口徑）
    if not tp:
        return None, None
    if '分攤登記面積_m2' in tp:
        return "分攤+面積", round(float(tp.get('分攤登記面積_m2', 0) or 0)
                                 + float(tp.get('面積_m2', 0) or 0), 2)
    if '面積_m2' in tp:
        return "面積_m2", round(float(tp.get('面積_m2', 0) or 0), 2)
    return None, None


def wrapped(ns, fake_st, cb, cad, snapshot, param_rows, build_parcels, winners_state,
            forced_map, setback, *a, **kw):
    before = {k: len(v) for k, v in ns["K917_DROPPED"].items()}
    sg = _orig(ns, fake_st, cb, cad, snapshot, param_rows, build_parcels, winners_state,
               forced_map, setback, *a, **kw)
    new = []
    for k, v in ns["K917_DROPPED"].items():
        for rec in v[before.get(k, 0):]:
            new.append({"街廓": k[0], "側": k[1], **rec})
    # 🩸 實測：同一宗於一次 `run_step_g` 內被記 `2` 次（多階段）⇒ 以暫編地號去重，並斷言重複者逐欄相同
    _uniq = {}
    for d in new:
        k = (d["街廓"], d["側"], d["暫編地號"])
        if k in _uniq and _uniq[k] != d:
            raise RuntimeError("🔴 同宗二記而內容相異：%r / %r" % (_uniq[k], d))
        _uniq[k] = d
    CAP.setdefault("dup", []).append((setback, len(new), len(_uniq)))
    new = list(_uniq.values())
    by_pid = {tp.get("暫編地號"): tp for tp in build_parcels}
    rows = sg["g_rows"]
    tmpl_keys = sorted(rows[0].keys()) if rows else []
    info = []
    for d in new:
        tp = by_pid.get(d["暫編地號"], {})
        ak, av = _a_of(tp)
        info.append({**d, "原地號": tp.get("原地號"), "a_key": ak, "a": av,
                     "tp_keys": sorted(tp.keys())})
    CAP["calls"].append({"mode": CAP["mode"], "setback": setback, "dropped": info,
                         "g_row_keys": tmpl_keys, "n_g_rows": len(rows)})
    if CAP["mode"] == "乙":
        sg = dict(sg)
        aug = list(rows)
        for d in info:
            if d["a"] is None or d["原地號"] is None:
                raise RuntimeError("🔴 不配地宗之 a／原地號 缺：%r" % (d,))
            aug.append({"暫編地號": d["暫編地號"], "原地號": d["原地號"], "所屬街廓": d["街廓"],
                        "推進側別": d["側"], "G(㎡)": d["G(㎡)"], "a 面積(㎡)": d["a"],
                        "畸零地旗標": "不配地"})
        sg["g_rows"] = aug
    return sg


wd4.run_step_g = wrapped
res = {}
for mode in ("甲", "乙"):
    CAP["mode"] = mode
    out = wd4.compute(fixture=False)
    res[mode] = {tag: out[tag]["groups"] for tag in out}
    json.dump({"calls": CAP["calls"], "dup": CAP.get("dup"), "groups": res}, open(OUT, "w", encoding="utf-8"),
              ensure_ascii=False, indent=1, default=str)
    print("mode", mode, "done", flush=True)
json.dump({"calls": CAP["calls"], "dup": CAP.get("dup"), "groups": res}, open(OUT, "w", encoding="utf-8"),
          ensure_ascii=False, indent=1, default=str)
print("done")
