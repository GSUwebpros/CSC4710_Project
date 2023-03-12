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

query = 'CREATE TABLE IF NOT EXISTS Retail_Application.Users(UserID INT PRIMARY KEY NOT NULL auto_increment, FirstName VARCHAR(255) NOT NULL, LastName VARCHAR(255) NOT NULL, Username VARCHAR(100) UNIQUE NOT NULL, pwd VARCHAR(16) NOT NULL, address VARCHAR(255) NOT NULL, parent_account INT DEFAULT NULL, FOREIGN KEY(parent_account) References Users(UserID));'
cursor.execute(query)