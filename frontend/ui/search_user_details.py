from backend.utils import Utils

class SearchUserDetails:
    def __init__(self, user_controller, user, user_info) -> None:
        self.user_controller = user_controller
        self.user = user
        self.decision = False
        self.viewing = True
        self.user_info = user_info
        
    def display(self):
        print() 
        user_name = self.user_info[1]
        user_bio = self.user_info[5]
        user_fav_char = self.user_info[6]
        user_fav_region = self.user_info[7]
        print(f"User: {user_name}")
        print(f"Bio: {Utils.format_content(user_bio)}")
        print(f"Favourite Character: {user_fav_char}")
        print(f"Favourite Region: {user_fav_region}")
        while self.decision == False or self.viewing == True:
            print("+--------------------------+")
            print("| 1. Add User              |")
            print("+--------------------------+")
            print("| 2. Return to Search List |")
            print("+--------------------------+")
            choice = input("Enter Choice: ")
            self.handle_menu_input(choice, user_name)


    def handle_menu_input(self, choice, user_name):
        options = ["1","2"]
        if choice not in options:
            print("Invalid Choice. Please Select a Valid Option.\n")
        else:
            if choice == "1":
                self.confirm_add(user_name)
            if choice == "2":
                print("Returning to Search List...")
                self.viewing = False
            
            self.decision = True

    def get_viewing(self):
        return self.viewing
        
    def confirm_add(self, user_name):
        confirm_options = ["y", "n"]
        confirm_login = input(f"Add {user_name}? (y/n): ").lower().strip()
        while confirm_login not in confirm_options:
            print("Please choose a valid option.")
            confirm_login = input(f"Add {user_name}? (y/n): ").lower().strip()
        
        if confirm_login == "y":
            self.add_user()

    def add_user(self):
        friends_list = self.user_controller.retrieve_friends_list_only_id(self.user)
        user_id = str(self.user_info[0])
        
        if user_id == self.user.get_uid():
            print("You cannot add yourself.")

        elif user_id in friends_list:
            print("You already added this user!")
        else:
            self.user_controller.send_friend_request(self.user.get_uid(), user_id)
                
