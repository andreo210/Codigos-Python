# Redes Neurais - Multilayer Perceptron 

# Importando pacotes
import tensorflow as tf
import matplotlib.pyplot as plt
import input_data

# Importando dataset MINST 
mnist = input_data.read_data_sets("/tmp/data/", one_hot = True)

# Parâmetros
learning_rate = 0.001
training_epochs = 15
batch_size = 100
display_step = 1

# Camadas
n_hidden_1 = 256 # primeira camada oculta
n_hidden_2 = 256 # segunda camada oculta
n_input = 784 # MNIST data input (img shape: 28*28)
n_classes = 10 # MNIST total classes (0-9 digits)

# tf Graph input
x = tf.placeholder("float", [None, n_input])
y = tf.placeholder("float", [None, n_classes])

# Função para criar o modelo
def multilayer_perceptron(x, weights, biases):
    # Camada oculta com ativação RELU 
    layer_1 = tf.add(tf.matmul(x, weights['h1']), biases['b1'])
    layer_1 = tf.nn.relu(layer_1)
    # Camada oculta com ativação RELU 
    layer_2 = tf.add(tf.matmul(layer_1, weights['h2']), biases['b2'])
    layer_2 = tf.nn.relu(layer_2)
    # Output layer com ativação linear
    out_layer = tf.matmul(layer_2, weights['out']) + biases['out']
    return out_layer

# Armazena camadas, pesos e bias
weights = {
    'h1': tf.Variable(tf.random_normal([n_input, n_hidden_1])),
    'h2': tf.Variable(tf.random_normal([n_hidden_1, n_hidden_2])),
    'out': tf.Variable(tf.random_normal([n_hidden_2, n_classes]))
}
biases = {
    'b1': tf.Variable(tf.random_normal([n_hidden_1])),
    'b2': tf.Variable(tf.random_normal([n_hidden_2])),
    'out': tf.Variable(tf.random_normal([n_classes]))
}

# Construindo o modelo
pred = multilayer_perceptron(x, weights, biases)

# Cost Function e Otimizador
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits = pred, labels = y))
optimizer = tf.train.AdamOptimizer(learning_rate = learning_rate).minimize(cost)

# Inicialziando as variáveis
init = tf.global_variables_initializer()

# Sessão
with tf.Session() as sess:
    sess.run(init)

    # Ciclo de Treinamento
    for epoch in range(training_epochs):
        avg_cost = 0.
        total_batch = int(mnist.train.num_examples/batch_size)
        
        # Loop por todos os batches
        for i in range(total_batch):
            batch_x, batch_y = mnist.train.next_batch(batch_size)
            
            # Executa a otimização 
            _, c = sess.run([optimizer, cost], feed_dict = {x: batch_x, y: batch_y})
            
            # Computando a média de perda 
            avg_cost += c / total_batch
        
        # Display logs por epoch step
        if epoch % display_step == 0:
            print ("Epoch:", '%04d' % (epoch+1), "Custo = ", "{:.9f}".format(avg_cost))
    print ("Treinamento Concluído!")

    # Testando o modelo
    correct_prediction = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1))

    # Calculando a acurácia
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
    print ("Acurácia:", accuracy.eval({x: mnist.test.images, y: mnist.test.labels}))



