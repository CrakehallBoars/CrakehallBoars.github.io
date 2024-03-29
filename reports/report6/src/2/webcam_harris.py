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
    gray = np.float32(gray)
    dst = cv.cornerHarris(gray, 2, 3, 0.04)
    dst = cv.dilate(dst, None)

    frame[dst > 0.01 * dst.max()] = [0, 0, 255]

    # Display the resulting frame
    cv.imshow('frame', frame)

    # Salva a foto do frame quando a tecla Enter for pressionada 
    if cv.waitKey(1) == 13:
        cv.imwrite('img_harris.jpg', frame)
        break

    # Check if the 'q' key is pressed to quit the loop
    if cv.waitKey(1) == ord('q'):
        break

# When everything is done, release the capture
cap.release()
cv.destroyAllWindows()
