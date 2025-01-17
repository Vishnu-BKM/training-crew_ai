from crewai import Crew, Process, Task
from my_agents import news_info_explorer, data_explorer, analyst, fin_expert
from my_tasks import get_company_financials, get_company_news, analyse, advise
from datetime import datetime

## function to print Current time stamp
def timestamp(Input):
    print(datetime.now())

## Crew has 4 tasks to do. Its composed of 4 agents.
## Overall objective is to perform task of Making a investment advise about the stock
## Done by performing 4 tasks sequentially. Crew agents collaborate and achive the final result
crew = Crew (
    agents = [data_explorer, news_info_explorer, analyst, fin_expert],
    tasks = [get_company_financials, get_company_news, analyse, advise],
    verbose = True,
    Process = Process.sequential,
    step_callback = timestamp
)

result = crew.kickoff (inputs={'stock' : 'Hdfc Bank'})

#print (result)
