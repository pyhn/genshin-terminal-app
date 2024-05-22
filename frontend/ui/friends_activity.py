class FriendsActivity:
    def __init__(self, user_controller, user) -> None:
        self.user_controller = user_controller
        self.user = user
        self.decision = False
        self.viewing = True
        self.friends_posts = None


    def retrieve_friends_posts(self):
        self.friends_posts = self.user_controller.retrieve_friends_posts(self.user)

    def display(self):
        while self.decision == False or self.viewing == True:
            self.retrieve_friends_posts()
            friends_post_count = len(self.friends_posts)
            print("+-----------------------------------+")
            print("| Welcome to your Friends Activity  |")
            print("+-----------------------------------+")

            if friends_post_count == 0:
                input("You're Friends Have 0 Posts. Press Enter to Return to Friends Menu.")
                break
            
            for i, post in enumerate(self.friends_posts):
                print(f"{i + 1}. {post}")
            choice = input("Enter Choice [or Enter to Return to Friends Menu]: ")
            self.handle_menu_input(choice)

    def handle_menu_input(self, choice):
        if choice.strip() == "":
            print("Returning to Friends Menu...")
            self.viewing = False
        else:
            try:
                choice = int(choice)
                if 0 < choice <= len(self.friends_posts):
                    self.handle_friend_choice(choice)
                else:
                    raise ValueError
            except ValueError:
                print("Invalid Choice. Please Select a Valid Option.\n")
        self.decision = True
    
    def handle_friend_choice(self, choice):
        index = choice - 1
        friend_info = self.friends_posts[index]
        print(friend_info)
