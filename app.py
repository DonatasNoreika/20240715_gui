from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/skaiciavimai")
def skaiciavimai():
    return render_template("skaiciavimai.html")

@app.route("/zmones")
def zmones():
    vardai = ["Jonas", "Antanas", "Petras"]
    return render_template("zmones.html", sarasas=vardai)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        vardas = request.form['vardas']
        return render_template("greetings.html", vardas=vardas)
    if request.method == "GET":
        return render_template("login.html")


# @app.route("/<name>")
# def user(name):
#     return f"Labas, {name}"


if __name__ == "__main__":
    app.run()