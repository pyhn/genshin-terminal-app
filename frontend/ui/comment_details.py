class CommentDetails:
    def __init__(self, user_controller, comment_info) -> None:
        self.user_controller = user_controller
        self.decision = False
        self.viewing = True
        self.comment_info = comment_info
        
    def display(self):
        print() 
        comment_date = self.comment_info[4][:10]
        comment_content = self.comment_info[5]
        print(f"Date: {comment_date}")
        print(f"Content: {self.format_content(comment_content)}")
        print(f"Like Count: {self.comment_info[6]}")
        print(f"Dislike Count: {self.comment_info[7]}")
        while self.decision == False or self.viewing == True:
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
            if choice == "1":
                pass
            if choice == "2":
                pass
            if choice == "3":
                print("Returning to Post's Comments...")
                self.viewing = False
            
            self.decision = True

    def get_viewing(self):
        return self.viewing
    
    def format_content(self, text):
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
        