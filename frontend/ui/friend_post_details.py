from .post_comments import PostComments
from backend.utils import Utils


class FriendPostDetails:
    def __init__(self, user_controller, user, post_info) -> None:
        self.user_controller = user_controller
        self.user = user
        self.decision = False
        self.viewing = True
        self.post_info = post_info
        
    def display(self):
        print() 
        post_title = self.post_info[1]
        post_content = self.post_info[2]
        post_date = self.post_info[4][:10]
        print(f"Title: {post_title} ")
        print(f"Post Date: {post_date}")
        print(f"Content: {Utils.format_content(post_content)}")
        while self.decision == False or self.viewing == True:
            print("+---------------------------------+")
            print("| 1. View Comments                |")
            print("+---------------------------------+")
            print("| 2. Comment to Post              |")
            print("+---------------------------------+")
            print("| 3. Like Post                    |")
            print("+---------------------------------+")
            print("| 4. Dislike Post                 |")
            print("+---------------------------------+")
            print("| 5. Return to Friends Activity   |")
            print("+---------------------------------+")
            choice = input("Enter Choice: ")
            self.handle_menu_input(choice)


    def handle_menu_input(self, choice):
        options = ["1","2","3","4","5"]
        if choice not in options:
            print("Invalid Choice. Please Select a Valid Option.\n")
        else:
            if choice == "1":
                post_comments = PostComments(self.user_controller, self.post_info[0])
                post_comments.display()
            if choice == "2":
                self.commenting()
            if choice == "3":
                pass
            if choice == "4":
                pass
            if choice == "5":
                print("Returning to Friends Activity...")
                self.viewing = False
            
            self.decision = True

    def get_viewing(self):
        return self.viewing
         
    def commenting(self):
        content = Utils.acquire_string_input("Desired","Comment Content")
        uid = self.user.get_uid()
        pid = self.post_info[0]
        self.user_controller.comment_to_post(uid, pid, content)
        print("Returning to Post...")