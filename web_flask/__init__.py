from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = '7ea0b663144af24c7d5dff519b97ce54'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
"""app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://TQ_Admin:TruthQuest24@localhost/TruthQuest_db?auth_plugin=mysql_native_password'"""

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from web_flask.models import User, Quiz, Verse

with app.app_context():
    db.create_all()

from web_flask import routes
