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
def extrair_rosto(imagem_path):
    img = Image.open(imagem_path).convert('RGB')
    pixels = np.asarray(img)
    faces = detector.detect_faces(pixels)

    if not faces:
        return None

    x1, y1, w, h = faces[0]['box']
    x1, y1 = abs(x1), abs(y1)
    x2, y2 = x1 + w, y1 + h
    face = pixels[y1:y2, x1:x2]
    face_image = Image.fromarray(face).resize((160, 160))
    return np.asarray(face_image)