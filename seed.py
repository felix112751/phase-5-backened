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

        # Add users to the session and commit
        db.session.add_all([user1, user2, user3, user4, user5])
        db.session.commit()

       # Create Books
        book1 = Book(
            id=str(uuid4()),
            title='The Midnight Library',
            author='Matt Haig',
            cover_image='https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?auto=format&fit=crop&q=80',
            description='A story about a woman who discovers a magical library that allows her to explore different versions of the past.'
        )
        book2 = Book(
            id=str(uuid4()),
            title='The Thursday Murder Club',
            author='Richard Osman',
            cover_image='https://images.unsplash.com/photo-1543002588-bfa74002ed7e?auto=format&fit=crop&q=80',
            description='A mystery novel about a group of seniors who form a detective club to solve a murder case.'
        )
        book3 = Book(
            id=str(uuid4()),
            title='Educated',
            author='Tara Westover',
            cover_image='https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&q=80',
            description='A memoir about a woman who grew up in a survivalist family and went on to become a teacher.'
        )
        book4 = Book(
            id=str(uuid4()),
            title='Atomic Habits',
            author='James Clear',
            cover_image='https://images.unsplash.com/photo-1586993197628-2e6e5f029c98?auto=format&fit=crop&q=80',
            description='A self-help book about how small changes in behavior can lead to significant improvements in life.'
        )
        book5 = Book(
            id=str(uuid4()),
            title='The Silent Patient',
            author='Alex Michaelides',
            cover_image='https://images.unsplash.com/photo-1583986846791-d0ebefb2315c?auto=format&fit=crop&q=80',
            description='A psychological thriller about a famous painter who shoots her husband and then remains silent.'
        )

        # Add books to the session and commit
        db.session.add_all([book1, book2, book3, book4, book5])
        db.session.commit()
            