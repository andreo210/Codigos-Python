import numpy as np
from PIL import Image
from mtcnn.mtcnn import MTCNN
from PIL import Image
import numpy as np

# carrega modlo
detector = MTCNN()


def preprocess_image(image_path):
    img = Image.open(image_path).convert('RGB').resize((160, 160))
    return np.asarray(img)


def extract_embeddings(model, face_pixels):
    face_pixels = face_pixels.astype('float32')
    mean, std = face_pixels.mean(), face_pixels.std()
    face_pixels = (face_pixels - mean) / std
    samples = np.expand_dims(face_pixels, axis=0)
    return model.predict(samples)[0]


# Função para extrair rosto da imagem
def extrair_rosto(image_path):
    try:
        # Abre a imagem e converte para RGB
        img = Image.open(image_path).convert('RGB')
        pixels = np.asarray(img)  # Converte a imagem em array NumPy

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
        return np.asarray(image_face)  # Retorna o rosto como array

    except Exception as e:
        print(f"Erro ao processar {image_path}: {e}")
        return None