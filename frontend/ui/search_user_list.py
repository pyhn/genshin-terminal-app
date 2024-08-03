from .search_user_details import SearchUserDetails

class SearchUserList:
    def __init__(self, user_controller, user, user_list, search_type) -> None:
        self.user_controller = user_controller
        self.user = user
        self.decision = False
        self.viewing = True
        self.user_list = user_list
        self.search_type = search_type

    def display(self):
        while self.decision == False or self.viewing == True:
            welcome_string = f"| {self.search_type} Results |"
            border_length = max(len(welcome_string) - 2, 0)  # ensure length is not negative
            border_string = "+" + "-" * border_length + "+"
            print(border_string)
            print(welcome_string)
            print(border_string)
            
            for i,search_user in enumerate(self.user_list): #here
                print(f"{i + 1}. User Id: {search_user[0]} Username: {search_user[1]}, Status: {search_user[4]}")
            choice = input("Enter Choice [or Enter to Return to Users Menu]: ")
            self.handle_menu_input(choice)

    def handle_menu_input(self, choice):
        if choice.strip() == "":
            print("Returning to Users Menu...")
            self.viewing = False
        else:
            try:
                choice = int(choice)
                if 0 < choice <= len(self.user_list):
                    self.handle_user_choice(choice)
                else:
                    raise ValueError
            except ValueError:
                print("Invalid Choice. Please Select a Valid Option.\n")
        self.decision = True
    
    def handle_user_choice(self, choice):
        index = choice - 1
        user_info = self.user_list[index]
        users_details = SearchUserDetails(self.user_controller, self.user, user_info)
        users_details.display()
        

