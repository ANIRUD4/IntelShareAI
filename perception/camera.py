import cv2

class Camera:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)

        if not self.cap.isOpened():
            raise RuntimeError("Camera not working")

    def capture_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            raise RuntimeError("Could not read frame")
        return frame

    def close(self):
        self.cap.release()
