def temp_convert(letter,t): #hwQ1
    if letter=='C':
        return fahrenheit_to_celsius(t)
    elif letter =='F':
        return celsius_to_fahrenheit(t)
    else:
        return None

def fahrenheit_to_celsius(temp): 
    C = (temp-32)/(9/5)
    return C

def celsius_to_fahrenheit(temp): 
    F = temp*9/5 + 32
    return F
###############################################

def get_even_list(nlist): #hwQ2
    counter=0
    nnlist=[]
    while counter<len(nlist):
        if nlist[counter] % 2 == 0:
            nnlist.append(nlist[counter])
            counter +=1
        else:
            counter +=1
    return nnlist


print (" get_even_list ([1 ,2 ,3 ,4 ,5])")
ans= get_even_list ([2,3,1,5,4])
print (ans)

print (" get_even_list ([11 ,22 ,33 ,44 ,55]) ")
ans= get_even_list ([11 ,22 ,33 ,44 ,55])
print (ans)
print (" get_even_list ([10 ,20 ,30 ,40 ,50]) ")
ans= get_even_list ([10 ,20 ,30 ,40 ,50])
print (ans)
print (" get_even_list ([11 ,21 ,31 ,41 ,51]) ")
ans= get_even_list ([11 ,21 ,31 ,41 ,51])
print (ans)


###########################################

def is_prime(n): #hwQ3
    counter = 1
    condition = True
    if n>1: # to test if input number is greater than 1
        while condition == True and n > counter: #if input number is greater than counter then run
            if n%(counter+1) == 0 and n != counter+1: #number divided by any number other than itself gives remainder 0 is NOT a prime
                condition = False
            else:
                counter+=1
    else:
        condition = False
    return condition
    
print (" is_prime (2)")
ans= is_prime (1)
print (ans)
print (" is_prime (3)")
ans= is_prime (3)
print (ans)
print (" is_prime (7)")
ans= is_prime (7)
print (ans)
print (" is_prime (9)")
ans= is_prime (9)
print (ans)
print (" is_prime (21) ")
ans= is_prime (29)
print (ans)

###########################################

from math import exp
def approx_ode(h,t0,y0,tn): #hwQ4
    while(t0 < tn):
        differential = 3 + exp(-t0) - 0.5*y0
        y1 = y0 + h * differential
        t1 = t0 + h
        t0 = t1
        y0 = y1
    return round(y0,3)

print ('approx_ode (0.1 , 0, 1, 5) ')
ans = approx_ode (0.1 , 0, 1, 5)
print ('Output : ', ans)

print ('approx_ode (0.1 , 0, 1, 2.5) ')
ans = approx_ode (0.1 , 0, 1, 2.5)
print ('Output : ', ans)

print ('approx_ode (0.1 , 0, 1, 3) ')
ans = approx_ode (0.1 , 0, 1, 3)
print ('Output : ', ans)

print ('approx_ode (0.1 , 0, 1, 1) ')
ans = approx_ode (0.1 , 0, 1, 1)
print ('Output : ', ans)

print ('approx_ode (0.1 , 0, 1, 0) ')
ans = approx_ode (0.1 , 0, 1, 0)
print ('Output : ', ans)