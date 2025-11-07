Face Recognition Backend (FastAPI) — Edge-ready (Raspberry Pi / Jetson)

Features included:
- Capture face images from camera and save under datasets/<username>/
- Train face recognition embeddings from datasets and save to models/faces.pkl
- Real-time recognition from camera; on recognized faces, new images are appended to dataset (incremental learning)
- FastAPI endpoints to control capture, training, and recognition
- Dockerfile + docker-compose.yml (notes for Raspberry Pi / Jetson included)

Important notes for edge devices:
- face_recognition depends on dlib which is heavy to build. On Raspberry Pi / Jetson, prefer installing platform-specific wheels or build from source.
- For NVIDIA Jetson, use NVIDIA's base images and install dlib/face_recognition appropriately (instructions in README).
- The provided Dockerfile works on many x86 Linux hosts; adapting for Pi/Jetson may require different base images and prebuilt wheels.

Run locally (non-Docker) recommended for initial tests on dev machine, then adapt Docker for target edge device.
