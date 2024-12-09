"""
Alterar valores de tupla
Uma vez que uma tupla é criada, você não pode alterar seus valores. 
Tuplas são inalteráveis , ou imutáveis ​​como também são chamadas.
Mas há uma solução alternativa. Você pode converter a tupla em uma lista, 
alterar a lista e converter a lista de volta em uma tupla.

"""

# Converta a tupla em uma lista para poder alterá-la:

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)


"""
Adicionar itens
Como as tuplas são imutáveis, elas não têm um método interno append(), 
mas existem outras maneiras de adicionar itens a uma tupla.
1. Converter em uma lista : assim como na solução alternativa para 
alterar uma tupla, você pode convertê-la em uma lista,
 adicionar seus itens e convertê-la novamente em uma tupla.
"""
# Converta a tupla em uma lista, adicione "laranja"
#  e converta-a novamente em uma tupla:

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)


"""
Adicione tupla a uma tupla . Você tem permissão para adicionar tuplas a tuplas,
 então se você quiser adicionar um item, (ou muitos), 
 crie uma nova tupla com o(s) item(ns), e adicione-a à tupla existente:
"""
# Crie uma nova tupla com o valor "laranja" e adicione essa tupla:
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)


"""
Tuplas são imutáveis , então você não pode remover itens delas, 
mas você pode usar a mesma solução alternativa que usamos para alterar
 e adicionar itens de tupla:
"""
# Converta a tupla em uma lista, remova "apple" 
# e converta-a novamente em uma tupla:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)


# A delpalavra-chave pode excluir a tupla completamente:
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) 