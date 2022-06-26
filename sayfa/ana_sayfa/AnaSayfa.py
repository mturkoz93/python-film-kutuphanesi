import tkinter as tk
from PIL import Image, ImageTk

class AnaSayfa:
    """
    ana sayfa frame'dir.
    """

    def __init__(self, window, fon_rengi, relief=tk.SUNKEN, side=tk.LEFT):
        self.frame = tk.Frame(
            master=window,
            name='anaSayfa',
            relief=relief,
            bg=fon_rengi
        )
        self.side = side
        self.frame_icerigi()
        self.frame_ekle()

    def frame_ekle(self):
        self.frame.pack(side=self.side, fill=tk.BOTH, expand=True)

    def frame_icerigi(self):

        tanitim = tk.Label(self.frame,
                        text='Python App',
                        font=('Helvetica', 18, 'bold'),
                        bg='orange'
                        )
        tanitim.place(x=335, y=50)

        isim = tk.Label(self.frame,
                        text='Mustafa Türköz',
                        font=('Helvetica', 18, 'bold'),
                        bg='orange'
                        )
        isim.place(x=324, y=105)

        self.render_image()

        proje = tk.Label(self.frame,
                        text='Tkinter ile Film Kütüphanesi',
                        font=('Helvetica', 18, 'bold'),
                        bg='black',
                        fg='white'
                        )
        proje.place(x=240, y=765)


    def render_image(self):
        load = Image.open('images/home/AppLogo.png')
        render = ImageTk.PhotoImage(load)
        img_lbl = tk.Label(self.frame, image=render, bg='orange')
        img_lbl.image = render
        img_lbl.place(x=136, y=187)
