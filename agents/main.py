import pyfiglet
from rich.console import Console
from rich.progress import Progress
from agent_orchestrator import Trading

console = Console()

class Console():
    
    def display_logo():
        logo = pyfiglet.figlet_format("AutoInvest")
        console.print(f'[bold blue]{logo}[/bold blue]')

    def show_progress(task_name):
        with Progress() as progress:
            task = progress.add_task(task_name, total=100)
            for i in range(100):
                progress.update(task, advance=1)

Trading.open_trading_app()
Trading.execute_trade()