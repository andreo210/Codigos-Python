# -*- coding: iso-8859-15 -*-

# Classificação de imagens com KNN
# O K-vizinho mais próximo (KNN - K-Nearest Neighbor) é um algoritmo de aprendizagem supervisionado tanto para a classificação como para a regressão. 
# É um sistema que atribui a classe da amostra testada de acordo com sua distância dos objetos armazenados na memória. A distância, d, é definida 
# como a distância euclidiana entre dois pontos.

# A vantagem deste método de classificação é a capacidade de classificar objetos cujas classes não são linearmente separáveis. 
# É um classificador estável, dado que pequenas perturbações (ruídos) dos dados de treinamento não afetam significativamente os resultados obtidos. 
# A desvantagem mais óbvia, no entanto, é que ele não fornece um verdadeiro modelo matemático. Em vez disso, para cada nova classificação, devem ser 
# adicionados novos dados a todas as instâncias iniciais e repetindo o procedimento de cálculo para o valor K selecionado. 

import numpy as np
import tensorflow as tf
import input_data

# Carregando o dataset (fazendo leitura localmente)
mnist = input_data.read_data_sets("/tmp/data/", one_hot = True)

# Construindo os datasets de treino e de teste
# Valores observados
train_pixels, train_list_values = mnist.train.next_batch(100) 
test_pixels, test_list_of_values  = mnist.test.next_batch(10) 

# Definindo os tensores com placeholders
# Valores previstos
train_pixel_tensor = tf.placeholder("float", [None, 784])
test_pixel_tensor = tf.placeholder("float", [784])

# Cost Function e Otimização de Distância
# A função de custo é representada pela distância em termos de pixels.
# A soma da função tf.reduce_sum calcula a soma dos elementos através das dimensões de um tensor.
distance = tf.reduce_sum(tf.abs(tf.add(train_pixel_tensor, tf.negative(test_pixel_tensor))), reduction_indices = 1)

# Finalmente, para minimizar a função de distância, usamos arg_min, que retorna o índice com a menor distância (vizinho mais próximo - KNN - K-Nearest Neighbor):
pred = tf.arg_min(distance, 0)

# Testando e Avaliando o Algoritmo
accuracy = 0.
init = tf.initialize_all_variables()
with tf.Session() as sess:
    sess.run(init)
    for i in range(len(test_list_of_values)):
        nn_index = sess.run(pred, feed_dict = {train_pixel_tensor:train_pixels, test_pixel_tensor:test_pixels[i,:]})
        print ("Teste N° ", i,"Classe Prevista: ", np.argmax(train_list_values[nn_index]), "Classe Observada (Verdadeira): ", np.argmax(test_list_of_values[i]))
        if np.argmax(train_list_values[nn_index]) == np.argmax(test_list_of_values[i]):
            accuracy += 1./len(test_pixels)
    print ("Resultado = ", accuracy)
