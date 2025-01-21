"""
Criando uma tabela
Para criar uma tabela no MySQL, use a instrução "CREATE TABLE".

Certifique-se de definir o nome do banco de dados ao criar a conexão
"""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123456",
  database ="teste"
)
mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")



"""
Verifique se a tabela existe
Você pode verificar se uma tabela existe listando todas as tabelas em seu banco de dados com a instrução "SHOW TABLES":
"""


mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)