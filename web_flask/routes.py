"""module contains routes of web application and servers as the main file for the web application"""
from uuid import uuid4
from datetime import datetime
from web_flask.forms import RegistrationFrom, LoginForm
from flask import render_template, flash, redirect, url_for, session, request
from web_flask import app, db, bcrypt
from web_flask.models import User, Quiz
from flask_login import login_user, current_user, logout_user
from web_flask.daily_objects import get_daily_verse, get_daily_quizzes
from apscheduler.schedulers.background import BackgroundScheduler
import atexit
from sqlalchemy.sql import func
from web_flask.user_stats import get_or_create_user_stats, update_user_stats

daily_verse = ""
daily_quizzes = []

"""for scheduled job"""
def fetch_and_store_daily_verse():
    global daily_verse
    daily_verse = get_daily_verse()

def fetch_and_store_daily_quizzes():
    global daily_quizzes
    daily_quizzes = get_daily_quizzes()

@app.route("/TruthQuest", strict_slashes=False)
@app.route("/", strict_slashes=False)
def landing_page():
    """return landing page"""
    return render_template("landing_page.html")

@app.route('/main', methods=['GET', 'POST'], strict_slashes=False)
def main():
    """Return main page with quizzes, user stats and daily verse"""
    global daily_quizzes
    user_stats = get_or_create_user_stats()
    current_date = datetime.utcnow().date()

    last_quiz_date = session.get('last_quiz_date')
    if last_quiz_date is None or datetime.strptime(last_quiz_date, '%Y-%m-%d').date() != current_date:
        session['quiz_index'] = 0
        session['quiz_answered'] = False
        session['quiz_answer'] = None
        session['last_quiz_date'] = current_date.strftime('%Y-%m-%d')
        session['daily_quizzes'] = [quiz.id for quiz in daily_quizzes]

    #for user stats
    if current_user.is_authenticated:
        update_user_stats(user_stats)

    if 'daily_quizzes' not in session:
        session['daily_quizzes'] = [quiz.id for quiz in daily_quizzes]

    quiz_index = session.get('quiz_index', 0)
    quizzes = Quiz.query.filter(Quiz.id.in_(session['daily_quizzes'])).all()
    
    quiz_complete = quiz_index >= len(quizzes)

    if quiz_complete:
      current_quiz = None
    else:
      current_quiz = quizzes[quiz_index]
    
    return render_template('main.html', quiz=current_quiz,
                           index=quiz_index + 1, daily_verse=daily_verse,
                           quiz_answered=session['quiz_answered'],
                           quiz_answer=session['quiz_answer'],
                           quiz_complete=quiz_complete,
                           user_stats=user_stats)

@app.route('/next_quiz', methods=['POST'], strict_slashes=False)
def next_quiz():
    """This function is called when user submits a quiz answer and updates the daily quiz to the next"""
    user_answer = request.form.get('answer')

    if user_answer:
        # Store user's answer and check correctness
        session['quiz_answer'] = user_answer
        session['quiz_answered'] = True

    quiz_index = session.get('quiz_index', 0)
    daily_quizzes = session.get('daily_quizzes', [])
    quizzes = Quiz.query.filter(Quiz.id.in_(daily_quizzes)).all()

    if quiz_index < len(quizzes):
        quiz = quizzes[quiz_index]

        if current_user.is_authenticated:
            user_stats = get_or_create_user_stats()
            if (user_answer == 'True' and quiz.answer) or (user_answer == 'False' and not quiz.answer):
                user_stats.correct_answers += 1

        # Move to the next quiz index if user submits 'Next Quiz'
        if 'next_quiz' in request.form:
            session['quiz_index'] += 1
            session['quiz_answered'] = False
            session['quiz_answer'] = None

            if current_user.is_authenticated:
                user_stats.quizzes_completed += 1

        db.session.commit()

    if session['quiz_index'] >= len(quizzes):
        return redirect(url_for('main'))
    
    return redirect(url_for('main'))

@app.route("/about", strict_slashes=False)
def about():
    """return about page"""
    return render_template("about.html")

@app.route('/register', methods=('GET', 'POST'), strict_slashes=False)
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

@app.route('/login', methods=('GET', 'POST'), strict_slashes=False)
def login():
    """return login page for users"""
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

@app.route('/logout', strict_slashes=False)
def logout():
    """retruns logout page for logged in users"""
    logout_user()
    return redirect(url_for('landing_page'))

"""Schedulers to run to retrieve and update daily quizzes and verses"""
scheduler = BackgroundScheduler()
scheduler.add_job(func=fetch_and_store_daily_quizzes, trigger="interval", hours=24)
scheduler.add_job(func=fetch_and_store_daily_verse, trigger="interval", hours=24)
scheduler.start()

atexit.register(lambda: scheduler.shutdown())

fetch_and_store_daily_verse()
fetch_and_store_daily_quizzes()
