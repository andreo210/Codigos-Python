"""
Estilo de linha
Você pode usar a palavra-chave argument linestyle, ou mais curta ls, para alterar o estilo da linha plotada:
"""
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linestyle = 'dotted')
plt.show()

# Use uma linha tracejada:
plt.plot(ypoints, linestyle = 'dashed')
plt.show()


"""
Sintaxe mais curta
O estilo de linha pode ser escrito em uma sintaxe mais curta:

linestyle pode ser escrito como ls.

dotted pode ser escrito como :.

dashed pode ser escrito como --.

solid'   	'-'	
dotted  	':'	
dashed  	'--'	
dashdot 	'-.'	
None    	or ' '
"""



"""
Cor da linha
Você pode usar o argumento de palavra-chave color ou o mais curto c para definir a cor da linha:
"""
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, color = 'r')
plt.show()

# Plot com uma linda linha verde: usando hexadecimal
plt.plot(ypoints, c = '#4CAF50')
plt.show()




"""
Largura da linha
Você pode usar o argumento de palavra-chave linewidth ou o shorter lw para alterar a largura da linha.

O valor é um número flutuante, em pontos:
"""
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linewidth = '20.5')
plt.show()



"""
Várias linhas
Você pode traçar quantas linhas quiser simplesmente adicionando mais plt.plot() funções:
"""
y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.plot(y1)
plt.plot(y2)

plt.show()


"""
Você também pode traçar muitas linhas adicionando os pontos dos eixos x e y para cada linha na mesma plt.plot().
(Nos exemplos acima, especificamos apenas os pontos no eixo y, o que significa que os pontos no eixo x obtiveram os valores padrão (0, 1, 2, 3).)
Os valores x e y vêm em pares:
"""
x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.plot(x1, y1, x2, y2)
plt.show()