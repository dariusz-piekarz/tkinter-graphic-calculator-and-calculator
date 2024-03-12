from error import Error
import matplotlib.pyplot as plt
from string_var import Variable
import numpy as np


class Draw:

    def __init__(self, names, variables, plot_type="simple_2D", prec=100, a1=-1, a2=1, b1=None, b2=None):
        self.plot_type = plot_type
        if plot_type not in ["simple_2D", "parametric_2D", "polar_2D", "implicit_2D", "simple_3D",
                             "curve_parametric_3D", "surface_parametric_3D", "spherical_3D"]:
            raise Error("Wrong type of error was provided")
        self.names = names
        self.variables = variables
        self.argsu = np.linspace(a1, a2, prec)
        if plot_type in ["implicit_2D", "simple_3D", "surface_parametric_3D", "spherical_3D"]:
            if b1 is None:
                b1 = -1
            if b2 is None:
                b2 = 1
            self.argsv = np.linspace(b1, b2, prec)
        self.argsx = list()
        self.argsy = list()
        self.argsz = list()
        self.set_arguments()

    def set_arguments(self):

        if self.plot_type == "simple_2D" and len(self.names) == 1 and len(self.variables) == 1:

            var = Variable(self.names[0], self.variables[0])
            self.argsy = [var.quick_eval(y) for y in self.argsu]
            Variable.replace_nan_values(self.argsy)

        elif self.plot_type == "parametric_2D" and len(self.names) == 2 and len(self.variables) == 1:
            var1 = Variable(self.names[0], self.variables[0])
            var2 = Variable(self.names[1], self.variables[0])
            self.argsx = [var1.quick_eval(y) for y in self.argsu]
            self.argsy = [var2.quick_eval(y) for y in self.argsu]
            Variable.replace_nan_values(self.argsx)
            Variable.replace_nan_values(self.argsy)

        elif self.plot_type == "polar_2D" and len(self.names) == 1 and len(self.variables) == 1:

            var = Variable(self.names[0], self.variables[0])
            for y in self.argsu:
                if var.quick_eval(y) < 0:
                    self.argsy.append(var.quick_eval(np.pi - y))
                else:
                    self.argsy.append(var.quick_eval(y))
            Variable.replace_nan_values(self.argsy)

        elif self.plot_type == "implicit_2D" and len(self.names) == 1 and len(self.variables) == 2:
            var = Variable(self.names[0], self.variables[0], self.variables[1])
            for x in self.argsu:
                temp = [var.quick_eval(x, y) for y in self.argsv]
                Variable.replace_nan_values(temp)
                self.argsz.append(temp)
                self.argsx.append([x for y in self.argsv])
                self.argsy.append([y for y in self.argsv])
            self.argsz = np.array(self.argsz)
            self.argsx = np.array(self.argsx)
            self.argsy = np.array(self.argsy)

        elif self.plot_type == "simple_3D" and len(self.names) == 1 and len(self.variables) == 2:

            var = Variable(self.names[0], self.variables[0], self.variables[1])
            for x in self.argsu:
                temp = [var.quick_eval(x, y) for y in self.argsv]
                Variable.replace_nan_values(temp)
                self.argsz.append(temp)
                self.argsx.append([x for y in self.argsv])
                self.argsy.append([y for y in self.argsv])
            self.argsz = np.array(self.argsz)
            self.argsx = np.array(self.argsx)
            self.argsy = np.array(self.argsy)

        elif self.plot_type == "curve_parametric_3D" and len(self.names) == 3 and len(self.variables) == 1:
            varx = Variable(self.names[0], self.variables[0])
            vary = Variable(self.names[1], self.variables[0])
            varz = Variable(self.names[2], self.variables[0])
            self.argsx = list(map(lambda x: varx.quick_eval(x), self.argsu))
            self.argsy = list(map(lambda x: vary.quick_eval(x), self.argsu))
            self.argsz = list(map(lambda x: varz.quick_eval(x), self.argsu))
            self.argsz = np.array(self.argsz)
            self.argsx = np.array(self.argsx)
            self.argsy = np.array(self.argsy)

        elif self.plot_type == "surface_parametric_3D" and len(self.names) == 3 and len(self.variables) == 2:

            varx = Variable(self.names[0], self.variables[0], self.variables[1])
            vary = Variable(self.names[1], self.variables[0], self.variables[1])
            varz = Variable(self.names[2], self.variables[0], self.variables[1])
            for x in self.argsu:
                tempx = [varx.quick_eval(x, y) for y in self.argsv]
                tempy = [vary.quick_eval(x, y) for y in self.argsv]
                tempz = [varz.quick_eval(x, y) for y in self.argsv]
                Variable.replace_nan_values(tempx)
                Variable.replace_nan_values(tempy)
                Variable.replace_nan_values(tempz)
                self.argsx.append(tempx)
                self.argsy.append(tempy)
                self.argsz.append(tempz)
            self.argsz = np.array(self.argsz)
            self.argsx = np.array(self.argsx)
            self.argsy = np.array(self.argsy)

        elif self.plot_type == "spherical_3D" and len(self.names) == 1 and len(self.variables) == 2:

            names = list()
            names.append("(" + self.names[0] + ")*cos(" + self.variables[0] + ")*cos(" + self.variables[1] + ")")
            names.append("(" + self.names[0] + ")*cos(" + self.variables[0] + ")*sin(" + self.variables[1] + ")")
            names.append("(" + self.names[0] + ")*sin(" + self.variables[0] + ")")
            varx = Variable(names[0], self.variables[0], self.variables[1])
            vary = Variable(names[1], self.variables[0], self.variables[1])
            varz = Variable(names[2], self.variables[0], self.variables[1])
            for x in self.argsu:
                self.argsz.append([varx.quick_eval(x, y) for y in self.argsv])
                self.argsx.append([vary.quick_eval(x, y) for y in self.argsv])
                self.argsy.append([varz.quick_eval(x, y) for y in self.argsv])
            self.argsz = np.array(self.argsz)
            self.argsx = np.array(self.argsx)
            self.argsy = np.array(self.argsy)

    def plot(self, sizex=8, sizey=4):
        fig = plt.figure(figsize=(sizex, sizey), dpi=100)

        if self.plot_type in ["simple_2D", "parametric_2D", "implicit_2D"]:
            ax = fig.add_subplot(111)
        elif self.plot_type in ["polar_2D"]:
            ax = fig.add_subplot(111, projection='polar')
        elif self.plot_type in ["simple_3D", "curve_parametric_3D", "surface_parametric_3D", "spherical_3D"]:
            ax = fig.add_subplot(111, projection='3d')

        if self.plot_type == "simple_2D" and len(self.names) == 1:
            ax.plot(self.argsu, self.argsy)
        elif self.plot_type == "parametric_2D" and len(self.names) == 2:
            ax.plot(self.argsx, self.argsy)
        elif self.plot_type == "polar_2D" and len(self.names) == 1:
            ax.plot(self.argsu, self.argsy)
        elif self.plot_type == "implicit_2D" and len(self.names) == 1:
            ax.contour(self.argsx, self.argsy, self.argsz, [0])
        elif self.plot_type == "simple_3D" and len(self.names) == 1:
            ax.plot_surface(self.argsx, self.argsy, self.argsz, rstride=1, cstride=1, cmap=plt.get_cmap('jet'),
                            linewidth=0, antialiased=False, alpha=0.5)
        elif self.plot_type == "curve_parametric_3D" and len(self.names) == 3:
            ax.plot(self.argsx, self.argsy, self.argsz, label='parametric curve')
        elif self.plot_type == "surface_parametric_3D" and len(self.names) == 3:
            ax.plot_surface(self.argsx, self.argsy, self.argsz, rstride=1, cstride=1, cmap=plt.get_cmap('jet'),
                            linewidth=0, antialiased=False, alpha=0.5)
        elif self.plot_type == "spherical_3D" and len(self.names) == 1:
            ax.plot_surface(self.argsx, self.argsy, self.argsz, rstride=1, cstride=1, cmap=plt.get_cmap('jet'),
                            linewidth=0, antialiased=False, alpha=0.5)
