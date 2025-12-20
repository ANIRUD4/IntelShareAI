import cv2
import numpy as np

class Preprocessor:
    """
    Prepares image for embedding extraction.
    """

    def __init__(self, target_size=(224, 224)):
        self.target_size = target_size

    def process(self, frame):
        """
        Resize + normalize.
        """
        resized = cv2.resize(frame, self.target_size)
        normalized = resized.astype(np.float32) / 255.0
        return normalized
