import numpy as np
a = np.array(([3,1], [1,2]))
b = np.array(([9,8]))
print(a,b)
x = np.linalg.solve(a, b)
print(x)