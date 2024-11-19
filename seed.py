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

        # Create Book Clubs
        club1 = BookClub(
            id=str(uuid4()),
            name='Fiction Fanatics',
            description='A community of fiction lovers exploring contemporary and classic novels together.',
            cover_image='https://images.unsplash.com/photo-1524995997946-a1c2e315a42f?auto=format&fit=crop&q=80',
            created_by_id=user4.id
        )
        club2 = BookClub(
            id=str(uuid4()),
            name='Mystery Readers',
            description='Unravelling mysteries and discussing thrilling detective stories.',
            cover_image='https://images.unsplash.com/photo-1481627834876-b7833e8f5570?auto=format&fit=crop&q=80',
            created_by_id=user2.id
        )
        club3 = BookClub(
            id=str(uuid4()),
            name='Self-Improvement Enthusiasts',
            description='For those who enjoy reading books that help them grow as individuals.',
            cover_image='https://images.unsplash.com/photo-1586916703502-0eae5b3708d9?auto=format&fit=crop&q=80',
            created_by_id=user3.id
        )

        # Add book clubs to the session and commit
        db.session.add_all([club1, club2, club3])
        db.session.commit()

        # Add members to clubs
        club1.members = [user1, user2, user4]
        club2.members = [user2, user3, user5]
        club3.members = [user3, user4, user5]

        # Commit the changes
        db.session.commit()

        # Add books to clubs

         # Create Book Summaries
        summary1 = BookSummary(
            id=str(uuid4()),
            book_id=book1.id,
            user_id=user1.id,
            club_id=club1.id,
            content='This book made me reflect on the choices I have made in life.',
            created_at=datetime.utcnow()
        )
        summary2 = BookSummary(
            id=str(uuid4()),
            book_id=book2.id,
            user_id=user2.id,
            club_id=club2.id,
            content='A brilliant mystery novel with many twists and turns!',
            created_at=datetime.utcnow()
        )
        summary3 = BookSummary(
            id=str(uuid4()),
            book_id=book3.id,
            user_id=user3.id,
            club_id=club3.id,
            content='A truly inspiring story about overcoming obstacles.',
            created_at=datetime.utcnow()
        )

        # Add book summaries to the session and commit
        db.session.add_all([summary1, summary2, summary3, summary4])
        db.session.commit()

        # Create Reviews
        review1 = Review(
            id=str(uuid4()),
            rating=5,
            comment='A masterpiece! One of my favorite books of all time.',
            user_id=user1.id,
            club_id=club.id,
            created_at=datetime.utcnow()
        )
        review2 = Review(
            id=str(uuid4()),
            rating=4,
            comment='Enjoyable read, but I figured out the mystery a bit too early.',
            user_id=user2.id,
            club_id=club2.id,
            created_at=datetime.utcnow()
        )
        review3 = Review(
            id=str(uuid4()),
            rating=5,
            comment='This book was life-changing for me!',
            user_id=user3.id,
            club_id=club3.id,
            created_at=datetime.utcnow()
        )

        # Add reviews to the session and commit
        db.session.add_all([review1, review2, review3])
        db.session.commit()

        print('Database seeded successfully.')

if __name__ == '__main__':
    seed_data()

        