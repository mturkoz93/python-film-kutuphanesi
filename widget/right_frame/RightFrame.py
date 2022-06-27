import tkinter as tk
from page import HomePage, MovieList, MovieDetail, About
# from page.film_listesi.MovieList import MovieList

class RightFrame:
    """
    ana sayfanın sağ tarafında sayfaları tutar
    """

    bg_color = 'orange'

    def __init__(self, window, name, relief=tk.SUNKEN, side=tk.LEFT):
        self.frame = tk.Frame(
            master=window,
            name=name,
            relief=relief,
            bg=RightFrame.bg_color
        )
        self.side = side
        self.add_frame()
    
    def add_frame(self):
        # frame içeriği
        self.frame_content()
        self.frame.pack(side=self.side, fill=tk.BOTH, expand=True)

    def frame_content(self, page_name='homePage'):
        try:
            comingFrame = self.frame
        except:
            comingFrame = self
        finally:
            if(page_name == 'homePage'):
                #ana sayfayı çağır
                HomePage(comingFrame, RightFrame.bg_color)
            elif page_name == 'movieList':
                #film listesi
                MovieList(comingFrame, RightFrame.bg_color)
            elif page_name == 'movieDetail':
                #film detay sayfası
                MovieDetail(comingFrame, RightFrame.bg_color)
            elif page_name == 'aboutApp':
                About(comingFrame, RightFrame.bg_color)

    def destroy_children(frame):
        # frame içindeki tüm çocukları sil
        for child in frame.winfo_children():
            child.destroy()
