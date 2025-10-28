from ultralytics import YOLO
import os
from .config import CUSTOM_MODEL, BASE_YOLO_MODEL

_model = None

def _load_model():
    global _model
    if _model is not None:
        return _model
    model_path = CUSTOM_MODEL if os.path.exists(CUSTOM_MODEL) else BASE_YOLO_MODEL
    if os.path.exists(model_path):
        _model = YOLO(model_path)
    else:
        _model = YOLO('yolov8n')
    return _model


def run_inference(image_path, conf=0.25, iou=0.45):
    model = _load_model()
    results = model.predict(source=image_path, conf=conf, iou=iou, verbose=False)
    out = []
    if len(results) > 0:
        r = results[0]
        boxes = r.boxes
        for box in boxes:
            cls = int(box.cls[0])
            label = model.names.get(cls, str(cls))
            confs = float(box.conf[0])
            xyxy = box.xyxy[0].tolist()
            out.append({'label': label, 'confidence': round(confs, 3), 'bbox': [round(x,1) for x in xyxy]})
    return out
