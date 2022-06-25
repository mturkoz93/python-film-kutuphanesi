import tkinter as tk


class Window:
    """
    Tkinter window nesnesi yaratan class.
    Window nesnesi root yani en temel nesnedir
    """

    # __init__ methodunda Tkinter window yaratalım
    def __init__(self, title):
        self.window = tk.Tk()
        self.window.title(title)


    def start_window(self):
        self.window.mainloop()