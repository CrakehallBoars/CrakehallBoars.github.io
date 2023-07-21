import numpy as np
import cv2 as cv

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

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    sift = cv.SIFT_create()
    kp = sift.detect(gray,None)

    frame=cv.drawKeypoints(gray,kp,frame)
 
    # Display the resulting frame
    cv.imshow('frame', frame)

    # Salva a foto do frame quando a tecla Enter for pressionada 
    if cv.waitKey(1) == 13:
        cv.imwrite('img_sift.jpg', frame)
        break

    # Check if the 'q' key is pressed to quit the loop
    if cv.waitKey(1) == ord('q'):
        break

# When everything is done, release the capture
cap.release()
cv.destroyAllWindows()
