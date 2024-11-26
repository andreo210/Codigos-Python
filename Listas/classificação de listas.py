# Objetos de lista têm um sort()método que classificará a
# lista alfanumericamente, em ordem crescente, por padrão

# Classifique a lista em ordem alfabética
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)


# Classifique a lista numericamente:
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# Classifique a lista em ordem decrescente:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
print(thislist)


# Classifique a lista em ordem decrescente:
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=True)
print(thislist)


"""
Personalizar função de classificação
Você também pode personalizar sua própria função usando o
 argumento de palavra-chave .key = function 
A função retornará um número que será usado para 
classificar a lista (o menor número primeiro):
"""

# Classifique a lista com base na proximidade do número de 50

def myfunc(n):
    return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)
print(thislist)


# A classificação com distinção entre maiúsculas e
#  minúsculas pode gerar um resultado inesperado:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)


# Execute uma classificação da lista que não
#  diferencia maiúsculas de minúsculas
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower)
print(thislist)


# Inverta a ordem dos itens da lista:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)