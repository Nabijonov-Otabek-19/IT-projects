# FACE VA EYES NI DETECTION QILISH SIMPLE USULI

import cv2

# Cascade larni import qilish
face_cascade = cv2.CascadeClassifier('Haar_cascades/haarcascade_frontalface_alt2.xml')
eye_cascade = cv2.CascadeClassifier('Haar_cascades/haarcascade_eye_tree_eyeglasses.xml')

cap = cv2.VideoCapture(0)

while (True):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)  # Scale larni detect qilish

    for (x, y, w, h) in faces:
        # print(x, y, w, h)  # Face koordinatalarini ekranga chiqaradi

        roi_gray = gray[x:x + w, y:y + h]  # (y_cord_start, y_cord_end)
        roi_color = frame[x:x + w, y:y + h]

        # Yuzni koordinatalarini aniqlab yuzni rasmga olish
        # Dasturni tugatganda rasmga oladi

        # img_item = "img_of_me.jpg"
        # cv2.imwrite(img_item, roi_gray)

        font = cv2.FONT_HERSHEY_COMPLEX
        color = (0, 255, 0)
        stroke2 = 2
        name = 'David Watson'

        # Detection object ga text yozish
        cv2.putText(frame, name, (x, y), font, 1, color, stroke2, cv2.LINE_AA)

        color = (255, 0, 0)  # BGR 0-255
        stroke = 2
        end_cord_x = x + w
        end_cord_y = y + h
        cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)

        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 0, 255), 2)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
