## bring your agents here
from crewai import Task
from my_agents import content_explorer, analyst, fin_expert

## 3 distinct tasks are defined here. Each task with a specific description and expected output.
## Check the variable, which is same parameter while triggering.

## A task to get company financial details from internet. expected output is defined to indicate what data is required
## An agent, who has relevant capability is assigned to the task
get_company_financials = Task (
                                description = "Get latest financial data for stock : {stock}",
                                expected_output = "Latest data about balance sheet, cash flow,  profit for stock {stock}",    
                                agent = content_explorer
                              )

## A task to Analyse the data. Expected output sets clear expectation. Also, context indicates which task provides input for this one.
Anlayse = Task (
                    description = "Make thorough analysis based on given financial data of a stock",
                    expected_output = "Comprehensive Analysis of a stock outlining financial health, stock valuation and risks",    
                    agent = analyst,
                    context = [get_company_financials],
                    output_file = 'Analysis.txt'
                )

## A Task that makes final recommendation and reasoning
Advise = Task (
                    description = "Make a recommendation about investing in a stock, based on analysis provided",
                    expected_output = "Recommendation (Buy / No Buy) of a stock, with reasons clearly mentioned",    
                    agent = analyst,                    
                    context = [Anlayse],
                    output_file = 'Recommendation.txt'
                )