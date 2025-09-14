from keras_facenet import FaceNet
from utils.dataset_builder import salvar_dataset
from utils.embedding_utils import gerar_embeddings
from train.train_svm import treinar_svm


from utils.gpu_manager import configurar_gpu_segura
configurar_gpu_segura()


# Caminhos
dataset_path = 'C:/Users/andre/Documents/codigos pyton/Codigos-Python/I.A/Visao/Face.net SVM/data/Indian-celebrities/'
dataset_npz = 'C:/Users/andre/Documents/codigos pyton/Codigos-Python/I.A/Visao/Face.net SVM/data/Indian-celeb-dataset.npz'
embedding_npz = 'C:/Users/andre/Documents/codigos pyton/Codigos-Python/I.A/Visao/Face.net SVM/data/Indian-celeb-embeddings.npz'
model_path = 'C:/Users/andre/Documents/codigos pyton/Codigos-Python/I.A/Visao/Face.net SVM/models/modelo_svm.pkl'
encoder_path = 'C:/Users/andre/Documents/codigos pyton/Codigos-Python/I.A/Visao/Face.net SVM/models/label_encoder.pkl'

# Executa pipeline
salvar_dataset(dataset_path, dataset_npz)
embedder = FaceNet()
gerar_embeddings(embedder.model, dataset_npz, embedding_npz)
treinar_svm(embedding_npz, model_path, encoder_path)
print("✅ Pipeline concluída com sucesso!")