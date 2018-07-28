from api.database.db import DatabaseConnection
from pprint import pprint


class Entry:
    def __init__(self, user_id, title, description, creation_time):
        self.user_id = user_id
        self.title = title
        self.description = description
        self.creation_time = creation_time

    def get_all_entries(self, dict_cursor):
        query = "SELECT * FROM entries WHERE user_id = %s"

        try:
            con = DatabaseConnection()
            cursor = con.dict_cursor
            cursor.execute(query,[self.user_id])
            row = cursor.fetchone()

            db_entries = []

            while row:
                entry_data = Entry(row["user_id"],
                                  row["title"],
                                  row["description"],
                                  row["creation_time"].strftime("%Y-%m-%d %H:%M:%S"))
                row = cursor.fetchone()
                db_entries.append(entry_data.__dict__)
            return db_entries
        
        except Exception as e:
            pprint(e)
            return None

    def add_an_entry(self,cursor):
        """Method to add an entry into the database"""
        query = "INSERT INTO entries (user_id, title, description, creation_time) VALUES (%s,%s,%s,%s) RETURNING entry_id;"
        cursor.execute(query,(self.user_id, self.title, self.description, self.creation_time))

    def get_entry_by_title(self,dict_cursor):
        """Queries the database to returen a specific entry"""
        query_string="SELECT * FROM entries WHERE title = %s "
        dict_cursor.execute(query_string, [self.title])
        row=dict_cursor.fetchone()
        return row
