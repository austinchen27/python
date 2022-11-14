from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models import user_model
from flask import flash

class Recipe:
  def __init__(self,data):
    self.id = data["id"]
    self.name = data["name"]
    self.description = data["description"]
    self.instructions = data["instructions"]
    self.date = data["date"]
    self.under = data["under"]
    self.created_at = data["created_at"]
    self.updated_at = data["updated_at"]
    self.user_id = data["user_id"]

  @classmethod 
  def create(cls,data):
    query = """
    INSERT INTO recipes (name, description, instructions, date, under, user_id)
    VALUES (%(name)s, %(description)s, %(instructions)s, %(date)s, %(under)s, %(user_id)s);
    """
    return connectToMySQL(DATABASE).query_db(query,data)

  @classmethod
  def get_all(cls):
    query = """
    SELECT * FROM recipes JOIN users ON recipes.user_id = users.id
    """
    results = connectToMySQL(DATABASE).query_db(query)
    all_recipes = []
    if results:
      for row in results:
        this_recipe = cls(row) #<== create party instance
        user_data = { #<== isolate out the user_data
          **row, #<== for all rows that are unique to 'users'
          "id": row["users.id"], #<== for rows that are ambiguous, need to specify
          "created_at": row["users.created_at"],
          "updated_at": row["users.updated_at"]
        }
        this_user = user_model.User(user_data) #<== create the user instance, (instantiated user + instantiated party (all_parties)), pass in user_data to this_user
                                      #aka: store the user instance under a new attribute under the party instance 
        this_recipe.planner = this_user#<== create a new attribute(planner) .planner that stores the entire 'this_user'
        all_recipes.append(this_recipe)
    return all_recipes

  @classmethod
  def get_by_id(cls,data): #used for edit page
    query = """
    SELECT * FROM recipes JOIN users ON recipes.user_id = users.id
    WHERE recipes.id = %(id)s;
    """
    #above query is just getting ONE ID
    results = connectToMySQL(DATABASE).query_db(query,data)
    if results:
      this_recipe = cls(results[0])
      row = results[0]
      user_data = { #<== isolate out the user_data
          **row, #<== for all rows that are unique to 'users'
          "id": row["users.id"], #<== for rows that are ambiguous, need to specify
          "created_at": row["users.created_at"],
          "updated_at": row["users.updated_at"],
        }
      this_user = user_model.User(user_data)
      this_recipe.planner = this_user
      return this_recipe
    return False

  @classmethod
  def update(cls,data):
    query = """
    UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, 
    under = %(under)s
    WHERE id = %(id)s;
    """
    return connectToMySQL(DATABASE).query_db(query,data)

  @classmethod
  def delete(cls,data):
    query = """
    DELETE FROM recipes WHERE id = %(id)s;
    """
    return connectToMySQL(DATABASE).query_db(query,data)


  @staticmethod
  def validator(data):
    is_valid = True
    if len(data["name"]) < 3:
      flash("Name must be at least 3 characters")
      is_valid = False
    if len(data["description"]) < 3:
      flash("Description must be at least 3 characters")
      is_valid = False
    if len(data["instructions"]) < 3:
      flash("Instructions must be at least 3 characters")
      is_valid = False
    return is_valid

# if data["instructions"] < 3:
# instruction would have to be int on db