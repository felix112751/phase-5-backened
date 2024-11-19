from flask import Blueprint, request, jsonify
from .models import db, User
from uuid import uuid4

main = Blueprint('main', _name_)


@main.route('/users', methods=['POST'])
def create_user():
    data = request.get_json() 
    user = User(
        id=str(uuid4()),  # Generate a new unique ID for the user
        name=data['name'],
        email=data['email'],
        role=data['role']
    )
    db.session.add(user)  # Add the user to the session
    db.session.commit()   # Commit the transaction to the database
    return jsonify({'message': 'User created successfully'}), 201