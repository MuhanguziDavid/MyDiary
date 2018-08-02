"""For database connection and table creation"""
import psycopg2
import psycopg2.extras as extra
import urlparse3
import os


class DatabaseConnection:
    def __init__(self, database=None):
        app_env = os.environ.get('app_env', None)
        try:

            if app_env == 'testing':
                print("td")
                self.connection = psycopg2.connect(
                    database="test_diary",
                    user='postgres',
                    password='12345',
                    host='localhost',
                    port='5432'
                )
            else:
                print("md")
                self.connection = psycopg2.connect(
                    database="mydiary",
                    user='postgres',
                    password='12345',
                    host='localhost',
                    port='5432'
                )

            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
            self.dict_cursor = self.connection.cursor(
                cursor_factory=extra.DictCursor)
        except:
            print("Cannot connect to database")

    def create_database_mydiary(self):
        query = ("CREATE DATABASE mydiary")
        self.cursor.execute(query)

    def create_table_users(self):
        create_table_query_users = (
            "CREATE TABLE IF NOT EXISTS users (user_id SERIAL PRIMARY KEY, name VARCHAR(20) NOT NULL, email VARCHAR(28) NOT NULL, password VARCHAR(12) NOT NULL)")
        self.cursor.execute(create_table_query_users)

    def create_table_entries(self):
        create_table_query_entries = (
            "CREATE TABLE IF NOT EXISTS entries (entry_id SERIAL PRIMARY KEY,user_id INTEGER NOT NULL,title VARCHAR(255) NOT NULL,description VARCHAR(255) NOT NULL,creation_time timestamp,FOREIGN KEY (user_id)REFERENCES users (user_id)ON UPDATE CASCADE ON DELETE CASCADE)")
        self.cursor.execute(create_table_query_entries)

    def drop_table_users(self):
        query = ("DROP TABLE IF EXISTS users cascade")
        self.cursor.execute(query)

    def drop_table_entries(self):
        query = ("DROP TABLE IF EXISTS entries cascade")
        self.cursor.execute(query)
    
    def close_db_connection(self):
        self.cursor.close()
        self.dict_cursor.close()
        self.connection.close()


if __name__ == "__main__":
    database_connection = DatabaseConnection()
    database_connection.create_table_users()
    database_connection.create_table_entries()
    database_connection.create_database_mydiary()
    database_connection.close_db_connection()
