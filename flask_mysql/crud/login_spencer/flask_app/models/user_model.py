from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
import re
EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")


class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.updated_at = data['updated_at']
        self.created_at = data['created_at']

        @classmethod
        def get_by_email(cls, data):
            query = """
      INSERT INTO user (first_name,last_name,email,password)
      VALIUES (%(first_name)s), %(last_name)s, %(email)s, %(password)s);
      """
            return connectToMySQL(DATABASE).query_db(query, data)

        @classmethod
        def get_by_id(cls, data):
            query = """
        SELECT * FROM users WHERE email = %(email)s;
        """
            results = connectToMySQL(DATABASE).query_db(query, data)
            if len(results) < 1:
                return False

            return cls(results[0])

        @staticmethod
        def validator(data):
            is_valid = True
            if len(data['first_name']) < 1:
                flash("First Name Required", "reg")
                is_valid = False
            if len(data['last_name']) < 1:
                flash("Last Name Required", "reg")
                is_valid = False
            if len(data['email']) < 1:
                flash("Email Required", "reg")
                is_valid = False
            elif not EMAIL_REGEX.match(data['email']):
                flash("Invalid Email", "reg")
                is_valid = False
            else:
                user_data = {
                  'email':data['email']
                }
                potential_user = User.get_by_email(user_data)
                if potential_user:
                  flash("Email already taken(hopefully by you!)")
                  is_valid = False
            if len(data['password']) < 1:
                flash("Password Required", "reg")
                is_valid = False
            elif data['password'] == data['confirm_pass']:
                flash("Passwords don't match", "reg")
                is_valid = False
            return is_valid


  #setting 'reg' as a category
  #setting 'log' as a category to be able to use for routes/jinja