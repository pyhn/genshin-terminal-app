from backend.utils import Utils
from .search_post_list import SearchPostList
from .search_comments_list import SearchCommentsList
from .search_user_list import SearchUserList

class SearchMenu:
    def __init__(self, user_controller, user) -> None:
        self.user_controller = user_controller
        self.user = user
        self.decision = False
        self.viewing = True
        

    def display(self):
        
        while self.decision == False or self.viewing == True:
            print("+------------------------+------------------------+")
            print("| 1. Search by Keyword   | 5. View Top Comments   |")
            print("+------------------------+------------------------+")
            print("| 2. Search by Tag       | 6. View Top Users      |")
            print("+------------------------+------------------------+")
            print("| 3. Search User by Name | 7. View Trending Posts |")
            print("+------------------------+------------------------+")
            print("| 4. View Top Posts      | 8. Return to Dashboard |")
            print("+-------------------------------------------------+")

            choice = input("Enter Choice: ")
            self.handle_menu_input(choice)
    # see if we can have a query result as input to another query and sort it that way?
    def handle_menu_input(self, choice):
        options = ["1","2","3","4","5","6","7", "8"]
        if choice not in options:
            print("Invalid Choice. Please Select a Valid Option.\n")
        else:
            post_list = False
            if choice == "1":
                search_type = "Search by Keyword"
                keywords = Utils.acquire_multi_string_input("Desired", "Post Keyword(s)")
                post_list = self.user_controller.retrieve_posts_with_keywords(keywords)

            if choice == "2":
                search_type = "Search by Tag"
                tags = Utils.acquire_multi_string_input("Desired", "Post Tags(s)")
                post_list = self.user_controller.retrieve_posts_with_tags(tags)
            if choice == "3":
                search_type = "Search User by Name"
                name = Utils.acquire_string_input("Desired", "Username")
                post_list = self.user_controller.retrieve_users_with_name(name)
                
            if choice == "4":
                search_type = "Top Posts"
                post_list = self.user_controller.retrieve_top_10_liked_posts()

            if choice == "5":
                search_type = "Top Comments"
                post_list = self.user_controller.retrieve_top_10_liked_comments()

            if choice == "6":
                search_type = "Top Users"
                post_list = self.user_controller.retrieve_top_10_most_famous_users()

            if choice == "7":
                search_type = "Trending Posts"
                post_list = self.user_controller.retrieve_top_10_liked_posts_last_24_hours()

            if choice == "8":
                print("Returning to Dashboard...")
                self.viewing = False

            if post_list:
                if search_type == "Top Comments":
                    comment_ui = SearchCommentsList(self.user_controller, self.user, post_list)
                    comment_ui.display()

                elif search_type == "Top Users" or search_type == "Search User by Name":
                    user_ui = SearchUserList(self.user_controller, self.user, post_list, search_type)
                    user_ui.display()  # Add parentheses here to call the method

                else:
                    post_ui = SearchPostList(self.user_controller, self.user, post_list, search_type)
                    post_ui.display()

            else:
                print("No results found. Returning to Search Menu...\n")
            
            self.decision = True

    def get_viewing(self):
        return self.viewing
    
