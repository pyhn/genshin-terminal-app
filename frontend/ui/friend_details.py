from backend.utils import Utils

class FriendDetails:
    def __init__(self, user_controller, user, friend_info) -> None:
        self.user_controller = user_controller
        self.user = user
        self.decision = False
        self.viewing = True
        self.friend_info = friend_info
        
    def display(self):
        print() 
        friend_name = self.friend_info[1]
        friend_bio = self.friend_info[5]
        friend_fav_char = self.friend_info[6]
        friend_fav_region = self.friend_info[7]
        print(f"User: {friend_name}")
        print(f"Bio: {Utils.format_content(friend_bio)}")
        print(f"Favourite Character: {friend_fav_char}")
        print(f"Favourite Region: {friend_fav_region}")
        while self.decision == False or self.viewing == True:
            print("+--------------------------+")
            print("| 1. Remove Friend         |")
            print("+--------------------------+")
            print("| 2. Return to Friend List |")
            print("+--------------------------+")
            choice = input("Enter Choice: ")
            self.handle_menu_input(choice)


    def handle_menu_input(self, choice):
        options = ["1","2"]
        if choice not in options:
            print("Invalid Choice. Please Select a Valid Option.\n")
        else:
            if choice == "1":
                self.confirm_remove()
            if choice == "2":
                print("Returning to Friends List...")
                self.viewing = False
            
            self.decision = True

    def get_viewing(self):
        return self.viewing
        
    def confirm_remove(self):
        confirm_options = ["y", "n"]
        confirm_login = input("Remove friend? (y/n): ").lower().strip()
        while confirm_login not in confirm_options:
            print("Please choose a valid option.")
            confirm_login = input("Log In? (y/n): ").lower().strip()
        
        if confirm_login == "y":
            uid = self.user.get_uid()
            friend_id = self.friend_info[0]
            self.user_controller.remove_friend(uid, friend_id)
            print("Friend has successfully been removed!")
            self.user_controller.decrease_fame(uid)
            self.user_controller.decrease_fame(friend_id)
            
            self.viewing = False
