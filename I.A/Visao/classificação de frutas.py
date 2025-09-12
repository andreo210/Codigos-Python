import kagglehub  # Importa a biblioteca kagglehub para baixar datasets do Kaggle.
import os  # Importa a biblioteca os para manipulação de arquivos e diretórios.
import shutil  # Importa a biblioteca shutil para copiar e mover arquivos/diretórios.
import matplotlib.pyplot as plt  # Importa a biblioteca matplotlib para visualização de gráficos e imagens.
import tensorflow as tf
import numpy as np  # Importa o NumPy para manipulação de arrays numéricos.

# Ignora avisos do tipo UserWarning para evitar poluição no console.
import warnings  
warnings.filterwarnings("ignore", category=UserWarning)  

print(tf.__file__)
print(tf.__version__)
# Baixar o dataset
caminho_origem = kagglehub.dataset_download("icebearogo/fruit-classification-dataset")  
# Faz o download do dataset "fruit-classification-dataset" do Kaggle.

# Caminho para onde você quer mover os arquivos
caminho_destino = "C:/Users/andre/Documents/codigos pyton/Codigos-Python/I.A/Visao/fruit-classification-dataset/Fruit_dataset"  
# Define o caminho onde os arquivos do dataset serão movidos.

# Criar a pasta de destino se não existir
os.makedirs(caminho_destino, exist_ok=True)  
# Cria o diretório de destino, se ele ainda não existir.

# Mover todos os arquivos do dataset para a nova pasta
for item in os.listdir(caminho_origem):  
    # Itera sobre todos os arquivos e diretórios no caminho de origem.
    origem = os.path.join(caminho_origem, item)  
    # Cria o caminho completo para o arquivo/diretório de origem.
    destino = os.path.join(caminho_destino, item)  
    # Cria o caminho completo para o arquivo/diretório de destino.
    if os.path.isdir(origem):  
        # Verifica se o item é um diretório.
        shutil.copytree(origem, destino, dirs_exist_ok=True)  
        # Copia o diretório e seu conteúdo para o destino.
    else:  
        # Caso contrário, o item é um arquivo.
        shutil.copy2(origem, destino)  
        # Copia o arquivo para o destino.

print("Arquivos movidos para:", caminho_destino)  
# Exibe uma mensagem indicando que os arquivos foram movidos.



# Carregar o dataset de frutas
train_data = tf.keras.utils.image_dataset_from_directory(
    directory="C:/Users/andre/Documents/codigos pyton/Codigos-Python/I.A/Visao/fruit-classification-dataset/Fruit_dataset/train1",  
    # Define o diretório do dataset de treino.
    labels="inferred",  
    # Infere automaticamente os rótulos com base nos nomes das pastas.
    label_mode='int',  
    # Define o formato dos rótulos como inteiros.
    batch_size=32,  
    # Define o tamanho do batch como 32.
    image_size=(256,256),  
    # Redimensiona as imagens para 256x256 pixels.
)

val_data = tf.keras.utils.image_dataset_from_directory(
    directory="C:/Users/andre/Documents/codigos pyton/Codigos-Python/I.A/Visao/fruit-classification-dataset/Fruit_dataset/val1",  
    # Define o diretório do dataset de validação.
    labels="inferred",  
    label_mode='int',  
    batch_size=32,  
    image_size=(256,256),  
)

test_data = tf.keras.utils.image_dataset_from_directory(
    directory="C:/Users/andre/Documents/codigos pyton/Codigos-Python/I.A/Visao/fruit-classification-dataset/Fruit_dataset/test1",  
    # Define o diretório do dataset de teste.
    labels="inferred",  
    label_mode='int',  
    batch_size=32,  
    image_size=(256,256),  
)

# Exibir os nomes das classes
nomes_classes = train_data.class_names  
# Obtém os nomes das classes do dataset de treino.
print(nomes_classes)  
# Exibe os nomes das classes.

# Função para plotar o dataset
def plotar_dataset(dataset):  
    # Define uma função para exibir imagens do dataset.
    plt.gcf().clear()  
    # Limpa a figura atual.
    plt.figure(figsize=(15, 15))  
    # Define o tamanho da figura.
    for features, labels in dataset.take(1):  
        # Itera sobre o primeiro batch do dataset.
        for i in range(9):  
            # Exibe as primeiras 9 imagens.
            plt.subplot(3, 3, i + 1)  
            # Cria um subplot 3x3.
            plt.axis('off')  
            # Remove os eixos.
            plt.imshow(features[i].numpy().astype('uint8'))  
            # Exibe a imagem.
            plt.title(nomes_classes[labels[i]])  
            # Define o título como o nome da classe correspondente.
    plt.show()  
    # Mostra o gráfico.

