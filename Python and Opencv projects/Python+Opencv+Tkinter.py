import cv2
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

white = "#ffffff"
lightBlue2 = "#adc5ed"
font = "Constantia"
fontButtons = (font, 12)
maxWidth = 800
maxHeight = 640

# Grafik oyna
mainWindow = tk.Tk()
mainWindow.configure(bg=lightBlue2)
mainWindow.geometry('%dx%d+%d+%d' % (maxWidth, maxHeight, 0, 0))
mainWindow.resizable(0, 0)

mainFrame = Frame(mainWindow)
mainFrame.place(x=70, y=70)

# Video tasvirlarni joylash
lmain = tk.Label(mainFrame)
lmain.grid(row=0, column=0)


def Tugadi():
    answer = tk.messagebox.askquestion("Are you sure ?", "Dastur tugatilsinmi ?")
    if answer == 'yes':
        mainWindow.destroy()


startButton = Button(mainWindow, text="START", font=fontButtons, bg=white, width=15, height=1)
startButton.place(x=200, y=570)
startButton.configure(command=lambda: show_frame())

closeButton = Button(mainWindow, text="QUIT", font=fontButtons, bg=white, width=15, height=1)
closeButton.configure(command=lambda: Tugadi())
closeButton.place(x=450, y=570)

cap = cv2.VideoCapture(0)


def show_frame():
    ret, frame = cap.read()

    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)

    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.configure(image=imgtk)
    lmain.imgtk = imgtk

    mainWindow.after(10, show_frame)


mainWindow.mainloop()  # GUI boshlanadi
