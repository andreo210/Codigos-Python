from PIL import Image
from numpy import asarray


"""def extrair_rosto(image_path, detector):
    try:
        img = Image.open(image_path).convert('RGB')
        img = img.resize((640, 480))
        pixels = asarray(img)
        faces = detector.detect_faces(pixels)

        if not faces:
            print(f"⚠️ Nenhum rosto detectado em: {image_path}")
            return None

        x1, y1, w, h = faces[0]['box']
        x1, y1 = abs(x1), abs(y1)
        x2, y2 = x1 + w, y1 + h
        face = pixels[y1:y2, x1:x2]
        image_face = Image.fromarray(face, 'RGB').resize((160, 160))
        return asarray(image_face)
    except Exception as e:
        print(f"Erro ao processar {image_path}: {e}")
        return None"""


def extrair_rosto(imagem_entrada, detector):
    from PIL import Image
    import numpy as np

    try:
        # ✅ Detecta se é caminho ou imagem
        if isinstance(imagem_entrada, str):
            img = Image.open(imagem_entrada).convert('RGB')
        elif isinstance(imagem_entrada, Image.Image):
            img = imagem_entrada.convert('RGB')
        else:
            raise ValueError("Entrada inválida: deve ser caminho ou PIL.Image")

        img = img.resize((640, 480))
        pixels = np.asarray(img)
        faces = detector.detect_faces(pixels)

        if not faces:
            print("⚠️ Nenhum rosto detectado")
            return None

        x1, y1, w, h = faces[0]['box']
        x1, y1 = abs(x1), abs(y1)
        x2, y2 = x1 + w, y1 + h
        face = pixels[y1:y2, x1:x2]
        image_face = Image.fromarray(face, 'RGB').resize((160, 160))
        return np.asarray(image_face)

    except Exception as e:
        print(f"❌ Erro ao processar imagem: {e}")
        return None

