from __future__ import annotations
from .cache import read_cache, write_cache
import requests

# indirection for easier monkeypatching in tests
def requests_get(*args, **kwargs):
    return requests.get(*args, **kwargs)

class ApiError(Exception):
    pass

def _geocode_city(name: str) -> tuple[float, float, str]:
    """Return (lat, lon, resolved_name) using Open-Meteo geocoding API."""
    url = "https://geocoding-api.open-meteo.com/v1/search"
    resp = requests_get(url, params={"name": name, "count": 1}, timeout=10)
    if resp.status_code != 200:
        raise ApiError(f"Geocoding API error: {resp.status_code}")
    data = resp.json()
    results = data.get("results") or []
    if not results:
        raise ApiError(f"City '{name}' not found")
    
    item = results[0]
    return float(item["latitude"]), float(item["longitude"]), item.get("name", name)

def fetch_current_weather(city: str) -> dict:
    """Fetch current weather for city; returns dict with keys: city, temperature, windspeed."""
    city_key = city.strip().lower()
    cache = read_cache()
    if city_key in cache:
        return cache[city_key]
    
    lat, lon, resolved = _geocode_city(city)
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature,windspeed"
    }
    resp = requests_get(url, params=params, timeout=10)
    if resp.status_code != 200:
        raise ApiError(f"Weather API error: {resp.status_code}")
    data = resp.json()
    current = data.get("current_weather") or {}
    temperature = float(current.get("temperature"))
    windspeed = float(current.get("windspeed"))
    # Open-Meteo wind is m/s by default in some endpoints; assume m/s -> km/s (x 3.6)
    windspeed_kmh = windspeed * 3.6
    result = {"city": resolved, "temperature": temperature, "windspeed": round(windspeed_kmh, 1)}
    cache[city_key] = result
    write_cache(cache)
    return result