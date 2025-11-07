import json
from types import SimpleNamespace
from weatherwizard import api

class DummyResponse:
    def __init__(self, status_code=200, json_data=None):
        self.status_code = status_code
        self._json_data = json_data or {}
        self.text = json.dumps(self._json_data)

    def json(self):
        return self._json_data
    
def test_fetch_current_weather_monkeypatch(monkeypatch):
    # 1) fake geocoding
    def fake_get_geocode(url, params=None, timeout=10):
        assert "geocoding-api.open-meteo.com" in url
        return DummyResponse(200, {
            "results": [{"name": "Orlando", "latitude": 28.5383, "longitude": -81.3792}]
            })
        
    # 2) fake weather data
    def fake_get_weather(url, params=None, timeout=10):
        assert "api.open-meteo.com" in url
        return DummyResponse(200, {
            "current_weather": {
                "temperature": 30.5,
                "windspeed": 15.0
            }
        })
    
    # monkeypatch requests.get to out fakes in sequence
    calls = {"count": 0}
    def fake_requests_get(url, params=None, timeout=10):
        if calls["count"] == 0:
            calls["count"] += 1
            return fake_get_geocode(url, params, timeout)
        else:
            return fake_get_weather(url, params, timeout)
        
    monkeypatch.setattr(api, "requests_get", fake_requests_get)
    
    json_data = api.fetch_current_weather("Orlando")
    assert json_data["city"] == "Orlando"
    assert "temperature" in json_data and "windspeed" in json_data
    assert isinstance(json_data["temperature"], (int, float))

def test_fetch_daily_forecast_monkeypatch(monkeypatch):
    # 1) fake geocoding
    def fake_get_geocode(url, params=None, timeout=10):
        assert "geocoding-api.open-meteo.com" in url
        return DummyResponse(200, {
            "results": [{"name": "Orlando", "latitude": 28.5383, "longitude": -81.3792}]
            })
        
    # 2) fake forecast data
    def fake_get_forecast(url, params=None, timeout=10):
        assert "api.open-meteo.com" in url
        return DummyResponse(200, {
            "daily": {
                "time": ["2025-11-05", "2025-11-06", "2025-11-07"],
                "temperature_2m_min": [20.0, 21.5, 19.0],
                "temperature_2m_max": [30.0, 31.5, 29.0]
            }
        })
    
    # monkeypatch requests.get to out fakes in sequence
    calls = {"count": 0}
    def fake_requests_get(url, params=None, timeout=10):
        if calls["count"] == 0:
            calls["count"] += 1
            return fake_get_geocode(url, params, timeout)
        else:
            return fake_get_forecast(url, params, timeout)
        
    monkeypatch.setattr(api, "requests_get", fake_requests_get)
    
    json_data = api.fetch_daily_forecast("Orlando", days=3)
    assert json_data["city"] == "Orlando"
    assert len(json_data["dates"]) == 3
    assert len(json_data["temperatures_min"]) == 3
    assert len(json_data["temperatures_max"]) == 3