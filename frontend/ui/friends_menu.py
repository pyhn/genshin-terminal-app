from .friends_list import FriendsList

class FriendsMenu:
    def __init__(self, user_controller, user) -> None:
        self.user_controller = user_controller
        self.user = user
        self.decision = False
        self.viewing = True
        

    def display(self):
        
        while self.decision == False or self.viewing == True:
            print("+--------------------------+")
            print("| 1. View Friend List      |")
            print("+--------------------------+")
            print("| 2. View Friend Activity  |")
            print("+--------------------------+")
            print("| 3. Add Friend by ID      |")
            print("+--------------------------+")
            print("| 4. Return to Dashboard   |")
            print("+--------------------------+")
            choice = input("Enter Choice: ")
            self.handle_menu_input(choice)


    def handle_menu_input(self, choice):
        options = ["1","2","3","4"]
        if choice not in options:
            print("Invalid Choice. Please Select a Valid Option.\n")
        else:
            if choice == "1":
                friends_list = FriendsList(self.user_controller, self.user)
                friends_list.display()
                # self.viewing = friends_list.get_viewing()
            if choice == "3":
                self.add_by_id()
            if choice == "4":
                print("Returning to Dashboard...")
                self.viewing = False
            
            self.decision = True

    def get_viewing(self):
        return self.viewing
    
    def add_by_id(self):
        confirmed = False
        while not confirmed:
            user_id = input(f"Enter User ID: ")
            if user_id == self.user.get_uid():
                print("You cannot add yourself.")
            else:
                result = self.user_controller.get_user_info_by_id(user_id)
                if result == None:
                    print("Invalid User ID")
                else:
                    username = result[1]
                    confirm_input = input(f"Add {username}? (y/n): ").lower().strip()

                    while confirm_input not in ["y", "n"]:
                        print("Please choose a valid option.")
                        confirm_input = input(f"Add {username}? (y/n): ").lower().strip()

                    if confirm_input == "y":
                        confirmed = True
                        self.user_controller.send_friend_request(self.user.get_uid(), user_id)
                    
                    
