import psycopg2
import psycopg2.extras as extra
from pprint import pprint

class DatabaseConnection:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                database = 'mydiary',
                user = 'postgres',
                password = '12345',
                host = 'localhost',
                port = '5432'
            )
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
            self.dict_cursor = self.connection.cursor(cursor_factory=extra.DictCursor)
        except:
            pprint("Cannot connect to database")
    
    def create_table(self):
        create_table_query = ("CREATE TABLE users (user_id SERIAL PRIMARY KEY, name VARCHAR(20) NOT NULL, email VARCHAR(28) NOT NULL, password VARCHAR(12) NOT NULL)")
        self.cursor.execute(create_table_query)

if __name__=="__main__":
    database_connection = DatabaseConnection()
    database_connection.create_table()

