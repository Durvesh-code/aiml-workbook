from agno.agent import Agent
from agno.models.openai import OpenAIResponses
from agno.models.groq import Groq
from dotenv import load_dotenv
# Importing the tools
from agno.tools.duckduckgo import DuckDuckGoTools

load_dotenv(override= True)

def build_agent():
    return Agent(
        model= OpenAIResponses(id="gpt-5.2"),
        tools= [DuckDuckGoTools()],
        markdown= True,
        instructions= "you are an helpful traveller ai agent",
        add_datetime_to_context = True
    )

agent = build_agent()

agent.print_response(input("Enter where you wnat to GO...........................\n"))