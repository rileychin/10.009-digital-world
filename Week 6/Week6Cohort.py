def reverse(s): #csQ1
    ns=''
    for i in s:
        ns = i + ns
        
    return ns
        
reverse('hello')
        
        

def check_password(pw): #csQ2
    if len(pw) < 8:
        return False
    digit_counter = 0
    for i in pw: 
        if i.isdigit() == False and i.isalpha() == False:
            return False
        if i.isdigit() == True:
            digit_counter += 1 
    if digit_counter < 2:
        return False
    return True

def longest_common_prefix(str1, str2): #csQ3
    str3 =''
    for x,y in zip(str1, str2):
        if x == y:
            str3 += x
        else:
            return str3
    return str3
    


def foo ():
    a= Coordinate ()
    a.x =1.0
    a.y =2.0
    return a

class Coordinate:
    x = 0
    y = 0

def get_maxmin_mag(f): #csQ4
    mag_dict = {} #create dictionary to pair magnitude and coordinates
    p1 = Coordinate()
    for i in f: #loop through the file to 
        splitty = i.split()
        
        mag = (float(splitty[0])**2 + float(splitty[1])**2 ) ** 0.5
        mag_dict[mag] = "{} {}".format(float(splitty[0]),float(splitty[1]))
    print(mag_dict)
    max_value = max(mag_dict)
    min_value = min(mag_dict)
    f1=mag_dict[max_value]
    f2=mag_dict[min_value]
    print(f1,f2,'asddsa')
    f1_split = f1.split()
    f2_split = f2.split()
    
    pmax = Coordinate()
    pmax.x = float(f1_split[0])
    pmax.y = float(f1_split[1])
 
    pmin = Coordinate()
    pmin.x = float(f2_split[0])
    pmin.y = float(f2_split[1])
    print(f1,f2,'hello')
    return pmax, pmin


f= open('http://localhost:8888/lab/tree/DW%20Week%205/xy.txt','r')
pmax , pmin = get_maxmin_mag (f)
print ('max: ({:f}, {:f}) '. format ( pmax .x, pmax .y))
print ('min: ({:f}, {:f}) '. format ( pmin .x, pmin .y))

dictionary = {1:'a',2:'b'}
print(max(dictionary.values()))