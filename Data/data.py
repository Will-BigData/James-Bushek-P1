from DAO.dao import DAO
from Resources.user import User

class Data:
    def __init__(self, dao=DAO()) -> None:
        self.dao = dao


    def UserLogin(self, username, password):
        result = self.dao.GetUsersBy(f"UserName = '{username}' AND UserPwd = '{password}'")
        self.dao.CloseConnection()
        print(result.__len__())
        if result.__len__() > 0:
            return True
        else:
            return False
        
    def GetUser():
        pass
        
    def GetInventory(self):
        result = self.dao.GetAllProducts("ProductName, Quantity")
        print(result)

        product_list = []
        for row in result:
            if row[1] > 0:
                product_list.append(row)

        return product_list

    def GetProductsBy():
        pass

    def GetAllUsers():
        pass

    def GetUsersBy():
        pass

    def GetAllAdmins():
        pass
    
    def GetAdminsBy():
        pass

    def AddProduct():
        pass

    def AddUser():
        pass

    def MakeAdmin():
        pass

    def UnMakeAdmin():
        pass

    def DeleteProduct():
        pass

    
    def CleanData():
        pass