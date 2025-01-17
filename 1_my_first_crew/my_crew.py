from crewai import Crew, Process
import os

## Your agents and tasks
from my_agents import chat_bot
from my_tasks import chat_task

## Your Groq API key goes here ...
## If using other cloud for LLM, provide the API key
os.environ['GROQ_API_KEY'] = "Your API Key"
# os.environ['OPENAI_API_KEY'] = "Your API Key"

## Define the crew with Agent and Task. Here simple crew.
crew = Crew (
    agents = [chat_bot],
    tasks = [chat_task],
)

## Initiate a run for Crew and get the response. Provide input with the same parameter name as used in the agent, task definition
## Now your first AI Agent should work and respond to your query. Try asking some other interesting question ...!
result = crew.kickoff (inputs={'query' : 'What is Bangalore famously known for?'})