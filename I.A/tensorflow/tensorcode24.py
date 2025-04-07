# Redes Neurais Artificiais - Multilayer Perceptron

# O Multilayer Perceptron (MLP) é uma arquitetura complexa e eficiente. É substancialmente formada a partir de múltiplas camadas de perceptrons e, portanto, 
# pela presença de pelo menos uma camada oculta. Uma rede deste tipo é normalmente treinada usando aprendizagem supervisionada. 
# Em particular, um algoritmo de aprendizagem típico para redes MLP é o chamado algoritmo de retropropagação (backpropagation).

# O algoritmo de retropropagação é um algoritmo de aprendizagem para redes neurais. Ele compara o valor de saída do sistema com o valor desejado. 
# Com base na diferença calculada (o erro), o algoritmo modifica os pesos sinápticos da rede neural, convergindo progressivamente o conjunto de valores de saída para os desejados. 
# É importante notar que em redes MLP, embora você não saiba as saídas desejadas dos neurônios das camadas ocultas da rede, é sempre possível aplicar um método de 
# aprendizagem supervisionado com base na minimização de uma função de erro através da aplicação de técnicas de gradient-descent. 
# A seguir, a implementação com MLP para um problema de classificação de imagens (MNIST).

# Importando pacotes
import tensorflow as tf
import matplotlib.pyplot as plt
import input_data

# Importando dataset MINST 
mnist = input_data.read_data_sets("/tmp/data/", one_hot = True)

# Parâmetros
learning_rate = 0.001
training_epochs = 20
batch_size = 100
display_step = 1

# Deve ser observado que, embora para um dado aplicativo, o tamanho do conjunto de entrada e saída seja perfeitamente definido, não existem critérios estritos 
# para definir o número de camadas ocultas e o número de neurônios para cada camada. 
# Cada escolha deve ser baseada na experiência de aplicações semelhantes. Ao aumentar o número de camadas ocultas, devemos também aumentar 
# o tamanho do conjunto de treinamento que é necessário e também aumentar o número de conexões a serem atualizadas, durante a aprendizagem. 
# Isso resulta em um aumento no tempo de treinamento. Além disso, se houver muitos neurônios na camada oculta, não só há mais pesos a serem atualizados, 
# mas a rede também tem uma tendência a aprender demais com os exemplos de treinamento estabelecidos, resultando em uma má capacidade de generalização (overfitting). 
# Mas então, se o número de neurônios ocultos for muito pouco, a rede não é capaz de aprender mesmo com o conjunto de treinamento (underfitting).

# Parâmetros da rede
n_hidden_1 = 256 # primeira camada - número de features (número de neurônios)
n_hidden_2 = 256 # segunda camada - número de features (número de neurônios)
n_input = 784 # dados de entrada MNIST (img shape: 28*28)
n_classes = 10 # total de classes MNIST (0-9 digits)

# Placeholders
x = tf.placeholder("float", [None, n_input])
y = tf.placeholder("float", [None, n_classes])

# Camadas, Pesos e Bias

# No meio, temos duas camadas ocultas. A primeira camada é constituída pelo tensor h de pesos, cujo tamanho é [784 × 256], onde 256 é o número total de nós da camada. 
# Cada neurônio recebe os pixels da imagem de entrada a serem classificados combinados com as conexões de peso hij e adicionados aos respectivos valores do tensor de polarização (bias). 

# Ele envia sua saída para os neurônios da próxima camada através da função de ativação. Deve-se dizer que as funções podem ser diferentes de um neurônio para outro, 
# mas na prática, no entanto, adotamos uma característica comum para todos os neurônios, tipicamente do tipo sigmoidal. Às vezes, os neurônios de saída são equipados 
# com uma função de ativação linear. É interessante notar que as funções de ativação dos neurônios nas camadas ocultas não podem ser lineares porque, neste caso, 
# a rede MLP seria equivalente a uma rede com duas camadas e, portanto, não mais do tipo MLP. A segunda camada deve executar as mesmas etapas que a primeira.

