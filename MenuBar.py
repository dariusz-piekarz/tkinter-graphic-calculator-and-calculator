from share import Share
from tkinter import Menu


class MenuBar(Menu, Share):
    def __init__(self, parent, fun_names):
        super().__init__(parent)
        __thisMenuBar = Menu(self, tearoff=0)

        __thisSubMenu = Menu(__thisMenuBar, tearoff=0)

        __thisFileMenu = Menu(__thisMenuBar, tearoff=0)
        __thisWindowMenu = Menu(__thisMenuBar, tearoff=0)
        __thisCommandMenu = Menu(__thisMenuBar, tearoff=0)
        __thisHelpMenu = Menu(__thisMenuBar, tearoff=0)

        __thisFileMenu.add_command(label="Save picture", command=fun_names['save'])
        __thisFileMenu.add_command(label="Exit app", command=fun_names['quite'])

        __thisMenuBar.add_cascade(label="File", menu=__thisFileMenu)

        __thisCommandMenu.add_command(label="Calculator", command=fun_names['calc'])
        __thisCommandMenu.add_command(label="Graphic calculator", command=fun_names['graphic'])

        __thisMenuBar.add_cascade(label="Menu", menu=__thisCommandMenu)
        __thisMenuBar.add_cascade(label="Window", menu=__thisWindowMenu)

        __thisSubMenu.add_command(label="Alt", command=fun_names['alt'])
        __thisSubMenu.add_command(label="Clam", command=fun_names['clam'])
        __thisSubMenu.add_command(label="Classic", command=fun_names['classic'])
        __thisSubMenu.add_command(label="Classic new", command=fun_names['classicn'])
        __thisSubMenu.add_command(label="Dark", command=fun_names['dark'])
        __thisSubMenu.add_command(label="Default", command=fun_names['def'])
        __thisSubMenu.add_command(label="Winnative", command=fun_names['win'])
        __thisSubMenu.add_command(label="Xpnative", command=fun_names['xp'])

        __thisWindowMenu.add_cascade(label="Themes", menu=__thisSubMenu)
        __thisWindowMenu.add_command(label="Line style", command=fun_names['custom_theme'])

        __thisMenuBar.add_cascade(label="Help", menu=__thisHelpMenu)
        __thisHelpMenu.add_command(label="How to use Calculator", command=fun_names['calc_help'])
        __thisHelpMenu.add_command(label="How to use Graphic Calculator", command=fun_names['gr_calc_help'])

        # this command display menu, if __thisMenuBar was self. argument, then it does not work
        parent.config(menu=__thisMenuBar)

# the author: Dariusz Piekarz
