# import
import tkinter as tk
from tkinter import Text

# ana pencere
window = tk.Tk()
window.title('Tkinter Temelleri - Text')
window.geometry('600x400')

# Text Widget
txt = Text(master=window, width=40, height=2)


# yerleştir
txt.pack()

# mainloop
window.mainloop()