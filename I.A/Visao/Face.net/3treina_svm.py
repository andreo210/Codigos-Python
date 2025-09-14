from numpy import load
from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder
import pickle

# Carrega os embeddings
data = load('C:/Users/andre/Documents/codigos pyton/Codigos-Python/I.A/Visao/Face.net/Indian-celeb-embeddings.npz')
embeddings, rotulos = data['arr_0'], data['arr_1']

# Codifica os rótulos
encoder = LabelEncoder()
rotulos_codificados = encoder.fit_transform(rotulos)

# Treina o SVM
modelo_svm = SVC(kernel='linear', probability=True)
modelo_svm.fit(embeddings, rotulos_codificados)

# Salva o modelo e o encoder
with open('modelo_svm.pkl', 'wb') as f:
    pickle.dump(modelo_svm, f)
with open('label_encoder.pkl', 'wb') as f:
    pickle.dump(encoder, f)

print("✅ Modelo SVM e codificador salvos com sucesso!")
