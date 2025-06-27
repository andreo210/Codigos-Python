from PIL import Image

def converter_para_cinza(caminho_imagem, caminho_saida):
    imagem = Image.open(caminho_imagem)
    imagem_cinza = imagem.convert('L')  # 'L' é o modo para tons de cinza
    imagem_cinza.save(caminho_saida)

def converter_para_pb(caminho_imagem, caminho_saida, limiar=128):
    imagem = Image.open(caminho_imagem).convert('L')  # Converte para cinza primeiro
    imagem_pb = imagem.point(lambda x: 255 if x > limiar else 0, '1')  # Binariza a imagem
    imagem_pb.save(caminho_saida)

    # Converter para cinza
converter_para_cinza('C:\\Users\\andreoa\\Documents\\Codigos-Python\\Liguagem Pyton\\Manipulacao de arquivo\\converter imagem para cinza e preto\\scaled.jpg', 'C:\\Users\\andreoa\\Documents\\Codigos-Python\\Liguagem Pyton\\Manipulacao de arquivo\\converter imagem para cinza e preto\\cinza.jpg')

# Converter para preto e branco com limiar 128
#converter_para_pb('como-ter-fotos-mais-nitidas-scaled.jpg', 'saida_pb.jpg')