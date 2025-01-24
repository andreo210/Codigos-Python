"""
Limite o resultado
Você pode limitar o número de registros retornados da consulta usando a instrução "LIMIT":
"""
# Selecione os 5 primeiros registros na tabela "clientes":
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers LIMIT 5")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)



"""
Comece de outra posição
Se você quiser retornar cinco registros, começando pelo terceiro registro, você pode usar a palavra-chave "OFFSET":
"""
# Comece na posição 3 e retorne 5 registros:
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)