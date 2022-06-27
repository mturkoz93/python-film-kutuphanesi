import tkinter as tk
from data.colors import COLORS
from data.geometry import GEOMETRY

class Window:
    """
    Tkinter window nesnesi yaratan class.
    Window nesnesi root yani en temel nesnedir
    """

    # __init__ methodunda Tkinter window yaratalım
    def __init__(self, title):
        self.window = tk.Tk()
        self.window.title(title)
        self.window.configure(bg=COLORS.BLACK)
        self.set_height()


    def start_window(self):
        self.window.mainloop()

    def set_height(self):
        w, h = GEOMETRY.HOME_PAGE_WIDTH, GEOMETRY.HOME_PAGE_HEIGHT
        self.window.geometry('%dx%d' % (w, h))