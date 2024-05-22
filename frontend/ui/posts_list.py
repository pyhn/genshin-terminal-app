from .post_details import PostDetails

class PostsList:
    def __init__(self, user_controller, user) -> None:
        self.user_controller = user_controller
        self.user = user
        self.decision = False
        self.viewing = True
        self.posts_list = None


    def retrieve_posts_list(self):
        self.posts_list = self.user_controller.retrieve_posts_list(self.user)

    def display(self):
        while self.decision == False or self.viewing == True:
            self.retrieve_posts_list()
            post_count = len(self.posts_list)
            print("+-------------------------------+")
            print("| Welcome to your Posts List    |")
            print("+-------------------------------+")

            if post_count == 0:
                input("You have 0 Posts. Press Enter to Return to Posts Menu.")
                break
            
            for i,post in enumerate(self.posts_list):
                print(f"{i + 1}. [Title]: {post[1]} [Content]: {self.truncate_string(post[2])}")
            choice = input("Enter Choice [or Enter to Return to Posts Menu]: ")
            self.handle_menu_input(choice)

    def truncate_string(self, string):
        if len(string) > 15:
            return string[:15] + "..."
        return string

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
        

    