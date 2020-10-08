def compound_value_months(a,r,n): #csQ2
    total = 0  
    monthly_rate = r/12
    acc=0
    for i in range(n):
        acc=(a+acc)*(1+monthly_rate)
    return round(acc,2)
        
compound_value_months(100,0.03,7)

def find_average(l): ##csQ3
    summation=0
    num_count=0
    total_sum=0
    new_list = []
    if len(l) == 0:
        return 0,0
    for i in l:
        print(i)
        if len(i) == 0:
            avg = 0
            new_list.append(avg)
        else:
            for j in i:
                summation = summation+j
                total_sum = total_sum + j
                avg = summation/(len(i))
                num_count+=1
            
            new_list.append(avg)
            summation = 0
    overall = total_sum/num_count
    
    return new_list, overall

ans= find_average ([[3 ,4] ,[5 ,6 ,7] ,[ -1 ,2 ,8]])
print(ans)


def transpose_matrix(l): #csQ4
    transpose = []
    for i in range(len(l[0])): #row becomes column
        inside_list=[]
        print(i)
        for j in range(len(l)): #column becomes row
            print(j)
            inside_list.append(l[j][i]) #j increments first, then i
        transpose.append(inside_list)
    return transpose

        
            
a = [[1 ,2 ,3] , [4 ,5 ,6] , [7 ,8 ,9],[10,11,12]]
transpose_matrix(a)



phonebook = [{'name':'Andrew', 'mobile_phone':'9477865', 'office_phone':'6612345', 'email':'andrew@sutd.edu.sg'}, {'name':'Bobby', 'mobile_phone':'8123498', 'office_phone':'6654321', 'email':'bobby@sutd.edu.sg'}]

def get_details(name,info,pb): #csQ5
    for i in pb:
        print(i['name'])
        if i['name'] == name:
            return i[info]
        
        
print ( get_details ('Andrew', 'mobile_phone', phonebook ))




def get_base_counts(dna): #csQ5
    new_dict = {'A' : 0, 'C':0,'G':0, 'T':0}
    for i in dna:
        if i == 'A':
            new_dict['A'] += 1
            
        elif i == 'C':
            new_dict['C'] +=1
        
        elif i == 'G':
            new_dict['G'] +=1
        
        elif i == 'T':
            new_dict['T'] +=1

        else:
            return 'The input DNA string is invalid'
    return new_dict


