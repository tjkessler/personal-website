from src import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/research')
def research():
    return render_template('research.html')


@app.route('/projects')
def projects():
    return render_template('projects.html')
