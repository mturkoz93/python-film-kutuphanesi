# import
import tkinter as tk

# ana pencere
window = tk.Tk()
window.title('Tkinter Temelleri - CheckButton')
window.geometry('600x400')

# CheckButton Widget
chkBtn_1 = tk.Checkbutton(master=window, text='Doğru')
chkBtn_2 = tk.Checkbutton(master=window, text='Yanlış')


# yerleştir
chkBtn_1.grid(row=0, column=0)
chkBtn_2.grid(row=1, column=0)


# mainloop
window.mainloop()