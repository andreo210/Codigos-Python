# Garante que o código só será executado se este arquivo for o principal
if __name__ == "__main__":        
        # Importa a classe YOLO da biblioteca ultralytics
        from ultralytics import YOLO

        # Carrega um modelo oficial pré-treinado (.pt)
        model = YOLO("yolo11n.pt")  # Carrega um modelo oficial

        # Carrega um modelo customizado treinado pelo usuário
        model = YOLO("runs/detect/train41/weights/best.pt")  # Carrega um modelo customizado

        # Valida o modelo carregado usando o conjunto de validação, aqui voce pode colocar alguns parametros 
        # veja mais em https://docs.ultralytics.com/modes/val/
        metrics = model.val(save_json=True) # Realiza a validação e salva os resultados em JSON

        metrics.box.map      # Exibe o mAP geral (mAP50-95)
        metrics.box.map50    # Exibe o mAP@0.5
        metrics.box.map75    # Exibe o mAP@0.75
        metrics.box.maps     # Exibe uma lista com o mAP de