def list_sum(num): #csQ1
    total = 0
    counter = 0 

    if len(num)==0:
        return 0
    else:
        while counter< len(num):
            total += num[counter]
            counter+=1
    
    return total 

print (" Test case 1: [4.25 ,5.0 ,10.75] ")
ans= list_sum ([4.25 ,5.0 ,10.75])
print (ans)
print (" Test case 2: [5.0] ")
ans= list_sum ([5.0])
print (ans)
print (" Test case 3: []")
ans= list_sum ([])
print (ans)

def minmax_in_list(nl): #csQ2
    nlist = nl
    if len(nlist)>0:
        greatest=nlist[0]
        lowest=nlist[0]
        for i in nl:
            if greatest<i:
                greatest = i
            elif lowest>i:
                lowest=i
    else: 
        return None,None
        
    return (lowest,greatest)

print (" Test case 1: [1 ,2 ,3 ,4 ,5]")
ans= minmax_in_list ([-1 ,2 ,3 ,4 ,5])
print (ans)

print (" Test case 2: [1 ,1 ,3 ,0]")
ans= minmax_in_list ([1 ,1 ,3 ,0])
print (ans)

print (" Test case 3: [3 ,2 ,1]")
ans= minmax_in_list ([3 ,2 ,1])
print (ans)

print (" Test case 4: [0 ,10]")
ans= minmax_in_list ([0 ,10])
print (ans)

print (" Test case 5: [1]")
ans= minmax_in_list ([1])
print (ans)

print (" Test case 6: []")
ans= minmax_in_list ([])
print (ans)

print (" Test case 7: [1 ,1 ,1 ,1 ,1]")
ans= minmax_in_list ([1 ,1 ,1 ,1 ,1])
print (ans)

import math
def is_palindrome(nl): #csQ3
    counter = 0
    strnl=str(nl)

    while counter < ((len(strnl)/2)):

        if strnl[counter] == strnl[(len(strnl)-1)-counter]:
            counter +=1
            if counter == int(len(strnl)/2) or counter == (len(strnl)): #for 1
                return True
        else:
            return False
print (" Test case 1: 1")
ans= is_palindrome (1)
print (ans)
