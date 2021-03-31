# ODDIY FACE DETECTION YASASH

import cv2  # Opencv kutubxonasini import qilamiz

# cascade faylni o'qiymiz
face_cascade = cv2.CascadeClassifier('Haar_cascades/haarcascade_frontalface_alt2.xml')

# Kamerani yoqamiz
cap = cv2.VideoCapture(0)

# Sikl orqali to'xtovsiz ekranga chop qilamiz
while (True):
    ret, frame = cap.read()

    # Har bir tasvirni kulrang qilamiz
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Yuz atrofini aniqlab olamiz
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)

    # Sikl orqali yuz atrofiga ramka chizamiz
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Ekranga chiqaramiz
    cv2.imshow('frame', frame)

    # Agar esc bosilsa dastur tugatiladi
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
