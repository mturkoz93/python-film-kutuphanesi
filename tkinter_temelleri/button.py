# import
import tkinter as tk

# ana pencere
window = tk.Tk()
window.title('Tkinter Temelleri - Button')
window.geometry('600x400')

# Button Widget
btn = tk.Button(master=window,
                text='Durdur',
                width=45,
                height=5,
                bg='red',
                fg='white',
                command=window.destroy)

# btn'i yerleştir
btn.pack()

# mainloop
window.mainloop()