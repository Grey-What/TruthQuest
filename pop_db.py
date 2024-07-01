from web_flask import app, db
from web_flask.models import User, Verse, Quiz

""" print(Quiz.query.all())"""

with app.app_context(): 
    quizzes = [
        {"question": "Question 1True", "answer": True},
        {"question": "Question 2True", "answer": True},
        {"question": "Question 3True", "answer": True},
        {"question": "Question 4True", "answer": True},
        {"question": "Question 5False", "answer": False},
        {"question": "Question 6False", "answer": False},
        {"question": "Question 7False", "answer": False},
        {"question": "Question 8False", "answer": False},
    ]
    for quiz in quizzes:
        db.session.add(Quiz(**quiz))

    db.session.commit()








