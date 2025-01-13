#!/usr/bin/env python
# -*- Coding: UTF-8 -*-

"""
author: Eduardo S. Pereira
email:
from crewai import Agent

"""
from .baseagent import BaseAgent


class ContentWriterAgent(BaseAgent):
    def __init__(self, tools, llm):
        super().__init__(
            role="Content Writer",
            goal="Write a comprehensive financial report based on the data provided by the Site Scraper and the `Financial tool`.",
            backstory="You're tasked with creating a detailed financial report on {topic}. This report should include:\n"
            "1. An introduction summarizing the overall research efforts.\n"
            "2. A financial analysis section with details, tables, and numerical summaries from `Financial tool`.\n"
            "3. A conclusion summarizing the findings and providing insights.",
            tools=tools,
            llm=llm
        )
