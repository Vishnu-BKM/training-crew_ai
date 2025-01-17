## bring your agents here
from crewai import Task
from my_agents import explorer, synthesiser

## 2 distint tasks are defined here. Each task with a specific description and expected output.
## Check the variable, which is same parameter while triggering.

## A task to explore information about a 'topic'. expected output is defined qualitatively
## An agent, who has relevant capability is assigned to the task
explore = Task (
    description = ('Explore and gather information about topic : {topic}'),
    expected_output = 'Information from various sources and aspect about {topic}',    
    agent = explorer,
)

## A task to summarise. Expected output sets clear expectation
summarise = Task (
    description = ('Summarise provided information'),
    expected_output = 'Simple, concise, synthetic summary of provided information',    
    agent = synthesiser,    
)