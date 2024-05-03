class sign_up_menu:
    def __init__(self) -> None:
        self.user = None
        self.password = None
        self.logged_in = False

    def display_sign_up(self):
        user_confirmed = False
        while not user_confirmed:
            confirm_options = ["y","n"]
            temp_user = input("Enter Desired Username: ")
            user_confirm_input = input("Accept Username? (y/n): ").lower().strip()
            if user_confirm_input in confirm_options:
                if user_confirm_input == confirm_options[0]:
                    self.handle_user_inputs(temp_user, True)
                    user_confirmed = True
                else:
                     user_confirmed = False
            else:
                print("Please choose a valid option. ")

        pass_confirmed = False
        while not pass_confirmed:
            temp_pass = input("Enter Desired Password: ")
            pass_confirm_input = input("Accept Password? (y/n): ").lower().strip()
            if pass_confirm_input in confirm_options:
                if pass_confirm_input == confirm_options[0]:
                    self.handle_user_inputs(temp_pass, False)
                    pass_confirmed = True
                else:
                    pass_confirmed = False
            else:
                print("Please choose a valid option. ")
        
        confirm_login = input("Log In? (y/n): ").lower().strip()
        if confirm_login in confirm_options:
            if confirm_login == confirm_options[0]:
                self.logged_in = True
                print(f"Log In Successful\n")
            else:
                print(f"Thank you for signing up {self.user}! Returning to Main Menu...")
        else:
           print(f"Thank you for signing up {self.user}! Returning to Main Menu...")
        
    def get_logged_in(self):
        return self.logged_in
    def get_user(self):
        return self.user
    
    def handle_user_inputs(self, temp, is_user):
        if is_user:
            self.user = temp
        else:
            self.password = temp
    
           
           