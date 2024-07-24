from backend.utils import Utils

class CommentDetails:
    def __init__(self, user_controller, user, comment_info) -> None:
        self.user_controller = user_controller
        self.decision = False
        self.viewing = True
        self.user = user
        self.comment_info = comment_info
        
    def display(self):
        print() 
        comment_date = self.comment_info[4][:10]
        comment_content = self.comment_info[5]
        
        while self.decision == False or self.viewing == True:
            print(f"Date: {comment_date}")
            print(f"Content: {Utils.format_content(comment_content)}")
            print(f"Like Count: {self.comment_info[6]}")
            print(f"Dislike Count: {self.comment_info[7]}")
            print("+--------------------------------+")
            print("| 1. Like Comment                |")
            print("+--------------------------------+")
            print("| 2. Dislike Comment             |")
            print("+--------------------------------+")
            print("| 3. Return to Post's Comments   |")
            print("+--------------------------------+")
            choice = input("Enter Choice: ")
            self.handle_menu_input(choice)

    def handle_menu_input(self, choice):
        options = ["1","2","3"]
        if choice not in options:
            print("Invalid Choice. Please Select a Valid Option.\n")
        else:
            uid = self.user.get_uid()
            cid = self.comment_info[0]
            if choice == "1":
                if str(self.comment_info[1]) == uid:
                    print("You cannot like your own comment! Returning to details...")
                else:
                    self.handle_like(uid, cid)
            if choice == "2":
                if str(self.comment_info[1]) == uid:
                    print("You cannot dislike your own comment! Returning to details...")
                else:
                    self.handle_dislike(uid, cid)

            if choice == "3":
                print("Returning to Post's Comments...")
                self.viewing = False
            
            self.decision = True

    def get_viewing(self):
        return self.viewing
    
    def handle_like(self, uid, cid):
        if self.user_controller.has_user_liked_comment(uid, cid):
            print("You have already liked this comment! Returning to details...")
        else:
            if self.user_controller.has_user_disliked_comment(uid, cid):
                self.user_controller.remove_dislike_from_comment(uid, cid)
            self.user_controller.like_comment(uid, cid)
        
    def handle_dislike(self, uid, cid):
        if self.user_controller.has_user_disliked_comment(uid, cid):
            print("You have already disliked this comment! Returning to details...")
        else:
            if self.user_controller.has_user_liked_comment(uid, cid):
                self.user_controller.remove_like_from_comment(uid, cid)
            self.user_controller.dislike_comment(uid, cid)
    
        