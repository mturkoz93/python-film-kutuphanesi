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
        self.tablo_olustur()

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


    def tablo_olustur(self):
        for i, film in enumerate(self.filmler):
            for j, key in enumerate(FilmListesi.sutunlar):
                name = 'table_row' + str(i) + str(j) + '_' + film['imdbID']
                if j == 0:
                    # resim bastır
                    self.render_image(film, i, j, name)
                else:
                    # yazı bastır
                    self.write_label(film, i, j, key, name)

    def render_image(self, film, i, j, name):
        try:
            # resim var mı
            load = Image.open('images/posters_small/' + film['imdbID'] + '.jpg')
        except:
            # yoksa no_image'ı al
            load = Image.open('images/posters_small/no_image.jpg')
        finally:
            render = ImageTk.PhotoImage(load)
            img_label = tk.Label(self.frame, name=name, image=render, bg='orange')
            img_label.image = render
            img_label.grid(row=i + 2, column=j, padx=(7, 0), sticky='we')

    def write_label(self, film, i, j, key, name):
        lbl = tk.Label(self.frame, name=name, text=str(film[key]), height=4, fg='black', font=('Arial', 10, 'bold'),
            cursor='hand2')
        
        if key == 'Id':
            lbl.configure(width=4)
        elif key == 'Title':
            lbl.configure(width=54, anchor='w') # sola yasla
        elif key == 'Year':
            lbl.configure(width=8)
        elif key == 'imdbRating':
            lbl.configure(width=8)
        elif key == 'imdbVotes':
            lbl.configure(width=12)
        
        if key == 'imdbVotes':
            lbl.grid(row=i + 2, column=j, sticky='we', padx=(0, 10))
        else:
            lbl.grid(row=i + 2, column=j, sticky='we', padx=(0, 1))