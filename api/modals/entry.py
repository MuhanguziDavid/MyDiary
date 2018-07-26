from api.database.db import DatabaseConnection
from pprint import pprint


class Entry:
    def __init__(self, entry_id, user_id, title, description, creation_time):
        self.entry_id = entry_id
        self.user_id = user_id
        self.title = title
        self.description = description
        self.creation_time = creation_time

    @staticmethod
    def get_all_entries(dict_cursor, user_id):
        query = "SELECT * FROM entries WHERE user_id = %s"

        try:
            con = DatabaseConnection()
            cursor = con.dict_cursor
            cursor.execute(query,[user_id])
            row = cursor.fetchone()

            db_entries = []

            while row:
                entry_data = Entry(row["entry_id"],
                                  row["user_id"],
                                  row["title"],
                                  row["description"],
                                  row["creation_time"].strftime("%Y-%m-%d %H:%M:%S"))
                row = cursor.fetchone()
                db_entries.append(entry_data.__dict__)
            return db_entries
        
        except Exception as e:
            pprint(e)
            return None
    
    @staticmethod
    def add_an_entry(cursor, user_id, title, description, creation_time):
        """Method to add an entry into the database"""
        query = "INSERT INTO entries (user_id, title, description, creation_time) VALUES (%s,%s,%s,%s) RETURNING entry_id;"
        cursor.execute(query,(user_id, title, description, creation_time))
    
    @staticmethod   
    def get_entry_by_title(dict_cursor, title):
        """Queries the database to returen a specific entry"""
        query_string="SELECT * FROM entries WHERE title = %s "
        dict_cursor.execute(query_string,[title])
        row=dict_cursor.fetchone()
        return row
