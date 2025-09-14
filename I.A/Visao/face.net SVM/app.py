from utils.gpu_manager import configurar_gpu_segura
configurar_gpu_segura(modo='growth')

from flask import Flask, request, jsonify
import pickle
from utils.face_extraction import extrair_rosto
from utils.embedding_utils import extract_embeddings
import os
from werkzeug.utils import secure_filename
import subprocess
import tensorflow as tf

# Inicializa a aplicação Flask
app = Flask(__name__)

# Diretórios e caminhos
BASE_DIR = 'C:/Users/andre/Documents/codigos pyton/Codigos-Python/I.A/Visao/Face.net SVM'
NOVOS_ROSTOS_DIR = os.path.join(BASE_DIR, 'data/novos_rostos')
MODEL_PATH = os.path.join(BASE_DIR, 'models/modelo_svm.pkl')
ENCODER_PATH = os.path.join(BASE_DIR, 'models/label_encoder.pkl')
PIPELINE_SCRIPT = os.path.join(BASE_DIR, 'pipeline_incremental.py')

# Carrega apenas o SVM e o encoder (não usam GPU)
from keras_facenet import FaceNet
from mtcnn.mtcnn import MTCNN


# ✅ Carregados uma vez na inicialização
facenet_model = FaceNet().model
detector = MTCNN()

with open('models/modelo_svm.pkl', 'rb') as f:
    svm_model = pickle.load(f)
with open('models/label_encoder.pkl', 'rb') as f:
    label_encoder = pickle.load(f)

"""
# Endpoint: reconhecimento facial
@app.route('/reconhecer', methods=['POST'])
def reconhecer():
    import tensorflow as tf
    tf.keras.backend.clear_session()
    imagem = request.files.get('imagem')
    if not imagem:
        return jsonify({'erro': 'Nenhuma imagem enviada'}), 400

    imagem_path = 'temp.jpg'
    imagem.save(imagem_path)

    # 🔄 Inicializa os modelos apenas quando necessário
    from keras_facenet import FaceNet
    from mtcnn.mtcnn import MTCNN
    facenet_model = FaceNet().model
    detector = MTCNN()

    face_pixels = extrair_rosto(imagem_path, detector)
    if face_pixels is None:
        return jsonify({'erro': 'Nenhum rosto detectado'}), 400

    embedding = extract_embeddings(facenet_model, face_pixels)
    pred = svm_model.predict([embedding])[0]
    nome = label_encoder.inverse_transform([pred])[0]

    return jsonify({'nome': nome})
"""


@app.route('/reconhecer', methods=['POST'])
def reconhecer():
    imagem = request.files.get('imagem')
    if not imagem:
        return jsonify({'erro': 'Nenhuma imagem enviada'}), 400

    from PIL import Image
    img = Image.open(imagem.stream).convert('RGB')
    img = img.resize((640, 480))

    face_pixels = extrair_rosto(img, detector)
    if face_pixels is None:
        return jsonify({'erro': 'Nenhum rosto detectado'}), 400

    embedding = extract_embeddings(facenet_model, face_pixels)
    pred = svm_model.predict([embedding])[0]
    nome = label_encoder.inverse_transform([pred])[0]

    return jsonify({'nome': nome})


