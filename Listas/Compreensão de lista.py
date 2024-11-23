"""
A compreensão de lista oferece uma sintaxe mais curta quando você deseja criar
 uma nova lista com base nos valores de uma lista existente.

Exemplo:
Com base em uma lista de frutas, você quer uma nova lista, contendo apenas
 as frutas com a letra "a" no nome.

Sem compreensão de lista, você terá que escrever uma
 for declaração com um teste condicional dentro:
"""

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)


# Com a compreensão de lista você pode fazer
#  tudo isso com apenas uma linha de código:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

# Aceite apenas itens que não sejam "apple":
newlist = [x for x in fruits if x != "apple"]
print(newlist)


# Sem declaração if:
newlist = [x for x in fruits]
print(newlist)


"""Iterável(laço)""" 
# Você pode usar a função range()para criar um iterável:
newlist = [x for x in range(10)]
print(newlist)

# Aceite apenas números menores que 5:
newlist = [x for x in range(10) if x < 5]
print(newlist)


"""Expressão""" 
# Defina os valores na nova lista para letras maiúsculas:
newlist = [x.upper() for x in fruits]
print(newlist)

# Defina todos os valores na nova lista como 'hello':
newlist = ['hello' for x in fruits]
print(newlist)

# A expressão também pode conter condições, não como um filtro,
#  mas como uma forma de manipular o resultad
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)