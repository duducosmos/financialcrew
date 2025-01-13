#!/usr/bin/env python
# -*- Coding: UTF-8 -*-

"""
Custom DuckDuckGo Tool
author: Eduardo S. Pereira
email: pereira.somoza@gmail.com
"""
from typing import Type
from pydantic import BaseModel, Field


class DuckDuckGoToolInput(BaseModel):
    query: str = Field(..., description="Query to search using DuckDuckGo.")


class FinancialToolInput(BaseModel):
    ticker: str = Field(...,
                        description="Stock ticker symbol. E.g., AAPL, GOOGL, PETR4.SA, MGLU3.SA")
    interval: str = Field(...,
                          description="Interval for the stock data. E.g., 1d, 1wk, 1mo")
    start: str = Field(...,
                       description="Start date for the stock data. E.g., 2021-01-01")
    end: str = Field(...,
                     description="End date for the stock data. E.g., 2021-12-31")
