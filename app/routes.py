from flask import Blueprint, request, jsonify
from .models import db, User
from uuid import uuid4
import re

main = Blueprint('main', __name__)

def is_valid_email(email):
    """Helper function to validate email format"""
    email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    return re.match(email_regex, email)

@main.route('/users', methods=['POST'])
def create_user():
    data = request.get_json() 

    # Ensure all required fields are in the request
    if 'name' not in data or 'email' not in data or 'role' not in data:
        return jsonify({'message': 'Missing required fields'}), 400

    # Validate the email format
    if not is_valid_email(data['email']):
        return jsonify({'message': 'Invalid email format'}), 400

    # Create a new user instance
    user = User(
        id=str(uuid4()),  # Generate a new unique ID for the user
        name=data['name'],
        email=data['email'],
        role=data['role']
    )

    try:
        # Add the user to the session and commit to the database
        db.session.add(user)  
        db.session.commit()

        # Return the created user as a response (with the ID)
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
        # Handle any database errors
        db.session.rollback()
        return jsonify({'message': 'Failed to create user', 'error': str(e)}), 500
