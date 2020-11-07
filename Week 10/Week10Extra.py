#NORMALIZATION (rescaling from 0 to 1)
import numpy as np

data = np.array([101,6,2,4,1])
max_d = np.max(data)
min_d = np.min(data)
range_d = max_d - min_d

#scale the data to a range of 1
data_o = data/range_d
print(data_o)

#offset the data to start from 0 
data_o = data_o - min_d/range_d
print(data_o)


#LINEAR REGRESSION 
import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
from sklearn import linear_model


regr = linear_model.LinearRegression()

regr.fit




import numpy as np

x = np.array([[1,2],[3,4],[5,6]])
x=x.reshape(2,3)

print(x[:,[0,1]])
print(x)