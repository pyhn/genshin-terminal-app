class sign_up_menu:
    def __init__(self) -> None:
        self.user = None
        self.password = None
        self.logged_in = False

    def display_sign_up(self):
        username = self.acquire_user_info("username")
        password = self.acquire_user_info("password")
        email = self.acquire_user_info("email")

        confirm_options = ["y", "n"]
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
    
    def acquire_user_info(self, info_type):
        confirm_options = ["y", "n"]
        confirmed = False
        
        while not confirmed:
            user_input = input(f"Enter Desired {info_type.capitalize()}: ")
            confirm_input = input(f"Accept {info_type.capitalize()}? (y/n): ").lower().strip()
            
            if confirm_input in confirm_options:
                if confirm_input == confirm_options[0]:
                    confirmed = True
                    return user_input
                else:
                    confirmed = False
            else:
                print("Please choose a valid option.")

    def handle_user_inputs(self, temp, is_user):
        if is_user:
            self.user = temp
        else:
            self.password = temp
    
           
           