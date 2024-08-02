from .post_details import PostDetails
from backend.utils import Utils
from frontend.general_interfaces import GenInterfaces
class PostsList:
    def __init__(self, user_controller, user) -> None:
        self.user_controller = user_controller
        self.user = user
        self.decision = False
        self.viewing = True
        self.posts_list = None


    def retrieve_posts_list(self, sort_order):
        self.posts_list = self.user_controller.retrieve_posts_list(self.user, sort_order)

    def display(self):
        while self.decision == False or self.viewing == True:
            print("+-------------------------------+")
            print("| Welcome to your Posts List    |")
            print("+-------------------------------+")
            sort_order = GenInterfaces.acquire_sort_order("post")
            self.retrieve_posts_list(sort_order)
            post_count = len(self.posts_list)

            if post_count == 0:
                input("You have 0 Posts. Press Enter to Return to Posts Menu.")
                break
            
            for i,post in enumerate(self.posts_list): #here
                print(f"{i + 1}. [Title]: {post[1]} [Content]: {Utils.truncate_string(post[2])}")
            choice = input("Enter Choice [or Enter to Return to Posts Menu]: ")
            self.handle_menu_input(choice)

    def handle_menu_input(self, choice):
        if choice.strip() == "":
            print("Returning to Posts Menu...")
            self.viewing = False
        else:
            try:
                choice = int(choice)
                if 0 < choice <= len(self.posts_list):
                    self.handle_post_choice(choice)
                    
                else:
                    raise ValueError
            except ValueError:
                print("Invalid Choice. Please Select a Valid Option.\n")
        self.decision = True

    def handle_post_choice(self, choice):
        index = choice - 1
        post_info = self.posts_list[index]
        post_details = PostDetails(self.user_controller, self.user, post_info)
        post_details.display()
        

    