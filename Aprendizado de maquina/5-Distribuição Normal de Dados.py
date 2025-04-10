"""
Distribuição Normal de Dados
No capítulo anterior, aprendemos como criar uma matriz completamente aleatória, de um determinado tamanho e entre dois valores fornecidos.
Neste capítulo, aprenderemos como criar uma matriz onde os valores são concentrados em torno de um determinado valor.
Na teoria da probabilidade, esse tipo de distribuição de dados é conhecido como distribuição normal de dados ou distribuição gaussiana de dados ,
em homenagem ao matemático Carl Friedrich Gauss, que criou a fórmula dessa distribuição de dados.
"""
# Uma distribuição de dados normal típica:
import numpy
import matplotlib.pyplot as plt

x = numpy.random.normal(5.0, 1.0, 100000)

plt.hist(x, 100)
plt.show()
"""
Observação: um gráfico de distribuição normal também é conhecido como curva de sino devido ao seu formato característico de sino.

Histograma Explicado
Usamos a matriz do numpy.random.normal() método, com 100.000 valores, para desenhar um histograma com 100 barras.
Especificamos que o valor médio é 5,0 e o desvio padrão é 1,0.
Isso significa que os valores devem se concentrar em torno de 5,0 e raramente mais distantes do que 1,0 da média.
E como você pode ver no histograma, a maioria dos valores está entre 4,0 e 6,0, com um máximo em aproximadamente 5,0.
"""