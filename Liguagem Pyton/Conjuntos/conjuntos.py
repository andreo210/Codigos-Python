"""
Conjuntos são usados ​​para armazenar vários itens em uma única variável.
Conjunto é um dos quatro tipos de dados internos do Python u
usados ​​para armazenar coleções de dados; os outros três são Lista , 
Tupla e Dicionário , todos com qualidades e usos diferentes.
Um conjunto é uma coleção que não é ordenada , imutável* e não indexada .
Observação: os itens do conjunto são inalteráveis,
 mas você pode remover itens e adicionar novos.
"""

conjunto = {"apple", "banana", "cherry"}
print(conjunto)


# Duplicatas não permitidas
# Os conjuntos não podem ter dois itens com o mesmo valor.
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)


# Os valores True e 1são considerados o mesmo valor
#  em conjuntos e são tratados como duplicados:
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

# Os valores False e 0são considerados o mesmo valor 
# em conjuntos e são tratados como duplicados:
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)

# obter o comprimento de um conjunto
thisset = {"apple", "banana", "cherry"}
print(len(thisset))


# Definir Itens - Tipos de Dados
# Os itens definidos podem ser de qualquer tipo de dados:
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

# Um conjunto pode conter diferentes tipos de dados:
set1 = {"abc", 34, True, 40, "male"}

# Qual é o tipo de dado de um conjunto
myset = {"apple", "banana", "cherry"}
print(type(myset))

# O construtor set()
# Também é possível usar o construtor set() para criar um conjunto.
thisset = set(("apple", "banana", "cherry"))
print(thisset)