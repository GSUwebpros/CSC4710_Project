import mysql.connector
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'

conn = mysql.connector.connect(
    user='root',
    password='csc4710$database',
    host='localhost'
)

cursor = conn.cursor()
query = 'CREATE DATABASE IF NOT EXISTS Retail_Application;'
cursor.execute(query)

query = 'CREATE TABLE IF NOT EXISTS Retail_Application.Users(UserID INT PRIMARY KEY NOT NULL auto_increment, FirstName VARCHAR(255) NOT NULL, LastName VARCHAR(255) NOT NULL, Username VARCHAR(100) UNIQUE NOT NULL, pwd VARCHAR(16) NOT NULL, address VARCHAR(255) NOT NULL, Tokens INT DEFAULT 0);'
cursor.execute(query)

query = 'CREATE TABLE IF NOT EXISTS Retail_Application.Inventory(ID INT PRIMARY KEY NOT NULL, Current_Stock INT)'
cursor.execute(query)

query = 'CREATE TABLE IF NOT EXISTS Retail_Application.Product(ProductID INT PRIMARY KEY NOT NULL auto_increment, Name VARCHAR(255) UNIQUE NOT NULL, Price DECIMAL(10, 2) NOT NULL, image_file_path VARCHAR(255), category VARCHAR(100) NOT NULL, InventoryID INT, FOREIGN KEY(InventoryID) REFERENCES Retail_Application.Inventory(ID))'
cursor.execute(query)

query = 'CREATE TABLE IF NOT EXISTS Retail_Application.ShoppingCart(CartID INT PRIMARY KEY NOT NULL auto_increment, Quantity INT NOT NULL, Amount_Due Decimal(10,2) NOT NULL, TransactionID INT, FOREIGN KEY(TransactionID) REFERENCES Retail_Application.Transaction(TransactionID))'
cursor.execute(query)

query = 'CREATE TABLE IF NOT EXISTS Retail_Application.Cart_consistsof_Product(CID INT, PID INT, Primary Key(CID, PID), FOREIGN KEY(CID) REFERENCES Retail_Application.ShoppingCart(CartID) ON DELETE CASCADE, FOREIGN KEY(PID) REFERENCES Retail_Application.Product(ProductID) ON DELETE CASCADE)'
cursor.execute(query)

query = 'CREATE TABLE IF NOT EXISTS Retail_Application.Transaction(TransactionID INT PRIMARY KEY NOT NULL auto_increment, Amount_Paid Decimal(10,2) NOT NULL, Full_Name VARCHAR(255) NOT NULL, Email VARCHAR(150) NOT NULL, Card_num VARCHAR(16) NOT NULL, Name_on_card VARCHAR(255) NOT NULL, ExpiryMonth VARCHAR(9), CVV SMALLINT NOT NULL, ExpiryYear SMALLINT NOT NULL, Address VARCHAR(255) NOT NULL, City VARCHAR(50), State VARCHAR(2), ZipCode SMALLINT NOT NULL, UserID INT NOT NULL, FOREIGN KEY(UserID) REFERENCES Users(UserID) )'
cursor.execute(query)

query= 'CREATE TABLE IF NOT EXISTS Retail_Application.User_shops_Product(ProductID INT, UserID INT, PRIMARY KEY(UserID, ProductID), FOREIGN KEY(UserID) REFERENCES Users(UserID), FOREIGN KEY(ProductID) REFERENCES Product(ProductID))'
cursor.execute(query)

query = 'CREATE TABLE IF NOT EXISTS Retail_Application.Reviews(ReviewID INT Primary Key NOT NULL auto_increment, ReviewerID INT, Username VARCHAR(100) NOT NULL,Title VARCHAR(255) NOT NULL, Review TEXT(1000) NOT NULL, FOREIGN KEY(ReviewerID) REFERENCES Users(UserID))'
cursor.execute(query)

