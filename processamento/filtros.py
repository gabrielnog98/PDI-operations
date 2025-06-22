import cv2
import numpy as np
def filtro_media(img):
    return cv2.blur(img, (5, 5))

def filtro_gaussiano(img):
    return cv2.GaussianBlur(img, (5, 5), 0)

def filtro_sobel(img):
    sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
    sobel = cv2.magnitude(sobelx, sobely)
    sobel = cv2.convertScaleAbs(sobel)
    return sobel
def filtro_laplaciano(img):
    lap = cv2.Laplacian(img, cv2.CV_64F)
    lap = cv2.convertScaleAbs(lap)
    return lap
def filtro_mediana(img):
    return cv2.medianBlur(img, 5)

def filtro_maximo(img):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.dilate(img, kernel)

def filtro_minimo(img):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.erode(img, kernel)

def filtro_roberts(img):
    import numpy as np
    import cv2

    kernelx = np.array([[1, 0], [0, -1]], dtype=np.float32)
    kernely = np.array([[0, 1], [-1, 0]], dtype=np.float32)
    x = cv2.filter2D(img, -1, kernelx)
    y = cv2.filter2D(img, -1, kernely)
    roberts = cv2.magnitude(x.astype(np.float32), y.astype(np.float32))
    return cv2.convertScaleAbs(roberts)

def filtro_prewitt(img):
    import numpy as np
    import cv2

    kernelx = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]], dtype=np.float32)
    kernely = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]], dtype=np.float32)
    x = cv2.filter2D(img, -1, kernelx)
    y = cv2.filter2D(img, -1, kernely)
    prewitt = cv2.magnitude(x.astype(np.float32), y.astype(np.float32))
    return cv2.convertScaleAbs(prewitt)
