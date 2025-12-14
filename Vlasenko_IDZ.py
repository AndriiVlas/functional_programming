import yfinance as yf
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

# Функція завантаження числового ряду з yfinance (З ПОБІЧНИМ ЕФЕКТОМ)
def download_market_data(start="2015-01-01", end="2025-04-13"):
    tickers = {
    'IBM': 'IBM',
    'S&P500': '^GSPC',
    'CrudeOil': 'CL=F',
    'Crypto_BTC': 'BTC-USD'
    }
    df = pd.DataFrame()
    for name, ticker in tickers.items():
        data = yf.download(ticker, start=start, end=end)['Close']
        df[name] = data
    return df

# Функція виводу інформації користувачу (З ПОБІЧНИМ ЕФЕКТОМ)
def visualize_time_series(df, title="Ціни закриття активів"):
    fig = go.Figure()
    for col in df.columns:
        fig.add_trace(go.Scatter(x=df.index, y=df[col], mode='lines', name=col))  
    fig.update_layout(title=f'{title} (Plotly)', xaxis_title='Дата', yaxis_title='Значення', height=500)
    fig.show()

# Функція очищення даних від пропущених значень (ЧИСТА)
def clear_data(df):
    df_tmp = df.dropna()
    return df_tmp

# Функція нормалізації даних (ЧИСТА)
def normalize_data(df):
    df_copy = df.copy()
    def min_max_scale(series):
        min_val = series.min()
        max_val = series.max()
        if max_val == min_val:
            return series * 0.0
        return (series - min_val) / (max_val - min_val)
    df_tmp = df_copy.apply(min_max_scale, axis=0)
    return df_tmp

# Функція, яка для заданого датафрейму повертає таблицю з описовою статистикою (ЧИСТА)
def my_describe(df):
    df_tmp = df.describe()
    return df_tmp

# Функції підготовки наборів даних (ЧИСТІ)
def create_univariate_dataset(series, window_size, forecast_horizon):
    max_start_index = len(series) - window_size - forecast_horizon + 1
    for i in range(max_start_index):
        X = series[i:i + window_size]
        y = series[i + window_size : i + window_size + forecast_horizon]
        yield X, y

def create_multivariate_dataset(df, target_col, window_size, forecast_horizon):
    values = df.values
    target_idx = df.columns.get_loc(target_col)
    max_start_index = len(df) - window_size - forecast_horizon + 1
    for i in range(max_start_index):
        X = values[i:i + window_size, :]
        future_values = values[i + window_size : i + window_size + forecast_horizon, target_idx]
        yield X, future_values


raw_df = download_market_data()
visualize_time_series(raw_df, '1. Сирі ціни закриття')
cleaned_df = clear_data(raw_df)
normalized_df = normalize_data(cleaned_df)
stats_df = my_describe(normalized_df)
print("Описова статистика нормалізованих даних:")
print(stats_df)
visualize_time_series(normalized_df, '2. Нормалізовані ціни закриття')