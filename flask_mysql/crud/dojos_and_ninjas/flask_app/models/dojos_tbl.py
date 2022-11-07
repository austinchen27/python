from flask_app.config.mysqlconnections import connectToMySQL
from flask_app.models import ninjas_tbl

class Dojo:
  def __init__(self, data):
    self.id = data['id']
    self.name = data['name']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']

  @classmethod
  def get_all(cls):
    query = """
    SELECT * FROM dojos;
    """
    results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
    dojos = [] #create a list
    for dojo in results: #for all the dojos from the db
      dojos.append(cls(dojo)) # add the dojos from the db into dojos variable
    return dojos #show all dojos

  @classmethod
  def save(cls, data):  #how does this data know to grab "data" from dojosctrl get_one(data)
    query = """
    INSERT INTO dojos (name)
    VALUES (%(name)s)
    """
    return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)


  @classmethod
  def get_one(cls, data):
    query = """
    SELECT * FROM dojos WHERE id = %(id)s;"
    """
    results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
    if not results:
      return False
    return cls(results[0])

  @classmethod
  def get_one(cls, data):
      query = """
      SELECT * FROM dojos LEFT JOIN ninjas
      ON dojos.id = ninjas.dojo_id 
      WHERE dojos.id = %(id)s;
      """
      results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
      if results:
          this_dojo = cls(results[0])
          these_ninjas = []
          for row in results:
              ninja_data = {
                  "id": row['ninjas.id'],
                  "first_name": row['first_name'],
                  "last_name": row['last_name'],
                  "age": row['age'],
                  "created_at": row['ninjas.created_at'],
                  "updated_at": row['ninjas.updated_at'],
                  "dojo_id": row["dojo_id"]
              }
              this_ninja = ninjas_tbl.Ninja(ninja_data)
              these_ninjas.append(this_ninja)
          this_dojo.ninjas = these_ninjas
          return this_dojo

      return False