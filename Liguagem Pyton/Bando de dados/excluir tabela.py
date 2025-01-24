"""
Excluir uma tabela
Você pode excluir uma tabela existente usando a instrução "DROP TABLE":
"""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "DROP TABLE customers"

mycursor.execute(sql)





"""
somente se existir
Se a tabela que você deseja excluir já tiver sido excluída ou, por qualquer outro motivo, não existir, você pode usar a palavra-chave IF EXISTS para evitar um erro.
"""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "DROP TABLE IF EXISTS customers"

mycursor.execute(sql)