from datetime import datetime
from . import db

class User(db.Model):
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    avatar = db.Column(db.String(255))
    role = db.Column(db.String(20), nullable=False)

