from .posts_list import PostsList
from backend.utils import Utils


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
        options = ["1","2","3"]
        if choice not in options:
            print("Invalid Choice. Please Select a Valid Option.\n")
        else:
            if choice == "1":
                posts_list = PostsList(self.user_controller, self.user)
                posts_list.display()
            if choice == "2":
                
                post_title = Utils.acquire_string_input("Desired", "Title")
                post_content = Utils.acquire_string_input("Desired", "Content")
                post_tags = Utils.acquire_multi_string_input("Desired", "Tag(s)")
                
                self.user_controller.create_post(self.user, post_title, post_content)
                
               
                if len(post_tags) > 0:
                    uid = self.user.get_uid()
                    post_info = self.user_controller.retrieve_most_recent_post_by_uid(uid)
                    pid = post_info[0]
                    
                    self.user_controller.add_tags_to_table(post_tags)
                    self.user_controller.add_tags_to_mentions(uid, pid, post_tags)

            if choice == "3":
                print("Returning to Dashboard...")
                self.viewing = False
            self.decision = True

    def get_viewing(self):
        return self.viewing
    
    