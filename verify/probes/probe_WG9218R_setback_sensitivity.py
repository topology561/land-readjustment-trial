# -*- coding: utf-8 -*-
r"""**`W-G.9-218R` `工項五`**：**側別對退縮之敏感度**（🛑 唯讀·⛔ 零生產碼·⛔ 改任何狀態）

## 本探針要回答的唯一問題

> **同時跨占同街廓左右兩街角之宗地（`K-9-24` 之 `M`），其<u>歸側</u>是否隨「退縮」而變？**

## 受詞之取得（🔒 全部資料驅動·⛔ 硬寫）

| 受詞 | 取得法 | ⛔ |
|---|---|---|
| 退縮之二值 | **以 `ast` 自 `verify/run_verification.py` 之 `for setback, tag in (…)` 字面取出** | ⛔ 探針內另寫常數 |
| `M` 之識別 | 自 `ss['f3_k6b_dual_side_assign']`（生產碼之出艙鍵）取 | ⛔ 硬寫地號 |
| 街廓／側別 | 自出艙列之欄取（`p1_end`／`p2_end` 幾何端） | ⛔ 硬寫街廓名／「左」「右」字面 |
| 對照組 | **資料驅動**：非 `M` 之候選中，同側指數差最大之街廓側 | ⛔ 人工指定地號 |

## 路徑同一性（`GB-123` 之射程）

退縮值**經 `selection_pipeline.run_corner_pk(…, setback)`** 帶入，該函式於 `:289` 逐字
`ss["f3L_setback_default"] = setback` —— 即 `app.py:12677` 所讀之**同一 session 鍵**。
⇒ 探針與 UI 走**同一取值路徑**；⛔ 於探針內另設常數。

## ⛔ 本檔不做

⛔ 改生產碼一字；⛔ 寫任何檔（純 stdout）；⛔ 觸基線；⛔ 判斷域邊界（僅出艙）。
"""
import ast
import contextlib
import io
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)          # 🔒 自 `__file__` 推得·⛔ 寫死絕對路徑
sys.path.insert(0, VERIFY)
os.chdir(REPO)


def setbacks_from_production():
    """🔒 自 `verify/run_verification.py` 之字面取退縮二值（⛔ 探針內另寫常數）。"""
    src = open(os.path.join(VERIFY, "run_verification.py"), encoding="utf-8").read()
    tree = ast.parse(src)
    out = []
    for node in ast.walk(tree):
        if isinstance(node, ast.For) and isinstance(node.iter, (ast.Tuple, ast.List)):
            try:
                v = ast.literal_eval(node.iter)
            except Exception:
                continue
            if (isinstance(v, (tuple, list)) and v
                    and all(isinstance(x, (tuple, list)) and len(x) == 2
                            and isinstance(x[0], float) and isinstance(x[1], str) for x in v)):
                out.append((node.lineno, tuple(v)))
    if not out:
        raise RuntimeError("🔴 取不到退縮之字面（`for setback, tag in (…)`）⇒ 停；⛔ 靜默兜底")
    vals = {v for _, v in out}
    if len(vals) != 1:
        raise RuntimeError("🔴 退縮字面於多處而不一致：%r ⇒ 停" % (out,))
    return out, out[0][1]


