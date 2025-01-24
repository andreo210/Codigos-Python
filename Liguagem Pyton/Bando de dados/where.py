"""
Selecione com um filtro
Ao selecionar registros de uma tabela, você pode filtrar a seleção usando a instrução "WHERE":
"""
# Selecione registro(s) onde o endereço é "Park Lane 38": resultado:
import mysql.connector as my

mydb = my.connect(
  host="localhost",
  user="root",
  password="123456",
  database ="teste"
)

mycursor = mydb.cursor()



sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)



  """
Caracteres curinga
Você também pode selecionar os registros que começam, incluem ou terminam com uma determinada letra ou frase.

Use %  para representar caracteres curinga:
"""
sql = "SELECT * FROM customers WHERE address LIKE '%way%'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)