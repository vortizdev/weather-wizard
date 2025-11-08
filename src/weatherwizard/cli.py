from rich.console import Console
from rich.table import Table
from typing import Iterable

def print_weather_row(city: str, temperature: float, windspeed: float, units: str = "c") -> None:
    """ 
    Render a 2-row table for current weather.
    - units: "c" for Celsius, Windspeed in km/h
    - units: "f" for Fahrenheit, Windspeed in mph
    """
    console = Console()
    u = units.lower()
    temp_label = "°C" if u == "c" else "°F"
    wind_label = "km/h" if u == "c" else "mph"
    
    table = Table(title=f"Weather - {city}", show_lines=False)
    table.add_column("Metric", justify="left")
    table.add_column("Value", justify="right")
    table.add_row(f"Temperature ({temp_label})", f"{temperature:.1f}")
    table.add_row(f"Windspeed ({wind_label})", f"{windspeed:.1f}")
    console.print(table)
    
def print_forecast_table(city: str, dates: list[str], tmin: Iterable[float], tmax: Iterable[float], units: str = "c") -> None:
    console = Console()
    unit_label = "°C" if units == "c" else "°F"
    
    table = Table(title=f"Forecast - {city}", show_lines=False)
    table.add_column("Date", justify="left")
    table.add_column(f"Min ({unit_label})", justify="right")
    table.add_column(f"Max ({unit_label})", justify="right")
    
    for d, lo, hi in zip(dates, tmin, tmax):
        table.add_row(d, f"{lo:.1f}", f"{hi:.1f}")
    
    console.print(table)