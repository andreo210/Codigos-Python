"""
Forma de uma matriz
O formato de uma matriz é o número de elementos em cada dimensão.

Obtenha a forma de uma matriz
Os arrays NumPy têm um atributo chamado shape que retorna uma tupla com cada índice contendo o número de elementos correspondentes.
"""
# Imprima o formato de uma matriz 2-D:
import numpy as np
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)

# Crie uma matriz com 5 dimensões usando ndminum vetor com valores 1,2,3,4 e verifique se a última dimensão tem valor 4:
import numpy as np

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('shape of array :', arr.shape)