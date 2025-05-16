##############################@title-1 Instale as bibliotecas necessárias
"""
!pip install keras~=3.8.0 \
  matplotlib~=3.10.0 \
  numpy~=2.0.0 \
  pandas~=2.2.0 \
  tensorflow~=2.18.0

print('\n\nAll requirements successfully installed.')

"""



###############################@title-2 Code - Carregar dependências
#general
import io

# data
import numpy as np
import pandas as pd

# machine learning
import keras

# data visualization
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import seaborn as sns



###################### @title-3 carregar dataset
chicago_taxi_dataset = pd.read_csv("https://download.mlcc.google.com/mledu-datasets/chicago_taxi_train.csv")



############################@title-4 Code - Ler dataset
# Atualiza o dataframe para usar colunas específicas.
training_df = chicago_taxi_dataset[['TRIP_MILES', 'TRIP_SECONDS', 'FARE', 'COMPANY', 'PAYMENT_TYPE', 'TIP_RATE']]

print('Read dataset completed successfully.')
print('Total number of rows: {0}\n\n'.format(len(training_df.index)))
training_df.head(200)



##############################@title-5 Code - Ver estatísticas do conjunto de dados
print('Total number of rows: {0}\n\n'.format(len(training_df.index)))
training_df.describe(include='all')



#############################@title-6 Clique duas vezes ou execute para visualizar respostas sobre estatísticas do conjunto de dados

answer = '''
Qual é a tarifa máxima? Resposta: R$ 159,25
Qual é a distância média entre todas as viagens? Resposta: 8,2895 milhas
Quantas empresas de táxi existem no conjunto de dados? Resposta: 31
Qual é o tipo de pagamento mais frequente? Resposta: Cartão de Crédito
Há algum recurso com dados faltando? Resposta: Não
'''

# Você deve conseguir encontrar as respostas para as perguntas sobre o conjunto de dados
# inspecionando a saída da tabela após executar o método describe do DataFrame.
#
# Execute esta célula de código para verificar suas respostas.

# Qual é a tarifa máxima?
max_fare = training_df['FARE'].max()
print("What is the maximum fare? \t\t\t\tAnswer: ${fare:.2f}".format(fare = max_fare))

# Qual é a distância média em todas as viagens?
mean_distance = training_df['TRIP_MILES'].mean()
print("What is the mean distance across all trips? \t\tAnswer: {mean:.4f} miles".format(mean = mean_distance))

# Quantas empresas de táxi existem no conjunto de dados?
num_unique_companies =  training_df['COMPANY'].nunique()
print("How many cab companies are in the dataset? \t\tAnswer: {number}".format(number = num_unique_companies))

# Qual é o tipo de pagamento mais frequente?
most_freq_payment_type = training_df['PAYMENT_TYPE'].value_counts().idxmax()
print("What is the most frequent payment type? \t\tAnswer: {type}".format(type = most_freq_payment_type))

# Há algum recurso com dados faltando?
missing_values = training_df.isnull().sum().sum()
print("Are any features missing data? \t\t\t\tAnswer:", "No" if missing_values == 0 else "Yes")



##############################################@title-7 Code - Ver matriz de correlação
training_df.corr(numeric_only = True)



##############################################@title-8 Clique duas vezes para ver as respostas sobre a matriz de correlação

# Qual característica se correlaciona mais fortemente com o rótulo FARE?
# ---------------------------------------------------------
answer ='''
O recurso com a correlação mais forte com a TARIFA é TRIP_MILES.
Como você pode esperar, TRIP_MILES parece um bom recurso para começar a treinar
o modelo. Observe também que o recurso TRIP_SECONDS também tem uma forte correlação
com a tarifa.
'''
print(answer)


# Which feature correlates least strongly to the label FARE?
# -----------------------------------------------------------
answer = '''The feature with the weakest correlation to the FARE is TIP_RATE.'''
print(answer)



#########################################@title-7 Code - View pairplot
sns.pairplot(training_df, x_vars=["FARE", "TRIP_MILES", "TRIP_SECONDS"], y_vars=["FARE", "TRIP_MILES", "TRIP_SECONDS"])



###########################################@title-8 Definir funções de plotagem aqui 

