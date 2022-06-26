import tkinter as tk
from sayfa import AnaSayfa
from sayfa.film_listesi.FilmListesi import FilmListesi

class SagFrame:
    """
    ana sayfanın sağ tarafında sayfaları tutar
    """

    fon_rengi = 'orange'

    def __init__(self, window, name, relief=tk.SUNKEN, side=tk.LEFT):
        self.frame = tk.Frame(
            master=window,
            name=name,
            relief=relief,
            bg=SagFrame.fon_rengi
        )
        self.side = side
        self.frame_ekle()
    
    def frame_ekle(self):
        # frame içeriği
        self.frame_icerigi()
        self.frame.pack(side=self.side, fill=tk.BOTH, expand=True)

    def frame_icerigi(self, sayfa_adi='anaSayfa'):
        try:
            gelenFrame = self.frame
        except:
            gelenFrame = self
        finally:
            if(sayfa_adi == 'anaSayfa'):
                #ana sayfayı çağır
                AnaSayfa(gelenFrame, SagFrame.fon_rengi)
            elif sayfa_adi == 'filmListesi':
                #film listesi
                FilmListesi(gelenFrame, SagFrame.fon_rengi)
                pass
            elif sayfa_adi == 'filmDetayi':
                #film detay sayfası
                pass

    def destroy_children(frame):
        # frame içindeki tüm çocukları sil
        for child in frame.winfo_children():
            child.destroy()