cursor.execute('INSERT IGNORE INTO Retail_Application.Inventory(ID, Current_Stock) VALUES (1, 10)')
cursor.execute('INSERT IGNORE INTO Retail_Application.Inventory(ID, Current_Stock) VALUES (2, 15)')
cursor.execute('INSERT IGNORE INTO Retail_Application.Inventory(ID, Current_Stock) VALUES (3, 7)')
cursor.execute('INSERT IGNORE INTO Retail_Application.Inventory(ID, Current_Stock) VALUES (4, 5)')
cursor.execute('INSERT IGNORE INTO Retail_Application.Inventory(ID, Current_Stock) VALUES (5, 8)')
cursor.execute('INSERT IGNORE INTO Retail_Application.Inventory(ID, Current_Stock) VALUES (6,6)')
cursor.execute('INSERT IGNORE INTO Retail_Application.Inventory(ID, Current_Stock) VALUES (7, 12)')
cursor.execute('INSERT IGNORE INTO Retail_Application.Inventory(ID, Current_Stock) VALUES (8, 10)')
cursor.execute('INSERT IGNORE INTO Retail_Application.Inventory(ID, Current_Stock) VALUES (9, 9)')
cursor.execute('INSERT IGNORE INTO Retail_Application.Inventory(ID, Current_Stock) VALUES (10, 9)')
cursor.execute('INSERT IGNORE INTO Retail_Application.Inventory(ID, Current_Stock) VALUES (11, 19)')
cursor.execute('INSERT IGNORE INTO Retail_Application.Inventory(ID, Current_Stock) VALUES (12, 8)')
cursor.execute('INSERT IGNORE INTO Retail_Application.Inventory(ID, Current_Stock) VALUES (13, 3)')
cursor.execute('INSERT IGNORE INTO Retail_Application.Inventory(ID, Current_Stock) VALUES (14, 6)')
cursor.execute('INSERT IGNORE INTO Retail_Application.Inventory(ID, Current_Stock) VALUES (15, 10)')
cursor.execute('INSERT IGNORE INTO Retail_Application.Inventory(ID, Current_Stock) VALUES (16, 4)')
cursor.execute('INSERT IGNORE INTO Retail_Application.Inventory(ID, Current_Stock) VALUES (17, 2)')
cursor.execute('INSERT IGNORE INTO Retail_Application.Inventory(ID, Current_Stock) VALUES (18, 11)')
cursor.execute('INSERT IGNORE INTO Retail_Application.Inventory(ID, Current_Stock) VALUES (19, 7)')
cursor.execute('INSERT IGNORE INTO Retail_Application.Inventory(ID, Current_Stock) VALUES (20, 2)')
cursor.execute('INSERT IGNORE INTO Retail_Application.Inventory(ID, Current_Stock) VALUES (21, 2)')
cursor.execute('INSERT IGNORE INTO Retail_Application.Inventory(ID, Current_Stock) VALUES (22, 5)')
cursor.execute('INSERT IGNORE INTO Retail_Application.Inventory(ID, Current_Stock) VALUES (23, 3)')
cursor.execute('INSERT IGNORE INTO Retail_Application.Inventory(ID, Current_Stock) VALUES (24, 6)')
cursor.execute('INSERT IGNORE INTO Retail_Application.Inventory(ID, Current_Stock) VALUES (25, 10)')
cursor.execute('INSERT IGNORE INTO Retail_Application.Inventory(ID, Current_Stock) VALUES (26, 4)')
cursor.execute('INSERT IGNORE INTO Retail_Application.Inventory(ID, Current_Stock) VALUES (27, 2)')
cursor.execute('INSERT IGNORE INTO Retail_Application.Inventory(ID, Current_Stock) VALUES (28, 1)')
cursor.execute('INSERT IGNORE INTO Retail_Application.Inventory(ID, Current_Stock) VALUES (29, 7)')
cursor.execute('INSERT IGNORE INTO Retail_Application.Inventory(ID, Current_Stock) VALUES (30, 2)')
cursor.execute('INSERT IGNORE INTO Retail_Application.Inventory(ID, Current_Stock) VALUES (31, 2)')
cursor.execute('INSERT IGNORE INTO Retail_Application.Inventory(ID, Current_Stock) VALUES (32, 5)')
cursor.execute('INSERT IGNORE INTO Retail_Application.Inventory(ID, Current_Stock) VALUES (33, 3)')
cursor.execute('INSERT IGNORE INTO Retail_Application.Inventory(ID, Current_Stock) VALUES (34, 6)')
cursor.execute('INSERT IGNORE INTO Retail_Application.Inventory(ID, Current_Stock) VALUES (35, 10)')
cursor.execute('INSERT IGNORE INTO Retail_Application.Inventory(ID, Current_Stock) VALUES (36, 4)')
cursor.execute('INSERT IGNORE INTO Retail_Application.Inventory(ID, Current_Stock) VALUES (37, 2)')
cursor.execute('INSERT IGNORE INTO Retail_Application.Inventory(ID, Current_Stock) VALUES (38, 1)')
cursor.execute('INSERT IGNORE INTO Retail_Application.Inventory(ID, Current_Stock) VALUES (39, 3)')
cursor.execute('INSERT IGNORE INTO Retail_Application.Inventory(ID, Current_Stock) VALUES (40, 6)')
cursor.execute('INSERT IGNORE INTO Retail_Application.Inventory(ID, Current_Stock) VALUES (41, 10)')
cursor.execute('INSERT IGNORE INTO Retail_Application.Inventory(ID, Current_Stock) VALUES (42, 4)')
cursor.execute('INSERT IGNORE INTO Retail_Application.Inventory(ID, Current_Stock) VALUES (43, 2)')
cursor.execute('INSERT IGNORE INTO Retail_Application.Inventory(ID, Current_Stock) VALUES (44, 1)')
cursor.execute('INSERT IGNORE INTO Retail_Application.Inventory(ID, Current_Stock) VALUES (45, 1)')


