import numpy as np
from sklearn import datasets
from sklearn.metrics import confusion_matrix


##################===Qn1 Answer===##################

def get_metrics(actual_targets, predicted_targets, labels):
    
    c_matrix = confusion_matrix(actual_targets, predicted_targets, labels)
    
    # your code here
    accuracy = round((c_matrix[0][0] + c_matrix[1][1]) / len(actual_targets),3)

    sensitivity = round(c_matrix[1][1] / (c_matrix[1][0] + c_matrix[1][1]),3)
    falsePositiveRate = round(c_matrix[0][1] / (c_matrix[0][0] + c_matrix[0][1]),3)
    output = {'confusion matrix': c_matrix, 'total records': len(actual_targets), 'accuracy': accuracy, 'sensitivity': sensitivity, 'false positive rate': falsePositiveRate }
    
    return output

##################===Qn2 Answer===##################

def five_number_summary(x):
    try:
        row, column = x.shape
    except:
        return None
    result = []
    for i in range(column):
        dic = {'minimum': np.min(x[:,i]), 
            'first quartile': np.percentile(x[:,i], 25),
            'median': np.median(x[:,i]),
            'third quartile': np.percentile(x[:,i],75),
            'maximum': np.max(x[:,i])}
        result.append(dic)
    return result

##################===Qn3 Answer===##################

def normalize_minmax(data):
    try:
        row, column = data.shape
    except:
        return None
    for i in range(column):
        maximum = np.max(data[:,i])
        minimum = np.min(data[:,i])
        data[:,i] = (data[:,i] - minimum) / (maximum - minimum)
    
    return data

##################===Qn4 Answer===##################

from sklearn.model_selection import train_test_split 
from sklearn import neighbors

def knn_classifier(bunchobject, feature_list, size, seed , k ): 
    data = bunchobject.data[:, feature_list]
    target = bunchobject.target
    
    data = normalize_minmax(data)
    
    data_train, data_test, target_train, target_test = train_test_split(data , target , test_size = size, random_state = seed )
    
    clf = neighbors.KNeighborsClassifier(k)
    clf.fit(data_train, target_train)
    target_predicted = clf.predict(data_test)

    results = get_metrics(target_test, target_predicted, [1,0])
    
    return results

##################===Qn5 Answer===##################

from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression

def linear_regression(bunchobject, x_index, y_index, size, seed):
    data = bunchobject.data
    x = data[:, np.newaxis, x_index]
    y = data[:, np.newaxis, y_index]
    
    x_train, x_test, y_train, y_test = train_test_split( x , y , test_size =size, random_state = seed )
    
    regr = LinearRegression()
    regr.fit(x_train, y_train)
    predicted_y = regr.predict(x_test)
    
    mse = mean_squared_error(y_test, predicted_y)
    
    var = r2_score(y_test, predicted_y)
    
    results = {
        'coefficients': regr.coef_,
        'intercept': regr.intercept_,
        'mean squared error': mse,
        'r2 score': var
    }
    
    return x_train, y_train, x_test, predicted_y, results

##################===Qn6 Answer===##################

from sklearn.preprocessing import PolynomialFeatures

def multiple_linear_regression(bunchobject, x_index, y_index, order, size, seed):
    data = bunchobject.data
    x = data[:, np.newaxis, x_index]
    y = data[:, np.newaxis, y_index]
    
    poly = PolynomialFeatures(order,include_bias=False)
    c_data = poly.fit_transform(x)
    
    x_transformed_train, x_transformed_test, y_train, y_test = train_test_split(c_data,y,test_size=size, random_state=seed)
    
    regr = LinearRegression()
    regr.fit(x_transformed_train, y_train)
    y_pred = regr.predict(x_transformed_test)
    
    mse = mean_squared_error(y_test, y_pred)
    var = r2_score(y_test, y_pred)
    
    results= {
        'coefficients': regr.coef_,
        'intercept': regr.intercept_,
        'mean squared error': mse,
        'r2 score': var
    }
    x_transformed_train = x_transformed_train[:,0:1]
    y_train = y_train[:,0:1]
    x_transformed_test = x_transformed_test[:,0:1]
    y_pred = y_pred[:,0:1]
    
    return x_transformed_train , y_train, x_transformed_test, y_pred, results

#######################===Qn7 Answer===#######################
def knn_classifier_full(bunchobject, feature_list, size, seed):
    data = bunchobject.data[:, feature_list]
    target = bunchobject.target
    data = normalize_minmax(data)
    
    data_train, data_part2, target_train, target_part2 = train_test_split(data, target, test_size=size, random_state = seed)
    data_validation, data_test, target_validation, target_test = train_test_split(data_part2, target_part2, test_size = 0.5, random_state = seed)
    
    updated_k_value = 1
    updated_accuracy = 0
    updated_predicted_target = 0
    
    for k in range(1,20):
        classifier = neighbors.KNeighborsClassifier(k)
        classifier.fit(data_train, target_train)
        
        predicted_target = classifier.predict(data_validation)
        results = get_metrics(target_validation, predicted_target, [1,0])
        accuracy = results['accuracy']

        if (accuracy > updated_accuracy):
            updated_k_value = k
            updated_accuracy = accuracy
            updated_predicted_target = predicted_target

    classifier = neighbors.KNeighborsClassifier(updated_k_value)
    classifier.fit(data_train, target_train)
    new_predicted_target = classifier.predict(data_test)

    compared_test_set = get_metrics(target_test, new_predicted_target, [1,0])
    compared_validation_set = get_metrics(target_validation, updated_predicted_target, [1,0])
    
    results = {
        'best k': updated_k_value,
        'validation set': compared_validation_set,
        'test set': compared_test_set
    }
    return results