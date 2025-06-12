# Baixe e extraia o dataset de gatos e cachorros, e instale o tensorflow
"""
!wget https://storage.googleapis.com/mledu-datasets/cats_and_dogs_filtered.zip
!unzip cats_and_dogs_filtered.zip
!rm -rf cats_and_dogs_filtered.zip
!pip install tensorflow
"""

import os
import matplotlib.pyplot as plt
import tensorflow as tf

# Diretórios base do dataset
diretorio_dataset = os.path.join(os.getcwd(), 'cats_and_dogs_filtered')
diretorio_treino = os.path.join(diretorio_dataset, 'train')
diretorio_validacao = os.path.join(diretorio_dataset, 'validation')

# Conta quantas imagens há em cada classe de treino/validação (para informação)
quantidade_gatos_treino = len(os.listdir(os.path.join(diretorio_treino, 'cats')))
quantidade_cachorros_treino = len(os.listdir(os.path.join(diretorio_treino, 'dogs')))
quantidade_gatos_validacao = len(os.listdir(os.path.join(diretorio_validacao, 'cats')))
quantidade_cachorros_validacao = len(os.listdir(os.path.join(diretorio_validacao, 'dogs')))

print('Treino Gatos: %s' % quantidade_gatos_treino)
print('Treino Cachorros: %s' % quantidade_cachorros_treino)
print('Validação Gatos: %s' % quantidade_gatos_validacao)
print('Validação Cachorros: %s' % quantidade_cachorros_validacao)

# Parâmetros de imagem e treinamento
largura_imagem = 160
altura_imagem = 160
canais_imagem = 3
tamanho_canal_imagem = 255
tamanho_imagem = (largura_imagem, altura_imagem)
formato_imagem = tamanho_imagem + (canais_imagem,)

tamanho_lote = 32
epocas = 20
taxa_aprendizado = 0.0001

nomes_classes = ['gato', 'cachorro']

# Carrega os datasets de treino e validação já redimensionando as imagens
dataset_treino = tf.keras.preprocessing.image_dataset_from_directory(
    diretorio_treino,
    image_size=tamanho_imagem,
    batch_size=tamanho_lote,
    shuffle=True
)

dataset_validacao = tf.keras.preprocessing.image_dataset_from_directory(
    diretorio_validacao,
    image_size=tamanho_imagem,
    batch_size=tamanho_lote,
    shuffle=True
)

# Divide o dataset de validação em validação e teste (20% para teste)
cardinalidade_validacao = tf.data.experimental.cardinality(dataset_validacao)
lotes_teste = cardinalidade_validacao // 5

dataset_teste = dataset_validacao.take(lotes_teste)
dataset_validacao = dataset_validacao.skip(lotes_teste)

print('Cardinalidade Validação: %d' % tf.data.experimental.cardinality(dataset_validacao))
print('Cardinalidade Teste: %d' % tf.data.experimental.cardinality(dataset_teste))

# Otimização de performance usando prefetch
autotune = tf.data.AUTOTUNE
dataset_treino = dataset_treino.prefetch(buffer_size=autotune)
dataset_validacao = dataset_validacao.prefetch(buffer_size=autotune)
dataset_teste = dataset_teste.prefetch(buffer_size=autotune)

# Função para visualizar 9 imagens de um dataset
def plotar_dataset(dataset):
    plt.gcf().clear()
    plt.figure(figsize=(15, 15))
    for features, labels in dataset.take(1):
        for i in range(9):
            plt.subplot(3, 3, i + 1)
            plt.axis('off')
            plt.imshow(features[i].numpy().astype('uint8'))
            plt.title(nomes_classes[labels[i]])
    plt.show()

# Visualiza amostras do treino, validação e teste
plotar_dataset(dataset_treino)
plotar_dataset(dataset_validacao)
plotar_dataset(dataset_teste)

# Data augmentation para aumentar a variedade das imagens de treino
aumentacao_dados = tf.keras.models.Sequential([
    tf.keras.layers.experimental.preprocessing.RandomFlip('horizontal'),
    tf.keras.layers.experimental.preprocessing.RandomRotation(0.2),
    tf.keras.layers.experimental.preprocessing.RandomZoom(0.2)
])

# Função para visualizar o efeito do data augmentation em uma imagem de treino
def plotar_aumentacao_dados(dataset):
    plt.gcf().clear()
    plt.figure(figsize=(15, 15))
    for features, _ in dataset.take(1):
        feature = features[0]
        for i in range(9):
            feature_aumentada = aumentacao_dados(tf.expand_dims(feature, 0))
            plt.subplot(3, 3, i + 1)
            plt.axis('off')
            plt.imshow(feature_aumentada[0] / tamanho_canal_imagem)
    plt.show()

plotar_aumentacao_dados(dataset_treino)

