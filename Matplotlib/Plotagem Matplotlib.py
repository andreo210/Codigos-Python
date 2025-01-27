"""
Traçando os pontos x e y
A plot() função é usada para desenhar pontos (marcadores) em um diagrama.
Por padrão, a plot()função desenha uma linha de ponto a ponto.
A função usa parâmetros para especificar pontos no diagrama.
O parâmetro 1 é uma matriz contendo os pontos no eixo x .
O parâmetro 2 é uma matriz contendo os pontos no eixo y .
Se precisarmos traçar uma linha de (1, 3) a (8, 10), temos que passar dois arrays [1, 8] e [3, 10] para a função plot.
"""
# Desenhe uma linha em um diagrama da posição (1, 3) para a posição (8, 10):
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints)
plt.show()



""""
Plotagem sem linha
Para plotar apenas os marcadores, você pode usar o parâmetro de notação de string de atalho 'o', que significa 'anéis'.
"""
xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints, 'o')
plt.show()




"""
Vários pontos
Você pode traçar quantos pontos quiser, apenas certifique-se de ter o mesmo número de pontos em ambos os eixos.
"""
xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.plot(xpoints, ypoints)
plt.show()




"""
Pontos X padrão
Se não especificarmos os pontos no eixo x, eles receberão os valores padrão 0, 1, 2, 3 etc., dependendo do comprimento dos pontos y.
Então, se pegarmos o mesmo exemplo acima e deixarmos de fora os pontos x, o diagrama ficará assim:
"""
ypoints = np.array([3, 8, 1, 10, 5, 7])

plt.plot(ypoints)
plt.show()