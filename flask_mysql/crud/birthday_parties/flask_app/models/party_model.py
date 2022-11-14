from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import user_model

class Party:
  def __init__(self,data) -> None:
    self.id = data["id"]
    self.what = data["what"]
    self.location = data["location"]
    self.date = data["date"]
    self.all_ages = data["all_ages"]
    self.description = data["description"]
    self.updated_at = data["updated_at"]
    self.created_at = data["created_at"]
    self.user_id = data["user_id"]

  @classmethod
  def create(cls, data):
    query = """
    INSERT INTO parties (what, location, date, all_ages, description, user_id)
    VALUES (%(what)s, %(location)s, %(date)s, %(all_ages)s, %(description)s, %(user_id)s);
    """
    return connectToMySQL(DATABASE).query_db(query,data)

  @classmethod
  def get_all(cls):
    query = """
    SELECT * FROM parties JOIN users ON parties.user_id = users.id
    """
    results = connectToMySQL(DATABASE).query_db(query)
    all_parties = []
    if results:
      for row in results:
        this_party = cls(row) #<== create party instance
        user_data = { #<== isolate out the user_data
          **row, #<== for all rows that are unique to 'users'
          "id": row["users.id"], #<== for rows that are ambiguous, need to specify
          "created_at": row["users.created_at"], 
          "updated_at": row["users.updated_at"], 
        }
        this_user = user_model.User(user_data) #<== create the user instance, (instantiated user + instantiated party (all_parties)), pass in user_data to this_user
        this_party.planner = this_user#<== create a new attribute(planner) .planner that stores the entire 'this_user'
                                      #aka: store the user instance under a new attribute under the party instance 
        all_parties.append(this_party)
    return all_parties

  @classmethod
  def get_by_id(cls,data): #used for edit page
    query = """
    SELECT * FROM parties JOIN users ON parties.user_id = users.id
    WHERE parties.id = %(id)s;
    """
    #above query is just getting ONE ID
    results = connectToMySQL(DATABASE).query_db(query,data)
    if results:
      this_party = cls(results[0])
      row = results[0]
      user_data = { #<== isolate out the user_data
          **row, #<== for all rows that are unique to 'users'
          "id": row["users.id"], #<== for rows that are ambiguous, need to specify
          "created_at": row["users.created_at"],
          "updated_at": row["users.updated_at"],
        }
      this_user = user_model.User(user_data)
      this_party.planner = this_user
      return this_party
    return False

  @classmethod
  def update(cls,data):
    query = """
    UPDATE parties SET what = %(what)s, location = %(location)s, date = %(date)s, 
    all_ages = %(all_ages)s, description = %(description)s
    WHERE id = %(id)s;
    """
    return connectToMySQL(DATABASE).query_db(query,data)

  @classmethod
  def delete(cls,data):
    query = """
    DELETE FROM parties WHERE id = %(id)s;
    """
    return connectToMySQL(DATABASE).query_db(query,data)

  @staticmethod
  def validator(form_data):
    is_valid = True
    if len(form_data["what"]) < 1:
      flash("What required")
      is_valid = False
    if len(form_data["location"]) < 1:
      flash("Location required")
      is_valid = False
    if len(form_data["date"]) < 1:
      flash("Date required")
      is_valid = False
    if len(form_data["description"]) < 1:
      flash("Description required")
      is_valid = False
    if "all_ages" not in form_data:
      flash("All Ages Required")
      is_valid = False
    return is_valid