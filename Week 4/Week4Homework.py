def f_to_c(f):                ### hwQ1a,b
    c = (f-32) * (5/9)
    return c
    
def f_to_c_approx(f):
    c = (f-30)/2
    return c

def get_conversion_table_a():
    overall = []
    for i in range(0,110,10):
        inside =[]
        x = round(f_to_c(i),1)
        y = f_to_c_approx(i)

        inside.append(i)
        inside.append(x)
        inside.append(y)
        overall.append(inside)
        
    return overall


def get_conversion_table_b():
    temp_list = []
    approx =[]
    exact =[]
    overall = []
    for i in range(0,110,10):

        x = round(f_to_c(i),1)
        y = f_to_c_approx(i)

        temp_list.append(i)
        exact.append(x)
        approx.append(y)
    overall.append(temp_list)
    overall.append(exact)
    overall.append(approx)
        
    return overall



def max_list(l): ##hwQ2
    new_list = []
    for i in l:
        max_num = i[0]
        for j in i:
            if j>max_num:
                max_num = j 
        new_list.append(max_num)
    return new_list

]

def multiplication_table(n): ##hwQ3
    overall = []
    if n>0:
        for i in range(n):
            print(i)
            inside =[]
            for j in range(n):
                prod = (j+1)*(i+1)
                inside.append(prod)
            overall.append(inside)
    else:
        return None
    return overall
        
multiplication_table(7)


x=[1,2,3,4,5]
print(x.count(5))


def most_frequent(l):##hwQ4
    mf_list = []
    most_freq = l[0]
    for i in l: #run one time to check the most 
        if i not in mf_list:
            if l.count(i) > l.count(most_freq):
                most_freq = i
    mf_list.append(most_freq)
    print(mf_list)
    for i in l: #run again to check if there are others
        if i not in mf_list:
            if (l.count(i) == l.count(most_freq)):
                mf_list.append(i)
    return mf_list


most_frequent([9,30,3,9,3,2,4])


def diff(p): #hwQ5
    new_dict = {}
    coeff_list = list(p.values()) #make values into a list for easy reference
    exponent_list = list(p.keys()) #make exponents into a list for easy reference
    print(coeff_list,exponent_list)
    counter = 0
    for i in exponent_list:
        if i != 0:
            new_exp = i - 1 #exponent -1
            new_coeff = i * coeff_list[counter] #new coeff = exponent * coeff
            new_dict[new_exp] = new_coeff #adding new entry into dictionary
            counter+=1
        else: 
            counter+=1
    return new_dict
        
        
p={0: -3 , 3:2 , 5: -1}       #keys are EXPONENTS, values are COEFF 
diff(p)

x={'a':1,'b':2}
for i in x:
    print(x[i])