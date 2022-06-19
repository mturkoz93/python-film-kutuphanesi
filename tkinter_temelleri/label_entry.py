# import
import tkinter as tk
from tkinter import Label, Entry

# Label -> Metin Yazar
# Entry -> Metin Girişi Yapar

# ana pencere
window = tk.Tk()
window.title('Tkinter Temelleri - Label - Entry')
window.geometry('600x400')

# Label Widget
lblAd = Label(master=window, text='Adınız:')
lblSoyad = Label(window, text='Soyadınız:')

# Entry Widget
entAd = Entry(window, width=20)
entSoyad = Entry(window, width=20)

# yerleştir
lblAd.grid(row=0)
entAd.grid(row=0, column=1)
lblSoyad.grid(row=1)
entSoyad.grid(row=1, column=1)


# mainloop
window.mainloop()