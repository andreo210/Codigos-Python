from numpy import load
from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder
import pickle


def treinar_svm(embedding_path, model_path, encoder_path):
    data = load(embedding_path)
    X, y = data['arr_0'], data['arr_1']
    encoder = LabelEncoder()
    y_encoded = encoder.fit_transform(y)

    modelo = SVC(kernel='linear', probability=True)
    modelo.fit(X, y_encoded)

    with open(model_path, 'wb') as f:
        pickle.dump(modelo, f)
    with open(encoder_path, 'wb') as f:
        pickle.dump(encoder, f)

    print("✅ Modelo SVM e codificador salvos com sucesso!")
