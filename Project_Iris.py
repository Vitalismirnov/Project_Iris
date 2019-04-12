# Project Iris
# Vitalijs Smirnovs
# GMIT, Programming and Scripting
# Lecturer: Ian McLoughlin
# Student ID # g00317774

# import needed modules
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# read in Iris data as a data frame
df = pd.read_csv('Iris.csv')
