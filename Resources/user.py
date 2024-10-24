from typing import Any


class User():
    def __init__(self, user_id:int, user_name:str, cart:int, admin:bool, password = "") -> None:
        self.user_id = user_id
        self.user_name = user_name
        self.cart = cart
        self.admin = admin
        self.password = password