from api.database.db import DatabaseConnection

class User():
    def __init__(self, _id, username, email, password, confirm_password):
        self.id = _id
        self.username = username
        self.email = email
        self.password = password
        self.confirm_password = confirm_password

    @staticmethod
    def create_user(cursor, name, email, password):
        """method to insert a user into the users table in the database"""
        db_query="INSERT INTO users (name,email,password) VALUES (%s,%s,%s)"
        cursor.execute(db_query,(name,email,password))
    
    @staticmethod   
    def get_user_by_name(cursor, name):
        """Queries the database to returen a specific user"""
        query = "SELECT * FROM users WHERE name = %s "
        cursor.execute(query,[name])
        result = cursor.fetchone()
        return result
