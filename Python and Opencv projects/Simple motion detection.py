import cv2

# ODDIY SODDA MOTION DETECTION

# BACKGROUNDNI OLIB TASHLASH

# fgbgl = cv2.createBackgroundSubtractorKNN()  # Shovqinsiz salgina

# Sal shovqinliroq
fgbgl = cv2.createBackgroundSubtractorMOG2(detectShadows=True)

cam = cv2.VideoCapture("count.mp4")

while 1:
    ret, frame = cam.read()

    # Backgroundni olib tashlash
    fgmask = fgbgl.apply(frame)

    _, thresh = cv2.threshold(fgmask, 254, 255, cv2.THRESH_BINARY)

    cv2.imshow('frame', frame)
    cv2.imshow('fgmask', thresh)

    if cv2.waitKey(1) == 27:
        break

cam.release()
cv2.destroyAllWindows()
