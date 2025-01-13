#!/usr/bin/env python
# -*- Coding: UTF-8 -*-

"""
author: Eduardo S. Pereira
email:
from crewai import Agent

"""
from .baseagent import BaseAgent


class WebSearcherAgent(BaseAgent):
    def __init__(self, tools, llm):
        super().__init__(
            role="Web Researcher",
            goal="Collect links related to the topic: {topic}.",
            backstory="You're performing research on {topic}, focusing on gathering relevant links for further analysis.",
            tools=tools,
            llm=llm
        )
