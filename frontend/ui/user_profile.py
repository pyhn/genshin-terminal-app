from .edit_user_profile import EditUserProfile
from .user_preferences import UserPreferences
from backend.utils import Utils

class UserProfile:
    def __init__(self, user_controller, user) -> None:
        self.user_controller = user_controller
        self.user = user
        self.decision = False
        self.viewing = True
        

    def display(self):
        print()
        print(f"[Welcome {self.user.get_username()}.]")
        print(f"Current Status: {self.user.get_status()}")
        print(f"Bio: {Utils.format_content(self.user.get_bio())}")
        print(f"Favourite Character: {self.user.get_fav_character()}")
        print(f"Favourite Region: {self.user.get_fav_region()}\n")


        while self.decision == False or self.viewing == True:
            print(f"+------------------------+")
            print(f"| 1. Edit Profile        |")
            print(f"+------------------------+")
            print(f"| 2. User Preferences    |")
            print(f"+------------------------+")
            print(f"| 3. Return to Dashboard |")
            print(f"+------------------------+")
            choice = input("Enter Choice: ")
            self.handle_menu_input(choice)
            
    def handle_menu_input(self, choice):
        options = ["1","2","3"]
        if choice not in options:
            print("Invalid Choice. Please Select a Valid Option.\n")
        else:
            if choice == "1":
                edit_profile = EditUserProfile(self.user_controller, self.user)
                edit_profile.display()
            if choice == "2":
                user_pref = UserPreferences(self.user_controller, self.user)
                user_pref.display()
            if choice == "3":
                print("Returning to Dashboard...")
                self.viewing = False
            
            self.decision = True

    def get_viewing(self):
        return self.viewing


        