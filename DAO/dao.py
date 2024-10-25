import mysql.connector


class DAO:
    def __init__(self, cnx="", cursor="") -> None:
        self.cnx = cnx
        self.cursor = cursor

    def GetAllProducts(self, columns="*"):
        self.MakeConnection()

        self.cursor.execute("USE Kamazon")
        self.cursor.execute(f"SELECT {columns} FROM Products")

        return self.cursor.fetchall()
    
    def GetProductsBy(self, conditions, columns="*"):
        self.MakeConnection()

        self.cursor.execute("USE Kamazon")
        self.cursor.execute(rf"SELECT {columns} FROM Products WHERE {conditions}")

        return self.cursor.fetchall()

    def GetAllUsers(self, columns="*"):
        self.MakeConnection()

        self.cursor.execute("USE Kamazon")
        self.cursor.execute(f"SELECT {columns} FROM Users JOIN Admins ON Users.User_ID=Admins.User_ID")

        return self.cursor.fetchall()
    
    def GetUsersBy(self, conditions, columns="*"):
        self.MakeConnection()

        self.cursor.execute("USE Kamazon")
        self.cursor.execute(rf"SELECT {columns} FROM Users JOIN Admins ON Users.User_ID=Admins.User_ID WHERE {conditions}")

        return self.cursor.fetchall()
    
    def AddProduct(self, product_name:str, product_description:str, quantity:int, price_per_unit:float):
        self.MakeConnection()

        self.cursor.execute("USE Kamazon")
        self.cursor.execute(rf"INSERT INTO Products (ProductName, ProductDescription, Quantity, PPU) VALUES ('{product_name}', '{product_description}', {quantity}, {price_per_unit})")

        self.cursor.execute("COMMIT")
        #maybe return something to let the app know it wrote properly?

    def AddUser(self, user_name:str, user_pwd:str):
        self.MakeConnection()

        self.cursor.execute("USE Kamazon")
        self.cursor.execute(rf"INSERT INTO Users (UserName, UserPwd, Cart) VALUES ('{user_name}','{user_pwd}',0)")
        self.cursor.execute("COMMIT")
        self.cursor.execute(rf"SELECT User_ID, UserName FROM Users WHERE UserName = '{user_name}' AND UserPwd = '{user_pwd}'")
        result = self.cursor.fetchall()
        new_id = result[0][0]
        
        self.cursor.execute(rf"INSERT INTO Admins (User_ID, AdminEnabled) VALUES ({new_id}, False)") #insert into admin as well as false
        self.cursor.execute("COMMIT")

        self.CloseConnection()

    def EditAdmin(self, user_id, access):
        self.MakeConnection()

        self.cursor.execute("USE Kamazon")
        self.cursor.execute(f"UPDATE Admins SET AdminEnabled = {access} WHERE User_ID = {user_id}")

        self.cursor.execute("COMMIT")

        self.CloseConnection()

    def UpdateProduct(self, product_id, attributes):
        self.MakeConnection()

        self.cursor.execute("USE Kamazon")
        self.cursor.execute(f"UPDATE Products SET {attributes} WHERE Product_ID = {product_id}")
        self.cursor.execute("COMMIT")

        self.CloseConnection()

    def UpdateUser(self, user_id, attributes):
        self.MakeConnection()

        self.cursor.execute("USE Kamazon")
        self.cursor.execute(f"UPDATE Users SET {attributes} WHERE User_ID = {user_id}")
        self.cursor.execute("COMMIT")

        self.CloseConnection()

    def DeleteProduct(self, product_id):
        self.MakeConnection()

        self.cursor.execute("USE Kamazon")
        self.cursor.execute(f"DELETE FROM Products WHERE Product_ID = {product_id}")

        self.cursor.execute("COMMIT")

        self.CloseConnection()

        

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