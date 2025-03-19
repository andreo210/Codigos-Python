"""
A diferença entre copiar e visualizar
A principal diferença entre uma cópia e uma visualização de um array é que a cópia é um novo array,
 e a visualização é apenas uma visualização do array original.

A cópia possui os dados e quaisquer alterações feitas na cópia não afetarão o array original, 
e quaisquer alterações feitas no array original não afetarão a cópia.

A exibição não possui os dados e quaisquer alterações feitas na exibição afetarão o array original,
e quaisquer alterações feitas no array original afetarão a exibição.
"""
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)


"""VISUALIZAR:"""
# Crie uma visualização, altere o array original e exiba ambos os arrays:
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr)
print(x)

# Faça alterações na VIEW:
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
x[0] = 31

print(arr)
print(x)



"""
Verifique se o Array possui seus dados
Como mencionado acima, as cópias são donas dos dados, e as visualizações não são donas dos dados, mas como podemos verificar isso?

Cada matriz NumPy tem o atributo baseque retorna Nonese a matriz possui os dados.

Caso contrário, o base  atributo se refere ao objeto original.
"""
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)