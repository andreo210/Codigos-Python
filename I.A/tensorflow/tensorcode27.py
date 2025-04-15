# Recurrent Neural Network com TensorFlow

# Para usar RNNs na classificação de imagens, precisamos considerar cada imagem como uma sequência de pixels. 
# Como as imagens no dataset MNIST possuem um shape 28x28 pixels, nós iremos trabalhar com 28 sequências de 28 timesteps para cada amostra.

# Pacotes
import input_data
import tensorflow as tf
from tensorflow.contrib import rnn

# Dataset
mnist = input_data.read_data_sets("/tmp/data/", one_hot = True)

# Parâmetros para o processo de aprendizagem
learning_rate = 0.001
training_iters = 100000
batch_size = 128
display_step = 10

# Inputs, Steps, Hidden e Output
n_input = 28 
n_steps = 28 
n_hidden = 128 # número de features na camada oculta
n_classes = 10 

# Input e classes
x = tf.placeholder("float", [None, n_steps, n_input])
y = tf.placeholder("float", [None, n_classes])

# Pesos e bias
weights = {'out': tf.Variable(tf.random_normal([n_hidden, n_classes]))}
biases = {'out': tf.Variable(tf.random_normal([n_classes]))}

# Função para o modelo RNN
def RNN(x, weights, biases):
    x = tf.transpose(x, [1, 0, 2])
    x = tf.reshape(x, [-1, n_input])
    x = tf.split(axis = 0, num_or_size_splits = n_steps, value = x)
    lstm_cell = rnn.BasicLSTMCell(n_hidden, forget_bias = 1.0)
    outputs, states = rnn.static_rnn(lstm_cell, x, dtype = tf.float32)
    return tf.matmul(outputs[-1], weights['out']) + biases['out']

# Executando o modelo
pred = RNN(x, weights, biases)

# Cost Function e Otimização
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits = pred, labels = y))
optimizer = tf.train.AdamOptimizer(learning_rate = learning_rate).minimize(cost)

# Previsões e acurácia
correct_pred = tf.equal(tf.argmax(pred,1), tf.argmax(y,1))
accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

# Inicializando as variáveis
init = tf.global_variables_initializer()

# Sessão
with tf.Session() as sess:
    sess.run(init)
    step = 1
    while step * batch_size < training_iters:
        batch_x, batch_y = mnist.train.next_batch(batch_size)
        batch_x = batch_x.reshape((batch_size, n_steps, n_input))
        sess.run(optimizer, feed_dict = {x: batch_x, y: batch_y})
        if step % display_step == 0:
            acc = sess.run(accuracy, feed_dict = {x: batch_x, y: batch_y})
            loss = sess.run(cost, feed_dict = {x: batch_x, y: batch_y})
            print("Iteração " + str(step*batch_size) + ", Perda = " + "{:.6f}".format(loss) + ", Acurácia no Treino = " + "{:.5f}".format(acc))
        step += 1
    print("Treinamento e Otimização Concluídos!")

    test_len = 128
    test_data = mnist.test.images[:test_len].reshape((-1, n_steps, n_input))
    test_label = mnist.test.labels[:test_len]
    print("Acurácia no Teste:", sess.run(accuracy, feed_dict = {x: test_data, y: test_label}))


