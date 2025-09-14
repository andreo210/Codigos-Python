from keras_facenet import FaceNet
from sklearn.preprocessing import LabelEncoder
import numpy as np
import pickle

# 🔒 Carrega o modelo uma única vez
facenet_model = FaceNet().model

# 🔒 Carrega o SVM e o encoder uma vez
with open('models/modelo_svm.pkl', 'rb') as f:
    modelo_svm = pickle.load(f)
with open('models/label_encoder.pkl', 'rb') as f:
    encoder = pickle.load(f)
 

def extrair_embedding(face):
    # ✅ Redimensiona e normaliza
    face = np.asarray(face).astype('float32')
    face = face.reshape(1, 160, 160, 3)
    return facenet_model.predict(face)[0]


def reconhecer(face):
    embedding = extrair_embedding(face)
    embedding = embedding.reshape(1, -1)
    pred = modelo_svm.predict(embedding)
    prob = modelo_svm.predict_proba(embedding)
    nome = encoder.inverse_transform(pred)[0]
    confianca = np.max(prob)
    return nome, confianca
