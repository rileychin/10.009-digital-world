import numpy as np
a = np.array(([3,1], [1,2]))
b = np.array(([9,8,7]))
print(a[0,0])
# print(type(a),type(b))
# x = np.linalg.solve(a, b) #solves it as a linear system
# # print(x)
print(a.shape,b.shape,x.shape)
# a1 = a[[0],:]
# print(a1, a1.shape)
# a2 = a[:,[0]]
# print(a2, a2.shape)



# ls = 1
# a3 = a[ls,:] #must have ,
# print(a3, a3.shape)
# a4 = a[:,ls]
# print(a4, a4.shape)

print(b)
b1 = b.reshape(1, b.size) #now b1 is a 1 by n 2D array
print(b1,b.shape)
b2 = b.reshape(b.size, 1) #now b2 is a n by 1 2D array 
print(b2)

#practice
m = [ [1,-1,0], [-1, 2, -1], [0, -1, 1] ]
M = np.array(m)
print(M) #3x3 matrix
w, v = np.linalg.eig(M) #w is eigenvalues, v is eigenvectors
v1 = v[:,0].reshape(v[:,0].size,1)
print(v1,v[:,[0]])

#to get column 1 of eigenvectors
v1= v[:,2]
print(v1)

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import neighbors, datasets

bunchobject = datasets.load_breast_cancer()
print( bunchobject.DESCR)
# print( bunchobject.data )
print(bunchobject.feature_names)
print(bunchobject.target_names)
print(bunchobject.data.shape)

column_index = [1]
print(bunchobject.feature_names[column_index])
feature_vals_in_column = bunchobject.data[:,column_index]
print(feature_vals_in_column,feature_vals_in_column.shape)
print( np.min(feature_vals_in_column), np.max(feature_vals_in_column))

row_index = [1]
print(bunchobject.feature_names)
record_vals_in_row = bunchobject.data[row_index,:]
print(record_vals_in_row)
print(bunchobject.target)

unique, counts = np.unique(bunchobject.target, return_counts = True)
print(type(np.unique(bunchobject.target, return_counts = True)))
for i in unique:
    print(i, bunchobject.target_names[i], counts[i])
    
    
from sklearn import datasets

bunchobject = datasets.load_breast_cancer()
print(bunchobject.DESCR)

