from .user_profile import UserProfile
class DashboardMenu:
    def __init__(self, user_controller, user) -> None:
        self.user = user
        self.logged_in = False
        self.decision = False
        self.user_controller = user_controller

    def set_logged_in(self, logged_in):
        self.logged_in = logged_in

    def display(self):
        print(f"Welcome {self.user.get_username()} to your Dashboard")
        print("+-------------------------------------+")
        print("| 1. Profile | 2. Friends | 3. Search |")
        print("+-------------------------------------+")
        while self.decision == False:
            self.choice = input("Enter Choice: ")
            self.handle_menu_input()

    def handle_menu_input(self):
        options = ["1","2","3"]
        if self.choice not in options:
            print("Invalid Choice. Please Select a Valid Option.\n")
        else:
            if self.choice == "1":
                profile = UserProfile(self.user_controller, self.user)
                profile.display()
            if self.choice == "2":
                print("Visiting Friends.")
            if self.choice == "3":
                print("Visiting Search.")
            self.decision = True


        