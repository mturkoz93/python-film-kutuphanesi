import tkinter as tk
from data.colors import COLORS

class About:
    """
    about app
    """

    def __init__(self, window, bg_color, relief=tk.SUNKEN, side=tk.LEFT):
        self.frame = tk.Frame(
            master=window,
            name='aboutApp',
            relief=relief,
            bg=bg_color
        )
        self.side = side

        self.add_frame()

    def add_frame(self):
        self.frame_content()
        self.frame_title('About App')
        self.frame.pack(side=self.side, fill=tk.BOTH, expand=True)

    def frame_title(self, title):
        bsl = tk.Label(
            self.frame, text=title, height=3,
            bg=COLORS.BLACK, fg=COLORS.WHITE, font=('Arial', 12, 'bold')
        )
        bsl.pack(fill=tk.X, padx=(1, 0))

    def frame_content(self):
        about = tk.Label(self.frame,
                        text='IMDB Movie Library',
                        font=('Helvetica', 18, 'bold'),
                        bg='orange'
                        )
        about.place(x=305, y=90)