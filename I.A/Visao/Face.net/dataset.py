from PIL import Image
from numpy import savez_compressed, asarray
from os import listdir
from mtcnn.mtcnn import MTCNN
import os


# Função para extrair o rosto de uma imagem
def extrair_rosto(image_path):
    try:
        img = Image.open(image_path).convert('RGB')
        pixels = asarray(img)
        detector = MTCNN()
        faces = detector.detect_faces(pixels)

        if not faces:
            print(f"⚠️ Nenhum rosto detectado em: {image_path}")
            return None

        x1, y1, w, h = faces[0]['box']
        x1, y1 = abs(x1), abs(y1)
        x2, y2 = x1 + w, y1 + h
        face = pixels[y1:y2, x1:x2]
        image_face = Image.fromarray(face, 'RGB').resize((160, 160))
        return asarray(image_face)

    except Exception as e:
        print(f"Erro ao processar {image_path}: {e}")
        return None


# Função para carregar rostos de um diretório
def load_faces(directory):
    faces = []
    for filename in listdir(directory):
        path = os.path.join(directory, filename)
        face_array = extrair_rosto(path)
        if face_array is not None:
            faces.append(face_array)
    return faces


# Função para montar o dataset
def load_dataset(root_dir):
    x, y = [], []
    class_count = 0
    for subdir in listdir(root_dir):
        sub_path = os.path.join(root_dir, subdir)
        if not os.path.isdir(sub_path):
            continue
        class_faces = load_faces(sub_path)
        if class_faces:
            labels = [subdir] * len(class_faces)
            x.extend(class_faces)
            y.extend(labels)
            class_count += 1
            print(f"{class_count}.  {len(class_faces)} rostos encontrados na classe '{subdir}'")
        else:
            print(f"{class_count + 1}. ⚠️ Nenhum rosto válido na classe '{subdir}'")
    return asarray(x), asarray(y)


# Caminho do diretório de imagens
dataset_path = 'C:/Users/andre/Documents/codigos pyton/Codigos-Python/I.A/Visao/Face.net/Indian-celebrities/'

# Carrega o dataset
trainX, trainY = load_dataset(dataset_path)

# Verifica e salva
if len(trainX) > 0:
    savez_compressed('C:/Users/andre/Documents/codigos pyton/Codigos-Python/I.A/Visao/Face.net/Indian-celeb-dataset.npz', trainX, trainY)
    print(f"\n✅ Dataset salvo com sucesso! Total de imagens: {trainX.shape[0]}")
else:
    print("\n Nenhum rosto foi extraído. Verifique o diretório e as imagens.")