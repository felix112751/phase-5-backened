from datetime import datetime
from . import db

class User(db.Model):
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    avatar = db.Column(db.String(255))
    role = db.Column(db.String(20), nullable=False)

class Book(db.Model):
    id = db.Column(db.String, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    cover_image = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(500), nullable=False)

class BookClub(db.Model):
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    cover_image = db.Column(db.String(255), nullable=False)
    created_by_id = db.Column(db.String, db.ForeignKey('user.id'), nullable=False)
    created_by = db.relationship('User', backref=db.backref('book_clubs', lazy=True))

class BookSummary(db.Model):
    id = db.Column(db.String, primary_key=True)
    book_id = db.Column(db.String, db.ForeignKey('book.id'), nullable=False)
    user_id = db.Column(db.String, db.ForeignKey('user.id'), nullable=False)
    club_id = db.Column(db.String, db.ForeignKey('book_club.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

