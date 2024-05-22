from data.db_manager import DatabaseManager

def main():
    db = DatabaseManager()
    db.connect()

    db.drop_table("comments")
    db.drop_table("friends")
    db.drop_table("friend_requests")
    db.drop_table("posts")
    db.drop_table("users")
    

    db.create_user_table()
    db.create_posts_table()
    db.create_friend_request_table()
    db.create_friends_table()
    db.create_comments_table()
    
    db.insert_test_data()
    
    
    

    db.disconnect()

main()