# Cada neurônio nesta segunda camada recebe entradas a partir dos neurônios da camada 1, combinados com as conexões Wij de peso e adicionados aos respectivos 
# enviesamentos da camada 2:

# Pesos da camada 1 
h = tf.Variable(tf.random_normal([n_input, n_hidden_1]))

# Bias da camada 1
bias_layer_1 = tf.Variable(tf.random_normal([n_hidden_1]))

# Camada 1
layer_1 = tf.nn.sigmoid(tf.add(tf.matmul(x,h),bias_layer_1))

# Pesos da camada 2
w = tf.Variable(tf.random_normal([n_hidden_1, n_hidden_2]))

# Bias da camada 2
bias_layer_2 = tf.Variable(tf.random_normal([n_hidden_2]))

# Camada 2
layer_2 = tf.nn.sigmoid(tf.add(tf.matmul(layer_1,w),bias_layer_2))

# Pesos da camada de Saída (output)
output = tf.Variable(tf.random_normal([n_hidden_2, n_classes]))

# Bias da camada de Saída (output)
bias_output = tf.Variable(tf.random_normal([n_classes]))

# Camada de Saída (output)
output_layer = tf.matmul(layer_2, output) + bias_output

# Cost Function
# A função TensorFlow tf.nn.softmax_cross_entropy_with_logits calcula o custo para uma camada com função softmax. 
# É usado somente durante o treinamento. Os logits são as probabilidades do log de saída do modelo.
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits = output_layer, labels = y))

# Otimização da Cost Function
# Um outro tipo de otimizador que minimiza a função de custo é o tf.train.AdamOptimizer que usa o algoritmo Adam para controlar a taxa de aprendizado. 
# Adam oferece várias vantagens sobre o tf.train.GradientDescentOptimizer. De fato, ele usa um tamanho de passo maior e o algoritmo converge para 
# este tamanho de passo sem ajuste fino. 
# Um tf.train.GradientDescentOptimizer simples poderia igualmente ser usado em seu MLP, mas exigiria o ajuste dos parâmetros antes que pudesse convergir tão rapidamente.
optimizer = tf.train.AdamOptimizer(learning_rate = learning_rate).minimize(cost) 
#optimizer = tf.train.GradientDescentOptimizer(learning_rate = learning_rate).minimize(cost)


# Parâmetros do Plot
avg_set = []
epoch_set = []
    
# Inicializando as variáveis
init = tf.global_variables_initializer()

# Sessão
with tf.Session() as sess:
    sess.run(init)

    # Ciclo de Treinamento
    for epoch in range(training_epochs):
        avg_cost = 0.
        total_batch = int(mnist.train.num_examples/batch_size)
        
        # Loop por todas as iterações (batches)
        for i in range(total_batch):
            batch_xs, batch_ys = mnist.train.next_batch(batch_size)
            
            # Fit training usando batch data
            sess.run(optimizer, feed_dict = {x: batch_xs, y: batch_ys})
            
            # Computando average loss
            avg_cost += sess.run(cost, feed_dict = {x: batch_xs, y: batch_ys})/total_batch
        
        # Display logs por epoch step
        if epoch % display_step == 0:
            print ("Epoch: ", '%04d' % (epoch+1), "Custo = ", "{:.9f}".format(avg_cost))
        avg_set.append(avg_cost)
        epoch_set.append(epoch+1)
    print ("Treinamento Concluído")

    plt.plot(epoch_set,avg_set, 'o', label = 'MLP - Fase de Treinamento')
    plt.ylabel('Custo')
    plt.xlabel('Epoch')
    plt.legend()
    plt.show()
        
    # Testando o Modelo
    correct_prediction = tf.equal(tf.argmax(output_layer, 1), tf.argmax(y, 1))
    
    # Calculando a acurácia
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
    print ("Acurácia do Modelo:", accuracy.eval({x: mnist.test.images, y: mnist.test.labels}))


