import numpy as np
import scipy.constants as c #constants for whatever
import math #basic math operations
import sympy as sp #for differential
import cmath #complex math

def spherical_to_cartesian(r,theta,phi):
    x = r*(np.sin(theta))*(np.cos(phi))
    y = r*(np.sin(theta))*(np.sin(phi))
    z = r*(np.cos(theta))
    return round(x,5),round(y,5),round(z,5)
	
#########################################################
def cartesian_to_spherical(x, y, z):
    r = (x**2+y**2+z**2)**0.5
    if r == 0:
        theta = np.arccos(0)
    else:    
        theta = np.arccos(z/r)
    if r != 0:
        phi = np.arccos(x/(r*(np.sin(theta))))
    else:
        phi = np.arctan(0)

    return round(r,5),round(theta,5),round(phi,5)
############################################################



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
    
   
    gen2=LP
    if abs(m) > 0:
        for i in range(abs(m)):
            d = sp.diff(gen2)
            gen2=d

    ALP = (1-x**2)**(abs(m)/2) * gen2 ##Associated Legendre function(Pml(x))
    
    f = sp.lambdify(x,ALP) ##make ALP a function of x --> ALP(x)
    ALP = f(math.cos(theta))  #sub cos(theta) as x into ALP --> ALP(cos(theta))


    NAS = epsilon * (((2*l+1)/(4*math.pi))*((math.factorial(l-abs(m)))/(math.factorial(l+abs(m)))))**0.5 *cmath.exp((1j*m*phi)) #####Normalized Angular Solution(Yml(theta,phi))
    
    

    combine = NAS * ALP
    
    return combine
##################################################################
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

    

    
    eqn2=LQ
    if p>0:
        for i in range(p):
            d=sp.diff(eqn2)
            eqn2=d
    ALQ = (-1)**p * eqn2 
    
    
    f = sp.lambdify(x,ALQ)
    ALQ = f(2*c)  #Associated Lagueere function(ALQ(X)))


    NRS = ((((2/(n*a))**3) * ((math.factorial(n-l-1))/(2*n*(math.factorial(n+l))**3)))**0.5) * (math.exp(-c))*((2*c)**l)

    final = (NRS * ALQ)/ (a**(-3/2))
    
    return final
#####################################################################
def mgrid3d(xstart, xend, xpoints, 
            ystart, yend, ypoints, 
            zstart, zend, zpoints):
    xr = []
    yr = []
    zr = []
    xval = xstart
    xcount = 0

    # calculate the step size for each axis
    xstep = (xend-xstart)/(xpoints-1)
    ystep = (yend-ystart)/(ypoints-1)
    zstep = (zend-zstart)/(zpoints-1)
    
    while xcount < xpoints:
        # initialize y points
        # create temporary variable to store x, y and z list
        yval = ystart
        ycount=0
        xrow =[]
        yrow=[]
        zrow=[]
        
    
        while ycount < ypoints:
            # initialize z points
            # create temporary variable to store the inner x, y, and z list
            zval=zstart
            zcount=0
            xxrow=[]
            yyrow=[]
            zzrow=[]
        
            while zcount < zpoints:
                # add the points x, y, and z to the inner most list
                xxrow.append(xval)
                yyrow.append(yval)
                zzrow.append(zval)
            
                # increase z point
                zval += zstep
                zcount+=1
            # add the inner most lists to the second lists
            xrow.append(xxrow)
            yrow.append(yyrow)
            zrow.append(zzrow)
        
            # increase y point
            yval+= ystep
            ycount+=1
        # add the second lists to the returned lists
        xr.append(xrow)
        yr.append(yrow)
        zr.append(zrow)
    
        # increase x point
        xval+=xstep
        xcount+=1
        
    return [xr, yr, zr]


###########################################################
def magni(im):
    v = np.vectorize(round)
    real = im.real
    imag = im.imag
    magnitude = (real**2 + imag**2)**0.5 #calculates magnitude of radial and imaginary component)
    
    return v(magnitude,5)

##################################################
def hydrogen_wave_func(n,l, m, roa, Nx, Ny, Nz):
    a=c.physical_constants['Bohr radius'][0]
    v = np.vectorize(round)
    lists = np.array (mgrid3d(-roa,roa,Nx,-roa,roa,Ny,-roa,roa,Nz))
    #print(lists)               
    
    x = v(lists[0],5) #returns x list from lists
    y = v(lists[1],5) #returns y list from lists
    z = v(lists[2],5) #returns z list from lists

    vs = np.vectorize(cartesian_to_spherical) #vectorize coordinates
    r,t,p = vs(x,y,z) # returns radius, theta, phi in vector form
    #print(r,'radius',t,'theta',p,'phi')
    
    vr = np.vectorize(radial_wave_func) #vectorize radial wave functions
    r_normal = r * a #denormalizes radius 
    r_func = vr(n,l,r_normal) #returns RADIAL solution in vector form
    #print(r_func,'radial')
    
    va = np.vectorize(angular_wave_func) #vectorize angular wave functions
    a_func = va(m,l,t,p) #returns ANGULAR solution in vector form
   # print(a_func,'angular')
    
    if m<0:
        angular = 1j/(2**(0.5)) * (a_func - ((-1**m) * va(abs(m),l,t,p)))
    elif m>0:
        angular = 1/(2**(0.5)) * (va(-abs(m),l,t,p) + ((-1**m) * a_func))
    else:
        angular = va(0,l,t,p)
        
    #print(angular,'1st')
    #print(angular[0],angular[1],'hello')
    angular = magni(angular)

    #print(angular)
    
    final_mag = v(((angular*r_func)**2),5)
    
  
    return (x,y,z,final_mag)
    


###Test:
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