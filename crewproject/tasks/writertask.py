#!/usr/bin/env python
# -*- Coding: UTF-8 -*-

"""
author: Eduardo S. Pereira
email:
"""
from .basetask import BaseTask


class WriterTask(BaseTask):
    def __init__(self, agent):
        super().__init__(
            description=(
                "1. Scrape the content from the links provided by the Web Researcher.\n"
                "2. Generate a summary of key findings from the scraped content, limited to 250 words.\n"
                "OBS: The ScrapeWebsiteTool has as input the variable `website_url` that is a string with link or url of site."
            ),
            expected_output=(
                "A JSON containing the text scraped from the websites and a concise summary of key findings."
            ),
            agent=agent
        )
