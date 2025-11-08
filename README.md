<div align="center">

# ☁️ Weather Wizard CLI  
**A sleek terminal app for real-time weather and multi-day forecasts — powered by Open-Meteo API.**  

[![Tests](https://github.com/vortizdev/weatherwizard/actions/workflows/tests.yml/badge.svg)](https://github.com/vortizdev/weatherwizard/actions/workflows/tests.yml)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.11%2B-yellow.svg)]()
[![Built with Rich](https://img.shields.io/badge/UI-Rich%20Library-8A2BE2.svg)](https://github.com/Textualize/rich)

</div>

---

## Overview
**Weather Wizard** is a Python-based command-line interface (CLI) for checking live weather and forecasts.  
It uses the [Open-Meteo](https://open-meteo.com) public API and prints beautiful, colorized tables using the `rich` library.

### Features
- `weather city "Orlando"` — current temperature and wind  
- `weather forecast "Orlando" --days 5` — 5-day forecast  
- `--units c|f` — display °C/km/h or °F/mph  
- Smart caching to avoid redundant network calls  
- Fully tested with `pytest` (mocked API responses)  

---

## Quickstart
```bash
git clone https://github.com/vortizdev/weatherwizard.git
cd weatherwizard
python -m venv .venv
.venv\Scripts\activate   # (on macOS/Linux: source .venv/bin/activate)
pip install -e .
weather city "Orlando" --units c
weather forecast "Orlando" --days 3 --units f

