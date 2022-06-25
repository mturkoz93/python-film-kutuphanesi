"""
Film Kütüphanesi
Sayfalar:
    1- Ana Sayfa
    2- Film Listesi
    3- Film Detayı
"""

from widget import Window, SolFrame, SagFrame

if __name__ == '__main__':
    pencere = Window('Film Kütüphanesi')

    # Ana Pencere


    # Sol Frame
    sol_frame = SolFrame(pencere.window, 'solFrame')



    # Sağ Frame
    sag_frame = SagFrame(pencere.window, 'sagFrame')


    # penceremizi başlat -> mainloop()
    pencere.start_window()