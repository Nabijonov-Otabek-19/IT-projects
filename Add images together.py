# 2 TA RASMNI VERTIKAL VA GORIZONTAL QOSHISH

import cv2  # opencv kutubxonasini import qilamiz
import numpy as np  # numpy kutubxonasini import qilamiz

img1 = cv2.imread('Example1.jpg')  # 1-chi rasmni olamiz
img2 = cv2.imread('Example2.jpg')  # 2-chi rasmni olamiz

# ETIBOR BERING, IKKALA RASM PIKSEL HAJMI BIR XIL BO'LISHI SHART

print(img1.shape)
print(img2.shape)

# YOKI TURLI XIL PIKSEL HAJMDAGI RASMLARNI BIR XIL HAJMGA KELTIRIB OLAMIZ

img1 = cv2.resize(img1, (0, 0), None, 0.4, 0.4)
img2 = cv2.resize(img2, (0, 0), None, 0.4, 0.4)

hor = np.hstack((img1, img2))  # 2ta rasmni gorizontal holda birlashtiramiz
ver = np.vstack((img1, img2))  # 2ta rasmni vertikal holda birlashtiramiz

# imshow() funksiyasi orqali ekranga chiqaramiz
cv2.imshow('Vertical', ver)  # vertikal qo'shilgan rasmlarni ekranga chiqaramiz
cv2.imshow('Horizontal', hor)  # gorizontal qo'shilgan rasmlarni ekranga chiqaramiz

# Natija ekranda uzoq vaqt turishi uchun waitKey() funksiyasidan foydalanamiz
cv2.waitKey(0)
