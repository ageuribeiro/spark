import pyautogui as pag
from agents.main import Console

class Trading:
    def open_trading_app():
        Console.console.print("[bold green] * Iniciando a automação...[/bold green]")
        pag.hotkey("ctrl", "alt", "t") #abrir terminal
        pag.typewrite("google-chrome https://binance.com")
        pag.press("enter")

    def execute_trade():
        Console.console.print("[bold red]Realizando investimento...[/bold red]")
        pag.click(100,200)