def make_plots(df, feature_names, label_name, model_output, sample_size=200):

  random_sample = df.sample(n=sample_size).copy()
  random_sample.reset_index()
  weights, bias, epochs, rmse = model_output

  is_2d_plot = len(feature_names) == 1
  model_plot_type = "scatter" if is_2d_plot else "surface"
  fig = make_subplots(rows=1, cols=2,
                      subplot_titles=("Loss Curve", "Model Plot"),
                      specs=[[{"type": "scatter"}, {"type": model_plot_type}]])

  plot_data(random_sample, feature_names, label_name, fig)
  plot_model(random_sample, feature_names, weights, bias, fig)
  plot_loss_curve(epochs, rmse, fig)

  fig.show()
  return

def plot_loss_curve(epochs, rmse, fig):
  curve = px.line(x=epochs, y=rmse)
  curve.update_traces(line_color='#ff0000', line_width=3)

  fig.append_trace(curve.data[0], row=1, col=1)
  fig.update_xaxes(title_text="Epoch", row=1, col=1)
  fig.update_yaxes(title_text="Root Mean Squared Error", row=1, col=1, range=[rmse.min()*0.8, rmse.max()])

  return

def plot_data(df, features, label, fig):
  if len(features) == 1:
    scatter = px.scatter(df, x=features[0], y=label)
  else:
    scatter = px.scatter_3d(df, x=features[0], y=features[1], z=label)

  fig.append_trace(scatter.data[0], row=1, col=2)
  if len(features) == 1:
    fig.update_xaxes(title_text=features[0], row=1, col=2)
    fig.update_yaxes(title_text=label, row=1, col=2)
  else:
    fig.update_layout(scene1=dict(xaxis_title=features[0], yaxis_title=features[1], zaxis_title=label))

  return

def plot_model(df, features, weights, bias, fig):
  df['FARE_PREDICTED'] = bias[0]

  for index, feature in enumerate(features):
    df['FARE_PREDICTED'] = df['FARE_PREDICTED'] + weights[index][0] * df[feature]

  if len(features) == 1:
    model = px.line(df, x=features[0], y='FARE_PREDICTED')
    model.update_traces(line_color='#ff0000', line_width=3)
  else:
    z_name, y_name = "FARE_PREDICTED", features[1]
    z = [df[z_name].min(), (df[z_name].max() - df[z_name].min()) / 2, df[z_name].max()]
    y = [df[y_name].min(), (df[y_name].max() - df[y_name].min()) / 2, df[y_name].max()]
    x = []
    for i in range(len(y)):
      x.append((z[i] - weights[1][0] * y[i] - bias[0]) / weights[0][0])

    plane=pd.DataFrame({'x':x, 'y':y, 'z':[z] * 3})

    light_yellow = [[0, '#89CFF0'], [1, '#FFDB58']]
    model = go.Figure(data=go.Surface(x=plane['x'], y=plane['y'], z=plane['z'],
                                      colorscale=light_yellow))

  fig.add_trace(model.data[0], row=1, col=2)

  return

def model_info(feature_names, label_name, model_output):
  weights = model_output[0]
  bias = model_output[1]

  nl = "\n"
  header = "-" * 80
  banner = header + nl + "|" + "MODEL INFO".center(78) + "|" + nl + header

  info = ""
  equation = label_name + " = "

  for index, feature in enumerate(feature_names):
    info = info + "Weight for feature[{}]: {:.3f}\n".format(feature, weights[index][0])
    equation = equation + "{:.3f} * {} + ".format(weights[index][0], feature)

  info = info + "Bias: {:.3f}\n".format(bias[0])
  equation = equation + "{:.3f}\n".format(bias[0])

  return banner + nl + info + nl + equation

print("SUCCESS: defining plotting functions complete.")




##################################@title-9 Code - Define ML functions

def build_model(my_learning_rate, num_features):
  """Create and compile a simple linear regression model."""
  # Descreva a topografia do modelo.
  # A topografia de um modelo de regressão linear simples
  # é um único nó em uma única camada.
  inputs = keras.Input(shape=(num_features,))
  outputs = keras.layers.Dense(units=1)(inputs)
  model = keras.Model(inputs=inputs, outputs=outputs)

  # Compilar a topografia do modelo em código que o Keras possa executar com eficiência
  # Configurar o treinamento para minimizar o erro quadrático médio do modelo.
  model.compile(optimizer=keras.optimizers.RMSprop(learning_rate=my_learning_rate),
                loss="mean_squared_error",
                metrics=[keras.metrics.RootMeanSquaredError()])

  return model


