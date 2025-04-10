"""
Distribuição de dados
Anteriormente neste tutorial, trabalhamos com quantidades muito pequenas de dados em nossos exemplos, apenas para entender os diferentes conceitos.

No mundo real, os conjuntos de dados são muito maiores, mas pode ser difícil coletar dados do mundo real, pelo menos em um estágio inicial de um projeto.

Como podemos obter grandes conjuntos de dados?
Para criar grandes conjuntos de dados para testes, usamos o módulo Python NumPy, que vem com vários métodos para criar conjuntos de dados aleatórios, de qualquer tamanho.
"""
# Crie uma matriz contendo 250 floats aleatórios entre 0 e 5:
import numpy
x = numpy.random.uniform(0.0, 5.0, 250)
print(x)





"""
Histograma
Para visualizar o conjunto de dados, podemos desenhar um histograma com os dados coletados.
Usaremos o módulo Python Matplotlib para desenhar um histograma.
Saiba mais sobre o módulo Matplotlib em nosso Tutorial Matplotlib .
"""
# Desenhe um histograma:
import numpy
import matplotlib.pyplot as plt
x = numpy.random.uniform(0.0, 5.0, 250)
plt.hist(x, 5)
plt.show()
"""
Histograma Explicado
Usamos a matriz do exemplo acima para desenhar um histograma com 5 barras.
A primeira barra representa quantos valores na matriz estão entre 0 e 1.
A segunda barra representa quantos valores estão entre 1 e 2.
Etc.

O que nos dá este resultado:

52 valores estão entre 0 e 1
48 valores estão entre 1 e 2
49 valores estão entre 2 e 3
51 valores estão entre 3 e 4
50 valores estão entre 4 e 5
Observação: os valores da matriz são números aleatórios e não mostrarão exatamente o mesmo resultado no seu computador.
"""





"""
Distribuições de Big Data
Uma matriz contendo 250 valores não é considerada muito grande, mas agora você sabe como criar um conjunto aleatório de valores e, 
alterando os parâmetros, pode criar um conjunto de dados tão grande quanto desejar.
"""
# Crie uma matriz com 100.000 números aleatórios e exiba-os usando um histograma com 100 barras:
import numpy
import matplotlib.pyplot as plt
x = numpy.random.uniform(0.0, 5.0, 100000)
plt.hist(x, 100)
plt.show()