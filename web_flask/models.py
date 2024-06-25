from web_flask import db
from datetime import datetime

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
