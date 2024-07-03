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
    url = "https://beta.ourmanna.com/api/v1/get?format=json&order=daily"
    headers = {"accept": "application/json"}

    with app.app_context():
        response = requests.get(url, headers=headers)
        r = response.json()

        text = r['verse']['details']['text']
        reference = r['verse']['details']['reference']

        book = reference.split(' ')[0]
        chapter = int(reference.split(' ')[1].split(':')[0])
        verse = int(reference.split(' ')[1].split(':')[1])

            #add to desired sturcture
        daily_verse["bookname"] = book
        daily_verse["chapter"] = chapter
        daily_verse["verse"] = verse
        daily_verse["text"] = text
        daily_verse["date"] = datetime.now().strftime("%Y-%m-%d")

                #add to database
        db_verse = Verse(date=daily_verse["date"], book=daily_verse["bookname"], chapter=daily_verse["chapter"], verse=daily_verse["verse"], text=daily_verse["text"])
        db.session.add(db_verse)
        db.session.commit()
        print("test daily verse:\n {}".format(daily_verse))

    return daily_verse

"""
verse structure from api

{
  "verse": {
    "details": {
      "text": "My soul yearns for you in the night; in the morning my spirit longs for you. When your judgments come upon the earth, the people of the world learn righteousness.",
      "reference": "Isaiah 26:9",
      "version": "NIV",
      "verseurl": "http://www.ourmanna.com/"
    },
    "notice": "Powered by OurManna.com"
  }
}

desired structure to model
{
    "bookname": "Genesis",
    "chapter": 1,
    "verse": 1,
    "date": "2022-01-01",
    "text": "In the beginning was the Word, and the Word was with God, and the Word was God."
}
"""
