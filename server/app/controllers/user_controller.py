from flask import request, jsonify 
from app import db
from app.models.user_model import User
from sqlalchemy.exc import SQLAlchemyError
from werkzeug.security import generate_password_hash, check_password_hash
import logging


logging.basicConfig(level=logging.INFO)

def handle_error(e, status_code):
    logging.error(f'Error: {str(e)}')
    return jsonify({'error': str(e)}), status_code

def create_user():
    try:
        data = request.get_json()

        if 'username' not in data or 'password' not in data:
            return handle_error('Missing username or password in data fields', 400)
        
        hashed_password = generate_password_hash(data['password'], method='sha256')
        user = User(username=data['username'], password=hashed_password)

        db.session.add(user)
        db.session.commit()
        return jsonify(user.serialize()), 201
    except SQLAlchemyError as e:
        return handle_error(e, 500)

def get_user_by_username(username):
    try:
        user = User.query.filter_by(username=username).first()
        return user
    except SQLAlchemyError as e:
       
        return None


def get_users():
    try:
        users = User.query.all()
        return jsonify([user.serialize() for user in users]), 200
    except SQLAlchemyError as e:
        return handle_error(e, 400)

def get_user(id):
    try:
        user = User.query.filter_by(id=id).first()
        if user:
            return jsonify(user.serialize()), 200
        else:
            return jsonify({'error': 'User not found'}), 404
    except SQLAlchemyError as e:
        return handle_error(e, 400)

def update_user(id):
    try:
        user = User.query.get(id)
        if not user:
            return jsonify({'error': 'User not found'}), 404

        username = request.json.get('username')
        password = request.json.get('password')

        if username:
            user.username = username
        if password:
            user.password = generate_password_hash(password, method='sha256')

        db.session.commit()
        return jsonify({'message': 'User updated successfully'}), 200
    except SQLAlchemyError as e:
        return handle_error(e, 400)

def delete_user(id):
    try:
        user = User.query.get(id)
        if not user:
            return jsonify({'error': 'User not found'}), 404

        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted successfully'}), 200
    except SQLAlchemyError as e:
        return handle_error(e, 400)