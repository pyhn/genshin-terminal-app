class UserProfile:
    def __init__(self, user_controller) -> None:
        self.user_controller = user_controller
        

    def display(self):
        print(f"Current Status:")