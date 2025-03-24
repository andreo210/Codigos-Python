"""
Remodelando matrizes
Remodelar significa mudar a forma de uma matriz.
O formato de uma matriz é o número de elementos em cada dimensão.
Ao remodelar, podemos adicionar ou remover dimensões ou alterar o número de elementos em cada dimensão.
"""

"""Remodelar de 1-D para 2-D"""
# Converta a seguinte matriz 1-D com 12 elementos em uma matriz 2-D.
# A dimensão mais externa terá 4 matrizes, cada uma com 3 elementos:
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)


"""Remodelar de 1-D para 3-D"""
# Converta a seguinte matriz 1-D com 12 elementos em uma matriz 3-D.
# A dimensão mais externa terá 2 matrizes que contêm 3 matrizes, cada uma com 2 elementos:
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2, 3, 2)
print(newarr)


""""
Podemos nos remodelar em qualquer formato?
Sim, desde que os elementos necessários para remodelar sejam iguais em ambas as formas.
Podemos remodelar uma matriz 1D de 8 elementos em uma matriz 2D de 4 elementos em 2 linhas, 
mas não podemos remodelá-la em uma matriz 2D de 3 elementos e 3 linhas, pois isso exigiria 3x3 = 9 elementos.
"""


"""Retorna Copiar ou Exibir?"""
# Verifique se o array retornado é uma cópia ou uma visualização:
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr.reshape(2, 4).base)


"""
Dimensão Desconhecida
Você tem permissão para ter uma dimensão "desconhecida".
Isso significa que você não precisa especificar um número exato para uma das dimensões no método de remodelagem.
Passe -1 como valor e o NumPy calculará esse número para você.
"""
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 2, -1)
print(newarr)



"""
Achatando as matrizes
Achatar uma matriz significa converter uma matriz multidimensional em uma matriz 1D.
Podemos usar reshape(-1)para fazer isso.
"""
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(newarr)