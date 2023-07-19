import cv2

# Objeto da camera
cam = cv2.VideoCapture(0)

# Obtendo as dimensões do vídeo da camera
width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

fps = 15

# Configurando a gravação de vídeo
output = cv2.VideoWriter('../media/camera_tracked.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

while True:
    _, img_1 = cam.read()
    _, img_2 = cam.read()
    
    # Exibe o frame sem detecção
    cv2.imshow("Original",img_1)

    # Detecção de movimento
    diff = cv2.absdiff(img_1, img_2)
    diff_gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    diff_blur = cv2.GaussianBlur(diff_gray, (5, 5), 0)
    _, thresh_bin = cv2.threshold(diff_blur, 20, 255, cv2.THRESH_BINARY)

    contours, hierarchy = cv2.findContours(thresh_bin, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Desenha os contornos no frame
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        if cv2.contourArea(contour) > 300:
            cv2.rectangle(img_1, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Exibe o frame com a detecção 
    cv2.imshow("Detecção de movimento", img_1)

    # Gravando o frame atual no vídeo de saída
    output.write(img_1)

    # Termina o programa ao apertar Enter
    if cv2.waitKey(100) == 13:
        break

# Liberando os recursos
cam.release()
output.release()
cv2.destroyAllWindows()

