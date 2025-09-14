from os import listdir
from numpy import asarray, savez_compressed
from utils.face_extraction import extrair_rosto
import os
from mtcnn.mtcnn import MTCNN


def load_faces(directory):
    return [extrair_rosto(os.path.join(directory, f)) for f in listdir(directory) if extrair_rosto(os.path.join(directory, f)) is not None]


def load_dataset(pasta):
    from os import listdir
    from os.path import isdir, join
    from numpy import asarray

    detector = MTCNN()  # ✅ cria o detector uma vez

    faces, labels = [], []
    for pessoa in listdir(pasta):
        subpasta = join(pasta, pessoa)
        if not isdir(subpasta):
            continue
        for arquivo in listdir(subpasta):
            caminho = join(subpasta, arquivo)
            face = extrair_rosto(caminho, detector)  # ✅ passa o detector
            if face is not None:
                faces.append(face)
                labels.append(pessoa)

    return asarray(faces), asarray(labels)
