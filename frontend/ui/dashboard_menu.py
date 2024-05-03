class dashboard_menu:
    def __init__(self) -> None:
        self.user = None
        self.logged_in = False
        self.decision = False
    
    def set_user(self, user):
        self.user = user

    def set_logged_in(self, logged_in):
        self.logged_in = logged_in

    def display(self):
        print(f"Welcome {self.user} to your Dashboard")
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
                print("Visiting Profile.")
            if self.choice == "2":
                print("Visiting Friends.")
            if self.choice == "3":
                print("Visiting Search.")
            self.decision = True


        