# Endpoint: incrementar novo rosto
@app.route('/incrementar', methods=['POST'])
def incrementar():
    nome = request.form.get('nome')
    imagens = request.files.getlist('imagens')

    if not nome or not imagens:
        return jsonify({'erro': 'Envie o nome e pelo menos uma imagem'}), 400

    pasta_destino = os.path.join(NOVOS_ROSTOS_DIR, secure_filename(nome))
    os.makedirs(pasta_destino, exist_ok=True)

    for img in imagens:
        caminho = os.path.join(pasta_destino, secure_filename(img.filename))
        img.save(caminho)

    try:
        subprocess.run(['python', PIPELINE_SCRIPT], check=True)
        return jsonify({'mensagem': f'✅ Imagens adicionadas e modelo atualizado para {nome}'}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({'erro': f'Falha ao atualizar o modelo: {str(e)}'}), 500


# Endpoint: reiniciar TensorFlow e recarregar modelos
@app.route('/reiniciar-tf', methods=['POST'])
def reiniciar_tensorflow():
    global svm_model, label_encoder

    try:
        tf.keras.backend.clear_session()
        configurar_gpu_segura()

        svm_model = pickle.load(open(MODEL_PATH, 'rb'))
        label_encoder = pickle.load(open(ENCODER_PATH, 'rb'))

        return jsonify({'mensagem': '✅ TensorFlow reiniciado e modelos recarregados'}), 200
    except Exception as e:
        return jsonify({'erro': f'Falha ao reiniciar TensorFlow: {str(e)}'}), 500


@app.route('/excluir-pessoa', methods=['POST'])
def excluir_pessoa():
    nome = request.form.get('nome')
    if not nome:
        return jsonify({'erro': 'Nome da pessoa não informado'}), 400

    import shutil
    from numpy import load, asarray, savez_compressed
    import pickle
    from sklearn.svm import SVC
    from sklearn.preprocessing import LabelEncoder

    # 1️⃣ Remove pasta de imagens
    pasta = os.path.join(NOVOS_ROSTOS_DIR, secure_filename(nome))
    if os.path.exists(pasta):
        shutil.rmtree(pasta)

    # 2️⃣ Remove do dataset consolidado
    try:
        dataset_path = os.path.join(BASE_DIR, 'data/Indian-celeb-dataset.npz')
        data = load(dataset_path)
        faces, labels = data['arr_0'], data['arr_1']

        novas_faces = [f for f, l in zip(faces, labels) if l != nome]
        novas_labels = [l for l in labels if l != nome]

        if len(novas_faces) == 0:
            return jsonify({'erro': 'Remoção resultaria em dataset vazio'}), 400

        savez_compressed(dataset_path, asarray(novas_faces), asarray(novas_labels))
    except Exception as e:
        return jsonify({'erro': f'Erro ao atualizar dataset: {str(e)}'}), 500

    # 3️⃣ Remove dos embeddings
    try:
        embeddings_path = os.path.join(BASE_DIR, 'data/Indian-celeb-embeddings.npz')
        data = load(embeddings_path)
        embeddings, emb_labels = data['arr_0'], data['arr_1']

        novos_embeddings = [e for e, l in zip(embeddings, emb_labels) if l != nome]
        novos_labels = [l for l in emb_labels if l != nome]

        if len(novos_embeddings) == 0:
            return jsonify({'erro': 'Remoção resultaria em embeddings vazios'}), 400

        savez_compressed(embeddings_path, asarray(novos_embeddings), asarray(novos_labels))
    except Exception as e:
        return jsonify({'erro': f'Erro ao atualizar embeddings: {str(e)}'}), 500

    # 4️⃣ Reentreina o modelo SVM
    try:
        encoder = LabelEncoder()
        y_encoded = encoder.fit_transform(novos_labels)
        modelo_svm = SVC(kernel='linear', probability=True)
        modelo_svm.fit(novos_embeddings, y_encoded)

        with open(MODEL_PATH, 'wb') as f:
            pickle.dump(modelo_svm, f)
        with open(ENCODER_PATH, 'wb') as f:
            pickle.dump(encoder, f)
    except Exception as e:
        return jsonify({'erro': f'Erro ao reentreinar modelo: {str(e)}'}), 500

    return jsonify({'mensagem': f'✅ Pessoa {nome} removida e modelo atualizado com sucesso'}), 200


@app.route('/status-pessoa', methods=['GET'])
def status_pessoa():
    nome = request.args.get('nome')
    if not nome:
        return jsonify({'erro': 'Nome da pessoa não informado'}), 400

    import os
    from numpy import load
    from datetime import datetime

    status = {'nome': nome}

    # 📁 Verifica imagens em novos_rostos
    pasta = os.path.join(NOVOS_ROSTOS_DIR, secure_filename(nome))
    if os.path.exists(pasta):
        arquivos = os.listdir(pasta)
        status['imagens_novas'] = len(arquivos)
        status['ultima_modificacao'] = datetime.fromtimestamp(os.path.getmtime(pasta)).strftime('%d/%m/%Y %H:%M')
    else:
        status['imagens_novas'] = 0
        status['ultima_modificacao'] = 'n/a'

    # 📦 Verifica exemplos no dataset consolidado
    try:
        dataset_path = os.path.join(BASE_DIR, 'data/Indian-celeb-dataset.npz')
        data = load(dataset_path)
        labels = data['arr_1']
        status['exemplos_dataset'] = sum(1 for label in labels if label == nome)        
    except:
        status['exemplos_dataset'] = 'erro'

    # 🧠 Verifica embeddings
    try:
        embeddings_path = os.path.join(BASE_DIR, 'data/Indian-celeb-embeddings.npz')
        data = load(embeddings_path)
        labels = data['arr_1']
        status['embeddings'] = sum(1 for label in labels if label == nome)
    except:
        status['embeddings'] = 'erro'

    return jsonify(status)


@app.route('/upload-pastas', methods=['POST'])
def upload_pastas():
    from werkzeug.utils import secure_filename
    from PIL import Image
    import os

    arquivos = request.files
    if not arquivos:
        return jsonify({'erro': 'Nenhum arquivo enviado'}), 400

    salvos = {}

    for chave in arquivos:
        if not chave.startswith('pastas[') or not chave.endswith(']'):
            continue

        nome = chave[7:-1]  # extrai o nome entre colchetes
        nome_seguro = secure_filename(nome)
        pasta_destino = os.path.join(NOVOS_ROSTOS_DIR, nome_seguro)
        os.makedirs(pasta_destino, exist_ok=True)

        imagens = request.files.getlist(chave)
        salvos[nome] = []

        for imagem in imagens:
            nome_arquivo = secure_filename(imagem.filename)
            caminho = os.path.join(pasta_destino, nome_arquivo)

            try:
                # 🧠 Redimensiona antes de salvar
                img = Image.open(imagem.stream).convert('RGB')
                img = img.resize((640, 480))
                img.save(caminho)
                salvos[nome].append(nome_arquivo)
            except Exception as e:
                print(f"❌ Erro ao processar {nome_arquivo}: {e}")

    return jsonify({'mensagem': '✅ Pastas enviadas com sucesso', 'detalhes': salvos}), 200


@app.route('/atualizar-dataset', methods=['POST'])
def atualizar_dataset():
    import subprocess
    import os

    script_path = os.path.join(BASE_DIR, 'pipeline_incremental.py')

    try:
        subprocess.run(['python', script_path], check=True)
        return jsonify({'mensagem': '✅ Dataset e modelo atualizados com sucesso via pipeline_incremental'}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({'erro': f'Falha ao executar pipeline: {str(e)}'}), 500


# Execução segura
if __name__ == '__main__':
    app.run(debug=False, use_reloader=False, threaded=False)
