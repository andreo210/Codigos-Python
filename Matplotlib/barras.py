"""
Criando Barras
Com o Pyplot, você pode usar a função  bar() para desenhar gráficos de barras:
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y)
plt.show()




"""
A função bar() recebe argumentos que descrevem o layout das barras.
As categorias e seus valores representados pelo primeiro e segundo argumentos como matrizes.
"""
x = ["APPLES", "BANANAS"]
y = [400, 350]
plt.bar(x, y)




"""
Barras horizontais
Se você quiser que as barras sejam exibidas horizontalmente em vez de verticalmente, use a função: barh()
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.barh(x, y)
plt.show()



"""
Cor da barra
O bar()e barh() pegue o argumento da palavra-chave colorpara definir a cor das barras:
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, color = "red")
plt.show()



"""
Nomes de cores
Você pode usar qualquer um dos 140 nomes de cores suportados .
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, color = "hotpink")
plt.show()




"""
Cor Hex
Ou você pode usar valores de cores hexadecimais :
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, color = "#4CAF50")
plt.show()




"""
Largura da barra
O bar() argumento da palavra-chave é usado widthpara definir a largura das barras:
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, width = 0.1)
plt.show()