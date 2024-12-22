import yfinance as yf
from agents.main import Console

def get_market_data(ticker="AAPL"):
    Console.console.print("[bold yellow]Coletando dados do ticker AAPL...[/bold yellow]")
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1d")
    Console.console.print(hist)