from .user_profile import UserProfile
from .friends_menu import FriendsMenu
from .user_notifications import UserNotifications
from .posts_menu import PostsMenu
class DashboardMenu:
    def __init__(self, user_controller) -> None:
        self.user = None
        self.logged_in = False
        self.decision = False
        self.user_controller = user_controller
        self.viewing = False
        self.notif_count = 0
        self.requests = None

    def get_logged_in(self):
        return self.logged_in

    def set_default(self):
        self.user = None
        self.logged_in = False
        self.decision = False
        self.viewing = False
        self.notif_count = 0
        self.requests = None

    def set_logged_in(self, logged_in):
        self.logged_in = logged_in

    def display(self):
        while self.decision == False and self.viewing == False:
            count_len = len(str(self.notif_count))
            num_spaces = max(41 - count_len, 0)
            dash_string = f"| Dashboard   | You have {self.notif_count} Notifications " + " " * num_spaces + "|" 
            print()
            print("+-------------+------------------------------------------------------------------+")
            print(dash_string)
            print("+-------------+------------------------------------------------------------------+")
            print("| 1. Profile  | 2. Friends | 3. Posts | 4. Search | 5. Notifications | 6. Logout |")
            print("+-------------+------------------------------------------------------------------+")
            choice = input("Enter Choice: ")
            self.handle_menu_input(choice)

    def handle_menu_input(self, choice):
        options = ["1","2","3","4","5","6"]
        if choice not in options:
            print("Invalid Choice. Please Select a Valid Option.\n")
        else:
            if choice == "1":
                profile = UserProfile(self.user_controller, self.user)
                profile.display()
                self.viewing = profile.get_viewing()

            if choice == "2":
                friends_menu = FriendsMenu(self.user_controller, self.user)
                friends_menu.display()
                self.viewing = friends_menu.get_viewing()

            if choice == "3":
                posts_menu = PostsMenu(self.user_controller, self.user)
                posts_menu.display()
                self.viewing = posts_menu.get_viewing()

            if choice == "4":
                print("Visiting Search.")

            if choice == "5":
                notifs = UserNotifications(self.user_controller, self.user, self.requests)
                notifs.display()
                self.viewing = notifs.get_viewing()
                
            if choice == "6":
                print("Logging out...")
                self.logged_in = False
                self.user = None
                self.viewing = True

            self.decision = True

    def set_user(self, user):
        self.user = user

    def check_friend_requests(self):
        result = self.user_controller.check_friend_requests(self.user)
        self.notif_count = len(result)
        self.requests = result
    
    

        