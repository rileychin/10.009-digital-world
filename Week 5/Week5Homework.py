# NB: you do not need to submit the 'get_data' function

def get_data(): ##hwQ1
    integers = str(input("enter 2 integers"))
    return integers

def extract_values(values):
    f = values.split()
    return(int(f[0]),int(f[1]))
    print(f)
    pass

def calc_ratios(values):
    
    if values[1] == 0:
        ratio = None
    else: 
        ratio = float(values[0])/float(values[1])
    return ratio
    pass
x=get_data()
l=extract_values(x)
calc_ratios(l)


x=(1,2)
print(x[1])


from Week5Cohort import *

def display_calendar_modified(year, month): #hwQ2
    md = {1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}
    
    if month == None:
        f = display_calendar(year)
    else: 
        year_list = construct_cal_year(year)

        for i in md:
            if i == month: 
                month_string = md[i]
                month_list = year_list[month]
                month_list.append(1,'  S  M  T  W  T  F  S')
        print(month_list)

        ret_val = ""
        for i in month_list:
            ret_val += i +"\n"
            

        return ret_val
    pass


display_calendar_modified(2007,2)