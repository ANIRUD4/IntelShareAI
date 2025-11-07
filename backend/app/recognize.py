import cv2, os, time, pickle, face_recognition, numpy as np
from app.config import MODELS_DIR, DATASETS_DIR, FACE_DISTANCE_THRESHOLD, RECOGNITION_SAVE_ON_MATCH
from app.utils import timestamped_filename, ensure_dirs

_model_path = os.path.join(MODELS_DIR, 'faces.pkl')
_loaded = None

def load_model():
    global _loaded
    if _loaded is not None:
        return _loaded
    if not os.path.exists(_model_path):
        return None
    with open(_model_path, 'rb') as f:
        _loaded = pickle.load(f)
    return _loaded

def recognize_once_from_camera(device_index=0, save_on_match=True):
    model = load_model()
    if model is None:
        raise RuntimeError('No trained model found. Run training first.')
    known_encodings = model['encodings']
    known_labels = model['labels']
    cap = cv2.VideoCapture(device_index)
    if not cap.isOpened():
        raise RuntimeError('Could not open camera.')
    ret, frame = cap.read()
    result = {'matches': []}
    if not ret:
        cap.release()
        return result
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    boxes = face_recognition.face_locations(rgb, model='hog')
    encs = face_recognition.face_encodings(rgb, boxes)
    for enc, box in zip(encs, boxes):
        if len(known_encodings)==0:
            continue
        distances = face_recognition.face_distance(known_encodings, enc)
        # distances is numpy array
        best_idx = int(np.argmin(distances))
        best_dist = float(distances[best_idx])
        label = known_labels[best_idx]
        match = best_dist <= FACE_DISTANCE_THRESHOLD
        result['matches'].append({'label': label, 'distance': best_dist, 'match': match, 'bbox': box})
        # if recognized and configured to save, append new image to that user's dataset
        if match and save_on_match and RECOGNITION_SAVE_ON_MATCH:
            user_dir = os.path.join(DATASETS_DIR, label)
            ensure_dirs(user_dir)
            fname = timestamped_filename('recog')
            path = os.path.join(user_dir, fname)
            cv2.imwrite(path, frame)
    cap.release()
    return result
