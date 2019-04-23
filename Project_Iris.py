# Project Iris
# Vitalijs Smirnovs
# GMIT, Programming and Scripting
# Lecturer: Ian McLoughlin
# Student ID # g00317774

# import needed modules
import pandas as pd
from pandas.tools.plotting import scatter_matrix
import numpy as np
import seaborn as sns
#sns.set(color_codes=True)
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC


# read in Iris data as a data frame
iris = pd.read_csv('Iris.csv')
#check the data read in correctly
#top 5 lines of data frame
iris.head()
#bottom 5 lines of dara frame
iris.tail()
#info on dataset
iris.info()
#summary stats of numeric vars
#to check for count (are there missing data?)
#mean, min, max, standard deviation (is mean representative?)
iris.describe()

#from: https://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342
iris.sample(5) #pops up 5 random rows from the data set 
iris.isnull().sum() #checks out how many null info are on the dataset

# plot data description stats
iris.plot(kind="box")
iris.hist()
scatter_matrix(iris)
sns.pairplot(iris, hue = 'species')
# show plots
plt.show()

## Classification algorithms
# from:https://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342
# Split-out validation dataset
array = iris.values
X = array[:,0:4]
Y = array[:,4]
validation_size = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)
# Test options and evaluation metric
seed = 7
scoring = 'accuracy'
# Spot Check Algorithms
models = []
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC()))
# evaluate each model in turn
results = []
names = []
for name, model in models:
 kfold = model_selection.KFold(n_splits=10, random_state=seed)
 cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
 results.append(cv_results)
 names.append(name)
 msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
 print(msg)
 # Make predictions on validation dataset

print("***KNN predict***************")
knn = KNeighborsClassifier()
knn.fit(X_train, Y_train)
predictions = knn.predict(X_validation)
print(accuracy_score(Y_validation, predictions))
print(confusion_matrix(Y_validation, predictions))
print(classification_report(Y_validation, predictions))

print("*******SVC predict******************************************")
svm = SVC()
svm.fit(X_train, Y_train)
predictions = svm.predict(X_validation)
print(accuracy_score(Y_validation, predictions))
print(confusion_matrix(Y_validation, predictions))
print(classification_report(Y_validation, predictions))