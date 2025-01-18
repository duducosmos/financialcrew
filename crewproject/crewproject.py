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
from crewai import LLM
from crewai import Crew
from crewai_tools import ScrapeWebsiteTool

from .tools import FinancialTool, DuckDuckGoTool

from .crewfromyaml import CrewFromYaml


def create_crew(llm: LLM, crewai_yaml) -> Crew:

    financialtool = FinancialTool()
    duckduckgotool = DuckDuckGoTool()
    scraptool = ScrapeWebsiteTool()

    crew_from_yaml = CrewFromYaml(crewai_yaml)
    agents = crew_from_yaml.agents
    taks = crew_from_yaml.tasks

    web_researcher = CrewFromYaml.create_agent(
        agents["websearcher"],
        llm,
        [duckduckgotool]

    )

    site_scraper = CrewFromYaml.create_agent(
        agents["scraper"],
        llm,
        [scraptool]
    )

    content_writer = CrewFromYaml.create_agent(
        agents["writer"],
        llm,
        [financialtool]
    )

    editor = CrewFromYaml.create_agent(
        agents["editor"],
        llm
    )

    research_task = CrewFromYaml.create_task(taks["search"], web_researcher)
    scrape_task = CrewFromYaml.create_task(taks["scrape"], site_scraper)
    write_task = CrewFromYaml.create_task(taks["write"], content_writer)
    edit_task = CrewFromYaml.create_task(taks["edit"], editor)

    crew = Crew(
        agents=[web_researcher, site_scraper, content_writer, editor],
        tasks=[research_task, scrape_task, write_task, edit_task],
        verbose=True
    )
    return crew
