from agno.agent import Agent
from agno.models.openai import OpenAIResponses
from agno.models.groq import Groq
from dotenv import load_dotenv
# import team of ai agent
from agno.team import Team



load_dotenv(override= True)
eng_agent = Agent( name="English Agent", role= "Ans Questions in english")
chi_agent = Agent( name="Chinese Agent", role= "Ans Questions in Chinese")
hindi_agent = Agent( name="Hindi Agent", role= "Ans Questions in Hindi")

team = Team(
    name= "Translation Team",
    members= [eng_agent, chi_agent, hindi_agent ],
    model= OpenAIResponses(id= "gpt-5.4"),
    markdown= True,
    show_members_responses= True,
    instructions= """
                All member agents must respond to answer the query in thier specific language. 
                Do not route just one agent.
                Output the response of all agents
    """
)

team.print_response("what is the capital of India?")