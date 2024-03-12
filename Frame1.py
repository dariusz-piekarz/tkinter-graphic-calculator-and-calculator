from share import Share
from matplotlib.pyplot import figure, get_cmap
from tkinter import ttk
from tkinter import StringVar, Frame
from grapher import Draw
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Frame1(Frame, Share):
    __tabs = list()
    picture = figure()
    bg_color = 'white'
    ax_color = 'white'
    line_color = 'blue'
    line_thickness = 1
    own_style = dict({'bg_plot_color': "", 'ax_plot_color': "", 'line_plot_color': "", 'line_thickness': 1})

    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        self.__tabControl = ttk.Notebook(self, height=Share.total_height, width=Share.total_width)
        self.pack(fill='both', expand=True)
        self.tab('Simple Plot 2D', ["f(var) = "], ["lower limit="], ["upper limit="], ["var = "], "simple_2D")
        self.tab('Parametric Plot 2D', ['x(var) = ', 'y(var) = '], ["lower limit="], ["upper limit="], ["var = "],
                 "parametric_2D")
        self.tab('Polar Plot 2D', ["r(var)  ="], ["lower limit="], ["upper limit="], ["var = "], "polar_2D")
        self.tab('Implicit Plot 2D', ["0  ="], ["lower var\N{SUBSCRIPT ONE} limit=",
                                                "lower var\N{SUBSCRIPT TWO}  limit="],
                 ["upper var\N{SUBSCRIPT ONE} limit=", "upper var\N{SUBSCRIPT TWO} limit="],
                 ["var\N{SUBSCRIPT ONE} = ", "var\N{SUBSCRIPT TWO} = "], "implicit_2D")
        self.tab('Surface Plot 3D', ["f(var\N{SUBSCRIPT ONE},var\N{SUBSCRIPT TWO})   ="],
                 ["lower var\N{SUBSCRIPT ONE} limit=", "lower var\N{SUBSCRIPT TWO}  limit="],
                 ["upper var\N{SUBSCRIPT ONE} limit=", "upper var\N{SUBSCRIPT TWO}  limit="],
                 ["var\N{SUBSCRIPT ONE} = ", "var\N{SUBSCRIPT TWO} = "], "simple_3D")
        self.tab('Curve Parametric Plot 3D', ["x(var) =", "y(var) =", "z(var) ="], ["lower limit="], ["upper limit="],
                 ["var = "], "curve_parametric_3D")
        self.tab('Surface Parametric Plot 3D', ["x(var\N{SUBSCRIPT ONE},var\N{SUBSCRIPT TWO} ) =",
                 "y(var\N{SUBSCRIPT ONE},var\N{SUBSCRIPT TWO} ) =", "z(var\N{SUBSCRIPT ONE},var\N{SUBSCRIPT TWO} ) ="],
                 ["lower var\N{SUBSCRIPT ONE} limit=", "lower var\N{SUBSCRIPT TWO}  limit="],
                 ["upper var\N{SUBSCRIPT ONE} limit=", "upper var\N{SUBSCRIPT TWO} limit="],
                 ["var\N{SUBSCRIPT ONE} = ", "var\N{SUBSCRIPT TWO} = "], "surface_parametric_3D")
        self.tab('Spherical Plot 3D', ["r(var\N{SUBSCRIPT ONE},var\N{SUBSCRIPT TWO} ) ="],
                 ["lower var\N{SUBSCRIPT ONE} limit=", "lower var\N{SUBSCRIPT TWO}  limit="],
                 ["upper var\N{SUBSCRIPT ONE} limit=", "upper var\N{SUBSCRIPT TWO}  limit="],
                 ["var\N{SUBSCRIPT ONE} = ", "var\N{SUBSCRIPT TWO} = "], "spherical_3D")

        self.__tabControl.grid(row=0, column=0, sticky="nsew")

    def tab(self, label, function_labels, lower_lim_labels, upper_lim_labels, variable_labels, plot_type):
        tab = ttk.Frame(self.__tabControl)
        self.__tabs += [tab]
        self.__tabControl.add(tab, text=label)
        plot_type = plot_type
        function_str = []
        variable_str = []
        lower_str = []
        upper_str = []
        function_names = []
        variables = []
        lower_lim = []
        upper_lim = []
        function_entries = []
        lower_lim_entries = []
        upper_lim_entries = []
        variable_entries = []
        row = 1

        for function_label in function_labels:
            function_names += [StringVar()]
            function_entries += [ttk.Entry(tab, textvariable=function_names[-1])]
            function_str += [ttk.Label(tab, text=function_label)]
            function_str[-1].grid(row=row, column=1)
            function_entries[-1].grid(row=row, column=2)
            row += 1

        for i in range(len(lower_lim_labels)):
            variable_str += [ttk.Label(tab, text=variable_labels[i])]
            variables += [StringVar()]
            variable_entries += [ttk.Entry(tab, textvariable=variables[-1])]
            variable_str[-1].grid(row=row, column=1)
            variable_entries[-1].grid(row=row, column=2)
            row += 1
            lower_lim += [StringVar()]
            upper_lim += [StringVar()]
            lower_lim_entries += [ttk.Entry(tab, textvariable=lower_lim[-1])]
            upper_lim_entries += [ttk.Entry(tab, textvariable=upper_lim[-1])]
            lower_str += [ttk.Label(tab, text=lower_lim_labels[i])]
            upper_str += [ttk.Label(tab, text=upper_lim_labels[i])]
            lower_str[-1].grid(row=row, column=1)
            lower_lim_entries[-1].grid(row=row, column=2)
            row += 1
            upper_str[-1].grid(row=row, column=1)
            upper_lim_entries[-1].grid(row=row, column=2)
            row += 1

        def submit():

            name = [fun_name.get() for fun_name in function_entries]
            up = [fun_name.get() for fun_name in upper_lim_entries]
            low = [fun_name.get() for fun_name in lower_lim_entries]
            var = [fun_name.get() for fun_name in variable_entries]
            try:
                a1 = eval(low[0])
            except:
                a1 = None
            try:
                a2 = eval(up[0])
            except:
                a2 = None
            try:
                b1 = eval(low[1])
            except:
                b1 = None
            try:
                b2 = eval(up[1])
            except:
                b2 = None

            try:
                if a1 is not None and a2 is not None:
                    pt = Draw(name, variables=var, plot_type=plot_type, a1=a1, a2=a2, b1=b1, b2=b2)
                elif a1 is not None and a2 is None:
                    pt = Draw(name, variables=var, plot_type=plot_type, a1=a1, b1=b1, b2=b2)
                elif a2 is not None and a1 is None:
                    pt = Draw(name, variables=var, plot_type=plot_type, a2=a2, b1=b1, b2=b2)
                else:
                    pt = Draw(name, variables=var, plot_type=plot_type, b1=b1, b2=b2)
            except:
                pt = Draw(name, variables=var, plot_type=plot_type, b1=b1, b2=b2)

            self.plot_style = Share.plot_style
            if self.plot_style['bg_plot_color'] != "":
                self.bg_color = self.plot_style['bg_plot_color']
            if self.plot_style['ax_plot_color'] != "":
                self.ax_color = self.plot_style['ax_plot_color']
            if self.plot_style['line_plot_color'] != "":
                self.line_color = self.plot_style['line_plot_color']
            self.line_thickness = self.plot_style['line_thickness']

            fig = figure(figsize=(10, 6), dpi=100)
            fig.patch.set_facecolor(self.ax_color)
            if plot_type in ["simple_2D", "parametric_2D", "implicit_2D"]:
                sub_fig = fig.add_subplot(111)
            elif plot_type in ["polar_2D"]:
                sub_fig = fig.add_subplot(111, projection='polar')
            elif plot_type in ["simple_3D", "curve_parametric_3D", "surface_parametric_3D", "spherical_3D"]:
                sub_fig = fig.add_subplot(111, projection='3d')
            sub_fig.patch.set_facecolor(self.bg_color)

            if plot_type == "simple_2D" and len(name) == 1:
                sub_fig.plot(pt.argsu, pt.argsy, linewidth=self.line_thickness)
                sub_fig.lines[0].set_color(self.line_color)
            elif plot_type == "parametric_2D" and len(name) == 2:
                sub_fig.plot(pt.argsx, pt.argsy, linewidth=self.line_thickness)
                sub_fig.lines[0].set_color(self.line_color)
            elif plot_type == "polar_2D" and len(name) == 1:
                sub_fig.plot(pt.argsu, pt.argsy, linewidth=self.line_thickness)
                sub_fig.lines[0].set_color(self.line_color)
            elif plot_type == "implicit_2D" and len(name) == 1:
                sub_fig.contour(pt.argsx, pt.argsy, pt.argsz, [0], colors=self.line_color,
                                linewidths=self.line_thickness)
            elif plot_type == "simple_3D" and len(name) == 1:
                sub_fig.plot_surface(pt.argsx, pt.argsy, pt.argsz, rstride=1, cstride=1, cmap=get_cmap('jet'),
                                     linewidth=0, antialiased=False, alpha=0.5)
            elif plot_type == "curve_parametric_3D" and len(name) == 3:
                sub_fig.plot(pt.argsx, pt.argsy, pt.argsz, label='parametric curve', linewidth=self.line_thickness)
                sub_fig.lines[0].set_color(self.line_color)
            elif plot_type == "surface_parametric_3D" and len(name) == 3:
                sub_fig.plot_surface(pt.argsx, pt.argsy, pt.argsz, rstride=1, cstride=1, cmap=get_cmap('jet'),
                                     linewidth=0, antialiased=False, alpha=0.5)
            elif plot_type == "spherical_3D" and len(name) == 1:
                sub_fig.plot_surface(pt.argsx, pt.argsy, pt.argsz, rstride=1, cstride=1, cmap=get_cmap('jet'),
                                     linewidth=0, antialiased=False, alpha=0.5)
            self.picture = fig
            canvas = FigureCanvasTkAgg(fig, master=tab)
            canvas.draw()
            canvas.get_tk_widget().grid(row=row+1, column=6, columnspan=8, rowspan=12, sticky="nesw")

        plot_button = ttk.Button(tab, text="Plot", command=submit, width=16)
        plot_button.grid(row=row, column=2)


# the author: Dariusz Piekarz
