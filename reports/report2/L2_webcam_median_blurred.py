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

    # Apply filter to the frame
    blur = cv.medianBlur(frame,5)

    # Display the resulting frame
    cv.imshow('frame', blur)

    key = cv.waitKey(1)
    if key == ord('q'):
        break
    if(key != -1):
        time.sleep(1)
        ret, frame = cap.read()
        # Apply filter to the captured frame and save it
        blur_frame = cv.medianBlur(frame,5)
        cv.imwrite(f"fotos/{key}.png", blur_frame)

    ### Salva o frame atual gravado na camera no arquivo
    if (key == ord('x')):
        # Apply filter to the captured frame and save it
        blur_frame = cv.medianBlur(frame,5)
        cv.imwrite("Foto.png", blur_frame)
    ###

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
