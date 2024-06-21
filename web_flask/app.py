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

db = SQLAlchemy(app)

"""to be moved"""
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        """print string representation of a user"""
        return "User('{}', '{}', '{}')".format(self.id, self.username, self.email)

 """to be moved"""   
class Quiz(db.Model):
    __tablename__ = 'quiz'

    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(256), nullable=False)
    answer = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        """print string representation of a quiz"""
        return "Quiz('{}', '{}', '{}')".format(self.id, self.question, self.answer)

"""to be moved"""
class Verse(db.Model):
    __tablename__ = 'verses'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default = datetime.utcnow, nullable=False)
    book = db.Column(db.String(64), nullable=False)
    chapter = db.Column(db.Integer, nullable=False)
    verse = db.Column(db.Integer, nullable=False)
    text = db.Column(db.String(256), nullable=False)

    def __repr__(self):
        """print string representation of a verse"""
        return "Verse('{}', '{}', '{}', '{}', '{}', '{}')".format(self.id, self.date, self.book, self.chapter, self.verse, self.text)


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
