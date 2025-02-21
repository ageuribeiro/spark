from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    msg = "Olá, Mundo!"
    
    return render_template("index.html", texto=msg)


if __name__ == "__main__":
    app.run(debug=True)
