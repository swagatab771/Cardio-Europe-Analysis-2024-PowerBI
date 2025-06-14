import pandas as pd
from prophet import Prophet
import pmdarima as pm


def forecast_mortality(input_csv, target_year):
    """
    Forecast mortality rates for the target_year using data from input_csv.
    Uses Prophet if 3 or more data points are available; otherwise, uses ARIMA.

    Parameters:
    - input_csv: str, path to the CSV file with historical data
    - target_year: int, the year to forecast

    Returns:
    - forecast_df: pandas.DataFrame with columns ['Year', 'Country', 'Disease', 'Gender', 'Rate']
    - original_df: pandas.DataFrame, original data loaded from input_csv
    """
    data = pd.read_csv(input_csv)
    results = []

    for (country, disease, gender), group in data.groupby(['Country', 'Disease', 'Gender']):
        group = group.sort_values('Year')
        df_ts = pd.DataFrame()
        df_ts['ds'] = group['Year'].astype(str) + '-01-01'
        df_ts['y'] = group['Rate']

        if len(df_ts) >= 3:
            model = Prophet(yearly_seasonality=False, daily_seasonality=False, weekly_seasonality=False)
            model.fit(df_ts)
            future = pd.DataFrame({'ds': [f'{target_year}-01-01']})
            forecast = model.predict(future)
            prediction = forecast['yhat'].values[0]
        else:
            arima_model = pm.auto_arima(df_ts['y'], seasonal=False, suppress_warnings=True)
            prediction = arima_model.predict(n_periods=1)[0]

        results.append({
            'Year': target_year,
            'Country': country,
            'Disease': disease,
            'Gender': gender,
            'Rate': round(prediction, 2)
        })

    forecast_df = pd.DataFrame(results)
    return forecast_df, data


def main():
    input_file = 'Mortality_2021_2023.csv'  # Change if needed
    target_year = 2024  # Change to desired forecast year

    forecast_df, original_df = forecast_mortality(input_file, target_year)

    # Save forecast only file
    forecast_file = f'Mortality_trend_{target_year}.csv'
    forecast_df.to_csv(forecast_file, index=False)
    print(f"Forecast for {target_year} saved to {forecast_file}")

    # Combine original data and forecast
    combined_df = pd.concat([original_df, forecast_df], ignore_index=True)

    # Sort combined data by Country, Disease, Gender, Year
    combined_df = combined_df.sort_values(by=['Country', 'Disease', 'Gender', 'Year'])

    # Save combined sorted file
    combined_file = f'Mortality_combined_{target_year}.csv'
    combined_df.to_csv(combined_file, index=False)
    print(f"Combined and sorted data saved to {combined_file}")


if __name__ == "__main__":
    main()
