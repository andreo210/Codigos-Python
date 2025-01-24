"""
Definição e uso
O count()método retorna o número de vezes
que um valor especificado aparece na tupla
"""
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x)






"""
Definição e uso
O index()método encontra a primeira ocorrência do valor especificado.
O index()método gera uma exceção se o valor não for encontrado.
"""
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x)