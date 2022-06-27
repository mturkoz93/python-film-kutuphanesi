import tkinter as tk
from data.colors import COLORS

class About:
    """
    about app
    """

    def __init__(self, window, fon_rengi, relief=tk.SUNKEN, side=tk.LEFT):
        self.frame = tk.Frame(
            master=window,
            name='uygulamaHakkinda',
            relief=relief,
            bg=fon_rengi
        )
        self.side = side

        self.frame_ekle()

    def frame_ekle(self):
        self.frame_icerigi()
        self.frame_basligi('About App')
        self.frame.pack(side=self.side, fill=tk.BOTH, expand=True)

    def frame_basligi(self, baslik):
        bsl = tk.Label(
            self.frame, text=baslik, height=3,
            bg=COLORS.SIYAH, fg=COLORS.BEYAZ, font=('Arial', 12, 'bold')
        )
        bsl.pack(fill=tk.X, padx=(1, 0))

    def frame_icerigi(self):
        about = tk.Label(self.frame,
                        text='IMDB Movie Library',
                        font=('Helvetica', 18, 'bold'),
                        bg='orange'
                        )
        about.place(x=335, y=90)