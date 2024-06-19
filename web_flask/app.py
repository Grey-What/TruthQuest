#!/usr/bin/python3
""" Start TruthQuest web application"""
from flask import Flask, render_template
from uuid import uuid4
from datetime import datetime


app = Flask(__name__)

quiz_data = [
    {
        'id': str(uuid4()),
        'question': "Is there one true GOD?",
        'answer': True
    }
]

daily_truth = [ 
    {
        'id': str(uuid4()),
        'date': str(datetime.now()),
        'book': 'John',
        'chapter': '16',
        'verse': '33',
        'text': "In the world you will have tribulation. But take heart; I have overcome the world."
    }
]

@app.route("/")
def landing_page():
    return render_template("index.html")

@app.route('/main')
def main_page():
    return render_template('main.html', quiz_data=quiz_data, daily_truth=daily_truth)

@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
