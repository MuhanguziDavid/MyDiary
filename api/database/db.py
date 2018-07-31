"""For database connection and table creation"""
import psycopg2
import psycopg2.extras as extra
from flask import current_app


class DatabaseConnection:
    def __init__(self):
        try:
            if current_app.config['TEST_MODE']:
                self.connection = psycopg2.connect(
                    database="test_diary",
                    user='postgres',
                    password='12345',
                    host='localhost',
                    port='5432')
            else:
                self.connection = psycopg2.connect(
                    database="mydiary",
                    user='postgres',
                    password='12345',
                    host='localhost',
                    port='5432')
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
            self.dict_cursor = self.connection.cursor(
                cursor_factory=extra.DictCursor)
        except:
            print("Cannot connect to database")

    def create_table_users(self):
        create_table_query_users = (
            "CREATE TABLE IF NOT EXISTS users (user_id SERIAL PRIMARY KEY, name VARCHAR(20) NOT NULL, email VARCHAR(28) NOT NULL, password VARCHAR(12) NOT NULL)")
        self.cursor.execute(create_table_query_users)

    def create_table_entries(self):
        create_table_query_entries = (
            "CREATE TABLE IF NOT EXISTS entries (entry_id SERIAL PRIMARY KEY,user_id INTEGER NOT NULL,title VARCHAR(255) NOT NULL,description VARCHAR(255) NOT NULL,creation_time timestamp,FOREIGN KEY (user_id)REFERENCES users (user_id)ON UPDATE CASCADE ON DELETE CASCADE)")
        self.cursor.execute(create_table_query_entries)


if __name__ == "__main__":
    database_connection = DatabaseConnection()
    database_connection.create_table_users()
    database_connection.create_table_entries()
