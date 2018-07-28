from api.database.db import DatabaseConnection


class Entry:
    con = DatabaseConnection()
    cursor = con.cursor
    dict_cursor = con.dict_cursor

    def __init__(self, user_id, title, description, creation_time):
        self.user_id = user_id
        self.title = title
        self.description = description
        self.creation_time = creation_time

    def get_all_entries(self):
        query = "SELECT * FROM entries WHERE user_id = %s"

        try:
            Entry.dict_cursor.execute(query,(self.user_id,))
            row = Entry.dict_cursor.fetchone()

            db_entries = []

            while row:
                entry_data = Entry(row["user_id"],
                                  row["title"],
                                  row["description"],
                                  row["creation_time"].strftime("%Y-%m-%d %H:%M:%S"))
                row = Entry.dict_cursor.fetchone()
                db_entries.append(entry_data.__dict__)
            return db_entries
        except:
            return {"Message": "No databse entries retreived"}

    def add_an_entry(self):
        """Method to add an entry into the database"""
        query = "INSERT INTO entries (user_id, title, description, creation_time) VALUES (%s,%s,%s,%s) RETURNING entry_id;"
        Entry.cursor.execute(query,(self.user_id, self.title, self.description, self.creation_time))

    def get_entry_by_title(self):
        """Queries the database to returen a specific entry"""
        query_string="SELECT * FROM entries WHERE title = %s "
        Entry.dict_cursor.execute(query_string, [self.title])
        row=Entry.dict_cursor.fetchone()
        return row