def train_model(model, features, label, epochs, batch_size):
  """Train the model by feeding it data."""

  # Alimente o modelo com o recurso e o rótulo.
  # O modelo será treinado para o número especificado de épocas.
  history = model.fit(x=features,
                      y=label,
                      batch_size=batch_size,
                      epochs=epochs)

  # Reúna o peso e o viés do modelo treinado.
  trained_weight = model.get_weights()[0]
  trained_bias = model.get_weights()[1]

  # A lista de épocas é armazenada separadamente do resto do histórico
  epochs = history.epoch

  # Isole o erro para cada época.
  hist = pd.DataFrame(history.history)

  # Para acompanhar a progressão do treinamento, vamos tirar um instantâneo
  # do erro quadrático médio do modelo em cada época.
  rmse = hist["root_mean_squared_error"]

  return trained_weight, trained_bias, epochs, rmse


def run_experiment(df, feature_names, label_name, learning_rate, epochs, batch_size):

  print('INFO: starting training experiment with features={} and label={}\n'.format(feature_names, label_name))

  num_features = len(feature_names)

  features = df.loc[:, feature_names].values
  label = df[label_name].values

  model = build_model(learning_rate, num_features)
  model_output = train_model(model, features, label, epochs, batch_size)

  print('\nSUCCESS: training experiment complete\n')
  print('{}'.format(model_info(feature_names, label_name, model_output)))
  make_plots(df, feature_names, label_name, model_output)

  return model

print("SUCCESS: defining linear regression functions complete.")


######################################@title-10 Code - Experimento 1

# As variáveis ​​a seguir são os hiperparâmetros.
learning_rate = 0.001
epochs = 20
batch_size = 50

# Especifique o recurso e o rótulo.
features = ['TRIP_MILES']
label = 'FARE'

model_1 = run_experiment(training_df, features, label, learning_rate, epochs, batch_size)




############################################@title-11 Clique duas vezes para ver as respostas do modelo de treinamento com um recurso

# Quantas épocas foram necessárias para convergir para o modelo final?
# -----------------------------------------------------------------------------
answer = """
Use a curva de perda para ver onde a perda começa a se estabilizar durante o treinamento.

Com este conjunto de hiperparâmetros:

learning_rate = 0,001
epochs = 20
batch_size = 50

Leva cerca de 5 épocas para que a execução do treinamento converja para o modelo final.
"""
print(answer)

# Quão bem o modelo se ajusta aos dados da amostra?
# -----------------------------------------------------------------------------
answer = '''
Parece, a partir do gráfico do modelo, que o modelo se ajusta muito bem aos dados da amostra.
'''
print(answer)





"""
É comum em aprendizado de máquina executar múltiplos experimentos para encontrar o melhor conjunto de hiperparâmetros para treinar seu modelo.
Nesta etapa, tente variar os hiperparâmetros um a um com este conjunto de experimentos:

Experimento 1: Aumente a taxa de aprendizado para 1 (tamanho do lote em 50).
Experimento 2: Diminua a taxa de aprendizado para 0,0001 (tamanho do lote em 50).
Experimento 3: Aumente o tamanho do lote para 500 (taxa de aprendizado em 0,001).
Instruções

Atualize os valores dos hiperparâmetros na célula de código do Experimento 2 de acordo com o experimento.
Execute a célula de código do Experimento 2.
Após a execução do treinamento, examine a saída e observe quaisquer diferenças observadas na curva de perdas ou na saída do modelo.
Repita as etapas 1 a 3 para cada experimento com hiperparâmetros.
Verifique sua compreensão respondendo a estas perguntas:
Como o aumento da taxa de aprendizado impactou sua capacidade de treinar o modelo?
Como a redução da taxa de aprendizado impactou sua capacidade de treinar o modelo?
A alteração do tamanho do lote afetou os resultados do treinamento?
"""

######################################@title-11 Code - Experimento 2

