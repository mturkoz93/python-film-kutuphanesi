import tkinter as tk
from data.colors import COLORS
from PIL import Image, ImageTk

class MovieDetail:
    """
    film detay frame'dir.
    """

    def __init__(self, window, bg_color, imdbID=None, movies=[], relief=tk.SUNKEN, side=tk.LEFT):
        self.frame = tk.Frame(
            master=window,
            name='movieDetail',
            relief=relief,
            bg=bg_color
        )
        self.side = side
        self.imdbID = imdbID
        self.movies = movies
        self.add_frame()

    def add_frame(self):
        self.frame_content()
        self.frame_title('Movie Detail')
        self.frame.pack(side=self.side, fill=tk.BOTH, expand=True)

    def frame_title(self, title):
        if self.imdbID != None:
            bsl = tk.Label(
                self.frame, text=self.film['Title'], height=3,
                bg=COLORS.BLACK, fg=COLORS.WHITE, font=('Arial', 12, 'bold')
            )
            
            bsl.grid(row=0, column=0, columnspan=8, padx=1, pady=(0,8), sticky='we')
        else:
            bsl = tk.Label(
                self.frame, text=title, height=3,
                bg=COLORS.BLACK, fg=COLORS.WHITE, font=('Arial', 12, 'bold')
            )
            bsl.pack(fill=tk.X, padx=(1, 0))

        

    def frame_content(self):
        if self.imdbID != None:
            self.render_image()
            self.get_film()
            self.render_keys()
            self.render_values()
        else:
            pass

    def render_image(self):
        try:
            # resim var mı
            load = Image.open('images/posters_large/' + self.imdbID + '.jpg')
        except:
            # yoksa no_image'ı al
            load = Image.open('images/posters_large/no_image.jpg')
        finally:
            render = ImageTk.PhotoImage(load)
            img_label = tk.Label(self.frame, image=render, bg='orange')
            img_label.image = render
            img_label.grid(row=1, column=0, columnspan=2, pady=(0, 10))
    
    def get_film(self):
        for f in self.movies:
            if f['imdbID'] == self.imdbID:
                self.film = f
                break

    def render_keys(self):
        for i, key in enumerate(self.film.keys()):
            txt = str(key)
            lbl = tk.Label(self.frame, text=txt, height=2, width=12, anchor='w')
            self.fill_bg(lbl, i)
            lbl.grid(row=i + 2, column=0, padx=(10, 1))

    def fill_bg(self, widget, i):
        if i % 2 == 1:
            widget.configure(bg=COLORS.LIST_ROW_ODD)
        else:
            widget.configure(bg=COLORS.LIST_ROW_EVEN)

    def render_values(self):
        for i, value in enumerate(self.film.values()):
            txt = str(value)
            lbl = tk.Label(self.frame, text=txt, height=2, width=96, anchor='w')
            self.fill_bg(lbl, i)
            lbl.grid(row=i + 2, column=1, padx=(0, 8))
