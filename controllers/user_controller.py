class UserController:
    def __init__(self, db_manager) -> None:
        self.db_manager = db_manager
    
    def create_user(self, new_user):
        username = new_user.get_username()
        password = new_user.get_password()
        email = new_user.get_email()

        new_uid = self.db_manager.create_new_user(username, password, email)
        return new_uid

    def retrieve_user_pass_by_id(self, user_id):
        result = self.db_manager.retrieve_user_pass_by_id(user_id)
        return result
    
    def retrieve_user_info_by_id(self, user_id):
        result = self.db_manager.retrieve_user_info_by_id(user_id)
        return result
        
    def update_user_info(self, user):
        self.db_manager.update_user_info(user)

    def update_user_pref(self, user):
        self.db_manager.update_user_pref(user)

    def send_friend_request(self, requester, requestee):
        self.db_manager.send_friend_request(requester, requestee)

    def remove_friend(self, uid_1, uid_2):
        self.db_manager.remove_friend(uid_1, uid_2)

    def check_friend_requests(self, user):
        results = self.db_manager.check_friend_requests(user)
        requests = []
        if results:
            for user_obj in results:
                requests.append((user_obj[5], user_obj[1]))
        return requests
    
    def accept_friend_request(self, requester, requestee):
        self.db_manager.accept_friend_request(requester, requestee)
    
    def reject_friend_request(self, requester, requestee):
        self.db_manager.reject_friend_request(requester, requestee)

    def retrieve_friends_list(self, user):
        result = self.db_manager.retrieve_friends_list(user)
        return result
    
    def retrieve_friends_list_only_id(self, user):
        result = self.db_manager.retrieve_friends_list_only_id(user)
        if len(result) > 0:
            new_result = []
            for friend in result:
                new_result.append(str(friend[0]))
            result = new_result
            
        return result
    
    def create_post(self, user, title, content):
        self.db_manager.create_post(user, title, content)

    def retrieve_posts_list(self, user, sort_order):
        result = self.db_manager.retrieve_posts_list(user, sort_order)
        return result
    
    def delete_post(self, pid):
        self.db_manager.delete_post(pid)

    def retrieve_friends_posts(self, user, sort_order):
        result = self.db_manager.retrieve_friends_posts(user, sort_order)
        return result
    
    def comment_to_post(self, uid, pid, content):
        self.db_manager.comment_to_post(uid, pid, content)

    def comment_to_comment(self, uid, pid, cid, content):
        self.db_manager.comment_to_comment(uid, pid, cid, content)

    def retrieve_comments(self, pid, sort_order):
        result = self.db_manager.retrieve_comments(pid, sort_order)
        return result
    
    def like_comment(self, cid, uid):
        self.db_manager.like_comment(cid, uid)

    def dislike_comment(self, cid, uid):
        self.db_manager.dislike_comment(cid, uid)

    def like_post(self, pid, uid):
        self.db_manager.like_post(pid, uid)
    
    def dislike_post(self, pid, uid):
        self.db_manager.dislike_post(pid, uid)

    def has_user_liked_comment(self, uid, cid):
        result = self.db_manager.has_user_liked_comment(uid, cid)
        return result
    
    def has_user_disliked_comment(self, uid, cid):
        result = self.db_manager.has_user_disliked_comment(uid, cid)
        return result

    def has_user_liked_post(self, uid, pid):
        result = self.db_manager.has_user_liked_post(uid, pid)
        return result

    def has_user_disliked_post(self, uid, pid):
        result = self.db_manager.has_user_disliked_post(uid, pid)
        return result
    
    def remove_like_from_post(self, uid, pid):
        self.db_manager.remove_like_from_post(uid, pid)

    def remove_dislike_from_post(self, uid, pid):
        self.db_manager.remove_dislike_from_post(uid, pid)

    def remove_like_from_comment(self, uid, cid):
        self.db_manager.remove_like_from_comment(uid, cid)

    def remove_dislike_from_comment(self, uid, cid):
        self.db_manager.remove_dislike_from_comment(uid, cid)

    def increase_fame(self, uid):
        self.db_manager.increase_fame(uid)

    def decrease_fame(self, uid):
        self.db_manager.decrease_fame(uid)

    def retrieve_most_recent_post_by_uid(self, user_id):
        result = self.db_manager.retrieve_most_recent_post_by_uid(user_id)
        return result
    
    def add_tags_to_table(self, words):
        self.db_manager.add_tags(words)

    def add_tags_to_mentions(self, uid, pid, post_tags):
        self.db_manager.add_tags_to_mentions(uid, pid, post_tags)

    def retrieve_posts_with_keywords(self, keywords):
        result = self.db_manager.retrieve_posts_with_keywords(keywords)
        return result
    
    def retrieve_posts_with_tags(self, tags):
        result = self.db_manager.retrieve_posts_with_tags(tags)
        return result

    def retrieve_top_10_liked_posts(self):
        result = self.db_manager.retrieve_top_10_liked_posts()
        return result

    def retrieve_top_10_liked_comments(self):
        result = self.db_manager.retrieve_top_10_liked_comments()
        return result

    def retrieve_top_10_most_famous_users(self):
        result = self.db_manager.retrieve_top_10_most_famous_users()
        return result

    def retrieve_top_10_liked_posts_last_24_hours(self):
        result = self.db_manager.retrieve_top_10_liked_posts_last_24_hours()
        return result

    def retrieve_users_with_name(self, name):
        result = self.db_manager.retrieve_users_with_name(name)
        return result

    
    
    
