import cv2
import numpy as np
import matplotlib.pyplot as plt

def plot_histogram(image, title, save_path=None):
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])
    plt.figure()
    plt.title(title)
    plt.xlabel("Pixel Value")
    plt.ylabel("Frequency")
    plt.plot(hist)
    plt.xlim([0, 256])
    
    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()

# Leitura da imagem
image_path = "../media/fernando/eu.jpg"  

# Verificar se o arquivo existe
if not cv2.haveImageReader(image_path):
    raise FileNotFoundError(f"Arquivo da imagem não encontrado: {image_path}")

# Tentar abrir a imagem
image = cv2.imread(image_path)

# Verificar se a imagem foi carregada corretamente
if image is None:
    raise ValueError(f"Falha ao abrir a imagem: {image_path}")

# Conversão para tons de cinza
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Cálculo do histograma antes da equalização
histogram_path_before = "histograma_before.png"
plot_histogram(gray, "Histograma antes da equalização", save_path=histogram_path_before)

# Equalização do histograma
equalized = cv2.equalizeHist(gray)

# Cálculo do histograma após a equalização
histogram_path_after = "histograma_after.png"
plot_histogram(equalized, "Histograma após a equalização", save_path=histogram_path_after)

# Salvando as imagens em tons de cinza e equalizada
cv2.imwrite("imagem_cinza.jpg", gray)
cv2.imwrite("imagem_equalizada.jpg", equalized)

# Exibição dos gráficos de histograma
plt.show()


