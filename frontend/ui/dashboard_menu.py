from .user_profile import UserProfile
class DashboardMenu:
    def __init__(self, user_controller, user) -> None:
        self.user = user
        self.logged_in = True
        self.decision = False
        self.user_controller = user_controller
        self.viewing = False

    def get_logged_in(self):
        return self.logged_in

    def set_logged_in(self, logged_in):
        self.logged_in = logged_in

    def display(self):
        while self.decision == False or self.viewing == False:
            print()
            print("+------------+")
            print("| Dashboard  |")
            print("+------------+------------------------------------+")
            print("| 1. Profile | 2. Friends | 3. Search | 4. Logout |")
            print("+-------------------------------------------------+")
            choice = input("Enter Choice: ")
            self.handle_menu_input(choice)

    def handle_menu_input(self, choice):
        options = ["1","2","3","4"]
        if choice not in options:
            print("Invalid Choice. Please Select a Valid Option.\n")
        else:
            if choice == "1":
                profile = UserProfile(self.user_controller, self.user)
                profile.display()
                self.viewing = profile.get_viewing()
            if choice == "2":
                print("Visiting Friends.")
            if choice == "3":
                print("Visiting Search.")
            if choice == "4":
                print("Logging out...")
                self.logged_in = False
                self.viewing = True

            self.decision = True

    def set_decision(self, decision):
        self.decision = decision
        