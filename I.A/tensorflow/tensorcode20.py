# -*- coding: iso-8859-15 -*-

# Carregando o dataset
# http://yann.lecun.com/exdb/mnist/
# MNIST = Modified National Institute of Standards and Technology database

# O conjunto de dados é dividido em dois grupos: 60.000 elementos para treinar o modelo e 10.000 adicionais para testá-lo. 
# As imagens originais, em preto e branco, foram normalizadas para caber em uma caixa de tamanho 28 × 28 pixels e centrado pelo cálculo do centro de massa dos pixels. 
# Cada ponto de dados MNIST é uma matriz de números que descrevem quão escuro cada pixel é. 


import input_data
import numpy as np
import matplotlib.pyplot as plt

# Usando o pacote input_data para carregar o dataset:

mnist_images = input_data.read_data_sets("MNIST_data/", one_hot = False)

# train.next_batch(10) retorna as 10 primeiras imagens:
pixels,real_values = mnist_images.train.next_batch(10)

# São retornadas duas listas, a matriz dos pixels carregados e a lista que contém os valores reais carregados:
print ("Lista de valores carregados ", real_values)
example_to_visualize = 5
print ("Elemento N° " + str(example_to_visualize + 1) + " da lista")


# Visualizando a imagem
# image = pixels[example_to_visualize,:]
# image = np.reshape(image,[28,28])
# plt.imshow(image)
# plt.show()