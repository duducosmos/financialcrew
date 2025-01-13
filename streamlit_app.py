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
from crewproject import create_crew
from crewai import LLM
from dotenv import load_dotenv


from langchain_openai import ChatOpenAI


load_dotenv()

# Configuração do LLM
agent_llm = ChatOpenAI(
    temperature=0.0,
    model_name="gpt-3.5-turbo"
)


BASEURL = "http://192.168.100.123:11434"
MODEL = "llama3.1"


# agent_llm = LLM(
#     base_url=BASEURL,
#     model=f"ollama/{MODEL}",
#     api_key="your-api-key"
# )

crew = create_crew(agent_llm)

result = crew.kickoff(inputs={
                      "topic": "Para o período de 01 de janeiro de 2024 até 01 deJaneiro de 2025 e intervalo de '1wk'."
                      "Como foi o resultado financeiro para Weg no IBOVESPA em 2024?"
                      })
print(result)
