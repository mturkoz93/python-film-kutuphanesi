import tkinter as tk
from data.colors import COLORS


# Wrapper class'lar -> Kapsayıcı
class Button:
    """
    Tkinter button yaratan class
    """

    def __init__(self, master, name, text, 
        fg, bg, en, boy, 
        handle_click,
        padx=0, pady=0, side=tk.TOP):
        self.button = tk.Button(
            master=master,
            name=name,
            text=text,
            fg=fg,
            bg=bg,
            width=en,
            height=boy,
            activebackground=COLORS.ORANGE
        )
        self.padx = padx
        self.pady = pady
        self.side = side
        self.add_button()
        self.bind_event(handle_click)

    def add_button(self):
        self.button.configure(font=('Arial', 12))
        self.button.pack(
            padx=self.padx,
            pady=self.pady,
            side=self.side
        )


    def bind_event(self, handle_click):
        self.button.bind('<Button-1>', handle_click) # sol menu click