"""
Acessar Elementos de Matriz
A indexação de array é o mesmo que acessar um elemento de array.

Você pode acessar um elemento de uma matriz consultando seu número de índice.

Os índices em matrizes NumPy começam com 0, o que significa que o primeiro elemento tem índice 0, o segundo tem índice 1, etc.
"""
import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[0])




"""
Obtenha o segundo elemento da seguinte matriz.
"""
import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[1])




"""Obtenha o terceiro e o quarto elementos da seguinte matriz e adicione-os"""
import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[2] + arr[3])



"""
Acessar matrizes 2-D
Para acessar elementos de matrizes 2-D, podemos usar inteiros separados por vírgulas representando a dimensão e o índice do elemento.

Pense em matrizes 2D como uma tabela com linhas e colunas, onde a dimensão representa a linha e o índice representa a coluna.
"""
import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st row: ', arr[0, 1])



"""Acesse o elemento na 2ª linha, 5ª coluna:"""
import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('5th element on 2nd row: ', arr[1, 4])


"""
Acessar matrizes 3-D
Para acessar elementos de matrizes 3D, podemos usar inteiros separados por vírgulas representando as dimensões e o índice do elemento.
"""
import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr)
print(arr[0, 1, 2])




"""
Indexação Negativa
Use indexação negativa para acessar uma matriz a partir do final.
"""
import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('Last element from 2nd dim: ', arr[1, -1])