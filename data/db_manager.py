import sqlite3

class DatabaseManager:
    def __init__(self):
        self.db_name = "genshin_tracker.db"
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

    def disconnect(self):
        if self.connection:
            print()
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

    def create_new_user(self, username, password, email, status=None, bio=None, fav_character=None, fav_region=None):
        # Get the maximum user ID currently in the table
        self.cursor.execute("SELECT MAX(uid) FROM users")
        max_uid = self.cursor.fetchone()[0]
        
        # Calculate the new user ID by adding 1 to the maximum UID
        new_uid = max_uid + 1 if max_uid is not None else 1
        
        # Insert the new user into the users table
        self.cursor.execute("""
            INSERT INTO users (uid, username, password, email, status, bio, fav_character, fav_region)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (new_uid, username, password, email, status, bio, fav_character, fav_region))
        
        # Commit the transaction to make the changes persistent
        self.connection.commit()

    def get_user_pass_by_id(self, user_id):
        user_query = "SELECT username, password FROM users WHERE uid = ?"
        result = self.execute_query(user_query, (user_id,))

        # Check if the result contains any rows
        if result:
            # Extract the username and password from the first tuple in the result
            username = result[0][0]
            password = result[0][1]
            
            # Use the username and password as needed
            return username, password
        else:
            return None
        
    def get_user_info_by_id(self, user_id):
        user_query = "SELECT * FROM users WHERE uid = ?"
        result = self.execute_query(user_query, (user_id,))

        # Check if the result contains any rows
        if result:
            # Extract the username and password from the first tuple in the result
            user_info = result[0]
            
            # Use the username and password as needed
            return user_info
        else:
            return None


