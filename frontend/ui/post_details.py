from backend.utils import Utils

class PostDetails:
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
            print("+--------------------------+")
            print("| 1. View Comments         |")
            print("+--------------------------+")
            print("| 2. Delete Post           |")
            print("+--------------------------+")
            print("| 3. Return to Post List   |")
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
                self.confirm_delete()
            if choice == "3":
                print("Returning to Post List...")
                self.viewing = False
            
            self.decision = True

    def get_viewing(self):
        return self.viewing
        
    def confirm_delete(self):
        confirm_options = ["y", "n"]
        confirm_login = input("Delete Post? (y/n): ").lower().strip()
        while confirm_login not in confirm_options:
            print("Please choose a valid option.")
            confirm_login = input("Log In? (y/n): ").lower().strip()
        
        if confirm_login == "y":
            self.user_controller.delete_post(self.post_info[0])
            print("Post has been succesfully deleted!")
            self.viewing = False
