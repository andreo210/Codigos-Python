import cv2
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator

model = YOLO('C:/Users/andre/Documents/codigos pyton/Codigos-Python/I.A/treinar_yolov8-main/Face-detection/deteccao/model.pt')

video_cap = cv2.VideoCapture("C:/Users/andre/Downloads/VID_20250705_150836 (1).mp4")

while True:
    ret, frame = video_cap.read() # leitura do vídeo
    controlkey = cv2.waitKey(1)

    if not ret:
        break

    detections = model.track(frame, persist=True, tracker="bytetrack.yaml")[0] # detecta rosto e atribui ID com track

    for r in detections:
        annotator = Annotator(frame) # anota face detectada
        boxes = r.boxes
        for box in boxes:
            b = box.xyxy[0]  # pega as coordenadas do local da face detectada
            c = box.cls
            annotator.box_label(b, model.names[int(c)]) # adiciona caixa delimitadora na face

    cv2.imshow("Frame", frame) # exibe vídeo
    if cv2.waitKey(1) == ord("q"):
        break

video_cap.release()
cv2.destroyAllWindows()