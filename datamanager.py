"""DataManager handles all database operations."""

import sqlite3


class DataManager:
    def __init__(self):
        self.conn = sqlite3.connect('journal.db', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """
        Create table in journal database.
        :return:
        """

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS journal (
                                entry_date date,
                                entry text)
                                """)

    def insert_entry(self, date, entry):
        with self.conn:
            self.cursor.execute("INSERT INTO journal VALUES (:date, :entry)",
                                {'date': date,
                                 'entry': entry})

    def search_entries(self, query):

        with self.conn:
            self.cursor.execute(f"SELECT * FROM journal WHERE entry LIKE '%{query}%' --case-insensitive")

            rows = self.cursor.fetchall()

            dates = [row['entry_date'] for row in rows]
            entries = [row['entry'] for row in rows]

            return list(zip(dates, entries))

    def select_all_entries(self):
        with self.conn:
            self.cursor.execute("SELECT * FROM journal")

            rows = self.cursor.fetchall()

            dates = [row['entry_date'] for row in rows]
            entries = [row['entry'] for row in rows]

            return list(zip(dates, entries))
