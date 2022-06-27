import tkinter as tk
from PIL import Image, ImageTk

class HomePage:
    """
    ana page frame'dir.
    """

    def __init__(self, window, bg_color, relief=tk.SUNKEN, side=tk.LEFT):
        self.frame = tk.Frame(
            master=window,
            name='homePage',
            relief=relief,
            bg=bg_color
        )
        self.side = side
        self.frame_content()
        self.add_frame()

    def add_frame(self):
        self.frame.pack(side=self.side, fill=tk.BOTH, expand=True)

    def frame_content(self):
        name = tk.Label(self.frame,
                        text='Mustafa Türköz',
                        font=('Helvetica', 18, 'bold'),
                        bg='orange'
                        )
        name.place(x=324, y=105)

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
