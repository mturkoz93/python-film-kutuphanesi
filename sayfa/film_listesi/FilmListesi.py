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
        self.frame.pack(side=self.side, fill=tk.BOTH, expand=True)

    def frame_basligi(self, baslik):
        bsl = tk.Label(
            self.frame, text=baslik, height=3,
            bg=COLORS.SIYAH, fg=COLORS.BEYAZ, font=('Arial', 12, 'bold')
        )

        bsl.grid(row=0, column=0, columnspan=8, padx=1, pady=(0,8), sticky='we')


