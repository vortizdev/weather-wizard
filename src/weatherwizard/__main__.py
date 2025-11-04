import argparse
from weatherwizard import api
from weatherwizard.cli import print_weather_row

def main():
    parser = argparse.ArgumentParser(prog="weather", description="Fetch current weather for a specified city.")
    sub = parser.add_subparsers(dest="command")
    
    city_p = sub.add_parser("city", help="Show current weather for a city")
    city_p.add_argument("name", type=str, help='City name, e.g. "Orlando"')
    
    args = parser.parse_args()
    
    if args.command == "city":
        try:
            data = api.fetch_current_weather(args.name)
            print_weather_row(data["city"], data["temperature"], data["windspeed"])
        except api.ApiError as e:
            print(f"Error: {e}")
    else:
        parser.print_help()
        
if __name__ == "__main__":
    main()