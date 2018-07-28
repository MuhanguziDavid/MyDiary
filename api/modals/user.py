from api.database.db import DatabaseConnection

class User():
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def create_user(self, cursor):
        """method to insert a user into the users table in the database"""
        db_query="INSERT INTO users (name,email,password) VALUES (%s,%s,%s)"
        cursor.execute(db_query,(self.username,self.email,self.password))

    def get_user_by_name(self, cursor):
        """Queries the database to returen a specific user"""
        query = "SELECT * FROM users WHERE name = %s "
        cursor.execute(query, [self.username])
        result = cursor.fetchone()
        return result