def run_one(setback):
    """跑一次完整之街角選位管線，回傳所需之全部素材。"""
    from app_harvest import harvest
    import run_verification as rv
    from selection_pipeline import build_ownership, build_build_parcels, run_corner_pk

    ns, fake_st = harvest()
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        snapshot = rv.load_snapshot()
        cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
        build_ownership(ns, fake_st, rv.ANON_XLSX)
        with open(rv.V6DXF, "rb") as f:
            v6 = f.read()
        temp_p, build_p, _ = build_build_parcels(ns, fake_st, v6, list(cb_by.values()), snapshot)
        params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
        diag, sel, off, wins, forced = run_corner_pk(
            ns, fake_st, list(cb_by.values()), cad, params, temp_p, build_p, setback,
            snapshot=snapshot)
    ss = fake_st.session_state
    # 🔒 路徑同一性之機械證：管線確已把該值寫入 UI 鍵
    got = ss.get("f3L_setback_default")
    if got is None:
        raise RuntimeError("🔴 `f3L_setback_default` 未被管線寫入 ⇒ 路徑非同一 ⇒ 停（繫 GB-123）")
    if float(got) != float(setback):
        raise RuntimeError("🔴 UI 鍵之值 %r ≠ 帶入值 %r ⇒ 路徑非同一 ⇒ 停" % (got, setback))
    return {"ns": ns, "ss": ss, "diag": diag, "sel": sel, "off": off,
            "wins": wins, "forced": forced, "noise": len(buf.getvalue()),
            "step0": ss.get("f3_k6_step0_diag"), "dual": ss.get("f3_k6b_dual_side_assign"),
            "locks": ss.get("f3_k6b_stage1_locks"), "stage2": ss.get("f3_k6b_stage2_order"),
            "ranges": ss.get("f3_corner_range_areas")}


def f(x, nd=None):
    """全精度輸出（⛔ 四捨五入、⛔ 截位）。"""
    if x is None:
        return "—"
    if isinstance(x, float):
        return repr(x)
    return str(x)


