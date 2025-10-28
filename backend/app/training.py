from ultralytics import YOLO
import os, shutil
from .config import MODELS_DIR

def run_training(dataset_path, epochs=50, imgsz=640):
    data_yaml = None
    for root, dirs, files in os.walk(dataset_path):
        for f in files:
            if f.endswith('.yaml') or f == 'data.yaml':
                data_yaml = os.path.join(root, f)
                break
        if data_yaml:
            break
    if data_yaml is None:
        return {'status':'error', 'detail':'data.yaml not found in dataset'}
    base = os.path.join(MODELS_DIR, 'yolov8n.pt')
    if not os.path.exists(base):
        base = 'yolov8n'
    model = YOLO(base)
    out = model.train(data=data_yaml, epochs=epochs, imgsz=imgsz)
    run_dir = None
    runs_base = os.path.join('runs', 'train')
    if os.path.exists(runs_base):
        candidates = [os.path.join(runs_base, d) for d in os.listdir(runs_base)]
        candidates = [c for c in candidates if os.path.isdir(c)]
        if candidates:
            run_dir = sorted(candidates, key=os.path.getmtime)[-1]
    if run_dir:
        best = os.path.join(run_dir, 'weights', 'best.pt')
        if os.path.exists(best):
            dest = os.path.join(MODELS_DIR, 'trained_custom.pt')
            shutil.copyfile(best, dest)
            return {'status':'ok', 'model': dest}
    return {'status':'error', 'detail':'training finished but best.pt not found'}