cursor.execute('INSERT IGNORE INTO Retail_Application.Inventory(ID, Current_Stock) VALUES (46, 6)')
cursor.execute('INSERT IGNORE INTO Retail_Application.Inventory(ID, Current_Stock) VALUES (47, 10)')
cursor.execute('INSERT IGNORE INTO Retail_Application.Inventory(ID, Current_Stock) VALUES (48, 4)')
cursor.execute('INSERT IGNORE INTO Retail_Application.Inventory(ID, Current_Stock) VALUES (49, 2)')
cursor.execute('INSERT IGNORE INTO Retail_Application.Inventory(ID, Current_Stock) VALUES (50, 1)')
cursor.execute('INSERT IGNORE INTO Retail_Application.Inventory(ID, Current_Stock) VALUES (51, 7)')
cursor.execute('INSERT IGNORE INTO Retail_Application.Inventory(ID, Current_Stock) VALUES (52, 2)')
cursor.execute('INSERT IGNORE INTO Retail_Application.Inventory(ID, Current_Stock) VALUES (53, 2)')
cursor.execute('INSERT IGNORE INTO Retail_Application.Inventory(ID, Current_Stock) VALUES (54, 5)')
cursor.execute('INSERT IGNORE INTO Retail_Application.Inventory(ID, Current_Stock) VALUES (55, 3)')
cursor.execute('INSERT IGNORE INTO Retail_Application.Inventory(ID, Current_Stock) VALUES (56, 6)')
cursor.execute('INSERT IGNORE INTO Retail_Application.Inventory(ID, Current_Stock) VALUES (57, 10)')
cursor.execute('INSERT IGNORE INTO Retail_Application.Inventory(ID, Current_Stock) VALUES (58, 4)')
cursor.execute('INSERT IGNORE INTO Retail_Application.Inventory(ID, Current_Stock) VALUES (59, 2)')
cursor.execute('INSERT IGNORE INTO Retail_Application.Inventory(ID, Current_Stock) VALUES (60, 1)')
cursor.execute('INSERT IGNORE INTO Retail_Application.Inventory(ID, Current_Stock) VALUES (61, 3)')
cursor.execute('INSERT IGNORE INTO Retail_Application.Inventory(ID, Current_Stock) VALUES (62, 6)')
cursor.execute('INSERT IGNORE INTO Retail_Application.Inventory(ID, Current_Stock) VALUES (63, 10)')
cursor.execute('INSERT IGNORE INTO Retail_Application.Inventory(ID, Current_Stock) VALUES (64, 4)')



