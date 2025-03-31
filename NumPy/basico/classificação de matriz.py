"""
Classificando matrizes
Classificar significa colocar elementos em uma sequência ordenada .
Sequência ordenada é qualquer sequência que tem uma ordem correspondente aos elementos, como numérica ou alfabética, crescente ou decrescente.
O objeto NumPy ndarray tem uma função chamada sort(), que classificará uma matriz especificada.
"""
# Classifique a matriz:
import numpy as np
arr = np.array([3, 2, 0, 1])
print(np.sort(arr))


"""
Observação: esse método retorna uma cópia do array, deixando o array original inalterado.
Você também pode classificar matrizes de strings ou qualquer outro tipo de dado:
"""
# Classifique a matriz em ordem alfabética:
import numpy as np
arr = np.array(['banana', 'cherry', 'apple'])
print(np.sort(arr))


# Classificar uma matriz booleana:
import numpy as np
arr = np.array([True, False, True])
print(np.sort(arr))


"""
Classificando uma matriz 2-D
Se você usar o método sort() em um array 2-D, ambos os arrays serão classificados:
"""
# Classificar uma matriz 2-D:
import numpy as np
arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr))