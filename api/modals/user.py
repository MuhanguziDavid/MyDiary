from api.database.db import DatabaseConnection


class User:
    con = DatabaseConnection()
    con.create_table_users()
    con.create_table_entries()
    cursor = con.cursor
    dict_cursor = con.dict_cursor

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def create_user(self):
        """method to insert a user into the users table in the database"""
        db_query = "INSERT INTO users (name,email,password) VALUES (%s,%s,%s)"
        User.cursor.execute(
            db_query, (self.username, self.email, self.password))

    def get_user_by_name(self):
        """Queries the database to returen a specific user"""
        query = "SELECT * FROM users WHERE name = %s "
        User.dict_cursor.execute(query, [self.username])
        result = User.dict_cursor.fetchone()
        return result
