from backend.utils import Utils
from .friend_details import FriendDetails

class FriendsList:
    def __init__(self, user_controller, user) -> None:
        self.user_controller = user_controller
        self.user = user
        self.decision = False
        self.viewing = True
        self.friends_list = None


    def retrieve_friends_list(self):
        self.friends_list = self.user_controller.retrieve_friends_list(self.user)

    def display(self):
        while self.decision == False or self.viewing == True:
            self.retrieve_friends_list()
            friend_count = len(self.friends_list)
            print("+-------------------------------+")
            print("| Welcome to your Friends List  |")
            print("+-------------------------------+")

            if friend_count == 0:
                input("You have 0 Friends Added. Press Enter to Return to Friends Menu.")
                break
            
            for i,friend in enumerate(self.friends_list):
                print(f"{i + 1}. Username: {friend[1]}, Status: {friend[4]}")
            choice = input("Enter Choice [or Enter to Return to Friends Menu]: ")
            self.handle_menu_input(choice)

    def handle_menu_input(self, choice):
        if choice.strip() == "":
            print("Returning to Friends Menu...")
            self.viewing = False
        else:
            try:
                choice = int(choice)
                if 0 < choice <= len(self.friends_list):
                    self.handle_friend_choice(choice)
                else:
                    raise ValueError
            except ValueError:
                print("Invalid Choice. Please Select a Valid Option.\n")
        self.decision = True
    
    def handle_friend_choice(self, choice):
        index = choice - 1
        friend_info = self.friends_list[index]
        friends_details = FriendDetails(self.user_controller, self.user, friend_info)
        friends_details.display()
        

