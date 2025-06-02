# model.py
import os
from dotenv import load_dotenv
from phi.agent import Agent
from phi.tools.yfinance import YFinanceTools
from phi.model.groq import Groq

# Load environment variables from .env file
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
PHI_API_KEY = os.getenv("PHI_API_KEY", "")
GROQ_MODEL_TO_USE = "llama-3.3-70b-versatile"

# Preload agent once
_agent = Agent(
    name="financial_agent",
    description="A financial agent that can analyze financial data and search the web for information.",
    instructions=["Always include sources", "Use tables to display data"],
    model=Groq(id=GROQ_MODEL_TO_USE),
    markdown=True,
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            stock_fundamentals=True,
            company_news=True,
        )
    ],
)

def get_agent():
    return _agent
