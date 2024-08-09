import numpy as np
from sklearn.datasets import load_iris
from sklearn import tree

iris = load_iris()
test_idx = [0,50,149]

#training Data
train_target = np.delete(iris.target, test_idx)
train_data= np.delete(iris.data, test_idx, axis=0)

#testing data
test_target = iris.target[test_idx]
test_data = iris.data[test_idx]


#Classifier training
clf = tree.DecisionTreeClassifier()
clf.fit(train_data,train_target)


#unknown data as a 1d array
l= [5.7,3.8,1.7,0.3]

#reshaping unknown data as a 2d array
l_reshaped = np.array(l).reshape(1, -1)

#prediction and verification through test data
print (test_target)
print (clf.predict(test_data))

#prediction through unknown data
print (clf.predict(l_reshaped))

# print (test_data[2],test_target[2])

# print (iris.data[18])
# print (iris.target[18])


