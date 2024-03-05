# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sobre", methods=["GET", "POST"])
def sobre(nome=None):
    if request.method == "POST":
        nome = request.form.get("nome")
    return render_template("sobre.html", nome=nome)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)