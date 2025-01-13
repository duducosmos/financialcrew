#!/usr/bin/env python
# -*- Coding: UTF-8 -*-

"""
author: Eduardo S. Pereira
email:
"""
from .basetask import BaseTask


class SiteScraperTask(BaseTask):
    def __init__(self, agent):
        super().__init__(
            description=(
                "1. Use the summary and scraped text from the Site Scraper, along with data from the FinancialTool, to craft a financial report.\n"
                "2. The report should have the following sections:\n"
                "   - Introduction: Overview of the research conducted.\n"
                "   - Financial Analysis: Include tables and summaries of financial data.\n"
                "   - Conclusion: Provide insights and summarize the findings.\n"
                "3. Ensure the report is structured clearly and written in markdown format, with each section containing at least 2-3 paragraphs."
            ),
            expected_output="A well-structured financial report in markdown format, ready for publication.",
            agent=agent
        )
