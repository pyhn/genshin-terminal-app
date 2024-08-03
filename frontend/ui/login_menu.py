import getpass
from data.user import User

class LogInMenu:
    def __init__(self, user_controller) -> None:
        self.user = None
        self.logged_in = False
        self.attempts = 0
        self.user_controller = user_controller
  
    def get_logged_in(self):
        return self.logged_in

    def get_user(self):
        return self.user

    def display_menu(self):
        while self.attempts < 4 and self.logged_in == False:
            user_id = input("Enter User ID: ")
            password = getpass.getpass("Enter Password: ")
            self.handle_user_inputs(user_id, password)
                
        if self.attempts > 3:
            print(f"Too Many Attempts. Returning to Main Menu")

    def handle_user_inputs(self, user_id, password):
        result = self.user_controller.retrieve_user_pass_by_id(user_id)
        
        if result is None:
            print("Invalid User ID or Password.")
            self.attempts += 1
        elif password != result[1]:
            print("Invalid Password.")
            self.attempts += 1
        else:
            self.user = self.initialize_user(user_id)
            print("Log In Successful")
            self.logged_in = True

    def initialize_user(self, user_id):

        result = self.user_controller.retrieve_user_info_by_id(user_id)
        user = User()
        user.set_uid(user_id)
        user.set_username(result[1])
        user.set_password(result[2])
        user.set_email(result[3])
        user.set_status(result[4])
        user.set_bio(result[5])
        user.set_fav_character(result[6])
        user.set_fav_region(result[7])
        return user



