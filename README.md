# IntelShare 🧠  
**Human-in-the-Loop Personalized AI on the Edge**

IntelShare is a system that allows users to **teach AI systems using natural interaction** — vision, voice, and confirmation — without datasets, retraining, or machine learning expertise.

The system learns incrementally from real-world inputs and always keeps the **human in control**.

---

## 🚀 Key Features

- 📷 Vision-based learning using live camera input  
- 🎙️ Voice-based labeling using **offline speech recognition (Vosk)**  
- 🔁 Human-in-the-loop confirmation and correction  
- 📈 Incremental learning without retraining models  
- 🧠 Embedding-based knowledge storage  
- ⚙️ Edge-friendly and hardware-ready architecture  

---

## 🧩 High-Level Workflow

Camera → Embedding → Learn → Store Knowledge
↓
Inference
↓
Human Confirmation
↓
Incremental Update


The system never makes autonomous decisions — every prediction is verified or corrected by the user.

---

## 🛠️ Tech Stack

### Backend
- Python
- FastAPI
- Vosk (offline speech recognition)
- OpenCV
- NumPy

### Frontend
- HTML
- JavaScript
- Browser Camera & Microphone APIs

### AI / ML
- Embedding-based similarity
- Confidence-based incremental updates
- No datasets, no retraining

---

## 📁 Project Structure


The system never makes autonomous decisions — every prediction is verified or corrected by the user.

---

## 🛠️ Tech Stack

### Backend
- Python
- FastAPI
- Vosk (offline speech recognition)
- OpenCV
- NumPy

### Frontend
- HTML
- JavaScript
- Browser Camera & Microphone APIs

### AI / ML
- Embedding-based similarity
- Confidence-based incremental updates
- No datasets, no retraining

---

## 📁 Project Structure

intelshare/
├── backend/
│ ├── routes/ # learn, infer, confirm, speech
│ ├── orchestrator.py
│ └── main.py
├── perception/
│ └── embedding_engine.py
├── interaction/
│ ├── voice_listener.py
│ └── voice_api.py
├── data/
│ └── knowledge_units/
├── frontend/
│ ├── index.html
│ └── script.js
└── README.md


---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
git clone <repo-url>
cd intelshare


2️⃣ Install Python Dependencies
pip install -r requirements.txt

3️⃣ Install FFmpeg (Required for Speech)

FFmpeg is required to convert browser-recorded audio into a format usable by Vosk.

Download FFmpeg:
https://www.gyan.dev/ffmpeg/builds/

Add the bin directory to your system PATH

Verify installation:

ffmpeg -version

4️⃣ Download Vosk Model

Download an English Vosk model:
https://alphacephei.com/vosk/models/

Example:
vosk-model-small-en-us-0.15


Place it inside:
models/

5️⃣ Run the Backend

uvicorn backend.main:app --reload


6️⃣ Run the Frontend

Open frontend/index.html using Live Server or any local web server
