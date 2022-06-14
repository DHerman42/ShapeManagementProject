from flask import flash, session
from flask_app.config.mysqlconnection import connectToMySQL

class Shape:
    def __init__(self, data):
        self.id = data['id']
        self.shape_number = data['shape_number']
        self.customer = data['customer']
        self.job_name = data['job_name']
        self.price = data['price']
        self.notes = data['notes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_shape(cls, data):
        query = "INSERT INTO shapes (shape_number, customer, job_name, price, notes, created_at, updated_at) VALUES (%(shape_number)s, %(customer)s, %(job_name)s, %(price)s, %(notes)s, %(created_at)s, %(created_at)s);"
        return connectToMySQL('shapelogschema').query_db(query, data)

    @classmethod
    def get_all_shapes(cls):
        query = "SELECT * FROM shapes ORDER BY shape_number DESC;"
        results = connectToMySQL('shapelogschema').query_db(query)

        shapes = []
        for shape in results:
            shapes.append(shape)

        return shapes

    @classmethod
    def get_shape_by_id(cls, data):
        query = "SELECT * FROM shapes WHERE id = %(id)s;"
        result = connectToMySQL('shapelogschema').query_db(query, data)
        return result[0]


    @classmethod
    def delete_shape(cls, data):
        deleted = True

        if session.get('user_id') == None:
            deleted = False
        else:
            query = "DELETE FROM shapes WHERE id = %(id)s;"
            connectToMySQL('shapelogschema').query_db(query, data)
        
        return deleted

    @classmethod
    def update_shape(cls, data):
        query = """UPDATE shapes
                    SET shape_number = %(shape_number)s, 
                    customer = %(customer)s, 
                    job_name = %(job_name)s, 
                    price = %(price)s, 
                    notes = %(notes)s, 
                    updated_at = NOW() 
                    WHERE id = %(id)s;"""
        connectToMySQL('shapelogschema').query_db(query, data)

    