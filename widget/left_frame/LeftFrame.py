import tkinter as tk
from data.colors import COLORS
from data.menus import MENU

from widget.button.Button import Button
from widget.right_frame.RightFrame import RightFrame


class LeftFrame:
    """
    sayfanın sol tarafında menü butonlarını tutar
    """

    def __init__(self, window, name):
        self.frame = tk.Frame(
            master=window,
            name=name,
            bg=COLORS.BLACK
        )
        self.master = window
        self.add_menus()
        self.add_frame()


    def add_frame(self):
        self.frame.pack(side=tk.LEFT, fill=tk.Y, pady=(62, 0))

    # click edilecek butondan gelecek event
    def handle_click(self, event):
        self.manage_to_button_colors(event)
        page_name = str(event.widget).split('.')[2]

        # sağ frame'i al
        sgFrame = self.master.children['rightFrame']

        # sağ frame içerisindeki tüm çocukları destroy et
        RightFrame.destroy_children(sgFrame)
        RightFrame.frame_content(sgFrame, page_name)



    def add_menus(self):
        # Buttonları döngü ile ekle
        for menu_key, menu_text in MENU.items():
            if menu_key == 'aboutApp':
                button = Button(self.frame, menu_key, menu_text, COLORS.ORANGE, COLORS.BLACK, 18, 2, self.handle_click, 0, 0, tk.BOTTOM)
            else:
                button = Button(self.frame, menu_key, menu_text, COLORS.ORANGE, COLORS.BLACK, 18, 2, self.handle_click)

                if menu_key == 'homePage':
                    LeftFrame.selected_button_color(button.button)

    def manage_to_button_colors(self, event):
        # tıklanan button : event.widget
        # hepsini siyah yap
        for child in event.widget.master.winfo_children():
            child.configure(bg=COLORS.BLACK, fg=COLORS.ORANGE)
        # seçili olanı turuncu yap
        LeftFrame.selected_button_color(event.widget)

    def selected_button_color(button):
        button.configure(bg=COLORS.ORANGE, fg=COLORS.WHITE)