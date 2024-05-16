class EditUserProfile:
    def __init__(self, user_controller, user) -> None:
        self.user_controller = user_controller
        self.user = user
        self.decision = False
    
    def display(self):
        print("+------------------------------+")
        print("| 1. Edit Status | 2. Edit Bio |")
        print("+------------------------------+")
        print("| 3. Edit Favourite Character  |")
        print("+------------------------------+")
        print("| 4. Edit Favourite Region     |")
        print("+------------------------------+")
        print("| 5. Return to User Profile    |")
        print("+------------------------------+")
        while self.decision == False:
            choice = input("Enter Choice: ")
            self.handle_menu_input(choice)

    def handle_menu_input(self, choice):
        options = ["1","2","3","4","5"]
        if choice not in options:
            print("Invalid Choice. Please Select a Valid Option.\n")
        else:
            if choice == "1":
                info_type = "Status"
            if choice == "2":
                info_type = "Bio"
            if choice == "3":
                info_type = "Favourite Character"
            if choice == "4":
                info_type = "Favourite Region"
            if choice == "5":
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
        if info_type == "Status":
            self.user.set_status(new_info)
        if info_type == "Bio":
            self.user.set_bio(new_info)
        if info_type == "Favourite Character":
            self.user.set_fav_character(new_info)
        if info_type == "Favourite Region":
            self.user.set_fav_region(new_info)

        self.user_controller.update_user_info(self.user)
        
