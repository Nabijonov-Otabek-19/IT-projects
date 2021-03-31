# WEB KAMERANI YOQISH

import cv2  # Opencv kutubxonasini import qilamiz

# Web kamerani yoqib olamiz
cap = cv2.VideoCapture(0)

# Sikl orqali ekranga to'xtovsiz chop qilib boramiz
while True:
    success, img = cap.read()

    # Ekranga chiqaramiz
    cv2.imshow("Video", img)

    # Agar esc bosilsa dastur tugatiladi
    if cv2.waitKey(1) == 27:
        break

cap.release()
