# load libraries
from huggingface_hub import hf_hub_download
from ultralytics import YOLO
from supervision import Detections
from PIL import Image

# download model
model_path = hf_hub_download(
    repo_id="arnabdhar/YOLOv8-Face-Detection", 
    filename="model.pt",
    cache_dir="C:/Users/andre/Documents/codigos pyton/Codigos-Python/I.A/treinar_yolov8-main/Face-detection/modelos"  # pasta onde o modelo será salvo
    )

# load model
model = YOLO(model_path)

# inference
image_path = "C:/Users/andre/Documents/codigos pyton/Codigos-Python/I.A/treinar_yolov8-main/Face-detection/modelos"
output = model(Image.open(image_path))
results = Detections.from_ultralytics(output[0])