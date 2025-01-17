from crewai import Agent

## Your environment variables need to be stored in '.env' file. That is loaded into the program
## environment variale contains your API key
from dotenv import load_dotenv

# loading env
load_dotenv ()

## Here we are defining 2 agents, that are going to collaborate as a 'crew'. They both of defined role and objective

## Agent designed to explore and gather information about a topic. The parameter used same as while triggering
## Back story sets the context for the agent & goal says the objective clearly.
explorer = Agent (
    role = 'Data Explorer',
    goal = 'Research, gather and provide information about the topic : {topic}',    
    llm = 'groq/llama3-70b-8192',
    verbose = True,    
    backstory = ('You are an expert researcher, who can gather detailed information about a topic'),
)

## Agent designed to synthesie and summarise the information provided.
## Back story sets the context for the agent & goal says the objective clearly.
synthesiser = Agent (
    role = 'Information Synthesiser',
    goal = 'Summarise the information given in a synthetic manner',    
    llm = 'groq/llama3-70b-8192',
    verbose = True,    
    backstory = ('You are an expert in summarising provided information in a simple, concise and synthetic way'),
)