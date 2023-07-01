import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
counter = 0

# Define a cor a ser rastreada (no exemplo, vermelho)
target_color = (128, 0, 128)  # BGR format

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        break

    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # Define range of target color in HSV
    target_color_hsv = cv.cvtColor(np.uint8([[target_color]]), cv.COLOR_BGR2HSV)
    target_hue = target_color_hsv[0][0][0]
    tolerance = 10  # Adjust this value to allow for some color variation

    lower_color = np.array([target_hue - tolerance, 50, 50])
    upper_color = np.array([target_hue + tolerance, 255, 255])

    # Threshold the HSV image to get only the target color
    mask = cv.inRange(hsv, lower_color, upper_color)

    # Bitwise-AND mask and original frame
    res = cv.bitwise_and(frame, frame, mask=mask)

    # Display the frames
    cv.imshow('Original', frame)
    cv.imshow('Mask', mask)
    cv.imshow('Result', res)

    key = cv.waitKey(1)

    # Save images when the "Q" key is pressed
    if key == ord('q') or key == ord('Q'):
        cv.imwrite(f'webcam_image_{counter}.jpg', frame)
        cv.imwrite(f'mask_image_{counter}.jpg', mask)
        cv.imwrite(f'result_image_{counter}.jpg', res)
        counter += 1

    if key == 27:
        break
        
# Release the capture and destroy windows
cap.release()
cv.destroyAllWindows()

