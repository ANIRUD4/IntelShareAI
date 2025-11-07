import os, time, cv2

def ensure_dirs(*paths):
    for p in paths:
        os.makedirs(p, exist_ok=True)

def timestamped_filename(prefix='img', ext='jpg'):
    return f"{prefix}_{int(time.time()*1000)}.{ext}"
