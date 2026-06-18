from agno.agent import Agent
from agno.models.openai import OpenAIResponses
from agno.models.groq import Groq
from dotenv import load_dotenv
# import database
from agno.db.sqlite import SqliteDb
# Importing the tools
from agno.tools.duckduckgo import DuckDuckGoTools
from rich.pretty import pprint

load_dotenv(override= True)

db = SqliteDb(db_file="agno.db")
db.clear_memories()

def build_agent():
    return Agent(
        db = db,
        model= OpenAIResponses(id="gpt-5.2"),
        tools= [DuckDuckGoTools()],
        markdown= True,
        instructions= "you are an helpful traveller ai agent",
        add_history_to_context= True,
        enable_user_memories= True
    )

agent = build_agent()
user_id = "rahul@comcom"
agent.print_response(input("Enter where you wnat to GO...........................\n"),user_id= user_id)
agent.print_response(input("Enter where you wnat to GO...........................\n"),user_id= user_id)

memories =agent.get_user_memories(
    user_id= user_id
)
print("Memories :--------")

pprint(memories)