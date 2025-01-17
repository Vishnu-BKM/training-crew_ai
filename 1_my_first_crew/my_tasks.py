from crewai import Task

## Import your agents
from my_agents import chat_bot

## Defining a Task. Provide task description and expected output. Associate the agent who will do it
## Parameter is in {}, which will be user input
chat_task = Task (
    description = ('{query}'),
    expected_output = 'A response to {query}',
    agent = chat_bot,
)