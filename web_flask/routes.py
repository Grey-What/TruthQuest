from uuid import uuid4
from datetime import datetime
from web_flask.forms import RegistrationFrom, LoginForm
from flask import render_template, flash, redirect, url_for
from web_flask import app, db, bcrypt
from web_flask.models import User
from flask_login import login_user, current_user

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
    if current_user.is_authenticated:
        return redirect(url_for('main'))
    form = RegistrationFrom()
    if form.validate_on_submit():
        hashed_pass = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_pass)
        db.session.add(user)
        db.session.commit()
        flash('Account Registration has been succesful!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', tile='Register', form=form)

@app.route('/login', methods=('GET', 'POST'))
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main'))
    form = LoginForm()
    if form.validate_on_submit():
           user = User.query.filter_by(email=form.email.data).first()
           if user and bcrypt.check_password_hash(user.password, form.password.data):
               login_user(user, remember=form.remember.data)
               return redirect(url_for('main'))
           else:
                flash("Login unsuccessful. Please check email and password", 'danger')
    return render_template('login.html', tile='Login', form=form)