from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
  def __init__(self,data) -> None:
    self.id = data['id']
    self.first_name = data['first_name']
    self.last_name = data['last_name']
    self.age = data['age']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']

  @classmethod
  def new_ninja(cls, data):
    query = """
    INSERT INTO ninjas (first_name, last_name, age, dojo_id)
    VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s)
    """
    results = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
    if not results:
      return False
    return results

  @classmethod
  def all_ninjas(cls,data):
    query = """
    SELECT * FROM dojos LEFT JOIN ninjas
    ON dojos.id = ninjas.dojo_id
    WHERE dojos.id = %(id)s;
    """
    results = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
    ninjas = []
    for one_ninja in results:
      ninjas.append(cls(one_ninja))
    return ninja


# #john's code below, does not help my code - no difference made
#   @classmethod
#   def all_ninjas(cls, data):
#     query = """
#     SELECT * FROM dojos
#     LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id
#     WHERE dojos.id = %(id)s;
#     """
#     result = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
#     # THIS IS SENDING THE NINJA JOIN TO THE NINJAS CLASS TO RENDER IT
#     dojo = cls(result[0])
#     for data in result:
#         ninjainfo = {
#             'id': data['ninjas.id'],
#             'first_name': data['first_name'],
#             'last_name': data['last_name'],
#             'age': data['age'],
#             'created_at': data['ninjas.created_at'],
#             'updated_at': data['ninjas.updated_at']
#         }
#         # PUSHING INTO NINJAS
#         dojo.ninjas.append(Ninja(ninjainfo))
#     return dojo