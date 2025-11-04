from rich.console import Console
from rich.table import Table

def print_weather_row(city: str, temperature: float, windspeed: float) -> None:
    console = Console()
    table = Table(title=f"Weather - {city}", show_lines=False)
    table.add_column("Metric", justify="left")
    table.add_column("Value", justify="right")
    table.add_row("Temperature (°C)", f"{temperature:.1f}")
    table.add_row("Windspeed (km/h)", f"{windspeed:.1f}")
    console.print(table)