# insert all xbox one products into product table
path = "img/Xbox One/fifa.jpg"
category = "Xbox One"
cursor.execute("INSERT IGNORE INTO Retail_Application.Product(Name, Price, image_file_path, category, InventoryID) VALUES (%s, %s, %s, %s, %s);", ("FIFA 23 - Xbox One", 23.99, path, category, 1))

path = "img/Xbox One/blackops3.jpg"
cursor.execute("INSERT IGNORE INTO Retail_Application.Product(Name, Price, image_file_path, category, InventoryID) VALUES (%s, %s, %s, %s, %s);", ("Call of Duty: Black Ops III - Xbox One", 19.99, path, category, 2))

path = "img/Xbox One/modern_warfare.jpg"
cursor.execute("INSERT IGNORE INTO Retail_Application.Product(Name, Price, image_file_path, category, InventoryID) VALUES (%s, %s, %s, %s, %s);", ("Call of Duty: Modern Warfare - Xbox One", 17.99, path, category, 3))

path = "img/Xbox One/hogwarts.jpg"
cursor.execute("INSERT IGNORE INTO Retail_Application.Product(Name, Price, image_file_path, category, InventoryID) VALUES (%s, %s, %s, %s, %s);", ("Hogwarts Legacy - Xbox One", 59.99, path, category, 4))

path = "img/Xbox One/madden.jpg"
cursor.execute("INSERT IGNORE INTO Retail_Application.Product(Name, Price, image_file_path, category, InventoryID) VALUES (%s, %s, %s, %s, %s);", ("Madden 23 - Xbox One", 17.99, path, category, 5))

path = "img/Xbox One/mlb.jpg"
cursor.execute("INSERT IGNORE INTO Retail_Application.Product(Name, Price, image_file_path, category, InventoryID) VALUES (%s, %s, %s, %s, %s);", ("MLB The Show 23 - Xbox One", 59.99, path, category, 6))

path = "img/Xbox One/nba.jpg"
cursor.execute("INSERT IGNORE INTO Retail_Application.Product(Name, Price, image_file_path, category, InventoryID) VALUES (%s, %s, %s, %s, %s);", ("NBA 2K23 - Xbox One", 18.99, path, category, 7))

path = "img/Xbox One/wwe.jpg"
cursor.execute("INSERT IGNORE INTO Retail_Application.Product(Name, Price, image_file_path, category, InventoryID) VALUES (%s, %s, %s, %s, %s);", ("WWE  2K23 - Xbox One", 59.99, path, category, 8))

path = "img/Xbox One/supercross.jpg"
cursor.execute("INSERT IGNORE INTO Retail_Application.Product(Name, Price, image_file_path, category, InventoryID) VALUES (%s, %s, %s, %s, %s);", ("Monster Energy Supercross 6 - Xbox One", 59.99, path, category, 9))



# insert xbox series x products
category = "Xbox Series X|S"
path = "img/Xbox Series XS/fifa.jpg"
cursor.execute("INSERT IGNORE INTO Retail_Application.Product(Name, Price, image_file_path, category, InventoryID) VALUES (%s, %s, %s, %s, %s);", ("FIFA 23 - Xbox Series X|S", 23.99, path, category, 10))
path = "img/Xbox Series XS/blackops3.jpg"
cursor.execute("INSERT IGNORE INTO Retail_Application.Product(Name, Price, image_file_path, category, InventoryID) VALUES (%s, %s, %s, %s, %s);", ("Call of Duty: Black Ops III - Xbox Series X|S", 19.99, path, category, 11))

path = "img/Xbox Series XS/modern_warfare.jpg"
cursor.execute("INSERT IGNORE INTO Retail_Application.Product(Name, Price, image_file_path, category, InventoryID) VALUES (%s, %s, %s, %s, %s);", ("Call of Duty: Modern Warfare - Xbox Series X|S", 17.99, path, category, 12))

