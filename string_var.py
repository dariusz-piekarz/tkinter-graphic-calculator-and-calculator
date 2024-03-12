from numpy import nan, isnan, where
from error import Error
from re import sub
from math import *


class Variable:
    def __init__(self, name, *args):
        """
            name: is an expression we want to potentially evaluate
            args: we specify which elements in the 'name' expression are variables to evaluate

            the purpose of this class is an evaluation of an expression provided by a user with a common rules
        """
        self.name = name
        self.arg_list = []
        self.load_args(*args)
        self.mod = str()

    def load_args(self, *args):
        """ the method 'load_args' aggregate all arguments to a one list"""

        for arg in args:
            self.arg_list.append(arg)

    def quick_eval(self, *args):
        """
            this function is a combination of functions written above:
            provided that the 'args' values correspond to an order provided in arg_list we firstly replace symbols
             commonly known by symbols specific for the python language, then in assuming the order of numerical
             values is the same as order of variables
            we replace names of variables by its values, the final value is returned.

        """
        mod = self.name.replace("^", "**")
        if len(self.arg_list) == len(args):
            for i in range(len(self.arg_list)):
                mod = mod.replace(self.arg_list[i] + "**", "(" + str(args[i]) + ")**")
                mod = mod.replace("**" + self.arg_list[i], "**" + str(args[i]))
                mod = mod.replace("(" + self.arg_list[i], "(" + str(args[i]))
                mod = mod.replace("+" + self.arg_list[i], "+" + str(args[i]))
                mod = mod.replace(self.arg_list[i] + "+", str(args[i]) + "+")
                mod = mod.replace(self.arg_list[i] + "-", str(args[i]) + "-")
                mod = mod.replace("-" + self.arg_list[i], "-" + str(args[i]))
                mod = mod.replace("*" + self.arg_list[i], "*" + str(args[i]))
                mod = mod.replace(self.arg_list[i] + "*", str(args[i]) + "*")
                mod = mod.replace(self.arg_list[i] + "/", str(args[i]) + "/")
                mod = mod.replace("/" + self.arg_list[i], "/" + str(args[i]))
                if len(self.name) == 1:
                    mod = mod.replace(self.arg_list[i], str(args[i]))
            try:
                return eval(mod)
            except:
                return nan

    @staticmethod
    def replace_nan_values(args):
        """
        the function interpolate the closest non NAN-value to a NAN list element. The list is provided as an argument
        :param args:  list of arguments with nan-values to remove
        :return: fixed list with non-nan values

        """
        if all([isnan(arg) for arg in args]):
            raise Error("All data are non-numerical")
        while any(([isnan(arg) for arg in args])):
            nan_indicies = where(isnan(args))[0]

            for ind in nan_indicies:

                if ind == 0:
                    args[ind] = args[ind + 1]
                elif ind == args[-1]:
                    args[ind] = args[ind - 1]
                else:
                    try:
                        args[ind] = args[ind + 1]
                    except:
                        args[ind] = args[ind - 1]


def calculator_symbols(expression):
    expr = sub(r"(\d+)!", r"fact(\1)", expression)
    expr = sub(r"\((.*?)\)!", r"fact(\1)", expr)
    expr = sub(r"%", r"*0.01", expr)
    expr = sub(r"I", r"1j", expr)
    return sub(r"\^", r"**", expr)
