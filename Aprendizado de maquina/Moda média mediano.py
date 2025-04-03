"""
Média, mediana e moda
O que podemos aprender ao observar um grupo de números?

Em Aprendizado de Máquina (e em matemática) geralmente há três valores que nos interessam:

Média - O valor médio
Mediana - O valor do ponto médio
Modo - O valor mais comum
Exemplo: Registramos a velocidade de 13 carros:

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

Qual é o valor de velocidade médio, intermediário ou mais comum?

Significar
O valor médio é o valor médio.

Para calcular a média, encontre a soma de todos os valores e divida a soma pelo número de valores:

(99+86+87+88+111+86+103+87+94+78+77+85+86) / 13 = 89.77

O módulo NumPy tem um método para isso. Aprenda sobre o módulo NumPy em nosso Tutorial NumPy .
"""

"""média"""
# Use o mean() NumPy para encontrar a velocidade média:
import numpy
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = numpy.mean(speed)
print(x)



"""
Mediana
O valor mediano é o valor no meio, depois de você ter classificado todos os valores:
77, 78, 85, 86, 86, 86, 87, 87, 88, 94, 99, 103, 111
"""
# Use o median() NumPy para encontrar o valor médio:
import numpy
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = numpy.median(speed)
print(x)

# Usando o módulo NumPy:
import numpy
speed = [99,86,87,88,86,103,87,94,78,77,85,86]
x = numpy.median(speed)
print(x)



"""
Moda
O valor Moda é o valor que aparece mais vezes:
O módulo SciPy tem um método para isso. 
"""
from scipy import stats
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = stats.mode(speed)
print(x)