path = "img/Xbox Series XS/hogwarts.jpg"
cursor.execute("INSERT IGNORE INTO Retail_Application.Product(Name, Price, image_file_path, category, InventoryID) VALUES (%s, %s, %s, %s, %s);", ("Hogwarts Legacy - Xbox Series X|S", 59.99, path, category, 13))
path = "img/Xbox Series XS/madden.jpg"
cursor.execute("INSERT IGNORE INTO Retail_Application.Product(Name, Price, image_file_path, category, InventoryID) VALUES (%s, %s, %s, %s, %s);", ("Madden 23 - Xbox Series X|S", 17.99, path, category, 14))

path = "img/Xbox Series XS/mlb.jpg"
cursor.execute("INSERT IGNORE INTO Retail_Application.Product(Name, Price, image_file_path, category, InventoryID) VALUES (%s, %s, %s, %s, %s);", ("MLB The Show 23 - Xbox Series X|S", 59.99, path, category, 15))
path = "img/Xbox Series XS/nba.jpg"
cursor.execute("INSERT IGNORE INTO Retail_Application.Product(Name, Price, image_file_path, category, InventoryID) VALUES (%s, %s, %s, %s, %s);", ("NBA 2K23 - Xbox Series X|S", 18.99, path, category, 16))

path = "img/Xbox Series XS/wwe.jpg"
cursor.execute("INSERT IGNORE INTO Retail_Application.Product(Name, Price, image_file_path, category, InventoryID) VALUES (%s, %s, %s, %s, %s);", ("WWE  2K23 - Xbox Series X|S", 59.99, path, category, 17))
path = "img/Xbox Series XS/supercross.jpg"
cursor.execute("INSERT IGNORE INTO Retail_Application.Product(Name, Price, image_file_path, category, InventoryID) VALUES (%s, %s, %s, %s, %s);", ("Monster Energy Supercross 6 - Xbox Series X|S", 59.99, path, category, 18))


# insert ps4 products

path = "img/Playstation_4/fifa.jpg"
category = "Playstation 4"
cursor.execute("INSERT IGNORE INTO Retail_Application.Product(Name, Price, image_file_path, category, InventoryID) VALUES (%s, %s, %s, %s, %s);", ("FIFA 23 - Playstation 4", 23.99, path, category, 19))

path = "img/Playstation_4/blackops3.jpg"
cursor.execute("INSERT IGNORE INTO Retail_Application.Product(Name, Price, image_file_path, category, InventoryID) VALUES (%s, %s, %s, %s, %s);", ("Call of Duty: Black Ops III - Playstation 4", 19.99, path, category, 20))

path = "img/Playstation_4/modern_warfare.jpg"
cursor.execute("INSERT IGNORE INTO Retail_Application.Product(Name, Price, image_file_path, category, InventoryID) VALUES (%s, %s, %s, %s, %s);", ("Call of Duty: Modern Warfare - Playstation 4", 17.99, path, category, 21))
path = "img/Playstation_4/hogwarts.jpg"
cursor.execute("INSERT IGNORE INTO Retail_Application.Product(Name, Price, image_file_path, category, InventoryID) VALUES (%s, %s, %s, %s, %s);", ("Hogwarts Legacy - Playstation 4", 59.99, path, category, 22))

path = "img/Playstation_4/madden.jpg"
cursor.execute("INSERT IGNORE INTO Retail_Application.Product(Name, Price, image_file_path, category, InventoryID) VALUES (%s, %s, %s, %s, %s);", ("Madden 23 - Playstation 4", 17.99, path, category, 23))
path = "img/Playstation_4/mlb.jpg"
cursor.execute("INSERT IGNORE INTO Retail_Application.Product(Name, Price, image_file_path, category, InventoryID) VALUES (%s, %s, %s, %s, %s);", ("MLB The Show 23 - Playstation 4", 59.99, path, category, 24))
path = "img/Playstation_4/nba.jpg"
cursor.execute("INSERT IGNORE INTO Retail_Application.Product(Name, Price, image_file_path, category, InventoryID) VALUES (%s, %s, %s, %s, %s);", ("NBA 2K23 - Playstation 4", 18.99, path, category, 25))
path = "img/Playstation_4/wwe.jpg"
cursor.execute("INSERT IGNORE INTO Retail_Application.Product(Name, Price, image_file_path, category, InventoryID) VALUES (%s, %s, %s, %s, %s);", ("WWE  2K23 - Playstation 4", 59.99, path, category, 26))
path = "img/Playstation_4/supercross.jpg"
cursor.execute("INSERT IGNORE INTO Retail_Application.Product(Name, Price, image_file_path, category, InventoryID) VALUES (%s, %s, %s, %s, %s);", ("Monster Energy Supercross 6 - Playstation 4", 59.99, path, category, 27))


