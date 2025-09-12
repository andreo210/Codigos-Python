if __name__ == "__main__":     
        # Importa utilitários para downloads do ultralytics
        from ultralytics.utils.downloads import GITHUB_ASSETS_STEMS
        GITHUB_ASSETS_STEMS  # Lista de arquivos de ativos do GitHub

        # Importa a classe YOLO e configurações do ultralytics
        from ultralytics import YOLO, settings
        settings  # Exibe as configurações atuais

        # Atualiza o diretório onde os resultados dos treinamentos serão salvos
        settings.update({'runs_dir': './runs'})

        settings  # Exibe as configurações atualizadas

        # Cria o modelo YOLO usando a configuração padrão 'yolov8n'
        model = YOLO('yolo11n.pt')  # Pode ser substituído por yolov8n_custom.yaml

        # Treina o modelo com o conjunto de dados personalizado
        model.train(
            data='C:/Users/andre/Documents/codigos pyton/Codigos-Python/I.A/treinar_yolov8-main/custom_dataset.yaml',  # Caminho para o arquivo de configuração do dataset
            epochs=30,  # Número de épocas de treinamento
            device=0,  # Usa GPU 0; pode ser 'cpu' ou lista de GPUs
            patience=8,  # Número de épocas sem melhora antes de parar
            batch=16,  # Tamanho do batch; -1 para automático
            imgsz=640,  # Tamanho das imagens
            workers=8,  # Número de workers para carregamento dos dados
            pretrained=True,  # Usa pesos pré-treinados
            resume=False,  # Não retoma treinamento anterior
            single_cls=False,  # Se True, considera apenas uma classe
            # project='runs/detect',  # Diretório do projeto
            box=7.5,  # Parâmetro de recall/IoU/precisão
            cls=0.5,  # Parâmetro de classificação de bbox
            dfl=1.5,  # Parâmetro de Distribution Focal Loss
            val=True,  # Realiza validação durante o treinamento
            # Augmentações
            degrees=0.3,  # Rotação das imagens
            hsv_s=0.3,  # Saturação HSV
            hsv_v=0.3,  # Valor HSV
            scale=0.5,  # Escala das imagens
            fliplr=0.5  # Probabilidade de flip horizontal
        )

        # Carrega o modelo treinado com os melhores pesos
        model = YOLO('runs/detect/train/weights/best.pt')

        # Avalia o modelo usando o conjunto de teste
        results = model.val(
            #project='runs/detect',
            imgsz=640,  # Tamanho das imagens
            batch=16,  # Tamanho do batch
            conf=0.001,  # Confiança mínima para detecção
            iou=0.7,  # Threshold de IoU para NMS
            save_json=False,  # Não salva resultados em JSON
            save_hybrid=False,  # Não salva labels híbridos
            split='test'  # Usa o conjunto de teste
        )

        results  # Exibe os resultados da avaliação

        results.box  # Exibe as caixas delimitadoras

        results.box.map50  # Exibe o mAP@0.5

        # Carrega novamente o modelo treinado
        model = YOLO('runs/detect/train/weights/best.pt')

        # Realiza predição em uma imagem
        results_img = model.predict(
            source='img.jpg',  # Caminho da imagem
            conf=0.25,  # Confiança mínima
            iou=0.7,  # Threshold de IoU para NMS
            imgsz=640,  # Tamanho da imagem
            show=False,  # Não exibe a imagem
            save=True,  # Salva a imagem com as detecções
            save_txt=True,  # Salva coordenadas das caixas
            save_conf=True,  # Salva confiança das detecções
            save_crop=True,  # Salva os crops das detecções
            # project='runs/detect',
            stream=False  # Faz inferência imediatamente
        )
        results_img  # Exibe resultados da predição

        results_img[0].boxes  # Exibe caixas da primeira imagem

        # Realiza predição em um vídeo
        results_video = model.predict(
            source='eolico.mp4',  # Caminho do vídeo
            conf=0.25,  # Confiança mínima
            iou=0.7,  # Threshold de IoU para NMS
            imgsz=640,  # Tamanho das imagens
            show=False,  # Não exibe o vídeo
            save=True,  # Salva o vídeo com as detecções
            save_txt=False,  # Não salva coordenadas das caixas
            save_conf=False,  # Não salva confiança das detecções
            save_crop=False,  # Não salva crops das detecções
            # project='runs/detect',
            stream=True  # Faz inferência em tempo real
        )

        results_video  # Exibe resultados da predição no vídeo

        # Itera sobre os resultados do vídeo
        for result in results_video:
            # Aqui você pode processar os resultados
            pass
            # boxes = result.boxes  # Caixas delimitadoras
            # masks = result.masks  # Máscaras de segmentação
            # keypoints = result.keypoints  # Pontos chave para pose
            # probs = result.probs  # Probabilidades de classificação

        # Carrega novamente o modelo treinado
        model = YOLO('runs/detect/train/weights/best.pt')

        # Importa bibliotecas para manipulação de imagens
        from PIL import Image
        import numpy as np
        import cv2

        # Abre uma imagem usando PIL
        img_pil = Image.open('img.jpg')
        img_pil  # Exibe a imagem

        # Realiza predição usando uma imagem PIL
        results_img_pil = model.predict(
            source=img_pil,  # Imagem PIL
            conf=0.25,
            iou=0.7,
            imgsz=640,
            show=False,
            save=True,
            save_txt=True,
            save_conf=True,
            save_crop=True,
            # project='runs/detect',
            stream=False
        )

        xyxy = results_img_pil[0].boxes.xyxy.cpu().numpy()  # Coordenadas das caixas

        # Recorta a imagem usando PIL
        img_pil.crop((xyxy[0][0], xyxy[0][1], xyxy[0][2], xyxy[0][3]))

        # Lê a imagem usando OpenCV
        img_cv = cv2.imread('img.jpg')

        # Realiza predição usando uma imagem OpenCV
        results_img_cv2 = model.predict(
            source=img_cv,  # Imagem OpenCV
            conf=0.25,
            iou=0.7,
            imgsz=640,
            show=False,
            save=False,
            save_txt=False,
            save_conf=False,
            save_crop=False,
            # project='runs/detect',
            stream=False
        )

        xyxy = results_img_cv2[0].boxes.xyxy.cpu().numpy().astype(int)  # Coordenadas das caixas

        # Recorta a imagem usando OpenCV
        img_cv_cropped = img_cv[xyxy[0][1]:xyxy[0][3], xyxy[0][0]:xyxy[0][2]]
        Image.fromarray(cv2.cvtColor(img_cv_cropped, cv2.COLOR_BGR2RGB))  # Exibe o crop com PIL

        # Realiza rastreamento de objetos em vídeo
        results_track = model.track(
            source='eolico.mp4',
            # project='runs/detect',
            show=False,
            save=True
        )

        results_track  # Exibe resultados do rastreamento

        results_track[0].boxes  # Exibe caixas do primeiro