import scipy.constants as c #constants for whatever
import math #basic math operations
import sympy as sp #for differential
import numpy as np #extra
import cmath #complex math

def angular_wave_func(m,l,theta,phi):
    if m>0:
        epsilon=(-1)**m
    elif m <= 0:
        epsilon = 1
    x = sp.Symbol('x')
    gen1 = (x**2-1)**l
    if l > 0:
        for i in range(l):
            d = sp.diff(gen1)
            gen1 = d
    LP = (1/(2**l*(math.factorial(l)))) * (gen1)     ##Legendre Polynomial(Pl(x))
    
##############################################################    
    gen2=LP
    if abs(m) > 0:
        for i in range(abs(m)):
            d = sp.diff(gen2)
            gen2=d

    ALP = (1-x**2)**(abs(m)/2) * gen2 ##Associated Legendre function(Pml(x))
    
    f = sp.lambdify(x,ALP) ##make ALP a function of x --> ALP(x)
    ALP = f(math.cos(theta))  #sub cos(theta) as x into ALP --> ALP(cos(theta))

##########################################################


    NAS = epsilon * (((2*l+1)/(4*math.pi))*((math.factorial(l-abs(m)))/(math.factorial(l+abs(m)))))**0.5 *cmath.exp((1j*m*phi)) #####Normalized Angular Solution(Yml(theta,phi))
    
    

    combine = NAS * ALP
    
    return combine


angular_wave_func (0,1,c.pi,0)
angular_wave_func (1,1,c.pi/2,c.pi) 
angular_wave_func (0,2,c.pi,0) 








##############################################################################################################3

import scipy.constants as c #constants for whatever
import math #basic math operations
import sympy as sp #for differential
import numpy as np #extra
import cmath #complex math

a=c.physical_constants['Bohr radius'][0]
def radial_wave_func(n,l,r):
    
    
    p = 2*l+1 #define p
    q = n+l #define q
    c = r/(n*a)
    
    x=sp.Symbol('x')
    eqn1 = (sp.exp(-x))*x**(q)
    if q>0:
        for i in range(q):
            d=sp.diff(eqn1)
            eqn1=d
    LQ = (sp.exp(x))*eqn1 #Laguerre Polynomial(LQ(X))
    print(LQ)
    
    #################################
    
    eqn2=LQ
    if p>0:
        for i in range(p):
            d=sp.diff(eqn2)
            eqn2=d
    ALQ = (-1)**p * eqn2 
    
    
    f = sp.lambdify(x,ALQ)
    ALQ = f(2*c)  #Associated Lagueere function(ALQ(X)))
    print(ALQ)
    ###############################################
    
    NRS = ((((2/(n*a))**3) * ((math.factorial(n-l-1))/(2*n*(math.factorial(n+l))**3)))**0.5) * (math.exp(-c))*((2*c)**l)
    print(NRS)
    final = NRS * ALQ
    
    return final

radial_wave_func(1,0,a)
radial_wave_func (1,0,a)
radial_wave_func(2,1,a)
radial_wave_func(2,1,2*a)
radial_wave_func(3,1,2*a)