"""
Juntando matrizes NumPy
Unir significa colocar o conteúdo de duas ou mais matrizes em uma única matriz.
Em SQL, unimos tabelas com base em uma chave, enquanto em NumPy unimos matrizes por eixos.

Passamos uma sequência de arrays que queremos unir à função concatenate(), junto com o axis.
Se axis não for explicitamente passado, ele é tomado como 0.
"""

# Junte duas matrizes
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)

# Junte duas matrizes 2-D ao longo de linhas (eixo=1):
import numpy as np
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)
print(arr)



"""
Juntando matrizes usando funções de pilha
Empilhamento é o mesmo que concatenação, a única diferença é que o empilhamento é feito ao longo de um novo eixo.
Podemos concatenar duas matrizes 1-D ao longo do segundo eixo, o que resultaria em colocá-las uma sobre a outra, ou seja, empilhando-as.
Passamos uma sequência de arrays que queremos unir ao método stack() junto com o axis. Se axis não for explicitamente passado, ele é tomado como 0.
"""
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2), axis=1)
print(arr)



"""
Empilhamento ao longo das linhas
O NumPy fornece uma função auxiliar: hstack() empilhar ao longo das linhas.
"""
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.hstack((arr1, arr2))
print(arr)



"""
Empilhamento ao longo de colunas
O NumPy fornece uma função auxiliar: vstack()  empilhar ao longo de colunas.
"""
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.vstack((arr1, arr2))
print(arr)



"""
Empilhamento ao longo da altura (profundidade)
O NumPy fornece uma função auxiliar: dstack() empilhar ao longo da altura, que é o mesmo que a profundidade.
"""
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.dstack((arr1, arr2))
print(arr)