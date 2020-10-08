import scipy.constants as c
import numpy as np
from sympy import diff, lambdify, Symbol, exp

a=c.physical_constants['Bohr radius'][0]
x = Symbol('x')

def laguerre_polynomial(q):
    diff_equation = exp(-x) * x**q
    equation = exp(x) * diff_equation.diff(x,q)
    return equation

def laguerre_function(p,q):
    diff_equation = laguerre_polynomial(q)
    equation = -1**p * diff(diff_equation,x,p)
    return equation

def radial_wave_func(n,l,r):
    q = n + l
    p = 2*l + 1
    constant = r / (n * a)
    part3 = lambdify(x, laguerre_function(p,q))
    part3_subbed = part3(2*constant)
    part2 = exp(-constant) * (2 * constant)**l
    part1 = np.sqrt(((2 / (n*a))**3) * np.math.factorial(n - l - 1) / (2 * n * (np.math.factorial(n + l)**3)))
    solution = part1 * part2 * part3_subbed / (a**(-3 / 2))
    rounded_solution = round(solution,5)
    return print(rounded_solution)

radial_wave_func(1,0,a)
radial_wave_func(2,1,a)
radial_wave_func(2,1,2*a)
radial_wave_func(3,1,2*a)