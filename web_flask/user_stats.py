from flask_login import current_user
from web_flask.models import UserStats, User
from web_flask import db
from datetime import datetime, timedelta

def get_or_create_user_stats():
    if current_user.is_authenticated:
        user_stats = UserStats.query.filter_by(user_id=current_user.id).first()
        if not user_stats:
            user_stats = UserStats(user_id=current_user.id)
            db.session.add(user_stats)
            db.session.commit()
    else:
        user_stats = None
    return user_stats

def update_user_stats(user_stats):
    """keeps track of user streak and updates stat information"""
    today = datetime.utcnow().date()

    if user_stats.last_played < today:
        if user_stats.last_played < today - timedelta(days=1):
            user_stats.streak = 0

        user_stats.last_played = today
        user_stats.streak += 1
        db.session.commit()
