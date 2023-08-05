import cv2
import sys

# Cria o rastreador
tracker = cv2.TrackerKCF_create()

# Lê o vídeo
video = cv2.VideoCapture("lab8\chaplin.mp4")

# Sai se o vídeo não for aberto
if not video.isOpened():
    print("Não foi possível abrir o vídeo")
    sys.exit()

# Lê o primeiro quadro
ok, frame = video.read()
if not ok:
    print("Não foi possível ler o arquivo de vídeo")
    sys.exit()

# Define uma caixa delimitadora (ROI)
bbox = cv2.selectROI(frame, False)

# Inicializa o rastreador com o primeiro quadro e a caixa delimitadora
ok = tracker.init(frame, bbox)

# Define o codec e cria o objeto VideoWriter
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('Lab-08.mp4', fourcc, 20.0, (frame.shape[1], frame.shape[0]))

while True:
    # Lê um novo quadro
    ok, frame = video.read()
    if not ok:
        break

    # Atualiza o rastreador
    ok, bbox = tracker.update(frame)

    # Desenha a caixa delimitadora
    if ok:
        # Sucesso no rastreamento
        p1 = (int(bbox[0]), int(bbox[1]))
        p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        cv2.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)
    else:
        # Falha no rastreamento
        cv2.putText(frame, "Falha no rastreamento detectada", (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

    # Mostra o resultado
    cv2.imshow("Rastreamento", frame)

    # Escreve o quadro no arquivo de saída
    out.write(frame)

    # Sai se a tecla ESC for pressionada
    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break


video.release()
out.release()
cv2.destroyAllWindows()
