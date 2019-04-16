# Project Iris
# Vitalijs Smirnovs
# GMIT, Programming and Scripting
# Lecturer: Ian McLoughlin
# Student ID # g00317774

# import needed modules
import pandas as pd
from pandas.tools.plotting import scatter_matrix
import numpy as np
#import seaborn as sns
#sns.set(color_codes=True)
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# read in Iris data as a data frame
iris = pd.read_csv('Iris.csv')
#check the data read in correctly
iris.head()
iris.tail()
#info on dataset
iris.info()
#summary stats of numeric vars
iris.describe()

# plot data description stats
iris.plot(kind="box")
iris.hist()
iris.scatter()
# show plots
plt.show()