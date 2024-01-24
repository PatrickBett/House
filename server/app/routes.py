from flask import Blueprint, request, jsonify
from app.controllers.user_controller import create_user, get_users, get_user, update_user, delete_user ,get_user_by_username
from app.controllers.house_controller import create_house, get_houses, get_house, update_house, delete_house
from app.controllers.review_controller import create_review, get_reviews, get_review, update_review, delete_review
from app.models.user_model import User

bp = Blueprint('bp', __name__)

@bp.route('/user', methods=['POST'])
def add_user():
    """Create a new user."""
    data = request.json
    username = data.get('username', '')

    # Check if the username already exists
    existing_user = get_user_by_username(username)
    if existing_user:
        return jsonify({'message': 'Error: Username already exists. Please choose another username.'}), 400

    # Check if the username length is valid
    if len(username) < 5:
        return jsonify({'message': 'Error: Username must be at least 5 characters.'}), 400

    # If username is unique and length is okay, proceed with user creation
    response, status_code = create_user()
    return jsonify(response), status_code


@bp.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username', '')
    password = data.get('password', '')

    # Find the user by username
    user = get_user_by_username(username)

    if user and user.check_password(password):
        
        return jsonify({'message': 'Login successful'}), 200
    
    else:
        return jsonify({'message': 'Invalid username or password'}), 401
    
   

@bp.route('/user', methods=['GET'])
def get_users_route():
    """Get all users."""
    return get_users()

@bp.route('/user/<int:id>')
def get_user_route(id):
    """Get a specific user by ID."""
    return get_user(id)

@bp.route('/user/<int:id>', methods=['PUT', 'PATCH'])
def update_user_route(id):
    """Update a user by ID."""
    return update_user(id)

@bp.route('/user/<int:id>', methods=['DELETE'])
def delete_user_route(id):
    """Delete a user by ID."""
    return delete_user(id)

# House routes


@bp.route('/house', methods=['POST'])
def add_house_route():
    """Create a new house."""
    return create_house()

@bp.route('/house')
def get_houses_route():
    """Get all houses."""
    return get_houses()

@bp.route('/house/<int:id>')
def get_house_route(id):
    """Get a specific house by ID."""
    return get_house(id)

@bp.route('/house/<int:id>', methods=['PUT', 'PATCH'])
def update_house_route(id):
    """Update a house by ID."""
    return update_house(id)

@bp.route('/house/<int:id>', methods=['DELETE'])
def delete_house_route(id):
    """Delete a house by ID."""
    return delete_house(id)

# Review routes
# (Similar structure for other resource routes)

@bp.route('/review', methods=['POST'])
def add_review_route():
    """Create a new review."""
    return create_review()

@bp.route('/review')
def get_reviews_route():
    """Get all reviews."""
    return get_reviews()

@bp.route('/review/<int:id>')
def get_review_route(id):
    """Get a specific review by ID."""
    return get_review(id)

@bp.route('/review/<int:id>', methods=['PUT', 'PATCH'])
def update_review_route(id):
    """Update a review by ID."""
    return update_review(id)

@bp.route('/review/<int:id>', methods=['DELETE'])
def delete_review_route(id):
    """Delete a review by ID."""
    return delete_review(id)