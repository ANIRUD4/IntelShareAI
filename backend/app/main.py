from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.responses import JSONResponse
import os, zipfile, shutil, time
from app import capture, train_faces, recognize
from app.config import DATASETS_DIR, MODELS_DIR, OUTPUTS_DIR, CAPTURE_IMAGE_COUNT

app = FastAPI(title='Face Recognition Backend (Edge)')

# ensure directories
os.makedirs(DATASETS_DIR, exist_ok=True)
os.makedirs(MODELS_DIR, exist_ok=True)
os.makedirs(OUTPUTS_DIR, exist_ok=True)

@app.get('/')
def root():
    return {'status':'ok'}

@app.post('/capture_face')
async def capture_face(username: str = Form(...), num_images: int = Form(CAPTURE_IMAGE_COUNT)):
    # capture images from camera into datasets/<username>/
    try:
        saved = capture.capture_images_for_user(username, DATASETS_DIR, num_images)
        return JSONResponse({'status':'ok', 'saved': saved})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post('/upload_dataset')
async def upload_dataset(name: str = Form(...), dataset_zip: UploadFile = File(...)):
    dest = os.path.join(DATASETS_DIR, name)
    if os.path.exists(dest):
        shutil.rmtree(dest)
    os.makedirs(dest, exist_ok=True)
    zip_path = os.path.join(dest, dataset_zip.filename)
    with open(zip_path, 'wb') as f:
        f.write(await dataset_zip.read())
    with zipfile.ZipFile(zip_path, 'r') as z:
        z.extractall(dest)
    os.remove(zip_path)
    return {'status':'ok', 'path': dest}

@app.post('/train_faces')
def train_faces_endpoint():
    out = train_faces.train_face_embeddings()
    return JSONResponse(out)

@app.post('/recognize_once')
def recognize_once_endpoint():
    try:
        out = recognize.recognize_once_from_camera()
        return JSONResponse({'status':'ok', 'result': out})
    except Exception as e:
        return JSONResponse({'status':'error', 'detail': str(e)}, status_code=500)

@app.get('/models')
def list_models():
    models = []
    for f in os.listdir(MODELS_DIR):
        if f.endswith('.pkl') or f.endswith('.pt') or f.endswith('.pth'):
            models.append(f)
    return {'models': models}

#upload image to recognise
from fastapi import UploadFile, File
from app.recognize import recognize_from_image_bytes

@app.post("/recognize_face")
async def recognize_face(file: UploadFile = File(...)):
    image_bytes = await file.read()
    result = recognize_from_image_bytes(image_bytes)
    return result
