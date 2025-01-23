"""
Classificar o resultado
Use a instrução ORDER BY para classificar o resultado em ordem crescente ou decrescente.

A palavra-chave ORDER BY classifica o resultado em ordem crescente por padrão. Para classificar o resultado em ordem decrescente, use a palavra-chave DESC.
"""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers ORDER BY name"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)





"""
ORDEM POR DESC
Use a palavra-chave DESC para classificar o resultado em ordem decrescente.
"""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers ORDER BY name DESC"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)