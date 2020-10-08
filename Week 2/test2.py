#class Coordinate:
 #   x=0.0
  #  y=0.0
    
def f():
    return 1, 2, 3

_, _, x = f()
_,y,_=f()
print(y)
print(x)

x="{:.3f}".format(x)

print(x)

def print_temp():
    return 3,4

x,_=print_temp()
x="{:.3f}".format(x)
_,y=print_temp()
y="{:.3f}".format(y)
command = "the temperature in celsius is " +x + " and in fahrenheit " +y
print(command)
command= str(command)
print(command)

from timer import Timer

t=Timer()
x=t.start()

print()

class Coordinate:
    x=0
    y=0
    
def is_in_square(c1,side1,c2,side2):
    topleft_1 = Coordinate()
    botright_1 = Coordinate()
    topleft_2 = Coordinate()
    botright_2 = Coordinate()
    
    topleft_1.x = c1.x-0.5*side1
    topleft_1.y = c1.y+0.5*side1
    botright_1.x = c1.x+0.5*side1
    botright_1.y = c1.y-0.5*side1
    
    topleft_2.x = c1.x-0.5*side1
    topleft_2.y = c1.y+0.5*side1
    botright_2.x = c1.x+0.5*side1
    botright_2.y = c1.y-0.5*side1
    
    #c1=Coordinate()
    #c1.x,c1.y = 10,10
    #c2=Coordinate()
    #c2.x,c2.y = 20,10

    
    print (topleft_1.x,topleft_1.y)
    print (botright_1.x,botright_1.y)
    print (topleft_2.x,topleft_2.y)
    print (botright_2.x,botright_2.y)
    
    if botright_2.y > topleft_1.y:
        return False
    if botright_2.x < topleft_1.x:
        return False
    if topleft_2.y < botright_1.y:
        return False
    if topleft_2.x > botright_1.x:
        return False
    else:
        return True
    
s1 = Coordinate() 
s1.x,s1.y = 10,10 #square1 center coordinate
s2 = Coordinate()
s2.x,s2.y = 20,10 #square2 center coordinate
is_in_square(s1,5,s2,4)

x=1
typ = type(x)
if typ == bool:
    print(True)
else:
    print(False)
    
x="/hello"

for i in x:
    print(x.index(i))
sl = (x[1:3])
print(sl)


message = "speed is now " , 7
message= str(message)
print(message)