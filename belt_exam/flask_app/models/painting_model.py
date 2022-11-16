from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import user_model

class Painting:
  def __init__(self,data):
    self.id = data["id"]
    self.title = data["title"]
    self.description = data["description"]
    self.price = data["price"]
    self.created_at = data["created_at"]
    self.updated_at = data["updated_at"]
    self.purchased = data["purchased"]
    self.quantity = data["quantity"]
    self.user_id = data["user_id"]

  @classmethod
  def create(cls, data):
    query = """
    INSERT INTO paintings (title, description, price, quantity, user_id)
    VALUES (%(title)s, %(description)s, %(price)s, %(quantity)s, %(user_id)s);
    """
    return connectToMySQL(DATABASE).query_db(query,data)


  @classmethod
  def get_all(cls):
    query = """
    SELECT * FROM paintings JOIN users ON paintings.user_id = users.id
    """
    results = connectToMySQL(DATABASE).query_db(query)
    all_paintings = []
    if results:
      for row in results:
        this_painting = cls(row) #<== create party instance
        user_data = { #<== isolate out the user_data
          **row, #<== for all rows that are unique to 'users'
          "id": row["users.id"], #<== for rows that are ambiguous, need to specify
          "created_at": row["users.created_at"],
          "updated_at": row["users.updated_at"]
        }
        this_user = user_model.User(user_data) #<== create the user instance, (instantiated user + instantiated party (all_parties)), pass in user_data to this_user
                                      #aka: store the user instance under a new attribute under the party instance 
        this_painting.picasso = this_user#<== create a new attribute(planner) .planner that stores the entire 'this_user'
        all_paintings.append(this_painting)
    return all_paintings

  @classmethod
  def get_by_id(cls,data): #used for edit page
    query = """
    SELECT * FROM paintings JOIN users ON paintings.user_id = users.id
    WHERE paintings.id = %(id)s;
    """
    #above query is just getting ONE ID
    results = connectToMySQL(DATABASE).query_db(query,data)
    if results:
      this_painting = cls(results[0])
      row = results[0]
      user_data = { #<== isolate out the user_data
          **row, #<== for all rows that are unique to 'users'
          "id": row["users.id"], #<== for rows that are ambiguous, need to specify
          "created_at": row["users.created_at"],
          "updated_at": row["users.updated_at"],
        }
      this_user = user_model.User(user_data)
      this_painting.picasso = this_user
      return this_painting
    return False

  @classmethod
  def update(cls,data): #added quantity for many to many
    query = """
    UPDATE paintings SET title = %(title)s, description = %(description)s, quantity = %(quantity)s, price = %(price)s
    WHERE id = %(id)s;
    """
    return connectToMySQL(DATABASE).query_db(query,data)

  @classmethod
  def delete(cls,data):
    query = """
    DELETE FROM paintings WHERE id = %(id)s;
    """
    return connectToMySQL(DATABASE).query_db(query,data)

  @classmethod #this method is to buy a painting
  def buy_painting(cls,data):
    query = """
    UPDATE paintings SET purchased = %(purchased)s
    WHERE id = %(id)s;
    """
    return connectToMySQL(DATABASE).query_db(query,data)

  @classmethod #this method to identify which purchase belongs to which
  def purchased(cls,data):
    query = """
    INSERT INTO purchases (user_id, painting_id)
    VALUES (%(user_id)s, %(painting_id)s)
    """
    return connectToMySQL(DATABASE).query_db(query,data)

  @classmethod #many2many join. select each needed for div display
  def select_all(cls,data): 
    query = """
    SELECT DISTINCT painting_id,title,first_name,last_name FROM purchases
    JOIN paintings ON painting_id = paintings.id
    JOIN users ON paintings.user_id = users.id
    WHERE purchases.user_id = %(id)s;
    """
    return connectToMySQL(DATABASE).query_db(query,data)

#    display:
# 1)start with select all from purchases where id = person logged in
# but also join paintings onto that query
# will not have persons name to created
# join users table onto foreign key of paintings table to access name of 
# creator

  @staticmethod
  def validator(data):
    is_valid = True
    if len(data["title"]) < 2:
      flash("Name field required to be 3 characters minimum")
      is_valid = False
    if len(data["description"]) < 10:
      flash("Not descriptive enough, need more details")
      is_valid = False
    if data["price"]:
      if int(data["price"]) <= 0:
        flash("You're worth more than that!")
        is_valid = False
    if data["quantity"]:
      if int(data["quantity"]) < 1:
        flash("More")
        is_valid = False
    return is_valid

    # shows_ctrl line 54-55 20-21
