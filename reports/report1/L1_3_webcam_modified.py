import numpy as np
import cv2 as cv
import time

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()
    
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    
    # Display the resulting frame
    cv.imshow('frame', frame)

    ### Armazena o código ascii da tecla pressionada pelo usuário
    key = cv.waitKey(1) 
    if key == ord('q'):
        break
    # Se alguma tecla for pressionada(exceto o q, ele encerra o programa),
    # O programa espera 5s e salva o frame atual como um arquivo
    if(key != -1):
        time.sleep(5)
        ret, frame = cap.read()
        cv.imwrite(f"fotos/{key}.png", frame)

    ### Salva o frame atual gravado na camera no arquivo
    if (key == ord('x')):
        cv.imwrite("Foto.png", frame)
    ###
    

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
