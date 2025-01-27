"""
Verificando a versão do Matplotlib
A string da versão é armazenada no __version__  atributo.
"""
import matplotlib
print(matplotlib.__version__)







"""
Pyplot
A maioria dos utilitários do Matplotlib fica no pyplot e geralmente são importados sob o plt alias:
"""
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()

