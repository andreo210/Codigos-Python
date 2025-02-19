"""
Criando gráficos de dispersão
Com o Pyplot, você pode usar a scatter()função para desenhar um gráfico de dispersão.
A scatter()função plota um ponto para cada observação. 
Ela precisa de dois arrays do mesmo comprimento, um para os valores do eixo x e um para os valores no eixo y:
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.scatter(x, y)
plt.show()

"""
A observação no exemplo acima é o resultado de 13 carros passando.
O eixo X mostra a idade do carro.
O eixo Y mostra a velocidade do carro quando ele passa.
Há alguma relação entre as observações?
Parece que quanto mais novo o carro, mais rápido ele anda, mas isso pode ser uma coincidência, afinal registramos apenas 13 carros.
"""






"""
Comparar gráficos
No exemplo acima, parece haver uma relação entre velocidade e idade, 
mas e se plotarmos as observações de outro dia também? O gráfico de dispersão nos dirá algo mais?
"""
import matplotlib.pyplot as plt
import numpy as np

#day one, the age and speed of 13 cars:
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y)

#day two, the age and speed of 15 cars:
x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y)

plt.show()




"""
Cores
Você pode definir sua própria cor para cada gráfico de dispersão com o argumento colorou c :
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y, color = 'hotpink')

x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y, color = '#88c999')

plt.show()




"""
Pinte cada ponto
Você pode até definir uma cor específica para cada ponto usando uma matriz de cores como valor para o cargumento:
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])

plt.scatter(x, y, c=colors)

plt.show()





""""
Como usar o ColorMap
Você pode especificar o mapa de cores com o argumento de palavra-chave cmapcom o valor do mapa de cores, neste caso, 
'viridis'um dos mapas de cores integrados disponíveis no Matplotlib.
Além disso, você deve criar uma matriz com valores (de 0 a 100), um valor para cada ponto no gráfico de dispersão:"""
import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

plt.scatter(x, y, c=colors, cmap='viridis')

plt.show()