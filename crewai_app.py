from crewproject import create_crew
from crewai import LLM
from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_openai import ChatOpenAI


load_dotenv()


BASEURL = "http://192.168.100.123/:11434"
MODEL = "llama3.1"

agents = {
    "gemmini": LLM(
        model='gemini/gemini-1.5-flash',
        api_key=os.getenv("GOOGLE_API_KEY")
    ),
    "ollama": LLM(
        base_url=BASEURL,
        model=f"ollama/{MODEL}",
        api_key="your-api-key"
    ),
    "gpt": ChatOpenAI(
        temperature=0.0,
        model_name="gpt-3.5-turbo"
    )
}

agent_llm = agents["gpt"]


crew = create_crew(agent_llm, "agents_task.yaml")

result = crew.kickoff(inputs={
    "topic": "Para o período de 01 de janeiro de 2024 até 01 deJaneiro de 2025 e intervalo de '1wk'. Como foi o resultado financeiro para Petrobras no IBOVESPA em 2024?"
})
