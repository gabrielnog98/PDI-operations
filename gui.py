import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import cv2
import numpy as np
from processamento import histograma, filtros, morfologia, segmentacao, intensidade, fourier

imagem = None
painel = None
imagem_original = None

def abrir_imagem():
    global imagem, imagem_original
    caminho = filedialog.askopenfilename()
    if caminho:
        imagem_colorida = cv2.imread(caminho)
        imagem = cv2.cvtColor(imagem_colorida, cv2.COLOR_BGR2GRAY)
        imagem_original = imagem.copy() 
        mostrar_imagem(imagem)


def salvar_imagem():
    global imagem
    if imagem is not None:
        caminho = filedialog.asksaveasfilename(defaultextension=".png")
        if caminho:
            cv2.imwrite(caminho, imagem)
            messagebox.showinfo("Salvo", "Imagem salva com sucesso!")

def mostrar_imagem(img):
    global painel
    img_rgb = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
    im_pil = Image.fromarray(img_rgb)
    imgtk = ImageTk.PhotoImage(image=im_pil)
    
    painel.config(image=imgtk)
    painel.image = imgtk


    largura, altura = im_pil.size
    painel.master.geometry(f"{largura}x{altura + 25}")  


def aplicar_histograma():
    if imagem is not None:
        histograma.exibir_histograma(imagem)

def aplicar_equalizacao():
    global imagem
    if imagem is not None:
        imagem = histograma.equalizar_histograma(imagem)
        mostrar_imagem(imagem)

def aplicar_filtro_media():
    global imagem
    if imagem is not None:
        imagem = filtros.filtro_media(imagem)
        mostrar_imagem(imagem)

def aplicar_filtro_gaussiano():
    global imagem
    if imagem is not None:
        imagem = filtros.filtro_gaussiano(imagem)
        mostrar_imagem(imagem)

def aplicar_sobel():
    global imagem
    if imagem is not None:
        imagem = filtros.filtro_sobel(imagem)
        mostrar_imagem(imagem)

def aplicar_laplaciano():
    global imagem
    if imagem is not None:
        imagem = filtros.filtro_laplaciano(imagem)
        mostrar_imagem(imagem)

def aplicar_erosao():
    global imagem
    if imagem is not None:
        imagem = morfologia.erosao(imagem)
        mostrar_imagem(imagem)

def aplicar_dilatacao():
    global imagem
    if imagem is not None:
        imagem = morfologia.dilatacao(imagem)
        mostrar_imagem(imagem)

def aplicar_otsu():
    global imagem
    if imagem is not None:
        imagem = segmentacao.aplicar_otsu(imagem)
        mostrar_imagem(imagem)

def aplicar_alargamento_contraste():
    global imagem
    if imagem is not None:
        imagem = intensidade.alargamento_contraste(imagem)
        mostrar_imagem(imagem)

def aplicar_mediana():
    global imagem
    if imagem is not None:
        imagem = filtros.filtro_mediana(imagem)
        mostrar_imagem(imagem)

def aplicar_maximo():
    global imagem
    if imagem is not None:
        imagem = filtros.filtro_maximo(imagem)
        mostrar_imagem(imagem)

def aplicar_minimo():
    global imagem
    if imagem is not None:
        imagem = filtros.filtro_minimo(imagem)
        mostrar_imagem(imagem)
        
def aplicar_roberts():
    global imagem
    if imagem is not None:
        imagem = filtros.filtro_roberts(imagem)
        mostrar_imagem(imagem)

def aplicar_prewitt():
    global imagem
    if imagem is not None:
        imagem = filtros.filtro_prewitt(imagem)
        mostrar_imagem(imagem)

def aplicar_fourier():
    if imagem is not None:
        fourier.espectro_fourier(imagem)

def aplicar_filtro_freq_pb():
    global imagem
    if imagem is not None:
        imagem = fourier.filtro_frequencia(imagem, tipo="passa-baixa", raio=30)
        mostrar_imagem(imagem)

def aplicar_filtro_freq_pa():
    global imagem
    if imagem is not None:
        imagem = fourier.filtro_frequencia(imagem, tipo="passa-alta", raio=30)
        mostrar_imagem(imagem)

def resetar_imagem():
    global imagem, imagem_original
    if imagem_original is not None:
        imagem = imagem_original.copy()
        mostrar_imagem(imagem)

def iniciar_app():
    global painel
    root = tk.Tk()
    root.title("Projeto PDI")
    root.geometry("800x600")

    menubar = tk.Menu(root)

    menu_arquivo = tk.Menu(menubar, tearoff=0)
    menu_arquivo.add_command(label="Abrir imagem", command=abrir_imagem)
    menu_arquivo.add_command(label="Salvar imagem", command=salvar_imagem)
    menubar.add_cascade(label="Arquivo", menu=menu_arquivo)

    menu_proc = tk.Menu(menubar, tearoff=0)

    menu_hist = tk.Menu(menu_proc, tearoff=0)
    menu_hist.add_command(label="Exibir", command=aplicar_histograma)
    menu_hist.add_command(label="Equalizar", command=aplicar_equalizacao)
    menu_proc.add_cascade(label="Histograma", menu=menu_hist)
    menu_hist.add_command(label="Alargamento de Contraste", command=aplicar_alargamento_contraste)

    menu_filtros = tk.Menu(menu_proc, tearoff=0)
    menu_filtros.add_command(label="Média", command=aplicar_filtro_media)
    menu_filtros.add_command(label="Gaussiano", command=aplicar_filtro_gaussiano)
    menu_filtros.add_command(label="Sobel", command=aplicar_sobel)
    menu_filtros.add_command(label="Laplaciano", command=aplicar_laplaciano)
    menu_filtros.add_command(label="Mediana", command=aplicar_mediana)
    menu_filtros.add_command(label="Máximo", command=aplicar_maximo)
    menu_filtros.add_command(label="Mínimo", command=aplicar_minimo)
    menu_filtros.add_command(label="Roberts", command=aplicar_roberts)
    menu_filtros.add_command(label="Prewitt", command=aplicar_prewitt)

    menu_proc.add_cascade(label="Filtros", menu=menu_filtros)

    menu_morf = tk.Menu(menu_proc, tearoff=0)
    menu_morf.add_command(label="Erosão", command=aplicar_erosao)
    menu_morf.add_command(label="Dilatação", command=aplicar_dilatacao)
    menu_proc.add_cascade(label="Morfologia", menu=menu_morf)

    menu_proc.add_command(label="Segmentação (Otsu)", command=aplicar_otsu)

    menubar.add_cascade(label="Processamento", menu=menu_proc)
   
    menu_fourier = tk.Menu(menu_proc, tearoff=0)
    menu_fourier.add_command(label="Exibir Espectro", command=aplicar_fourier)
    menu_proc.add_cascade(label="Fourier", menu=menu_fourier)
    menu_fourier.add_command(label="Filtro Passa-Baixa", command=aplicar_filtro_freq_pb)
    menu_fourier.add_command(label="Filtro Passa-Alta", command=aplicar_filtro_freq_pa)



    root.config(menu=menubar)

    frame_botoes = tk.Frame(root)
    frame_botoes.pack(side=tk.TOP, fill=tk.X)
    botao_reset = tk.Button(frame_botoes, text="Resetar imagem", command=resetar_imagem)
    botao_reset.pack(side=tk.RIGHT, padx=10, pady=10)
    painel = tk.Label(root)
    painel.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    
    root.mainloop()
