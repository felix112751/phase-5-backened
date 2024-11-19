from app import create_app, db
from app.models import User, BookClub, Book, BookSummary, Review
from uuid import uuid4
from datetime import datetime

app = create_app()

def seed_data():
    with app.app_context():

        # Create users
        user1 = User(
            id=str(uuid4()),
            name='Alice Smith',
            email='alice.smith@example.com',
            role='user'
        )