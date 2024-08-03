from .search_comment_details import SearchCommentDetails
from backend.utils import Utils

class SearchCommentsList:
    def __init__(self, user_controller, user, comment_list) -> None:
        self.user_controller = user_controller
        self.user = user
        self.decision = False
        self.viewing = True
        self.comments_list = comment_list

    def display(self):
        while self.decision == False or self.viewing == True:
            print("+----------------------+")
            print("| Viewing Top Comments |")
            print("+----------------------+")

            for i, comment in enumerate(self.comments_list): #here
                author_info = self.user_controller.get_user_info_by_id(comment[1])
                author_name = author_info[1]
                print(f"{i + 1}. [Author]: {author_name} [Content]: {Utils.truncate_string(comment[5])}")
            choice = input("Enter Choice [or Enter to Return to Search Menu]: ")
            self.handle_menu_input(choice)

    def handle_menu_input(self, choice):
        if choice.strip() == "":
            print("Returning to Search Menu...")
            self.viewing = False
        else:
            try:
                choice = int(choice)
                if 0 < choice <= len(self.comments_list):
                    self.handle_comment_choice(choice)
                else:
                    raise ValueError
            except ValueError:
                print("Invalid Choice. Please Select a Valid Option.\n")
        self.decision = True
    
    def handle_comment_choice(self, choice):
        index = choice - 1
        comment_info = self.comments_list[index]
        comment_details = SearchCommentDetails(self.user_controller, self.user, comment_info)
        comment_details.display()