# As seguintes variáveis ​​são os hiperparâmetros.
# TODO - Ajuste esses hiperparâmetros para ver como eles impactam uma corrida de treinamento.
learning_rate = 0.001
epochs = 20
batch_size = 50

# Specify the feature and the label.
features = ['TRIP_MILES']
label = 'FARE'

model_1 = run_experiment(training_df, features, label, learning_rate, epochs, batch_size)



#@title Clique duas vezes para ver as respostas dos experimentos com hiperparâmetros

# Como o aumento da taxa de aprendizado impactou sua capacidade de treinar o modelo?
# -----------------------------------------------------------------------------
answer = """
Quando a taxa de aprendizado é muito alta, a curva de perdas oscila e não
parece estar se movendo em direção à convergência a cada iteração. Observe também que
o modelo previsto não se ajusta muito bem aos dados. Com uma taxa de aprendizado
muito alta, é improvável que você consiga treinar um modelo com bons
resultados.
"""
print(answer)

# Como a redução da taxa de aprendizagem impactou sua capacidade de treinar o modelo?
# -----------------------------------------------------------------------------
answer = '''
Quando a taxa de aprendizado é muito pequena, a curva de perdas pode levar mais tempo para convergir. 
Com uma taxa de aprendizado pequena, a curva de perdas diminui lentamente, mas não apresenta uma queda drástica ou estabilização. 
Com uma taxa de aprendizado pequena, você poderia aumentar o número de épocas para que seu modelo eventualmente convergisse, mas isso levaria mais tempo..
'''
print(answer)

# A alteração do tamanho do lote afetou os resultados do treinamento??
# -----------------------------------------------------------------------------
answer = '''
Aumentar o tamanho do lote faz com que cada época seja executada mais rapidamente, mas, assim como acontece com a menor
taxa de aprendizado, o modelo não converge com apenas 20 épocas. Se você tiver
tempo, tente aumentar o número de épocas e, eventualmente, você deverá ver
o modelo convergir..
'''
print(answer)





""""
O modelo que você treinou com o recurso TOTAL_MILES demonstra um poder preditivo bastante forte, mas é possível melhorar? 
Nesta etapa, tente treinar o modelo com dois recursos, TRIP_MILES e TRIP_MINUTES, 
para ver se é possível aprimorá-lo. 
Você deve se lembrar de que o conjunto de dados original não inclui o recurso TRIP_MINUTES,
mas esse recurso pode ser facilmente derivado de TRIP_SECONDS, conforme mostrado no código abaixo.*

Instruções

Revise o código na célula de código do Experimento 3.
Execute a célula de código do Experimento 3.
Revise a saída da execução do treinamento e responda às seguintes perguntas:
O modelo com dois recursos produz resultados melhores do que um usando um único recurso?
Faz diferença usar TRIP_SECONDS em vez de TRIP_MINUTES?
Qual a sua opinião sobre o desempenho do modelo no cálculo de tarifas para viagens de táxi em Chicago?
Observe que o gráfico de dispersão dos recursos em relação ao rótulo é um gráfico tridimensional (3D). 
Esta representação permite visualizar os recursos e o rótulo juntos. 
Os dois recursos (TRIP_MILES e TRIP_MINUTES) estão nos eixos x e y, e o rótulo (FARE) está no eixo z.
O gráfico mostra exemplos individuais no conjunto de dados como círculos e o modelo como uma superfície (plana). 
Com este modelo 3D, se o modelo treinado for bom, você esperaria que a maioria dos exemplos caísse na superfície plana. 
O gráfico 3D é interativo, então você pode explorar os dados mais detalhadamente clicando ou arrastando o gráfico.
"""

####################################@title Code-12 - Experimento 3

# As seguintes variáveis ​​são os hiperparâmetros.
learning_rate = 0.001
epochs = 20
batch_size = 50

training_df.loc[:, 'TRIP_MINUTES'] = training_df['TRIP_SECONDS']/60

features = ['TRIP_MILES', 'TRIP_MINUTES']
label = 'FARE'

model_2 = run_experiment(training_df, features, label, learning_rate, epochs, batch_size)



#@title Clique duas vezes para ver as respostas para o treinamento com dois recursos

