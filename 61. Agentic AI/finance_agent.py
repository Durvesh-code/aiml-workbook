from agno.agent import Agent
from agno.models.openai import OpenAIResponses
from agno.models.groq import Groq
from dotenv import load_dotenv
# Importing the tools
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools

load_dotenv(override= True)

def build_agent():
    return Agent(
        model= OpenAIResponses(id="gpt-5.2"),
        tools= [DuckDuckGoTools(), YFinanceTools()],
        markdown= True,
        description="You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",
        instructions=["Format your response using markdown and use tables to display data where possible."],
        add_datetime_to_context = True
    )

agent = build_agent()

agent.print_response(input("Enter where you wnat to GO...........................\n"))