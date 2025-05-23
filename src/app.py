from flask import Flask, render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/research")
def research():
    return render_template("research.html")


@app.route("/projects")
def projects():
    return render_template("projects.html")
