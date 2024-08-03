from .search_post_details import SearchPostDetails
from backend.utils import Utils

class SearchPostList:
    def __init__(self, user_controller, user, post_list, search_type) -> None:
        self.user_controller = user_controller
        self.user = user
        self.decision = False
        self.viewing = True
        self.posts_list = post_list
        self.search_type = search_type
        self.page_size = 10  # number of posts to display per page

    def display(self):
        current_page = 0
        
        while not self.decision and self.viewing:
            # Calculate the start and end index for the current page
            start_index = current_page * self.page_size
            end_index = min(start_index + self.page_size, len(self.posts_list))
            
            # Check if there are posts to display
            if start_index >= len(self.posts_list):
                print("No more posts to display.")
                self.viewing = False
                continue
            
            # Display the posts for the current page
            welcome_string = f"| {self.search_type} Results |"
            border_length = max(len(welcome_string) - 2, 0)  # ensure length is not negative
            border_string = "+" + "-" * border_length + "+"
            print(border_string)
            print(welcome_string)
            print(border_string)
            
            for i in range(start_index, end_index):
                post = self.posts_list[i]
                print(f"{i + 1}. [Title]: {post[1]} [Content]: {Utils.truncate_string(post[2])}")
            
            # Display pagination controls
            if end_index < len(self.posts_list):
                print("Type 'next' for more posts or 'back' to go to the previous page.")
            if current_page > 0:
                print("Type 'back' to go to the previous page.")
            
            choice = input("Enter Choice [or Enter to Return to Search Menu]: ")
            self.handle_menu_input(choice, current_page, end_index)
            
            if choice.strip().lower() == 'next':
                if end_index < len(self.posts_list):
                    current_page += 1
                else:
                    print("No more posts to display.")
            elif choice.strip().lower() == 'back':
                if current_page > 0:
                    current_page -= 1
                else:
                    print("You are already on the first page.")

    def handle_menu_input(self, choice, current_page, end_index):
        if choice.strip() == "":
            print("Returning to Search Menu...")
            self.viewing = False
        elif choice.strip().lower() in ['next', 'back']:
            return  # Handled in the main loop
        else:
            try:
                choice = int(choice)
                if 1 <= choice <= end_index:
                    self.handle_post_choice(choice)
                else:
                    raise ValueError
            except ValueError:
                print("Invalid Choice. Please Select a Valid Option.\n")
        self.decision = True

    def handle_post_choice(self, choice):
        index = choice - 1
        post_info = self.posts_list[index]
        post_details = SearchPostDetails(self.user_controller, self.user, post_info)
        post_details.display()
