from share import Share
from matplotlib.pyplot import figure, get_cmap
from tkinter import ttk
from tkinter import StringVar, Frame
from grapher import Draw
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Frame1(Frame, Share):
    __tabs = []
    bg_color = 'white'
    ax_color = 'white'
    line_color = 'blue'
    line_thickness = 1
    own_style = dict({'bg_plot_color': "", 'ax_plot_color': "", 'line_plot_color': "", 'line_thickness': 1})

    def __init__(self, *arg, **kwargs):
        super(Frame1, self).__init__(*arg, **kwargs)
        print(Share.total_height, Share.total_width)
        self.__tabControl = ttk.Notebook(self, height=Share.total_height, width=Share.total_width)
        self.pack(fill='both', expand=True)
        self.create_tabs()
        self.__tabControl.grid(row=0, column=0, sticky="nsew")

    def create_tabs(self):
        tabs_info =\
            [
            {
                'label': 'Simple Plot 2D',
                'function_labels': ["f(var) = "],
                'lower_lim_labels': ["lower limit="],
                'upper_lim_labels': ["upper limit="],
                'variable_labels': ["var = "],
                'plot_type': "simple_2D"
            },
            {
                'label': 'Parametric Plot 2D',
                'function_labels': ['x(var) = ', 'y(var) = '],
                'lower_lim_labels': ["lower limit="],
                'upper_lim_labels': ["upper limit="],
                'variable_labels': ["var = "],
                'plot_type': "parametric_2D"
            },
            {
                'label': 'Polar Plot 2D',
                'function_labels': ["r(var)  ="],
                'lower_lim_labels': ["lower limit="],
                'upper_lim_labels': ["upper limit="],
                'variable_labels': ["var = "],
                'plot_type': "polar_2D"
            },
            {
                'label': 'Implicit Plot 2D',
                'function_labels': ["0  ="],
                'lower_lim_labels': ["lower var\N{SUBSCRIPT ONE} limit=", "lower var\N{SUBSCRIPT TWO}  limit="],
                'upper_lim_labels': ["upper var\N{SUBSCRIPT ONE} limit=", "upper var\N{SUBSCRIPT TWO} limit="],
                'variable_labels': ["var\N{SUBSCRIPT ONE} = ", "var\N{SUBSCRIPT TWO} = "],
                'plot_type': "implicit_2D"
            },
            {
                'label': 'Surface Plot 3D',
                'function_labels': ["f(var\N{SUBSCRIPT ONE},var\N{SUBSCRIPT TWO})   ="],
                'lower_lim_labels': ["lower var\N{SUBSCRIPT ONE} limit=", "lower var\N{SUBSCRIPT TWO}  limit="],
                'upper_lim_labels': ["upper var\N{SUBSCRIPT ONE} limit=", "upper var\N{SUBSCRIPT TWO} limit="],
                'variable_labels': ["var\N{SUBSCRIPT ONE} = ", "var\N{SUBSCRIPT TWO} = "],
                'plot_type': "simple_3D"
            },
            {
                'label': 'Curve Parametric Plot 3D',
                'function_labels': ["x(var) =", "y(var) =", "z(var) ="],
                'lower_lim_labels': ["lower limit="],
                'upper_lim_labels': ["upper limit="],
                'variable_labels': ["var = "],
                'plot_type': "curve_parametric_3D"
            },
            {
                'label': 'Surface Parametric Plot 3D',
                'function_labels': ["x(var\N{SUBSCRIPT ONE},var\N{SUBSCRIPT TWO} ) =",
                                    "y(var\N{SUBSCRIPT ONE},var\N{SUBSCRIPT TWO} ) =",
                                    "z(var\N{SUBSCRIPT ONE},var\N{SUBSCRIPT TWO} ) ="],
                'lower_lim_labels': ["lower var\N{SUBSCRIPT ONE} limit=", "lower var\N{SUBSCRIPT TWO}  limit="],
                'upper_lim_labels': ["upper var\N{SUBSCRIPT ONE} limit=", "upper var\N{SUBSCRIPT TWO} limit="],
                'variable_labels': ["var\N{SUBSCRIPT ONE} = ", "var\N{SUBSCRIPT TWO} = "],
                'plot_type': "surface_parametric_3D"
            },
            {
                'label': 'Spherical Plot 3D',
                'function_labels': ["r(var\N{SUBSCRIPT ONE},var\N{SUBSCRIPT TWO} ) ="],
                'lower_lim_labels': ["lower var\N{SUBSCRIPT ONE} limit=", "lower var\N{SUBSCRIPT TWO}  limit="],
                'upper_lim_labels': ["upper var\N{SUBSCRIPT ONE} limit=", "upper var\N{SUBSCRIPT TWO} limit="],
                'variable_labels': ["var\N{SUBSCRIPT ONE} = ", "var\N{SUBSCRIPT TWO} = "],
                'plot_type': "spherical_3D"
            }
            ]
        for tab_info in tabs_info:
            self.create_tab(**tab_info)

    def create_tab(self, label, function_labels, lower_lim_labels, upper_lim_labels, variable_labels, plot_type):
        tab = ttk.Frame(self.__tabControl)
        self.__tabs.append(tab)
        self.__tabControl.add(tab, text=label)
        plot_type = plot_type
        row = 1

        function_names = [StringVar() for i in range(len(function_labels))]
        function_entries = [ttk.Entry(tab, textvariable=function_name) for function_name in function_names]
        function_str = [ttk.Label(tab, text=function_label) for function_label in function_labels]
        variable_str = [ttk.Label(tab, text=variable_label) for variable_label in variable_labels]
        variables = [StringVar() for i in range(len(variable_labels))]
        variable_entries = [ttk.Entry(tab, textvariable=variable) for variable in variables]
        lower_lims = [StringVar() for _ in lower_lim_labels]
        upper_lims = [StringVar() for _ in upper_lim_labels]
        lower_lim_entries = [ttk.Entry(tab, textvariable=lower_lim) for lower_lim in lower_lims]
        upper_lim_entries = [ttk.Entry(tab, textvariable=upper_lim) for upper_lim in upper_lims]
        lower_str = [ttk.Label(tab, text=lower_lim_label) for lower_lim_label in lower_lim_labels]
        upper_str = [ttk.Label(tab, text=upper_lim_label) for upper_lim_label in upper_lim_labels]

        for i in range(len(function_labels)):
            function_str[i].grid(row=row, column=1)
            function_entries[i].grid(row=row, column=2)
            row += 1

        for i in range(len(lower_lim_labels)):
            variable_str[i].grid(row=row, column=1)
            variable_entries[i].grid(row=row, column=2)
            row += 1
            lower_str[i].grid(row=row, column=1)
            lower_lim_entries[i].grid(row=row, column=2)
            row += 1
            upper_str[i].grid(row=row, column=1)
            upper_lim_entries[i].grid(row=row, column=2)
            row += 1

        plot_button = ttk.Button(tab, text="Plot",
                                 command=lambda: self.submit(tab, function_entries, variable_entries, lower_lim_entries,
                                                             upper_lim_entries, plot_type, row), width=16)
        plot_button.grid(row=row, column=2)

    def submit(self, tab, function_entries, variable_entries, lower_lim_entries, upper_lim_entries, plot_type, row):
        pt = None
        fig = None
        self.canvas = None
        self.picture = None
        sub_fig = None

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
            sub_fig.contour(pt.argsx, pt.argsy, pt.argsz, [0], colors=self.line_color, linewidths=self.line_thickness)
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
        self.canvas = FigureCanvasTkAgg(fig, master=tab)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=row + 1, column=6, columnspan=8, rowspan=12, sticky="nesw")
