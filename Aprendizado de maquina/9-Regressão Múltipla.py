"""
Regressão múltipla
A regressão múltipla é como a regressão linear , mas com mais de um valor independente, 
o que significa que tentamos prever um valor com base em duas ou mais variáveis.

"""
import pandas
from sklearn import linear_model

df = pandas.read_csv("C:\\Users\\andreoa\\Documents\\Codigos-Python\\Aprendizado de maquina\\data.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(X, y)

#predict the CO2 emission of a car where the weight is 2300kg, and the volume is 1300cm3:
predictedCO2 = regr.predict([[2300, 1300]])

print(predictedCO2)





"""
Coeficiente
O coeficiente é um fator que descreve a relação com uma variável desconhecida.
Exemplo: se x é uma variável, então 2x é x duas vezes. x é a variável desconhecida, e o número 2 é o coeficiente.
Neste caso, podemos pedir o valor do coeficiente de peso contra CO2, 
e de volume contra CO2. A(s) resposta(s) que obtemos nos diz(ão) o que aconteceria se aumentássemos, ou diminuíssemos, um dos valores independentes.
"""
# Imprima os valores dos coeficientes do objeto de regressão:
import pandas
from sklearn import linear_model

df = pandas.read_csv("C:\\Users\\andreoa\\Documents\\Codigos-Python\\Aprendizado de maquina\\data.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(X, y)

print(regr.coef_)

"""
Resultado Explicado
A matriz de resultados representa os valores dos coeficientes de peso e volume.

Peso: 0,00755095
Volume: 0,00780526

Esses valores nos dizem que se o peso aumentar em 1 kg, a emissão de CO2 aumentará em 0,00755095 g.
E se o tamanho do motor (volume) aumentar em 1 cm 3 , a emissão de CO2 aumentará em 0,00780526 g.
Acho que é um palpite justo, mas vamos testar!
Já previmos que se um carro com motor de 1300 cm3 pesar 2300 kg, a emissão de CO2 será de aproximadamente 107 g.
E se aumentarmos o peso em 1000 kg?
"""
# Copie o exemplo anterior, mas altere o peso de 2300 para 3300:
import pandas
from sklearn import linear_model

df = pandas.read_csv("C:\\Users\\andreoa\\Documents\\Codigos-Python\\Aprendizado de maquina\\data.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(X, y)

predictedCO2 = regr.predict([[3300, 1300]])

print(predictedCO2)