# Normalização dos pixels para [-1, 1] (como espera o MobileNetV2)
reescala = tf.keras.layers.experimental.preprocessing.Rescaling(1. / (tamanho_canal_imagem / 2.), offset=-1, input_shape=formato_imagem)

# Instancia o MobileNetV2 pré-treinado como backbone (sem o topo)
modelo_transfer = tf.keras.applications.MobileNetV2(input_shape=formato_imagem, include_top=False, weights='imagenet')
modelo_transfer.trainable = False # Congela o backbone

# Mostra a arquitetura do modelo base
modelo_transfer.summary()

# Early stopping para evitar overfitting
early_stopping = tf.keras.callbacks.EarlyStopping(monitor='loss', patience=3)

# Modelo final com reescala, aumentação, backbone, pooling e camada final
modelo = tf.keras.models.Sequential([
    reescala,
    aumentacao_dados,
    modelo_transfer,
    tf.keras.layers.GlobalAveragePooling2D(),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(1, activation='sigmoid') # Saída binária: gato ou cachorro
])

# Compila o modelo
modelo.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=taxa_aprendizado),
    loss=tf.keras.losses.BinaryCrossentropy(),
    metrics=['accuracy']
)

modelo.summary()

# Treina o modelo
historico = modelo.fit(
    dataset_treino,
    validation_data=dataset_validacao,
    epochs=epocas,
    callbacks=[early_stopping]
)

# Função para plotar a acurácia e a loss do treino e validação ao longo das épocas
def plotar_historico():
    acuracia = historico.history['accuracy']
    val_acuracia = historico.history['val_accuracy']
    perda = historico.history['loss']
    val_perda = historico.history['val_loss']
    epocas_range = range(len(acuracia))
    plt.gcf().clear()
    plt.figure(figsize=(15, 8))
    plt.subplot(1, 2, 1)
    plt.title('Acurácia de Treino e Validação')
    plt.plot(epocas_range, acuracia, label='Treino')
    plt.plot(epocas_range, val_acuracia, label='Validação')
    plt.legend(loc='lower right')
    plt.subplot(1, 2, 2)
    plt.title('Loss de Treino e Validação')
    plt.plot(epocas_range, perda, label='Treino')
    plt.plot(epocas_range, val_perda, label='Validação')
    plt.legend(loc='lower right')
    plt.show()

# Plota o desempenho do modelo
plotar_historico()

# Avalia o modelo no conjunto de teste
perda_teste, acuracia_teste = modelo.evaluate(dataset_teste)
print('Loss Teste:     %s' % perda_teste)
print('Acurácia Teste: %s' % acuracia_teste)

# Função para mostrar 9 predições do modelo no conjunto de teste
def plotar_predicoes_teste(dataset):
    features, labels = next(dataset.as_numpy_iterator())
    predicoes = modelo.predict_on_batch(features).flatten()
    predicoes = tf.where(predicoes < 0.5, 0, 1)
    print('Rótulos:      %s' % labels)
    print('Predições: %s' % predicoes.numpy())
    plt.gcf().clear()
    plt.figure(figsize=(15, 15))
    for i in range(9):
        plt.subplot(3, 3, i + 1)
        plt.axis('off')
        plt.imshow(features[i].astype('uint8'))
        plt.title(nomes_classes[predicoes[i]])
    plt.show()

# Visualiza as predições no conjunto de teste
plotar_predicoes_teste(dataset_teste)

# Salva o modelo treinado em disco
modelo.save('modelo')

# Carrega o modelo salvo
modelo = tf.keras.models.load_model('modelo')

# Função para fazer predição com arquivo local
def predizer(imagem_arquivo):
    """
    Recebe o caminho de uma imagem, processa e faz a predição.
    Mostra no terminal o valor da predição e a classe prevista.
    """
    imagem = tf.keras.preprocessing.image.load_img(imagem_arquivo, target_size=tamanho_imagem)
    imagem = tf.keras.preprocessing.image.img_to_array(imagem)
    imagem = tf.expand_dims(imagem, 0)
    predicao = modelo.predict(imagem)[0][0]
    print('Predição: {0} | {1}'.format(predicao, ('gato' if predicao < 0.5 else 'cachorro')))

# Função para fazer predição com imagem de uma URL
def predizer_url(nome_imagem, origem_url):
    """
    Baixa uma imagem de uma URL, salva localmente, chama a função predizer e retorna o resultado.
    """
    imagem_arquivo = tf.keras.utils.get_file(nome_imagem, origin=origem_url)
    return predizer(imagem_arquivo)

# Exemplos de uso:
# predizer('chico.png')
# predizer_url('dog', 'https://www.sciencemag.org/sites/default/files/styles/article_main_large/public/main_puppies_1280p.jpg')