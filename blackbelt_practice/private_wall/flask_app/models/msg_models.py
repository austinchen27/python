from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import user_models

class Message:
  def __init__(self,data):
    self.id = data["id"]
    self.description = data["description"]
    self.created_at = data["created_at"]
    self.updated_at = data["updated_at"]
    self.user_id = data["user_id"]

  @classmethod
  def create_message(cls,data):
    query = """
    INSERT INTO messages (description, user_id)
    VALUES (%(description)s, %(user_id)s);
    """
    return connectToMySQL(DATABASE).query_db(query,data)

  @classmethod
  def get_by_id(cls,data):
    query = """
    SELECT * FROM messages JOIN users ON messages.user_id = users.id
    WHERE messages.id = %(id)s;
    """
    results = connectToMySQL(DATABASE).query_db(query,data)
    if results:
      this_message = cls(results[0])
      row = results[0]
      user_msg = {
        **row,
        "id": row["users.id"],
        "created_at": row["users.created_at"],
        "updated_at": row["users.udpated_at"]
      }
      this_user = user_models.User(user_msg)
      this_message.sender = this_user
      return this_user
    return False

  @classmethod
  def get_all(cls):
    query = """
    SELECT * FROM messages JOIN users ON messages.user_id = users.id
    """
    results = connectToMySQL(DATABASE).query_db(query)
    all_messages = []
    if results:
      for row in results:
        this_message = cls(row)
        msg_data = {
          **row,
          "id": row["users.id"],
          "created_at": row["users.created_at"],
          "updated_at": row["users.updated_at"]
        }
        this_user = user_models.User(msg_data)
        this_message.sender = this_user
        all_messages.append(this_message)
    return all_messages

  @staticmethod
  def validator_msg(form_data):
    is_valid = True
    if len(form_data["description"]) < 1:
      flash("Message must be longer than 1 character")
      is_valid = False
    return is_valid