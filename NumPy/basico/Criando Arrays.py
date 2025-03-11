"""
Crie um objeto NumPy ndarray
NumPy é usado para trabalhar com arrays. O objeto array em NumPy é chamado ndarray.
Podemos criar um ndarrayobjeto NumPy usando a array()função.
"""
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)

print(type(arr))



"""
Matrizes 0-D
Matrizes 0-D, ou Scalars, são os elementos em uma matriz. Cada valor em uma matriz é uma matriz 0-D.
"""
import numpy as np

arr = np.array(42)

print(arr)




"""
Matrizes 1-D
Uma matriz que tem matrizes 0-D como seus elementos é chamada de matriz unidimensional ou 1-D.
Essas são as matrizes mais comuns e básicas.
"""
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)



"""
Matrizes 2-D
Uma matriz que tem matrizes 1-D como elementos é chamada de matriz 2-D.
Eles são frequentemente usados ​​para representar matrizes ou tensores de segunda ordem.
"""
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr)



"""
Matrizes 3-D
Uma matriz que tem matrizes 2-D como seus elementos é chamada de matriz 3-D.
Eles são frequentemente usados ​​para representar um tensor de 3ª ordem.
"""
import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(arr)



"""
Verificar número de dimensões?
O NumPy Arrays fornece o ndimatributo que retorna um inteiro que nos diz quantas dimensões o array tem.
"""
import numpy as np

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)




"""
Matrizes de Dimensão Superior
Uma matriz pode ter qualquer número de dimensões.
Quando a matriz é criada, você pode definir o número de dimensões usando o ndminargumento.
"""
import numpy as np

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)