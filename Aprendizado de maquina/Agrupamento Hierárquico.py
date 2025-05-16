"""
Agrupamento hierárquico
O agrupamento hierárquico é um método de aprendizado não supervisionado para agrupar pontos de dados. 
O algoritmo cria agrupamentos medindo as dissimilaridades entre os dados. O aprendizado não supervisionado significa que um modelo não precisa ser treinado
 e não precisamos de uma variável "alvo". Este método pode ser usado em qualquer dado para visualizar e interpretar a relação entre pontos de dados individuais.

Aqui, usaremos o agrupamento hierárquico para agrupar pontos de dados e visualizar os agrupamentos usando um dendrograma e um gráfico de dispersão.

Como funciona?
Utilizaremos o Clustering Aglomerativo, um tipo de clustering hierárquico que segue uma abordagem de baixo para cima. Começamos tratando cada ponto de dados como seu próprio cluster. Em seguida, unimos os clusters que têm a menor distância entre si para criar clusters maiores. Essa etapa é repetida até que um grande cluster seja formado contendo todos os pontos de dados.

O agrupamento hierárquico exige que decidamos sobre um método de distância e um método de ligação. Usaremos a distância euclidiana e o método de ligação de Ward, que tenta minimizar a variância entre os agrupamentos.
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering

x = [4, 5, 10, 4, 3, 11, 14 , 6, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]

data = list(zip(x, y))

hierarchical_cluster = AgglomerativeClustering(n_clusters=2, affinity='euclidean', linkage='ward')
labels = hierarchical_cluster.fit_predict(data)

plt.scatter(x, y, c=labels)
plt.show()