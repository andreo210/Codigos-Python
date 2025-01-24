"""
Atualizar tabela
Você pode atualizar registros existentes em uma tabela usando a instrução "UPDATE":
"""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")




"""
Prevenir injeção de SQL
É considerada uma boa prática escapar os valores de qualquer consulta, também em instruções de atualização.
Isso evita injeções de SQL, uma técnica comum de invasão na web para destruir ou usar indevidamente seu banco de dados.

O módulo mysql.connector usa o espaço reservado %spara escapar valores na instrução de atualização:
"""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "UPDATE customers SET address = %s WHERE address = %s"
val = ("Valley 345", "Canyon 123")

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")