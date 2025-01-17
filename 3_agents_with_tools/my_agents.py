from crewai import Agent, Task
from crewai.tools import tool
from datetime import datetime

## Use a web search tool from lang chain community.
from langchain_community.tools import DuckDuckGoSearchRun

## Your environment variables need to be stored in '.env' file. That is loaded into the program
## environment variale contains your API key
from dotenv import load_dotenv

# loading env
load_dotenv ()

## Current time and date
Now = datetime.now ()
Today = Now.strftime ("%d-%b-%Y")

## Making a tool form lang chain into a typical tool in crew AI
@tool("DuckDuckGo Search")
def search_tool(search_query: str) :
    """Search the internet for information on a given topic"""
    # Call the tool
    return DuckDuckGoSearchRun ().run (search_query)

## Here we are defining 3 agents, for different purpose. Its stated in the role and goal

## Agent designed to gather information about a topic from internet. Agent is given search tool to get results
## Back story sets the context for the agent. Also Agent is set to current day scenario to make it clear context
content_explorer = Agent (
    role = 'data researcher',
    goal = 'Gather and provide latest information about the topic from internet',    
    # llm = 'groq/llama3-70b-8192',
    llm = 'gpt-4o-mini',
    verbose = True,    
    backstory = ('You are an expert researcher, who can gather detailed information about a topic. \
                  Consider you are on : '+Today),
    tools = [search_tool],
    cache = True,
    max_iter = 5
)

## Agent designed to as a financial data analyst. It requires financial data and can make analysis out of it.
## Back story sets the context for the agent.
analyst = Agent (
    role = 'Data Analyst',
    goal = 'Consolidate financial data, stock information and provide a summary',    
    # llm = 'groq/llama3-70b-8192',
    llm = 'gpt-4o-mini',
    verbose = True,    
    backstory = ('You are an expert in analysing financial data and stock related information to make it into a analysis summary.\
                 Consider you are on '+Today),
)

## Agent designed to be a financial expert, who can make investment recommendation
fin_expert = Agent (
    role = 'Financial Expert',
    goal = 'Considering Financial analysis of a stock, make investment recommendation',    
    # llm = 'groq/llama3-70b-8192',
    llm = 'gpt-4o-mini',
    verbose = True,    
    backstory = ('You are financial advisor, who can provide investment recommendation.\
                 Consider the financial analysis and make recommendation whether to buy a stock or not.\
                 Consider you are on '+Today),
)
