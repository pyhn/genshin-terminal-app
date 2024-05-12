class UserProfile:
    def __init__(self, user_controller, user) -> None:
        self.user_controller = user_controller
        self.user = user
        self.choice = None
        

    def display(self):
        print(f"Current Status: {self.user.get_status()}")
        print(f"Bio: {self.format_bio()}")
        print(f"Favourite Character: {self.user.get_fav_character()}")
        print(f"Favourite Region: {self.user.get_fav_region()}")
        print(f"+-------------------------------------------------+")
        print(f"| 1. Edit Profile | 2. User Preferences | 3. Exit |")
        print(f"+-------------------------------------------------+")

        choice = input("Enter Choice: ")
        self.handle_menu_input(choice)
            
    def format_bio(self):
        text = self.user.get_bio()
        if text != None:
            lines = []
            max_width = 25
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
                print(line)
        else:
            return None

    def handle_menu_input(self, choice):
        options = ["1","2","3"]
        if choice not in options:
            print("Invalid Choice. Please Select a Valid Option.\n")
        else:
            if self.choice == "1":
                print(f"Editing Profile")