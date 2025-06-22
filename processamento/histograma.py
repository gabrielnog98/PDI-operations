import matplotlib.pyplot as plt
import cv2

def exibir_histograma(img):
    # Supondo que a imagem já está em tons de cinza
    plt.figure("Histograma")
    plt.hist(img.ravel(), 256, [0, 256])
    plt.title("Histograma")
    plt.xlabel("Intensidade")
    plt.ylabel("Frequência")
    plt.grid()
    plt.show()

def equalizar_histograma(img):
    # Equaliza a imagem em tons de cinza
    eq = cv2.equalizeHist(img)
    return eq
