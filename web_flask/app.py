#!/usr/bin/python3
""" Start TruthQuest web application"""
from flask import Flask, render_template


app = Flask(__name__)



@app.route("/")
def main_page():
    return render_template("test_index.html")

@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
