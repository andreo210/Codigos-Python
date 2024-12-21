"""
Junte conjuntos
Existem várias maneiras de juntar dois ou mais conjuntos em Python.

Os métodos union() e update() unem todos os itens de ambos os conjuntos.

O intersection() método mantém SOMENTE as duplicatas.

O difference() método mantém os itens do primeiro conjunto que não estão nos outros conjuntos.

O symmetric_difference() método mantém todos os itens EXCETO as duplicatas.
"""


"""
União
O union() método retorna um novo conjunto com todos os
 itens de ambos os conjuntos.
"""
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

# Você pode usar o |operador em vez do union()método e obterá o mesmo resultado.
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)


"""
Junte vários conjuntos
Todos os metodos e operadores de junção podem ser usados 
​​para unir vários conjuntos.
Ao usar um método, basta adicionar mais conjuntos entre parênteses,
separados por vírgulas:
"""
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)

# Ao usar o |operador, separe os conjuntos com mais |operadores:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 | set4
print(myset)


"""
Junte um conjunto e uma tupla
O union()método permite que você junte um conjunto com outros tipos de dados,
 como listas ou tuplas.
O resultado será um conjunto.
"""
x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)


"""
Atualizar
O update()método insere todos os itens de um conjunto em outro.
Isso update()altera o conjunto original e não retorna um novo conjunto.
"""
set1 = {"a", "b", "h"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)


"""
Interseção
Mantenha SOMENTE as duplicatas
O intersection()método retornará um novo conjunto, 
que contém apenas os itens que estão presentes em ambos os conjuntos.
"""
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)

# Você pode usar o &operador em vez do intersection()método e obterá o mesmo resultado.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2
print(set3)


"""
O intersection_update()método também manterá SOMENTE as duplicatas,
 mas alterará o conjunto original em vez de retornar um novo conjunto.
"""
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)

# Junte conjuntos que contenham os valores True, False, 1, e 0, e veja o que é considerado duplicado
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
set3 = set1.intersection(set2)
print(set3)


"""
Diferença
O difference() método retornará um novo conjunto que conterá apenas os itens do
primeiro conjunto que não estão presentes no outro conjunto.
"""
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)

# Você pode usar o -operador em vez do difference()método e obterá o mesmo result
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 - set2
print(set3)


"""
O difference_update()método também manterá os itens do primeiro conjunto que
não estão no outro conjunto, mas alterará o conjunto original em vez de 
retornar um novo conjunto.
"""
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1)


"""
Diferenças Simétricas
O symmetric_difference() método manterá apenas os elementos que NÃO estão 
presentes em ambos os conjuntos.
"""
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)

# Você pode usar o ^operador em vez do symmetric_difference()método e obterá o mesmo resultado
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 ^ set2
print(set3)


"""
O symmetric_difference_update()método também manterá tudo, exceto as
 duplicatas, mas alterará o conjunto original em vez de retornar um novo conjunto.
"""
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)