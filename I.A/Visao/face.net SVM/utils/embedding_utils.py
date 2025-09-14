from numpy import expand_dims, asarray, savez_compressed


def extract_embeddings(model, face_pixels):
    face_pixels = face_pixels.astype('float32')
    #face_pixels = face_pixels.reshape(1, 160, 160, 3)
    face_pixels = (face_pixels - face_pixels.mean()) / face_pixels.std()
    samples = expand_dims(face_pixels, axis=0)
    return model.predict(samples)[0]


def gerar_embeddings(model, dataset_path, output_path):
    from numpy import load
    data = load(dataset_path)
    faces, labels = data['arr_0'], data['arr_1']
    embeddings = asarray([extract_embeddings(model, face) for face in faces])
    savez_compressed(output_path, embeddings, labels)
    print(f"✅ Embeddings salvos: {embeddings.shape[0]} vetores")
