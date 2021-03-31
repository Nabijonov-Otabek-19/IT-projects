# VEB KAMERANI HAJMINI OZGARTIRIB YOQISH

import cv2  # Opencv kutubxonasini import qilamiz

frameWidth = 640  # kamera kengligini belgilimiz
frameHeight = 480  # kamera balandligini belgilimiz

cap = cv2.VideoCapture(0)  # Kamerani yoqamiz

# Kamera hajmini kengaytiramiz
cap.set(3, frameWidth)
cap.set(4, frameHeight)

# Sikl orqali to'xtovsiz ekranga chop qilamiz
while True:
    success, img = cap.read()

    # Har bir frame ni kengaytiramiz
    img = cv2.resize(img, (frameWidth, frameHeight))

    # EKranga chiqaramiz
    cv2.imshow("Video", img)

    # Agar esc bosilsa dastur tugatiladi
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
