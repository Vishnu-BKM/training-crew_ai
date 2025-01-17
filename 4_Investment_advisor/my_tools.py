from crewai.tools import tool
import json

## Import Yahoo Finance APIs
import yfinance as yf

## A function is defined, that will work as a tool and that is provided to the framework (hence to agents) as a tool with the '@tool' decorator
## Note the function description  (purpose, usage) in doc strigs.
@tool ("Get current stock price")
def get_current_stock_price(symbol: str) -> str:
    """Use this function to get the current stock price for a given symbol.

    Args:
        symbol (str): The stock symbol.

    Returns:
        str: The current stock price or error message.
    """
    try:
        stock = yf.Ticker(symbol)
        
        current_price = stock.info.get("regularMarketPrice", stock.info.get("currentPrice"))
        return f"{current_price:.2f}" if current_price else f"Could not fetch current price for {symbol}"
    except Exception as e:
        return f"Error fetching current price for {symbol}: {e}"

@tool
def get_company_info(symbol: str):
    """Use this function to get company information and current financial snapshot for a given stock symbol.

    Args:
        symbol (str): The stock symbol.

    Returns:
        JSON containing company profile and current financial snapshot.
    """
    try:
        company_info_full = yf.Ticker(symbol).info
        if company_info_full is None:
            return f"Could not fetch company info for {symbol}"

        company_info_cleaned = {
            "Name": company_info_full.get("shortName"),
            "Symbol": company_info_full.get("symbol"),
            "Current Stock Price": f"{company_info_full.get('regularMarketPrice', company_info_full.get('currentPrice'))} {company_info_full.get('currency', 'USD')}",
            "Market Cap": f"{company_info_full.get('marketCap', company_info_full.get('enterpriseValue'))} {company_info_full.get('currency', 'USD')}",
            "Sector": company_info_full.get("sector"),
            "Industry": company_info_full.get("industry"),
            "City": company_info_full.get("city"),
            "Country": company_info_full.get("country"),
            "EPS": company_info_full.get("trailingEps"),
            "P/E Ratio": company_info_full.get("trailingPE"),
            "52 Week Low": company_info_full.get("fiftyTwoWeekLow"),
            "52 Week High": company_info_full.get("fiftyTwoWeekHigh"),
            "50 Day Average": company_info_full.get("fiftyDayAverage"),
            "200 Day Average": company_info_full.get("twoHundredDayAverage"),
            "Employees": company_info_full.get("fullTimeEmployees"),
            "Total Cash": company_info_full.get("totalCash"),
            "Free Cash flow": company_info_full.get("freeCashflow"),
            "Operating Cash flow": company_info_full.get("operatingCashflow"),
            "EBITDA": company_info_full.get("ebitda"),
            "Revenue Growth": company_info_full.get("revenueGrowth"),
            "Gross Margins": company_info_full.get("grossMargins"),
            "Ebitda Margins": company_info_full.get("ebitdaMargins"),
        }
        return json.dumps(company_info_cleaned)
    except Exception as e:
        return f"Error fetching company profile for {symbol}: {e}"

@tool
def get_income_statements(symbol: str):

    """Use this function to get income statements for a given stock symbol.

    Args:
    symbol (str): The stock symbol.

    Returns:
    JSON containing income statements or an empty dictionary.
    """
    try:
        stock = yf.Ticker(symbol)
        financials = stock.financials
        return financials.to_json(orient="index")
    except Exception as e:
        return f"Error fetching income statements for {symbol}: {e}"
