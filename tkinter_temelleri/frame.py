# import
import tkinter as tk
from tkinter import Frame, Button

# Frame: Bir çok widgeti bir arada tutar.

# ana pencere
window = tk.Tk()
window.title('Tkinter Temelleri - Frame')
window.geometry('600x400')

# Frame Widget
frame = Frame(master=window)

# frame içini doldur
btnLeft = Button(master=frame, text='Frame Buttonu Left', bg='black', fg='white')
btnLeft.pack(side=tk.LEFT)

btnRight = Button(master=frame, text='Frame Buttonu Right', bg='black', fg='white')
btnRight.pack(side=tk.RIGHT)

# yerleştir
frame.pack()


# mainloop
window.mainloop()