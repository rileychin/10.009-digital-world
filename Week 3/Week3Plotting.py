import matplotlib.pyplot as plt
x = [ 1 , 2 , 3 , 4 , 5 ]
y = [ 1 , 4 , 9 , 16 , 25 ]
plt.scatter(x,y) ##(xpoints,ypoints)
plt.xlabel( 'x values' )
plt.ylabel( 'y values' )
plt.title( 'y = x squared' )
plt.show()

print("hello",end=" ")
print("yo",end=" ")

x=[0,1,1.5,2,2.5,3,4,5] ##histogram bins

plt.hist(x,[0,1,2,3])#2nd argument is the bins inside which the number of values are tallied 0<=x<1, 1<=x<2, 2<=x<=3
plt.xlabel("hello")
plt.ylabel("hey here")
plt.show()
#PART 2 PSET
import math
import matplotlib.pyplot as plt
x_list = list(range(-5,6))

def logistic(x):
    #e=math.exp(x)
    y=1/(1+ math.exp(-x))
    return y
               
def calculate_y(xpoints):
    y=[]
    
    pos = 0
    
    while pos<len(xpoints):
        y.append(logistic(xpoints[pos]))
        
        pos += 1
        
    return y

y_list = calculate_y(x_list)
print(y_list)
plt.plot(x_list, y_list,'-o')
plt.ylabel("y values")
plt.xlabel("x labels")
plt.title("Logistic Function")
plt.show()


#########################################################################


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 15:49:03 2019

@author: norman_lee
"""

"""
data for Nov 2018
daily total rainfall in mm of rain 
""" 


# -5 to 5, step 1

x_list = list(range(-5, 6))
from math import exp
import matplotlib.pyplot
import matplotlib.pyplot as plt


def logistic(x):
    #to calculate logistic
    # for one x point
    y = 1/(1+exp(-x))
    return y

def calculate_y(xpoints):
    #you need to call logistic()
    #use while loop for every x
    #use y.append
    y = []
    # your code
    #Init block
    pos = 0 # zero is the index of the first element
    #condition
    while pos < len(xpoints):
        #Block A
        y.append(logistic(xpoints[pos]))
        #Modify condition
        pos += 1
        #Block B
        
    return y

y_list = calculate_y(x_list)
plt.plot(x_list, y_list, '-o')
plt.scatter(x_list, y_list)
plt.ylabel("y values")
plt.xlabel("x values")
plt.title("Logistic Funcition")
plt.show()
print(y_list) #remove?

#rainfall###################################################################
                 
rainfall = [ 0.2, 
7.8,
0.4,
3.4,
0.4,
3.8,
12,
5.4,
1.6,
0,
0.8,
12.4,
2.4,
2,
4.6,
0.8,
18.4,
7.4,
20.6,
4,
13.2,
2,
4,
0,
4.8,
14.4,
9.6,
0,
5.6,
7.6 ] 

plt.hist(rainfall, bins = [0, 4, 8, 12, 16, 20, 24])
plt.xlabel('whass')
plt.show()
#box plot


import numpy as np
spread = np.random.rand(50) * 100
print(type(spread))
center = np.ones(25) * 50
print(len(center))
flier_high = np.random.rand(10) * 100 + 100
print(flier_high)
flier_low = np.random.rand(10) * -100
print(flier_low)
data = np.concatenate((spread, center, flier_high, flier_low))
#randomly generate values

print(data)

plt.boxplot(data)
plt.title('box plot')

import numpy as np
x=[np.array([1,2,3,4,5])]
print(type(x))
y=[np.array([6,7,8,9,10])]
print(type(y),y)
data=np.concatenate((x,y))
print(type(data))

# barchart for dry and wet days
performance = [10,8,6,4,2,1,7,2,1,2,2]
labels=["A","B"]
A=[]
B=[]
for i in performance:
    if i<5:
        A+=[i]
    else:
        B+=[i]
count=[len(A),len(B)]
        
plt.bar([0,3],count)
plt.xticks([0,3], count)
###################################3

def count_dry(rainfall, threshold):
    # rainfall_data is a list
    # if rainfall <= threshold: consider as dry
    dry_days = 0
    # Init block
    day = 0 # first element in data
    # condition
    while day < len(rainfall):
        # Block A
        if rainfall[day] <= threshold:
            # modify condition
            dry_days+= 1
    # Block B
        day +=1
    return dry_days

dry = count_dry(rainfall, 5)
wet = len(rainfall) - dry
plt.bar([0,4], [dry, wet])
plt.xticks([0,7], ["dry", "wet"])
plt.show()

dry = count_dry(rainfall, 0)
print(dry)
""" 
data for Jan 2018
mean temperature is in degrees C
""" 

mean_temperature = [
        24.8,
25.5,
26.5,
26.1,
26,
26.8,
26.9,
26.4,
27.2,
24.5,
23.9,
23.1,
23,
23.4,
25.2,
26.2,
27.2,
27.2,
26.9,
26.4,
27.2,
27.5,
26.8,
26.7,
26.6,
26.4,
27.1,
26.3,
27.7,
26.9,
27.3]




