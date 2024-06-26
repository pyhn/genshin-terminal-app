class FriendsList:
    def __init__(self, user_controller, user) -> None:
        self.user_controller = user_controller
        self.user = user
        self.decision = False
        self.viewing = True
        self.friends_list = None


    def retrieve_friends_list(self):
        self.friends_list = self.user_controller.retrieve_friends_list(self.user)

    def display(self):
        while self.decision == False or self.viewing == True:
            self.retrieve_friends_list()
            friend_count = len(self.friends_list)
            print("+-------------------------------+")
            print("| Welcome to your Friends List  |")
            print("+-------------------------------+")

            if friend_count == 0:
                input("You have 0 Friends Added. Press Enter to Return to Friends Menu.")
                break
            
            for i,friend in enumerate(self.friends_list):
                print(f"{i + 1}. Username: {friend[1]}, Status: {friend[4]}")
            choice = input("Enter Choice [or Enter to Return to Friends Menu]: ")
            self.handle_menu_input(choice)

    def handle_menu_input(self, choice):
        if choice.strip() == "":
            print("Returning to Friends Menu...")
            self.viewing = False
        else:
            try:
                choice = int(choice)
                if 0 < choice <= len(self.friends_list):
                    self.handle_friend_choice(choice)
                else:
                    raise ValueError
            except ValueError:
                print("Invalid Choice. Please Select a Valid Option.\n")
        self.decision = True
    
    def handle_friend_choice(self, choice):
        index = choice - 1
        friend_info = self.friends_list[index]
        friend_name = friend_info[1]
        friend_bio = friend_info[5]
        friend_fav_char = friend_info[6]
        friend_fav_region = friend_info[7]
        print(f"User: {friend_name}")
        print(f"Bio: {self.format_bio(friend_bio)}")
        print(f"Favourite Character: {friend_fav_char}")
        print(f"Favourite Region: {friend_fav_region}")

    def format_bio(self, text):
        formated_text = ""
        if text != None:
            lines = []
            max_width = 50
            remaining_text = text
            while len(remaining_text) > max_width:
                # Find the index of the last space within the max_width
                last_space_index = remaining_text.rfind(' ', 0, max_width)
                if last_space_index == -1:
                    # No space found within max_width, break the word
                    lines.append(remaining_text[:max_width])
                    remaining_text = remaining_text[max_width:]
                else:
                    # Split the text at the last space within max_width
                    lines.append(remaining_text[:last_space_index])
                    remaining_text = remaining_text[last_space_index + 1:]
            lines.append(remaining_text)  # Add the remaining text as the last line

            for line in lines:
                formated_text += line + "\n"
            return formated_text
        else:
            return None