def main():
    src, SB = setbacks_from_production()
    print("=" * 116)
    print("【`工項五`】側別對退縮之敏感度　🛑 唯讀·⛔ 零生產碼")
    print("=" * 116)
    print("🔒 退縮二值之來源（**⛔ 探針內常數**）：")
    for ln, v in src:
        print("   verify/run_verification.py:%-5d 字面 = %r" % (ln, v))
    print("   ⇒ 採用 = %r（二處同值·已機械確認）" % (SB,))
    print()

    R = {}
    for sb, tag in SB:
        print("── 跑 退縮 = %s（tag `%s`） ──" % (f(sb), tag))
        R[tag] = run_one(sb)
        R[tag]["sb"] = sb
        print("   ✅ 完成／app 側噪音 %d 字元（已隔離）／🔒 UI 鍵 `f3L_setback_default` ＝ %r（＝ 帶入值）"
              % (R[tag]["noise"], R[tag]["ss"].get("f3L_setback_default")))
    print()

    # ═══════════ M 之識別（資料驅動） ═══════════
    print("=" * 116)
    print("【M 之識別】自 `ss['f3_k6b_dual_side_assign']`（生產碼出艙鍵）·⛔ 硬寫地號")
    for tag in R:
        d = R[tag]["dual"] or []
        print("   退縮 `%s`：跨占雙街角之宗 ＝ **%d** 宗 ⇒ %s"
              % (tag, len(d), [(r["街廓"], r["M之暫編地號"]) for r in d] or "無"))
    tags = list(R)
    dual_ids = {tag: {(r["街廓"], r["M之暫編地號"]) for r in (R[tag]["dual"] or [])} for tag in tags}
    same_M = (len(set(map(frozenset, dual_ids.values()))) == 1)
    print("   🔒 二情境之 `M` 集合相同 = **%s**%s"
          % (same_M, "" if same_M else "  🔴 **停機款 ④**（跨角情形隨退縮而變）"))
    print()

    # ═══════════ a–d ═══════════
    print("=" * 116)
    print("【a–d】逐情境之全值（🔒 `G` 與指數**全精度**·⛔ 四捨五入、⛔ 截位）")
    for tag in tags:
        r = R[tag]
        print()
        print("── 退縮 `%s`（值 %s） ──" % (tag, f(r["sb"])))
        st0 = r["step0"] or {}
        print("  【a】步驟 0 之合併（自 `f3_k6_step0_diag`）")
        print("      groups_merged=%s／parcels_absorbed=%s／parcels_in=%s／parcels_out=%s"
              % (st0.get("groups_merged"), st0.get("parcels_absorbed"),
                 st0.get("parcels_in"), st0.get("parcels_out")))
        for m in (st0.get("merged") or []):
            print("      ・街廓 %s｜命名 %s｜成員 %s｜gid %s｜Σ幾何面積 %s ㎡｜聯集 %s"
                  % (m.get("街廓"), m.get("命名"), m.get("成員"), m.get("gid"),
                     f(m.get("Σ幾何面積_m2")), m.get("聯集 geom_type")))
        for row in (r["dual"] or []):
            print("  【b–d】`M` ＝ %s（街廓 %s·跨占 %s）"
                  % (row["M之暫編地號"], row["街廓"], row["跨占之街角"]))
            for s in ("p1_end", "p2_end"):
                print("      %-7s 真G＝%-22s 門檻＝%-14s 達標＝%-6s 指數＝%-22s winner＝%-3s 拿得下＝%s"
                      % (s, f(row.get("%s.真G(㎡)" % s)), f(row.get("%s.門檻(㎡)" % s)),
                         row.get("%s.達標" % s), f(row.get("%s.指數" % s)),
                         row.get("%s.winner" % s) or "—", row.get("%s.拿得下" % s) or "—"))
            print("      ⇒ **依據款次 %s ／ 歸側結果 ＝ %s**" % (row["依據款次"], row["歸側結果"]))
            print("      ⇒ 另一側之後果 ＝ %s ／【e】強制抵費地範圍面積 ＝ **%s** ㎡"
                  % (row["另一側之後果"], f(row.get("另一側.強制抵費地範圍面積(㎡)"))))
        print("  【c】同側全部候選之指數併列（全精度·母體 ＝ 該側 `diag` 全列）")
        by = {}
        for d in r["diag"]:
            by.setdefault((d["街廓"], d["端"]), []).append(d)
        for k in sorted(by):
            g = sorted(by[k], key=lambda x: (-float(x["總分"]), str(x["候選地號"])))
            print("      %s／%s（%d 候選）：" % (k[0], k[1], len(g)))
            for x in g:
                print("         %-14s 總分＝%-22s 名次＝%-4s 達標＝%-6s 選中＝%-3s 真G＝%s"
                      % (x["候選地號"], f(x["總分"]), x.get("指數名次"), x["達標"],
                         x["選中"] or "—", f(x.get("真G(㎡)"))))
        print("  【e】強制抵費地（自 `off`·全列）")
        for o in (r["off"] or []):
            print("      %r" % (o,))
        print("  【e】該街廓側之街角規定範圍面積（`f3_corner_range_areas`·全精度）")
        for blk, v in sorted((r["ranges"] or {}).items()):
            print("      %-4s %r" % (blk, v))

    # ═══════════ 敏感度判 ═══════════
    print()
    print("=" * 116)
    print("【敏感度判】**側別是否隨退縮值而變？**")
    side = {}
    for tag in tags:
        side[tag] = {(x["街廓"], x["M之暫編地號"]): x["歸側結果"] for x in (R[tag]["dual"] or [])}
    keys = sorted(set().union(*[set(v) for v in side.values()])) if side else []
    print("  | `M` | " + " | ".join("退縮 `%s`" % t for t in tags) + " | 判 |")
    print("  |---|" + "---|" * (len(tags) + 1))
    allsame = True
    for k in keys:
        vs = [side[t].get(k, "（無此宗）") for t in tags]
        same = len(set(vs)) == 1
        allsame = allsame and same
        print("  | %s／%s | %s | %s |" % (k[0], k[1], " | ".join(vs), "**同**" if same else "🔴 **異**"))
    print()
    if allsame and keys:
        print("  ⇒ 🟢 **側別<u>不</u>隨退縮值而變**（二情境之勝側逐宗相同）")
        print("     ⇒ 主線既落之歸屬於**二情境下皆成立**。")
    elif not keys:
        print("  ⇒ ⚠️ 本案無跨占雙街角之宗 ⇒ 本判**無受詞**。")
    else:
        print("  ⇒ 🛑 **停機**：側別隨退縮而變 ⇒ 真域邊界，須以 KL 格式上呈。")

    # ═══════════ 對照組（資料驅動） ═══════════
    print()
    print("=" * 116)
    print("【對照組】🔒 **資料驅動選定**（⛔ 人工指定地號）：非 `M` 之候選中，**同側指數差最大**之街廓側")
    base = tags[0]
    dm = {p for _, p in dual_ids[base]}
    cand = {}
    for d in R[base]["diag"]:
        if d["候選地號"] in dm:
            continue
        cand.setdefault((d["街廓"], d["端"]), []).append(d)
    scored = []
    for k, g in cand.items():
        if len(g) < 2:
            continue
        v = sorted((float(x["總分"]) for x in g), reverse=True)
        scored.append((v[0] - v[1], k))
    if not scored:
        print("   ⚠️ 無「同側 ≥2 候選且不含 `M`」之街廓側 ⇒ 對照組**無受詞**（具名·⛔ 略過）")
    else:
        scored.sort(reverse=True)
        gap, kk = scored[0]
        print("   選定 ＝ **%s／%s**（同側指數差 ＝ **%s**·全部候選側之最大者·母體 %d 側）"
              % (kk[0], kk[1], f(gap), len(scored)))
        print("   ── 二情境並列 ──")
        for tag in tags:
            g = [d for d in R[tag]["diag"] if (d["街廓"], d["端"]) == kk]
            g = sorted(g, key=lambda x: (-float(x["總分"]), str(x["候選地號"])))
            w = [x["候選地號"] for x in g if x["選中"]]
            print("      退縮 `%-4s` winner ＝ %-14s ｜ 候選 %d：" % (tag, (w[0] if w else "（無）"), len(g)))
            for x in g:
                print("            %-14s 總分＝%-22s 名次＝%-4s 達標＝%-6s 真G＝%s"
                      % (x["候選地號"], f(x["總分"]), x.get("指數名次"), x["達標"], f(x.get("真G(㎡)"))))
        ws = []
        for tag in tags:
            g = [d for d in R[tag]["diag"] if (d["街廓"], d["端"]) == kk and d["選中"]]
            ws.append(g[0]["候選地號"] if g else None)
        print("   ⇒ 二情境之 winner %s ⇒ %s"
              % ("相同" if len(set(ws)) == 1 else "**相異**",
                 "✅ 對照組亦不敏感" if len(set(ws)) == 1 else "🟡 對照組敏感（具名）"))

    # ═══════════ f：藍影 ═══════════
    print()
    print("=" * 116)
    print("【f】藍影線（`K-9-23`）之可及性")
    ns0 = R[tags[0]]["ns"]
    have = "_blue_shadow_tri" in ns0
    print("   `_blue_shadow_tri` 於 harvest 之 ns 內 = **%s**" % have)
    print("   🛑 其於生產碼係**觀測模式**（`app.py` 逐字「本區塊之一切輸出**只寫入診斷**」／")
    print("      「**只印**，⛔ 無回傳值被消費、⛔ 不改任何狀態」）⇒ **⛔ 有任何 session 出艙鍵**。")
    keys_bs = [k for k in R[tags[0]]["ss"] if "blue" in str(k).lower() or "藍影" in str(k)]
    print("   session 內與藍影相關之鍵 = %r ⇒ **%d** 個" % (keys_bs, len(keys_bs)))
    print("   ⇒ 🔴 **`f` 於本探針之路徑上⛔ 可及**——其構成幾何**⛔ 經由 `run_corner_pk` 出艙**；")
    print("      欲取之須另呼叫 `_blue_shadow_tri` 並自備其六參數，**⛔ 屬同一路徑** ⇒ 依單具名回報、⛔ 代擬。")

    print()
    print("=" * 116)
    print("🔒 探針自陳：⛔ 改任何檔·⛔ 觸基線·純 stdout。")


if __name__ == "__main__":
    main()
