from .post_comments import PostComments

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
        print(f"Content: {self.format_content(post_content)}")
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
        options = ["1","2","3"]
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
        
    def commenting(self):
        content = self.acquire_comment_info("Comment Content")
        uid = self.user.get_uid()
        pid = self.post_info[0]
        self.user_controller.comment_to_post(uid, pid, content)
        print("Returning to Post...")

    def acquire_comment_info(self, info_type):
        confirmed = False
        while not confirmed:
            user_input = input(f"Enter Desired {info_type.capitalize()}: ")
            confirm_input = input(f"Accept {info_type.capitalize()}? (y/n): ").lower().strip()

            while confirm_input not in ["y", "n"]:
                print("Please choose a valid option.")
                confirm_input = input(f"Accept {info_type.capitalize()}? (y/n): ").lower().strip()

            if confirm_input == "y":
                confirmed = True
                return user_input