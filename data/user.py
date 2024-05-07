class User:
    def __init__(self) -> None:
        self._username = None
        self._password = None
        self._email = None
        self._status = None
        self._bio = None
        self._fav_character = None
        self._fav_region = None

    # setters
    def set_username(self, username):
        self._username = username

    def set_password(self, password):
        self._password = password

    def set_email(self, email):
        self._email = email

    def set_status(self, status):
        self._status = status

    def set_bio(self, bio):
        self._bio = bio

    def set_fav_character(self, fav_character):
        self._fav_character = fav_character

    def set_fav_region(self, fav_region):
        self._fav_region = fav_region

    # setters
    def get_username(self):
        return self._username

    def get_password(self):
        return self._password
    
    def get_email(self):
        return self._email

    def get_status(self):
        return self._status

    def get_bio(self):
        return self._bio

    def get_fav_character(self):
        return self._fav_character

    def get_fav_region(self):
        return self._fav_region
