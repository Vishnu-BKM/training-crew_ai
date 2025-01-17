from crewai import Agent

## Defining an agent. Give it a role and purpose.
## 'llm' need to indicate LLM model to be used. By default, it considers OpenAI
chat_bot = Agent (
    role = 'Responder to Queries',
    goal = 'Provide a response to {query}',
    llm = 'groq/llama3-70b-8192',
    verbose = True,    
    backstory = ('A generalist having broad view about various topics, you will be able to answer to the queries, questions or statements'),
)