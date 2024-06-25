from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = '7ea0b663144af24c7d5dff519b97ce54'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
"""app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://TQ_Admin:TruthQuest24@localhost/TruthQuest_db?auth_plugin=mysql_native_password'"""

db = SQLAlchemy(app)

from web_flask import routes
