# Junte-se a duas listas
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)


# Outra maneira de unir duas listas é anexar todos os
#  itens da lista2 na lista1, um por um:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)
print(list1)


# Use o extend()método para adicionar list2 no final de list1
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)