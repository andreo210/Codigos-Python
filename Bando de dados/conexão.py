
"""
Testar conector MySQL
Para testar se a instalação foi bem-sucedida ou se você já tem o "MySQL Connector" instalado, crie uma página Python com o seguinte conteúdo:
"""
import mysql.connector



"""
Criar conexão
Comece criando uma conexão com o banco de dados.

Use o nome de usuário e a senha do seu banco de dados MySQL:

"""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123456"
)

print(mydb)