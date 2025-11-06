import os
BASE_DIR = os.path.dirname(__file__)
MODELS_DIR = os.path.join(BASE_DIR, 'models')
DATASETS_DIR = os.path.join(BASE_DIR, 'datasets')
OUTPUTS_DIR = os.path.join(BASE_DIR, 'outputs')
BASE_YOLO_MODEL = os.path.join(MODELS_DIR, 'yolov8n.pt')
CUSTOM_MODEL = os.path.join(MODELS_DIR, 'trained_custom.pt')
DEFAULT_EPOCHS = 50
