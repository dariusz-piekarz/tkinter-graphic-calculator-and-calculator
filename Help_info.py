from share import Share
from tkinter import Label, Toplevel


class HelpInfo(Toplevel, Share):

    def __init__(self, parent, title, text):
        if Share.help_counter == 0:
            Share.help_counter = 1
            Toplevel.__init__(self, parent)
            self.title(title)
            self.label = Label(self, text=text, justify='left')
            self.label.pack(padx=20, pady=20)
            self.geometry(f"450x150+{parent.winfo_screenwidth() // 2 - 150}+{parent.winfo_screenheight() // 2 - 75}")
            self.protocol("WM_DELETE_WINDOW", self.quit_toplevel)

    def quit_toplevel(self):
        self.destroy()
        Share.help_counter = 0

# the author: Dariusz Piekarz
