import requests
from web_flask import db, app
from web_flask.models import Verse, Quiz
from datetime import datetime
from sqlalchemy.sql import func

def get_daily_quizzes():
    """get a daily quiz database"""
    with app.app_context():
        today = datetime.utcnow().date()
        quizzes = Quiz.query.filter(func.date(Quiz.date_added)==today).order_by(func.random()).limit(5).all()
        print(quizzes)
    return quizzes

def get_daily_verse():
    """get a daily verse from bible api and save to db"""
    daily_verse = {}

    with app.app_context():
        response = requests.get("https://labs.bible.org/api/?passage=votd&formatting=plain&type=json")
        verse = response.json()

        #add to desired sturcture
        daily_verse["bookname"] = verse[0]["bookname"]
        daily_verse["chapter"] = verse[0]["chapter"]
        daily_verse["verse"] = verse[0]["verse"]
        daily_verse["text"] = verse[0]["text"]
        daily_verse["date"] = datetime.now().strftime("%Y-%m-%d")

        #add to database
        db_verse = Verse(date=daily_verse["date"], book=daily_verse["bookname"], chapter=daily_verse["chapter"], verse=daily_verse["verse"], text=daily_verse["text"])
        db.session.add(db_verse)
        db.session.commit()

    return daily_verse

"""
verse structure from api

[{
    "bookname": "Genesis",
    "chapter": 1,
    "verse": 1,
    "text": "In the beginning was the Word, and the Word was with God, and the Word was God."
}]

desired structure to model
{
    "bookname": "Genesis",
    "chapter": 1,
    "verse": 1,
    "date": "2022-01-01",
    "text": "In the beginning was the Word, and the Word was with God, and the Word was God."
}
"""
