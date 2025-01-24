"""
Pyplot
A maioria dos utilitários do Matplotlib fica no pyplotsubmódulo e geralmente são importados sob o pltalias:
"""
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()