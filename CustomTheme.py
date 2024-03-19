from share import Share
from tkinter import ttk
from tkinter import Label, StringVar, Spinbox, Toplevel


class Nad(type):
    # this class prevent from a chance of opening the TopLevel window twice or more
    # alternatively it is possible to use Share class
    counter = 0

    def __new__(mcs, clsbase, clsname, clsdict, **kwargs):
        return super().__new__(mcs, clsbase, clsname, clsdict, **kwargs)

    def __call__(cls, *args, **kwargs):
        if Nad.counter in [1, 2]:
            Nad.counter = 2
        elif Nad.counter == 0:
            Nad.counter = 1
            return super().__call__(*args, **kwargs)


class CustomTheme(Toplevel, Share, metaclass=Nad):
    theme = dict({'bg_plot_color': "", 'ax_plot_color': "", 'line_plot_color': "", 'line_thickness': 1})

    def __init__(self, parent):
        if Nad.counter < 2:
            # parent is self.__root from the file core_app.py - to inherit properties of global app
            Toplevel.__init__(self, parent)
            self.title("Custom Theme")
            self.geometry("400x150+{}+{}".format(parent.winfo_screenwidth()//2-150, parent.winfo_screenheight()//2-75))
            self.labels()
            self.entries()
            self.button_apply()
            self.button_cancel()
            self.button_ok()
            # modifies action of [X] Exit red button of TopLevel widow
            self.protocol("WM_DELETE_WINDOW", self.quit_toplevel)

    def labels(self):
        plot_background_label = Label(self, text="Plot background color: ")
        axis_background_color_label = Label(self, text="Axis background color: ")
        line_color_label = Label(self, text="Line color: ")
        line_thickness_label = Label(self, text="Line thickness: ")
        plot_background_label.grid(row=1, column=1)
        axis_background_color_label.grid(row=2, column=1)
        line_color_label.grid(row=3, column=1)
        line_thickness_label.grid(row=4, column=1)

    def entries(self):
        plot_background_str = StringVar()
        axis_background_str = StringVar()
        line_str = StringVar()
        thickness_str = StringVar()
        self. plot_background_entry = ttk.Entry(self, textvariable=plot_background_str)
        self.axis_background_entry = ttk.Entry(self, textvariable=axis_background_str)
        self.thickness_entry = Spinbox(self, from_=1, to=10, textvariable=thickness_str, wrap=True)
        self.line_entry = ttk.Entry(self, textvariable=line_str)
        self.plot_background_entry.grid(row=1, column=2)
        self.axis_background_entry.grid(row=2, column=2)
        self.line_entry.grid(row=3, column=2)
        self.thickness_entry.grid(row=4, column=2)

    def send_style(self):
        self.theme['bg_plot_color'] = self.plot_background_entry.get()
        self.theme['ax_plot_color'] = self.axis_background_entry.get()
        self.theme['line_plot_color'] = self.line_entry.get()
        self.theme['line_thickness'] = self.thickness_entry.get()
        Share.plot_style = self.theme

    def send_style_and_close(self):
        self.theme['bg_plot_color'] = self.plot_background_entry.get()
        self.theme['ax_plot_color'] = self.axis_background_entry.get()
        self.theme['line_plot_color'] = self.line_entry.get()
        self.theme['line_thickness'] = self.thickness_entry.get()
        # Shares established values with other components of the app
        Share.plot_style = self.theme
        Nad.counter = 0
        self.destroy()

    def quit_toplevel(self):
        self.destroy()
        Nad.counter = 0

    def button_apply(self):
        plot_button = ttk.Button(self, text="Apply", command=self.send_style, width=10)
        plot_button.grid(row=7, column=2, columnspan=1, sticky='E')

    def button_ok(self):
        plot_button = ttk.Button(self, text="Ok", command=self.send_style_and_close, width=9)
        plot_button.grid(row=7, column=2, columnspan=2, sticky='W')

    def button_cancel(self):
        plot_button = ttk.Button(self, text="Cancel", command=self.quit_toplevel, width=10)
        plot_button.grid(row=7, column=1, columnspan=1, sticky='E')

# the author: Dariusz Piekarz
