"""
Dividindo matrizes NumPy
Dividir é a operação inversa de unir.
A junção mescla vários arrays em um e a divisão quebra um array em vários.
Usamos array_split()para dividir arrays, passamos o array que queremos dividir e o número de divisões.
Se o array tiver menos elementos do que o necessário, ele será ajustado a partir do final conforme necessário.
"""
# Divida a matriz em 3 partes:
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr)

# Divida a matriz em 4 partes:
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 4)
print(newarr)



"""
Dividir em matrizes
O valor de retorno do array_split() é uma matriz contendo cada uma das divisões como uma matriz.
Se você dividir um array em 3 arrays, poderá acessá-los a partir do resultado como qualquer elemento do array:
"""
# Acesse os arrays divididos:
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr[0])
print(newarr[1])
print(newarr[2])



"""
Dividindo matrizes 2-D
Use a mesma sintaxe ao dividir matrizes 2-D.
Use o array_split(), passe o array que você quer dividir e o número de divisões que você quer fazer.
"""
import numpy as np
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 3)
print(newarr)


# Divida a matriz 2-D em três matrizes 2-D.
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3)
print(newarr)

# O exemplo acima retorna três matrizes 2-D.
# Além disso, você pode especificar em torno de qual eixo deseja fazer a divisão.
# O exemplo abaixo também retorna três matrizes 2-D, mas elas são divididas ao longo da linha (eixo=1).


# Divida a matriz 2-D em três matrizes 2-D ao longo das linhas.
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3, axis=1)
print(newarr)

# Use o hsplit()método para dividir a matriz 2-D em três matrizes 2-D ao longo das linhas.
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.hsplit(arr, 3)
print(newarr)