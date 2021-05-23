import argparse
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from typing import Tuple


def get_absolute_values(global_years: pd.Series, local_years: pd.Series) -> Tuple[int, int]:
    """
    Returns the absolute minimum and maximum values for years between the two vectors

    Parameters:
        global_years: Vector of global years
        local_years: Vector of local years

    Returns:
        Minimum years to filter out
        Maximum year to filter out
    """
    global_years_min = global_years.min()
    global_years_max = global_years.max()
    local_years_min = local_years.min()
    local_years_max = local_years.max()

    min_years = max(global_years_min, local_years_min)
    max_years = min(global_years_max, local_years_max)

    return min_years, max_years


def get_aggregate_temperatures(weather: pd.Series) -> Tuple[float, float]:
    """
    Returns the average temperature and average temperature differences based on a vector of weather data.

    Parameters:
        weather

    Returns:
        Average temperature
        Average temperature difference
    """

    array = weather.to_numpy()
    avg_temp = np.mean(array)
    avg_temp_diff = np.mean(np.diff(array))
    return round(avg_temp, 2), round(avg_temp_diff, 2)


def plot_weather_trends(filtered_global_weather: pd.DataFrame, filtered_local_weather: pd.DataFrame, local_city_name: str, rolling_average: int) -> None:
    """
     Plots the weather trends locally and globally on a line plot chart or graph.

     Parameters:
         filtered_global_weather
         filtered_local_weather
         local_city_name
         rolling_average

     Returns:
         None
     """

    fig = plt.figure()
    fig.subplots_adjust(top=0.8)
    ax1 = fig.add_subplot(211)
    ax1.set_xlabel('Years')
    ax1.set_ylabel('Degrees (°C)')
    ax1.set_title('Exploration of Weather Trends')

    plt.plot(filtered_global_weather["year"], filtered_global_weather["avg_temp"].rolling(rolling_average).mean(), label="Global")
    plt.plot(filtered_local_weather["year"], filtered_local_weather["avg_temp"].rolling(rolling_average).mean(), label=local_city_name)
    plt.legend()
    plt.show()


def print_weather_trends(global_weather: pd.DataFrame, local_weather: pd.DataFrame) -> None:
    """
     Prints weather trends locally and globally in text form.

     Parameters:
         global_weather
         local_weather
     Returns:
         None
     """

    global_weather_avg_temp, global_weather_avg_temp_diff = get_aggregate_temperatures(global_weather["avg_temp"])
    local_weather_avg_temp, local_weather_avg_temp_diff = get_aggregate_temperatures(local_weather["avg_temp"])

    print(f"Global average temperature : {global_weather_avg_temp} degrees (°C)")
    print(f"Global average temperature differences : {global_weather_avg_temp_diff} degrees (°C)")
    print(f"Local average temperature : {local_weather_avg_temp} degrees (°C)")
    print(f"Local average temperature differences : {local_weather_avg_temp_diff} degrees (°C)")


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
    global_weather = pd.read_csv(global_weather_file)
    local_weather = pd.read_csv(local_weather_file)

    min_years, max_years = get_absolute_values(global_weather["year"], local_weather["year"])
    filtered_global_weather = global_weather[(global_weather.year >= min_years) & (global_weather.year <= max_years)]
    filtered_local_weather = local_weather[(local_weather.year >= min_years) & (local_weather.year <= max_years)]

    print_weather_trends(filtered_global_weather, filtered_local_weather)

    plot_weather_trends(filtered_global_weather, filtered_local_weather, local_city_name, rolling_average)


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




