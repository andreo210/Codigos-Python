"""
Tupla
Tuplas são usadas para armazenar vários itens em uma única variável.

Tupla é um dos quatro tipos de dados internos do Python usados 
​​para armazenar coleções de dados; os outros três são Lista , 
Conjunto e Dicionário , todos com qualidades e usos diferentes.
Uma tupla é uma coleção ordenada e imutável.
Tuplas são escritas com colchetes.
"""

thistuple = ("apple", "banana", "cherry")
print(thistuple)


# Comprimento da Tupla
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))


# Criar Tupla com um Item
# Para criar uma tupla com apenas um item, você precisa adicionar uma 
# vírgula após o item, caso contrário, 
# o Python não o reconhecerá como uma tupla.
thistuple = ("apple",)
print(type(thistuple))

# Não é tupla
thistuple = ("apple")
print(type(thistuple))


# Itens de Tupla - Tipos de Dados
# Os itens da tupla podem ser de qualquer tipo de dado:
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)


# Uma tupla pode conter diferentes tipos de dados
# Uma tupla com strings, inteiros e valores booleanos:
tuple1 = ("abc", 34, True, 40, "male")


# Qual é o tipo de dado de uma tupla?
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))


# Usando o método tuple() para criar uma tupla:
thistuple = tuple(("apple", "banana", "cherry")) 
print(thistuple)