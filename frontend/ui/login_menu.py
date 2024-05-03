class login_menu:
    def __init__(self) -> None:
        self.user = None
        self.password = None
        self.attempts = 0
        self.logged_in = False
  
    def get_logged_in(self):
        return self.logged_in

    def get_user(self):
        return self.user

    def display_menu(self):
        while self.attempts < 4 and self.logged_in == False:
            self.user = input("Enter Username: ")
            self.password = input("Enter Password: ")
            self.handle_user_inputs()
                
        if self.attempts > 3:
            print(f"Too Many Attempts. Returning to Main Menu")

    def handle_user_inputs(self):
        if self.user == "pog" and self.password == "pyhn":
                print(f"Log In Successful\n")
                self.logged_in = True
        else :
            if self.user != "pog":
                print(f"Invalid Username.\n")
            else:
                print(f"Invalid Password.\n")
            self.attempts += 1


