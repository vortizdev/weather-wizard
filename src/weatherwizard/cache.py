import json
from pathlib import Path
from typing import Any

CACHE_PATH = Path(".weather_cache.json")

def read_cache() -> dict[str, Any]:
    """Read cache from disk; return empty dict if not found or invalid."""
    if not CACHE_PATH.exists():
        return {}
    try:
        return json.loads(CACHE_PATH.read_text(encoding="utf-8") or "{}")
    except Exception:
        return {}
    
def write_cache(cache: dict[str, Any]) -> None:
    """Write cache dict to disk as JSON."""
    CACHE_PATH.write_text(json.dumps(cache, indent=2), encoding="utf-8")