from flask import Flask
import config
import os
from flask_sqlalchemy import SQLAlchemy
from app.flask_replicated import FlaskReplicated

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.SQLALCHEMY_TRACK_MODIFICATIONS
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
# app.config.from_pyfile('../config.py')

db = SQLAlchemy(app)
