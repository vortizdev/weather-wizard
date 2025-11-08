# weather-wizard

## Quickstart
'''bash
python -m venv .venv
\venv\Scripts\activate
pip install -e .
python -m weatherwizard city "Orlando"

## Usage
### Current Weather
python -m weatherwizard city "Orlando" --units c
python -m weatherwizard city "Orlando" --units f # Fahrenheit + mph

### Forecast
python -m weatherwizard forecast "Orlando" --days 5 --units c
python -m weatherwizard forecast "Orlando" --days 5 --units f

### Help
python -m weatherwizard --help