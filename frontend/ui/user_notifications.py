class UserNotifications:
    def __init__(self, user_controller, user, requests) -> None:
        self.user_controller = user_controller
        self.user = user
        self.decision = False
        self.viewing = True
        self.requests = requests

    def display(self):
        while self.decision == False or self.viewing == True:
            req_count = len(self.requests)
            print("+------------------------------------+")
            print("| Welcome to your Notifications Page |")
            print("+------------------------------------+")

            if req_count == 0:
                input("You have 0 Notifcations. Press Enter to Return to Dashboard.")
                break

            for i, entry in enumerate(self.requests):
                print(f"{i + 1}. {entry[0]} has sent you a friend request!")
            choice = input("Enter Choice [or Enter to Return to Dashboard]: ")
            self.handle_menu_input(choice)


    def handle_menu_input(self, choice):
        if choice.strip() == "":
            print("Returning to Dashboard...")
            self.viewing = False
        else:
            try:
                choice = int(choice)
                if 0 < choice <= len(self.requests):
                    self.handle_friend_request(choice)
                else:
                    raise ValueError
            except ValueError:
                print("Invalid Choice. Please Select a Valid Option.\n")
        self.decision = True

    def handle_friend_request(self, choice):
        index = choice - 1
        requester_name = self.requests[index][0]
        requester_id = self.requests[index][1]
        requestee_id = self.user.get_uid()
        
        confirm_input = input(f"Accept {requester_name}'s Friend Request? (y/n/c): ").lower().strip()
        while confirm_input not in ["y", "n", "c"]:
            print("Please choose a valid option.")
            confirm_input = input(f"Accept {requester_name}'s Friend Request? (y/n/c): ").lower().strip()

        if confirm_input == "y":
            self.user_controller.accept_friend_request(requester_id, requestee_id)
            del self.requests[index]
            print("Friend Request Accepted!")
        if confirm_input == "n":
            self.user_controller.reject_friend_request(requester_id, requestee_id)
            del self.requests[index]
            print("Friend Request Rejected!")

    def get_viewing(self):
        return self.viewing