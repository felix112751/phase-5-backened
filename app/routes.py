from flask import Blueprint, request, jsonify
from .models import db, User, Book, BookClub, BookSummary, Review
from uuid import uuid4
import re
from datetime import datetime

main = Blueprint('main', __name__)

def is_valid_email(email):
    """Helper function to validate email format"""
    email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    return re.match(email_regex, email)



@main.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if 'name' not in data or 'email' not in data or 'role' not in data:
        return jsonify({'message': 'Missing required fields'}), 400

    if not is_valid_email(data['email']):
        return jsonify({'message': 'Invalid email format'}), 400

    user = User(
        id=str(uuid4()),  
        name=data['name'],
        email=data['email'],
        role=data['role']
    )

    try:
        db.session.add(user)
        db.session.commit()
        return jsonify({
            'message': 'User created successfully',
            'user': {
                'id': user.id,
                'name': user.name,
                'email': user.email,
                'role': user.role
            }
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Failed to create user', 'error': str(e)}), 500

@main.route('/users', methods=['GET'])
def get_users():
    try:
        users = User.query.all()
        users_list = [{
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'role': user.role
        } for user in users]
        return jsonify(users_list)
    except Exception as e:
        return jsonify({'message': 'Failed to fetch users', 'error': str(e)}), 500

@main.route('/users/<id>', methods=['GET'])
def get_user(id):
    try:
        user = User.query.get_or_404(id)
        return jsonify({
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'role': user.role
        })
    except Exception as e:
        return jsonify({'message': 'Failed to fetch user', 'error': str(e)}), 500

@main.route('/users/<id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()

    if 'name' not in data or 'email' not in data or 'role' not in data:
        return jsonify({'message': 'Missing required fields'}), 400

    if not is_valid_email(data['email']):
        return jsonify({'message': 'Invalid email format'}), 400

    try:
        user = User.query.get_or_404(id)

        user.name = data['name']
        user.email = data['email']
        user.role = data['role']

        db.session.commit()

        return jsonify({
            'message': 'User updated successfully',
            'user': {
                'id': user.id,
                'name': user.name,
                'email': user.email,
                'role': user.role
            }
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Failed to update user', 'error': str(e)}), 500

@main.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    try:
        user = User.query.get_or_404(id)
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted successfully'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Failed to delete user', 'error': str(e)}), 500



@main.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    if 'title' not in data or 'author' not in data or 'description' not in data:
        return jsonify({'message': 'Missing required fields'}), 400

    book = Book(
        id=str(uuid4()),
        title=data['title'],
        author=data['author'],
        cover_image=data.get('cover_image', ''),
        description=data['description']
    )

    try:
        db.session.add(book)
        db.session.commit()
        return jsonify({
            'message': 'Book created successfully',
            'book': {
                'id': book.id,
                'title': book.title,
                'author': book.author,
                'cover_image': book.cover_image,
                'description': book.description
            }
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Failed to create book', 'error': str(e)}), 500

@main.route('/books', methods=['GET'])
def get_books():
    try:
        books = Book.query.all()
        books_list = [{
            'id': book.id,
            'title': book.title,
            'author': book.author,
            'cover_image': book.cover_image,
            'description': book.description
        } for book in books]
        return jsonify(books_list)
    except Exception as e:
        return jsonify({'message': 'Failed to fetch books', 'error': str(e)}), 500

@main.route('/books/<id>', methods=['GET'])
def get_book(id):
    try:
        book = Book.query.get_or_404(id)
        return jsonify({
            'id': book.id,
            'title': book.title,
            'author': book.author,
            'cover_image': book.cover_image,
            'description': book.description
        })
    except Exception as e:
        return jsonify({'message': 'Failed to fetch book', 'error': str(e)}), 500

@main.route('/books/<id>', methods=['PUT'])
def update_book(id):
    data = request.get_json()

    if 'title' not in data or 'author' not in data or 'description' not in data:
        return jsonify({'message': 'Missing required fields'}), 400

    try:
        book = Book.query.get_or_404(id)

        book.title = data['title']
        book.author = data['author']
        book.cover_image = data.get('cover_image', '')
        book.description = data['description']

        db.session.commit()

        return jsonify({
            'message': 'Book updated successfully',
            'book': {
                'id': book.id,
                'title': book.title,
                'author': book.author,
                'cover_image': book.cover_image,
                'description': book.description
            }
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Failed to update book', 'error': str(e)}), 500

@main.route('/books/<id>', methods=['DELETE'])
def delete_book(id):
    try:
        book = Book.query.get_or_404(id)
        db.session.delete(book)
        db.session.commit()
        return jsonify({'message': 'Book deleted successfully'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Failed to delete book', 'error': str(e)}), 500



@main.route('/bookclubs', methods=['POST'])
def create_book_club():
    data = request.get_json()
    if 'name' not in data or 'description' not in data or 'created_by_id' not in data:
        return jsonify({'message': 'Missing required fields'}), 400

    book_club = BookClub(
        id=str(uuid4()),
        name=data['name'],
        description=data['description'],
        cover_image=data.get('cover_image', ''),
        created_by_id=data['created_by_id']
    )

    try:
        db.session.add(book_club)
        db.session.commit()
        return jsonify({
            'message': 'Book Club created successfully',
            'book_club': {
                'id': book_club.id,
                'name': book_club.name,
                'description': book_club.description,
                'cover_image': book_club.cover_image
            }
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Failed to create book club', 'error': str(e)}), 500

@main.route('/bookclubs', methods=['GET'])
def get_book_clubs():
    try:
        book_clubs = BookClub.query.all()
        book_clubs_list = [{
            'id': club.id,
            'name': club.name,
            'description': club.description,
            'cover_image': club.cover_image
        } for club in book_clubs]
        return jsonify(book_clubs_list)
    except Exception as e:
        return jsonify({'message': 'Failed to fetch book clubs', 'error': str(e)}), 500

@main.route('/bookclubs/<id>', methods=['GET'])
def get_book_club(id):
    try:
        club = BookClub.query.get_or_404(id)
        return jsonify({
            'id': club.id,
            'name': club.name,
            'description': club.description,
            'cover_image': club.cover_image
        })
    except Exception as e:
        return jsonify({'message': 'Failed to fetch book club', 'error': str(e)}), 500

@main.route('/reviews', methods=['POST'])
def create_review():
    data = request.get_json()
    if 'book_id' not in data or 'user_id' not in data or 'rating' not in data or 'review' not in data:
        return jsonify({'message': 'Missing required fields'}), 400

    review = Review(
        id=str(uuid4()),
        book_id=data['book_id'],
        user_id=data['user_id'],
        rating=data['rating'],
        review=data['review'],
        created_at=datetime.utcnow()
    )

    try:
        db.session.add(review)
        db.session.commit()
        return jsonify({
            'message': 'Review created successfully',
            'review': {
                'id': review.id,
                'book_id': review.book_id,
                'user_id': review.user_id,
                'rating': review.rating,
                'review': review.review,
                'created_at': review.created_at
            }
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Failed to create review', 'error': str(e)}), 500

