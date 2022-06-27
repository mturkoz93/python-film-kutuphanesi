import tkinter as tk
from tkinter import ttk
from data.colors import COLORS
import csv
from PIL import Image, ImageTk
from page.movie_detail.MovieDetail import MovieDetail

class MovieList:
    """
    film listesi frame'dir
    """

    page_no = 1
    page_per = 10
    total_page_count = 0
    columns = ['imdbID', 'Id', 'Title', 'Year', 'imdbRating', 'imdbVotes']

    def __init__(self, master, bg_color, relief=tk.SUNKEN, side=tk.LEFT):
        self.frame = tk.Frame(
            master=master,
            name='movieList',
            relief=relief,
            bg=bg_color,
        )
        self.side = side
        self.movies = []
        self.add_frame()

    def add_frame(self):
        self.frame_title('Movie List')
        self.csv_read()
        self.create_page()
        self.frame.pack(side=self.side, fill=tk.BOTH, expand=True)

    def frame_title(self, title):
        bsl = tk.Label(
            self.frame, text=title, height=3,
            bg=COLORS.BLACK, fg=COLORS.WHITE, font=('Arial', 12, 'bold')
        )

        bsl.grid(row=0, column=0, columnspan=8, padx=1, pady=(0,8), sticky='we')

    def csv_read(self):
        read_movie = 'data/imdb_top_250.csv'
        with open(read_movie, 'r') as file:
            film_dict = csv.DictReader(file, delimiter=';')
            for movie in film_dict:
                self.movies.append(movie)
        
        # toplam page sayısı hesapla
        MovieList.total_page_count = len(self.movies) // MovieList.page_per + 1


    def create_page(self):
        self.add_title_row()
        self.create_table()
        self.create_combo_box()

    def add_title_row(self):
        for j, column in enumerate(MovieList.columns):
            if column != 'imdbID':
                lbl = tk.Label(
                    self.frame, text=str(column),
                    width=54,
                    height=2,
                    bg=COLORS.BLACK,
                    fg='white',
                    font=('Arial', 10, 'bold')
                )
                if column == 'Id':
                    lbl.configure(text='#', width=4)
                elif column == 'Title':
                    lbl.configure(text='Movie Title')
                elif column == 'Year':
                    lbl.configure(text='Year', width=8)
                elif column == 'imdbRating':
                    lbl.configure(text='Score', width=8)
                elif column == 'imdbVotes':
                    lbl.configure(text='Number of Votes', width=12)

                if column == 'imdbVotes':
                    lbl.grid(row=1, column=j, sticky='we', padx=(0, 10))
                else:
                    lbl.grid(row=1, column=j, sticky='we', padx=(0, 1))


    def create_table(self):
        for i, film in enumerate(self.movies):
            if (MovieList.page_no - 1) * MovieList.page_per <= i < MovieList.page_no * MovieList.page_per:
                for j, key in enumerate(MovieList.columns):
                    name = 'table_row_' + str(i) + str(j) + '_' + film['imdbID']
                    if j == 0:
                        # resim bastır
                        self.render_image(film, i, j, name)
                    else:
                        # yazı bastır
                        self.write_label(film, i, j, key, name)

            self.i = i + 3

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

        lbl.bind('<Button-1>', self.movie_click)
        
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

        self.fill_bg(lbl, i)
        
        if key == 'imdbVotes':
            lbl.grid(row=i + 2, column=j, sticky='we', padx=(0, 10))
        else:
            lbl.grid(row=i + 2, column=j, sticky='we', padx=(0, 1))

    def fill_bg(self, widget, i):
        if i % 2 == 1:
            widget.configure(bg=COLORS.LIST_ROW_ODD)
        else:
            widget.configure(bg=COLORS.LIST_ROW_EVEN)

    def combo_box_selected_event(self, event):
        MovieList.page_no = int(event.widget.get())
        self.destroy_table(event)
        self.create_table()


    def create_combo_box(self):
        values = list(range(1, MovieList.total_page_count))
        pages = ttk.Combobox(self.frame, width=4, values=values)
        pages.current(MovieList.page_no - 1) # sıfırınca indeksten başlaması için
        pages.bind('<<ComboboxSelected>>', self.combo_box_selected_event)
        pages.grid(row=self.i, column=2, pady=(15, 0))

    def destroy_table(self, event):
        master = event.widget.master
        for child in master.children.copy():
            if 'table_row' in child:
                master.children[child].destroy()

    def movie_click(self, event):
        imdbID = str(event.widget).split('_')[3]

        # önce sağ frame için düzenle
        self.edit_right_frame(event, imdbID)

        # sol frame'i düzenle
        self.edit_left_frame(event)

    def edit_right_frame(self, event, imdbID):
        rightFrame = event.widget.master
        for child in rightFrame.winfo_children():
            child.destroy()

        # film detayı yaz
        MovieDetail(rightFrame, 'orange', imdbID=imdbID, movies=self.movies)

    def edit_left_frame(self, event):
        root = event.widget.master.master.master
        for child in root.winfo_children():
            if str(child) == '.leftFrame':
                for ch in child.winfo_children():
                    if str(ch) == '.leftFrame.movieDetail':
                        ch.configure(bg=COLORS.ORANGE, fg=COLORS.WHITE)
                    else:
                        ch.configure(bg=COLORS.BLACK, fg=COLORS.ORANGE)

