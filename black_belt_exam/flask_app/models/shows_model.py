from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import user_model

class Show:
  def __init__(self,data):
    self.id = data["id"]
    self.title = data["title"]
    self.network = data["network"]
    self.date = data["date"]
    self.description = data["description"]
    self.created_at = data["created_at"]
    self.updated_at = data["updated_at"]
    self.user_id = data["user_id"]

  @classmethod
  def create(cls,data):
    query = """
    INSERT INTO shows (title, network, date, description, user_id)
    VALUES (%(title)s, %(network)s, %(date)s, %(description)s, %(user_id)s);
    """
    return connectToMySQL(DATABASE).query_db(query,data)

  @classmethod
  def get_all(cls):
    query = """
    SELECT * FROM shows JOIN users on shows.user_id = users.id
    """
    results = connectToMySQL(DATABASE).query_db(query)
    all_shows = []
    if results:
      for row in results:
        this_show = cls(row)
        user_data = {
          **row,
          "id": row["users.id"],
          "created_at": row["users.created_at"],
          "updated_at": row["updated_at"]
        }
        this_user = user_model.User(user_data)
        this_show.viewer = this_user
        all_shows.append(this_show)
    return all_shows

#insert data (show_id and user_id) into the likes table
  @classmethod
  def data_into_likes(cls,data):
    query = """
    INSERT INTO likes (user_id, show_id)
    VALUES (%(user_id)s, %(show_id)s)
    """
    return connectToMySQL(DATABASE).query_db(query,data)

  @classmethod
  def data_delete_likes(cls,data):
    query = """
    DELETE FROM likes WHERE user_id = %(user_id)s AND show_id = %(show_id)s;
    """
    return connectToMySQL(DATABASE).query_db(query,data)


  @classmethod
  def get_by_id(cls,data):
    query = """
    SELECT * FROM shows JOIN users ON shows.user_id = users.id
    WHERE shows.id = %(id)s;
    """
    results = connectToMySQL(DATABASE).query_db(query,data)
    if results:
      this_show = cls(results[0])
      row = results[0]
      user_data = {
        **row,
        "id": row["users.id"],
        "created_at": row["users.created_at"],
        "updated_at": row["users.updated_at"]
      }
      this_user = user_model.User(user_data)
      this_show.viewer = this_user
      return this_show
    return False

  @classmethod
  def update(cls,data):
    query = """
    UPDATE shows SET title = %(title)s, network = %(network)s, date = %(date)s, description = %(description)s
    WHERE id = %(id)s;
    """
    return connectToMySQL(DATABASE).query_db(query,data)

  @classmethod
  def delete(cls,data):
    query = """
    DELETE FROM shows WHERE id = %(id)s;
    """
    return connectToMySQL(DATABASE).query_db(query,data)

  # @classmethod
  # def like_show(cls,data):
  #   query = """
  #   UPDATE shows SET quantity = %(quantity)s
  #   WHERE id = %(id)s;
  #   """
  #   return connectToMySQL(DATABASE).query_db(query,data)

  @classmethod #this method to identify which like-quantity belongs to which
  def user_liked(cls,data):
    query = """
    INSERT INTO likes (user_id, show_id)
    VALUES (%(user_id)s, %(show_id)s)
    """
    results = connectToMySQL(DATABASE).query_db(query,data)
    return results

  # @classmethod
  # def unlike_show(cls,data):
  #   query = """
  #   UPDATE shows SET quantity = %(quantity)s
  #   WHERE id = %(id)s;
  #   """
  #   results = connectToMySQL(DATABASE).query_db(query,data)
  #   return results

  @classmethod
  def count_likes_by_show_id(cls, show_id): #this parameter brings in argument for def show_one countbylikes id
    data = {
      "show_id": show_id #this key gets a value of 5 (or whatever the id is)
    }                    # "show_id" matches %(show_id)s
    query = """
    SELECT count(user_id) as num FROM likes WHERE show_id = %(show_id)s;
    """
    results = connectToMySQL(DATABASE).query_db(query,data)
    return results[0]["num"]

  @classmethod #many2many join. select each needed for div display
  def select_all(cls,data): 
    query = """
    SELECT DISTINCT first_name FROM shows
    LEFT JOIN likes ON shows.id = likes.show_id
    JOIN users ON users.id = shows.user_id
    """
    results = connectToMySQL(DATABASE).query_db(query,data)
    return results

    #     query = """
    # SELECT DISTINCT show_id,title,first_name,last_name FROM likes
    # JOIN shows ON show_id = shows.id
    # JOIN users ON shows.user_id = users.id
    # WHERE likes.user_id = %(id)s;
    # """

  @staticmethod
  def validator(data):
    is_valid = True
    if len(data["title"]) < 2:
      flash("Title field required to be 3 characters minimum")
      is_valid = False
    if len(data["network"]) < 2:
      flash("Network field required to be 3 characters minimum")
      is_valid = False
    if len(data["description"]) < 2:
      flash("Description field required to be 3 characters minimum")
      is_valid = False
    return is_valid
