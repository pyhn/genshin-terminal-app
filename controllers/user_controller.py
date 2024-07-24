class UserController:
    def __init__(self, db_manager) -> None:
        self.db_manager = db_manager
    
    def create_user(self, new_user):
        username = new_user.get_username()
        password = new_user.get_password()
        email = new_user.get_email()

        new_uid = self.db_manager.create_new_user(username, password, email)
        return new_uid

    def get_user_pass_by_id(self, user_id):
        result = self.db_manager.get_user_pass_by_id(user_id)
        return result
    
    def get_user_info_by_id(self, user_id):
        result = self.db_manager.get_user_info_by_id(user_id)
        return result
        
    def update_user_info(self, user):
        self.db_manager.update_user_info(user)

    def update_user_pref(self, user):
        self.db_manager.update_user_pref(user)

    def send_friend_request(self, requester, requestee):
        self.db_manager.send_friend_request(requester, requestee)

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

    def retrieve_posts_list(self, user):
        result = self.db_manager.retrieve_posts_list(user)
        return result
    
    def delete_post(self, pid):
        self.db_manager.delete_post(pid)

    def retrieve_friends_posts(self, user):
        result = self.db_manager.retrieve_friends_posts(user)
        return result
    
    def comment_to_post(self, uid, pid, content):
        self.db_manager.comment_to_post(uid, pid, content)

    def comment_to_comment(self, uid, pid, cid, content):
        self.db_manager.comment_to_comment(uid, pid, cid, content)

    def retrieve_comments(self, pid):
        result = self.db_manager.retrieve_comments(pid)
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

    
    
    
