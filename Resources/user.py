

from typing import Any


class User():
    def __init__(self, user_id, user_name, cart=0) -> None:
        self.user_id = user_id
        self.user_name = user_name
        self.cart = cart

    def CheckIfAdmin(self):
        #calls data layer to find through dao if user is an admin
        #if so, return true
        pass