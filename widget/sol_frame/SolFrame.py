import tkinter as tk
from data.colors import COLORS
from data.menus import MENU

from widget.button.Button import Button
from widget.sag_frame.SagFrame import SagFrame


class SolFrame:
    """
    sayfanın sol tarafında menü butonlarını tutar
    """

    def __init__(self, window, name):
        self.frame = tk.Frame(
            master=window,
            name=name,
            bg=COLORS.SIYAH
        )
        self.master = window
        self.menuleri_ekle()
        self.frame_ekle()


    def frame_ekle(self):
        self.frame.pack(side=tk.LEFT, fill=tk.Y, pady=(62, 0))

    # click edilecek butondan gelecek event
    def handle_click(self, event):
        self.buton_renklerini_yonet(event)
        sayfa_adi = str(event.widget).split('.')[2]

        # sağ frame'i al
        sgFrame = self.master.children['sagFrame']

        # sağ frame içerisindeki tüm çocukları destroy et
        SagFrame.destroy_children(sgFrame)
        SagFrame.frame_icerigi(sgFrame, sayfa_adi)



    def menuleri_ekle(self):
        # Buttonları döngü ile ekle
        for menu_key, menu_text in MENU.items():
            if menu_key == 'uygulamaHakkinda':
                button = Button(self.frame, menu_key, menu_text, COLORS.TURUNCU, COLORS.SIYAH, 18, 2, self.handle_click, 0, 0, tk.BOTTOM)
            else:
                button = Button(self.frame, menu_key, menu_text, COLORS.TURUNCU, COLORS.SIYAH, 18, 2, self.handle_click)

    def buton_renklerini_yonet(self, event):
        # tıklanan button : event.widget
        # hepsini siyah yap
        for child in event.widget.master.winfo_children():
            child.configure(bg=COLORS.SIYAH, fg=COLORS.TURUNCU)
        # seçili olanı turuncu yap
        self.secili_button_rengi(event.widget)

    def secili_button_rengi(self, button):
        button.configure(bg=COLORS.TURUNCU, fg=COLORS.BEYAZ)