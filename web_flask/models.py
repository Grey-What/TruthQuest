from web_flask import db, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    """return a user that match id"""
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        """print string representation of a user"""
        return "User('{}', '{}', '{}')".format(self.id, self.username, self.email)
 
class Quiz(db.Model, UserMixin):
    __tablename__ = 'quiz'

    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(256), nullable=False)
    answer = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        """print string representation of a quiz"""
        return "Quiz('{}', '{}', '{}')".format(self.id, self.question, self.answer)

class Verse(db.Model, UserMixin):
    __tablename__ = 'verses'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(64), nullable=False)
    book = db.Column(db.String(64), nullable=False)
    chapter = db.Column(db.Integer, nullable=False)
    verse = db.Column(db.Integer, nullable=False)
    text = db.Column(db.Text, nullable=False)

    def __repr__(self):
        """print string representation of a verse"""
        return "Verse('{}', '{}', '{}', '{}', '{}', '{}')".format(self.id, self.date, self.book, self.chapter, self.verse, self.text)
