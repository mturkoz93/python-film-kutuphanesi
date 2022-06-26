import imp
import tkinter as tk
from tkinter import ttk
from data.colors import COLORS
import csv
from PIL import Image, ImageTk

class FilmListesi:
    """
    film listesi frame'dir
    """

    sutunlar = ['imdbID', 'Id', 'Title', 'Year', 'imdbRating', 'imdbVotes']

    def __init__(self, master, fon_rengi, relief=tk.SUNKEN, side=tk.LEFT):
        self.frame = tk.Frame(
            master=master,
            name='filmListesi',
            relief=relief,
            bg=fon_rengi,
        )
        self.side = side
        self.filmler = []
        self.frame_ekle()

    def frame_ekle(self):
        self.frame_basligi('Film Listesi')
        self.csv_oku()
        self.sayfa_olustur()
        self.frame.pack(side=self.side, fill=tk.BOTH, expand=True)

    def frame_basligi(self, baslik):
        bsl = tk.Label(
            self.frame, text=baslik, height=3,
            bg=COLORS.SIYAH, fg=COLORS.BEYAZ, font=('Arial', 12, 'bold')
        )

        bsl.grid(row=0, column=0, columnspan=8, padx=1, pady=(0,8), sticky='we')

    def csv_oku(self):
        film_oku = 'data/imdb_top_250.csv'
        with open(film_oku, 'r') as dosya:
            film_dict = csv.DictReader(dosya, delimiter=';')
            for film in film_dict:
                self.filmler.append(film)

    def sayfa_olustur(self):
        self.add_title_row()
        # self.tablo_olustur()

    def add_title_row(self):
        for j, sutun in enumerate(FilmListesi.sutunlar):
            if sutun != 'imdbID':
                lbl = tk.Label(
                    self.frame, text=str(sutun),
                    width=54,
                    height=2,
                    bg=COLORS.SIYAH,
                    fg='white',
                    font=('Arial', 10, 'bold')
                )
                if sutun == 'Id':
                    lbl.configure(text='#', width=4)
                elif sutun == 'Title':
                    lbl.configure(text='Film Adı')
                elif sutun == 'Year':
                    lbl.configure(text='Yıl', width=8)
                elif sutun == 'imdbRating':
                    lbl.configure(text='Puanı', width=8)
                elif sutun == 'imdbVotes':
                    lbl.configure(text='Oy Sayısı', width=12)

                if sutun == 'imdbVotes':
                    lbl.grid(row=1, column=j, sticky='we', padx=(0, 10))
                else:
                    lbl.grid(row=1, column=j, sticky='we', padx=(0, 1))



