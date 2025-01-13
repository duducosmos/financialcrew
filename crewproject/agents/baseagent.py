#!/usr/bin/env python
# -*- Coding: UTF-8 -*-

"""
author: Eduardo S. Pereira
email:
"""

from crewai import Agent


class BaseAgent:
    def __init__(self, role, goal, backstory, tools, llm):
        self._agent = Agent(
            role=role,
            goal=goal,
            backstory=backstory,
            tools=tools,
            llm=llm
        )

    @property
    def agent(self) -> Agent:
        return self._agent
