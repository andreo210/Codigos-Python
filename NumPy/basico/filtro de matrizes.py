"""
Filtrando matrizes
Obter alguns elementos de uma matriz existente e criar uma nova matriz a partir deles é chamado de filtragem .
No NumPy, você filtra uma matriz usando uma lista de índices booleanos .
Uma lista de índices booleanos é uma lista de booleanos correspondentes aos índices na matriz.
Se o valor em um índice for Trueesse elemento, ele estará contido na matriz filtrada; se o valor nesse índice for Falseesse elemento, ele será excluído da matriz filtrada.
"""
# Crie uma matriz a partir dos elementos nos índices 0 e 2:
import numpy as np
arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr[x]
print(newarr)

"""
O exemplo acima retornará [41, 43], por quê?
Porque a nova matriz contém apenas os valores onde a matriz de filtros tinha o valor True, neste caso, índice 0 e 2.
"""





"""
Criando o Array de Filtros
No exemplo acima, codificamos os valores True e False, mas o uso comum é criar uma matriz de filtros com base em condições.
"""
# Crie uma matriz de filtros que retornará apenas valores maiores que 42:
import numpy as np

arr = np.array([41, 42, 43, 44])

# Create uma lista vazia
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is higher than 42, set the value to True, otherwise False:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)




# Crie uma matriz de filtros que retornará apenas elementos pares da matriz original:
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is completely divisble by 2, set the value to True, otherwise False
  if element % 2 == 0:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)



"""
Criando filtro diretamente do array
O exemplo acima é uma tarefa bastante comum no NumPy e o NumPy fornece uma boa maneira de lidar com isso.
Podemos substituir diretamente o array em vez da variável iterável em nossa condição e funcionará exatamente como esperamos.
"""
# Crie uma matriz de filtros que retornará apenas valores maiores que 42:
import numpy as np
arr = np.array([41, 42, 43, 44])
filter_arr = arr > 42
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)


# Crie uma matriz de filtros que retornará apenas elementos pares da matriz original:
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
filter_arr = arr % 2 == 0
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)