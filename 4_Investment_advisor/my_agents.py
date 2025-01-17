from crewai import Agent, Task
from crewai.tools import tool
from datetime import datetime

## Use a web search tool from lang chain community.
from langchain_community.tools import DuckDuckGoSearchRun

## Use the custom tools built
from my_tools import get_current_stock_price, get_company_info, get_income_statements

## Your environment variables need to be stored in '.env' file. That is loaded into the program
## environment variale contains your API key
from dotenv import load_dotenv

# loading env
load_dotenv ()

## Current time and date
Now = datetime.now ()
Today = Now.strftime ("%d-%b-%Y")

## Making a tool from lang chain into a typical tool in crew AI
@tool("DuckDuckGo Search")
def search_tool(search_query: str) :
    """Search the internet for information on a given topic"""
    # Call the tool
    return DuckDuckGoSearchRun ().run (search_query)

## Here we are defining 4 agents, for different purpose. Its stated in the role and goal

## Agent designed to gather news and about a company internet. Agent is given search tool to get results
## Back story sets the context for the agent. Also Agent is set to current day scenario to make it clear context
news_info_explorer = Agent (
    role = 'news and info researcher',
    goal = 'Gather and provide latest information and news about a company from internet and sythesise',    
    # llm = 'groq/llama3-70b-8192',
    llm = 'gpt-4o-mini',
    verbose = True,    
    backstory = ('You are an expert researcher, who can gather detailed information about a company. \
                  Consider you are on : '+Today),
    tools = [search_tool],
    cache = True,
    max_iter = 5
)

## Agent to specifically get financial data of the company.
data_explorer = Agent (
    role = 'data researcher',
    goal = 'Gather and provide financial data and company information about a stock',    
    # llm = 'groq/llama3-70b-8192',
    llm = 'gpt-4o-mini',
    verbose = True,    
    backstory = ("You are an expert researcher, who can gather detailed information about a company or stock. \
                  When you use the tools, add suffix '.NS' to symbol agrument. Consider you are on : "+Today),
    tools = [get_company_info, get_income_statements],
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
    backstory = ("You are an expert in analysing financial data of a company, stock / company related current inforamtionand make it into a analysis summary.\
                  You are making analyis about indian companies. Use indian units for numbers (lakh, crore) accordingly.\
                 Consider you are on "+Today),
)

## This is the expert who is going to make a call about investment.
fin_expert = Agent (
    role = 'Financial Expert',
    goal = 'Considering Financial analysis of a stock, make investment recommendation',    
    # llm = 'groq/llama3-70b-8192',
    llm = 'gpt-4o-mini',
    verbose = True,
    tools = [get_current_stock_price],
    max_iter = 5,
    backstory = ("You are an expert financial advisor who can provide investment recommendation.\
                 Consider the financial analysis, current information about company, current stock price \
                 and make recommendation whether to buy a stock or not.\
                 When you use the tools, add suffix '.NS' to symbol agrument.\
                 Consider you are on "+Today),
)
