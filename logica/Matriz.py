"""
Observação: o Python não tem suporte integrado para matrizes, mas pode ser usada lista.

Exemplo: 
Crie uma matriz contendo nomes de carros:
"""
cars = ["Ford", "Volvo", "BMW"]
for x in cars:
    print(x)


"""
Adicionando elementos de matriz
Você pode usar o append() para adicionar um elemento a uma matriz
"""
cars.append("Honda")
for x in cars:
    print(x)


"""Exclua o segundo elemento da matriz"""
cars.pop(1) # ou
cars.remove("Volvo")


"""
Métodos de matriz
O Python tem um conjunto de métodos integrados que você pode usar em listas/matrizes.

Method	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
"""