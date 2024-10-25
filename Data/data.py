from DAO.dao import DAO
from Resources.user import User
from Resources.product import Product

class Data:
    def __init__(self, dao=DAO()) -> None:
        self.dao = dao


    def UserLogin(self, username, password):
        result = self.dao.GetUsersBy(f"UserName = '{username}' AND UserPwd = '{password}'")
        self.dao.CloseConnection()
        if result.__len__() > 0:
            return True
        else:
            return False
        
    def GetUser(self, username, password):
        result = self.dao.GetUsersBy(f"UserName = '{username}' AND UserPwd = '{password}'")
        self.dao.CloseConnection()
        target_user = User(int(result[0][0]), result[0][1], int(result[0][3]), bool(result[0][5]))
        return target_user
        
    def GetInventory(self):
        result = self.dao.GetAllProducts()

        product_list = []
        for row in result:
            if row[3] > 0:
                product_list.append(Product(row[0], row[1], row[2], row[3], row[4]))

        self.dao.CloseConnection()

        return product_list
    
    def GetItem(self, product_id):
        result = self.dao.GetProductsBy(f"Product_ID = '{product_id}'")

        target_product = Product(result[0][0], result[0][1], result[0][2], result[0][3], result[0][4])

        return target_product

    def UpdateStock(self, product_list):
        for product in product_list:
            new_stock = product.__getattribute__("quantity")
            product_id = product.__getattribute__("product_id")

            self.dao.UpdateProduct(product_id, f"Quantity = {new_stock}")

    def SaveUserCart(self, current_user):
        u_cart = current_user.__getattribute__("cart")
        u_id = current_user.__getattribute__("user_id")

        self.dao.UpdateUser(u_id, f"Cart = {u_cart}")
        

    def GetAllUsers(self):
        result = self.dao.GetAllUsers()
        self.dao.CloseConnection()
        all_users = []
        for row in result:
            next_user = User(int(row[0]), row[1], int(row[3]), bool(row[5]), row[2])
            all_users.append(next_user)
        return all_users
    
    def UpdateUser(self, user_id, field, value):
        self.dao.UpdateUser(user_id, f"{field} = {value}")

    def AddProduct(self, name, descr, quantity, ppu):
        self.dao.AddProduct(name, descr, quantity, ppu)

    def UpdateProduct(self, product_id, field, value):
        self.dao.UpdateProduct(product_id, f"{field} = {value}")

    def AddUser(self, username, password):
        self.dao.AddUser(username, password)

    def EditAdmin(self, user_id, access):
        self.dao.EditAdmin(user_id, access)

    def DeleteProduct(self, product_id:int):
        self.dao.DeleteProduct(product_id)


