from app import app
from flask import render_template

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/form")
def form():
    return render_template('form.html')
