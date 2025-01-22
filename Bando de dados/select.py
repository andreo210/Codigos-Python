"""
Selecione de uma tabela
Para selecionar de uma tabela no MySQL, use a instrução "SELECT":
"""
import mysql.connector

mydb = mysql.connector.connect(
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
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchone()
print(myresult)