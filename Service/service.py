from UI.menu import Menu
from Data.data import Data
from Resources.user import User
import logging

class Service:
    #TODO check for other todo's w/ this one
    def __init__(self) -> None:
        pass


    def Shop(self):
        logger = logging.getLogger(__name__)
        mn = Menu()
        dt = Data()
        current_user = ""
        u_input = 0
        login_req = True
        product_list = []

        while login_req:
            login_choice = input("Would you like to Login(0) or create an Account(1)? :")

            if login_choice.isdigit():
                if int(login_choice) == 0:
                    success = False
                    username = input("Username: ")
                    password = input("Password: ")
                    username.strip()
                    password.strip()

                    if username != "" and password != "":
                        success = dt.UserLogin(username, password)

                    if success:
                        
                        login_req = False
                        current_user = dt.GetUser(username, password)
                        logger.info(f"User {username} Logged in | Admin:{current_user.__getattribute__("admin")}")

                    else:
                        print("Invalid Username or Password")

                elif int(login_choice) == 1:
                    username = input("Username: ")
                    password = input("Password: ")
                    username.strip()
                    password.strip()

                    if username != "" and password != "":
                        dt.AddUser(username, password)
                        logger.info(f"User {username} Registered")
                        print("")
                        print("You are now registered with Kamazon!")
                    else:
                        print("")
                        print("You must enter something for both username and password")
                        print("")

                else:
                    print("")
                    print("Please enter a valid input")
                    print("")
            else:
                print("")
                print("Please enter a valid input")
                print("")

        shop_active = True

        # UpdateStock
        while shop_active:
            dt.SaveUserCart(current_user)

            product_list = dt.GetInventory()

            i = 0
            for product in product_list:
                stock = product.__getattribute__("quantity")
                for id in list(str(current_user.__getattribute__("cart"))):
                    if int(id) == product.__getattribute__("product_id"):
                        stock -= 1

                product.__setattr__("quantity", stock)
                product_list[i] = product
                i+=1

            up_menu = ["Welcome to Kamazon!"]
            lo_menu = []

            if current_user.__getattribute__("admin"):
                lo_menu = ["Browse Items", "Cart", "Users", "Edit Inventory", "Logout"]
            else:
                lo_menu = ["Browse Items", "Cart", "Logout"]

            mn.SwitchMenu(up_menu, lo_menu)
            mn.DrawMenu()

            u_input = self.UserInput(lo_menu.__len__())

            inner_menu_1 = True
            
            while inner_menu_1:
                inner_menu_2 = False

                if lo_menu[u_input] == "Browse Items":
                    inner_menu_2 = True
                    

                    while inner_menu_2:

                        up_menu = []
                        
                        for product in product_list:
                            up_menu.append(product.__getattribute__("product_name"))

                        lo_menu = ["Cart", "Back"]
                        mn.SwitchMenu(up_menu, lo_menu, True)
                        mn.DrawMenu()
                        total_menu = up_menu + lo_menu

                        u_input = self.UserInput(total_menu.__len__())

                        if total_menu[u_input] == "Cart":
                            inner_menu_2 = False
                            lo_menu = ["Cart"]
                            u_input = 0

                        elif total_menu[u_input] == "Back":
                            inner_menu_1 = False
                            inner_menu_2 = False

                        else:
                            product_index = u_input
                            active_product = product_list[u_input]
                            product_info = active_product.ReturnAttr()
                            
                            up_menu = []
                            up_menu.append(product_info[0])
                            up_menu.append("")
                            up_menu.append(product_info[1])
                            up_menu.append("")
                            up_menu.append("In Stock: " + str(product_info[2]))
                            up_menu.append("Price: $" + str(product_info[3]))

                            lo_menu = ["Add to Cart", "Back"]

                            mn.SwitchMenu(up_menu, lo_menu)
                            mn.DrawMenu()

                            u_input = self.UserInput(lo_menu.__len__())

                            if lo_menu[u_input] == "Add to Cart":
                                user_cart = current_user.__getattribute__("cart")
                                if user_cart == 0:
                                    current_user.__setattr__("cart", active_product.__getattribute__("product_id"))

                                    
                                    old_stock = active_product.__getattribute__("quantity")
                                    active_product.__setattr__("quantity", old_stock-1)

                                    product_list[product_index] = active_product

                                elif user_cart > 100000000:
                                    print("Your cart is full, please checkout or remove an item to continue shopping.")

                                elif active_product.__getattribute__("quantity") < 1:
                                    print("We're incredibly sorry, that item is out of stock.")

                                else:
                                    new_cart = str(user_cart) + str(active_product.__getattribute__("product_id"))
                                    current_user.__setattr__("cart", int(new_cart))

                                    old_stock = active_product.__getattribute__("quantity")
                                    active_product.__setattr__("quantity", old_stock-1)

                                    product_list[product_index] = active_product
                    
                elif lo_menu[u_input] == "Cart":
                    inner_menu_2 = True

                    
                    while inner_menu_2:
                        cart_list = []
                        up_menu = []

                        cart_exists = False

                        if current_user.__getattribute__("cart") > 0:
                            for item in list(str(current_user.__getattribute__("cart"))):
                                cart_list.append(dt.GetItem(int(item)))

                            for product in cart_list:
                                up_menu.append(product.__getattribute__("product_name"))

                            lo_menu = ["Checkout", "Back"]

                            cart_exists = True
                        else:
                            up_menu = ["Your cart is empty."]
                            lo_menu = ["Back"]

                
                        mn.SwitchMenu(up_menu, lo_menu, cart_exists)
                        mn.DrawMenu()

                        total_menu = []

                        if cart_exists:
                            total_menu = up_menu + lo_menu
                        else:
                            total_menu = lo_menu

                        u_input = self.UserInput(total_menu.__len__())

                        if total_menu[u_input] == "Checkout":
                            cust_total = 0
                            for product in cart_list:
                                cust_total += product.__getattribute__("ppu")
                            
                            up_menu = [f"Your total for these items is ${cust_total}", "", "Confirm Purchase?"]
                            lo_menu = ["Confirm", "Cancel"]

                            mn.SwitchMenu(up_menu, lo_menu)
                            mn.DrawMenu()

                            u_input = self.UserInput(lo_menu.__len__())

                            if lo_menu[u_input] == "Confirm":
                                dt.UpdateStock(product_list)

                                current_user.__setattr__("cart", 0)

                                print("Your purchases will arrive in (1) business day(s)")
                                print("")
                                print("Thank you for shopping Kamazon!")

                                logger.info(f"User {username} completed a transaction")

                                inner_menu_1 = False
                                inner_menu_2 = False
                            

                        elif total_menu[u_input] == "Back":
                            inner_menu_1 = False
                            inner_menu_2 = False

                        else:
                            product_index = u_input
                            active_product = cart_list[u_input]
                            product_info = active_product.ReturnAttr()
                            
                            up_menu = []
                            up_menu.append(product_info[0])
                            up_menu.append("")
                            up_menu.append(product_info[1])
                            up_menu.append("")
                            up_menu.append("Price: $" + str(product_info[3]))

                            lo_menu = ["Remove from Cart", "Back"]

                            mn.SwitchMenu(up_menu, lo_menu)
                            mn.DrawMenu()

                            u_input = self.UserInput(lo_menu.__len__())

                            if lo_menu[u_input] == "Remove from Cart":
                                returned_product_stock = product_list[product_index].__getattribute__("quantity")
                                product_list[cart_list[product_index].__getattribute__("product_id")-1].__setattr__("quantity", returned_product_stock+1)

                                del cart_list[product_index]
                                new_cart = ""

                                if cart_list.__len__() > 0:
                                    for product in cart_list:
                                        new_cart += str(product.__getattribute__("product_id"))
                                else:
                                    new_cart = 0

                                current_user.__setattr__("cart", int(new_cart))
                    
                elif lo_menu[u_input] == "Logout":
                    shop_active = False
                    inner_menu_1 = False

                    logger.info(f"User {username} Logged out")

                    print("Have a Great Day!")
                    print("")
                    print("We look forward to you future patronage!")
                    
                elif lo_menu[u_input] == "Users":
                    inner_menu_2 = True

                    while inner_menu_2:
                        all_users = dt.GetAllUsers()
                        up_menu = []
                        lo_menu = []

                        for user in all_users:
                            up_menu.append(user.__getattribute__("user_name"))

                        lo_menu = ["Back"]

                        mn.SwitchMenu(up_menu, lo_menu, True)
                        mn.DrawMenu()

                        total_menu = up_menu + lo_menu

                        u_input = self.UserInput(total_menu.__len__())

                        if total_menu[u_input] == "Back":
                            inner_menu_2 = False
                            inner_menu_1 = False
                        else:
                            up_menu = []
                            lo_menu = []

                            target_user = all_users[u_input]

                            up_menu.append("User_ID: " + str(target_user.__getattribute__("user_id")))
                            up_menu.append("Username: " + target_user.__getattribute__("user_name"))
                            up_menu.append("Cart: " + str(target_user.__getattribute__("cart")))
                            up_menu.append("Admin: " + str(target_user.__getattribute__("admin")))
                            up_menu.append("Password: " + target_user.__getattribute__("password"))

                            lo_menu.append("Edit Username")
                            lo_menu.append("Clear Cart")
                            lo_menu.append("Edit Admin Access")
                            lo_menu.append("Edit Password")
                            lo_menu.append("Back")


                            mn.SwitchMenu(up_menu, lo_menu)
                            mn.DrawMenu()

                            u_input = self.UserInput(lo_menu.__len__())

                            if lo_menu[u_input] == "Back":
                                inner_menu_1 = False
                                inner_menu_2 = False

                            elif lo_menu[u_input] == "Edit Username":
                                new_username = input("New Username: ")
                                new_username = rf"'{new_username}'"
                                dt.UpdateUser(target_user.__getattribute__("user_id"), "UserName", new_username)
                                print("Updated User Name")
                                logger.info(f"Admin {username} changed the Username of User {target_user.__getattribute__("user_name")} to {new_username}")

                            elif lo_menu[u_input] == "Clear Cart":
                                target_user.__setattr__("cart", 0)
                                dt.SaveUserCart(target_user)
                                print("Cleared User Cart")
                                logger.info(f"Admin {username} cleared the cart of User {target_user.__getattribute__("user_id")}")

                            elif lo_menu[u_input] == "Edit Admin Access":
                                new_access = input("Edit User Admin Access(0|1): ")

                                if new_access.isdigit():
                                    if int(new_access) == 0:
                                        dt.EditAdmin(target_user.__getattribute__("user_id"), False)
                                        logger.info(f"Admin {username} revoked Admin access from User {target_user.__getattribute__("user_id")}")
                                        
                                    elif int(new_access) == 1:
                                        dt.EditAdmin(target_user.__getattribute__("user_id"), True)
                                        logger.info(f"Admin {username} granted Admin access to User {target_user.__getattribute__("user_id")}")
                                        
                                    else:
                                        print("Enter a valid input, booting you back a menu...")

                            elif lo_menu[u_input] == "Edit Password":
                                new_password = input("New Password: ")
                                new_password = rf"'{new_password}'"
                                dt.UpdateUser(target_user.__getattribute__("user_id"), "UserPwd", new_password)
                                print("Updated User Password")
                                logger.info(f"Admin {username} changed the password of User {target_user.__getattribute__("user_id")}")
                                              
                elif lo_menu[u_input] == "Edit Inventory":
                    inner_menu_2 = True

                    while inner_menu_2:
                        up_menu = []
                        lo_menu = []

                        for product in product_list:
                            up_menu.append(product.__getattribute__("product_name"))

                        lo_menu.append("Add Item")
                        lo_menu.append("Back")

                        mn.SwitchMenu(up_menu, lo_menu, True)
                        mn.DrawMenu()

                        total_menu = up_menu + lo_menu

                        u_input = self.UserInput(total_menu.__len__())

                        if total_menu[u_input] == "Back":
                            inner_menu_1 = False
                            inner_menu_2 = False

                        elif total_menu[u_input] == "Add Item":
                            product_name = input("Product Name: ")
                            product_description = input("Product Description: ")
                            quantity = input("Quantity: ")
                            ppu = input("Price Per Unit: ")
                            dt.AddProduct(product_name, product_description, quantity, ppu)
                            print("Item Added!")
                            print("")
                            print("To Reflect the new changes, back out to the main menu")
                            logger.info(f"Admin {username} added the product {product_name} to the Kamazon inventory")
                            
                        else:
                            up_menu = []
                            lo_menu = []
                            current_product = product_list[u_input]

                            up_menu.append("Product_ID: " + str(current_product.__getattribute__("product_id")))
                            up_menu.append("Product Name: " + current_product.__getattribute__("product_name"))
                            up_menu.append("Description: " + current_product.__getattribute__("product_description"))
                            up_menu.append("Quantity in Stock: " + str(current_product.__getattribute__("quantity")))
                            up_menu.append("Price Per Unit: " + str(current_product.__getattribute__("ppu")))

                            lo_menu.append("Edit Name")
                            lo_menu.append("Edit Description")
                            lo_menu.append("Edit Quantity")
                            lo_menu.append("Edit Price")
                            lo_menu.append("Remove Item")
                            lo_menu.append("Back")

                            mn.SwitchMenu(up_menu, lo_menu)
                            mn.DrawMenu()

                            u_input = self.UserInput(lo_menu.__len__())

                            if lo_menu[u_input] == "Edit Name":
                                new_product_name = input("New Product Name: ")
                                new_product_name = rf"'{new_product_name}'"
                                dt.UpdateProduct(current_product.__getattribute__("product_id"), "ProductName", new_product_name)
                                print("Updated Product Name")
                                print("")
                                print("To Reflect the new changes, back out to the main menu")
                                logger.info(f"Admin {username} changed the name of Product {current_product.__getattribute__("product_name")} to {new_product_name}")

                            elif lo_menu[u_input] == "Edit Description":
                                new_product_descr = input("New Product Description: ")
                                new_product_descr = rf"'{new_product_descr}'"
                                dt.UpdateProduct(current_product.__getattribute__("product_id"), "ProductDescription", new_product_descr)
                                print("Updated Product Name")
                                print("")
                                print("To Reflect the new changes, back out to the main menu")
                                logger.info(f"Admin {username} changed the description of Product {current_product.__getattribute__("product_name")} to {new_product_descr}")

                            elif lo_menu[u_input] == "Edit Quantity":
                                new_quantity = input("New Product Quantity: ")
                                if new_quantity.isdigit():
                                    dt.UpdateProduct(current_product.__getattribute__("product_id"), "Quantity", int(new_quantity))
                                    print("Updated Product Quantity")
                                    print("")
                                    print("To Reflect the new changes, back out to the main menu")
                                    logger.info(f"Admin {username} changed the quantity of Product {current_product.__getattribute__("product_name")} to {new_quantity}")
                                        
                                else:
                                    print("Enter a valid input, booting you back a menu...")

                            elif lo_menu[u_input] == "Edit Price":
                                new_ppu = input("New Product Price: ")

                                dt.UpdateProduct(current_product.__getattribute__("product_id"), "PPU", float(new_ppu))
                                print("Updated Product Price Per Unit")
                                print("")
                                print("To Reflect the new changes, back out to the main menu")
                                logger.info(f"Admin {username} changed the ppu of Product {current_product.__getattribute__("product_name")} to {new_ppu}")

                            elif lo_menu[u_input] == "Remove Item":
                                dt.DeleteProduct(current_product.__getattribute__("product_id"))
                                print("Product Removed")
                                logger.info(f"Admin {username} removed {current_product.__getattribute__("product_name")}")

                            elif lo_menu[u_input] == "Back":
                                inner_menu_1 = False
                                inner_menu_2 = False

                else:
                    print("Somehow, something went wrong")
                    inner_menu_1 = False

        # end of shop method
    


    def UserInput(self, menu_max):
        check_input = True
        while check_input:
            u_input = input()
            if u_input.isdigit():
                u_input = int(u_input) - 1
                if u_input >= 0 and u_input < menu_max:
                    check_input = False
                    return u_input
                else:
                    print("Please enter a valid choice.")
            else:
                print("Please enter a non-negative number.")



