from data.user import User

class SignUpMenu:
    def __init__(self, user_controller, user):
        self.logged_in = False
        self.user = user
        self.user_controller = user_controller

    def display_sign_up(self):
        username = self.acquire_user_info("username")
        password = self.acquire_user_info("password")
        email = self.acquire_user_info("email")

        new_user = User()
        new_user.set_username(username)
        new_user.set_password(password)
        new_user.set_email(email)

        if self.confirm_login():
            self.logged_in = True
            print("Log In Successful\n")
        else:
            print(f"Thank you for signing up, {new_user.username}! Returning to Main Menu...")

        self.user = new_user

    def get_user(self):
        return self.user

    def confirm_login(self):
        confirm_options = ["y", "n"]
        confirm_login = input("Log In? (y/n): ").lower().strip()
        while confirm_login not in confirm_options:
            print("Please choose a valid option.")
            confirm_login = input("Log In? (y/n): ").lower().strip()
        return confirm_login == confirm_options[0]

    def acquire_user_info(self, info_type):
        confirmed = False
        while not confirmed:
            user_input = input(f"Enter Desired {info_type.capitalize()}: ")
            confirm_input = input(f"Accept {info_type.capitalize()}? (y/n): ").lower().strip()

            while confirm_input not in ["y", "n"]:
                print("Please choose a valid option.")
                confirm_input = input(f"Accept {info_type.capitalize()}? (y/n): ").lower().strip()

            if confirm_input == "y":
                confirmed = True
                return user_input
