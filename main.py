"""
Film Kütüphanesi
Sayfalar:
    1- Ana Sayfa
    2- Film Listesi
    3- Film Detayı
"""

from widget import Window, SolFrame

if __name__ == '__main__':
    pencere = Window('Film Kütüphanesi')

    # Ana Pencere


    # Sol Frame
    sol_frame = SolFrame(pencere.window, 'solFrame')



    # Sağ Frame


    # penceremizi başlat -> mainloop()
    pencere.start_window()