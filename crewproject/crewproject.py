#!/usr/bin/env python
# -*- Coding: UTF-8 -*-

"""
author: Eduardo S. Pereira
email: pereira.somoza@gmail.com


MIT License

Copyright (c) 2025 Eduardo dos Santos Pereira. pereira.somoza@gmail.com

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from crewai import Crew
from crewai_tools import ScrapeWebsiteTool

from .agents import WebSearcherAgent, ScraperAgent, ContentWriterAgent, EditorAgent
from .tools import FinancialTool, DuckDuckGoTool
from .tasks import WebSearchTask, SiteScraperTask, WriterTask, EditorTask


def create_crew(llm):

    financialtool = FinancialTool()
    duckduckgotool = DuckDuckGoTool()
    scraptool = ScrapeWebsiteTool()

    web_researcher = WebSearcherAgent([duckduckgotool], llm).agent
    site_scraper = ScraperAgent([scraptool], llm).agent
    content_writer = ContentWriterAgent([financialtool], llm).agent
    editor = EditorAgent([], llm).agent

    research_task = WebSearchTask(web_researcher).task
    scrape_task = SiteScraperTask(site_scraper).task
    write_task = WriterTask(content_writer).task
    edit_task = EditorTask(editor).task

    crew = Crew(
        agents=[web_researcher, site_scraper, content_writer, editor],
        tasks=[research_task, scrape_task, write_task, edit_task],
        verbose=True
    )
    return crew
