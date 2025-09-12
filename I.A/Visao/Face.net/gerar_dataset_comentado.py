from PIL import Image  # Biblioteca para abrir e manipular imagens
from numpy import savez_compressed, asarray  # Funções para salvar arrays e converter imagens em arrays
from os import listdir  # Para listar arquivos em diretórios
from mtcnn.mtcnn import MTCNN  # Detector de rostos baseado em rede neural
import os  # Manipulação de caminhos e diretórios


# Função para extrair o rosto de uma imagem
def extrair_rosto(image_path):
    try:
        # Abre a imagem e converte para RGB
        img = Image.open(image_path).convert('RGB')
        pixels = asarray(img)  # Converte a imagem em array NumPy

        detector = MTCNN()  # Inicializa o detector de rostos
        faces = detector.detect_faces(pixels)  # Detecta rostos na imagem

        if not faces:
            print(f"⚠️ Nenhum rosto detectado em: {image_path}")
            return None

        # Extrai coordenadas da caixa delimitadora do rosto
        x1, y1, w, h = faces[0]['box']
        x1, y1 = abs(x1), abs(y1)
        x2, y2 = x1 + w, y1 + h

        # Recorta o rosto e redimensiona para 160x160 pixels
        face = pixels[y1:y2, x1:x2]
        image_face = Image.fromarray(face, 'RGB').resize((160, 160))
        return asarray(image_face)  # Retorna o rosto como array

    except Exception as e:
        print(f"Erro ao processar {image_path}: {e}")
        return None


# Função para carregar rostos de um diretório
def load_faces(directory):
    faces = []
    for filename in listdir(directory):  # Itera sobre os arquivos do diretório
        path = os.path.join(directory, filename)
        face_array = extrair_rosto(path)  # Extrai o rosto da imagem
        if face_array is not None:
            faces.append(face_array)  # Adiciona à lista se o rosto for válido
    return faces


# Função para montar o dataset completo
def load_dataset(root_dir):
    x, y = [], []  # Listas para imagens e rótulos
    class_count = 0  # Contador de classes

    for subdir in listdir(root_dir):  # Itera sobre as subpastas (classes)
        sub_path = os.path.join(root_dir, subdir)
        if not os.path.isdir(sub_path):
            continue  # Ignora arquivos que não são diretórios

        class_faces = load_faces(sub_path)  # Carrega rostos da subpasta
        if class_faces:
            labels = [subdir] * len(class_faces)  # Cria rótulos para cada rosto
            x.extend(class_faces)
            y.extend(labels)
            class_count += 1
            print(f"{class_count}.  {len(class_faces)} rostos encontrados na classe '{subdir}'")
        else:
            print(f"{class_count + 1}. ⚠️ Nenhum rosto válido na classe '{subdir}'")
    return asarray(x), asarray(y)  # Retorna arrays de imagens e rótulos


# Caminho do diretório de imagens organizadas por pessoa
dataset_path = 'C:/Users/andre/Documents/codigos pyton/Codigos-Python/I.A/Visao/Face.net/Indian-celebrities/'

# Carrega o dataset completo
trainX, trainY = load_dataset(dataset_path)

# Verifica se há rostos e salva o dataset em formato compactado
if len(trainX) > 0:
    savez_compressed(
        'C:/Users/andre/Documents/codigos pyton/Codigos-Python/I.A/Visao/Face.net/Indian-celeb-dataset.npz',
        trainX, trainY
    )
    print(f"\n✅ Dataset salvo com sucesso! Total de imagens: {trainX.shape[0]}")
else:
    print("\n❌ Nenhum rosto foi extraído. Verifique o diretório e as imagens.")
