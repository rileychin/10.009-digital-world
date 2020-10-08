####
x = 'aces' #Q1
y = 1.23
z = x
x = y
y = z
print(x, y)

# line 3, z =  'aces'
#line 4, x = 1.23
#line 5, y = 'aces'


####
french = [ 'sept', 'huit', 'neuf' ] #the words mean 'seven','eight','nine'. 
greek = french[:]
greek[0] = 'epta' # 'seven'
greek[1] = 'okto' # 'eight'
greek[2] = 'enea' # 'nine'
print(greek is french)
print(french, greek)

####
import = int(input("Enter a number: "))
if import==2:
print("Yes")
else:
print("No")

####
my_string = "Computing"
for character in my_string:
    print(character)
    if character == "u":
        print("Found 'u' :)")
        break
        
####        
def my_function(n):
    return_value = None
    if n == 0 or n == 1:
        return_value = False
    i=2
    while i < n**0.5:
        if n%i==0:
            return_value = False
            break
        i+=1
        return_value = True
    return return_value

my_function(37)
print(my_function(37))



#PART B 
#### Q3
def area_square(s):
    return s**2

def vol_frustum(top_area,bottom_area,height):
    vol = height/3*(top_area + bottom_area + (top_area * bottom_area) ** 0.5)
    return vol

def get_volume(s1,s2,height):
    a1 = area_square(s1)
    a2 = area_square(s2)
    vol = vol_frustum(a1,a2,height)
    return vol

print('{:.3f}'.format(area_square(2)))
print('{:.3f}'.format(area_square(3)))
print('{:.3f}'.format(vol_frustum(1,4,2)))
print('{:.3f}'.format(vol_frustum(2,2,2)))


#### Q4
def determinant(matrix):
    if len(matrix[0]) != len(matrix):
        return None
    if len(matrix[0]) <1 or len(matrix[0]) > 3:
        return None
    if len(matrix) == 1:
        det = matrix[0][0]
        return matrix[0][0]
    if len(matrix) == 2:
        det = matrix[0][0] * matrix[1][1] - matrix[0][1]*matrix[1][0]
        return det
    if len(matrix) == 3:
        new_list = []
        other_list = []
        det = 0
        for i in range(3):
            if i == 0:
                other_list.append(matrix[1][1])
                other_list.append(matrix[1][2])
                new_list.append(other_list)
                other_list = []
                other_list.append(matrix[2][1])
                other_list.append(matrix[2][2])
                new_list.append(other_list)
                other_list = []
                det += matrix[0][0] * determinant(new_list)
                print(new_list,det,'a')
                new_list.clear()
            if i == 1:
                other_list.append(matrix[1][0])
                other_list.append(matrix[1][2])
                new_list.append(other_list)
                other_list = []
                other_list.append(matrix[2][0])
                other_list.append(matrix[2][2])
                new_list.append(other_list)
                other_list = []
                det += -matrix[0][1] * determinant(new_list)
                print(new_list,det,'a')
                new_list.clear()
            if i == 2:
                other_list.append(matrix[1][0])
                other_list.append(matrix[1][1])
                new_list.append(other_list)
                other_list = []
                other_list.append(matrix[2][0])
                other_list.append(matrix[2][1])
                new_list.append(other_list)
                other_list = []
                det += matrix[0][2] * determinant(new_list)
                print(new_list,det,'a')
                new_list.clear()
        return det
            
print(determinant([[100]]))
print(determinant([[-5, -4], [-2, -3]]))
print(determinant([[2, -3, 1],
[2, 0, -1], [1, 4, 5]]))



x= 1 
print(x.imag,x.real)
##### Q5
def nroot(n,i,num):
    if i == 1:
        return 1 - (1**n - num)/(n*1**(n-1))
    else:
        return nroot(n,i-1,num) - (nroot(n,i-1,num)**n-num)/(n*nroot(n,i-1,num)**(n-1))

print(nroot(2,5,2))
    


#####Q6
f= open("C:\\Users\\riley\\Desktop\\todo.txt")

def read_stations(f): #part a
    listy1=[]
    listy2 = []
    train_dict = {}
    for i in f:
        listy1.append(i)
        listy2.append(listy1)
        listy1=[]
    for i in listy2:
        for j in i:
            stripped = j.rstrip() #remove trailing \n
            strippped = stripped.strip('=') #remove =
            stripppped = strippped.strip() #remove spaces but not needed
            listy1.append(stripppped)
    for i in range(0,len(listy1),2):
        train_dict[listy1[i]] = listy1[i+1].split(', ')
    return train_dict

    
def get_stationline(mrt):
    dict_train = {}
    line_list = []
    for line in mrt:
        for station in mrt[line]:
            line_list.append(line)
            if station not in dict_train:
                dict_train[station] = line_list
            if dict_train[station][0] != line:
                dict_train[station].append(line)
            line_list=[]
    return dict_train




