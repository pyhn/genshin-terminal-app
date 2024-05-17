import sqlite3

class DatabaseManager:
    def __init__(self):
        self.db_name = "genshin_tracker.db"
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        self.cursor.execute("PRAGMA foreign_keys = ON;")

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

    def create_friend_request_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS friend_requests (
            request_id INTEGER PRIMARY KEY AUTOINCREMENT,
            requester_id INTEGER,
            requestee_id INTEGER,
            request_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            status TEXT DEFAULT 'pending',
            FOREIGN KEY (requester_id) REFERENCES users(uid) ON DELETE CASCADE,
            FOREIGN KEY (requestee_id) REFERENCES users(uid) ON DELETE CASCADE, 
            UNIQUE(requester_id, requestee_id)
        );
        '''
        self.execute_update(query)

    def create_friends_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS friends (
            uid INTEGER,
            friend_id INTEGER,
            start_date DATE DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (uid, friend_id),
            FOREIGN KEY (uid) REFERENCES users(uid) ON DELETE CASCADE,
            FOREIGN KEY (friend_id) REFERENCES users(uid) ON DELETE CASCADE
        );
    '''
        self.execute_update(query)

    def drop_table(self, table):
        query = f"DROP TABLE IF EXISTS {table}"
        self.execute_update(query)

    def insert_test_data(self):
        self.cursor.execute("""
            INSERT INTO users (uid, username, password, email, status, bio, fav_character, fav_region)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (1, "rei", "pog", "pogger", None, None, None, None))

        self.cursor.execute("""
            INSERT INTO users (uid, username, password, email, status, bio, fav_character, fav_region)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (2, "pogi", "pog", "pogged", None, None, None, None))

        self.cursor.execute("""
            INSERT INTO users (uid, username, password, email, status, bio, fav_character, fav_region)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (3, "jin", "pog", "poggies", None, None, None, None))

        self.cursor.execute("""
            INSERT INTO users (uid, username, password, email, status, bio, fav_character, fav_region)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (4, "eli", "pog", "poggier", None, None, None, None))

        self.cursor.execute("INSERT INTO friend_requests (requester_id, requestee_id) VALUES (?, ?)", (1, 4))
        self.cursor.execute("INSERT INTO friend_requests (requester_id, requestee_id) VALUES (?, ?)", (2, 4))
        self.cursor.execute("INSERT INTO friend_requests (requester_id, requestee_id) VALUES (?, ?)", (3, 4))
        
        insert_query = """INSERT INTO friends (uid, friend_id) VALUES (?, ?);"""
        self.execute_update(insert_query, (2, 3))
        self.execute_update(insert_query, (3, 2))
        self.execute_update(insert_query, (2, 1))
        self.execute_update(insert_query, (1, 2))
        
        self.connection.commit()


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
        return new_uid

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
        
    def update_user_info(self, user):
        user_id = user.get_uid()
        new_status = user.get_status()
        new_bio = user.get_bio()
        new_fav_char = user.get_fav_character()
        new_fav_region = user.get_fav_region()

        query = """
        UPDATE users 
        SET bio = ?, 
            status = ?, 
            fav_character = ?, 
            fav_region = ?
        WHERE uid = ?;
        """
        self.execute_update(query, (new_bio, new_status, new_fav_char, new_fav_region, user_id))
        
    def update_user_pref(self, user):
        user_id = user.get_uid()
        new_username = user.get_username()
        new_password = user.get_password()
        new_email = user.get_email()

        query = """
        UPDATE users 
        SET username = ?, 
            password = ?, 
            email = ?
        WHERE uid = ?;
        """
        self.execute_update(query, (new_username, new_password, new_email, user_id))

    def send_friend_request(self, requester, requestee):
        try:
            query = """
            INSERT INTO friend_requests (requester_id, requestee_id) VALUES (?, ?) 
            """
            self.execute_update(query, (requester, requestee))
            print("Friend Request Sent. Returning to Friends Menu...")
        except sqlite3.IntegrityError as e:
            print(f"Failed to send friend request. Returning to Friends Menu.")

    def check_friend_requests(self, user):
        uid = user.get_uid()
        query = """
        SELECT fr.*, u.username
        FROM friend_requests fr
        JOIN users u ON fr.requester_id = u.uid
        WHERE fr.requestee_id = ? AND fr.status = 'pending';
        """
        results = self.execute_query(query, (uid,))

        if results:
            return results
        else:
            return None
        
    def accept_friend_request(self, requester, requestee):
        update_query = """
        UPDATE friend_requests
        SET status = 'accepted'
        WHERE requester_id = ? AND requestee_id = ?;
        """

        self.execute_update(update_query, (requester, requestee))

        insert_query = """INSERT INTO friends (uid, friend_id) VALUES (?, ?);"""
        self.execute_update(insert_query, (requester, requestee))
        self.execute_update(insert_query, (requestee, requester))
    
    def reject_friend_request(self, requester, requestee):
        update_query = """
        UPDATE friend_requests
        SET status = 'rejected'
        WHERE requester_id = ? AND requestee_id = ?;
        """
        self.execute_update(update_query, (requester, requestee))

    def retrieve_friends_list(self, user):
        uid = user.get_uid()
        query = """
        SELECT u.*
        FROM users u
        JOIN friends f ON u.uid = f.friend_id
        WHERE f.uid = ?;
        """

        results = self.execute_query(query, (uid,))
        if results:
            return results
        else:
            return []