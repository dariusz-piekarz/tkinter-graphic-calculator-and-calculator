from share import Share
from tkinter.ttk import Entry, Label, Button
from tkinter import Frame, END
from string_var import calculator_symbols
from math_fun_and_var import *


class Frame2(Frame, Share):
    dftx = 2
    dfty = 1

    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        self.pack(fill='both', expand=True, anchor="center")
        self.input_cell = str()
        self.output_cell = str()
        self.inputs_cell()
        self.outputs_cell()
        self.labels()
        self.buttons()

    def inputs_cell(self):
        self.input_cell = Entry(self, self.input_cell, font='Arial 28')
        self.input_cell.grid(row=2+self.dfty, columnspan=1, column=2+self.dftx, padx=int(Share.window_width/4*1.35),
                             sticky="w")

    def outputs_cell(self):
        self.output_cell = Entry(self, self.output_cell, font='Arial 28')
        self.output_cell.grid(row=2+self.dfty, columnspan=1, column=3+self.dftx, padx=int(Share.window_width/4*0.75),
                              sticky="w")

    def insert_number(self, label):
        return lambda: self.input_cell.insert(END, label)

    def delete_entry(self):
        self.input_cell.delete(0, END)
        self.output_cell.delete(0, END)

    def delete_last_character(self):
        return lambda: self.input_cell.delete(len(self.input_cell.get())-1, END)

    def equal_action(self):
        self.output_cell.delete(0, END)
        self.output_cell.insert(END, eval(calculator_symbols(self.input_cell.get())))

    def eval_entry(self):
        return lambda: self.equal_action()

    def labels(self):

        empty_label_1 = Label(self, text="             ")
        empty_label_1.grid(row=1+self.dfty, column=1+self.dftx, sticky='w')
        empty_label_1.grid(row=2+self.dfty, column=1+self.dftx, sticky='w')
        empty_label_1.grid(row=1, column=1, sticky='w')
        eq_label = Label(self, text="=", width=1, font='Arial 28')
        eq_label.grid(row=2+self.dfty, column=2+self.dftx, sticky="e")
        empty_label_2 = Label(self, text=" ")
        empty_label_2.grid(row=3+self.dfty, column=2+self.dftx, ipady=20)
        const_label = Label(self, text="Constants:", font='Arial 28')
        const_label.grid(row=9+self.dfty, column=2+self.dftx, sticky="w")

    def button(self, label, parameters, action, width=39, hight=15):
        button = Button(self, text=label, command=action, width=width)
        button.grid(row=parameters[0]+self.dfty, column=parameters[1]+self.dftx, columnspan=parameters[2],
                    sticky=parameters[3], ipady=hight)

    def buttons(self):

        for i in range(3):
            self.button(f"{1+3*i}", [4+i, 2, 1, "w"], action=self.insert_number(f"{1+3*i}"))
            self.button(f"{2+3*i}", [4+i, 2, 1, "e"], width=40, action=self.insert_number(f"{2+3*i}"))
            self.button(f"{3+3*i}", [4+i, 3, 1, "w"], action=self.insert_number(f"{3+3*i}"))
        self.button(".", [7, 2, 1, "w"], action=self.insert_number("."))
        self.button("0", [7, 2, 1, "e"], width=40, action=self.insert_number("0"))
        self.button("%", [7, 3, 1, "w"], action=self.insert_number("%"))
        self.button(",", [8, 2, 1, "w"], width=39, action=self.insert_number(","))
        self.button("C", [8, 2, 1, "e"], width=40, action=self.delete_entry)
        self.button("Del", [8, 3, 1, "w"], action=self.delete_last_character())
        self.button(u"\u03C0", [10, 2, 1, "w"], action=self.insert_number("pi"))
        self.button(u"e", [10, 2, 1, "e"], width=40, action=self.insert_number("e"))
        self.button(u"\u03C6", [10, 3, 1, "w"], action=self.insert_number("phi"))
        self.button(u"\u03B3", [11, 2, 1, "w"], action=self.insert_number("gamma"))
        self.button("i", [11, 2, 1, "e"], width=40, action=self.insert_number("I"))
        self.button(u"g", [11, 3, 1, "w"], action=self.insert_number("g"))
        self.button("=", [4, 3, 1, "e"], width=20, action=self.eval_entry())
        self.button("+", [4, 4, 1, "w"], width=20, action=self.insert_number("+"))
        self.button("-", [4, 5, 1, "w"], width=20, action=self.insert_number("-"))
        self.button("*", [5, 4, 1, "w"], width=20, action=self.insert_number("*"))
        self.button("/", [5, 3, 1, "e"], width=20, action=self.insert_number("/"))
        self.button("^2", [5, 5, 1, "w"], width=20, action=self.insert_number("^2"))
        self.button("^n", [6, 5, 1, "w"], width=20, action=self.insert_number("^"))
        self.button("!", [6, 4, 1, "w"], width=20, action=self.insert_number("!"))
        self.button(u"\u0393", [6, 3, 1, "e"], width=20, action=self.insert_number("Gamma("))
        self.button("(", [7, 3, 1, "e"], width=20, action=self.insert_number("("))
        self.button(")", [7, 4, 1, "w"], width=20, action=self.insert_number(")"))
        self.button("|x|", [7, 5, 1, "w"], width=20, action=self.insert_number("abs("))
        self.button(u'\u221A', [8, 3, 1, "e"], width=20, action=self.insert_number("Sqrt("))
        self.button(u'\u221B', [8, 4, 1, "w"], width=20, action=self.insert_number("Cbrt("))
        self.button(f'\u207F\u221A', [8, 5, 1, "w"], width=20, action=self.insert_number("Nrt("))
        self.button("sin", [9, 3, 1, "e"], width=20, action=self.insert_number("sin("))
        self.button("cos", [9, 4, 1, "w"], width=20, action=self.insert_number("cos("))
        self.button("tan", [9, 5, 1, "w"], width=20, action=self.insert_number("tan("))
        self.button("asin", [10, 3, 1, "e"], width=20, action=self.insert_number("asin("))
        self.button("acos", [10, 4, 1, "w"], width=20, action=self.insert_number("acos("))
        self.button("atan", [10, 5, 1, "w"], width=20, action=self.insert_number("atan("))
        self.button(u"log\u2099", [11, 3, 1, "e"], width=20, action=self.insert_number("log("))
        self.button("ln", [11, 4, 1, "w"], width=20, action=self.insert_number("log("))
        self.button("exp", [11, 5, 1, "w"], width=20, action=self.insert_number("exp("))

# the author: Dariusz Piekarz
