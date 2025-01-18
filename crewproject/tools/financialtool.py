#!/usr/bin/env python
# -*- Coding: UTF-8 -*-

"""
Custom DuckDuckGo Tool
author: Eduardo S. Pereira
email: pereira.somoza@gmail.com
"""
from crewai.tools import BaseTool
from duckduckgo_search import DDGS
import pandas as pd
from typing import Type
from pydantic import BaseModel
import yfinance as yf
from .schema import FinancialToolInput
import matplotlib.pyplot as plt
import mplfinance as mpf
import matplotlib.dates as mpl_dates
import numpy as np
import datetime

import os


class FinancialTool(BaseTool):
    name: str = "Financial tool"
    description: str = "Uses Yahoo Finance to analyze stock market data."
    args_schema: Type[BaseModel] = FinancialToolInput

    def _run(self, ticker: str, interval: str, start: str, end: str) -> str:
        try:
            data = yf.Ticker(ticker)
            df1 = data.history(interval=interval, start=start, end=end)

            if df1.empty:
                return '{"error": "No data returned. Check provided parameters."}'

            # Reformatar os dados
            df = pd.DataFrame({
                "date": df1.index.to_list(),
                "year": df1.index.year.tolist(),
                "month": df1.index.month.tolist(),
                "day": df1.index.day.tolist(),
                "Open": df1['Open'].tolist(),
                "Close": df1['Close'].tolist()
            })
            df = df.set_index("date")

            # Adicionar colunas calculadas ao DataFrame
            df['Daily Change'] = df['Close'] - df['Open']
            df['Return'] = (df['Close'] / df['Open']) - 1

            # Indicadores estatísticos
            summary = {
                "Mean Open Price": df['Open'].mean(),
                "Median Open Price": df['Open'].median(),
                "Mean Close Price": df['Close'].mean(),
                "Median Close Price": df['Close'].median(),
                "Max Price": df[['Open', 'Close']].max().max(),
                "Min Price": df[['Open', 'Close']].min().min(),
                "Average Daily Change": df['Daily Change'].mean(),
                "Volatility (Std Dev)": df['Daily Change'].std(),
                "Cumulative Return (%)": ((df['Close'].iloc[-1] / df['Open'].iloc[0]) - 1) * 100,
                "Positive Day Ratio (%)": (df['Daily Change'] > 0).mean() * 100
            }

            output = pd.DataFrame(summary.items(), columns=[
                                  'Metric', 'Value']).to_markdown(index=False)

            imagedir = "./images/reports/"

            os.makedirs(imagedir, exist_ok=True)

            daily_change_image = f"{imagedir}daily_change_{ticker}_{interval}_{start}_{end}.png"

            mpf.plot(df1, type='candle', volume=True,
                     mav=(3, 7, 13), savefig=daily_change_image)

            output += f"\nImage plot: ![Candle for {ticker}]({daily_change_image})"

            return output

        except Exception as error:
            return f'{{"error": "{str(error)}"}}'

    async def _arun(self, *args, **kwargs) -> str:
        return self._run(*args, **kwargs)
