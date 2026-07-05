# -*- coding: utf-8 -*-
"""
W-V 驗證熔爐 — module-harvest（shim 路線，additive-only）。

目的：headless 取得 app.py 的**真函式**（非複本），不執行其模組級 UI script。
做法：
  1. AST 解析 app.py；只保留 top-level `import` / `def` / `class` / 常數 Assign，
     跳過模組級 UI 語句（`st.set_page_config`、`st.tabs(...)`、button-if、for/with…）。
  2. 把 fake `streamlit` 注入 `sys.modules['streamlit']`（session_state=可控 dict、
     其餘 st.* 為 no-op、cache_data 為 passthrough decorator）。
  3. compile 過濾後模組 + exec 進獨立命名空間 → 得真函式活命名空間。

app.py 一字不改（本檔在 runtime 讀其原始碼、過濾、exec）。
`_pk_one_side_v12` 之 golden（手冊圖8 0.6685/0.3315）在此 harvest 命名空間下仍成立，
即證 harvest 出的是與 tests/test_corner_priority_golden.py 同一份真函式。
"""
import ast
import os
import sys

APP_PY = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "app.py")


# ---------------- fake streamlit ----------------
class _SessionState(dict):
    """dict + 屬性存取（模擬 st.session_state）。"""
    def __getattr__(self, k):
        try:
            return self[k]
        except KeyError as e:
            raise AttributeError(k) from e

    def __setattr__(self, k, v):
        self[k] = v

    def __delattr__(self, k):
        try:
            del self[k]
        except KeyError as e:
            raise AttributeError(k) from e


class _Noop:
    """context-manager / callable / iterable 皆惰性 no-op（cover st.expander/columns/…）。"""
    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False

    def __call__(self, *a, **k):
        return self

    def __iter__(self):
        return iter(())

    def __bool__(self):
        return False


class _FakeStreamlit:
    def __init__(self):
        self.session_state = _SessionState()

    def _cache_deco(self, *a, **k):
        # 支援 @st.cache_data 與 @st.cache_data(...) 兩式
        if len(a) == 1 and callable(a[0]) and not k:
            return a[0]

        def _wrap(fn):
            return fn
        return _wrap

    def __getattr__(self, name):
        if name in ("cache_data", "cache_resource", "cache", "experimental_memo",
                    "experimental_singleton"):
            return self._cache_deco
        # 其餘 st.* 一律 no-op（回傳 _Noop，兼容 with/呼叫/迭代）
        def _noop(*a, **k):
            return _Noop()
        return _noop


def _install_fake_streamlit():
    fake = _FakeStreamlit()
    sys.modules["streamlit"] = fake
    return fake


# ---------------- AST filter ----------------
_KEEP_TOP = (ast.Import, ast.ImportFrom, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)


def _refs_streamlit(node):
    """RHS 是否引用 st / streamlit（用以剔除 UI 衍生之模組級 Assign）。"""
    for n in ast.walk(node):
        if isinstance(n, ast.Name) and n.id in ("st", "streamlit"):
            return True
        if isinstance(n, ast.Attribute) and isinstance(n.value, ast.Name) \
                and n.value.id in ("st", "streamlit"):
            return True
    return False


def _filter_module(src):
    tree = ast.parse(src)
    kept, skipped = [], 0
    for node in tree.body:
        if isinstance(node, _KEEP_TOP):
            kept.append(node)
        elif isinstance(node, (ast.Assign, ast.AnnAssign)):
            # 只留「非 st 衍生」之常數/賦值（HUALIEN_MIN_LOT_TABLE 等）
            if node.value is not None and not _refs_streamlit(node):
                kept.append(node)
            else:
                skipped += 1
        else:
            # 模組級 Expr/If/For/While/With/Try（UI script）→ 跳過
            skipped += 1
    new_mod = ast.Module(body=kept, type_ignores=[])
    ast.fix_missing_locations(new_mod)
    return new_mod, len(kept), skipped


_CACHE = {}


def harvest(app_py=APP_PY):
    """回傳 (ns, fake_st)：ns 為真函式活命名空間，fake_st 供 driver 填 session_state。"""
    if app_py in _CACHE:
        return _CACHE[app_py]
    with open(app_py, "r", encoding="utf-8") as f:
        src = f.read()
    fake = _install_fake_streamlit()
    mod, nkept, nskip = _filter_module(src)
    code = compile(mod, filename="<app.py:harvest>", mode="exec")
    ns = {"__name__": "app_harvested", "__file__": app_py}
    exec(code, ns)
    ns["__harvest_stats__"] = {"kept": nkept, "skipped": nskip}
    _CACHE[app_py] = (ns, fake)
    return ns, fake


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    ns, st = harvest()
    print("harvest stats:", ns["__harvest_stats__"])
    need = [
        "parse_block_dxf", "parse_ua_cadastral_dxf", "_extract_cad_lines",
        "get_min_lot_size", "_estimate_G_for_qualification",
        "select_corner_lots_both_sides_v12", "_pk_one_side_v12",
        "_build_corner_range_v2", "_make_chamfer_tri_wb",
        "_compute_per_end_cutoff_areas", "_rebuild_corners_topology",
        "_boundary_len_on_line", "rw_from_width",
    ]
    print("\n=== required functions present? ===")
    missing = []
    for name in need:
        ok = callable(ns.get(name))
        print(f"  {'OK ' if ok else 'MISS'} {name}")
        if not ok:
            missing.append(name)

    # smoke 1: harvested _pk_one_side_v12 reproduces 手冊圖8 golden
    print("\n=== smoke: _pk_one_side_v12 fig8 golden ===")
    grp = [
        {"暫編地號": "1", "min_area_to_apply": 0.0, "G_value": 1e9,
         "_corner_cut_len": 5.0, "_corner_cut_den": 5.0, "_side_line_len": 25.0,
         "_side_line_den": 37.0, "_corner_intersection_area": 100.0, "_corner_range_area": 300.0},
        {"暫編地號": "2", "min_area_to_apply": 0.0, "G_value": 1e9,
         "_corner_cut_len": 0.0, "_corner_cut_den": 5.0, "_side_line_len": 12.0,
         "_side_line_den": 37.0, "_corner_intersection_area": 200.0, "_corner_range_area": 300.0},
    ]
    res = ns["_pk_one_side_v12"](grp, {}, 100.0)
    by = {c["暫編地號"]: round(float(c["priority_index"]), 4) for c in res["qualified"]}
    print("  scores:", by, "winner:", res["winner"]["暫編地號"])
    assert by == {"1": 0.6685, "2": 0.3315} and res["winner"]["暫編地號"] == "1", "golden mismatch!"
    print("  golden OK (harvested == real)")

    # smoke 2: parse_block_dxf on V6.dxf
    print("\n=== smoke: parse_block_dxf(V6.dxf) ===")
    dxf = os.path.join(os.path.dirname(APP_PY), "data", "V6.dxf")
    with open(dxf, "rb") as f:
        raw = f.read()
    try:
        blocks = ns["parse_block_dxf"](raw)
        n = len(blocks.get("polygons", blocks)) if isinstance(blocks, dict) else len(blocks)
        print("  parse_block_dxf returned type:", type(blocks).__name__,
              "| keys:", list(blocks.keys())[:8] if isinstance(blocks, dict) else n)
    except Exception as e:
        print("  parse_block_dxf ERROR:", repr(e))

    print("\nRESULT:", "ALL PRESENT + GOLDEN OK" if not missing else f"MISSING {missing}")
