from matplotlib import pyplot as plt
from PIL import Image
from numpy import asarray, expand_dims, load
from mtcnn.mtcnn import MTCNN
from keras_facenet import FaceNet
from sklearn.preprocessing import LabelEncoder, Normalizer
from sklearn.svm import SVC


def extract_image(image_path):
    img = Image.open(image_path).convert('RGB')
    pixels = asarray(img)
    detector = MTCNN()
    faces = detector.detect_faces(pixels)
    if not faces:
        raise Exception("Nenhum rosto detectado.")
    x1, y1, w, h = faces[0]['box']
    x1, y1 = abs(x1), abs(y1)
    x2, y2 = x1 + w, y1 + h
    face = pixels[y1:y2, x1:x2]
    face_image = Image.fromarray(face).resize((160, 160))
    return asarray(face_image)


def extract_embeddings(model, face_pixels):
    face_pixels = face_pixels.astype('float32')
    mean, std = face_pixels.mean(), face_pixels.std()
    face_pixels = (face_pixels - mean) / std
    samples = expand_dims(face_pixels, axis=0)
    yhat = model.predict(samples)
    return yhat[0]


def reconheceRosto(imagem_path, dataset_path, embeddings_path):
    # Carrega imagem e extrai rosto
    face = extract_image(imagem_path)
    testx = face.reshape(-1, 160, 160, 3)

    # Inicializa modelo FaceNet
    embedder = FaceNet()
    model_facenet = embedder.model

    # Extrai embedding da imagem de teste
    new_testx = [extract_embeddings(model_facenet, pixels) for pixels in testx]
    new_testx = asarray(new_testx)

    # Carrega dados de treino
    data_raw = load(dataset_path)
    train_x, train_y = data_raw['arr_0'], data_raw['arr_1']

    data_embed = load(embeddings_path)
    trainx, trainy = data_embed['arr_0'], data_embed['arr_1']

    # Normaliza embeddings
    normalizador = Normalizer(norm='l2')
    trainx = normalizador.transform(trainx)
    new_testx = normalizador.transform(new_testx)

    # Codifica rótulos
    encoder = LabelEncoder()
    encoder.fit(trainy)
    trainy_enc = encoder.transform(trainy)

    # Treina SVM
    modelo_svm = SVC(kernel='linear', probability=True)
    modelo_svm.fit(trainx, trainy_enc)

    # Predição
    predict_test = modelo_svm.predict(new_testx)
    prob = modelo_svm.predict_proba(new_testx)
    confianca = max(prob[0])
    nome = encoder.inverse_transform(predict_test)[0]

    # Localiza imagem correspondente
    trainy_list = list(trainy)
    val = trainy_list.index(nome)

    # Exibe resultado
    plt.subplot(1, 2, 1)
    plt.imshow(face)
    plt.title(f"Entrada: {nome}")
    plt.xlabel("Imagem de Entrada")

    plt.subplot(1, 2, 2)
    plt.imshow(train_x[val])
    plt.title(f"Reconhecido: {nome}")
    plt.xlabel(f"Confiança: {confianca:.2f}")

    plt.show()

    print(f"Reconhecimento concluído: {nome} com confiança de {confianca:.2f}")
