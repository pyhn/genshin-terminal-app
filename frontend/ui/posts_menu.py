from .posts_list import PostsList

class PostsMenu:
    def __init__(self, user_controller, user) -> None:
        self.user_controller = user_controller
        self.user = user
        self.decision = False
        self.viewing = True
        

    def display(self):
        
        while self.decision == False or self.viewing == True:
            print("+--------------------------+")
            print("| 1. View My Posts         |")
            print("+--------------------------+")
            print("| 2. Create Posts          |")
            print("+--------------------------+")
            print("| 3. Return to Dashboard   |")
            print("+--------------------------+")

            choice = input("Enter Choice: ")
            self.handle_menu_input(choice)


    def handle_menu_input(self, choice):
        options = ["1","2","3","4"]
        if choice not in options:
            print("Invalid Choice. Please Select a Valid Option.\n")
        else:
            if choice == "1":
                posts_list = PostsList(self.user_controller, self.user)
                posts_list.display()
            if choice == "2":
                post_title = self.acquire_post_info("Title")
                post_content = self.acquire_post_info("Content")
                self.user_controller.create_post(self.user, post_title, post_content)
            if choice == "3":
                print("Returning to Dashboard...")
                self.viewing = False
            self.decision = True

    def get_viewing(self):
        return self.viewing
    
    def acquire_post_info(self, info_type):
        confirmed = False
        while not confirmed:
            user_input = input(f"Enter Desired {info_type.capitalize()}: ")
            confirm_input = input(f"Accept {info_type.capitalize()}? (y/n): ").lower().strip()

            while confirm_input not in ["y", "n"]:
                print("Please choose a valid option.")
                confirm_input = input(f"Accept {info_type.capitalize()}? (y/n): ").lower().strip()

            if confirm_input == "y":
                confirmed = True
                return user_input
    
    
    