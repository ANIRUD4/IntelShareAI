# NOTE: This Dockerfile is a reasonable starting point for x86_64 Linux.
# For Raspberry Pi or NVIDIA Jetson, use device-specific base images and install dlib/face_recognition appropriately.
FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential cmake git wget \
    libopenblas-dev liblapack-dev \
    libx11-6 libgtk2.0-0 libglib2.0-0 libsm6 libxrender1 libxext6 \
    pkg-config libboost-all-dev \
    libgl1 libgl1-mesa-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy requirements and install (may take time)
COPY backend/requirements.txt /app/requirements.txt
RUN pip install --upgrade pip setuptools wheel && pip install --no-cache-dir -r /app/requirements.txt

# Copy app
COPY backend/app /app/app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]