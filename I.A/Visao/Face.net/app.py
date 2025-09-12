from flask import Flask, request, jsonify
import pickle
from keras_facenet import FaceNet
from utils import preprocess_image, extract_embeddings, extrair_rosto

# Inicializa Flask
app = Flask(__name__)

# Carrega modelos uma vez
facenet = FaceNet().model
svm_model = pickle.load(open('modelo_svm.pkl', 'rb'))
label_encoder = pickle.load(open('label_encoder.pkl', 'rb'))


# Endpoint de reconhecimento
@app.route('/reconhecer', methods=['POST'])
def reconhecer():
    imagem = request.files['imagem']
    imagem_path = 'temp.jpg'
    imagem.save(imagem_path)

    face_pixels = extrair_rosto(imagem_path)
    if face_pixels is None:
        return jsonify({'erro': 'Nenhum rosto detectado'}), 400

    embedding = extract_embeddings(facenet, face_pixels)
    pred = svm_model.predict([embedding])[0]
    nome = label_encoder.inverse_transform([pred])[0]

    return jsonify({'nome': nome})


# Executa a API
if __name__ == '__main__':
    app.run(debug=True)
