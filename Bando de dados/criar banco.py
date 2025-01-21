"""
Criando um banco de dados
Para criar um banco de dados no MySQL, use a instrução "CREATE DATABASE":
"""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123456"
)
mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE teste")

# Verifique se o banco de dados existe
mycursor.execute("SHOW DATABASES")
for x in mycursor:
  print(x)