# insert ps5 products
category = "Playstation 5"
path = "img/Playstation_5/fifa.jpg"
cursor.execute("INSERT IGNORE INTO Retail_Application.Product(Name, Price, image_file_path, category, InventoryID) VALUES (%s, %s, %s, %s, %s);", ("FIFA 23 - Playstation 5", 23.99, path, category, 28))
path = "img/Playstation_5/blackops3.jpg"
cursor.execute("INSERT IGNORE INTO Retail_Application.Product(Name, Price, image_file_path, category, InventoryID) VALUES (%s, %s, %s, %s, %s);", ("Call of Duty: Black Ops III - Playstation 5", 19.99, path, category, 29))
path = "img/Playstation_5/modern_warfare.jpg"
cursor.execute("INSERT IGNORE INTO Retail_Application.Product(Name, Price, image_file_path, category, InventoryID) VALUES (%s, %s, %s, %s, %s);", ("Call of Duty: Modern Warfare - Playstation 5", 17.99, path, category, 30))
path = "img/Playstation_5/hogwarts.jpg"
cursor.execute("INSERT IGNORE INTO Retail_Application.Product(Name, Price, image_file_path, category, InventoryID) VALUES (%s, %s, %s, %s, %s);", ("Hogwarts Legacy - Playstation 5", 59.99, path, category, 31))
path = "img/Playstation_5/madden.jpg"
cursor.execute("INSERT IGNORE INTO Retail_Application.Product(Name, Price, image_file_path, category, InventoryID) VALUES (%s, %s, %s, %s, %s);", ("Madden 23 - Playstation 5", 17.99, path, category, 32))
path = "img/Playstation_5/mlb.jpg"
cursor.execute("INSERT IGNORE INTO Retail_Application.Product(Name, Price, image_file_path, category, InventoryID) VALUES (%s, %s, %s, %s, %s);", ("MLB The Show 23 - Playstation 5", 59.99, path, category, 33))
path = "img/Playstation_5/nba.jpg"
cursor.execute("INSERT IGNORE INTO Retail_Application.Product(Name, Price, image_file_path, category, InventoryID) VALUES (%s, %s, %s, %s, %s);", ("NBA 2K23 - Playstation 5", 18.99, path, category, 34))
path = "img/Playstation_5/wwe.jpg"
cursor.execute("INSERT IGNORE INTO Retail_Application.Product(Name, Price, image_file_path, category, InventoryID) VALUES (%s, %s, %s, %s, %s);", ("WWE  2K23 - Playstation 5", 59.99, path, category, 35))
path = "img/Playstation_5/supercross.jpg"
cursor.execute("INSERT IGNORE INTO Retail_Application.Product(Name, Price, image_file_path, category, InventoryID) VALUES (%s, %s, %s, %s, %s);", ("Monster Energy Supercross 6 - Playstation 5", 59.99, path, category, 36))

# insert switch products
category = "Nintendo Switch"
path = "img/Nintendo_Switch/fifa.jpg"
cursor.execute("INSERT IGNORE INTO Retail_Application.Product(Name, Price, image_file_path, category, InventoryID) VALUES (%s, %s, %s, %s, %s);", ("FIFA 23 - Nintendo Switch", 23.99, path, category, 37))

