import random

EMBEDDING_SIZE = 128

def get_embedding(image_frame=None) -> list[float]:
    """
    Mock embedding generator.
    Always returns a fixed-length vector.
    """
    return [round(random.random(), 4) for _ in range(EMBEDDING_SIZE)]
