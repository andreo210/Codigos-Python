import tensorflow as tf
import numpy as np  # Importa o NumPy para manipulação de arrays numéricos.

# Carregar o modelo
modelo_carregado = tf.keras.models.load_model("C:/Users/andre/Documents/codigos pyton/Codigos-Python/I.A/Visao/modelo_frutas.h5")  
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
imagem_exemplo = "banana_100.jpg"  
# Define o caminho de uma imagem de exemplo.
fruta_predita = predizer_fruta(imagem_exemplo)  
# Faz a predição da classe da imagem.
print(f"A fruta prevista para a imagem {imagem_exemplo} é: {fruta_predita}")  
# Exibe o nome da fruta prevista. tf.config.list_physical_devices('GPU'))
