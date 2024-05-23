# Genshin Terminal App

Genshin Terminal App is a terminal-based application designed to manage user profiles, friend requests, posts, and comments within the context of a Genshin Impact community. The app uses SQLite for data storage and management.

## Features

- User Management: Create, update, and delete user profiles.
- Friend Requests: Send, accept, and reject friend requests.
- Friends List: View a list of friends and manage friendships.
- Posts: Create, view, and delete posts.
- Comments: Add comments to posts, reply to other comments.

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/genshin-terminal-app.git
    cd genshin-terminal-app
    ```

2. **Set Up the Database**:
    Run the following Python script to create the necessary tables and insert test data.
    ```bash
    python create_db.py
    ```

## Usage

1. **Run the Application**:
    ```bash
    python main.py
    ```

2. **Navigate the Menus**:
    - **Dashboard**: View notifications and navigate to other menus.
    - **User Menu**: Manage user profiles.
    - **Friends Menu**: Send, accept, and reject friend requests.
    - **Posts Menu**: Create, view, and delete posts.
    - **Comments Menu**: Add and manage comments on posts.

## Database Schema

### Tables

- **users**:
    ```sql
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
    ```

- **friend_requests**:
    ```sql
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
    ```

- **friends**:
    ```sql
    CREATE TABLE IF NOT EXISTS friends (
        uid INTEGER,
        friend_id INTEGER,
        start_date DATE DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY (uid, friend_id),
        FOREIGN KEY (uid) REFERENCES users(uid) ON DELETE CASCADE,
        FOREIGN KEY (friend_id) REFERENCES users(uid) ON DELETE CASCADE
    );
    ```

- **posts**:
    ```sql
    CREATE TABLE IF NOT EXISTS posts (
        pid INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        body TEXT NOT NULL,
        uid INTEGER,
        post_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (uid) REFERENCES users(uid) ON DELETE CASCADE
    );
    ```

- **comments**:
    ```sql
    CREATE TABLE IF NOT EXISTS comments (
        cid INTEGER PRIMARY KEY AUTOINCREMENT,
        uid INTEGER,
        replyto INTEGER DEFAULT NULL,
        pid INTEGER,
        comment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        text TEXT NOT NULL,
        FOREIGN KEY (uid) REFERENCES users(uid) ON DELETE CASCADE,
        FOREIGN KEY (pid) REFERENCES posts(pid) ON DELETE CASCADE,
        FOREIGN KEY (replyto) REFERENCES users(uid) ON DELETE CASCADE
    );
    ```

## Example Code Snippets

### Database Connection

```python
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
```

### Sending a Friend Request

```python
def send_friend_request(self, requester, requestee):
    try:
        query = """
        INSERT INTO friend_requests (requester_id, requestee_id) VALUES (?, ?)
        """
        self.execute_update(query, (requester, requestee))
        print("Friend Request Sent. Returning to Friends Menu...")
    except sqlite3.IntegrityError as e:
        print(f"Failed to send friend request. Returning to Friends Menu.")
```

### Accepting a Friend Request

```python
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
```
