class Coordinate: ##csQ1

    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    
    def magnitude(self):
        mag = (self.x ** 2 + self.y **2) ** 0.5
        return mag
    def translate(self,dx,dy):
        newx = self.x + dx
        newy = self.y + dy 
        self.x = newx
        self.y = newy
        
        return None
    
    def __eq__(self,other): ## defines  p == q, where p is self, q = other
        if (self.x == other.x) and (self.y == other.y):
            return True
        else:
            return False
        
        
p = Coordinate()
p.x = 3
p.y = 4
print(p.x,p.y)
print(p.magnitude())
q = Coordinate()
q.x = 3 
q.y = 4

print(p == q)



class Celsius: ##csQ2
    def __init__(self,temperature = 0):
        self.temperature = temperature
        
        
    def to_fahrenheit(self):
        fahrenheit = self.temperature * 9/5 + 32
        return fahrenheit
    
    def get_temperature(self):
        return self.temperature
    
    def set_temperature(self,value):
        if value < -273:
            temperature = -273
        else: 
            temperature = value
        
        return self.temperature = temperature
    
    def temperature(self):
        
        self._temperature = get_temperature()
        
import time     
class StopWatch: #csQ3
    def __init__(self,start_time=0,end_time=0):
        self.start_time = time.time()
        self.end_time = -1
        
    def start(self):
        self.start_time = time.time()
        self.end_time = -1
    def stop(self):
        self.end_time = time.time()

    def elapsed_time(self):
        if (self.end_time <0):
            return None
        elapsed = round((self.end_time - self.start_time),1)
        
        return elapsed

        
sw = StopWatch ()
time.sleep (0.1)
sw.stop ()
print(sw.elapsed_time ())
sw.start()
time.sleep (0.2)
print(sw.elapsed_time ())
sw.stop()
print (sw. elapsed_time ())


class Line:     #csQ4
    
    def __init__(self,C0=0,C1=0):
        self.C0 = C0
        self.C1 = C1
    
    def __call__(self,x): #makes the object callable
        y = self.C0 + self.C1*x
        return y
   
    def table(self,L,R,n): #table function
        table_str = ""
        if R == L:
            table_str += "{:10.2f}{:10.2f}\n".format(round(L,2),round(self.__call__(L),2))#makes the string 10 spaces
        elif n == 0:
            return "Error in printing table"
        else:
            step = (R-L)/(n-1)
            counter = L
            while counter <= R:
                table_str += "{:10.2f}".format(round(counter,2)) + "{:10.2f}".format(round(self.__call__(counter),2)) + "\n"
                counter += step
        return table_str


##############################################################3    #
#pillars of oop, inheritance    
    
class Employee(object): ##parent class, all employess will inherit attriubtes from here
    
    def __init__(self,first,last,object):
        self.first = first
        self.last = last
        self.pay = pay
    
    def __str__(self):
        return "first"+ str(self.first) + "last" + str(self.last) + "pay" + str(self.pay)
        
class Developer(Employee):
    def __init__(self,first,last,pay,language):
        Employee.__init__(first,last,pay)
        self.language = language
    
    
    def __str__(self):
        return self.first
    
dev1 = Developer("john","luke",1000,'Python')

print(str(dev1))