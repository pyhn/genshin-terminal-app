from .comment_details import CommentDetails
from backend.utils import Utils
from frontend.general_interfaces import GenInterfaces

class PostComments:
    def __init__(self, user_controller, user, pid) -> None:
        self.user_controller = user_controller
        self.pid = pid
        self.user = user
        self.decision = False
        self.viewing = True
        self.comments_list = None


    def retrieve_comments(self, sort_order):
        self.comments_list = self.user_controller.retrieve_comments(self.pid, sort_order)

    def display(self):
        while self.decision == False or self.viewing == True:
            print("+----------------------+")
            print("| Viewing all comments |")
            print("+----------------------+")

            sort_order = GenInterfaces.acquire_sort_order("comment")
            self.retrieve_comments(sort_order)
            comment_count = len(self.comments_list)

            if comment_count == 0:
                input("This post has no comments. Returning to Post Details.")
                break
            
            for i, comment in enumerate(self.comments_list): #here
                author_info = self.user_controller.get_user_info_by_id(comment[1])
                author_name = author_info[1]
                print(f"{i + 1}. [Author]: {author_name} [Content]: {Utils.truncate_string(comment[5])}")
            choice = input("Enter Choice [or Enter to Return to Post Menu]: ")
            self.handle_menu_input(choice)

    def handle_menu_input(self, choice):
        if choice.strip() == "":
            print("Returning to Post Details...")
            self.viewing = False
        else:
            try:
                choice = int(choice)
                if 0 < choice <= len(self.comments_list):
                    self.handle_friend_choice(choice)
                else:
                    raise ValueError
            except ValueError:
                print("Invalid Choice. Please Select a Valid Option.\n")
        self.decision = True
    
    def handle_friend_choice(self, choice):
        index = choice - 1
        comment_info = self.comments_list[index]
        comment_details = CommentDetails(self.user_controller, self.user, comment_info)
        comment_details.display()
