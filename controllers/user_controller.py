class UserController:
    def __init__(self, db_manager) -> None:
        self.db_manager = db_manager
    
    def create_user(self, new_user):
        username = new_user.get_username()
        password = new_user.get_password()
        email = new_user.get_email()

        self.db_manager.create_new_user(username, password, email)

    def get_user_pass_by_id(self, user_id):
        username, password = self.db_manager.get_user_pass_by_id(user_id)
        return username, password
    
    def get_user_pass_by_id(self, user_id):
        result = self.db_manager.get_user_info_by_id(user_id)
        return result
        