path = "img/Nintendo_Switch/blackops3.jpg"
cursor.execute("INSERT IGNORE INTO Retail_Application.Product(Name, Price, image_file_path, category, InventoryID) VALUES (%s, %s, %s, %s, %s);", ("Call of Duty: Black Ops III - Nintendo Switch", 19.99, path, category, 38))
path = "img/Nintendo_Switch/modern_warfare.jpg"
cursor.execute("INSERT IGNORE INTO Retail_Application.Product(Name, Price, image_file_path, category, InventoryID) VALUES (%s, %s, %s, %s, %s);", ("Call of Duty: Modern Warfare - Nintendo Switch", 17.99, path, category, 39))
path = "img/Nintendo_Switch/hogwarts.jpg"
cursor.execute("INSERT IGNORE INTO Retail_Application.Product(Name, Price, image_file_path, category, InventoryID) VALUES (%s, %s, %s, %s, %s);", ("Hogwarts Legacy - Nintendo Switch", 59.99, path, category, 40))
path = "img/Nintendo_Switch/madden.jpg"
cursor.execute("INSERT IGNORE INTO Retail_Application.Product(Name, Price, image_file_path, category, InventoryID) VALUES (%s, %s, %s, %s, %s);", ("Madden 23 - Nintendo Switch", 17.99, path, category, 41))
path = "img/Nintendo_Switch/mlb.jpg"
cursor.execute("INSERT IGNORE INTO Retail_Application.Product(Name, Price, image_file_path, category, InventoryID) VALUES (%s, %s, %s, %s, %s);", ("MLB The Show 23 - Nintendo Switch", 59.99, path, category, 42))
path = "img/Nintendo_Switch/nba.jpg"
cursor.execute("INSERT IGNORE INTO Retail_Application.Product(Name, Price, image_file_path, category, InventoryID) VALUES (%s, %s, %s, %s, %s);", ("NBA 2K23 - Nintendo Switch", 18.99, path, category, 43))
path = "img/Nintendo_Switch/wwe.jpg"
cursor.execute("INSERT IGNORE INTO Retail_Application.Product(Name, Price, image_file_path, category, InventoryID) VALUES (%s, %s, %s, %s, %s);", ("WWE  2K23 - Nintendo Switch", 59.99, path, category, 44))
path = "img/Nintendo_Switch/supercross.jpg"
cursor.execute("INSERT IGNORE INTO Retail_Application.Product(Name, Price, image_file_path, category, InventoryID) VALUES (%s, %s, %s, %s, %s);", ("Monster Energy Supercross 6 - Nintendo Switch", 59.99, path, category, 45))


category = "PC Games"
path = "img/PC_Games/fifa.jpg"
cursor.execute("INSERT IGNORE INTO Retail_Application.Product(Name, Price, image_file_path, category, InventoryID) VALUES (%s, %s, %s, %s, %s);", ("FIFA 23 - PC", 23.99, path, category, 46))
path = "img/PC_Games/blackops3.jpg"
cursor.execute("INSERT IGNORE INTO Retail_Application.Product(Name, Price, image_file_path, category, InventoryID) VALUES (%s, %s, %s, %s, %s);", ("Call of Duty: Black Ops III - PC", 19.99, path, category, 47))
path = "img/PC_Games/modern_warfare.jpg"
cursor.execute("INSERT IGNORE INTO Retail_Application.Product(Name, Price, image_file_path, category, InventoryID) VALUES (%s, %s, %s, %s, %s);", ("Call of Duty: Modern Warfare - PC", 17.99, path, category, 48))
path = "img/PC_Games/hogwarts.jpg"
cursor.execute("INSERT IGNORE INTO Retail_Application.Product(Name, Price, image_file_path, category, InventoryID) VALUES (%s, %s, %s, %s, %s);", ("Hogwarts Legacy - PC", 59.99, path, category, 49))
path = "img/PC_Games/madden.jpg"
cursor.execute("INSERT IGNORE INTO Retail_Application.Product(Name, Price, image_file_path, category, InventoryID) VALUES (%s, %s, %s, %s, %s);", ("Madden 23 - PC", 17.99, path, category, 50))
path = "img/PC_Games/mlb.jpg"
cursor.execute("INSERT IGNORE INTO Retail_Application.Product(Name, Price, image_file_path, category, InventoryID) VALUES (%s, %s, %s, %s, %s);", ("MLB The Show 23 - PC", 59.99, path, category, 51))
path = "img/PC_Games/nba.jpg"
cursor.execute("INSERT IGNORE INTO Retail_Application.Product(Name, Price, image_file_path, category, InventoryID) VALUES (%s, %s, %s, %s, %s);", ("NBA 2K23 - PC", 18.99, path, category, 52))
path = "img/PC_Games/wwe.jpg"
cursor.execute("INSERT IGNORE INTO Retail_Application.Product(Name, Price, image_file_path, category, InventoryID) VALUES (%s, %s, %s, %s, %s);", ("WWE  2K23 - PC", 59.99, path, category, 53))
path = "img/PC_Games/supercross.jpg"
cursor.execute("INSERT IGNORE INTO Retail_Application.Product(Name, Price, image_file_path, category, InventoryID) VALUES (%s, %s, %s, %s, %s);", ("Monster Energy Supercross 6 - PC", 59.99, path, category, 54))