# O modelo com dois recursos produz melhores resultados do que aquele que usa
# um único recurso?
# -----------------------------------------------------------------------------
answer = '''
Para responder a essa pergunta para suas execuções de treinamento específicas, compare o RMSE de
cada modelo. Por exemplo, se o RMSE do modelo treinado com uma característica foi
3,7457 e o RMSE do modelo com duas características foi 3,4787, isso significa que
em média, o modelo com duas características faz previsões cerca de US$ 0,27
mais próximas da tarifa observada.

'''
print(answer)

# Faz alguma diferença se você usar TRIP_SECONDS em vez de TRIP_MINUTES?
# -----------------------------------------------------------------------------
answer = '''
Ao treinar um modelo com mais de uma característica, é importante que todos os valores numéricos estejam aproximadamente na mesma escala. 
Nesse caso, TRIP_SECONDS e TRIP_MILES não atendem a esse critério. 
O valor médio para TRIP_MILES é 8,3 e a média para TRIP_SECONDS é 1.320; isso representa uma diferença de duas ordens de magnitude. 
Em contraste, a média para TRIP_MINUTES é 22, que é mais semelhante à escala de TRIP_MILES (8,3) do que de TRIP_SECONDS (1.320). 
É claro que esta não é a única maneira de escalar valores antes do treinamento, mas você aprenderá sobre isso em outro módulo..
'''
print(answer)

# Quão bem você acha que o modelo chega ao cálculo de tarifas reais para
# viagens de táxi em Chicago?
# -----------------------------------------------------------------------------
answer = '''
Na realidade, os táxis de Chicago usam uma fórmula documentada para determinar as tarifas.
Para um único passageiro pagando em dinheiro, a tarifa é calculada da seguinte forma:

TARIFA = 2,25 * MILHAS_DE_VIAGEM + 0,12 * MINUTOS_DE_VIAGEM + 3,25

Normalmente, com problemas de aprendizado de máquina, você não saberia a fórmula "correta",
mas neste caso, você pode usar esse conhecimento para avaliar seu modelo.
Observe a saída do seu modelo (os pesos e o viés) e determine o quão bem ele
corresponde ao cálculo da tarifa baseado na verdade básica. Você deverá descobrir que o modelo está
aproximadamente próximo desta fórmula..
'''
print(answer)






"""---------------------------------------------------------Part 4 - Validação do modelo-------------------------------------------"""


###########################################################@title Code-13 - Defina funções para fazer previsões
def format_currency(x):
  return "${:.2f}".format(x)

def build_batch(df, batch_size):
  batch = df.sample(n=batch_size).copy()
  batch.set_index(np.arange(batch_size), inplace=True)
  return batch

def predict_fare(model, df, features, label, batch_size=50):
  batch = build_batch(df, batch_size)
  predicted_values = model.predict_on_batch(x=batch.loc[:, features].values)

  data = {"PREDICTED_FARE": [], "OBSERVED_FARE": [], "L1_LOSS": [],
          features[0]: [], features[1]: []}
  for i in range(batch_size):
    predicted = predicted_values[i][0]
    observed = batch.at[i, label]
    data["PREDICTED_FARE"].append(format_currency(predicted))
    data["OBSERVED_FARE"].append(format_currency(observed))
    data["L1_LOSS"].append(format_currency(abs(observed - predicted)))
    data[features[0]].append(batch.at[i, features[0]])
    data[features[1]].append("{:.2f}".format(batch.at[i, features[1]]))

  output_df = pd.DataFrame(data)
  return output_df

def show_predictions(output):
  header = "-" * 80
  banner = header + "\n" + "|" + "PREDICTIONS".center(78) + "|" + "\n" + header
  print(banner)
  print(output)
  return




############################################################@title Code-13 - Faça previsões

output = predict_fare(model_2, training_df, features, label)
show_predictions(output)






###################################################@title-14 Clique duas vezes para visualizar as respostas para validar o modelo

# Quão próximo está o valor previsto do valor do rótulo?
# -----------------------------------------------------------------------------
answer = '''
Com base em uma amostragem aleatória de exemplos, o modelo parece se sair muito bem
prevendo a tarifa de uma corrida de táxi. A maioria dos valores previstos não varia
significativamente em relação ao valor observado. Você deve conseguir ver isso observando
a coluna L1_LOSS = |observed - expected|.
'''
print(answer)