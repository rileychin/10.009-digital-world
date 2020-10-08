list=['a','b','c']

for i in list:
    print(i)


list=1
strnl=str(list)
print(len(strnl)/2)


x=[1,2,3,4,5]
x.remove(2)
print(x)

import sympy as sp
import math 
x = sp.Symbol('x')

y = x**2+1
y1= sp.exp(-x)
print(y1)
ff = sp.lambdify(x,y)
y=ff(math.cos(math.pi))

print(y)

import matplotlib.pyplot as plt
x = [ 1 , 2 , 3 , 4 , 5 ]
y = [ 1 , 4 , 9 , 16 , 25 ]
plt.plot(x,y)
plt.xlabel( 'x values' )
plt.ylabel( 'y values' )
plt.title( 'y = x squared' )
plt.show()


l = ['1234','12345']
counter = 0
while counter<len(l[1]):
    if l[1][counter] == '3':
        print('hi')
    print(l[1][counter])
    counter+=1
    
    
MCD = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'} 
statement=['SOS']


new = ""
print(MCD.keys())
morse_list=[""]

for i in statement[len(statement)-1]:
    new = new + MCD[i]
morse_list.append(new)
    
print(morse_list)

"import matplotlib.pyplot as plt
mean_temperature = [ 24.8, 25.5, 26.5, 26.1, 26, 26.8, 26.9, 26.4, 27.2, 24.5, 23.9, 23.1, 23, 23.4, 25.2, 26.2, 27.2, 27.2, 26.9, 26.4, 27.2, 27.5, 26.8, 26.7, 26.6, 26.4, 27.1, 26.3, 27.7, 26.9, 27.3] 

ll=[1,2,3,4,5]

plt.hist(ll, bins=range(1,5,2) )

plt.show()"