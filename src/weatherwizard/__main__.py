import argparse
from weatherwizard import api
from weatherwizard.cli import print_weather_row, print_forecast_table

def main():
    parser = argparse.ArgumentParser(prog="weather", description="Fetch current weather for a specified city.")
    sub = parser.add_subparsers(dest="command")
    
    city_p = sub.add_parser("city", help="Show current weather for a city")
    city_p.add_argument("name", type=str, help='City name, e.g. "Orlando"')
    
    forecast_p = sub.add_parser("forecast", help="Show daily weather forecast for a city")
    forecast_p.add_argument("name", type=str, help='City name, e.g. "Orlando"')
    forecast_p.add_argument("--days", type=int, default=3, help="Number of days (default 3, max ~7-14 depending on API)")
    forecast_p.add_argument("--units", choices=["c", "f"], default="c", help="Temperature units: c or f (default c)")
    
    args = parser.parse_args()
    
    if args.command == "city":
        try:
            data = api.fetch_current_weather(args.name)
            print_weather_row(data["city"], data["temperature"], data["windspeed"])
        except api.ApiError as e:
            print(f"Error: {e}")
            
    elif args.command == "forecast":
        try:
            data = api.fetch_daily_forecast(args.name, days=args.days)
            dates = data["dates"]
            tmin = data["temperatures_min"]
            tmax = data["temperatures_max"]
            if args.units == "f":
                tmin = [api.c_to_f(t) for t in tmin]
                tmax = [api.c_to_f(t) for t in tmax]
            print_forecast_table(data["city"], dates, tmin, tmax, units=args.units)
        except api.ApiError as e:
            print(f"Error: {e}")
            
    else:
        parser.print_help()
        
if __name__ == "__main__":
    main()