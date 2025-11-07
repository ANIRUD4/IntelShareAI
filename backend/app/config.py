import os
BASE_DIR = os.path.dirname(__file__)
DATASETS_DIR = os.path.join(BASE_DIR, 'datasets')
MODELS_DIR = os.path.join(BASE_DIR, 'models')
OUTPUTS_DIR = os.path.join(BASE_DIR, 'outputs')

# Recognition thresholds
FACE_DISTANCE_THRESHOLD = 0.5  # lower is stricter (0.4-0.6 typical)
RECOGNITION_SAVE_ON_MATCH = True  # if True, save recognized frames to dataset for incremental learning
CAPTURE_IMAGE_COUNT = 30  # default images to capture when creating dataset
