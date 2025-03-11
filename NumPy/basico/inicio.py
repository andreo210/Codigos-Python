"""
Aprenda NumPy
NumPy é uma biblioteca Python.
O NumPy é usado para trabalhar com matrizes.
NumPy é a abreviação de "Numerical Python".
"""




"""
Por que usar o NumPy?
Em Python, temos listas que servem ao propósito de matrizes, mas são lentas para processar.

O NumPy tem como objetivo fornecer um objeto de matriz que seja até 50x mais rápido que as listas tradicionais do Python.

O objeto array no NumPy é chamado de ndarray, ele fornece muitas funções de suporte que tornam o trabalho ndarraymuito fácil.

Arrays são usados ​​com muita frequência em ciência de dados, onde velocidade e recursos são muito importantes.
"""


"""
Por que o NumPy é mais rápido que as listas?
As matrizes NumPy são armazenadas em um local contínuo na memória, diferentemente das listas, para que os processos possam acessá-las e manipulá-las de forma muito eficiente.

Esse comportamento é chamado de localidade de referência na ciência da computação.

Esta é a principal razão pela qual o NumPy é mais rápido que listas. Ele também é otimizado para trabalhar com as arquiteturas de CPU mais recentes.
"""


"""
Exemplo
Crie uma matriz NumPy:
"""
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))