# TensorBoard
# Construindo um único neurônio

# Ao treinar uma rede neural, pode ser útil acompanhar os parâmetros da rede, as entradas e saídas dos nós, para que você possa ver se seu modelo 
# está aprendendo após cada etapa de treinamento e se o erro está sendo minimizado ou não. 

# TensorBoard é uma estrutura projetada para análise e depuração de modelos de redes neurais. O TensorBoard usa os chamados "summaries" 
# para visualizar os parâmetros do modelo. Uma vez que um código TensorFlow seja executado, podemos chamar o TensorBoard para ver resumos em uma 
# interface gráfica (GUI). Além disso, o TensorBoard pode ser usado para exibir e estudar o grafo computacional do TensorFlow, que pode ser muito 
# complexo para um modelo de Rede Neural Profunda.

# O TensorFlow usa grafos de computação para executar um aplicativo, onde cada nó representa uma operação e os arcos são os dados entre operações. 
# A ideia principal no TensorBoard é associar o chamado "summary" com os nós (operações) do grafo. Executando o código, as operações de summary 
# vão serializar os dados do nó que está associado a ele e emitirão os dados para um arquivo que pode ser lido pelo TensorBoard.

# Podemos então executar o TensorBoard e visualizar as operações de forma sumarizada. O fluxo de trabalho ao usar o TensorBoard é: 
# 1- Crie seu grafo / código computacional 
# 2- Anexe operações de resumo (summary) aos nós que você está interessado em examinar 
# 3- Inicie a execução do grafo como faria normalmente
# 4- Após executar o código, use o TensorBoard para visualizar as saídas de resumo

import tensorflow as tf

# Input
input_value = tf.constant(0.5, name="input_value")

# Peso
weight = tf.Variable(1.0, name="weight")

# Output esperado (usado no treinamento)
expected_output = tf.constant(0.0, name="expected_output")

# Criação do modelo
model = tf.multiply(input_value, weight, "model")

# Cost Function
loss_function = tf.pow(model - expected_output, 2, name="loss_function")

# Otimizador
optimizer = tf.train.GradientDescentOptimizer(0.025).minimize(loss_function)

# Definição do tf.summary.scalar() para visualizar no TensorBoard
for value in [input_value, weight, expected_output, model, loss_function]:
    tf.summary.scalar(value.op.name, value)

# Merge de todos os summaries em uma única saída
summaries = tf.summary.merge_all()
sess = tf.Session()

# Gravando os resultados
summary_writer = tf.summary.FileWriter('/tmp/testetb', sess.graph)

# Inicializando as variáveis na sessão
sess.run(tf.global_variables_initializer())

# Executando a sessão e gerando os summaries
for i in range(100):
    summary_writer.add_summary(sess.run(summaries), i)
    sess.run(optimizer)


# Inicializando o Tensorboard
# tensorboard --logdir = /tmp/testetb




