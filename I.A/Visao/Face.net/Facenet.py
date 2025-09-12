from keras_facenet import FaceNet


class FaceNetInit:
    def __init__(self):
        # Usa o modelo embutido da biblioteca keras-facenet
        self.embedder = FaceNet()
        self.model = self.embedder.model
