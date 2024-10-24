from UI.menu import Menu
from Data.data import Data
from Resources.user import User

class Service:
    def __init__(self) -> None:
        pass


    def Shop(self):
        mn = Menu()
        dt = Data()
        current_user = ""
        u_input = 0
        login_req = True

        while login_req:
            success = False
            username = input("Username: ")
            password = input("Password: ")
            username.strip()
            password.strip()

            if username != "" and password != "":
                success = dt.UserLogin(username, password)

            if success:
                login_req = False
                current_user.__setattr__("user_id")
                current_user.__setattr__("user_name")
                current_user.__setattr__("cart")
            else:
                print("Invalid Username or Password")

        shop_active = True

        while shop_active:
            up_menu = ["Welcome to Kamazon!"]
            lo_menu = []
            is_admin = False

            if is_admin:
                lo_menu = ["Browse Items", "Cart", "Users", "Admins", "Edit Inventory", "Logout"]
            else:
                lo_menu = ["Browse Items", "Cart", "Logout"]

            mn.SwitchMenu(up_menu, lo_menu)
            mn.DrawMenu()

            u_input = self.UserInput(lo_menu.__len__())

            inner_menu_1 = True
            
            while inner_menu_1:
                if lo_menu[u_input] == "Browse Items":
                    product_list = dt.GetInventory()
                    up_menu = [product_list]
                    lo_menu = ["Cart"]

                    mn.SwitchMenu()
                    
                elif lo_menu[u_input] == "Cart":
                    product_list = []
                    

                    up_menu = []
                    lo_menu = []
                    
                elif lo_menu[u_input] == "Logout":
                    shop_active = False
                    inner_menu_1 = False
                    print("Have a Great Day!")
                    print("")
                    print("We look forward to you future patronage!")
                    
                elif lo_menu[u_input] == "Users":
                    up_menu = []
                    lo_menu = []

                elif lo_menu[u_input] == "Admins":
                    up_menu = []
                    lo_menu = []
                    
                elif lo_menu[u_input] == "Edit Inventory":
                    up_menu = []
                    lo_menu = []

                else:
                    print("Somehow, something went wrong")
                    inner_menu_1 = False

                inner_menu_2 = False

                while inner_menu_2:
                    pass
                

            


        pass
    


    def UserInput(self, menu_max):
        check_input = True
        while check_input:
            u_input = input()
            if u_input.isdigit():
                u_input = int(u_input) - 1
                if u_input >= 0 & u_input < menu_max:
                    check_input = False
                    return u_input
                else:
                    print("Please enter a valid choice.")
            else:
                print("Please enter a non-negative number.")


