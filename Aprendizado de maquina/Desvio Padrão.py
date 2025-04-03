"""
O que é desvio padrão?
Desvio padrão é um número que descreve o quão dispersos os valores estão.
Um desvio padrão baixo significa que a maioria dos números está próxima do valor médio.
Um desvio padrão alto significa que os valores estão espalhados por uma faixa mais ampla.
Exemplo: Desta vez registramos a velocidade de 7 carros:

speed = [86,87,88,86,87,85,86]

O desvio padrão é:

0.9

Isso significa que a maioria dos valores está dentro da faixa de 0,9 do valor médio, que é 86,4.
"""

# Use o método NumPy std() para encontrar o desvio padrão:
import numpy
speed = [86,87,88,86,87,85,86]
x = numpy.std(speed)
print(x)

import numpy
speed = [32,111,138,28,59,77,97]
x = numpy.std(speed)
print(x)



"""
Variância
A variância é outro número que indica o quão dispersos os valores estão.
Na verdade, se você tirar a raiz quadrada da variância, você obtém o desvio padrão!
Ou o contrário, se você multiplicar o desvio padrão por ele mesmo, você obtém a variância!
Para calcular a variância você deve fazer o seguinte:

1. Encontre a média:
(32+111+138+28+59+77+97) / 7 = 77.4

2. Para cada valor: encontre a diferença da média:

 32 - 77.4 = -45.4
111 - 77.4 =  33.6
138 - 77.4 =  60.6
 28 - 77.4 = -49.4
 59 - 77.4 = -18.4
 77 - 77.4 = - 0.4
 97 - 77.4 =  19.6

3. Para cada diferença: encontre o valor quadrado:

(-45.4)2 = 2061.16
 (33.6)2 = 1128.96
 (60.6)2 = 3672.36
(-49.4)2 = 2440.36
(-18.4)2 =  338.56
(- 0.4)2 =    0.16
 (19.6)2 =  384.16

4. A variância é o número médio dessas diferenças quadradas:

(2061.16+1128.96+3672.36+2440.36+338.56+0.16+384.16) / 7 = 1432.2
"""

# Use o método NumPy var()para encontrar a variância:
import numpy
speed = [32,111,138,28,59,77,97]
x = numpy.var(speed)
print(x)