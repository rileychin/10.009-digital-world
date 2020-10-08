import numpy as np
import scipy.constants as c
from sympy import diff, lambdify, Symbol, exp, sqrt
from time import sleep

def spherical_to_cartesian(r,theta,phi):
    x = round(r * np.sin(theta) * np.cos(phi),1)
    y = round(r * np.sin(theta) * np.sin(phi),1)
    z = round(r * np.cos(theta),1)
    return x , y , z

def cartesian_to_spherical(x, y, z):
    r = np.sqrt(x**2 + y**2 + z**2)
    theta = np.arccos(z/r)
    if y == 0:
        phi = 0.0
    else:
        phi =  np.arcsin(y / (r * np.sin(theta)))
    return round(r,5), round(theta,5), round(phi,5)

def function(m,l):
    x = Symbol('x')
    equation = (x**2 -1)**l
    equation = equation.diff(x,l)
    polynomial = equation * (1 / (2**l * np.math.factorial(l)))
    polynomial = polynomial.diff(x,abs(m))
    function = ((1 - x**2)**(abs(m) / 2) * polynomial)
    return function

def angular_wave_func(m,l,theta,phi):
    x = Symbol('x')
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

def laguerre_polynomial(q):
    x = Symbol('x')
    diff_equation = exp(-x) * x**q
    equation = exp(x) * diff_equation.diff(x,q)
    return equation

def laguerre_function(p,q):
    x = Symbol('x')
    diff_equation = laguerre_polynomial(q)
    equation = -1**p * diff_equation.diff(x,p)
    return equation

def radial_wave_func(n,l,r):
    x = Symbol('x')
    a=c.physical_constants['Bohr radius'][0]
    q = n + l
    p = 2*l + 1
    constant = r / (n * a)
    part3 = lambdify(x, laguerre_function(p,q))
    part3_subbed = part3(2*constant)
    part2 = exp(-constant) * (2 * constant)**l
    part1 = sqrt(((2 / (n*a))**3) * np.math.factorial(n - l - 1) / (2 * n * (np.math.factorial(n + l)**3)))
    solution = part1 * part2 * part3_subbed / (a**(-3 / 2))
    rounded_solution = solution
    return solution

def mgrid3d(xstart, xend, xpoints, 
            ystart, yend, ypoints, 
            zstart, zend, zpoints):
    xr = []
    yr = []
    zr = []
    xval = xstart
    xcount = 0
    xstartcheck = 0
    ystartcheck = 0
    zstartcheck = 0
    if xstart > 0:
        xstartcheck = xstart
    elif ystart > 0:
        ystartcheck = ystart
    elif zstart > 0:
        zstartcheck = zstart

    # calculate the step size for each axis
    xstep = ((abs(xstart) + abs(xend)) / (xpoints -1)) - xstartcheck
    ystep = ((abs(ystart) + abs(yend)) / (ypoints -1)) - ystartcheck
    zstep = ((abs(zstart) + abs(zend)) / (zpoints -1)) - zstartcheck
    
    while xcount < xpoints:
        # initialize y points
        # create temporary variable to store x, y and z list
        yval = ystart
        ycount = 0
        xrow = []
        yrow = []
        zrow = []
    
        while ycount < ypoints:
            # initialize z points
            # create temporary variable to store the inner x, y, and z list
            zval = zstart
            zcount = 0
            xrow2 = []
            yrow2 = []
            zrow2 = []
        
            while zcount < zpoints:
                # add the points x, y, and z to the inner most list
                xrow2.append(xval)
                yrow2.append(yval)
                zrow2.append(zval)
            
                # increase z point
                zval += zstep
                zcount += 1
            # add the inner most lists to the second lists
            xrow.append(xrow2)
            yrow.append(yrow2)
            zrow.append(zrow2)
        
            # increase y point
            yval += ystep
            ycount += 1
        # add the second lists to the returned lists
        xr.append(xrow)
        yr.append(yrow)
        zr.append(zrow)
    
        # increase x point
        xval += xstep
        xcount += 1
    tuples1 = xr, yr, zr
    return tuples1

def density_calc(a,r):
    value = np.absolute(np.asarray((a*r)**2).astype(np.float64))
    return np.round(value,5)

def hydrogen_wave_func(n,l, m, roa, Nx, Ny, Nz):
    a=c.physical_constants['Bohr radius'][0]
    lst_of_points = mgrid3d(-roa, roa, Nx, -roa, roa, Ny, -roa, roa, Nz)
    vectorise_array = np.vectorize(np.array)
    xx, yy, zz = vectorise_array(lst_of_points)
    vectorise_C_to_S = np.vectorize(cartesian_to_spherical)
    vectorise_angular = np.vectorize(angular_wave_func)
    vectorise_radial = np.vectorize(radial_wave_func)
    r,theta,phi = vectorise_C_to_S(xx,yy,zz)
    r = r * a
    angular_value = vectorise_angular(m,l,theta,phi)
    if m < 0:
        angular_value = (1j/np.sqrt(2))*(angular_value - ((-1)**m * vectorise_angular(-m,l,theta,phi)))
    elif m > 0:
        angular_value = (1/np.sqrt(2))*(vectorise_angular(-m,l,theta,phi) + ((-1)**m * angular_value))
    radial_value = vectorise_radial(n,l,r)
    vectorise_density = np.vectorize(density_calc)
    density = vectorise_density(angular_value, radial_value)
    return xx, yy, zz, density

print('Test 1')
x,y,z,mag = hydrogen_wave_func(2 ,1 ,1 ,8 ,2 ,2 ,2)
print('x, y, z:')
print(x, y, z)
print('mag:')
print(mag)
print('\n')
print('Test 2')
x,y,z,mag = hydrogen_wave_func(2 ,1 ,1 ,5 ,3 ,4 ,2)
print('x, y, z:')
print(x, y, z)
print('mag:')
print(mag)
print('\n')
print('Test 3')
x,y,z,mag = hydrogen_wave_func(2 ,0 ,0 ,3 ,5 ,4 ,3)
print('x, y, z:')
print(x, y, z)
print('mag:')
print(mag)


