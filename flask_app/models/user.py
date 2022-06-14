from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt
from flask_app import app
import re

bcrypt = Bcrypt(app)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data):
        self.id = data['id']
        self.user_name = data['user_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def register(cls, data):
        query = "INSERT INTO users (user_name, email, password, created_at, updated_at) VALUES (%(user_name)s, %(email)s, %(password)s, NOW(), NOW());"
        return connectToMySQL('shapelogschema').query_db(query, data)

    @classmethod
    def get_user_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL('shapelogschema').query_db(query, data)
        return result[0]

    @staticmethod
    def validate_registration(data):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        email = connectToMySQL('shapelogschema').query_db(query, data)

        if len(data['user_name']) < 3:
            flash("User name must be at least 3 characters", "registration_user_name")
            is_valid = False
        if not EMAIL_REGEX.match(data['email']):
            flash("Email is not valid", "registration_email")
            is_valid = False
        elif not len(email) == 0:
            flash("Email is already entered", "registration_email")
            is_valid = False
        if len(data['password']) < 8:
            flash("Password must be at least 8 characters", "registration_password")
            is_valid = False
        if not data['password'] == data['confirm_password']:
            flash("Passwords must match", "registration_confirm")
            is_valid = False
        return is_valid

    @staticmethod
    def validate_login(data):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL('shapelogschema').query_db(query, data)
        if len(results) > 0:
            user = results[0]
            print(user)
        if len(results) == 0:
            flash("No matching email", "login_email")
            is_valid = False
        elif not bcrypt.check_password_hash(user['password'], data['password']):
            flash("Incorrect password entered", "login_password")
            is_valid = False
        if is_valid:
            return user
        else: 
            return is_valid