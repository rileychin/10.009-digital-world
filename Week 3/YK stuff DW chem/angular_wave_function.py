import scipy.constants as c
import numpy as np
from sympy import diff, lambdify, Symbol

x = Symbol('x')

def function(m,l):
    equation = (x**2 -1)**l
    equation = equation.diff(x,l)
    polynomial = equation * (1 / (2**l * np.math.factorial(l)))
    polynomial = polynomial.diff(x,m)
    function = ((1 - x**2)**(abs(m) / 2) * polynomial)
    return function

def angular_wave_func(m,l,theta,phi):
    e = 1
    if m > 0:
        e = (-1**m)
    function2 = lambdify(x, function(m,l))
    f = function2(np.cos(theta))
    y = np.exp(1j *m * phi)
    equation = np.sqrt((2 * l + 1) / (4 * c.pi) * (np.math.factorial(l - abs(m)) / np.math.factorial(l + abs(m))))
    full_equation = equation * y * f * e
    full_equation = round(full_equation.real, 5) + complex(round(full_equation.imag, 2))
    return full_equation

angular_wave_func(0,0,0,0) #0.28209
angular_wave_func(0,1,c.pi,0) #-0.4886
angular_wave_func(1,1,c.pi/2,c.pi) #0.34549 -0 j
angular_wave_func(0,2,c.pi,0) #0.63078
