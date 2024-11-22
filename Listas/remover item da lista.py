# O remove() remove o item especificado.
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# Remova a primeira ocorrência de "banana":
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

# O pop() remove o índice especificado.
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# Se você não especificar o índice, o pop() removerá o último item.
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# A palavra-chave del também remove o índice especificado:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# A palavra-chave  deltambém pode excluir a lista completamente.
thislist = ["apple", "banana", "cherry"]
del thislist

# O clear() esvazia a lista.
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)