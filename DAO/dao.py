import mysql.connector


class DAO:
    def __init__(self, cnx="", cursor="") -> None:
        self.cnx = cnx
        self.cursor = cursor

    def GetAllProducts(self, columns="*"):
        self.cursor.execute("USE Products")
        self.cursor.execute(f"SELECT {columns} FROM Products")

        return self.cursor.fetchall()
    
    def GetProductsBy(self, conditions, columns="*"):
        self.cursor.execute("USE Products")
        self.cursor.execute(f"SELECT {columns} FROM Products WHERE {conditions}")

        return self.cursor.fetchall()

    def GetAllUsers(self, columns="*"):
        self.cursor.execute("USE User")
        self.cursor.execute(f"SELECT {columns} FROM User")

        return self.cursor.fetchall()
    
    def GetUsersBy(self, conditions, columns="*"):
        self.cursor.execute("USE User")
        self.cursor.execute(f"SELECT {columns} FROM Users WHERE {conditions}")

        return self.cursor.fetchall()

    def GetAllAdmins(self, columns="*"):
        self.cursor.execute("USE Users")
        self.cursor.execute(f"SELECT {columns} FROM Users JOIN Admins ON Users.User_ID=Admins.User_ID")

        return self.cursor.fetchall()
    
    def GetAdminsBy(self, conditions, columns="*"):
        self.cursor.execute("USE Products")
        self.cursor.execute(f"SELECT {columns} FROM Users WHERE {conditions}")

        return self.cursor.fetchall()
    
    def AddProduct(self, product_name:str, product_description:str, quantity:int, price_per_unit:float):
        self.cursor.execute("USE Products")
        self.cursor.execute(f"INSERT INTO Products (ProductName, ProductDescription, Quantity, PPU) VALUES ({product_name}, {product_description}, {quantity}, {price_per_unit})")

        #maybe return something to let the app know it wrote properly?

    def AddUser(self, user_name:str, user_pwd:str, cart:int):
        self.cursor.execute("USE Users")
        self.cursor.execute(f"INSERT INTO Users (UserName, UserPwd, Cart) VALUES ({user_name},{user_pwd},{cart})")
        self.cursor.execute("") #insert into admin as well as false

    def MakeAdmin(self, user_id):
        self.cursor.execute("USE Admins")
        self.cursor.execute(f"UPDATE Admins SET AdminEnabled = True WHERE User_ID = {user_id}")

    def UnMakeAdmin(self, user_id):
        self.cursor.execute("USE Admins")
        self.cursor.execute(f"UPDATE Admins SET AdminEnabled = False WHERE User_ID = {user_id}")
        

    # def GetData4(self, columns):
    #     self.cursor.execute("USE Products")
    #     self.cursor.execute(f"SELECT {columns} FROM Products")

    #     return self.cursor.fetchall()

    # def GetData5(self, columns):
    #     self.cursor.execute("USE Products")
    #     self.cursor.execute(f"SELECT {columns} FROM Products")

    #     return self.cursor.fetchall()

    def MakeConnection(self):
        self.cnx = mysql.connector.connect(user="root", password="tSn3U-vDA>4^!),E", host="localhost", database="")
        self.cursor = self.cnx.cursor()

    def CloseConnection(self):
        self.cursor.close()
        self.cnx.close()