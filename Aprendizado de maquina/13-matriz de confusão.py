"""
O que é uma matriz de confusão?
É uma tabela usada em problemas de classificação para avaliar onde foram cometidos erros no modelo.

As linhas representam as classes reais em que os resultados deveriam ter sido obtidos. 
Já as colunas representam as previsões que fizemos. 
Usando esta tabela, é fácil ver quais previsões estão erradas.
"""

import matplotlib.pyplot as plt
import numpy
from sklearn import metrics

actual = numpy.random.binomial(1,.9,size = 1000)
predicted = numpy.random.binomial(1,.9,size = 1000)

confusion_matrix = metrics.confusion_matrix(actual, predicted)

cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = [0, 1])

cm_display.plot()
plt.show()


"""
Resultados explicados
A Matriz de Confusão criada possui quatro quadrantes diferentes:

Verdadeiro negativo (quadrante superior esquerdo)
Falso positivo (quadrante superior direito)
Falso negativo (quadrante inferior esquerdo)
Verdadeiro positivo (quadrante inferior direito)

Verdadeiro significa que os valores foram previstos com precisão. Falso significa que houve um erro ou uma previsão errada.

Agora que criamos uma Matriz de Confusão, podemos calcular diferentes medidas para quantificar a qualidade do modelo. Primeiro, vamos analisar a Precisão.
"""