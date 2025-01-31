"""
Adicionar linhas de grade a um gráfico
Com o Pyplot, você pode usar a grid() para adicionar linhas de grade ao gráfico.
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)

plt.grid()

plt.show()




"""
Especificar quais linhas de grade exibir
Você pode usar o axis parâmetro na grid() para especificar quais linhas de grade exibir.
Os valores legais são: 'x', 'y' e 'both'. O valor padrão é 'both'
"""
plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)

plt.grid(axis = 'x')

plt.show()



"""
Definir propriedades de linha para a grade
Você também pode definir as propriedades de linha da grade, assim: grid(color = ' color ', linestyle = ' linestyle ', linewidth = number )
"""
plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)

plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)

plt.show()