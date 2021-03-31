# FACE LARNI SANASH / COUNT HOW MANY FACES IN THE AREA

import cv2  # Opencv kutubxonasini import qilamiz

# Cascade faylni o'qiymiz
face_cascade = cv2.CascadeClassifier('Haar_cascades/haarcascade_frontalface_alt2.xml')

# Kamerani yoqamiz
cap = cv2.VideoCapture(0)

# Sikl orqali to'xtovsiz ekranga chop qilamiz
while (True):
    ret, frame = cap.read()

    # Har bir tasvirni kulrang qilamiz
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Yuz chegaralarini aniqlaymiz
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

    # Sikl orqali yuz atrofiga ramka chizamiz
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Yuzlar sonini aniqlaymiz
    numbers = str(len(faces))

    # Ekranga matn chiqaramiz
    cv2.putText(frame, "Soni = " + numbers, (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    # Ekranga chiqaramiz
    cv2.imshow('gray', frame)

    # Agar esc bosilsa dastur tugatiladis
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
