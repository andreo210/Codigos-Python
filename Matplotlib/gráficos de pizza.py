"""
Criando gráficos de pizza
Com o Pyplot, você pode usar a função pie() para desenhar gráficos de pizza:
"""
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])

plt.pie(y)
plt.show() 




"""
Etiquetas
Adicione rótulos ao gráfico de pizza com o labelsparâmetro.
O labels parâmetro deve ser uma matriz com um rótulo para cada fatia:
"""
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.show() 




"""
Ângulo inicial
Conforme mencionado, o ângulo inicial padrão é no eixo x, mas você pode alterá-lo especificando um startangle parâmetro.
O startangle parâmetro é definido com um ângulo em graus, o ângulo padrão é 0:
"""
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels, startangle = 90)
plt.show() 




"""
Explodir
Talvez você queira que uma das cunhas se destaque? O explode parâmetro permite que você faça isso.
O explode parâmetro, se especificado, e não None, deve ser uma matriz com um valor para cada fatia.
Cada valor representa a distância do centro em que cada cunha é exibida:
"""
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode)
plt.show()




"""
Sombra
Adicione uma sombra ao gráfico de pizza definindo o shadows parâmetro como True:
"""
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)
plt.show()



"""
Cores
Você pode definir a cor de cada fatia com o colorsparâmetro.
O colors parâmetro, se especificado, deve ser uma matriz com um valor para cada fatia:
"""
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
mycolors = ["black", "hotpink", "b", "#4CAF50"]

plt.pie(y, labels = mylabels, colors = mycolors)
plt.show() 



"""
Lengenda
Para adicionar uma lista de explicações para cada cunha, use a legend() função:
"""
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.legend()
plt.show() 





"""
Legenda com Cabeçalho
Para adicionar um cabeçalho à legenda, adicione o title parâmetro à legend função.
"""
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.legend(title = "Four Fruits:")
plt.show() 