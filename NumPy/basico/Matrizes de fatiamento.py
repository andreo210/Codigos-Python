"""
Matrizes de fatiamento
Fatiar em Python significa pegar elementos de um índice dado para outro índice dado.
Passamos slice em vez de index assim: .[start:end]
Também podemos definir o passo assim: .[start:end:step]
Se não passarmos start é considerado 0
Se não passarmos o fim, é considerado o comprimento do array nessa dimensão
Se não passarmos da etapa é considerado 1
"""
# Fatie os elementos do índice 1 ao índice 5 da seguinte matriz:
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])


# Fatie os elementos do índice 4 até o final do array:
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[4:])



# Fatie elementos do início ao índice 4 (não incluído):
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[:4])



"""
Fatiamento Negativo
Use o operador menos para se referir a um índice do final:
"""
# Corte do índice 3 do final para o índice 1 do final:
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[-3:-1])


"""
ETAPA
Use o stepvalor para determinar a etapa do fatiamento:
"""
# Retorna todos os outros elementos do índice 1 ao índice 5:
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5:2])

# Retorna todos os outros elementos do array inteiro:
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[::2])


"""Fatiando matrizes 2-D"""
# A partir do segundo elemento, corte os elementos do índice 1 ao índice 4 (não incluídos):
import numpy as np
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4])

# De ambos os elementos, retorne o índice 2:
import numpy as np
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 2])

# De ambos os elementos, divida o índice 1 ao índice 4 (não incluído), o que retornará uma matriz 2-D:
import numpy as np
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 1:4])
