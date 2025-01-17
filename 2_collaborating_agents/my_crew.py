from crewai import Crew, Process, Task
from my_agents import explorer, synthesiser
from my_tasks import explore, summarise
from datetime import datetime

## function to print Current time stamp
def timestamp(Input):
    print(datetime.now())

## Crew has two tasks to do. Its composed of two agents.
## Overall objective is to perform task of gather info and summarise.
## Done by performing 2 tasks sequentially. Crew agents collaborate and achive the final result
crew = Crew (
    agents = [explorer, synthesiser],
    tasks = [explore, summarise],
    verbose = True,
    Process = Process.sequential,
    step_callback = timestamp
)

result = crew.kickoff (inputs={'topic' : 'AI in software industry'})
# result = crew.kickoff (inputs={'topic' : 'Role of Indian IT industry in AI field'})
# result = crew.kickoff (inputs={'topic' : 'is TCS leveraging on AI for its business growth?'})

#print (result)