# Plotar o dataset de treino
plotar_dataset(train_data)  
# Chama a função para exibir imagens do dataset de treino.

# Criar o modelo de transferência
modelo_transfer = tf.keras.applications.ResNet50(weights="imagenet",include_top=False,input_shape=(256,256,3))  
# Carrega o modelo ResNet50 pré-treinado no ImageNet, sem a camada de saída.

modelo_transfer.trainable = False  
# Congela os pesos do modelo pré-treinado para evitar que sejam atualizados durante o treinamento.

# Criar o modelo final
modelo = tf.keras.Sequential([
    modelo_transfer,  
    # Adiciona o modelo pré-treinado como base.
    tf.keras.layers.GlobalAveragePooling2D(),  
    # Adiciona uma camada de pooling global.
    tf.keras.layers.Dense(128, activation='relu'),  
    # Adiciona uma camada densa com 128 neurônios e ativação ReLU.
    tf.keras.layers.Dense(len(nomes_classes), activation='softmax')  
    # Adiciona a camada de saída com softmax para classificação.
])

modelo.summary()  
# Exibe o resumo do modelo.

# Compilar o modelo
modelo.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),  
    # Define o otimizador Adam com taxa de aprendizado de 0.001.
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),  
    # Define a função de perda como entropia cruzada categórica.
    metrics=['accuracy']  
    # Define a métrica de avaliação como acurácia.
)   

# Treinar o modelo
modelo.fit(
    train_data,  
    # Usa o dataset de treino.
    validation_data=val_data,  
    # Usa o dataset de validação.
    epochs=10,  
    # Define o número de épocas como 10.
    batch_size=32  
    # Define o tamanho do batch como 32.
)

# Avaliar o modelo
loss, accuracy = modelo.evaluate(test_data)  
# Avalia o modelo no dataset de teste.
print(f"Loss: {loss}, Accuracy: {accuracy}")  
# Exibe a perda e a acurácia.

# Salvar o modelo
modelo.save("modelo_frutas.h5")  
# Salva o modelo treinado em um arquivo .h5.
print("Modelo salvo em /home/andreoa/code/datasets/frutas/modelo_frutas.h5")  
# Exibe uma mensagem indicando que o modelo foi salvo.

# Carregar o modelo
modelo_carregado = tf.keras.models.load_model("/home/andreoa/code/datasets/frutas/modelo_frutas.h5")  
# Carrega o modelo salvo.
print("Modelo carregado com sucesso.")  
# Exibe uma mensagem indicando que o modelo foi carregado.

# predição de uma imagem
def predizer_fruta(imagem_path):  
    # Define uma função para prever a classe de uma imagem.
    imagem = tf.keras.utils.load_img(imagem_path, target_size=(256, 256))  
    # Carrega a imagem e redimensiona para 256x256.
    imagem_array = tf.keras.utils.img_to_array(imagem)  
    # Converte a imagem para um array NumPy.
    imagem_array = np.expand_dims(imagem_array, axis=0)  
    # Adiciona uma dimensão para o batch.
    imagem_array = tf.keras.applications.resnet50.preprocess_input(imagem_array)  
    # Pré-processa a imagem para o ResNet50.

    predicao = modelo_carregado.predict(imagem_array)  
    # Faz a predição da classe da imagem.
    classe_predita = np.argmax(predicao, axis=1)[0]  
    # Obtém o índice da classe com maior probabilidade.    
    return nomes_classes[classe_predita]  
    # Retorna o nome da classe prevista.

# Exemplo de uso da função de predição
imagem_exemplo = "/home/andreoa/code/datasets/frutas/Fruit_dataset/test1/banana/banana_100.jpg"  
# Define o caminho de uma imagem de exemplo.
fruta_predita = predizer_fruta(imagem_exemplo)  
# Faz a predição da classe da imagem.
print(f"A fruta prevista para a imagem {imagem_exemplo} é: {fruta_predita}")  
# Exibe o nome da fruta prevista.