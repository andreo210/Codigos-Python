"""
Selecione de uma tabela
Para selecionar de uma tabela no MySQL, use a instrução "SELECT":
"""
import mysql.connector as my

mydb = my.connect(
  host="localhost",
  user="root",
  password="123456",
  database ="teste"
)
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)



"""
Selecionando Colunas
Para selecionar apenas algumas colunas em uma tabela, use a instrução "SELECT" seguida do(s) nome(s) da(s) coluna(s):
"""
mycursor.execute("SELECT name, address FROM customers")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)




"""
Usando o método fetchone()
Se você estiver interessado apenas em uma linha, você pode usar o fetchone()método.

O fetchone() retornará a primeira linha do resultado:
"""
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchone()
print(myresult)




"""
Prevenir injeção de SQL
Quando os valores da consulta são fornecidos pelo usuário, você deve escapar os valores.
Isso evita injeções de SQL, uma técnica comum de invasão na web para destruir ou usar indevidamente seu banco de dados.
O módulo mysql.connector possui métodos para escapar valores de consulta:
"""
sql = "SELECT * FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )

mycursor.execute(sql, adr)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)