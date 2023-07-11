import cv2
import numpy as np
import matplotlib.pyplot as plt

def plot_bgr_histogram(image: np.ndarray, filename: str) -> None:
    colors = ('b','g','r')
    for i,col in enumerate(colors):
        histr = cv2.calcHist([image],[i],None,[256],[0,256])
        plt.plot(histr,color = col)
        plt.xlim([0,256])
    plt.show()
    plt.savefig(filename)

# Leitura da imagem
image_path = "../media/1/magic/magic.jpg"  

# Verificar se o arquivo existe
if not cv2.haveImageReader(image_path):
    raise FileNotFoundError(f"Arquivo da imagem não encontrado: {image_path}")

# Tentar abrir a imagem
image = cv2.imread(image_path)

# Verificar se a imagem foi carregada corretamente
if image is None:
    raise ValueError(f"Falha ao abrir a imagem: {image_path}")

# Separa a imagens nos canais de cor BGR
channels = cv2.split(image)

equalized_channels = []
# Aplica a equalização de histograma canal a canal
for channel in channels:
    equalized_channels.append(cv2.equalizeHist(channel))

# Junta novamente os canais de cor separados após a equalização
equalized_image = cv2.merge(equalized_channels)

# Calcula histogramas em todos os canais de cor e salva em arquivos
plot_bgr_histogram(image, "raw_histogram.png")
plot_bgr_histogram(equalized_image, "equalized_histogram.png")

# Coloca a imagem original e a equalizada lado a lado e grava no arquivo final.png
final_image = np.hstack((image, equalized_image))

cv2.imwrite("final.png", final_image)
