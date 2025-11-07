import face_recognition, os, pickle
from app.config import DATASETS_DIR, MODELS_DIR

def train_face_embeddings(output_model_path=None):
    if output_model_path is None:
        output_model_path = os.path.join(MODELS_DIR, 'faces.pkl')
    encodings = []
    labels = []
    # iterate user folders
    for user in os.listdir(DATASETS_DIR):
        user_dir = os.path.join(DATASETS_DIR, user)
        if not os.path.isdir(user_dir):
            continue
        # process images in folder
        for fname in os.listdir(user_dir):
            if not fname.lower().endswith(('.jpg', '.jpeg', '.png')):
                continue
            img_path = os.path.join(user_dir, fname)
            image = face_recognition.load_image_file(img_path)
            faces = face_recognition.face_locations(image, model='hog')
            if len(faces) == 0:
                continue
            # take the first face found
            encoding = face_recognition.face_encodings(image, faces)[0]
            encodings.append(encoding)
            labels.append(user)
    if not encodings:
        return {'status':'error', 'detail':'no face encodings found'}
    # save
    os.makedirs(MODELS_DIR, exist_ok=True)
    with open(output_model_path, 'wb') as f:
        pickle.dump({'encodings': encodings, 'labels': labels}, f)
    return {'status':'ok', 'model_path': output_model_path, 'num_faces': len(encodings)}
