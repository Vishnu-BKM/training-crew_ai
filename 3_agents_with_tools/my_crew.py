from crewai import Crew, Process, Task
from my_agents import content_explorer, analyst, fin_expert
from my_tasks import get_company_financials, Anlayse, Advise
from datetime import datetime

## function to print Current time stamp
def timestamp(Input):
    print(datetime.now())

## The Crew playes the role of financial advisor (with current data taken from internet, make analysis and recommend)
## Crew has is composed of agents and tasks to achive the purpose
## Done by performing 3 tasks sequentially. Crew agents collaborate and achive the final result
crew = Crew (
    agents = [content_explorer, analyst, fin_expert],
    tasks = [get_company_financials, Anlayse, Advise],
    verbose = True,
    Process = Process.sequential,
    step_callback = timestamp
)

result = crew.kickoff (inputs={'stock' : 'Tata Steel'})

#print (result)
