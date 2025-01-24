"""
Dicionário
Dicionários são usados ​​para armazenar valores de dados em pares chave:valor.
Um dicionário é uma coleção ordenada*, mutável e que não permite duplicatas.
A partir da versão 3.7 do Python, os dicionários são ordenados
No Python 3.6 e anteriores, os dicionários são desordenados .
Os dicionários são escritos com chaves e têm chaves e valore
"""
# Exemplo
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)





"""
Itens do dicionário
Os itens do dicionário são ordenados, alteráveis ​​e não permitem duplicatas.
Os itens do dicionário são apresentados em pares chave:valor
e podem ser referenciados usando o nome da chave.
"""
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])





"""
Ordenado ou não ordenado?
A partir da versão 3.7 do Python, os dicionários são ordenados . No Python 3.6 e anteriores, os dicionários são desordenados .
Quando dizemos que os dicionários são ordenados, isso significa que os itens têm uma ordem definida e essa ordem não mudará.
Não ordenado significa que os itens não têm uma ordem definida; você não pode se referir a um item usando um índice.
"""


"""
Duplicatas não permitidas
Os dicionários não podem ter dois itens com a mesma chave:
"""
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}
print(thisdict)



"""
Comprimento do dicionário
Para determinar quantos itens um dicionário possui, use a len() função:
"""
print(len(thisdict))



"""
Itens do dicionário - Tipos de dados
Os valores nos itens do dicionário podem ser de qualquer tipo de dados:
"""
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}



"""
tipo()
Da perspectiva do Python, os dicionários são definidos como objetos com o tipo de dados 'dict':
"""
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))



"""
O construtor dict()
Também é possível usar o construtor dict() para criar um dicionário.
"""
thisdict = dict(name="John", age=36, country="Norway")
print(thisdict)