

from typing import Any


class User():
    def __init__(self, user_id, user_name, user_password, cart=0) -> None:
        self.user_id = user_id
        self.user_name = user_name
        self.user_password = user_password
        self.cart = cart

    def __ClearPassword__(self):
        #clears the password, for use after password is used to log in
        self.user_password = ""

    def CheckIfAdmin(self):
        #calls data layer to find through dao if user is an admin
        #if so, return true
        pass