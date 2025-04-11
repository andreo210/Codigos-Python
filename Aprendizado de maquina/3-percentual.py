"""
O que são percentual?
Os percentis são usados ​​em estatística para fornecer um número que descreve o valor que uma determinada porcentagem dos valores é menor.
Exemplo: Digamos que temos uma matriz que contém as idades de todas as pessoas que vivem em uma rua.

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

Qual é o 75º percentil? A resposta é 43, o que significa que 75% das pessoas têm 43 anos ou menos.

O módulo NumPy tem um método para encontrar o percentil especificado:
"""

# Use o método NumPy percentile() para encontrar os percentis:
import numpy
ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
x = numpy.percentile(ages, 75)
print(x)


# Qual é a idade em que 90% das pessoas têm menos?
import numpy
ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
x = numpy.percentile(ages, 90)
print(x)