from DAO.dao import DAO
from Resources.user import User

class Data:
    def __init__(self, dao=DAO()) -> None:
        self.dao = dao


    def UserLogin(self, username, password):
        result = self.dao.GetUsersBy(f"UserName = {username} AND UserPwd = {password}")
        print(result[0])
        if result[0] != "":
            return True
        else:
            return False
        
    def GetInventory(self):
        result = self.dao.GetAllProducts("ProductName, Quantity")
        print(result)
        

        return result

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