class UserPreferences:
    def __init__(self, user_controller, user) -> None:
        self.user_controller = user_controller
        self.user = user
        self.decision = False
    
    def display(self):
        print("+------------------------------+")
        print("| 1. Update Username           |")
        print("+------------------------------+")
        print("| 2. Update Password           |")
        print("+------------------------------+")
        print("| 3. Update Email              |")
        print("+------------------------------+")
        print("| 4. Return to User Profile    |")
        print("+------------------------------+")
        while self.decision == False:
            choice = input("Enter Choice: ")
            self.handle_menu_input(choice)

    def handle_menu_input(self, choice):
        options = ["1","2","3","4"]
        if choice not in options:
            print("Invalid Choice. Please Select a Valid Option.\n")
        else:
            if choice == "1":
                info_type = "Username"
            if choice == "2":
                info_type = "Password"
            if choice == "3":
                info_type = "Email"
            if choice == "4":
                self.decision = True
                return

            self.decision = True
            new_info = self.acquire_user_input(info_type)
            self.update_user(info_type, new_info)
    
    def acquire_user_input(self, info_type):
        confirmed = False
        while not confirmed:
            user_input = input(f"Enter New {info_type.capitalize()}: ")
            confirm_input = input(f"Accept {info_type.capitalize()}? (y/n): ").lower().strip()

            while confirm_input not in ["y", "n"]:
                print("Please choose a valid option.")
                confirm_input = input(f"Accept {info_type.capitalize()}? (y/n): ").lower().strip()

            if confirm_input == "y":
                confirmed = True
                return user_input
    
    def update_user(self, info_type, new_info):
        if info_type == "Username":
            self.user.set_username(new_info)
        if info_type == "Password":
            self.user.set_password(new_info)
        if info_type == "Email":
            self.user.set_email(new_info)

        self.user_controller.update_user_pref(self.user)