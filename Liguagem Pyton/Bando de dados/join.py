"""
Junte duas ou mais tabelas
Você pode combinar linhas de duas ou mais tabelas, com base em uma coluna relacionada entre elas, usando uma instrução JOIN.
Considere que você tem uma tabela "usuários" e uma tabela "produtos":
"""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  INNER JOIN products ON users.fav = products.id"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)