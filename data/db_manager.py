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

    def create_posts_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS posts (
            pid INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            body TEXT NOT NULL,
            uid INTEGER,
            post_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (uid) REFERENCES users(uid) ON DELETE CASCADE
            );
                '''
        self.execute_update(query)

    def create_comments_table(self):
        query = '''
            CREATE TABLE IF NOT EXISTS comments (
            cid INTEGER PRIMARY KEY AUTOINCREMENT,
            uid INTEGER,
            replyto INTEGER DEFAULT NULL,
            pid INTEGER,
            comment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            text TEXT NOT NULL,
            likes INTEGER DEFAULT 0,
            dislikes INTEGER DEFAULT 0,
            FOREIGN KEY (uid) REFERENCES users(uid) ON DELETE CASCADE,
            FOREIGN KEY (pid) REFERENCES posts(pid) ON DELETE CASCADE,
            FOREIGN KEY (replyto) REFERENCES users(uid) ON DELETE CASCADE
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
        """, (2, "pogi", "pog", "pogged", "dying", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus vehicula varius tincidunt. Integer dui nibh, iaculis quis diam et, aliquam eleifend justo. Aenean nec est sed ex malesuada imperdiet sed a erat. Sed at maximus urna, fermentum pretium orci. Donec facilisis dignissim libero, vitae sagittis sapien porta quis. Maecenas quis nisi sit amet justo sagittis laoreet viverra id nisi. Etiam vehicula tempus cursus. Aenean dignissim augue at augue scelerisque consectetur. Fusce tempus, est ac ornare consequat, purus ante pellentesque mauris, sit amet euismod metus est non ex. Pellentesque quis purus dapibus, tempus enim ac, facilisis dolor.", "Bennett", "Liyue"))

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
        
        self.cursor.execute("INSERT INTO posts (title, body, uid) VALUES (?, ?, ?)", ("Lorem Ippsum", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus vehicula varius tincidunt. Integer dui nibh, iaculis quis diam et, aliquam eleifend justo. Aenean nec est sed ex malesuada imperdiet sed a erat. Sed at maximus urna, fermentum pretium orci. Donec facilisis dignissim libero, vitae sagittis sapien porta quis. Maecenas quis nisi sit amet justo sagittis laoreet viverra id nisi. Etiam vehicula tempus cursus. Aenean dignissim augue at augue scelerisque consectetur. Fusce tempus, est ac ornare consequat, purus ante pellentesque mauris, sit amet euismod metus est non ex. Pellentesque quis purus dapibus, tempus enim ac, facilisis dolor.", 1))
        
        self.cursor.execute("INSERT INTO comments (uid, pid, text) VALUES (?, ?, ?)", (2, 1, "HALLLLLLOOOOOOOOO :D HALLLLLLOOOOOOOOO :DHALLLLLLOOOOOOOOO :DHALLLLLLOOOOOOOOO :D"))

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
            user_info = result[0]
            
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
        
    def retrieve_friends_list_only_id(self, user):
        uid = user.get_uid()
        query = """
        SELECT u.uid
        FROM users u
        JOIN friends f ON u.uid = f.friend_id
        WHERE f.uid = ?;
        """

        results = self.execute_query(query, (uid,))
        if results:
            return results
        else:
            return []
        
    def create_post(self, user, title, content):
        uid = user.get_uid()
        query = '''
        INSERT INTO posts (title, body, uid) VALUES (?, ?, ?);
        '''
        self.execute_update(query, (title, content, uid))

    def retrieve_posts_list(self, user):
        uid = user.get_uid()
        query = """
        SELECT p.*
        FROM posts p
        WHERE p.uid = ?;
        """

        results = self.execute_query(query, (uid,))
        if results:
            return results
        else:
            return []
        
    def delete_post(self, pid):
        delete_query = "DELETE FROM posts WHERE pid = ?;"
        self.execute_update(delete_query, (pid,))

    def retrieve_friends_posts(self, user):
        uid = user.get_uid()
        query = """
        SELECT p.*
        FROM posts p
        JOIN friends f ON p.uid = f.friend_id
        WHERE f.uid = ?;
        """
        results = self.execute_query(query, (uid,))
        if results:
            return results
        else:
            return []
        
    def comment_to_post(self, uid, pid, content):
        query = '''
        INSERT INTO comments (uid, pid, text) VALUES (?, ?, ?);
        '''
        self.execute_update(query, (uid, pid, content))

    def retrieve_comments(self, pid):
        query = """
        SELECT * 
        FROM comments 
        WHERE pid = ?;"""
        results = self.execute_query(query, (pid,))
        if results:
            return results
        else:
            return []