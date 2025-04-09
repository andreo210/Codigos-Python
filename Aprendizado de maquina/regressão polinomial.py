"""
Regressão Polinomial
Se seus pontos de dados claramente não se encaixam em uma regressão linear (uma linha reta passando por todos os pontos de dados), 
pode ser ideal para uma regressão polinomial.

A regressão polinomial, assim como a regressão linear, usa a relação entre as variáveis ​​x e y 
para encontrar a melhor maneira de traçar uma linha através dos pontos de dados.


Como funciona?
Python tem métodos para encontrar uma relação entre pontos de dados e para desenhar uma linha de regressão polinomial. 
Mostraremos como usar esses métodos em vez de passar pela fórmula matemática.
No exemplo abaixo, registramos 18 carros que estavam passando por um determinado pedágio.
Registramos a velocidade do carro e a hora do dia (hora) em que a ultrapassagem ocorreu.
O eixo x representa as horas do dia e o eixo y representa a velocidade:
"""
# Importe numpy e matplotlib desenhe a linha de Regressão Polinomial:
import numpy
import matplotlib.pyplot as plt

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))#O NumPy tem um método que nos permite criar um modelo polinomial:

myline = numpy.linspace(1, 22, 100)#Em seguida, especifique como a linha será exibida, começamos na posição 1 e terminamos na posição 22

plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()









"""
R-Quadrado
É importante saber quão boa é a relação entre os valores dos eixos x e y. Se não houver relação, a regressão polinomial não poderá ser usada para prever nada.

O relacionamento é medido com um valor chamado r-quadrado.

O valor de r-quadrado varia de 0 a 1, onde 0 significa nenhuma relação e 1 significa 100% relacionado.

O Python e o módulo Sklearn calcularão esse valor para você, tudo o que você precisa fazer é alimentá-lo com as matrizes x e y:
"""
# Quão bem meus dados se ajustam em uma regressão polinomial?
import numpy
from sklearn.metrics import r2_score

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

print(r2_score(y, mymodel(x)))
# O resultado 0,94 mostra que há uma relação muito boa e podemos usar regressão polinomial em previsões futuras.





"""
Prever valores futuros
Agora podemos usar as informações que coletamos para prever valores futuros.
Exemplo: Vamos tentar prever a velocidade de um carro que passa pelo pedágio por volta das 17:00:
Para fazer isso, precisamos do mesmo mymodelarray do exemplo acima:

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))
"""
# Preveja a velocidade de um carro passando às 17:00:
import numpy
from sklearn.metrics import r2_score

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

speed = mymodel(17)
print(speed)
# O exemplo previu uma velocidade de 88,87, o que também podemos ler no diagrama:








"""
Ajuste ruim?
Vamos criar um exemplo em que a regressão polinomial não seria o melhor método para prever valores futuros.
"""
# Esses valores para os eixos x e y devem resultar em um ajuste muito ruim para regressão polinomial:
import numpy
import matplotlib.pyplot as plt

x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

myline = numpy.linspace(2, 95, 100)

plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()


"""E o valor de r-quadrado?"""
# Você deve obter um valor de r-quadrado muito baixo.
import numpy
from sklearn.metrics import r2_score

x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

print(r2_score(y, mymodel(x)))
#O resultado: 0,00995 indica uma relação muito ruim e nos diz que esse conjunto de dados não é adequado para regressão polinomial.