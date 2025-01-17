## bring your agents here
from crewai import Task
from my_agents import news_info_explorer, data_explorer, analyst, fin_expert

## distinct tasks are defined here. Each task with a specific description and expected output.
## Check the variable, which is same parameter while triggering.

## A task to get the financial data of the stock. expected output is defined qualitatively
## An agent, who has relevant capability is assigned to the task
get_company_financials = Task (
                                description = "Get financial data like inccome statements and other fundamental ratios for stock : {stock}",
                                expected_output = "Detailed information from income statement,  key ratios for {stock}.\
                                                   Indicate also about current financial status and trend over the period.",
                                agent = data_explorer
                              )

## Task to get focused news about the company and business
get_company_news = Task (
                                description = "Get latest news and business information about company : {stock}",
                                expected_output = "Latest news and business information about company.\
                                                   Provide a summary also.",
                                agent = news_info_explorer
                              )

## A task make analysis from financial data and news. Expected output sets clear expectation
analyse = Task (
                    description = "Make thorough analysis based on given financial data and latest news of a stock",
                    expected_output = "Comprehensive Analysis of a stock outlining financial health, stock valuation, risks and news.\
                                        Mention currency information and number units in indian context (lakh / crore)",    
                    agent = analyst,
                    context = [get_company_financials, get_company_news],
                    output_file = 'Analysis.md'
                )

## Advisor task
advise = Task (
                    description = "Make a recommendation about investing in a stock, based on analysis provided and current stock price. State the reasons.",
                    expected_output = "Recommendation (Buy / No Buy) of a stock, with reasons clearly mentioned",    
                    agent = fin_expert,                    
                    context = [analyse],
                    output_file = 'Recommendation.md'
                )