category = "Controllers"
path = "img/Controllers/ps4.jpg"
cursor.execute("INSERT IGNORE INTO Retail_Application.Product(Name, Price, image_file_path, category, InventoryID) VALUES (%s, %s, %s, %s, %s);", ("Playstation 4 Controller", 30.00, path, category, 55))
path = "img/Controllers/ps5.jpg"
cursor.execute("INSERT IGNORE INTO Retail_Application.Product(Name, Price, image_file_path, category, InventoryID) VALUES (%s, %s, %s, %s, %s);", ("Xbox Series X|S Controller", 60.00, path, category, 56))
path = "img/Controllers/seriesx.jpg"
cursor.execute("INSERT IGNORE INTO Retail_Application.Product(Name, Price, image_file_path, category, InventoryID) VALUES (%s, %s, %s, %s, %s);", ("Playstation 5 Controller", 60.00, path, category, 57))
path = "img/Controllers/switch.jpg"
cursor.execute("INSERT IGNORE INTO Retail_Application.Product(Name, Price, image_file_path, category, InventoryID) VALUES (%s, %s, %s, %s, %s);", ("Xbox One Controller", 30.00, path, category, 58))
path = "img/Controllers/xbox.jpg"
cursor.execute("INSERT IGNORE INTO Retail_Application.Product(Name, Price, image_file_path, category, InventoryID) VALUES (%s, %s, %s, %s, %s);", ("Nintendo Switch Controller", 25.00, path, category, 59))


category = "Consoles"

path = "img/Consoles/ps4.jpg"
cursor.execute("INSERT IGNORE INTO Retail_Application.Product(Name, Price, image_file_path, category, InventoryID) VALUES (%s, %s, %s, %s, %s);", ("Playstation 4", 299.99, path, category, 60))
path = "img/Consoles/ps5.jpg"
cursor.execute("INSERT IGNORE INTO Retail_Application.Product(Name, Price, image_file_path, category, InventoryID) VALUES (%s, %s, %s, %s, %s);", ("Playstation 5", 399.99, path, category, 61))
path = "img/Consoles/seriesx.jpg"
cursor.execute("INSERT IGNORE INTO Retail_Application.Product(Name, Price, image_file_path, category, InventoryID) VALUES (%s, %s, %s, %s, %s);", ("Xbox Series X|S", 399.99, path, category, 62))
path = "img/Consoles/switch.jpg"
cursor.execute("INSERT IGNORE INTO Retail_Application.Product(Name, Price, image_file_path, category, InventoryID) VALUES (%s, %s, %s, %s, %s);", ("Nintendo Switch", 199.99, path, category, 63))
path = "img/Consoles/xbox.jpg"
cursor.execute("INSERT IGNORE INTO Retail_Application.Product(Name, Price, image_file_path, category, InventoryID) VALUES (%s, %s, %s, %s, %s);", ("Xbox One", 299.99, path, category, 64))


conn.commit()




