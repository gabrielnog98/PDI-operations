import numpy as np

def alargamento_contraste(img):
    min_val = np.min(img)
    max_val = np.max(img)
    if max_val - min_val == 0:
        return img.copy()
    stretched = ((img - min_val) * (255.0 / (max_val - min_val))).astype(np.uint8)
    return stretched
