#!/usr/bin/env python
# -*- Coding: UTF-8 -*-

"""
author: Eduardo S. Pereira
email:
"""
from .basetask import BaseTask


class WebSearchTask(BaseTask):
    def __init__(self, agent):
        super().__init__(
            description="Research the latest trends and news about {topic}. Provide a list of relevant links.",
            expected_output="A list of links relevant to {topic}.",
            agent=agent
        )
