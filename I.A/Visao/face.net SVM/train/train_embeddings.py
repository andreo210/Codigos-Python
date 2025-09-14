from numpy import load, asarray, savez_compressed
from keras_facenet import FaceNet
from utils.embedding_utils import extract_embeddings
from utils.gpu_manager import configurar_gpu_segura

#configurar_gpu_segura()
# Caminhos dos arquivos
dataset_path = 'data/Indian-celeb-dataset.npz'         # Dataset com rostos
embedding_output_path = 'data/Indian-celeb-embeddings.npz'  # Onde salvar os embeddings

# Carrega o dataset de rostos
data = load(dataset_path)
faces, labels = data['arr_0'], data['arr_1']

# Inicializa o modelo FaceNet
embedder = FaceNet()
model = embedder.model

# Extrai os embeddings de cada rosto
embeddings = asarray([extract_embeddings(model, face) for face in faces])

# Salva os embeddings e os rótulos
savez_compressed(embedding_output_path, embeddings, labels)
print(f"✅ Embeddings salvos com sucesso! Total: {embeddings.shape[0]}")
