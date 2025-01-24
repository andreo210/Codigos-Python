# Imprima todos os itens da lista, um por um:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)


# Imprima todos os itens consultando seu número de índice:
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])

# Imprima todos os itens, usando um whileloop para
#  percorrer todos os números de índice
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1


# Compreensão de Lista oferece a sintaxe mais curta para percorrer listas:
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]