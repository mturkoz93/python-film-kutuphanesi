import tkinter as tk
from data.colors import COLORS
from data.geometry import GEOMETRI

class Window:
    """
    Tkinter window nesnesi yaratan class.
    Window nesnesi root yani en temel nesnedir
    """

    # __init__ methodunda Tkinter window yaratalım
    def __init__(self, title):
        self.window = tk.Tk()
        self.window.title(title)
        self.window.configure(bg=COLORS.SIYAH)
        self.yukseklilk_ayarla()


    def start_window(self):
        self.window.mainloop()

    def yukseklilk_ayarla(self):
        w, h = GEOMETRI.ANA_SAYFA_GENISLIK, GEOMETRI.ANA_SAYFA_YUKSEKLIK
        self.window.geometry('%dx%d' % (w, h))