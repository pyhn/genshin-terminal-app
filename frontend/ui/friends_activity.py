from .friend_post_details import FriendPostDetails

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
                friend_info = self.user_controller.get_user_info_by_id(post[3])
                friend_name = friend_info[1]
                print(f"{i + 1}. [Friend]: {friend_name} [Title]: {post[1]} [Content]: {self.truncate_string(post[2])}")
            choice = input("Enter Choice [or Enter to Return to Friends Menu]: ")
            self.handle_menu_input(choice)

    def truncate_string(self, string):
        if len(string) > 15:
            return string[:15] + "..."
        return string

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
        friend_post_info = self.friends_posts[index]
        friend_post_details = FriendPostDetails(self.user_controller, self.user, friend_post_info)
        friend_post_details.display()
