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
from .schema import DuckDuckGoToolInput


class DuckDuckGoTool(BaseTool):
    name: str = "DuckDuckGo Search Tool"
    description: str = "Searches the web using DuckDuckGo."
    args_schema: Type[BaseModel] = DuckDuckGoToolInput

    def _run(self, query: str) -> str:
        ddg_results = DDGS().text(query, max_results=5)
        df = pd.DataFrame(ddg_results)
        return pd.DataFrame({"links": df["href"].tolist()}).to_json(index=False)

    async def _arun(self, query: str) -> str:
        return self._run(query)
