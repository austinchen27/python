from flask_app.config.mysqlconnections import connectToMySQL


class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['first_name']
        self.name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        ninjas = []
        for ninja in results:
            ninjas.append(cls(ninja))
        return ninjas

    @classmethod
    def new_ninja(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ( %(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s)"
        print("hihi")
        results = connectToMySQL(
            'dojos_and_ninjas_schema').query_db(query, data)
        if not results:
            return False
        print(results)
        return results

    @classmethod
    def all_ninjas(cls, data):
        query = """
        SELECT * FROM ninjas
        LEFT JOIN ninjas ON dojos.ninjas_id = dojos.id
        WHERE dojos.id = %(id)s;
        """
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        return results