import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
counter = 0

while True:
    # Capture frame-by-frame
    _, frame = cap.read()


    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # Define range of colors in HSV
    lower_red = np.array([0, 50, 50])	
    upper_red = np.array([10, 255, 255])
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])
    lower_green = np.array([50, 50, 50])
    upper_green = np.array([70, 255, 255])

    # Threshold the HSV image to get only specified colors
    mask_red = cv.inRange(hsv, lower_red, upper_red)
    mask_blue = cv.inRange(hsv, lower_blue, upper_blue)
    mask_green = cv.inRange(hsv, lower_green, upper_green)

    # Bitwise-AND masks and original frame
    res_red = cv.bitwise_and(frame, frame, mask=mask_red)
    res_blue = cv.bitwise_and(frame, frame, mask=mask_blue)
    res_green = cv.bitwise_and(frame, frame, mask=mask_green)

    # Display the frames
    cv.imshow('Original', frame)
    cv.imshow('Red Objects', res_red)
    cv.imshow('Blue Objects', res_blue)
    cv.imshow('Green Objects', res_green)
    
    key = cv.waitKey(1)

    # Save images when the "Q" key is pressed
    if key == ord('q') or key == ord('Q'):
        cv.imwrite(f'webcam_image_{counter}.jpg', frame)
        cv.imwrite(f'result_image_red{counter}.jpg', res_red)
        cv.imwrite(f'result_image_blue{counter}.jpg', res_blue)
        cv.imwrite(f'result_image_green{counter}.jpg', res_green)
        counter += 1
        
    if key == 27:
        break

# Release the capture and destroy windows
cap.release()
cv.destroyAllWindows()

