AI Vision Backend - FastAPI + YOLOv8 (Training + Inference) - Docker-ready

This package contains the backend server which supports:
- Inference endpoint (/detect) using YOLOv8 (custom model if trained, else base model)
- Training endpoint (/train) to fine-tune YOLO on user-uploaded datasets (YOLO format)
- Upload API for datasets and objects
- Dockerfile and docker-compose for easy deployment

Important:
- This repo expects Ultralytics YOLO (ultralytics package) and PyTorch available in the environment.
- Training in Docker may require additional GPU setup for speed (optional). CPU training is supported but slow.
