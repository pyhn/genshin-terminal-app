from backend.utils import Utils
from frontend.general_interfaces import GenInterfaces

class SearchMenu:
    def __init__(self, user_controller, user) -> None:
        self.user_controller = user_controller
        self.user = user
        self.decision = False
        self.viewing = True
        

    def display(self):
        
        while self.decision == False or self.viewing == True:
            print("+----------------------+------------------------+")
            print("| 1. Search by Keyword | 5. View Top Posts      |")
            print("+----------------------+------------------------+")
            print("| 2. Search by Tag     | 6. View Top Users      |")
            print("+----------------------+------------------------+")
            print("| 3. View Top Posts    | 7. View Trending Posts |")
            print("+----------------------+------------------------+")
            print("| 4. View Top Comments | 8. Return to Dashboard |")
            print("+-----------------------------------------------+")

            choice = input("Enter Choice: ")
            self.handle_menu_input(choice)
    # see if we can have a query result as input to another query and sort it that way?
    def handle_menu_input(self, choice):
        options = ["1","2","3","4","5","6","7","8"]
        if choice not in options:
            print("Invalid Choice. Please Select a Valid Option.\n")
        else:
            if choice == "1":
                keywords = Utils.acquire_multi_string_input("Desired", "Post Keyword(s)")
                sort_order = GenInterfaces.acquire_sort_order("Post")
            if choice == "2":
                tags = Utils.acquire_multi_string_input("Desired", "Post Tags(s)")
                sort_order = GenInterfaces.acquire_sort_order("Post")
            if choice == "3":
                pass
            if choice == "4":
                pass
            if choice == "5":
                pass
            if choice == "6":
                pass
            if choice == "7":
                pass
            if choice == "8":
                print("Returning to Dashboard...")
                self.viewing = False
            self.decision = True

    def get_viewing(self):
        return self.viewing
    
    