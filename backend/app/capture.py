import cv2, os, time
from .utils import ensure_dirs, timestamped_filename

def capture_images_for_user(username, dest_root, num_images=30, delay=0.2, device_index=0):
    dest = os.path.join(dest_root, username)
    ensure_dirs(dest)
    cap = cv2.VideoCapture(device_index)
    if not cap.isOpened():
        raise RuntimeError('Could not open camera. Check device permissions.')
    count = 0
    saved = []
    try:
        while count < num_images:
            ret, frame = cap.read()
            if not ret:
                time.sleep(0.1)
                continue
            filename = timestamped_filename('img')
            path = os.path.join(dest, filename)
            cv2.imwrite(path, frame)
            saved.append(path)
            count += 1
            time.sleep(delay)
    finally:
        cap.release()
    return saved
