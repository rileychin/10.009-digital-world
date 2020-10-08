import random ##csQ1

craps=set([2,3,12])
naturals=set([7,11])

def roll_two_dices():
    a = random.randint(1,6)
    b = random.randint(1,6)
    sumd = a + b
    return a,b
    

def print_lose():
    print("You lose")
    

def print_win():
    print("You win")
    

def print_point(p):
    print("Your points are",p)
    pass

def is_craps(n):
    if n in craps:
        return True


def is_naturals(n):
    if n in naturals:
        return True



# ATTENTION!
# You shouldn't need to edit the function below

def play_craps():
    point=-1
    while True:
        n1,n2=roll_two_dices()
        sumn=n1+n2
        print ('You rolled %d + %d = %d'%(n1,n2,sumn))   #initial points obtained here
        if point==-1:              #At the initialisation of point == -1 (see line 29)
            if is_craps(sumn):  #if the sum is in the set of craps
                print_lose()     #then it is an immediate loss
                return 0
            elif is_naturals(sumn):   #if the sum is in the set of naturals
                print_win()     #then it is an immediate  win
                return 1
            point=sumn
            print_point(point)
        else:
            if sumn==7:
                print_lose()
                return 0
            elif sumn==point:
                print_win()
                return 1   #goal of the game is to keep rolling dice until the sum == points obtained
    return True

def leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True
    pass

def R(a,n):
    return a%n

def day_of_week_jan1(year):
    d = R((1+5*R(year-1,4)+4*R(year-1,100)+6*R(year-1,400)),7)
    return d
    pass

def num_days_in_month(month_num, leap_year):

    days_31 = [1,3,5,7,8,10,12]
    days_30 = [4,6,9,11]
    if month_num in days_31:
        return 31
    elif month_num in days_30:
        return 30
    elif month_num == 2:
        if leap_year == True:
            return 29
        else: 
            return 28
    pass

def construct_cal_month(month_num, first_day_of_month, num_days_in_month): ##cs part d wtf 
    md = {1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}
    details = [md[month_num]]
    
    week_list=[]
    space = ' '
    first_space = first_day_of_month*(space*3)

    stringy = first_space
    for i in range(1,num_days_in_month+1):

        if len(stringy) > 20:
                details.append(stringy)
                stringy=''

        if i <10:
            stringy+=space*2
            stringy+=str(i)

        else: 
            stringy+=space
            stringy+=str(i)

                
    if len(stringy) > 0:
        details.append(stringy)
    
    return details



def construct_cal_year(year):
    year_list = [year] #make list for a calendar year
    is_leap = leap_year(year) #check if leap year
    first_day_of_year = day_of_week_jan1(year) #check the first day of the month of january 

    year_list.append(construct_cal_month(1,first_day_of_year,num_days_in_month(1, is_leap)))

    md = {2:'February',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}
    

    

    
    for i in md:
        last_day = int(len(year_list[i-1][-1]) / 3)
        if last_day == 7:
            last_day = 0
        first_day_of_month = int(last_day+1) #check for first day of each month
        
        days = num_days_in_month(i, is_leap)
        year_list.append(construct_cal_month(i,last_day,days))
        
    return year_list
    pass


def print_cal_month ( list_of_str ): #delete later also
    ret_val =''
    for l in list_of_str :
        ret_val += l. replace (' ','*')
        ret_val += '\n'
    return ret_val




def display_calendar(year):
    year_list = construct_cal_year(year)
    
    for l in year_list:
        
        if type(l) == list:
            print(l[0])
            l.insert(1,'  S  M  T  W  T  F  S')
            if l[0] != 'December':
                
            
                l.insert(len(year_list)-1,'')

    print(year_list)
    
    ret_val =''
    for l in year_list:
        if type(l) == list:
            for j in range(len(l)):
                ret_val += l[j].replace('*','')
                ret_val += '\n'
    ret_val_real = ret_val[:-1]    
    return ret_val_real

    pass

display_calendar(2000)







def fact_rec(n):#csQ3
    fact = 1
    if n == 1 or 0:
        return fact
    else:
        print(n * fact_rec(n-1),n,"hello")
        return n*(fact_rec(n-1))
        
fact_rec(6)
     
    
def fumi (n):
    if n == 0 : 
        return 0
    elif n == 1 :
        return 1 
    elif n == 2 :
        return 1
    else :
        return ((fumi(n-1) + fumi(n-2) ))
    
print (fumi(7)) #returns what the element is 


print(%3s)