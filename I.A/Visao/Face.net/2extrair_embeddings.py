from numpy import asarray, expand_dims, load, savez_compressed
from keras_facenet import FaceNet


# Função para extrair embeddings
def extract_embeddings(model, face_pixels):
    face_pixels = face_pixels.astype('float32')
    mean, std = face_pixels.mean(), face_pixels.std()
    face_pixels = (face_pixels - mean) / std
    samples = expand_dims(face_pixels, axis=0)
    yhat = model.predict(samples)
    return yhat[0]


# Carrega o dataset de rostos
data = load('C:/Users/andre/Documents/codigos pyton/Codigos-Python/I.A/Visao/Face.net/Indian-celeb-dataset.npz')
trainx, trainy = data['arr_0'], data['arr_1']


# Inicializa o modelo FaceNet
embedder = FaceNet()
model = embedder.model


# Extrai os embeddings(transforma as imagens em vetores)
new_trainx = [extract_embeddings(model, face) for face in trainx]
new_trainx = asarray(new_trainx)


# Salva os embeddings
savez_compressed('C:/Users/andre/Documents/codigos pyton/Codigos-Python/I.A/Visao/Face.net/Indian-celeb-embeddings.npz', new_trainx, trainy)
print("✅ Embeddings salvos com sucesso!")