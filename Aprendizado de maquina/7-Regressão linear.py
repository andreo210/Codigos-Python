"""
Regressão
O termo regressão é usado quando você tenta encontrar a relação entre variáveis.

No aprendizado de máquina e na modelagem estatística, esse relacionamento é usado para prever o resultado de eventos futuros.

Regressão Linear
A regressão linear usa a relação entre os pontos de dados para traçar uma linha reta através de todos eles.

Esta linha pode ser usada para prever valores futuros.

Como funciona?
Python tem métodos para encontrar uma relação entre pontos de dados e para desenhar uma linha de regressão linear.
Mostraremos como usar esses métodos em vez de passar pela fórmula matemática.
No exemplo abaixo, o eixo x representa a idade, e o eixo y representa a velocidade. Registramos a idade e a velocidade de 13 carros enquanto eles passavam por um pedágio. Vamos ver se os dados que coletamos podem ser usados ​​em uma regressão linear:
"""

# Comece desenhando um gráfico de dispersão:
import matplotlib.pyplot as plt

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

plt.scatter(x, y)
plt.show()


# Importe scipy e desenhe a linha de Regressão Linear:
import matplotlib.pyplot as plt
from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()




"""
R para Relacionamento
É importante saber qual é a relação entre os valores do eixo x e os valores do eixo y. Se não houver relação,
a regressão linear não poderá ser usada para prever nada.

Essa relação - o coeficiente de correlação - é chamada r.
O r valor varia de -1 a 1, onde 0 significa nenhuma relação e 1 (e -1) significa 100% relacionado.
O Python e o módulo Scipy calcularão esse valor para você, tudo o que você precisa fazer é alimentá-lo com os valores x e y.
"""
# Quão bem meus dados se ajustam em uma regressão linear?
from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

print(r)


"""
Prever valores futuros
Agora podemos usar as informações que coletamos para prever valores futuros.
Exemplo: Vamos tentar prever a velocidade de um carro de 10 anos.
Para fazer isso, precisamos da mesma myfunc() função do exemplo acima:
"""
# Preveja a velocidade de um carro de 10 anos:
from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

speed = myfunc(10)

print(speed)
"""O exemplo previu uma velocidade de 85,6, que também podemos ler no diagrama:"""




"""
Ajuste ruim?
Vamos criar um exemplo em que a regressão linear não seria o melhor método para prever valores futuros.
"""
# Esses valores para os eixos x e y devem resultar em um ajuste muito ruim para regressão linear:
import matplotlib.pyplot as plt
from scipy import stats

x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()

"""E o rrelacionamento?"""
# Você deve obter um rvalor muito baixo.
import numpy
from scipy import stats

x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

slope, intercept, r, p, std_err = stats.linregress(x, y)

print(r)