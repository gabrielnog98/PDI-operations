import numpy as np
import matplotlib.pyplot as plt
import cv2

def espectro_fourier(img):
    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)
    magnitude_spectrum = 20 * np.log(np.abs(fshift) + 1)
    
    plt.figure("Espectro de Fourier")
    plt.imshow(magnitude_spectrum, cmap='gray')
    plt.title("Magnitude do Espectro")
    plt.axis("off")
    plt.show()
def filtro_frequencia(img, tipo="passa-baixa", raio=30):
    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)

    linhas, colunas = img.shape
    crow, ccol = linhas // 2, colunas // 2

    mask = np.zeros((linhas, colunas), np.uint8)
    if tipo == "passa-baixa":
        cv2.circle(mask, (ccol, crow), raio, 1, -1)
    elif tipo == "passa-alta":
        mask[:] = 1
        cv2.circle(mask, (ccol, crow), raio, 0, -1)

    fshift_filtered = fshift * mask
    f_ishift = np.fft.ifftshift(fshift_filtered)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.abs(img_back)
    img_back = np.clip(img_back, 0, 255).astype(np.uint8)
    return img_back
