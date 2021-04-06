import cv2  # Opencv kutubxonasini import qilamiz
import numpy as np  # Numpy kutubxonasini import qilamiz

# Pyzbar dan decode ni import qilamiz, decode - qr kod nomi joylashgan joyini aniqlab beradi
from pyzbar.pyzbar import decode

# Kamerani yoqamiz
cam = cv2.VideoCapture(0)

cam.set(3, 640)
cam.set(4, 480)

while 1:
    ret, frame = cam.read()

    # Tasvirdan QR kodlarni aniqlaymiz
    for barcode in decode(frame):
        # QR kodni data sini olamiz
        myData = barcode.data.decode('utf-8')
        # print(barcode.data)

        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape((-1, 1, 2))
        # QR kod atrofiga rectangle chizamiz
        cv2.polylines(frame, [pts], True, (255, 0, 255), 5)
        pts2 = barcode.rect
        # QR kod ustiga text qoyamiz
        cv2.putText(frame, myData, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 255))

    # Ekranga tasvirlarni chiqaramiz
    cv2.imshow("frame", frame)

    # Agar esc bosilsa dastur toxtaydi
    if cv2.waitKey(1) == 27:
        break

cam.release()
cv2.destroyAllWindows()
