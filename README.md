
## Projeto PDI (Processamento Digital de Imagens)

Projeto desenvolvido como parte da disciplina de Processamento Digital de Imagens, com o objetivo de implementar um sistema interativo para edição e análise de imagens.

## Funcionalidades Implementadas

- Interface gráfica com Tkinter
- Carregamento de imagens RGB convertidas automaticamente para tons de cinza
- Salvamento da imagem processada
- Exibição do histograma e equalização
- Alargamento de contraste
- Filtros passa-baixa: Média, Mediana, Máximo, Mínimo
- Filtros passa-alta: Sobel, Laplaciano, Roberts, Prewitt
- Segmentação com limiarização de Otsu
- Morfologia matemática: Erosão e Dilatação
- Espectro de Fourier (visualização)
- Filtros no domínio da frequência: passa-baixa e passa-alta
- Botão de reset para restaurar a imagem original

## Tecnologias

- Python 3.12
- OpenCV
- NumPy
- Matplotlib
- Tkinter
- Pillow

## Execução

```bash
pip install -r requirements.txt
python main.py
```

---

Desenvolvido por Gabriel Nogueira Silva
