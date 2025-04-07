"""
Gráfico de dispersão
Um gráfico de dispersão é um diagrama em que cada valor no conjunto de dados é representado por um ponto.
"""

"""
Distribuições de dados aleatórios
No aprendizado de máquina, os conjuntos de dados podem conter milhares ou até milhões de valores.

Talvez você não tenha dados do mundo real ao testar um algoritmo e talvez tenha que usar valores gerados aleatoriamente.
Como aprendemos no capítulo anterior, o módulo NumPy pode nos ajudar com isso!

Vamos criar duas matrizes preenchidas com 1000 números aleatórios de uma distribuição de dados normal.
A primeira matriz terá a média definida como 5,0 com um desvio padrão de 1,0.
A segunda matriz terá a média definida como 10,0 com um desvio padrão de 2,0:
"""
import numpy
import matplotlib.pyplot as plt

x = numpy.random.normal(5.0, 1.0, 1000)
y = numpy.random.normal(10.0, 2.0, 1000)

plt.scatter(x, y)
plt.show()

"""
Gráfico de dispersão explicado
Podemos ver que os pontos estão concentrados em torno do valor 5 no eixo x e 10 no eixo y.

Também podemos ver que a dispersão é maior no eixo y do que no eixo x.
"""