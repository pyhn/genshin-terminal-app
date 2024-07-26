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
        create_table_query = """
        CREATE TABLE IF NOT EXISTS users (
            uid INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            email TEXT NOT NULL,
            status TEXT,
            bio TEXT,
            fav_character TEXT,
            fav_region TEXT,
            fame INTEGER DEFAULT 0
        );
        """
        self.execute_update(create_table_query)

    def create_friend_request_table(self):
        query = """
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
        """
        self.execute_update(query)

    def create_friends_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS friends (
            uid INTEGER,
            friend_id INTEGER,
            start_date DATE DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (uid, friend_id),
            FOREIGN KEY (uid) REFERENCES users(uid) ON DELETE CASCADE,
            FOREIGN KEY (friend_id) REFERENCES users(uid) ON DELETE CASCADE,
            CHECK (uid != friend_id)
        );
        """
        self.execute_update(query)

    def create_posts_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS posts (
            pid INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            body TEXT NOT NULL,
            author INTEGER,
            post_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            likes INTEGER DEFAULT 0,
            dislikes INTEGER DEFAULT 0,
            FOREIGN KEY (author) REFERENCES users(uid) ON DELETE CASCADE
        );
        """
        self.execute_update(query)

    def create_comments_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS comments (
            cid INTEGER PRIMARY KEY AUTOINCREMENT,
            author INTEGER,
            replyto INTEGER DEFAULT NULL,
            pid INTEGER,
            comment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            text TEXT NOT NULL,
            likes INTEGER DEFAULT 0,
            dislikes INTEGER DEFAULT 0,
            FOREIGN KEY (author) REFERENCES users(uid) ON DELETE CASCADE,
            FOREIGN KEY (pid) REFERENCES posts(pid) ON DELETE CASCADE,
            FOREIGN KEY (replyto) REFERENCES comments(cid) ON DELETE CASCADE
        );
        """
        self.execute_update(query)

    def create_likes_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS likes (
            lid INTEGER PRIMARY KEY AUTOINCREMENT,
            uid INTEGER,
            pid INTEGER DEFAULT NULL,
            cid INTEGER DEFAULT NULL,
            like_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (uid) REFERENCES users(uid) ON DELETE CASCADE,
            FOREIGN KEY (pid) REFERENCES posts(pid) ON DELETE CASCADE,
            FOREIGN KEY (cid) REFERENCES comments(cid) ON DELETE CASCADE,
            CHECK ((pid IS NOT NULL AND cid IS NULL) OR (pid IS NULL AND cid IS NOT NULL))
        );
        """
        self.execute_update(query)

    def create_dislikes_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS dislikes (
            did INTEGER PRIMARY KEY AUTOINCREMENT,
            uid INTEGER,
            pid INTEGER DEFAULT NULL,
            cid INTEGER DEFAULT NULL,
            dislike_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (uid) REFERENCES users(uid) ON DELETE CASCADE,
            FOREIGN KEY (pid) REFERENCES posts(pid) ON DELETE CASCADE,
            FOREIGN KEY (cid) REFERENCES comments(cid) ON DELETE CASCADE,
            CHECK ((pid IS NOT NULL AND cid IS NULL) OR (pid IS NULL AND cid IS NOT NULL))
        );
        """
        self.execute_update(query)

    def create_tags_table(self):
        query = """
         CREATE TABLE IF NOT EXISTS tags (
            term TEXT,
            PRIMARY KEY (term)
        );
            """
        self.execute_update(query)
        
    def create_mentions_table(self):
        query = """
         CREATE TABLE IF NOT EXISTS mentions (
            author INT,
            pid INT,
            term TEXT,
            PRIMARY KEY (author, pid, term),
            FOREIGN KEY (author) REFERENCES users(uid),
            FOREIGN KEY (pid) REFERENCES posts(pid),
            FOREIGN KEY (term) REFERENCES tags(term)
        );
            """
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
        """, (4, "eli", "pog", "poggied", None, None, None, None))

        self.cursor.execute("""
            INSERT INTO users (uid, username, password, email, status, bio, fav_character, fav_region)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (5, "joe", "pog", "poggiest", None, None, None, None))

        self.cursor.execute("""
            INSERT INTO users (uid, username, password, email, status, bio, fav_character, fav_region)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (6, "bob", "pog", "poggerest", None, None, None, None))

        self.cursor.execute("""
            INSERT INTO users (uid, username, password, email, status, bio, fav_character, fav_region)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (7, "guy", "pog", "poggier", None, None, None, None))

        self.cursor.execute("INSERT INTO friend_requests (requester_id, requestee_id) VALUES (?, ?)", (1, 4))
        self.cursor.execute("INSERT INTO friend_requests (requester_id, requestee_id) VALUES (?, ?)", (2, 4))
        self.cursor.execute("INSERT INTO friend_requests (requester_id, requestee_id) VALUES (?, ?)", (3, 4))
        
        self.cursor.execute("INSERT INTO posts (title, body, author) VALUES (?, ?, ?)", ("Lorem Ippsum", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus vehicula varius tincidunt. Integer dui nibh, iaculis quis diam et, aliquam eleifend justo. Aenean nec est sed ex malesuada imperdiet sed a erat. Sed at maximus urna, fermentum pretium orci. Donec facilisis dignissim libero, vitae sagittis sapien porta quis. Maecenas quis nisi sit amet justo sagittis laoreet viverra id nisi. Etiam vehicula tempus cursus. Aenean dignissim augue at augue scelerisque consectetur. Fusce tempus, est ac ornare consequat, purus ante pellentesque mauris, sit amet euismod metus est non ex. Pellentesque quis purus dapibus, tempus enim ac, facilisis dolor.", 1))
        self.cursor.execute("INSERT INTO posts (title, body, author) VALUES (?, ?, ?)", ("Poggeres", "Guys chat are we pogging like crazy or nah, coz lowkey im pogging like crazy and its just wayyyyyyyyyy tooo pog rn hahaahah.", 1))
        self.cursor.execute("INSERT INTO posts (title, body, author) VALUES (?, ?, ?)", ("Hehehe", "Muuheheheuehuuhueuheuhuhuehuehu Muheuheuheuhuehuheuheh eheheheheh heu uehuehuh uheu heuh euhuehhehu uehmeueehhee..", 1))
        self.cursor.execute("INSERT INTO posts (title, body, author) VALUES (?, ?, ?)", ("Crimp", "Bouldering bouldering bouldering Bouldering bouldering bouldering Bouldering bouldering bouldering Bouldering bouldering bouldering Bouldering bouldering bouldering", 2))
        self.cursor.execute("INSERT INTO posts (title, body, author) VALUES (?, ?, ?)", ("Slab", "Slab Bouldering bouldering bouldering Slab Bouldering bouldering bouldering Slab Bouldering bouldering bouldering Slab Bouldering bouldering bouldering SlabBouldering bouldering bouldering Slab Bouldering bouldering bouldering", 2))                                                                              
        self.cursor.execute("INSERT INTO posts (title, body, author) VALUES (?, ?, ?)", ("Dropknee", "When one foot inside edges while the other outside edges, the knee of the outside edging leg is lowered so that the feet are pushing away from each other rather than down", 2))
        self.cursor.execute("INSERT INTO posts (title, body, author) VALUES (?, ?, ?)", ("Gaston", "Gripping a vertical hold with the arm bent at the elbow and the hand, thumb down, pulling the hold away from the body.", 3))
        self.cursor.execute("INSERT INTO posts (title, body, author) VALUES (?, ?, ?)", ("Bicycle", "A technique in which one foot pushes a hold conventionally while the other foot toe hooks the same, or a nearby, hold. Most commonly used when climbing roofs ", 3))
        self.cursor.execute("INSERT INTO posts (title, body, author) VALUES (?, ?, ?)", ("Bouldering Pad", "A rectangular crash mat that consists of multiple layers of foam covered in a heavy duty material. The pad is placed where the climber is expected to fall to cushion their landing", 3))

        self.cursor.execute("INSERT INTO comments (author, pid, text) VALUES (?, ?, ?)", (2, 1, "HALLLLLLOOOOOOOOO :D HALLLLLLOOOOOOOOO :DHALLLLLLOOOOOOOOO :DHALLLLLLOOOOOOOOO :D"))
        self.cursor.execute("INSERT INTO comments (author, pid, text) VALUES (?, ?, ?)", (2, 1, "WHAAAAAAAAAAAAAT THE HEEEEEEEECKKKKKKKKKKKKKKKKK"))
        self.cursor.execute("INSERT INTO comments (author, pid, text) VALUES (?, ?, ?)", (3, 1, "TEAM FORTRESS 2 IS SO AMAZINNG LMAOOOO"))


        self.cursor.execute("INSERT INTO likes (uid, cid) VALUES (?, ?)", (1, 1))
        self.cursor.execute("INSERT INTO likes (uid, cid) VALUES (?, ?)", (1, 2))
        self.cursor.execute("INSERT INTO likes (uid, cid) VALUES (?, ?)", (1, 3))
        self.cursor.execute("INSERT INTO likes (uid, cid) VALUES (?, ?)", (3, 1))
        self.cursor.execute("INSERT INTO likes (uid, cid) VALUES (?, ?)", (3, 2))
        self.cursor.execute("INSERT INTO likes (uid, cid) VALUES (?, ?)", (4, 1))
        self.cursor.execute("INSERT INTO likes (uid, cid) VALUES (?, ?)", (4, 2))


        insert_query = """INSERT INTO friends (uid, friend_id) VALUES (?, ?);"""
        self.execute_update(insert_query, (2, 3))
        self.execute_update(insert_query, (3, 2))
        self.execute_update(insert_query, (2, 1))
        self.execute_update(insert_query, (1, 2))
        
        self.update_post_interactions()
        self.update_comment_interactions()
        self.update_user_fame()

        self.connection.commit()

    def update_comment_interactions(self):
        try:
            update_query = """
            UPDATE comments
            SET likes = (
                SELECT COUNT(*)
                FROM likes
                WHERE likes.cid = comments.cid
            );
            """
            self.execute_update(update_query)

            update_dislikes_query = """
            UPDATE comments
            SET dislikes = (
                SELECT COUNT(*)
                FROM dislikes
                WHERE dislikes.cid = comments.cid
            );
            """
            self.execute_update(update_dislikes_query)
            print("Comment likes and dislikes updated successfully!")
        except Exception as e:
            print(f"Error updating comment likes: {e}")

    def update_post_interactions(self):
        try:
            # Update likes count in the posts table based on the likes table
            update_likes_query = """
            UPDATE posts
            SET likes = (
                SELECT COUNT(*)
                FROM likes
                WHERE likes.pid = posts.pid
            );
            """
            self.execute_update(update_likes_query)
            
            # Update dislikes count in the posts table based on the dislikes table
            update_dislikes_query = """
            UPDATE posts
            SET dislikes = (
                SELECT COUNT(*)
                FROM dislikes
                WHERE dislikes.pid = posts.pid
            );
            """
            self.execute_update(update_dislikes_query)

            
            print("Post likes and dislikes updated successfully!")
        except Exception as e:
            print(f"Error updating post likes and dislikes: {e}")

    def update_user_fame(self):
        try:
            # Update fame based on the number of friends
            update_fame_friends_query = """
            UPDATE users
            SET fame = (
                SELECT COUNT(*)
                FROM friends
                WHERE friends.uid = users.uid
            )
            WHERE uid IN (
                SELECT uid
                FROM friends
                GROUP BY uid
            );
            """
            self.execute_update(update_fame_friends_query)

            # Update fame based on likes on posts
            update_fame_likes_posts_query = """
            UPDATE users
            SET fame = fame + (
                SELECT COALESCE(SUM(like_count), 0)
                FROM (
                    SELECT pid, COUNT(*) AS like_count
                    FROM likes
                    GROUP BY pid
                ) AS post_likes
                JOIN posts ON posts.pid = post_likes.pid
                WHERE posts.author = users.uid
            )
            WHERE uid IN (
                SELECT author
                FROM posts
                GROUP BY author
            );
            """
            self.execute_update(update_fame_likes_posts_query)

            # Update fame based on likes on comments
            update_fame_likes_comments_query = """
            UPDATE users
            SET fame = fame + (
                SELECT COALESCE(SUM(like_count), 0)
                FROM (
                    SELECT cid, COUNT(*) AS like_count
                    FROM likes
                    GROUP BY cid
                ) AS comment_likes
                JOIN comments ON comments.cid = comment_likes.cid
                WHERE comments.author = users.uid
            )
            WHERE uid IN (
                SELECT author
                FROM comments
                GROUP BY author
            );
            """
            self.execute_update(update_fame_likes_comments_query)

            # Update fame based on dislikes on posts
            update_fame_dislikes_posts_query = """
            UPDATE users
            SET fame = fame - (
                SELECT COALESCE(SUM(dislike_count), 0)
                FROM (
                    SELECT pid, COUNT(*) AS dislike_count
                    FROM dislikes
                    GROUP BY pid
                ) AS post_dislikes
                JOIN posts ON posts.pid = post_dislikes.pid
                WHERE posts.author = users.uid
            )
            WHERE uid IN (
                SELECT author
                FROM posts
                GROUP BY author
            );
            """
            self.execute_update(update_fame_dislikes_posts_query)

            # Update fame based on dislikes on comments
            update_fame_dislikes_comments_query = """
            UPDATE users
            SET fame = fame - (
                SELECT COALESCE(SUM(dislike_count), 0)
                FROM (
                    SELECT cid, COUNT(*) AS dislike_count
                    FROM dislikes
                    GROUP BY cid
                ) AS comment_dislikes
                JOIN comments ON comments.cid = comment_dislikes.cid
                WHERE comments.author = users.uid
            )
            WHERE uid IN (
                SELECT author
                FROM comments
                GROUP BY author
            );
            """
            self.execute_update(update_fame_dislikes_comments_query)

            # Commit the changes
            self.connection.commit()
            print("User fame updated successfully!")
        except Exception as e:
            print(f"Error updating user fame: {e}")



    def create_new_user(self, username, password, email, status=None, bio=None, fav_character=None, fav_region=None):
        try:
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
        except Exception as e:
            print(f"Error creating new user: {e}")

    def get_user_pass_by_id(self, user_id):
        try:
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
        except Exception as e:
            print(f"Error retrieving user password: {e}")

    def get_user_info_by_id(self, user_id):
        try:
            user_query = "SELECT * FROM users WHERE uid = ?"
            result = self.execute_query(user_query, (user_id,))

            # Check if the result contains any rows
            if result:
                user_info = result[0]
                return user_info
            else:
                return None
        except Exception as e:
            print(f"Error retrieving user info: {e}")

    def update_user_info(self, user):
        try:
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
        except Exception as e:
            print(f"Error updating user info: {e}")

    def update_user_pref(self, user):
        try:
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
        except Exception as e:
            print(f"Error updating user preferences: {e}")

    def send_friend_request(self, requester, requestee):
        try:
            query = """
            INSERT INTO friend_requests (requester_id, requestee_id) VALUES (?, ?) 
            """
            self.execute_update(query, (requester, requestee))
            print("Friend Request Sent. Returning to Friends Menu...")
        except sqlite3.IntegrityError as e:
            print(f"Failed to send friend request. Returning to Friends Menu.")
        except Exception as e:
            print(f"Error sending friend request: {e}")

    def check_friend_requests(self, user):
        try:
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
        except Exception as e:
            print(f"Error checking friend requests: {e}")

    def accept_friend_request(self, requester, requestee):
        try:
            update_query = """
            UPDATE friend_requests
            SET status = 'accepted'
            WHERE requester_id = ? AND requestee_id = ?;
            """
            self.execute_update(update_query, (requester, requestee))

            insert_query = """INSERT INTO friends (uid, friend_id) VALUES (?, ?);"""
            self.execute_update(insert_query, (requester, requestee))
            self.execute_update(insert_query, (requestee, requester))
        except Exception as e:
            print(f"Error accepting friend request: {e}")

    def reject_friend_request(self, requester, requestee):
        try:
            update_query = """
            DELETE FROM friend_requests
            WHERE requester_id = ? AND requestee_id = ?;
            """
            self.execute_update(update_query, (requester, requestee))
        except Exception as e:
            print(f"Error rejecting friend request: {e}")

    def remove_friend(self, uid_1, uid_2):
        try:
            query = """
            DELETE FROM friends
            WHERE (uid = ? AND friend_id = ?)
            OR (uid = ? AND friend_id = ?);
            """
            self.execute_update(query, (uid_1, uid_2, uid_2, uid_1))
            
        except Exception as e:
            print(f"Error removing friend: {e}")


    def retrieve_friends_list(self, user):
        try:
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
        except Exception as e:
            print(f"Error retrieving friends list: {e}")

    def retrieve_friends_list_only_id(self, user):
        try:
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
        except Exception as e:
            print(f"Error retrieving friends list (only ID): {e}")

    def create_post(self, user, title, content):
        try:
            uid = user.get_uid()
            query = """
            INSERT INTO posts (title, body, author) VALUES (?, ?, ?);
            """
            self.execute_update(query, (title, content, uid))
        except Exception as e:
            print(f"Error creating post: {e}")

    def retrieve_posts_list(self, user):
        try:
            uid = user.get_uid()
            query = """
            SELECT p.*
            FROM posts p
            WHERE p.author = ?;
            """

            results = self.execute_query(query, (uid,))
            if results:
                return results
            else:
                return []
        except Exception as e:
            print(f"Error retrieving posts list: {e}")

    def delete_post(self, pid):
        try:
            delete_query = "DELETE FROM posts WHERE pid = ?;"
            self.execute_update(delete_query, (pid,))
        except Exception as e:
            print(f"Error deleting post: {e}")

    def retrieve_friends_posts(self, user):
        try:
            uid = user.get_uid()
            query = """
            SELECT p.*
            FROM posts p
            JOIN friends f ON p.author = f.friend_id
            WHERE f.uid = ?;
            """
            results = self.execute_query(query, (uid,))
            if results:
                return results
            else:
                return []
        except Exception as e:
            print(f"Error retrieving friends' posts: {e}")

    def comment_to_post(self, uid, pid, content):
        try:
            query = """
            INSERT INTO comments (author, pid, text) VALUES (?, ?, ?);
            """
            self.execute_update(query, (uid, pid, content))
        except Exception as e:
            print(f"Error commenting on post: {e}")

    def comment_to_comment(self, uid, pid, cid, content):
        try:
            query = """
            INSERT INTO comments (author, pid, replyto, text) VALUES (?, ?, ?, ?);
            """
            self.execute_update(query, (uid, pid, cid, content))
        except Exception as e:
            print(f"Error commenting on post: {e}")

    def retrieve_comments(self, pid):
        try:
            query = """
            SELECT * 
            FROM comments 
            WHERE pid = ?;
            """
            results = self.execute_query(query, (pid,))
            if results:
                return results
            else:
                return []
        except Exception as e:
            print(f"Error retrieving comments: {e}")

    def like_comment(self, uid, cid):
        try:
            query = "INSERT INTO likes (uid, cid) VALUES (?, ?);"
            self.execute_update(query, (uid, cid))

            query = """UPDATE comments
                    SET likes = likes + 1
                    WHERE cid = ?;
                    """
            self.execute_update(query, (cid,))

            print("Comment successfully liked! Returning to details...")
        except Exception as e:
            print(f"Error liking comment: {e}")

    def dislike_comment(self, uid, cid):
        try:
            query = "INSERT INTO dislikes (uid, cid) VALUES (?, ?);"
            self.execute_update(query, (uid, cid))

            query = """UPDATE comments
                    SET dislikes = dislikes + 1
                    WHERE cid = ?;
                    """
            self.execute_update(query, (cid,))

            print("Comment successfully disliked! Returning to details...")
        except Exception as e:
            print(f"Error disliking comment: {e}")

    def like_post(self, uid, pid):
        try:
            query = "INSERT INTO likes (uid, pid) VALUES (?, ?);"
            self.execute_update(query, (uid, pid))

            query = """UPDATE posts
                    SET likes = likes + 1
                    WHERE pid = ?;
                    """
            self.execute_update(query, (pid,))

            print("Post successfully liked! Returning to details...")
        except Exception as e:
            print(f"Error liking post: {e}")

    def dislike_post(self, uid, pid):
        try:
            query = "INSERT INTO dislikes (uid, pid) VALUES (?, ?);"
            self.execute_update(query, (uid, pid))

            query = """UPDATE posts
                    SET dislikes = dislikes + 1
                    WHERE pid = ?;
                    """
            self.execute_update(query, (pid,))

            print("Post successfully disliked! Returning to details...")
        except Exception as e:
            print(f"Error disliking post: {e}")

    def has_user_liked_post(self, uid, pid):
        try:
            # Check for likes on posts
            like_query = """
            SELECT EXISTS (
                SELECT 1
                FROM likes
                WHERE uid = ? AND pid = ?
            ) AS has_liked;
            """
            self.cursor.execute(like_query, (uid, pid))
            has_liked = self.cursor.fetchone()[0] == 1
            
            return has_liked

        except Exception as e:
            print(f"Error checking if user liked the post: {e}")
            return False
        
    def has_user_disliked_post(self, uid, pid):
        try:
            # Check for dislikes on posts
            dislike_query = """
            SELECT EXISTS (
                SELECT 1
                FROM dislikes
                WHERE uid = ? AND pid = ?
            ) AS has_disliked;
            """
            self.cursor.execute(dislike_query, (uid, pid))
            has_disliked = self.cursor.fetchone()[0] == 1
            
            return has_disliked

        except Exception as e:
            print(f"Error checking if user disliked the post: {e}")
            return False
        
    def has_user_liked_comment(self, uid, cid):
        try:
            # Check for likes on comments
            like_query = """
            SELECT EXISTS (
                SELECT 1
                FROM likes
                WHERE uid = ? AND cid = ?
            ) AS has_liked;
            """
            self.cursor.execute(like_query, (uid, cid))
            has_liked = self.cursor.fetchone()[0] == 1
            
            return has_liked

        except Exception as e:
            print(f"Error checking if user liked the comment: {e}")
            return False

    def has_user_disliked_comment(self, uid, cid):
        try:
            # Check for dislikes on comments
            dislike_query = """
            SELECT EXISTS (
                SELECT 1
                FROM dislikes
                WHERE uid = ? AND cid = ?
            ) AS has_disliked;
            """
            self.cursor.execute(dislike_query, (uid, cid))
            has_disliked = self.cursor.fetchone()[0] == 1
            
            return has_disliked

        except Exception as e:
            print(f"Error checking if user disliked the comment: {e}")
            return False
        
    def remove_like_from_comment(self, uid, cid):
        try:
            # Remove the like from the likes table
            query = "DELETE FROM likes WHERE cid = ? AND uid = ?;"
            self.execute_update(query, (cid, uid))
            
            # Decrement the like count for the comment
            update_query = """
            UPDATE comments
            SET likes = likes - 1
            WHERE cid = ?;
            """
            self.execute_update(update_query, (cid,))
        except Exception as e:
            print(f"Error removing like from comment: {e}")

    def remove_dislike_from_comment(self, uid, cid):
        try:
            # Remove the dislike from the dislikes table
            query = "DELETE FROM dislikes WHERE cid = ? AND uid = ?;"
            self.execute_update(query, (cid, uid))
            
            # Decrement the dislike count for the comment
            update_query = """
            UPDATE comments
            SET dislikes = dislikes - 1
            WHERE cid = ?;
            """
            self.execute_update(update_query, (cid,))
            
        except Exception as e:
            print(f"Error removing dislike from comment: {e}")

    def remove_like_from_post(self, uid, pid):
        try:
            # Remove the like from the likes table
            query = "DELETE FROM likes WHERE pid = ? AND uid = ?;"
            self.execute_update(query, (pid, uid))
            
            # Decrement the like count for the post
            update_query = """
            UPDATE posts
            SET likes = likes - 1
            WHERE pid = ?;
            """
            self.execute_update(update_query, (pid,))
            
        except Exception as e:
            print(f"Error removing like from post: {e}")

    def remove_dislike_from_post(self, uid, pid):
        try:
            # Remove the dislike from the dislikes table
            query = "DELETE FROM dislikes WHERE pid = ? AND uid = ?;"
            self.execute_update(query, (pid, uid))
            
            # Decrement the dislike count for the post
            update_query = """
            UPDATE posts
            SET dislikes = dislikes - 1
            WHERE pid = ?;
            """
            self.execute_update(update_query, (pid,))

        except Exception as e:
            print(f"Error removing dislike from post: {e}")

    def increase_fame(self, uid):
        try:
            query = """UPDATE users
                    SET fame = fame + 1
                    WHERE uid = ?;
                    """
            self.execute_update(query, (uid,))

        except Exception as e:
            print(f"Error increasing fame: {e}")

    def decrease_fame(self, uid):
        try:
            query = """UPDATE users
                    SET fame = fame - 1
                    WHERE uid = ?;
                    """
            self.execute_update(query, (uid,))

        except Exception as e:
            print(f"Error decreasing fame: {e}")

    def retrieve_most_recent_post_by_uid(self, user_id):
        try:
            query = """
            SELECT * 
            FROM posts 
            WHERE author = ? 
            ORDER BY post_date DESC 
            LIMIT 1;
            """
            result = self.execute_query(query, (user_id,))[0]
            if result:
                return result
            else:
                return None
        except Exception as e:
            print(f"Error retrieving most recent post: {e}")

    def add_tags(self, words):
        query = "INSERT OR IGNORE INTO tags (term) VALUES (?);"
        for word in words:
            try:
                self.execute_update(query, (word,))
            except Exception as e:
                print(f"Error adding tag [{word}]: {e}")

    def add_tags_to_mentions(self, uid, pid, words):
        query = "INSERT OR IGNORE INTO mentions (author, pid, term) VALUES (?, ?, ?);"
        for word in words:
            try:
                self.execute_update(query, (uid, pid, word))
            except Exception as e:
                print(f"Error adding tag [{word}] to mentions: {e}")
            

