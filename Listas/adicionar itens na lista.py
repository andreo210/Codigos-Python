# Para adicionar um item ao final da lista, use o método append() 
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)


# Para inserir um item de lista em um índice especificado, use o insert()
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

# Para acrescentar elementos de outra lista à lista atual, use o extend()
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# O extend() não precisa anexar listas ,
#  você pode adicionar qualquer 
# objeto iterável (tuplas, conjuntos, dicionários etc.).
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)