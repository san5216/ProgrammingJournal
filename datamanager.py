import sqlite3


class DataManager:
    """
    A class to handle all database operations

    Methods
    _______
    create_table()
        Create journal table if one doesn't already exist
    insert_entry()
        Insert new journal entry into table
    search_entries(query)
        Search journal entries for query string
    select_all_entries()
        Select all rows of the journal table
    """

    def __init__(self):
        self.conn = sqlite3.connect('journal.db', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """Create journal table if one doesn't already exist

        :return: None
        """

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS journal (
                                entry_date date,
                                entry text)
                                """)

    def insert_entry(self, date, entry):
        """Insert new journal entries into table

        :param date: date object of today's date
        :param entry: string of journal entry
        :return: None
        """

        with self.conn:
            self.cursor.execute("INSERT INTO journal VALUES (:date, :entry)",
                                {'date': date,
                                 'entry': entry})

    def search_entries(self, query):
        """Search journal entries for query string

        :param query: query string
        :return: list of dates and entries containing query string
        """

        with self.conn:
            self.cursor.execute(f"SELECT * FROM journal WHERE entry LIKE '%{query}%' --case-insensitive")

            rows = self.cursor.fetchall()

            dates = [row['entry_date'] for row in rows]
            entries = [row['entry'] for row in rows]

            return list(zip(dates, entries))

    def select_all_entries(self):
        """Select all rows of the journal table

        :return: list of all rows in table
        """
        with self.conn:
            self.cursor.execute("SELECT * FROM journal")

            rows = self.cursor.fetchall()

            dates = [row['entry_date'] for row in rows]
            entries = [row['entry'] for row in rows]

            return list(zip(dates, entries))
