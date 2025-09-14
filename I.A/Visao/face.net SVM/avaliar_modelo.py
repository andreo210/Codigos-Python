from numpy import load
import pickle
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

# Carrega embeddings e rótulos
data = load('C:/Users/andre/Documents/codigos pyton/Codigos-Python/I.A/Visao/Face.net SVM/data/Indian-celeb-embeddings.npz')
X, y = data['arr_0'], data['arr_1']

# Carrega modelo SVM e encoder
with open('C:/Users/andre/Documents/codigos pyton/Codigos-Python/I.A/Visao/Face.net SVM/models/modelo_svm.pkl', 'rb') as f:
    modelo_svm = pickle.load(f)
with open('C:/Users/andre/Documents/codigos pyton/Codigos-Python/I.A/Visao/Face.net SVM/models/label_encoder.pkl', 'rb') as f:
    encoder = pickle.load(f)

# Codifica os rótulos reais para números
y_encoded = encoder.transform(y)

# Faz predições
y_pred = modelo_svm.predict(X)

# Avalia acurácia
acuracia = accuracy_score(y_encoded, y_pred)
print(f"\n✅ Acurácia do modelo treinado: {acuracia:.2%}")

# Matriz de confusão
cm = confusion_matrix(y_encoded, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=encoder.classes_)
disp.plot(cmap='Blues', xticks_rotation=45)
plt.title("Matriz de Confusão")
plt.tight_layout()
plt.show()
