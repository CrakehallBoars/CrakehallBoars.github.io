import cv2
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
image_path = "../media/1/leonardo/leonardo.png"  

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

# Limiarização
ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

# Salvando as imagens em tons de cinza e limiarizada
cv2.imwrite("imagem_cinza.jpg", gray)
cv2.imwrite("imagem_limiarizada.jpg", thresh)

# Exibição dos gráficos de histograma
plt.show()
