import numpy as np ##csQ1
from sklearn.metrics import confusion_matrix

def get_metrics(actual_targets, predicted_targets, labels):
    output = {}
    
    c_matrix = confusion_matrix(actual_targets, predicted_targets, labels)
    
    # your code here
    output['confusion matrix'] = c_matrix
    output['total records'] = round(len(actual_targets),3)
    output['accuracy'] = round((c_matrix[0][0] + c_matrix[1][1]) / output['total records'],3)
    output['sensitivity'] = round((c_matrix[1][1]/(c_matrix[1][0] +c_matrix[1][1])),3)
    output['false positive rate'] = round((c_matrix[0][1]/(c_matrix[0][0] + c_matrix[0][1])),3)
    
    
    print(output)
    return output
 
import numpy as np #csQ2
def five_number_summary(x):
    five_num ={}
    final = []
    print(x.shape)
    if len(x.shape) == 2:
        _,col = x.shape
        for i in range(col):
            five_num['minimum'] = np.min(x[:,[i]])
            five_num['first quartile'] = np.percentile(x[:,[i]],25)
            five_num['median'] = np.median(x[:,[i]])
            five_num['third quartile'] = np.percentile(x[:,[i]],75)
            five_num['maximum'] = np.max(x[:,[i]])
            final.append(five_num)
            five_num = {}
            print(final)
        return final
    else:
        return None
    

import numpy as np #csQ3
def normalize_minmax(data):
    if len(data.shape) == 2:
        _,col = data.shape
        for i in range(col):
            maxi = np.max(data[:,[i]])
            mini = np.min(data[:,[i]])
            range_max_min = maxi - mini
            data[:,[i]] = (data[:,[i]] - mini) / range_max_min
        return data
    else:
        return None
    

def knn_classifier(bunchobject, feature_list, size, seed , k ): 
    data = bunchobject.data[:,feature_list] #get x coordinates
    target = bunchobject.target #get y coordinates
    
    data = normalize_minmax(data)
    
    data_train, data_test, target_train, target_test = train_test_split(data,target,test_size = size, random_state = seed) #x_fake,x_real,y_fake,y_real
    #compares data with target data
    classifier = neighbors.KNeighborsClassifier(k)
    classifier.fit(data_train,target_train)
    target_predicted = classifier.predict(data_test)
    
    results = get_metrics(target_test,target_predicted,[1,0])
    
    return results
    

import numpy as np #csQ5 STEP BY STEP!!
from sklearn import linear_model 
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def linear_regression(bunchobject, x_index, y_index, size, seed):
    final = {}
    data = bunchobject.data #getting the data needed for LR
    x_points = data[:,[x_index]]#x points
    y_points = data[:,[y_index]]#y points
    
    x_train,x_test,y_train,y_test = train_test_split(x_points,y_points,test_size=size,random_state=seed)#get training data from real data points
    
    regr = LinearRegression()
    regr.fit(x_train,y_train)
    print(regr.fit(x_train,y_train),'asddsa')
    y_predicted = regr.predict(x_test) #get predicted y points from x real data
    
    mse = mean_squared_error(y_test,y_predicted)
    
    var = r2_score(y_test,y_predicted) #variation?
    
    final['coefficients'] = regr.coef_
    final['intercept'] = regr.intercept_
    final['mean squared error'] = mse
    final['r2 score'] = var
    
    return x_train,y_train, x_test,y_predicted,final
    


import numpy as np #csQ6
from sklearn import linear_model 
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

def multiple_linear_regression(bunchobject, x_index, y_index, order, size, seed):
    final = {}
    data = bunchobject.data
    x_points = data[:,[x_index]]
    y_points = data[:,[y_index]]
    
    poly = PolynomialFeatures(order,include_bias = False) #polynomial function based on order https://stackoverflow.com/questions/51906274/cannot-understand-with-sklearns-polynomialfeatures
    new_x_points = poly.fit_transform(x_points) #transforms x array into polynomial function of new order
    
    x_train,x_test,y_train,y_test = train_test_split(new_x_points,y_points,test_size = size, random_state=seed)
    
    regr = LinearRegression()
    regr.fit(x_train,y_train)
    y_predicted = regr.predict(x_test)
    
    mse = mean_squared_error(y_test,y_predicted)
    var = r2_score(y_test,y_predicted)
    
    final['coefficients'] = regr.coef_
    final['intercept'] = regr.intercept_
    final['mean squared error'] = mse
    final['r2 score'] = var
    
    print(x_train)
    print(y_train)
    print(x_test)
    print(y_predicted)
    
    x_train = x_train[:,[0]]
    y_train = y_train[:,[0]]
    x_test = x_test[:,[0]]
    y_predicted = y_predicted[:,[0]]
    
    
    return x_train,y_train,x_test,y_predicted,final