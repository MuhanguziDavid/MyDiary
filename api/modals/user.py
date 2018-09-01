from cryptography.fernet import Fernet

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

        key = b'pRmgMa8T0INjEAfksaq2aafzoZXEuwKI7wDe4c1F8AY='
        fernet_cipher = Fernet(key)
        encrypted_password = fernet_cipher.encrypt(bytes(self.password, encoding='utf-8'))
        self.encrypted_password = encrypted_password

    def create_user(self):
        """method to insert a user into the users table in the database"""
        db_query = "INSERT INTO users (name,email,password) VALUES (%s,%s,%s)"
        User.cursor.execute(
            db_query, (self.username, self.email, self.encrypted_password.decode("utf-8")))

    def get_user_by_name(self):
        """Queries the database to returen a specific user"""
        query = "SELECT * FROM users WHERE name = %s "
        User.dict_cursor.execute(query, [self.username])
        result = User.dict_cursor.fetchone()
        return result
