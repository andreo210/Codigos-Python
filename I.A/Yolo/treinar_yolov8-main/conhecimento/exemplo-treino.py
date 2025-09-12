# Garante que o código só será executado se este arquivo for o principal
if __name__ == "__main__":
    # Importa a classe YOLO da biblioteca ultralytics
    from ultralytics import YOLO

    # Carrega um modelo YOLO a partir de um arquivo YAML (estrutura do modelo)
    model = YOLO("yolo11n.yaml")  # Cria um novo modelo a partir do YAML

    # Carrega um modelo YOLO pré-treinado a partir de um arquivo .pt
    model = YOLO("yolo11n.pt")  # Carrega um modelo pré-treinado (recomendado para treinamento)

    # Cria um modelo a partir do YAML e transfere os pesos do modelo pré-treinado
    model = YOLO("yolo11n.yaml").load("yolo11n.pt")  # Estrutura do YAML + pesos do .pt

    # Treina o modelo usando o conjunto de dados coco8.yaml, na GPU 0, por 100 épocas e imagens de tamanho 640
    # veja mais em https://docs.ultralytics.com/modes/train/
    results = model.train(
        data="coco8.yaml", 
        device=0, 
        epochs=1, 
        imgsz=640
        )
    
    results = model.val()  # Valida o modelo treinado