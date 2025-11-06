from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
import os, time, zipfile, shutil
from . import detection, training, utils

app = FastAPI(title='AI Vision Backend')

BASE_DIR = os.path.dirname(__file__)
MODELS_DIR = os.path.join(BASE_DIR, 'models')
DATASETS_DIR = os.path.join(BASE_DIR, 'datasets')
OUTPUTS_DIR = os.path.join(BASE_DIR, 'outputs')

os.makedirs(MODELS_DIR, exist_ok=True)
os.makedirs(DATASETS_DIR, exist_ok=True)
os.makedirs(OUTPUTS_DIR, exist_ok=True)

@app.get('/')
def root():
    return {'status':'ok'}

@app.post('/detect')
async def detect(file: UploadFile = File(...)):
    tmp_path = os.path.join('/tmp' if os.name!='nt' else BASE_DIR, f'tmp_{int(time.time()*1000)}_{file.filename}')
    with open(tmp_path, 'wb') as f:
        f.write(await file.read())
    try:
        results = detection.run_inference(tmp_path)
        return JSONResponse({'status':'ok', 'results': results})
    finally:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)

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

@app.post('/train')
async def train(dataset_name: str = Form(...), epochs: int = Form(50)):
    ds_path = os.path.join(DATASETS_DIR, dataset_name)
    if not os.path.exists(ds_path):
        return JSONResponse({'status':'error', 'detail': 'dataset not found'}, status_code=400)
    out = training.run_training(ds_path, epochs=epochs)
    return JSONResponse({'status':'ok', 'output': out})

@app.get('/models')
def list_models():
    models = []
    for f in os.listdir(MODELS_DIR):
        if f.endswith('.pt') or f.endswith('.pth'):
            models.append(f)
    return {'models': models}
