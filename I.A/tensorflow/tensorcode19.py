# Regressão Linear com TensorFlow

# Vamos explorar um pouco mais as técnicas de aprendizagem de máquina com o algoritmo de regressão linear. 
# Nosso objetivo é construir um modelo que possa prever os valores de uma variável dependente a partir dos valores de uma ou mais variáveis independentes.

# A relação entre essas duas variáveis é linear. Isto é, se y é a variável dependente e x o independente, 
# então a relação linear entre as duas variáveis será assim: y = Ax + b.

# O algoritmo de regressão linear adapta-se a uma grande variedade de situações; Por sua versatilidade, é amplamente utilizado no campo das mais variadas 
# ciências aplicadas.

# Além disso, a implementação deste algoritmo nos permite introduzir de uma forma totalmente clara e compreensível os dois conceitos 
# importantes de aprendizagem de máquina: a função de custo e os algoritmos de descida de gradiente.

import numpy as np

# O primeiro passo é construir nosso modelo de dados. Mencionamos anteriormente que a relação entre nossas variáveis é linear, isto é: y = Ax + b, 
# onde A e b são constantes. Para testar nosso algoritmo, precisamos de pontos de dados em um espaço bidimensional.
number_of_points = 200

x_point = []
y_point = []

a = 0.22
b = 0.78

# Através da função random.normal do NumPy, geramos 300 pontos aleatórios em torno da equação de regressão y = 0.22x + 0.78:
for i in range(number_of_points):
    x = np.random.normal(0.0,0.5)
    y = a*x + b +np.random.normal(0.0,0.1)
    x_point.append([x])
    y_point.append([y])


# Visualizando os pontos de dados gerados
import matplotlib.pyplot as plt

plt.plot(x_point,y_point, 'o', label = 'Input Data')
plt.legend()
plt.show()


import tensorflow as tf

# O algoritmo de aprendizagem da máquina que queremos implementar com TensorFlow deve prever valores de y como uma função de dados x 
# de acordo com o nosso modelo de dados. O algoritmo de regressão linear determinará os valores das constantes A e b 
# (fixadas para o nosso modelo de dados), que são então as verdadeiras incógnitas do problema.
A = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
B = tf.Variable(tf.zeros([1]))
y = A * x_point + B


# O objetivo do algoritmo de ML é aprender um modelo que minimize os erros. A força motriz por trás do processo de otimização na aprendizagem de 
# máquina é a resposta de uma função interna do algoritmo, chamada de cost function. É também chamada de função de perda, função objetivo, 
# função de pontuação ou função de erro. A cost function é uma função de avaliação que mede quão bem o algoritmo mapeia a função-alvo, 
# aquela que ele está tentando deduzir a partir dos dados que você forneceu. 

# A Cost Function tem parâmetros contendo um par de valores A e b a serem determinados, que retorna um valor que estima o quão bem 
# os parâmetros estão corretos. Neste exemplo, nossa função de custo é o erro quadrático médio (mean square error).

# A Cost Function proporciona uma estimativa da variabilidade das medidas, ou mais precisamente, da dispersão de valores em torno do valor médio.
# Um valor pequeno como resultado desta função, corresponde a uma melhor estimativa para os parâmetros desconhecidos A e b.

# Comparando uma previsão contra o seu valor real, usando uma cost function, determinamos o nível de erro do algoritmo. 
# Por ser uma formulação matemática, a cost function expressa o nível de erro em uma forma numérica. A cost function transmite o que é 
# realmente importante e significativo para seus propósitos com o algoritmo de aprendizagem. 
cost_function = tf.reduce_mean(tf.square(y - y_point))


# Para minimizar a Cost Function, usamos um algoritmo de otimização com a descida do gradiente. Dada uma função matemática de diversas variáveis, 
# a descida do gradiente permite encontrar um mínimo local desta função. A técnica é a seguinte:

# Avaliar, em um primeiro ponto arbitrário do domínio da função, a própria função e seu gradiente. O gradiente indica a direção em que a função tende a um mínimo.
# Selecione um segundo ponto na direção indicada pelo gradiente. Se a função para este segundo ponto tiver um valor inferior ao valor calculado no primeiro ponto, 
# a descida pode continuar.

# Também observamos que a descida de gradiente é apenas uma função local mínima, mas também pode ser usada na busca de um mínimo global, escolhendo 
# aleatoriamente um novo ponto de partida depois de ter encontrado um mínimo local e repetir o processo muitas vezes. 
# Se o número de mínimos da função é limitado e há um número muito elevado de tentativas, há uma boa chance de que, mais cedo ou mais tarde, 
# o mínimo global seja identificado.

# Aqui 0,5 é a taxa de aprendizagem do algoritmo. A taxa de aprendizagem determina quão rápido ou lento nos movemos em direção aos pesos ótimos. 
# Se é muito grande, ignoramos a solução ideal e, se for muito pequena, precisamos de muitas iterações para convergir para os melhores valores. 
# Um valor intermediário (0.5) é fornecido, mas deve ser sintonizado para melhorar o desempenho de todo o procedimento. 
optimizer = tf.train.GradientDescentOptimizer(0.5)


# # Definimos o treinamento como o resultado da aplicação da função custo (otimizador), através de sua função de minimização:
train = optimizer.minimize(cost_function)


# Inicializa as variáveis 
model = tf.initialize_all_variables()

# Sessão para executar o modelo
with tf.Session() as session:
        session.run(model)
        for step in range(0,21):
                session.run(train)
                if (step % 5) == 0:
                        plt.plot(x_point, y_point, 'o',label = 'step = {}'.format(step))
                        plt.plot(x_point, session.run(A) * x_point + session.run(B))
                        plt.legend()
                        plt.show()

# Tensorboard

# Sessão
with tf.Session() as session:
    merged = tf.summary.merge_all()
    writer = tf.summary.FileWriter("/tmp/my_graph", session.graph)
    session.run(model)
    print(session.run(y))


# Para inicializar o TensorBoard: tensorboard --logdir=/tmp/my_graph








    



