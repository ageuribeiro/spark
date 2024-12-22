from sklearn.linear_model import LinearRegression
import numpy as np
from agents.main import Console

def analyze_market(data):
    Console.console("[bold cyan]Analisando o mercado...[/bold cyan]")
    model = LinearRegression()
    X = np.array(range(len(data))).reshape(-1,1)
    y = data["Close"].values
    model.fit(X,y)
    return model.predict([[len(data) + 1]]) 
    