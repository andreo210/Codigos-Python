import os
import pickle
from numpy import load, concatenate, asarray, savez_compressed
from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder
from datetime import datetime
import tensorflow as tf

# 🔧 Limpa sessão e configura GPU
tf.keras.backend.clear_session()
from utils.gpu_manager import configurar_gpu_segura
configurar_gpu_segura(modo='growth')  # ou 'limit', se preferir


# 🕒 Logger simples
def log(msg):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}")


# 📁 Caminhos
BASE_DIR = 'C:/Users/andre/Documents/codigos pyton/Codigos-Python/I.A/Visao/Face.net SVM'
NOVOS_ROSTOS_DIR = os.path.join(BASE_DIR, 'data/novos_rostos')
DATASET_PATH = os.path.join(BASE_DIR, 'data/Indian-celeb-dataset.npz')
EMBEDDINGS_PATH = os.path.join(BASE_DIR, 'data/Indian-celeb-embeddings.npz')
MODEL_PATH = os.path.join(BASE_DIR, 'models/modelo_svm.pkl')
ENCODER_PATH = os.path.join(BASE_DIR, 'models/label_encoder.pkl')

# 🔍 Verifica se há novas imagens
if not os.listdir(NOVOS_ROSTOS_DIR):
    log("⚠️ Nenhuma imagem nova encontrada. Encerrando.")
    exit(2)

# 🧠 Carrega dados antigos
try:
    data_antiga = load(DATASET_PATH)
    x_antigo, y_antigo = data_antiga['arr_0'], data_antiga['arr_1']
    log(f"✅ Dataset antigo carregado: {x_antigo.shape[0]} imagens")
except Exception as e:
    log(f"❌ Erro ao carregar dataset antigo: {e}")
    exit(2)

# 📥 Carrega novos rostos
try:
    from utils.dataset_builder import load_dataset
    x_novo, y_novo = load_dataset(NOVOS_ROSTOS_DIR)
    if len(x_novo) == 0:
        log("⚠️ Nenhum rosto válido nas novas imagens.")
        exit(2)
    log(f"✅ Novos rostos carregados: {len(x_novo)} imagens")
except Exception as e:
    log(f"❌ Erro ao carregar novos rostos: {e}")
    exit(2)

# 🔗 Junta tudo
try:
    x_final = concatenate((x_antigo, x_novo))
    y_final = concatenate((y_antigo, y_novo))
    savez_compressed(DATASET_PATH, x_final, y_final)
    log(f"✅ Dataset atualizado: {x_final.shape[0]} imagens")
except Exception as e:
    log(f"❌ Erro ao atualizar dataset: {e}")
    exit(2)

# 🔄 Gera embeddings
try:
    from keras_facenet import FaceNet
    from utils.embedding_utils import extract_embeddings
    facenet = FaceNet().model
    embeddings_final = asarray([extract_embeddings(facenet, face) for face in x_final])
    savez_compressed(EMBEDDINGS_PATH, embeddings_final, y_final)
    log(f"✅ Embeddings gerados: {embeddings_final.shape[0]} vetores")
except Exception as e:
    log(f"❌ Erro ao gerar embeddings: {e}")
    exit(2)

# 🧠 Treina SVM
try:
    encoder = LabelEncoder()
    y_encoded = encoder.fit_transform(y_final)
    modelo_svm = SVC(kernel='linear', probability=True)
    modelo_svm.fit(embeddings_final, y_encoded)
    with open(MODEL_PATH, 'wb') as f:
        pickle.dump(modelo_svm, f)
    with open(ENCODER_PATH, 'wb') as f:
        pickle.dump(encoder, f)
    log("✅ Modelo SVM treinado e salvo com sucesso")
except Exception as e:
    log(f"❌ Erro ao treinar ou salvar modelo: {e}")
    exit(2)

# 🧹 Limpa pasta de novos rostos
try:
    for pessoa in os.listdir(NOVOS_ROSTOS_DIR):
        subpasta = os.path.join(NOVOS_ROSTOS_DIR, pessoa)
        for arquivo in os.listdir(subpasta):
            os.remove(os.path.join(subpasta, arquivo))
        os.rmdir(subpasta)
    log("🧼 Pasta de novos rostos limpa")
except Exception as e:
    log(f"⚠️ Erro ao limpar pasta: {e}")
