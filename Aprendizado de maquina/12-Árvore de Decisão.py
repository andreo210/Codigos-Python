"""
Neste capítulo, mostraremos como criar uma "Árvore de Decisão". 
Uma Árvore de Decisão é um fluxograma e pode ajudar você a tomar decisões com base em experiências anteriores.

No exemplo, uma pessoa tentará decidir se deve ir a um show de comédia ou não.
Felizmente, a pessoa do nosso exemplo se registrou sempre que houve um show de comédia na cidade,
registrou algumas informações sobre o comediante e também se ele/ela foi ou não.
"""

import pandas
df = pandas.read_csv("C:\\Users\\andreoa\\Documents\\Codigos-Python\\Aprendizado de maquina\\12-data.csv")
print(df)



"""
Para criar uma árvore de decisão, todos os dados precisam ser numéricos.
Temos que converter as colunas não numéricas 'Nacionalidade' e 'Ir' em valores numéricos.
O Pandas tem um map() que recebe um dicionário com informações sobre como converter os valores.

{'UK': 0, 'USA': 1, 'N': 2}
Significa converter os valores 'UK' para 0, 'USA' para 1 e 'N' para 2.
"""
d = {'UK': 0, 'USA': 1, 'N': 2}
df['Nationality'] = df['Nationality'].map(d)
d = {'YES': 1, 'NO': 0}
df['Go'] = df['Go'].map(d)

print(df)




"""
Então temos que separar as colunas de recursos da coluna de destino .

As colunas de recursos são as colunas que tentamos prever , e a coluna de destino é a coluna com os valores que tentamos prever.
"""
# Xs ão as colunas de recursos, y é a coluna de destino:
features = ['Age', 'Experience', 'Rank', 'Nationality']

X = df[features]
y = df['Go']

print(X)
print(y)



"""
Agora podemos criar a árvore de decisão propriamente dita e ajustá-la aos nossos detalhes. Comece importando os módulos necessários:
"""
# Crie e exiba uma Árvore de Decisão:
import pandas
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

df = pandas.read_csv("C:\\Users\\andreoa\\Documents\\Codigos-Python\\Aprendizado de maquina\\12-data.csv")

d = {'UK': 0, 'USA': 1, 'N': 2}
df['Nationality'] = df['Nationality'].map(d)
d = {'YES': 1, 'NO': 0}
df['Go'] = df['Go'].map(d)

features = ['Age', 'Experience', 'Rank', 'Nationality']

X = df[features]
y = df['Go']

dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)

tree.plot_tree(dtree, feature_names=features)