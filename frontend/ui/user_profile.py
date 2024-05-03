class user_profile:
    def __init__(self) -> None:
        self.user = None
        self.status = "N/A"
        self.bio = "N/A"
        self.fav_character = "N/A"
        self.fav_region = "N/A"

    def set_user_details(self, user):
        self.user = user
        

    def display(self):
        print(f"Current Status: {self.status}")
        print(f"Bio: {self.bio}")
        print(f"Favourite Character: {self.fav_character}")
        print(f"Favourite Region: {self.fav_region}")