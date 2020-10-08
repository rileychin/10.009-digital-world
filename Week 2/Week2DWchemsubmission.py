import scipy.constants as c
import math

def deg_to_rad(deg): #submission1
    return round(deg/180 * math.pi,5)

 
def rad_to_deg(rad):
    return round(rad/math.pi * 180,5)

print(deg_to_rad(180))
print(rad_to_deg(2*math.pi))


import numpy as np  #submission2
def spherical_to_cartesian(r,theta,phi):
    x = r*(np.sin(theta))*(np.cos(phi))
    y = r*(np.sin(theta))*(np.sin(phi))
    z = r*(np.cos(theta))
    return round(x,5),round(y,5),round(z,5)
	

import numpy as np 
def spherical_to_cartesian(r,theta,phi):
    x = r*(np.sin(theta))*(np.cos(phi))
    y = r*(np.sin(theta))*(np.sin(phi))
    z = r*(np.cos(theta))
    return round(x,5),round(y,5),round(z,5)
	

    

import numpy as np
def cartesian_to_spherical(x, y, z):
    r = (x**2+y**2+z**2)**0.5
    theta = np.arccos(z/r)
    if y==0 or x==0:
        phi =0
    else:
        phi = np.arctan(y/x)

    return round(r,5),round(theta,5),round(phi,5)

cartesian_to_spherical(0,1,1)
