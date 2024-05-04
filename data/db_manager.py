import sqlite3

class db_manager:
    def __init__(self):
        self.db_name = "genshin_tracker.db"
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

    def disconnect(self):
        if self.connection:
            print("Closing Connection to Database...")
            self.connection.close()

    def execute_query(self, query, parameters=None):
        if parameters:
            self.cursor.execute(query, parameters)
        else:
            self.cursor.execute(query)
        return self.cursor.fetchall()

    def execute_update(self, query, parameters=None):
        if parameters:
            self.cursor.execute(query, parameters)
        else:
            self.cursor.execute(query)
        self.connection.commit()

    def create_user_table(self):
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS users (
            uid INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            email TEXT NOT NULL,
            status TEXT,
            bio TEXT,
            fav_character TEXT,
            fav_region TEXT
        );
        '''
        self.execute_update(create_table_query)

    def create_new_user(self):
        self.cursor.execute(""" 
        SELECT MAX(u.usr)
        FROM users u
        """,)
