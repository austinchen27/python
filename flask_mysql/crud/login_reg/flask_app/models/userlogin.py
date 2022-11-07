from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User:
  def __init__(self,data):
    self.id = data['id']
    self.first_name = data['first_name']
    self.last_name = data['last_name']
    self.email = data['email']
    self.password = data['password']
    self.created_at = data['updated_at']
    self.updated_at = data['created_at']
    
  @classmethod
  def create(cls,data):
    query = """
    INSERT INTO users (first_name, last_name, email, password)
    VALUES (%(first_name)s, %(last_name)s, %(emails), %(password)s);
    """
    return connectToMySQL(DATABASE).query_db(query,data)

  @classmethod
  def get_by_email(cls,data):
    query = """
      SELECT * FROM users WHERE email = %(email)s;
    """
    result = connectToMySQL(DATABASE).query_db(query,data)
    if len(results) < 1:
      return False

    return cls(results[0])

  @classmethod
  def get_by_id(cls,data):
    query = """
      SELECT * FROM users WHERE email = %(email)s;
    """
    result = connectToMySQL(DATABASE).query_db(query,data)
    if len(results) < 1:
      return False

    return cls(result[0])