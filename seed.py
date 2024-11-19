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
        user2 = User(
            id=str(uuid4()),
            name='Bob Johnson',
            email='bob.johnson@example.com',
            role='user'
        )
        user3 = User(
            id=str(uuid4()),
            name='Carol White',
            email='carol.white@example.com',
            role='user'
        )
        user4 = User(
            id=str(uuid4()),
            name='David Brown',
            email='david.brown@example.com',
            role='admin'
        )
        user5 = User(
            id=str(uuid4()),
            name='Eve Williams',
            email='eve.williams@example.com',
            role='user'
        )

        # Create book clubs
        book_club1 = BookClub(
            id=str(uuid4()),
            name='Book Club 1',
            description='Description for Book Club 1',
            cover_image='https://example.com/cover1.jpg',
            created_by_id=user4.id
        )
        book_club2 = BookClub(
            id=str(uuid4()),
            name='Book Club 2',
            description='Description for Book Club 2',
            cover_image='https://example.com/cover2.jpg',
            created_by_id=user5.id