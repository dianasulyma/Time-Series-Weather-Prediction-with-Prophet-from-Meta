# since we are dealing with several csv files, we need a way to merge them into one global file
import os
import pandas as pd

def combine_csvs(path, output_filename="weather_data.csv"):
    # list all .csv files in the directory
    files = [os.path.join(path, f) for f in os.listdir(path) if f.endswith(".csv")]
    if not files:
        raise FileNotFoundError("No CSV files found in the specified directory.")

    # read and combine them
    dfs = []
    for file in files:
        df = pd.read_csv(file)
        dfs.append(df)

    combined_df = pd.concat(dfs, ignore_index=True)

    combined_df.columns = [
        "longitude", "latitude", "station_name", "climate_id", "date_time", "year",
        "month", "day", "data_quality", "max_temp", "max_temp_flag", "min_temp",
        "min_temp_flag", "mean_temp", "mean_temp_flag", "heat_deg_days",
        "heat_deg_days_flag", "cool_deg_days", "cool_deg_days_flag", "total_rain",
        "total_rain_flag", "total_snow", "total_snow_flag", "total_percip",
        "total_percip_flag", "snow_on_ground", "snow_on_ground_flag",
        "dir_of_max_gust", "dir_of_max_gust_flag", "spd_of_max_gust",
        "spd_of_max_gust_flag"
    ]

    # save the combined CSV in your project folder
    output_path = os.path.join(path, output_filename)
    combined_df.to_csv(output_path, index=False)
    print(f"Combined CSV saved as: {output_path}")

    return combined_df

combine_csvs("/Users/dianarogachova/Desktop/Climate Data")