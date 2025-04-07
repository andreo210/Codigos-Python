# -*- coding: iso-8859-15 -*-

# Classifica��o de imagens com KNN
# O K-vizinho mais pr�ximo (KNN - K-Nearest Neighbor) � um algoritmo de aprendizagem supervisionado tanto para a classifica��o como para a regress�o. 
# � um sistema que atribui a classe da amostra testada de acordo com sua dist�ncia dos objetos armazenados na mem�ria. A dist�ncia, d, � definida 
# como a dist�ncia euclidiana entre dois pontos.

# A vantagem deste m�todo de classifica��o � a capacidade de classificar objetos cujas classes n�o s�o linearmente separ�veis. 
# � um classificador est�vel, dado que pequenas perturba��es (ru�dos) dos dados de treinamento n�o afetam significativamente os resultados obtidos. 
# A desvantagem mais �bvia, no entanto, � que ele n�o fornece um verdadeiro modelo matem�tico. Em vez disso, para cada nova classifica��o, devem ser 
# adicionados novos dados a todas as inst�ncias iniciais e repetindo o procedimento de c�lculo para o valor K selecionado. 

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

# Cost Function e Otimiza��o de Dist�ncia
# A fun��o de custo � representada pela dist�ncia em termos de pixels.
# A soma da fun��o tf.reduce_sum calcula a soma dos elementos atrav�s das dimens�es de um tensor.
distance = tf.reduce_sum(tf.abs(tf.add(train_pixel_tensor, tf.negative(test_pixel_tensor))), reduction_indices = 1)

# Finalmente, para minimizar a fun��o de dist�ncia, usamos arg_min, que retorna o �ndice com a menor dist�ncia (vizinho mais pr�ximo - KNN - K-Nearest Neighbor):
pred = tf.arg_min(distance, 0)

# Testando e Avaliando o Algoritmo
accuracy = 0.
init = tf.initialize_all_variables()
with tf.Session() as sess:
    sess.run(init)
    for i in range(len(test_list_of_values)):
        nn_index = sess.run(pred, feed_dict = {train_pixel_tensor:train_pixels, test_pixel_tensor:test_pixels[i,:]})
        print ("Teste N� ", i,"Classe Prevista: ", np.argmax(train_list_values[nn_index]), "Classe Observada (Verdadeira): ", np.argmax(test_list_of_values[i]))
        if np.argmax(train_list_values[nn_index]) == np.argmax(test_list_of_values[i]):
            accuracy += 1./len(test_pixels)
    print ("Resultado = ", accuracy)
