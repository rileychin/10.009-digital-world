import copy

x = [['1']]
y=x
y1 =x[:]
y2 = copy.deepcopy(x)

x[0] = 'hello'
print(x)

print(y,y1,y2)


mydict = {"cat":12, "dog":6, "elephant":23}
items=mydict.items()
print(items)
lister = list(mydict.values())
mydict.pop("cat")
print(mydict)
print(lister)
mydict["mouse"] = mydict["cat"] + mydict["dog"]
print(mydict)



def most_frequent(l):##hwQ4
    mf_list = []
    most_freq = l[0]
    for i in l: #run one time to check the most 
        if i not in mf_list:
            if l.count(i) > l.count(most_freq):
                most_freq = i
    mf_list.append(most_freq)
    print(mf_list)
    for i in l:
        if i not in mf_list:
            if (l.count(i) == l.count(most_freq)):
                mf_list.append(i)
    return mf_list

x=[1,1,2,2,3,3]
most_frequent(x)
      
p={0: -3 , 3:2 , 5: -1}
for i in p:
    print(p[i])
    
    
mylist = [1,2,3,4,5]
mylist[1::2]




def prime_prod(num):
    prime_list = [2]
    for i in range(2,num):
        for j in range(2,num):
            if i % j == 0:
                continue
            else: 
                prime_list.append(i)

return prime_list
prime_prod(33)