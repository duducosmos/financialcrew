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
import yaml
from crewai import Task, Agent
from crewai import LLM
from typing import Any, Dict, Optional
from pydantic import BaseModel, Field


class AgentConfig(BaseModel):
    config: Optional[Dict[str, Any]] = Field(
        description="Configuration for the agent",
        default=None,
        exclude=True
    )


class TaskConfig(BaseModel):
    config: Optional[Dict[str, Any]] = Field(
        description="Configuration for the Task",
        default=None,
        exclude=True
    )


class CrewFromYaml:
    task_parameters = [
        "description",
        "expected_output",
        "agent",
    ]
    agent_parameters = [
        "role",
        "goal",
        "backstory",
        "tools"
    ]

    def __init__(self, crewai_yaml: str):
        self._agents_tasks = CrewFromYaml.load_yaml(crewai_yaml)
        if "agents" not in self._agents_tasks:
            raise Exception(f"Agents not Found in {crewai_yaml}")
        if "tasks" not in self._agents_tasks:
            raise Exception(f"Tasks not Found in {crewai_yaml}")
        self._validate()
        self._agent_config = None
        self._task_config = None

    @property
    def agents(self):
        if self._agent_config is None:
            self._agent_config = {}
            for agent in self._agents:
                self._agent_config[agent] = self._agents[agent]

        return self._agent_config

    @property
    def tasks(self):
        if self._task_config is None:
            self._task_config = {}
            for task in self._tasks:
                self._task_config[task] = self._tasks[task]

        return self._task_config

    def _validate(self):
        self._agents = self._agents_tasks["agents"]
        self._tasks = self._agents_tasks["tasks"]
        for agent in self._agents:
            for key in self._agents[agent]:
                if key not in self.agent_parameters:
                    raise Exception(
                        f"Invalid Agent Parameter: {key}\nAgents must hav: {self.agent_parameters}")

        for taks in self._tasks:
            for key in self._tasks[taks]:
                if key not in self.task_parameters:
                    raise Exception(
                        f"Invalid Agent Parameter: {key}\nAgents must hav: {self.agent_parameters}")

    @staticmethod
    def load_yaml(crewai_yaml: str):
        with open(crewai_yaml) as crewyml:
            try:
                agents_task = yaml.safe_load(crewyml)
            except yaml.YAMLError as exc:
                print(exc)
        return agents_task

    @staticmethod
    def create_task(config: dict, agent: Agent, tools: list = []) -> Task:
        return Task(
            agent=agent,
            tools=tools,
            config=config
        )

    @staticmethod
    def create_agent(config: dict, llm: LLM, tools: list = []) -> Agent:
        return Agent(
            config=config,
            tools=tools,
            llm=llm
        )
