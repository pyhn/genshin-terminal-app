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



