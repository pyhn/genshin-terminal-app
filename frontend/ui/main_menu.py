from .login_menu import login_menu # import locally
from .sign_up_menu import sign_up_menu
class main_menu:
    def __init__(self) -> None:
        self.choice = None
        self.decision = False
        self.logged_in = False
        self.shutdown = False
        self.user = None

    def display_menu(self):
        while self.decision == False or self.logged_in == False:
            print(f"1. Login")
            print(f"2. Sign Up")
            print(f"3. Exit")
            self.choice = input("Enter Choice: ")
            self.handle_menu_input()
            if self.shutdown:
                break

    def handle_menu_input(self):
        options = ["1","2","3"]
        if self.choice not in options:
            print("Invalid Choice. Please Select a Valid Option.\n")
        else:
            if self.choice == "1":
                login = login_menu()
                login.display_menu()
                self.logged_in = login.get_logged_in()
                self.user = login.get_user()


            if self.choice == "2":
                sign_up = sign_up_menu()
                sign_up.display_sign_up()
                self.logged_in = sign_up.get_logged_in()
                if self.logged_in:
                    self.user = sign_up.get_user()

            if self.choice == "3":
                self.shutdown = True
            self.decision = True

    def get_logged_in(self):
        return self.logged_in
    
    def get_shutdown(self):
        return self.shutdown

    def get_user(self):
        return self.user


