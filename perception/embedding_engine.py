import cv2
import numpy as np

class EmbeddingEngine:
    """
    Extracts simple, explainable visual embeddings.
    No deep learning.
    Fully offline.
    """

    def get_embedding(self, image):
        """
        image: preprocessed image (224x224x3)
        returns: List[float]
        """

        # Convert image back to 0–255 range
        image_uint8 = (image * 255).astype(np.uint8)

        # Convert to grayscale
        gray = cv2.cvtColor(image_uint8, cv2.COLOR_BGR2GRAY)

        # Grayscale histogram (64 bins)
        hist = cv2.calcHist([gray], [0], None, [64], [0, 256])
        hist = cv2.normalize(hist, hist).flatten()

        # Edge features
        edges = cv2.Canny(gray, 100, 200)
        edge_mean = np.mean(edges)
        edge_std = np.std(edges)

        # Final embedding
        embedding = np.concatenate([hist, [edge_mean, edge_std]])

        return embedding.tolist()
