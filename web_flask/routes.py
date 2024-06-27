from uuid import uuid4
from datetime import datetime
from web_flask.forms import RegistrationFrom, LoginForm
from flask import render_template, flash, redirect, url_for
from web_flask import app, db, bcrypt
from web_flask.models import User
from flask_login import login_user, current_user, logout_user
from web_flask.daily_verse import get_daily_verse
from apscheduler.schedulers.background import BackgroundScheduler
import atexit

daily_verse = ""
#for scheduled job
def fetch_and_store_daily_verse():
    global daily_verse
    daily_verse = get_daily_verse()

quiz_data = [
    {
        'id': str(uuid4()), 
        'question': "Is there one true GOD?",
        'answer': True
    }
]

@app.route("/")
def landing_page():
    return render_template("landing_page.html")

@app.route('/main')
def main():
    return render_template('main.html', quiz_data=quiz_data, daily_verse=daily_verse)

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

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('landing_page'))

scheduler = BackgroundScheduler()
scheduler.add_job(func=fetch_and_store_daily_verse, trigger="interval", hours=24)
scheduler.start()

atexit.register(lambda: scheduler.shutdown())

fetch_and_store_daily_verse()
