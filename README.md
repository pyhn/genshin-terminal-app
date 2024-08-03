# Genshin Terminal App

Genshin Terminal App is a terminal-based application designed to manage user profiles, friend requests, posts, and comments within the context of a Genshin Impact community. The app uses SQLite for data storage and management.

## Features

- User Management: Create, update, and delete user profiles.
- Friend Requests: Send, accept, and reject friend requests.
- Friends List: View a list of friends and manage friendships.
- Posts: Create, view, and delete posts.
- Search: Search based on keyword, tag, user, or view top posts, comments, users, or trending posts.
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
