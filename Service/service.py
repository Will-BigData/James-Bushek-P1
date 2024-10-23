from UI.menu import Menu
from Data.data import Data
from Resources.user import User

class Service:
    def __init__(self) -> None:
        pass


    def Shop(self):
        mn = Menu()
        dt = Data()
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
            else:
                print("Invalid Username or Password")

        shop_active = True

        while shop_active:
            up_menu = ["Welcome to Kamazon!"]
            lo_menu = []
            inner_menu_1 = False
            is_admin = False
            if is_admin:
                lo_menu = ["Browse Items", "Cart", "Users", "Admins", "Edit Inventory", "Logout"]
            else:
                lo_menu = ["Browse Items", "Cart", "Logout"]
            mn.SwitchMenu(up_menu, lo_menu)

            u_input = self.UserInput(lo_menu.__len__())
            

            if lo_menu[u_input] == "Browse Items":
                dt.GetInventory()
                up_menu = []
                lo_menu = []
                inner_menu_1 = True
                
            elif lo_menu[u_input] == "Cart":
                up_menu = []
                lo_menu = []
                inner_menu_1 = True
                
            elif lo_menu[u_input] == "Logout":
                shop_active = False
                print("Have a Great Day!")
                print("")
                print("We look forward to you future patronage!")
                
            elif lo_menu[u_input] == "Users":
                up_menu = []
                lo_menu = []
                inner_menu_1 = True

            elif lo_menu[u_input] == "Admins":
                up_menu = []
                lo_menu = []
                inner_menu_1 = True
                
            elif lo_menu[u_input] == "Edit Inventory":
                up_menu = []
                lo_menu = []
                inner_menu_1 = True
                

            while inner_menu_1:
                pass


        pass
    


    def UserInput(self, menu_max):
        check_input = True
        while check_input:
            u_input = input()
            if u_input.isdigit():
                u_input = int(u_input) - 1
                if u_input > 0 & u_input < menu_max:
                    check_input = False
                    return u_input
                else:
                    print("Please enter a valid choice.")
            else:
                print("Please enter a non-negative number.")


