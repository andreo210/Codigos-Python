"""
Iterando Arrays
Iterar significa percorrer os elementos um por um.
Como lidamos com matrizes multidimensionais no numpy, podemos fazer isso usando foro loop básico do python.
Se iterarmos em uma matriz 1-D, ela percorrerá cada elemento um por um.
"""
# Itere nos elementos da seguinte matriz 1-D:
import numpy as np
arr = np.array([1, 2, 3])
for x in arr:
  print(x)

"Iterando matrizes 2-D"
# Em uma matriz 2-D, ele percorrerá todas as linhas.
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
  print(x)

# Para retornar os valores reais, os escalares, temos que iterar as matrizes em cada dimensão.
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
  for y in x:
    print(y)

"Iterando matrizes 3-D"
# Itere nos elementos da seguinte matriz 3-D:
import numpy as np
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr:
  print(x)

# Iterar até os escalares:
import numpy as np
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  for y in x:
    for z in y:
      print(z)


"""
Iterando Array com Diferentes Tipos de Dados
Podemos usar op_dtypeso argumento e passar o tipo de dados esperado para alterar o tipo de dados dos elementos durante a iteração.

O NumPy não altera o tipo de dados do elemento no local (onde o elemento está na matriz), 
então ele precisa de algum outro espaço para executar essa ação. Esse espaço extra é chamado de buffer e, 
para habilitá-lo, nditer()passamos flags=['buffered'].
"""
import numpy as np
arr = np.array([1, 2, 3])

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x)





"""
Iterando com diferentes tamanhos de passo
Podemos usar filtragem e, em seguida, iteração.
"""
# Itere por cada elemento escalar da matriz 2D pulando 1 elemento:
import numpy as np
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np.nditer(arr[:, ::2]):
  print(x)





"""
Iteração enumerada usando ndenumerate()
Enumeração significa mencionar a sequência numérica de algumas coisas, uma por uma.
Às vezes, precisamos do índice correspondente do elemento durante a iteração; o ndenumerate()método pode ser usado para esses casos de uso.
"""
# Enumere os seguintes elementos de matrizes 1D:
import numpy as np
arr = np.array([1, 2, 3])
for idx, x in np.ndenumerate(arr):
  print(idx, x)

# Enumere os seguintes elementos da matriz 2D:
import numpy as np
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for idx, x in np.ndenumerate(arr):
  print(idx, x)