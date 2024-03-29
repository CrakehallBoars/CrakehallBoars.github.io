import cv2

# Capturando o vídeo
capture = cv2.VideoCapture("mov_obj_rapido.avi")

# Obtendo as dimensões do vídeo
width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Obtendo a taxa de quadros do vídeo original
fps = 15

# Configurando a gravação de vídeo
output = cv2.VideoWriter('output.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

while capture.isOpened():
    _, img_1 = capture.read()
    _, img_2 = capture.read()

    diff = cv2.absdiff(img_1, img_2)
    diff_gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    diff_blur = cv2.GaussianBlur(diff_gray, (5, 5), 0)
    _, thresh_bin = cv2.threshold(diff_blur, 20, 255, cv2.THRESH_BINARY)

    contours, hierarchy = cv2.findContours(thresh_bin, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        if cv2.contourArea(contour) > 300:
            cv2.rectangle(img_1, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("Detecting Motion...", img_1)

    # Gravando o frame atual no vídeo de saída
    output.write(img_1)

    if cv2.waitKey(100) == 13:
        break

# Liberando os recursos
capture.release()
output.release()
cv2.destroyAllWindows()

