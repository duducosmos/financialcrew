#!/usr/bin/env python
# -*- Coding: UTF-8 -*-

"""
author: Eduardo S. Pereira
email:
from crewai import Agent

"""
from .baseagent import BaseAgent


class ScraperAgent(BaseAgent):
    def __init__(self, tools, llm):
        super().__init__(
            role="Site Scraper",
            goal="Scrape text from the websites provided by the Web Researcher and generate a summary of the findings.",
            backstory="You're extracting text data from the provided links to support further analysis on {topic}. "
            "Additionally, you create a summary of the key information gathered from the sites, limited to 250 words."
            "Organized links as Bibliograph reference."
            "OBS: The ScrapeWebsiteTool has as input the variable `website_url` that is a string with link or url of site.",
            tools=tools,
            llm=llm
        )
