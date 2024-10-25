DROP DATABASE IF EXISTS Kamazon;
CREATE DATABASE Kamazon;

USE Kamazon;

DROP TABLE IF EXISTS Users;
CREATE TABLE Users (
	User_ID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    UserName VARCHAR(25),
    UserPwd VARCHAR(30),
    Cart INT
    );
TRUNCATE Users;
INSERT INTO Users (UserName, UserPwd, Cart) VALUES
	('james', 'P@ssw0rd', 0),
    ('Admin', 'An!Adm1n!passw0rd', 0);

DROP TABLE IF EXISTS Admins;
CREATE TABLE Admins (
	User_ID INT NOT NULL,
    AdminEnabled BOOLEAN NOT NULL,
    FOREIGN KEY (User_ID) REFERENCES Users(User_ID)
);
TRUNCATE Admins;
INSERT INTO Admins (User_ID, AdminEnabled) VALUES 
	(1, False),
    (2, True);

DROP TABLE IF EXISTS Products;
CREATE TABLE Products (
	Product_ID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    ProductName VARCHAR(25),
    ProductDescription VARCHAR(255),
    Quantity INT NOT NULL,
    PPU FLOAT
);
TRUNCATE Products;
INSERT INTO Products (ProductName, ProductDescription, Quantity, PPU) VALUES 
	("Pepis", "A 16oz bottle of pepis-flavored soda", 10, 2.25);