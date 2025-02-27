from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = 'f7c5c9f8a38456b8575e6d6c'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from market import routes

