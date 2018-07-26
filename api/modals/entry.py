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
    def get_all_entries():
        query = "SELECT * FROM entries"

        try:
            con = DatabaseConnection()
            cursor = con.dict_cursor
            cursor.execute(query)
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
        
        except:
            return None
