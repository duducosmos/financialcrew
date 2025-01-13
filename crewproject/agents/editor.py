#!/usr/bin/env python
# -*- Coding: UTF-8 -*-

"""
author: Eduardo S. Pereira
email:
from crewai import Agent

"""
from .baseagent import BaseAgent


class EditorAgent(BaseAgent):
    def __init__(self, tools, llm):
        super().__init__(
            role="Editor",
            goal="Edit the financial report to align with journalistic and organizational standards.",
            backstory="You refine the financial report to ensure it is polished, aligns with the organization's voice, and follows best practices.",
            tools=tools,
            llm=llm
        )
