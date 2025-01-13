#!/usr/bin/env python
# -*- Coding: UTF-8 -*-

"""
author: Eduardo S. Pereira
email:
"""
from .basetask import BaseTask


class EditorTask(BaseTask):
    def __init__(self, agent):
        super().__init__(
            description="Proofread and edit the financial report for grammatical errors, clarity, and alignment with the brand's voice.",
            expected_output="A polished and publication-ready financial report in markdown format.",
            agent=agent
        )