def get_interchange(stationline):
    dd_train = {}
    for station in stationline:
        if len(stationline[station]) > 1:
            dd_train[station] = stationline[station]
    return dd_train
        



def find_path(f,start,end):
    change_counter = 0
    starting_p = {}
    ending_p = {}
    read_station = read_stations(f)
    stationline = get_stationline(read_station)
    interchanges = get_interchange(stationline)
    for line in read_station:
        if start in read_station[line]:
            starting_p[line] = list((start,read_station[line].index(start)))
        if end in read_station[line]:
            ending_p[line] = list((end,read_station[line].index(end)))
    print(starting_p,ending_p)
    optimal_path = []
    interchange_path = []
    print(optimal_path)
    for i,j in zip(starting_p,ending_p):
        if i == j:
            
            if starting_p[i][1] > ending_p[j][1]:
                for k in range(starting_p[i][1],ending_p[j][1]-1,-1):
                    optimal_path.append(read_station[i][k])
            elif starting_p[i][1] < ending_p[i][1]:
                for k in range(starting_p[j][1],ending_p[j][1]+1):
                    optimal_path.append(read_station[i][k])
        elif i != j: 
            
            for k in interchanges:
                if (i in interchanges[k]) and (j in interchanges[k]):
                    if starting_p[i][1] > read_station[i].index(k):
                        for length in range(starting_p[i][1],read_station[i].index(k)-1,-1):
                            interchange_path.append(read_station[i][length])
                        optimal_path.append(interchange_path)
                        interchange_path=[]
                        change_counter +=1
                    else:
                        for length in range(starting_p[i][1],read_station[i].index(k)+1):
                            interchange_path.append(read_station[i][length])
                        optimal_path.append(interchange_path)
                        interchange_path = []
                        change_counter +=1
                else:
                    return None
            print(optimal_path)
            optimal_path.sort()
            

            
            for station_list in optimal_path:
                last_element=station_list[len(station_list)-1]
                if ending_p[j][1] > read_station[j].index(last_element):
                    for length in range(read_station[j].index(last_element)+1,ending_p[j][1]+1,+1):
                        station_list.append(read_station[j][length])
                else:
                    for length in range(read_station[j].index(last_element)+1,ending_p[j][1]-1,-1):
                        station_list.append(read_station[j][length])
                
    return optimal_path[0]
                    

find_path(open("C:\\Users\\riley\\Desktop\\todo.txt"), 'Clementi', 'Changi Airport')


x = [1,2,3,4,5,6,7]

def reversse(x):
    reverse_list = []
    for i in x:
        print(i,reverse_list,'here')
        reverse_list = [i] + reverse_list
        
    return reverse_list

reversse(x)

x="12,3,4,5"
x=x.join(',')
print(x)
def reverse(x):
    if len(x) == 1:
        return x
    else:
        return reverse(x[1:]) + [x[0]]

reverse(x)


def gcd(n1,n2): #wk3 problem 4 
    gcd =0
    if n1 < 0 or n2< 0:
        return None
    else:
        if n1>n2:
            for i in range(1,n2+1):
                if n1 % i == 0 and n2 % i == 0 :
                    gcd = i
        else:
            for i in range(1,n1+1):
                if n1%i == 0 and n2%i == 0:
                    gcd = i
    return gcd

print(gcd(60,100))


def interlock(word1,word2,word3):
    counter = 0
    if (len(word1) != len(word2)) or (len(word1) + len(word2) != len(word3)):
        return False
    else:
        for i in range(0,len(word3)+1):
            if i+counter >= len(word3):
                break
            print(word1[i],word2[i],word3[i+counter],word3[i+counter+1])
            if word1[i] == word3[i+counter]:
                if word2[i] == word3[i+counter+1]:
                    counter+=1
                    continue
            
            else:
                return False
    return True

interlock('can','his','chains')

def hanoi(h,source,dest,spare):
    if h == 1:
        print(h,'from',source,'to',dest)
    else:
        hanoi(h-1,source,dest,spare)
        print(h,'from',source,'to',dest)
        hanoi(h-1,dest,spare,source)
    
hanoi(2,'A','B','C')


def find_all(array,n):
    occurence = []
    for num in range(len(array)):
        if array[num] == n:
            occurence.append(num)
    return occurence
    
    
find_all([10,16,20,6,14,11,20,2,17,16,14],16)    




def digital_root(n):
    if len(str(n)) == 1:
        return n
    elif len(str(n))>1:
        return int(str(n)[0]) + int(digital_root(str(n)[1:]))
    
digital_root(456)
digital_root(456)
