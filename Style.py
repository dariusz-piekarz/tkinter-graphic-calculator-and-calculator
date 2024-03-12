from share import Share
from tkinter.ttk import Style


class StyleClass(Share):
    def __init__(self, style_name='vista'):
        self.style = Style()
        if 'dark' not in self.style.theme_names():
            self.dark_style()
        self.style.theme_use(style_name)

    def set_theme(self, style_name):
        self.style.theme_use(style_name)

    def dark_style(self):
        self.style.theme_create('dark', settings={".": {"configure": {"background": "black"}},
            "TButton": {"configure": {'background': "green", 'foreground': "white", 'padding': [2, 2, 2, 2],
                                      'relief': "groove", 'lightcolor': '#DF7401', 'borderwidth': 4,
                                      "anchor": "center"}},
            "TNotebook.Tab": {"configure": {'background': "green", 'foreground': "white", 'lightcolor': '#DF7401',
                                            'borderwidth': 2}},
            "TFrame": {"configure": {"background": "black", "foreground": "white"}},
            "TLabel": {"configure": {"background": "black", "foreground": "white"}},
            "TNotebook": {"configure": {"background": "black", "foreground": "white"}}})

# the author: Dariusz Piekarz
