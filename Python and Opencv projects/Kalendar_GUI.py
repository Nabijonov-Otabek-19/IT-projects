from tkinter import *  # Tkinter kutubxonani import qilamiz
import calendar  # Calendar kutubxonasini import qilamiz

# Yilni aniqlab olamiz
text = calendar.calendar(2021)

# GUI yaratamiz
root = Tk()
root.geometry("550x640")  # GUI hajmini belgilimiz
root.title("KALENDAR")  # GUI ni nomlaymiz

# GUI ga text qoyamiz
label1 = Label(root, text="KALENDAR", bg="dark gray", font=("times", 28, "bold"))
label1.grid(row=1, column=1)

# GUI orqa qismini rangini belgilimiz
root.config(background="white")

# GUI ga kalendar kunlari oylarini joylimiz
l1 = Label(root, text=text, font="consolas 10 bold")
l1.grid(row=2, column=1, padx=20)

root.mainloop()  # GUI cheksiz chop qilinadi
