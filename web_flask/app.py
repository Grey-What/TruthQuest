#!/usr/bin/python3
""" Start TruthQuest web application"""
from flask import Flask, render_template, flash, redirect, url_for
from web_flask.forms import RegistrationFrom, LoginForm
from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4
from datetime import datetime

app = Flask(__name__)

app.config['SECRET_KEY'] = '7ea0b663144af24c7d5dff519b97ce54'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://TQ_Admin:TruthQuest24@localhost/TruthQuest_db'

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
    return render_template("landing_page.html")

@app.route('/main')
def main():
    return render_template('main.html', quiz_data=quiz_data, daily_truth=daily_truth)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/register', methods=('GET', 'POST'))
def register():
   form = RegistrationFrom()
   if form.validate_on_submit():
       flash('Welcome {}'.format(form.username.data), 'success')
       return redirect(url_for('main'))
   return render_template('register.html', tile='Register', form=form)

@app.route('/login', methods=('GET', 'POST'))
def login():
   form = LoginForm()
   if form.validate_on_submit():
       if form.email.data == 'greywhat2002@gmail.com' and form.password.data == '2002':
           flash('You have been logged in!', 'success')
           return redirect(url_for('main'))
       else:
           flash("Login unsuccessful. Please check username and password", 'danger')
   return render_template('login.html', tile='Login', form=form)


if __name__ == "__main__":
    app.run(debug=True)
