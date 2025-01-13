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
            expected_output="A polished and publication-ready, the final resport must be in  PT-BR, financial report in markdown format with:"
            "1- Title: A clean and short title based on the research.\n "
            "2- Introduction: General view of the report and research done.\n"
            "3- A short review, with 250 words, about the information searched on websites.\n"
            "4- Financial Analysis: The analysis based in the research with tables and solid informationn\n"
            "5- Final Consideration: The final considerations about the report.\n"
            "6- References: List of link and tools used to create the report.",
            agent=agent
        )
