import tkinter as tk

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
        if(sayfa_adi == 'anaSayfa'):
            #ana sayfayı çağır
            pass
        elif sayfa_adi == 'filmListesi':
            #film listesi
            pass
        elif sayfa_adi == 'filmDetayi':
            #film detay sayfası
            pass

