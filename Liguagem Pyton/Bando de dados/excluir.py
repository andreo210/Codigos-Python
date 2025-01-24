"""
Excluir registro
Você pode excluir registros de uma tabela existente usando a instrução "DELETE FROM":
Observe a declaração: mydb.commit(). É necessário fazer as alterações, caso contrário, nenhuma alteração será feita na tabela.
"""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "DELETE FROM customers WHERE address = 'Mountain 21'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")




"""
Prevenir injeção de SQL
É considerada uma boa prática escapar os valores de qualquer consulta, também em instruções delete.

Isso evita injeções de SQL, uma técnica comum de invasão na web para destruir ou usar indevidamente seu banco de dados.
O módulo mysql.connector usa o espaço reservado %spara escapar valores na instrução delete:
"""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "DELETE FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )

mycursor.execute(sql, adr)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")