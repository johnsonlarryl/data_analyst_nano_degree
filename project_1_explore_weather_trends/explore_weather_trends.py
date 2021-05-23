import argparse
import matplotlib.pyplot as plt
import pandas as pd
from typing import Tuple


def get_absolute_values(global_years: pd.Series, local_years: pd.Series) -> Tuple[int, int]:
    """
    Returns the absolute minimum and maximum values for years between the two vectors

    Parameters:
        global_years: Vector of global years
        local_years: Vector of local years

    Returns:
        int: Minimum years to filter out
        int: Maximum year to filter out
    """
    global_years_min = global_years.min()
    global_years_max = global_years.max()
    local_years_min = local_years.min()
    local_years_max = local_years.max()

    min_years = max(global_years_min, local_years_min)
    max_years = min(global_years_max, local_years_max)

    return min_years, max_years


def main(global_weather_file: str,
         local_weather_file: str,
         local_city_name: str,
         rolling_average: str) -> None:
    """
    Driver or main function that executes program with its associated command line arguments.

    Parameters:
        global_weather_file
        local_weather_file
        local_city_name
        rolling_averag

    Returns:
        None
    """
    fig = plt.figure()
    fig.subplots_adjust(top=0.8)
    ax1 = fig.add_subplot(211)
    ax1.set_xlabel('Years')
    ax1.set_ylabel('Degrees (°C)')
    ax1.set_title('Exploration of Weather Trends')

    global_weather = pd.read_csv(global_weather_file)
    local_weather = pd.read_csv(local_weather_file)

    min_years, max_years = get_absolute_values(global_weather["year"], local_weather["year"])
    filtered_global_weather = global_weather[(global_weather.year >= min_years) & (global_weather.year <= max_years)]
    filtered_local_weather = local_weather[(local_weather.year >= min_years) & (local_weather.year <= max_years)]

    plt.plot(filtered_global_weather["year"], filtered_global_weather["avg_temp"].rolling(rolling_average).mean(), label="Global")
    plt.plot(filtered_local_weather["year"], filtered_local_weather["avg_temp"].rolling(rolling_average).mean(), label=local_city_name)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Application that explores weather trends")

    parser.add_argument("--global_weather", help="Fully qualified file location of global weather trends", required=True)
    parser.add_argument("--local_weather", help="Fully qualified file location of local weather trends", required=True)
    parser.add_argument("--local_city", help="Local city name for local weather", required=True)
    parser.add_argument("--rolling_average", help="Number of years for rolling average", required=True, type=int)

    args = parser.parse_args()
    global_weather_file = args.global_weather
    local_weather_file = args.local_weather
    local_city_name = args.local_city
    rolling_average = args.rolling_average

    main(global_weather_file, local_weather_file, local_city_name, rolling_average)




