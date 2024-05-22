class PostsMenu:
    def __init__(self, user_controller, user) -> None:
        self.user_controller = user_controller
        self.user = user
        self.decision = False
        self.viewing = True
        

    def display(self):
        
        while self.decision == False or self.viewing == True:
            print("+--------------------------+")
            print("| 1. Create Posts          |")
            print("+--------------------------+")
            print("| 2. Delete Posts          |")
            print("+--------------------------+")
            print("| 3. Return to Dashboard   |")
            print("+--------------------------+")

            choice = input("Enter Choice: ")
            self.handle_menu_input(choice)


    def handle_menu_input(self, choice):
        options = ["1","2","3"]
        if choice not in options:
            print("Invalid Choice. Please Select a Valid Option.\n")
        else:
            if choice == "1":
                pass
            if choice == "2":
                pass
            if choice == "3":
                print("Returning to Dashboard...")
                self.viewing = False
            self.decision = True

    def get_viewing(self):
        return self.viewing