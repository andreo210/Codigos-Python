from PIL import Image
from numpy import load, savez_compressed, asarray, concatenate
from os import listdir
from mtcnn.mtcnn import MTCNN
import os


# Função para extrair rosto
def extract_image(image_path):
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
        print(f"❌ Erro ao processar {image_path}: {e}")
        return None


# Função para carregar rostos de um diretório
def load_faces(directory):
    faces = []
    for filename in listdir(directory):
        path = os.path.join(directory, filename)
        face_array = extract_image(path)
        if face_array is not None:
            faces.append(face_array)
    return faces


# Função para montar novo dataset
def load_new_dataset(new_dir):
    x_new, y_new = [], []
    for subdir in listdir(new_dir):
        sub_path = os.path.join(new_dir, subdir)
        if not os.path.isdir(sub_path):
            continue
        class_faces = load_faces(sub_path)
        if class_faces:
            labels = [subdir] * len(class_faces)
            x_new.extend(class_faces)
            y_new.extend(labels)
            print(f"✅ {len(class_faces)} rostos adicionados da classe '{subdir}'")
        else:
            print(f"⚠️ Nenhum rosto válido na classe '{subdir}'")
    return asarray(x_new), asarray(y_new)


# Caminhos
dataset_path = 'C:/Users/andre/Documents/codigos pyton/Codigos-Python/I.A/Visao/Face.net/Indian-celeb-dataset.npz'
new_images_path = 'C:/Users/andre/Documents/codigos pyton/Codigos-Python/I.A/Visao/Face.net/NOVAS-IMAGENS/'

# Carrega dataset existente
data = load(dataset_path)
trainX_old, trainY_old = data['arr_0'], data['arr_1']

# Carrega novas imagens
trainX_new, trainY_new = load_new_dataset(new_images_path)

# Junta tudo
trainX_combined = concatenate((trainX_old, trainX_new))
trainY_combined = concatenate((trainY_old, trainY_new))

# Salva novo dataset
savez_compressed('C:/Users/andre/Documents/codigos pyton/Codigos-Python/I.A/Visao/Face.net/Indian-celeb-dataset-ATUALIZADO.npz',
                 trainX_combined, trainY_combined)

print(f"\n✅ Dataset atualizado com sucesso! Total de imagens: {trainX_combined.shape[0]}")
