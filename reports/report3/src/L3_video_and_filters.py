import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

# Get current width of frame
width = cap.get(cv.CAP_PROP_FRAME_WIDTH)   # float
# Get current height of frame
height = cap.get(cv.CAP_PROP_FRAME_HEIGHT) # float
# Define Video Frame Rate in fps
fps = 30.0

# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'XVID')
filtered_video = cv.VideoWriter('Filtered.avi', fourcc, fps, (int(width),int(height)) )
raw_video = cv.VideoWriter('Raw.avi', fourcc, fps, (int(width),int(height)) )
mask_video= cv.VideoWriter('Mask.avi', fourcc, fps, (int(width),int(height)) )
final_video = cv.VideoWriter('Track.avi', fourcc, fps, (int(width),int(height)) )

current_filter = 0
while(1):
    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame,frame, mask= mask)


    ## Aplica um filtro caso selecionado
    match current_filter:
        case 1:
            filtered = cv.blur(res,(5,5))
        case 2:
            filtered = cv.medianBlur(res,5)
        case 3:
            filtered = cv.GaussianBlur(res,(5,5),0)
        case 4:
            filtered = cv.bilateralFilter(res,9,75,75)
        case _:
            filtered = res

    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break

    ## Salva a imagem e o vídeo  ao apertar a tecla 's'
    elif k == ord('s'):
        cv.imwrite("Raw.png", frame)
        cv.imwrite("Mask.png", mask)
        cv.imwrite("Final.png", res)
        cv.imwrite("Filtered.png", filtered)
        
        raw_video.release()
        mask_video.release()
        final_video.release()
        filtered_video.release()

    ## Seleciona o filtro da média ao apertar 'm'
    elif k == ord('m'):
        current_filter = 1

    ## Seleciona o filtro da mediana ao apertar 'e'
    elif k == ord('e'):
        current_filter = 2

    ## Seleciona o filtro gaussiano ao apertar 'g'
    elif k == ord('g'):
        current_filter = 3

    ## Seleciona o filtro bilinear ao apertar 'b'
    elif k == ord('b'):
        current_filter = 4

    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    cv.imshow('res',res)
    cv.imshow('filtered', filtered)

    # Write frames to the video
    raw_video.write(frame)
    mask_video.write(mask)
    final_video.write(res)
    filtered_video.write(filtered)


cv.destroyAllWindows()
