# Cross-Border Arbitrage Simulator

#This script contains the core functionality of the Cross-Border Arbitrage Simulator. 
# It includes functions for fetching stock prices, calculating exchange rates, and 
# executing the arbitrage strategy based on the provided parameters, using Shopify's 
# ticker for demonstration purposes.

import pandas as pd
import numpy as np
import yfinance as yf

def fetch_stock_prices(ticker, start_date, end_date):
    """
    Fetch historical stock prices for the given ticker between start_date and end_date.
    
    Parameters:
    ticker (str): The stock ticker symbol.
    start_date (str): The start date for fetching data in 'YYYY-MM-DD' format.
    end_date (str): The end date for fetching data in 'YYYY-MM-DD' format.
    
    Returns:
    pd.DataFrame: A DataFrame containing the historical stock prices.
    """
    prices = yf.download(ticker, start=start_date, end=end_date, auto_adjust=True)
    return prices['Close']

def calculate_exchange_rate(ex_ticker, start_date, end_date):
    """
    Fetch historical exchange rates for the given exchange ticker between start_date and end_date.
    
    Parameters:
    ex_ticker (str): The exchange rate ticker symbol (e.g., 'CADUSD=X').
    start_date (str): The start date for fetching data in 'YYYY-MM-DD' format.
    end_date (str): The end date for fetching data in 'YYYY-MM-DD' format.
    
    Returns:
    pd.DataFrame: A DataFrame containing the historical exchange rates.
    """
    exchange_rate = yf.download(ex_ticker, start=start_date, end=end_date)
    return exchange_rate['Close']

def execute_arbitrage_strategy(domestic_prices, foreign_prices, exchange_rates, initial_capital, cad_fee, usd_fee_rate, min_rel_spread=0.0):
    """
    Execute the arbitrage strategy based on the provided parameters.
    
    Parameters:
    domestic_prices (pd.Series): The domestic stock prices.
    foreign_prices (pd.Series): The foreign stock prices.
    exchange_rates (pd.Series): The exchange rates.
    initial_capital (float): The initial capital for trading.
    cad_fee (float): The flat fee in CAD for trading.
    usd_fee_rate (float): The fee rate in USD for trading.
    min_rel_spread (float): The minimum relative spread to consider for trading.
    
    Returns:
    pd.DataFrame: A DataFrame containing the equity over time and trades executed.
    """
    capital = initial_capital
    dates, capitals, trades = [], [], []

    for date in domestic_prices.index:
        actual = domestic_prices[date]
        implied = foreign_prices[date] / exchange_rates[date]
        spread = abs(actual - implied)

        if spread / min(actual, implied) >= min_rel_spread:
            num_shares = int(capital / actual)
            if num_shares > 0:
                fees = cad_fee + (num_shares * foreign_prices[date] * usd_fee_rate)
                capital += (spread * num_shares) - fees
                trades.append(1)
            else:
                trades.append(0)
        else:
            trades.append(0)

        dates.append(date)
        capitals.append(capital)

    equity_df = pd.DataFrame({"Equity": capitals, "TradesExecuted": trades}, index=pd.to_datetime(dates))
    equity_df["Profit"] = equity_df["Equity"] - initial_capital
    return equity_df