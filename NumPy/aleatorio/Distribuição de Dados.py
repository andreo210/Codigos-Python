"""
O que é Distribuição de Dados?
Distribuição de dados é uma lista de todos os valores possíveis e a frequência com que cada valor ocorre.
Essas listas são importantes ao trabalhar com estatística e ciência de dados.
O módulo aleatório oferece métodos que retornam distribuições de dados geradas aleatoriamente.

Distribuição aleatória
Uma distribuição aleatória é um conjunto de números aleatórios que seguem uma certa função de densidade de probabilidade .

Função de densidade de probabilidade: uma função que descreve uma probabilidade contínua, ou seja, probabilidade de todos os valores em uma matriz.
Podemos gerar números aleatórios com base em probabilidades definidas usando o método choice() do módulo random

O choice() nos permite especificar a probabilidade para cada valor.

A probabilidade é definida por um número entre 0 e 1, onde 0 significa que o valor nunca ocorrerá e 1 significa que o valor sempre ocorrerá.

"""




"""
Gere uma matriz 1-D contendo 100 valores, onde cada valor deve ser 3, 5, 7 ou 9.
A probabilidade do valor ser 3 é definida como 0,1
A probabilidade do valor ser 5 é definida como 0,3
A probabilidade do valor ser 7 é definida como 0,6
A probabilidade do valor ser 9 é definida como 0
"""
from numpy import random
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))
print(x)
"""
A soma de todos os números de probabilidade deve ser 1.
Mesmo se você executar o exemplo acima 100 vezes, o valor 9 nunca ocorrerá.
Você pode retornar matrizes de qualquer formato e tamanho especificando o formato no sizeparâmetro.
"""

# Mesmo exemplo acima, mas retorna uma matriz 2-D com 3 linhas, cada uma contendo 5 valores
from numpy import random
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))
print(x)

