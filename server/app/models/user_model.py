from app import db
from sqlalchemy.orm import validates
from flask import flash
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

class User(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    _password = db.Column("password", db.String(100), nullable=False)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, plaintext_password):
        self._password = bcrypt.generate_password_hash(plaintext_password).decode('utf-8')

    @validates('username')
    def validate_username(self, key, username):
        if not username:
            flash('Username cannot be empty', 'error')
            raise ValueError('Username cannot be empty')
        if len(username) < 5:
            flash('Username must be at least 5 characters', 'error')
            raise ValueError('Username must be at least 5 characters')
        # Add more username validations as needed
        return username

    @validates('password')
    def validate_password(self, key, password):
        if not password:
            flash('Password cannot be empty', 'error')
            raise ValueError('Password cannot be empty')
        if len(password) < 8:
            flash('Password must be at least 8 characters', 'error')
            raise ValueError('Password must be at least 8 characters')
        # Add more password validations as needed
        return password

    def check_password(self, plaintext_password):
        return bcrypt.check_password_hash(self._password, plaintext_password)

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self._password
        }