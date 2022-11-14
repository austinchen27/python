from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models import user_model
from flask import flash

class Recipe:
  def __init__(self,data):
    self.id = data['id']
    self.description = data['description']
    self.instructions = data['instructions']
    self.under = data["under"]
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']

  @classmethod
  def create_recipe(cls,data):
    query = """
    INSERT INTO recipes (description, instructions, under, user_id)
    VALUES (%(description)s, %(instructions)s, %(under)s, %(user_id)s)
    """
    results = connectToMySQL(DATABASE).query_db(query,data)
    if results:
      return results
    return False

  @classmethod
  def get_all(cls):
    query = """
    SELECT * FROM recipes JOIN users ON recipes.user_id = users.id;
    """
    results = connectToMySQL(DATABASE).query_db(query)
    all_recipes = []
    if results:
      for row in results:
        this_recipe = cls(row)
        user_data = {
          **row,
          "id": row["users.id"],
          "created_at": row["users.created_at"],
          "updated_at": row["users.updated_at"]
        }
        this_user = user_model.User(user_data)
        this_recipe.creator = this_user
        all_recipes.append(this_recipe)
        # print(all_recipes[0].creator.id)
    return all_recipes

  @classmethod
  def get_one(data):
    query = """
    SELECT * FROM recipes JOIN users ON recipes.user_id = user.id;
    WHERE id = %(id)s;
    """
    results = connectToMySQL(DATABASE).query_db(query,data)
    


#list of dictionaries (all_recipes) -> first dictionary ([0]) -> key of dictionary (creator) -> 

#dictionary (user_model.User) that creates a class instance of user_data
#put in key of .id to get value of id