Backend README - AI Vision Backend (FastAPI + YOLOv8)

Files of importance:
- main.py          : FastAPI app with endpoints for detection & training
- detection.py     : Inference logic - loads model and runs detection
- training.py      : Training logic - unzips dataset and runs YOLO training
- utils.py         : helper functions (save files, model selection)
- config.py        : constants and paths
- requirements.txt : pip install requirements
