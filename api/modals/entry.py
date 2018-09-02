from api.database.db import DatabaseConnection


class Entry:
    con = DatabaseConnection()
    con.create_table_users()
    con.create_table_entries()
    cursor = con.cursor
    dict_cursor = con.dict_cursor

    def __init__(self, entry_id, user_id, title, description, creation_time):
        self.entry_id = entry_id
        self.user_id = user_id
        self.title = title
        self.description = description
        self.creation_time = creation_time

    def get_all_entries(self):
        query = "SELECT * FROM entries WHERE user_id = %s"

        try:
            Entry.dict_cursor.execute(query, (self.user_id,))
            row = Entry.dict_cursor.fetchone()

            db_entries = []

            while row:
                entry_data = Entry(
                    row["entry_id"],
                    row["user_id"],
                    row["title"],
                    row["description"],
                    row["creation_time"].strftime("%Y-%m-%d %H:%M:%S"))
                row = Entry.dict_cursor.fetchone()
                db_entries.append(entry_data.__dict__)
            return db_entries
        except(Exception):
            return {"Message": "No databse entries retreived"}

    def get_entry_by_id(self):
        """
        Queries the database
        to returen a specific entry based on entry id
        """
        query = "SELECT * FROM entries WHERE entry_id = %s and user_id = %s"
        try:
            Entry.dict_cursor.execute(query, (self.entry_id, self.user_id))
            row = Entry.dict_cursor.fetchone()

            db_entry = []

            while row:
                entry_data = Entry(
                    row["entry_id"],
                    row["user_id"],
                    row["title"],
                    row["description"],
                    row["creation_time"].strftime("%Y-%m-%d %H:%M:%S")
                )
                row = Entry.dict_cursor.fetchone()
                db_entry.append(entry_data.__dict__)
            return db_entry

        except(Exception):
            return {"Message": "Entry does not exist"}

    def add_an_entry(self):
        """Method to add an entry into the database"""
        query = (
            """
            INSERT INTO entries
            (user_id, title, description, creation_time)
            VALUES (%s,%s,%s,%s);
            """)
        Entry.cursor.execute(
            query,
            (self.user_id, self.title, self.description, self.creation_time))

    def get_entry_by_title(self):
        """
        Returns a specific entry based on title
        and can be viewed in dictionary form
        """
        query = "SELECT * FROM entries WHERE title = %s AND user_id = %s"
        try:
            Entry.dict_cursor.execute(query, [self.title, self.user_id])
            row = Entry.dict_cursor.fetchone()

            db_entry = []

            while row:
                entry_data = Entry(
                    row["entry_id"],
                    row["user_id"],
                    row["title"],
                    row["description"],
                    row["creation_time"].strftime("%Y-%m-%d %H:%M:%S")
                )
                row = Entry.dict_cursor.fetchone()
                db_entry.append(entry_data.__dict__)
            return db_entry

        except(Exception):
            return {"Message": "Entry does not exist"}

    def update_an_entry(self):
        """Makes changes to entries table"""
        query = (
            """
            UPDATE entries
            SET title = %s,
            description = %s
            WHERE entry_id = %s
            """)
        Entry.dict_cursor.execute(
            query, (self.title, self.description, self.entry_id))

    def delete_an_entry(self):
        """Deletes an entry from the diary"""
        query = "DELETE FROM entries WHERE entry_id = %s AND user_id = %s"
        Entry.dict_cursor.execute(query, (self.entry_id, self.user_id))
