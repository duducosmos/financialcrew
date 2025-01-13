#!/usr/bin/env python
# -*- Coding: UTF-8 -*-

"""
author: Eduardo S. Pereira
email:
"""
from crewai import Task, Agent


class BaseTask:
    def __init__(self, description: tuple, expected_output: tuple, agent: Agent):
        self._task = Task(
            description=description,
            expected_output=expected_output,
            agent=agent
        )

    @property
    def task(self) -> Task:
        return self._task
