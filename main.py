"""
Film Kütüphanesi
Sayfalar:
    1- Ana Sayfa
    2- Film Listesi
    3- Film Detayı
"""

from widget import Window, LeftFrame, RightFrame

if __name__ == '__main__':
    pencere = Window('Film Kütüphanesi')

    # Ana Pencere


    # Sol Frame
    sol_frame = LeftFrame(pencere.window, 'leftFrame')



    # Sağ Frame
    sag_frame = RightFrame(pencere.window, 'rightFrame')


    # penceremizi başlat -> mainloop()
    pencere.start_window()