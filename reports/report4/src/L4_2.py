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

def process_image(image):
    # Conversão para tons de cinza
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    return gray

# Inicialização da webcam
cap = cv2.VideoCapture(0)

save_images = False
frame = None

while True:
    # Capturar um quadro da webcam
    ret, frame = cap.read()

    # Verificar se o quadro foi capturado corretamente
    if not ret:
        print("Erro ao capturar o quadro")
        break

    gray = process_image(frame)

    # Exibir a imagem cinza em uma janela separada
    cv2.imshow("Imagem Cinza", gray)

    # Equalizar a imagem cinza
    equalized = cv2.equalizeHist(gray)

    # Exibir a imagem equalizada em uma janela separada
    cv2.imshow("Imagem Equalizada", equalized)

    # Verificar se a tecla 'q' foi pressionada para sair
    if cv2.waitKey(1) == ord('q'):
        break

    # Verificar se a tecla 'x' foi pressionada para salvar as imagens
    elif cv2.waitKey(1) == ord('x'):
        if not save_images:
            # Salvar a imagem cinza
            cv2.imwrite("imagem_cinza.jpg", gray)

            # Salvar a imagem equalizada
            cv2.imwrite("imagem_equalizada.jpg", equalized)

            # Salvar o histograma antes da equalização
            plot_histogram(gray, "Histograma antes da equalização", save_path="histograma_before.png")

            # Salvar o histograma após a equalização
            plot_histogram(equalized, "Histograma após a equalização", save_path="histograma_after.png")

        save_images = True

    # Verificar se as imagens e histogramas devem ser salvos
    if save_images:
        # Liberação da webcam e fechamento das janelas
        cap.release()
        cv2.destroyAllWindows()
        break

# Liberação da webcam e fechamento das janelas
cap.release()
cv2.destroyAllWindows()
