"""
Um histograma é um gráfico que mostra distribuições de frequência.

É um gráfico que mostra o número de observações dentro de cada intervalo dado.

Exemplo: digamos que você pergunte a altura de 250 pessoas. Você pode acabar com um histograma como este:


Criar Histograma
No Matplotlib, usamos a função  hist() para criar histogramas.

A função hist() usará uma matriz de números para criar um histograma. A matriz é enviada para a função como um argumento.

Para simplificar, usamos o NumPy para gerar aleatoriamente uma matriz com 250 valores, onde os valores se concentrarão em torno de 170, e o desvio padrão é 10. Saiba mais sobre Distribuição Normal de Dados em nosso Tutorial de Aprendizado de Máquina .

A hist()função lerá o array e produzirá um histograma:
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(170, 10, 250)

plt.hist(x)
plt.show() 