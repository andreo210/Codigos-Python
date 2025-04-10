"""
Características da escala
Quando seus dados têm valores diferentes, e até mesmo unidades de medida diferentes,
pode ser difícil compará-los. O que são quilogramas comparados a metros? Ou altitude comparada a tempo?

A resposta para esse problema é o escalonamento. Podemos escalonar dados para novos valores que são mais fáceis de comparar.
Dê uma olhada na tabela abaixo, é o mesmo conjunto de dados que usamos no capítulo de regressão múltipla ,
mas desta vez a coluna de volume contém valores em litros em vez de cm 3 (1,0 em vez de 1000).

Pode ser difícil comparar o volume 1.0 com o peso 790, mas se os escalarmos em valores comparáveis, podemos ver facilmente o quanto um valor é comparado ao outro.
Existem diferentes métodos para dimensionar dados. Neste tutorial, usaremos um método chamado padronização.
O método de padronização usa esta fórmula:

z = (x - u) / s

Onde zé o novo valor, xé o valor original, ué a média e sé o desvio padrão.
Se você pegar a coluna de peso do conjunto de dados acima, o primeiro valor é 790, e o valor dimensionado será:

(790 - 1292.23) / 238.74 = -2.1
Se você pegar a coluna de volume do conjunto de dados acima, o primeiro valor será 1,0, e o valor dimensionado será:

(1.0 - 1.61) / 0.38 = -1.59

Agora você pode comparar -2,1 com -1,59 em vez de comparar 790 com 1,0.
Você não precisa fazer isso manualmente, o módulo sklearn do Python tem um método chamado StandardScaler() 
que retorna um objeto Scaler com métodos para transformar conjuntos de dados.
"""
# Dimensione todos os valores nas colunas Peso e Volume:
#import pandas
#from sklearn import linear_model
#from sklearn.preprocessing import StandardScaler
#scale = StandardScaler()

#df = pandas.read_csv("C:\\Users\\andreoa\\Documents\\Codigos-Python\\Aprendizado de maquina\\data.csv")

#X = df[['Weight', 'Volume']]

#scaledX = scale.fit_transform(X)

#print(scaledX)





"""
Prever valores de CO2
A tarefa no capítulo Regressão Múltipla era prever a emissão de CO2 de um carro quando você só sabia seu peso e volume.
Quando o conjunto de dados for dimensionado, você terá que usar a escala ao prever valores:
"""
#Preveja a emissão de CO2 de um carro de 1,3 litro que pesa 2.300 quilos:
import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()

df = pandas.read_csv("C:\\Users\\andreoa\\Documents\\Codigos-Python\\Aprendizado de maquina\\data.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

scaledX = scale.fit_transform(X)

regr = linear_model.LinearRegression()
regr.fit(scaledX, y)

scaled = scale.transform([[2300, 1.3]])