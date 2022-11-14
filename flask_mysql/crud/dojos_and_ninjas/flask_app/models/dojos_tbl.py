from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninjas_tbl


class Dojo:
    def __init__(self, data) -> None:
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
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def save(cls, data):
        query = """
    INSERT INTO dojos (name)
    VALUES (%(name)s)
    """
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

    @classmethod
    def get_one(cls, data):
        query = """
    SELECT * FROM dojos LEFT JOIN ninjas
    ON dojos.id = ninjas.dojo_id 
    WHERE dojos.id = %(id)s;
    """
        results = connectToMySQL(
            'dojos_and_ninjas_schema').query_db(query, data)
        if results:
            this_dojo = cls(results[0]) #select ONE dojo
            these_ninjas = [] #create open list to put ninja information in later
            for row in results: #this loop is getting the information
                data = {
                    "id": row['ninjas.id'],
                    "first_name": row['first_name'],
                    "last_name": row['last_name'],
                    "age": row['age'],
                    "created_at": row['ninjas.created_at'],
                    "updated_at": row['ninjas.updated_at'],
                }
                this_ninja = ninjas_tbl.Ninja(data) #'this_ninja' is a variable that you set equal to the data that you get from your ninjas class
                these_ninjas.append(this_ninja) #putting the ninja information into the open list created on line 42
            this_dojo.ninjas = these_ninjas  #.ninja in white is the ONE dojo you selected, calling the .ninjas table, and then setting it into a variable 'these_ninjas'
            return this_dojo

        return False

        # join is joining the data, but is not returning the ninjas data
        # this award = ninja
