class Time: #hwQ1
    def __init__(self,h,m,s):
        self._hours = h #private attribute hour
        self._minutes = m #private attribute minutes
        self._seconds = s #private attribute seconds
    
    def __str__(self):
        return "Time: {}:{}:{}".format(self._hours,self._minutes,self._seconds)
    
    def get_seconds(self):
        return self._hours * 3600 + self._minutes * 60 + self._seconds
    
    def set_seconds(self,value):
        if value>86400:
            dayselapsed = value//86400
            value = value - 86400*dayselapsed
        elif value == 86400:
            self._hours = 0
            self._minutes = 0
            self._seconds = 0
        
        self._hours = value//3600
        self._minutes = value%3600 //60
        self._seconds = value%3600 % 60
    
            
    elapsed_time = property(get_seconds,set_seconds) #property runs the functions and assigns new attributes to the class

def is_equal(t1,t2):
    h = int(t1._hours) == int(t2._hours)
    m = int(t1._minutes) == int(t2._minutes)
    s = int(t1._seconds) == int(t2._seconds)
    print(h,m,s)
    if h and m and s:
        return True
    else:
        return False
    

t1 = Time(10,19,10)
t1.elapsed_time = 361510
t2 = Time(4,25,10)
print(t1._hours,t2._hours)


class Account: ##hwQ2
    
    def __init__(self,owner,account_number,amount):
        self._owner = owner
        self._account_number = account_number
        self._balance = amount
        
    def deposit(self,amount):
        self._balance = self._balance + amount
    
    def withdraw(self,amount):
        self._balance = self._balance - amount
    
    def __str__(self):
        return "{}, {}, balance: {}".format(self._owner,self._account_number,self._balance)


def is_equal(a1,a2):
    own = a1._owner == a2._owner
    ac = a1._account_number == a2._account_number
    bal = a1._balance == a2._balance
    print(a1._balance, a2._balance)
    ans = True
    
    if own and ac and bal:
        ans = True
    else:
        ans = False
    return ans


a1 = Account('John Olsson', '19371554951', 20000)                             
a2 = Account('Liz Olsson', '19371564761', 20000)                              
a1.deposit(1000)                                                              
a1.withdraw(4000)                                                             
a2.withdraw(10500)                                                            
a1.withdraw(3500)                                                             
sol1 = Account('John Olsson', '19371554951', 13500)                           
return is_equal(a1, sol1)  








import numpy as np
class Diff:#hwQ3
    def __init__(self,function,h=(10**(-4))): #function h is already in built inside vocareum, no need to define ourselves
        self.h = h
        self.function = function
        print(function,'asdsadsadsa')
    
    def __call__(self,value):

        exact = (self.function(value+self.h) - self.function(value))/self.h
        return exact
        
import copy        
class Polynomial: #hwQ4
    def __init__(self,listi):
        self.coeff = listi
        
    def __call__(self,value): #makes the function callable
        total = 0
        for i in range(len(self.coeff)):
            total += self.coeff[i]*(value**i)
        return total
    
    def __add__(self,other): #magic method associated with +
        x3 = []
        p1 = copy.deepcopy(self.coeff)
        q1 = copy.deepcopy(other.coeff)
        if len(p1) > len(q1):
            l = p1
            s = q1
        else:
            l = q1
            s = p1
            
        diff = len(l) - len(s)
        for i in range(1,diff+1):
            s.append(0)
        
        for x,y in zip(l,s):
            x3.append(x+y)
        return Polynomial(x3) #create new class instance when 2 polynomials are added together
    
    def __sub__(self,other): #magic method associated with -
        x3 = []
        p2 = copy.deepcopy(self.coeff)
        q2 = copy.deepcopy(other.coeff)
        
        if len(p2) > len(q2):
            l = p2
            s = q2
        else:
            l = q2
            s = p2    
        
        diff = len(l) - len(s)
        for i in range(1,diff+1):
            s.append(0)
        
        for x,y in zip(l,s):
            if l == p2:
                x3.append(x-y)
            else:
                x3.append(y-x)
        return Polynomial(x3) #create new class instance when 2 polynomials are added together
        
    def __mul__(self,other): #magic method associated with *
        x3 = []
        p3 = copy.deepcopy(self.coeff)
        q3 = copy.deepcopy(other.coeff)
        
        if len(p3) > len(q3):
            l = p3
            s = q3
        else:
            l = q3
            s = p3
            
        poly_dict = {}
        for i in range(len(s)):
            if i == 0:
                for j in range(len(l)):
                    poly_dict[i+j] = s[i] *l[j]
            else:
                for j in range(len(l)):
                    if i+j not in poly_dict:
                        poly_dict[i+j] = s[i] * l[j]
                    else:
                        poly_dict[i+j] += s[i] * l[j]
        print(poly_dict)
        for i in poly_dict:
            x3.append(poly_dict[i])
        return Polynomial(x3)
    
    def derivative(self):
        x3 = []
        for i in range(1,len(self.coeff)):
            x3.append(self.coeff[i]*i)
        return Polynomial(x3)
    
    def differentiate(self):
        x3 = []
        for i in range(1,len(self.coeff)):
            x3.append(self.coeff[i]*i)
        self.coeff = x3
        return None
    
    
p1 = Polynomial ([1,-1])                                                     
p2 = Polynomial ([0,1,0,0,-6,-1])  
p3 = Polynomial([1,3,5,7,9])
p3.differentiate()
p3.coeff
print(p1.coeff,p2.coeff)
p4 = p1 + p2     #new class is created
print(p4.coeff,'hello')  #
print(p1.coeff,p2.coeff)
p3 = p1*p2
print(p3.coeff)


x=[1,2,3,4]
y=[7,8,9]

f = {1:2,5:6}
f[4] = 7
print(f)
f[4] = 5
print(2 not in f)