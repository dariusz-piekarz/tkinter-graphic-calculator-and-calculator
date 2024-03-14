from share import Share
from tkinter import Tk
from matplotlib.pyplot import figure
from Style import StyleClass
from MenuBar import MenuBar
from Frame1 import Frame1
from Frame2 import Frame2
from CustomTheme import CustomTheme
from tkinter.filedialog import asksaveasfilename
from Help_info import HelpInfo


class Grapher(Share):
    __root = Tk()
    # Set up the root widget
    style = StyleClass()
    picture = figure()

    def __init__(self, **kwargs):

        try:
            self.__thisWidth = kwargs['width']
        except KeyError:
            pass
        try:
            self.__thisHeight = kwargs['height']
        except KeyError:
            pass
        self.__root.title("Grapher")
        self.bg_color = 'white'
        screenWidth = self.__root.winfo_screenwidth()
        screenHeight = self.__root.winfo_screenheight()
        left = (screenWidth / 2) - (self.__thisWidth / 2)
        top = (screenHeight / 2) - (self.__thisHeight / 2)
        Share.window_width = left
        Share.window_height = top
        Share.total_width = self.__thisWidth
        Share.total_height = self.__thisHeight
        self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth, self.__thisHeight, left, top))
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_columnconfigure(0, weight=1)
        self.__thisMenuBar = MenuBar(self.__root, {'quite': self.__quitApplication, 'graphic': self.choose_graphic,
                                                    'calc': self.choose_calculator, 'alt': self.alt_theme,
                                                    'clam': self.clam_theme, 'classic': self.classic_theme,
                                                    'classicn': self.default_theme, 'dark': self.dark_theme,
                                                    'def': self.vista_theme, 'win': self.winnative_theme,
                                                    'xp': self.xpnative_theme, 'save': self.save,
                                                    'custom_theme': self.custom_theme,
                                                   'gr_calc_help': self.gr_calc_help, 'calc_help': self.calc_help})
        self.__calculator = Frame2(self.__root)
        self.__graphic_calc = Frame1(self.__root)
        self.__graphic_calc.pack_forget()

    def custom_theme(self):
        self.custom_theme = CustomTheme(self.__root)

    def alt_theme(self):
        self.style.set_theme('alt')
        Share.plot_style = dict({'bg_plot_color': "white", 'ax_plot_color': "white",
                                 'line_plot_color': "blue", 'line_thickness': 1})
        self.__graphic_calc.config(background="#d9d9d9")
        self.__calculator.config(background="#d9d9d9")

    def winnative_theme(self):
        self.style.set_theme('winnative')
        Share.plot_style = dict({'bg_plot_color': "white", 'ax_plot_color': "white",
                                 'line_plot_color': "blue", 'line_thickness': 1})
        self.__graphic_calc.config(background="SystemButtonFace")
        self.__calculator.config(background="SystemButtonFace")

    def xpnative_theme(self):
        self.style.set_theme('xpnative')
        Share.plot_style = dict({'bg_plot_color': "white", 'ax_plot_color': "white",
                                 'line_plot_color': "blue", 'line_thickness': 1})
        self.__graphic_calc.config(background="SystemButtonFace")
        self.__calculator.config(background="SystemButtonFace")

    def clam_theme(self):
        self.style.set_theme('clam')
        Share.plot_style = dict({'bg_plot_color': "#f9f7f2", 'ax_plot_color': "#f9f7f2",
                                 'line_plot_color': "blue", 'line_thickness': 1})
        self.__graphic_calc.config(background="#dcdad5")
        self.__calculator.config(background="#dcdad5")

    def vista_theme(self):
        self.style.set_theme('vista')
        Share.plot_style = dict({'bg_plot_color': "white", 'ax_plot_color': "white",
                                 'line_plot_color': "blue", 'line_thickness': 1})
        self.__graphic_calc.config(background="SystemButtonFace")
        self.__calculator.config(background="SystemButtonFace")

    def classic_theme(self):
        self.style.set_theme('classic')
        Share.plot_style = dict({'bg_plot_color': "white", 'ax_plot_color': "white",
                                 'line_plot_color': "blue", 'line_thickness': 1})
        self.__graphic_calc.config(background="#d9d9d9")
        self.__calculator.config(background="#d9d9d9")

    def default_theme(self):
        self.style.set_theme('default')
        Share.plot_style = dict({'bg_plot_color': "white", 'ax_plot_color': "white",
                                 'line_plot_color': "blue", 'line_thickness': 1})
        self.__graphic_calc.config(background="#d9d9d9")
        self.__calculator.config(background="#d9d9d9")

    def dark_theme(self):
        self.style.set_theme('dark')
        Share.plot_style = dict({'bg_plot_color': "grey", 'ax_plot_color': "grey",
                                 'line_plot_color': "blue", 'line_thickness': 1})
        self.__graphic_calc.config(background="black")
        self.__calculator.config(background="black")

    def choose_graphic(self):
        self.__calculator.pack_forget()
        self.__graphic_calc.pack(fill='both', expand=True)

    def choose_calculator(self):
        # clear currently displayed window
        self.__graphic_calc.pack_forget()
        # display new window
        self.__calculator.pack(fill='both', expand=True)

    def save(self):
        self.picture = self.__graphic_calc.picture
        # call a window that allow to save the picture
        a = asksaveasfilename(filetypes=(("PNG Image", "*.png"), ("All Files", "*.*")), defaultextension='.png',
                              title="Window-2")
        self.picture.savefig(a)

    def run(self):
        # Run main application
        self.__root.mainloop()

    def __quitApplication(self):
        # quite main app
        self.__root.destroy()

    def gr_calc_help(self):
        self.gr_calculator_help = HelpInfo(self.__root, "How to use Graphic Calculator?",
                                           "Use proper mathematical syntax.\n You can choose variable name, "
                                           "for example 'x'.\n Specify all variable you are using.\n "
                                           "Default range for each variable is the interval [-1,1]\n"
                                           " Whenever you want to change the range you can specify it.")

    def calc_help(self):
        self.calculator_help = HelpInfo(self.__root, "How to use Calculator?",
                                           "You can use this calculator as any other calculator.\n Gamma stands for"
                                           "Euler gamma function.\n Roots can take complex values, and then they are"
                                           "printed as a list of roots.")

# the author: Dariusz Piekarz
