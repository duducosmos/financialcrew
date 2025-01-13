#!/usr/bin/env python
# -*- Coding: UTF-8 -*-

"""
author: Eduardo S. Pereira
email:
from crewai import Agent

"""
from .baseagent import BaseAgent
from .schema import ContentWriterSchema


class ContentWriterAgent(BaseAgent):

    def __init__(self, tools, llm):
        super().__init__(
            role=ContentWriterSchema.role,
            goal=ContentWriterSchema.goal,
            backstory=ContentWriterSchema.backstory,
            tools=tools,
            llm=llm
        )
