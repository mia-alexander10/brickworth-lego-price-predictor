from __future__ import annotations
import time
import requests
import pandas as pd
from pathlib import Path
from typing import Iterator, Dict, Any, Optional
from src.config import Config

CFG = Config()
HEADERS = {"Authorization": f"key {CFG.rebrickable_key}"}  # required

def _paged_get(url: str, params: Optional[dict] = None) -> Iterator[Dict[str, Any]]:
    """Generic paginator for Rebrickable endpoints with ?page= & ?page_size=."""
    if not CFG.rebrickable_key:
        raise RuntimeError("Set REBRICKABLE_API_KEY in your environment/.env")
    page = 1
    params = dict(params or {})
    params.setdefault("page_size", 100)
    while True:
        params["page"] = page
        resp = requests.get(url, headers=HEADERS, params=params, timeout=30)
        if resp.status_code == 429:
            # backoff on rate limit
            time.sleep(5);  # simple backoff
            continue
        resp.raise_for_status()
        data = resp.json()
        for r in data.get("results", []):
            yield r
        if not data.get("next"):
            break
        page += 1
        time.sleep(0.2)  # be polite

def fetch_themes() -> pd.DataFrame:
    url = f"{CFG.rebrickable_base}/lego/themes/"
    rows = list(_paged_get(url))
    return pd.DataFrame(rows)

def fetch_all_sets(year_min: int = 1990, year_max: int | None = None) -> pd.DataFrame:
    """Fetch all LEGO sets within a year range."""
    url = f"{CFG.rebrickable_base}/lego/sets/"
    params = {"min_year": year_min}
    if year_max:
        params["max_year"] = year_max

    rows = list(_paged_get(url, params))
    return pd.DataFrame(rows)

def fetch_set_inventory(set_num: str) -> pd.DataFrame:
    # inventory parts for one set (useful for features)
    url = f"{CFG.rebrickable_base}/lego/sets/{set_num}/parts/"
    rows = list(_paged_get(url))
    return pd.DataFrame(rows)

def save_df(df: pd.DataFrame, path: Path) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    # save both csv + parquet for convenience
    df.to_csv(path.with_suffix(".csv"), index=False)
    try:
        df.to_parquet(path.with_suffix(".parquet"), index=False)
    except Exception:
        pass
    return path

def run_basic_pull() -> None:
    # 1) themes
    themes = fetch_themes()
    save_df(themes, CFG.raw_dir / "rebrickable_themes")

    # 2) ALL sets since 1990
    sets_df = fetch_all_sets(year_min=1990)
    save_df(sets_df, CFG.raw_dir / "rebrickable_sets_all")

    # 3) sample inventories for top 20 sets
    sample = sets_df["set_num"].dropna().unique()[:20]
    inv_frames = []
    for s in sample:
        parts_df = fetch_set_inventory(s)
        parts_df["set_num"] = s
        inv_frames.append(parts_df)
    if inv_frames:
        inv_df = pd.concat(inv_frames, ignore_index=True)
        save_df(inv_df, CFG.raw_dir / "rebrickable_inventories_sample")

if __name__ == "__main__":
    run_basic_pull()
