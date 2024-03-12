from numpy import sqrt, exp, cbrt, pi, sin, cos
import numpy as np
import math
from cmath import phase
e = exp(1)
phi = (sqrt(5)+1)/2
gamma = 0.57721566490153286060651209
g = 9.80665


def fact(n):
    if not isinstance(n, int):
        raise ValueError("It is possible to compute a factorial only for natural numbers.")
    if n in [0, 1]:
        return 1
    else:
        return n*fact(n-1)


def Gamma(x):
    if isinstance(x, int):
        return int(math.gamma(x+1))
    else:
        return math.gamma(x+1)


def Sqrt(x):
    if isinstance(x, (complex, np.complex128)):
        return str([sqrt(abs(x))*(cos((phase(x)+2*k*pi)/2)+1j*sin((phase(x)+2*k*pi)/2)) for k in range(2)])
    if isinstance(x, (float, np.float32, np.float64, int, np.int32, np.int64)):
        if x < 0:
            return str([sqrt(abs(x))*(cos((pi+2*k*pi)/2)+1j*sin((pi+2*k*pi)/2)) for k in range(2)])
        else:
            return sqrt(x)


def Cbrt(x):
    if isinstance(x, (complex, np.complex128)):
        return str([cbrt(abs(x))*(cos((phase(x)+2*k*pi)/3)+1j*sin((phase(x)+2*k*pi)/3)) for k in range(3)])
    if isinstance(x, (float, np.float32, np.float64, int, np.int32, np.int64)):
        if x < 0:
            return str([cbrt(abs(x))*(cos((pi+2*k*pi)/3)+1j*sin((pi+2*k*pi)/3)) for k in range(3)])
        else:
            return cbrt(x)


def Nrt(n, x):
    if isinstance(x, (complex, np.complex128)):
        return str([abs(x)**(1/n)*(cos((phase(x)+2*k*pi)/n)+1j*sin((phase(x)+2*k*pi)/n)) for k in range(n)])
    if isinstance(x, (float, np.float32, np.float64, int, np.int32, np.int64)):
        if x < 0:
            return str([abs(x)**(1/n)*(cos((pi+2*k*pi)/n)+1j*sin((pi+2*k*pi)/n)) for k in range(n)])
        else:
            return x**(1/n)

