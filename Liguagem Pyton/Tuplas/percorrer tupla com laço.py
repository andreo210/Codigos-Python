# Você pode percorrer os itens da tupla usando um for loop.
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)


# Percorrer os números de índice
# Você também pode percorrer os itens da tupla consultando seu número de índice.
# Use as funções range()e len()para criar um iterável adequado.
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print(thistuple[i])


"""
Usando um loop While
Você pode percorrer os itens da tupla usando um whileloop.
Use a len()função para determinar o comprimento da tupla, 
então comece em 0 e percorra os itens da tupla consultando seus índices.
Lembre-se de aumentar o índice em 1 após cada iteração
"""
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1