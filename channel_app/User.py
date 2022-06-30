# model.py

import logging as lg
from flask_sqlalchemy import SQLAlchemy
from views import app

# Create database connection object
db = SQLAlchemy(app)

# models
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    sub = db.Column(db.Integer, nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    picture = db.Column(db.String(255))
    fullname = db.Column(db.String(255))

def init_db():
    db.drop_all()
    db.create_all()
    db.session.commit()
    lg.warning('Database initialized!')
